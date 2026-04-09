"""
Deterministic prefilter for findings before R2 critic.
Removes structurally invalid findings (no evidence, no page, exact duplicates)
to reduce the LLM critic's workload. Run BEFORE build_critic_payload.py.

Usage:
    python prefilter_findings.py <project_path>

Example:
    python prefilter_findings.py projects/EOM/133_23-ГК-ГРЩ
"""

import sys, os, io, json, re, argparse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

parser = argparse.ArgumentParser(description='Deterministic prefilter for partial findings')
parser.add_argument('project_path', help='Path to project folder (contains _output/)')
args = parser.parse_args()

project_path = args.project_path.rstrip('/\\')
output_dir = os.path.join(project_path, '_output')

# === Step 1: Read all partial_*.json ===
partials = {}
for fname in sorted(os.listdir(output_dir)):
    if fname.startswith('partial_') and fname.endswith('.json'):
        with open(os.path.join(output_dir, fname), 'r', encoding='utf-8') as f:
            data = json.load(f)
        partials[fname] = data

total_before = sum(len(p.get('findings', [])) for p in partials.values())
rejected = []

# === Step 2: Filter findings in each partial ===
for fname, data in partials.items():
    agent = data.get('agent', fname.replace('partial_', '').replace('.json', ''))
    original = data.get('findings', [])
    kept = []

    for f in original:
        tid = f.get('temp_id', '?')
        reason = None

        # 2a. No evidence
        evidence = f.get('evidence', [])
        if not evidence:
            reason = 'no_evidence'

        # 2b. No page reference
        elif f.get('page') is None:
            reason = 'no_page'

        # 2c. Normalize evidence.source whitespace
        if not reason:
            for e in evidence:
                src = e.get('source', '')
                if isinstance(src, str):
                    e['source'] = re.sub(r'\s+', ' ', src).strip()

        if reason:
            rejected.append({
                'finding_id': tid,
                'agent': agent,
                'reason': reason,
                'title': f.get('title', '')[:100]
            })
        else:
            kept.append(f)

    data['findings'] = kept

# === Step 3: Remove exact duplicates across agents ===
seen_exact = set()
for fname, data in partials.items():
    agent = data.get('agent', '')
    original = data.get('findings', [])
    kept = []

    for f in original:
        # Exact duplicate key: page + title + norm_ref
        dup_key = f'{f.get("page", "?")}|{f.get("title", "")}|{f.get("norm_ref", "")}'
        if dup_key in seen_exact:
            rejected.append({
                'finding_id': f.get('temp_id', '?'),
                'agent': agent,
                'reason': 'exact_duplicate',
                'title': f.get('title', '')[:100]
            })
        else:
            seen_exact.add(dup_key)
            kept.append(f)

    data['findings'] = kept

# === Step 4: Write back filtered partials ===
total_after = sum(len(p.get('findings', [])) for p in partials.values())

for fname, data in partials.items():
    with open(os.path.join(output_dir, fname), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# === Step 5: Write stats ===
stats = {
    'total_before': total_before,
    'total_after': total_after,
    'filtered_out': len(rejected),
    'by_reason': {}
}
for r in rejected:
    reason = r['reason']
    stats['by_reason'][reason] = stats['by_reason'].get(reason, 0) + 1

stats_path = os.path.join(output_dir, 'prefiltered_stats.json')
with open(stats_path, 'w', encoding='utf-8') as f:
    json.dump({'stats': stats, 'rejected': rejected}, f, ensure_ascii=False, indent=2)

print(f'Done!')
print(f'  Before: {total_before} findings')
print(f'  After:  {total_after} findings')
print(f'  Filtered: {len(rejected)} ({", ".join(f"{k}: {v}" for k, v in stats["by_reason"].items())})')
