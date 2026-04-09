"""
Build critic_payload.json — compact findings payload for the R2 critic.
Extracts only verification-relevant fields from partial_*.json, reducing token cost by ~50-66%.

Usage:
    python build_critic_payload.py <project_path>

Example:
    python build_critic_payload.py projects/EOM/133_23-ГК-ГРЩ
"""

import sys, os, io, json, argparse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

parser = argparse.ArgumentParser(description='Build compact critic payload from partial findings')
parser.add_argument('project_path', help='Path to project folder (contains _output/)')
args = parser.parse_args()

project_path = args.project_path.rstrip('/\\')
output_dir = os.path.join(project_path, '_output')

# Fields to extract per finding (verification-relevant only)
KEEP_FIELDS = {
    'temp_id', 'category', 'title', 'page', 'sheet',
    'evidence', 'norm_ref', 'norm_quote', 'norm_confidence', 'confidence',
    'norm_role', 'norm_source', 'needs_norm_verification',
    'requires_exact_quote', 'claim_basis'
}

CLAIM_MAX_LEN = 200  # truncate description to this length for 'claim'
QUOTE_MAX_LEN = 200

AGENT_DEFAULTS = {
    'automation': {'claim_basis': 'mixed', 'norm_role': 'supporting', 'requires_exact_quote': False},
    'cable_routes': {'claim_basis': 'mixed', 'norm_role': 'supporting', 'requires_exact_quote': False},
    'cables': {'claim_basis': 'calculation', 'norm_role': 'supporting', 'requires_exact_quote': False},
    'consistency': {'claim_basis': 'drawing_consistency', 'norm_role': 'none', 'requires_exact_quote': False},
    'fire_safety': {'claim_basis': 'normative', 'norm_role': 'core', 'requires_exact_quote': True},
    'grounding': {'claim_basis': 'mixed', 'norm_role': 'core', 'requires_exact_quote': True},
    'lighting': {'claim_basis': 'mixed', 'norm_role': 'supporting', 'requires_exact_quote': False},
    'metering': {'claim_basis': 'mixed', 'norm_role': 'supporting', 'requires_exact_quote': False},
    'norms': {'claim_basis': 'normative', 'norm_role': 'core', 'requires_exact_quote': True},
    'outdoor_install': {'claim_basis': 'mixed', 'norm_role': 'supporting', 'requires_exact_quote': False},
    'power_equipment': {'claim_basis': 'mixed', 'norm_role': 'supporting', 'requires_exact_quote': False},
    'tables': {'claim_basis': 'calculation', 'norm_role': 'none', 'requires_exact_quote': False},
}


def load_norm_checks(output_dir):
    path = os.path.join(output_dir, 'norm_finding_checks.json')
    if not os.path.exists(path):
        return {}

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    checks = {}
    for item in data.get('checks', []):
        finding_id = item.get('finding_id')
        if finding_id:
            checks[finding_id] = item
    return checks


def apply_agent_defaults(compact, finding, agent):
    defaults = AGENT_DEFAULTS.get(agent, {})
    has_norm_ref = bool(finding.get('norm_ref'))
    has_norm_quote = bool(finding.get('norm_quote'))

    compact.setdefault('norm_role', defaults.get('norm_role', 'supporting' if has_norm_ref else 'none'))
    compact.setdefault(
        'norm_source',
        'vault_exact' if has_norm_quote else ('agent_memory' if has_norm_ref else 'none')
    )
    compact.setdefault('needs_norm_verification', compact['norm_role'] != 'none' or has_norm_ref)
    compact.setdefault('requires_exact_quote', defaults.get('requires_exact_quote', False))
    compact.setdefault('claim_basis', defaults.get('claim_basis', 'mixed'))

# === Step 1: Read all partial_*.json and measure original size ===
original_bytes = 0
findings_out = []
agent_count = 0
norm_checks = load_norm_checks(output_dir)
merged_norm_checks = 0

for fname in sorted(os.listdir(output_dir)):
    if not (fname.startswith('partial_') and fname.endswith('.json')):
        continue

    fpath = os.path.join(output_dir, fname)
    original_bytes += os.path.getsize(fpath)

    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    agent = data.get('agent', fname.replace('partial_', '').replace('.json', ''))
    agent_count += 1

    for finding in data.get('findings', []):
        compact = {k: finding[k] for k in KEEP_FIELDS if k in finding}
        compact['agent'] = agent
        apply_agent_defaults(compact, finding, agent)

        if compact.get('norm_quote'):
            compact['norm_quote'] = str(compact['norm_quote'])[:QUOTE_MAX_LEN]

        # Build short claim from description
        desc = finding.get('description', '')
        if desc:
            compact['claim'] = desc[:CLAIM_MAX_LEN].rstrip()

        norm_check = norm_checks.get(finding.get('temp_id', ''))
        if norm_check:
            compact['norm_check_status'] = norm_check.get('norm_check_status')
            compact['norm_support_level'] = norm_check.get('support_level')
            compact['norm_doc_status'] = norm_check.get('doc_status')
            compact['corrected_norm_ref'] = norm_check.get('corrected_norm_ref')
            if norm_check.get('quote_text'):
                compact['norm_quote_preview'] = str(norm_check['quote_text'])[:QUOTE_MAX_LEN]
            merged_norm_checks += 1

        findings_out.append(compact)

# === Step 2: Write compact payload ===
payload = {
    'meta': {
        'description': 'Compact findings payload for R2 critic — verification-relevant fields only',
        'total_findings': len(findings_out),
        'total_agents': agent_count,
        'original_bytes': original_bytes,
        'norm_checks_merged': merged_norm_checks
    },
    'findings': findings_out
}

payload_path = os.path.join(output_dir, 'critic_payload.json')
with open(payload_path, 'w', encoding='utf-8') as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

payload_bytes = os.path.getsize(payload_path)
payload['meta']['payload_bytes'] = payload_bytes

# Rewrite with final meta
with open(payload_path, 'w', encoding='utf-8') as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

reduction = (1 - payload_bytes / original_bytes) * 100 if original_bytes > 0 else 0

print(f'Done!')
print(f'  partial_*.json total: {original_bytes:>8,} bytes ({original_bytes // 4000:>5}K tokens)')
print(f'  critic_payload.json:  {payload_bytes:>8,} bytes ({payload_bytes // 4000:>5}K tokens)')
print(f'  Reduction: {reduction:.0f}%')
print(f'  Findings: {len(findings_out)} from {agent_count} agents')
