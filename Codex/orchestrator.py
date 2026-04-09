#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


TEMPLATE_ROOT = Path(__file__).resolve().parent
SOURCE_REPO_ROOT = Path(os.environ.get("MAM_SOURCE_REPO_ROOT", str(TEMPLATE_ROOT.parent))).resolve()
DEFAULT_RUNTIME_ROOT = Path(os.environ.get("MAM_CODEX_RUNTIME", r"D:\MAM_CODEX_RUNTIME")).resolve()
WORK_ROOT = TEMPLATE_ROOT.resolve()
PYTHON = Path(sys.executable).resolve()

GROUP_ORDER = [
    "prepare",
    "r1",
    "norms_subset",
    "norm_finding_checks",
    "critic_payload",
    "critic",
    "synthesize",
    "optimization",
    "optimization_review",
    "report",
]


@dataclass(frozen=True)
class AgentConfig:
    name: str
    prompt_file: str
    pages: tuple[int, ...] = ()
    full_document: bool = False


EOM_ACTIVE_AGENTS: tuple[AgentConfig, ...] = (
    AgentConfig("consistency", "R1_consistency.md", full_document=True),
    AgentConfig("tables", "R1_tables.md", pages=(5, 6, 7, 8)),
    AgentConfig("cables", "R1_cables.md", pages=(5, 6, 7, 8, 9)),
    AgentConfig("fire_safety", "R1_fire_safety.md", pages=(5, 6, 7, 8, 9, 12, 13)),
    AgentConfig("cable_routes", "R1_cable_routes.md", pages=(5, 6, 12, 13, 14, 16, 17, 18, 19)),
    AgentConfig("metering", "R1_metering.md", pages=(5, 6, 7, 14, 15)),
    AgentConfig("power_equipment", "R1_power_equipment.md", pages=(5, 6, 10, 14, 15)),
    AgentConfig("norms", "R1_norms.md", full_document=True),
)

EOM_SKIPPED_AGENTS = ["lighting", "automation", "outdoor_install", "grounding"]


def log(message: str) -> None:
    print(message, flush=True)


def set_work_root(root: Path) -> None:
    global WORK_ROOT
    WORK_ROOT = root.resolve()


def ensure_within(path: Path, root: Path) -> None:
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Path {path} is outside allowed root {root}")


def json_dump(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_rel(path: Path, base: Path | None = None) -> str:
    if base is None:
        base = WORK_ROOT
    return path.resolve().relative_to(base.resolve()).as_posix()


def sync_runtime_root(runtime_root: Path) -> None:
    runtime_root = runtime_root.resolve()
    if runtime_root == TEMPLATE_ROOT.resolve():
        return

    runtime_root.mkdir(parents=True, exist_ok=True)
    (runtime_root / "projects").mkdir(parents=True, exist_ok=True)

    for dirname in ("Audits", "Prompts_EN", "norms"):
        src = TEMPLATE_ROOT / dirname
        dst = runtime_root / dirname
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    for filename in ("orchestrator.py", "README.md", ".gitignore"):
        shutil.copy2(TEMPLATE_ROOT / filename, runtime_root / filename)

    meta = {
        "template_root": str(TEMPLATE_ROOT),
        "runtime_root": str(runtime_root),
        "source_repo_root": str(SOURCE_REPO_ROOT),
        "synced_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    json_dump(runtime_root / ".runtime_meta.json", meta)


def resolve_source_project(user_value: str) -> Path:
    raw = Path(user_value)
    candidates: list[Path] = []
    if raw.is_absolute():
        candidates.append(raw)
    else:
        candidates.append(SOURCE_REPO_ROOT / raw)
        candidates.append(WORK_ROOT / raw)

    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()

    raise FileNotFoundError(f"Project path not found: {user_value}")


def mirror_project_path(source_project: Path) -> Path:
    source_project = source_project.resolve()
    if source_project.is_relative_to(WORK_ROOT):
        return source_project
    rel = source_project.relative_to(SOURCE_REPO_ROOT)
    if not rel.parts or rel.parts[0] != "projects":
        raise ValueError("Only projects under root projects/ are supported for mirroring")
    return (WORK_ROOT / rel).resolve()


def copy_project_snapshot(source_project: Path, mirror_project: Path, refresh: bool) -> None:
    if source_project.resolve().is_relative_to(WORK_ROOT.resolve()):
        return

    ensure_within(mirror_project, WORK_ROOT / "projects")

    if mirror_project.exists() and not refresh:
        log(f"[prepare] Reusing existing Codex mirror: {mirror_project}")
        return

    if mirror_project.exists():
        shutil.rmtree(mirror_project)

    log(f"[prepare] Copying source project into Codex mirror: {mirror_project}")

    def ignore(dirpath: str, names: list[str]) -> set[str]:
        rel = Path(dirpath).resolve().relative_to(source_project.resolve())
        ignored: set[str] = set()
        if rel == Path("."):
            for name in ("blocks", "subagent_results", "agent_teams_results"):
                if name in names:
                    ignored.add(name)
        if rel == Path("_output"):
            for name in ("blocks", "audit_trail", "slices"):
                if name in names:
                    ignored.add(name)
        return ignored

    shutil.copytree(source_project, mirror_project, ignore=ignore)

    meta = {
        "source_project": str(source_project),
        "mirror_project": str(mirror_project),
        "synced_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    json_dump(mirror_project / "_codex_mirror.json", meta)


def ensure_document_enriched(project_path: Path) -> Path:
    output_dir = project_path / "_output"
    output_dir.mkdir(parents=True, exist_ok=True)
    enriched = output_dir / "document_enriched.md"
    if enriched.exists():
        return enriched

    info = read_json(project_path / "project_info.json")
    md_files = []
    if isinstance(info.get("md_files"), list):
        md_files = info["md_files"]
    elif isinstance(info.get("md_file"), str):
        md_files = [info["md_file"]]

    if not md_files:
        raise FileNotFoundError("project_info.json does not contain md_file or md_files")

    parts: list[str] = []
    for name in md_files:
        source = project_path / name
        if not source.exists():
            raise FileNotFoundError(f"Missing markdown source: {source}")
        parts.append(source.read_text(encoding="utf-8"))

    enriched.write_text("\n\n".join(parts), encoding="utf-8")
    log(f"[prepare] Built fallback document_enriched.md from source markdown files")
    return enriched


def load_project_section(project_path: Path) -> str:
    info = read_json(project_path / "project_info.json")
    section = info.get("section")
    if not isinstance(section, str) or not section:
        raise ValueError("project_info.json does not contain valid section")
    return section


def get_profile(section: str) -> tuple[tuple[AgentConfig, ...], list[str]]:
    if section == "EOM":
        return EOM_ACTIVE_AGENTS, EOM_SKIPPED_AGENTS
    raise NotImplementedError(f"Section {section} is not supported in Codex runtime yet")


def parse_pages(doc_text: str) -> dict[int, str]:
    pages: dict[int, str] = {}
    parts = re.split(r"(##\s+СТРАНИЦА\s+\d+)", doc_text)
    current_page = 0
    for index, part in enumerate(parts):
        match = re.match(r"##\s+СТРАНИЦА\s+(\d+)", part)
        if match:
            current_page = int(match.group(1))
            if index + 1 < len(parts):
                pages[current_page] = part + parts[index + 1]
        elif current_page == 0 and index == 0:
            pages[0] = part
    return pages


def build_slice(pages: dict[int, str], page_list: Iterable[int], full_document_text: str | None = None) -> str:
    if full_document_text is not None:
        return full_document_text
    header = pages.get(0, "")
    chunks = [header]
    for page_no in sorted(page_list):
        chunk = pages.get(page_no)
        if chunk:
            chunks.append(chunk)
    return "".join(chunks)


def generate_slices(project_path: Path, section: str) -> dict:
    agents, skipped_agents = get_profile(section)
    output_dir = project_path / "_output"
    slices_dir = output_dir / "slices"
    slices_dir.mkdir(parents=True, exist_ok=True)

    doc_path = ensure_document_enriched(project_path)
    doc_text = doc_path.read_text(encoding="utf-8")
    pages = parse_pages(doc_text)

    manifest = {
        "section": section,
        "generated_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source_document": normalize_rel(doc_path),
        "active_agents": {},
        "skipped_agents": skipped_agents,
        "coverage_warnings": [],
    }

    for agent in agents:
        slice_text = build_slice(
            pages,
            agent.pages,
            full_document_text=doc_text if agent.full_document else None,
        )
        slice_path = slices_dir / f"slice_{agent.name}.md"
        slice_path.write_text(slice_text, encoding="utf-8")
        manifest["active_agents"][agent.name] = {
            "pages": list(agent.pages),
            "full_document": agent.full_document,
            "slice_file": slice_path.name,
            "chars": len(slice_text),
        }

    json_dump(slices_dir / "slice_manifest.json", manifest)
    return manifest


def build_r1_prompt(project_rel: str, section: str, agent: AgentConfig) -> str:
    common = "Prompts_EN/common/00_base.md"
    ownership = f"Prompts_EN/{section}/OWNERSHIP_MATRIX_{section}.md"
    task = f"Prompts_EN/{section}/{agent.prompt_file}"
    slice_file = f"{project_rel}/_output/slices/slice_{agent.name}.md"
    output_file = f"{project_rel}/_output/partial_{agent.name}.json"

    numbered_files = [common, ownership]
    if agent.name == "norms":
        numbered_files.extend(["norms/norms_db.json", "norms/norms_paragraphs.json"])
    numbered_files.extend([slice_file, task])

    files_block = "\n".join(f"{idx}. {value}" for idx, value in enumerate(numbered_files, start=1))

    return textwrap.dedent(
        f"""\
        You are running inside an isolated Codex clone of the audit project.

        Claude-specific wording such as "use the Write tool" means: create or overwrite the target file directly in this workspace.

        Read these files in order:
        {files_block}

        Then perform the `{agent.name}` Round 1 audit.

        Hard rules:
        - Use only the files listed above as inputs.
        - Write the final JSON result to `{output_file}`.
        - Do not modify any other file.
        - Overwrite the output file completely with valid UTF-8 JSON.
        - If you need scratch work, keep it in reasoning only; do not create temp files.

        After writing the file, reply with a one-line status summary.
        """
    )


def build_critic_prompt(project_rel: str, section: str) -> str:
    files = [
        "Prompts_EN/common/00_base.md",
        "Prompts_EN/common/R2_critic.md",
        f"{project_rel}/_output/critic_payload.json",
        f"{project_rel}/_output/document_enriched.md",
        f"{project_rel}/_output/norms_subset.json",
    ]
    files_block = "\n".join(f"{idx}. {value}" for idx, value in enumerate(files, start=1))
    output_file = f"{project_rel}/_output/review.json"

    return textwrap.dedent(
        f"""\
        You are the isolated Codex critic for section `{section}`.

        Claude-specific wording such as "use the Write tool" means: create or overwrite the target file directly in this workspace.

        Read these files in order:
        {files_block}

        Run the full Round 2 critique and write the result to `{output_file}`.

        Hard rules:
        - Use only the files listed above.
        - Do not modify any file except `{output_file}`.
        - Output must be valid UTF-8 JSON.

        After writing the file, reply with a one-line status summary.
        """
    )


def build_optimizer_prompt(project_rel: str) -> str:
    files = [
        "Prompts_EN/common/R4_optimizer.md",
        f"{project_rel}/_output/findings.json",
        f"{project_rel}/_output/document_enriched.md",
        "norms/vendor_list.json",
    ]
    files_block = "\n".join(f"{idx}. {value}" for idx, value in enumerate(files, start=1))
    output_file = f"{project_rel}/_output/optimization.json"

    return textwrap.dedent(
        f"""\
        You are running the optimization stage in the isolated Codex workspace.

        Claude-specific wording such as "use the Write tool" means: create or overwrite the target file directly in this workspace.

        Read these files in order:
        {files_block}

        Write the optimizer result to `{output_file}`.
        Do not modify any other file.
        After writing the file, reply with a one-line status summary.
        """
    )


def build_optimizer_critic_prompt(project_rel: str) -> str:
    files = [
        "Prompts_EN/common/R4b_optimizer_critic.md",
        f"{project_rel}/_output/optimization.json",
        f"{project_rel}/_output/findings.json",
        f"{project_rel}/_output/document_enriched.md",
        "norms/vendor_list.json",
    ]
    files_block = "\n".join(f"{idx}. {value}" for idx, value in enumerate(files, start=1))
    output_file = f"{project_rel}/_output/optimization_review.json"

    return textwrap.dedent(
        f"""\
        You are the optimization critic in the isolated Codex workspace.

        Claude-specific wording such as "use the Write tool" means: create or overwrite the target file directly in this workspace.

        Read these files in order:
        {files_block}

        Write the critic result to `{output_file}`.
        Do not modify any other file.
        After writing the file, reply with a one-line status summary.
        """
    )


def run_subprocess(cmd: list[str], cwd: Path, timeout_sec: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        capture_output=True,
        timeout=timeout_sec,
        check=False,
    )


def run_python_stage(script_name: str, project_rel: str, timeout_sec: int) -> None:
    cmd = [str(PYTHON), f"Audits/{script_name}", project_rel]
    result = run_subprocess(cmd, WORK_ROOT, timeout_sec)
    if result.returncode != 0:
        raise RuntimeError(
            f"Python stage {script_name} failed:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )
    summary = result.stdout.strip() or f"{script_name} completed"
    log(f"[python] {script_name}: {summary}")


def write_prompt_file(project_path: Path, name: str, prompt_text: str) -> Path:
    prompt_dir = project_path / "_output" / "codex_prompts"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    prompt_file = prompt_dir / f"{name}.md"
    prompt_file.write_text(prompt_text, encoding="utf-8")
    return prompt_file


def run_codex_task(
    *,
    task_name: str,
    prompt_text: str,
    project_rel: str,
    model: str,
    reasoning_effort: str,
    timeout_sec: int,
    target_output_rel: str,
) -> dict:
    project_path = WORK_ROOT / project_rel
    log_dir = project_path / "_output" / "codex_logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    target_output = project_path / target_output_rel
    if target_output.exists():
        target_output.unlink()

    prompt_file = write_prompt_file(project_path, task_name, prompt_text)
    stdout_file = log_dir / f"{task_name}.stdout.log"
    stderr_file = log_dir / f"{task_name}.stderr.log"
    last_message_file = log_dir / f"{task_name}.last_message.txt"

    cmd = [
        "codex",
        "exec",
        "--full-auto",
        "--skip-git-repo-check",
        "--color",
        "never",
        "--model",
        model,
        "-c",
        f"reasoning_effort=\"{reasoning_effort}\"",
        "-C",
        str(WORK_ROOT),
        "--output-last-message",
        str(last_message_file),
        "-",
    ]

    result = subprocess.run(
        cmd,
        cwd=WORK_ROOT,
        text=True,
        encoding="utf-8",
        input=prompt_text,
        capture_output=True,
        timeout=timeout_sec,
        check=False,
    )

    stdout_file.write_text(result.stdout or "", encoding="utf-8")
    stderr_file.write_text(result.stderr or "", encoding="utf-8")

    return {
        "task_name": task_name,
        "prompt_file": normalize_rel(prompt_file),
        "stdout_file": normalize_rel(stdout_file),
        "stderr_file": normalize_rel(stderr_file),
        "last_message_file": normalize_rel(last_message_file),
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "target_output": normalize_rel(target_output),
    }


def check_output_exists(project_rel: str, output_rel: str) -> bool:
    return (WORK_ROOT / project_rel / output_rel).exists()


def run_r1_group(project_rel: str, section: str, model: str, reasoning_effort: str, timeout_sec: int) -> None:
    agents, _ = get_profile(section)
    jobs = []
    for agent in agents:
        prompt_text = build_r1_prompt(project_rel, section, agent)
        jobs.append((agent, prompt_text))

    max_workers = min(4, len(jobs))
    log(f"[r1] Launching {len(jobs)} Codex agents with up to {max_workers} concurrent workers")

    failures: list[str] = []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        future_map = {
            pool.submit(
                run_codex_task,
                task_name=f"r1_{agent.name}",
                prompt_text=prompt_text,
                project_rel=project_rel,
                model=model,
                reasoning_effort=reasoning_effort,
                timeout_sec=timeout_sec,
                target_output_rel=f"_output/partial_{agent.name}.json",
            ): agent
            for agent, prompt_text in jobs
        }

        for future in as_completed(future_map):
            agent = future_map[future]
            try:
                result = future.result()
            except Exception as exc:  # pragma: no cover - defensive path
                failures.append(f"{agent.name}: {exc}")
                continue

            output_rel = f"_output/partial_{agent.name}.json"
            output_exists = check_output_exists(project_rel, output_rel)
            status = "OK" if result["returncode"] == 0 and output_exists else "FAILED"
            log(
                f"[r1] {agent.name}: {status}; output={output_exists}; "
                f"prompt={result['prompt_file']}; log={result['last_message_file']}"
            )

            if status != "OK":
                failures.append(
                    f"{agent.name}: rc={result['returncode']}\nSTDOUT:\n{result['stdout']}\nSTDERR:\n{result['stderr']}"
                )

    if failures:
        raise RuntimeError("R1 group failed:\n\n" + "\n\n".join(failures))


def run_critic_group(project_rel: str, section: str, model: str, reasoning_effort: str, timeout_sec: int) -> None:
    prompt_text = build_critic_prompt(project_rel, section)
    result = run_codex_task(
        task_name="r2_critic",
        prompt_text=prompt_text,
        project_rel=project_rel,
        model=model,
        reasoning_effort=reasoning_effort,
        timeout_sec=timeout_sec,
        target_output_rel="_output/review.json",
    )
    output_exists = check_output_exists(project_rel, "_output/review.json")
    if result["returncode"] != 0 or not output_exists:
        raise RuntimeError(
            "Critic stage failed:\n"
            f"STDOUT:\n{result['stdout']}\nSTDERR:\n{result['stderr']}"
        )
    log(f"[critic] OK; output={output_exists}; log={result['last_message_file']}")


def run_optimizer_group(project_rel: str, model: str, reasoning_effort: str, timeout_sec: int) -> None:
    prompt_text = build_optimizer_prompt(project_rel)
    result = run_codex_task(
        task_name="r4_optimizer",
        prompt_text=prompt_text,
        project_rel=project_rel,
        model=model,
        reasoning_effort=reasoning_effort,
        timeout_sec=timeout_sec,
        target_output_rel="_output/optimization.json",
    )
    output_exists = check_output_exists(project_rel, "_output/optimization.json")
    if result["returncode"] != 0 or not output_exists:
        raise RuntimeError(
            "Optimization stage failed:\n"
            f"STDOUT:\n{result['stdout']}\nSTDERR:\n{result['stderr']}"
        )
    log(f"[optimization] OK; output={output_exists}; log={result['last_message_file']}")


def run_optimizer_critic_group(project_rel: str, model: str, reasoning_effort: str, timeout_sec: int) -> None:
    prompt_text = build_optimizer_critic_prompt(project_rel)
    result = run_codex_task(
        task_name="r4b_optimizer_critic",
        prompt_text=prompt_text,
        project_rel=project_rel,
        model=model,
        reasoning_effort=reasoning_effort,
        timeout_sec=timeout_sec,
        target_output_rel="_output/optimization_review.json",
    )
    output_exists = check_output_exists(project_rel, "_output/optimization_review.json")
    if result["returncode"] != 0 or not output_exists:
        raise RuntimeError(
            "Optimization critic stage failed:\n"
            f"STDOUT:\n{result['stdout']}\nSTDERR:\n{result['stderr']}"
        )
    log(f"[optimization_review] OK; output={output_exists}; log={result['last_message_file']}")


def run_prepare_group(source_project: Path, mirror_project: Path, refresh: bool) -> dict:
    copy_project_snapshot(source_project, mirror_project, refresh)
    section = load_project_section(mirror_project)
    doc_path = ensure_document_enriched(mirror_project)
    manifest = generate_slices(mirror_project, section)
    log(f"[prepare] Working document: {doc_path}")
    log(f"[prepare] Generated slices for agents: {', '.join(manifest['active_agents'].keys())}")
    return manifest


def group_slice(from_group: str, to_group: str) -> list[str]:
    try:
        start = GROUP_ORDER.index(from_group)
        end = GROUP_ORDER.index(to_group)
    except ValueError as exc:
        raise ValueError(f"Unknown group: {exc}") from exc
    if start > end:
        raise ValueError("--from-group must be earlier than or equal to --to-group")
    return GROUP_ORDER[start : end + 1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Run isolated Codex audit pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run Codex pipeline groups")
    run_parser.add_argument("--project", required=True, help="Root project path, e.g. projects/EOM/133_23-ГК-ГРЩ")
    run_parser.add_argument("--model", default="gpt-5.4-mini", help="Codex model for LLM stages")
    run_parser.add_argument(
        "--runtime-root",
        default=str(DEFAULT_RUNTIME_ROOT),
        help="ASCII-only runtime workspace for Codex model stages",
    )
    run_parser.add_argument(
        "--reasoning-effort",
        default="low",
        choices=["low", "medium", "high", "xhigh"],
        help="Reasoning effort for Codex model stages",
    )
    run_parser.add_argument("--from-group", default="prepare", choices=GROUP_ORDER)
    run_parser.add_argument("--to-group", default="optimization_review", choices=GROUP_ORDER)
    run_parser.add_argument("--refresh", action="store_true", help="Re-copy the source project into Codex mirror")
    run_parser.add_argument("--timeout-sec", type=int, default=1800, help="Timeout per model stage")

    args = parser.parse_args()

    if args.command != "run":
        parser.error("Unsupported command")

    runtime_root = Path(args.runtime_root).resolve()
    sync_runtime_root(runtime_root)
    set_work_root(runtime_root)

    source_project = resolve_source_project(args.project)
    mirror_project = mirror_project_path(source_project)
    project_rel = normalize_rel(mirror_project)

    stages = group_slice(args.from_group, args.to_group)
    log(f"[run] Source project: {source_project}")
    log(f"[run] Runtime root:   {runtime_root}")
    log(f"[run] Codex mirror:   {mirror_project}")
    log(f"[run] Stages:        {' -> '.join(stages)}")
    log(f"[run] Model:         {args.model}")
    log(f"[run] Reasoning:     {args.reasoning_effort}")

    if "prepare" in stages or not mirror_project.exists():
        run_prepare_group(source_project, mirror_project, args.refresh)

    section = load_project_section(mirror_project)

    for stage in stages:
        if stage == "prepare":
            continue
        if stage == "r1":
            run_r1_group(project_rel, section, args.model, args.reasoning_effort, args.timeout_sec)
        elif stage == "norms_subset":
            run_python_stage("build_norms_subset.py", project_rel, args.timeout_sec)
        elif stage == "norm_finding_checks":
            run_python_stage("build_norm_finding_checks.py", project_rel, args.timeout_sec)
        elif stage == "critic_payload":
            run_python_stage("build_critic_payload.py", project_rel, args.timeout_sec)
        elif stage == "critic":
            run_critic_group(project_rel, section, args.model, args.reasoning_effort, args.timeout_sec)
        elif stage == "synthesize":
            run_python_stage("synthesize.py", project_rel, args.timeout_sec)
        elif stage == "optimization":
            run_optimizer_group(project_rel, args.model, args.reasoning_effort, args.timeout_sec)
        elif stage == "optimization_review":
            run_optimizer_critic_group(project_rel, args.model, args.reasoning_effort, args.timeout_sec)
        elif stage == "report":
            run_python_stage("gen_report.py", project_rel, args.timeout_sec)
        else:  # pragma: no cover - defensive path
            raise ValueError(f"Unsupported stage: {stage}")

    log("[run] Completed successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
