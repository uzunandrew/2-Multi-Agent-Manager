"""
R3 Synthesizer — Python replacement for LLM synthesizer agent.
Filters, deduplicates, enriches, numbers, and outputs findings.json + rejected.json.

Usage:
    python synthesize.py <project_path>

Example:
    python synthesize.py projects/EOM/133_23-ГК-ГРЩ
"""

import sys, os, io, json, re, argparse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# === Arguments ===
parser = argparse.ArgumentParser(description='R3 Synthesizer — filter, dedup, enrich, number findings')
parser.add_argument('project_path', help='Path to project folder (contains _output/)')
args = parser.parse_args()

project_path = args.project_path.rstrip('/\\')
output_dir = os.path.join(project_path, '_output')
norms_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'norms')

# === Step 1: Read inputs ===
with open(os.path.join(output_dir, 'review.json'), 'r', encoding='utf-8') as f:
    review_data = json.load(f)

# Read all partial_*.json
partials = {}
for fname in os.listdir(output_dir):
    if fname.startswith('partial_') and fname.endswith('.json'):
        with open(os.path.join(output_dir, fname), 'r', encoding='utf-8') as f:
            data = json.load(f)
        agent = data.get('agent', fname.replace('partial_', '').replace('.json', ''))
        partials[agent] = data

# Read norms_paragraphs.json
norms_paragraphs = {}
norms_para_path = os.path.join(norms_dir, 'norms_paragraphs.json')
if os.path.exists(norms_para_path):
    with open(norms_para_path, 'r', encoding='utf-8') as f:
        norms_paragraphs = json.load(f)

# Build verdict map from review.json
verdicts = {}
for r in review_data.get('reviews', []):
    verdicts[r['finding_id']] = r

# === Step 2: Filter — keep only pass + pass_weak_norm ===
PASS_VERDICTS = {'pass', 'pass_weak_norm'}

accepted_ids = set()
rejected_list = []

for finding_id, v in verdicts.items():
    if v['verdict'] in PASS_VERDICTS:
        accepted_ids.add(finding_id)
    else:
        rejected_list.append({
            'original_id': finding_id,
            'reason': v['verdict'],
            'critic': 'main',
            'detail': v.get('reasoning', '')[:200]
        })

# Collect full finding objects for accepted IDs
accepted_findings = []
for agent_name, pdata in partials.items():
    for f in pdata.get('findings', []):
        tid = f.get('temp_id', '')
        if tid in accepted_ids:
            finding = dict(f)
            finding['source_agents'] = [agent_name]
            finding['critic_verdict'] = verdicts[tid]['verdict']
            accepted_findings.append(finding)

print(f'Step 2: {len(accepted_findings)} accepted, {len(rejected_list)} rejected')

# === Step 2.5: Apply structured corrections from critic ===
corrections_applied = 0
for f in accepted_findings:
    review = verdicts.get(f.get('temp_id', ''), {})
    if review.get('corrected_norm_ref'):
        f['norm_ref'] = review['corrected_norm_ref']
        corrections_applied += 1
    if review.get('norm_quote_used'):
        f['norm_quote'] = review['norm_quote_used']
        corrections_applied += 1
    if review.get('corrected_category'):
        f['category'] = review['corrected_category']
        corrections_applied += 1
    if review.get('needs_human_review'):
        f['needs_human_review'] = True
    if review.get('norm_review_status'):
        f['norm_review_status'] = review['norm_review_status']
    if review.get('norm_support_level'):
        f['norm_support_level'] = review['norm_support_level']
    if review.get('norm_doc_status'):
        f['norm_doc_status'] = review['norm_doc_status']

if corrections_applied:
    print(f'Step 2.5: {corrections_applied} corrections applied from critic')

# === Step 3: Deduplication ===
def extract_entities(text):
    """Extract technical designations: М-1.4, QF1, ВРУ-4, ЩСН..."""
    entities = set()
    for m in re.findall(r'[А-ЯA-Z][А-Яа-яA-Za-z]*[-.]?\d+[\.\d]*', text):
        entities.add(m.upper())
    return sorted(entities)[:5]

def normalize_norm_ref(ref):
    """Extract norm designation: 'СП 256' from 'СП 256.1325800.2016, п.14.15'"""
    if not ref:
        return ''
    m = re.search(r'(СП|ГОСТ|ПУЭ|СНиП|ФЗ|РД)\s*[\w\.\-]+', ref, re.IGNORECASE)
    return m.group(0).upper().strip() if m else ''

def dedup_key(f):
    """Generate dedup key from page + norm_ref + entity keywords."""
    page = f.get('page', '?')
    norm = normalize_norm_ref(f.get('norm_ref', ''))
    entities = extract_entities(f.get('title', '') + ' ' + f.get('description', '')[:200])
    entity_str = '|'.join(entities)
    # Fallback to title prefix if no norm and no entities
    if not norm and not entity_str:
        title = re.sub(r'[^\w\s]', '', f.get('title', '').lower())[:50].strip()
        return f'{page}_title_{title}'
    return f'{page}_{norm}_{entity_str}'

seen_keys = {}
deduped = []
merge_count = 0

for f in accepted_findings:
    key = dedup_key(f)
    if key in seen_keys:
        # Merge: add source_agent to existing
        existing = seen_keys[key]
        for sa in f.get('source_agents', []):
            if sa not in existing['source_agents']:
                existing['source_agents'].append(sa)
        merge_count += 1
    else:
        seen_keys[key] = f
        deduped.append(f)

print(f'Step 3: {merge_count} merged, {len(deduped)} after dedup')

# === Step 4: Confidence adjustment ===
for f in deduped:
    conf = f.get('confidence', 0.7)
    verdict = f.get('critic_verdict', 'pass')

    # Adjustments per R3_synthesizer rules
    if verdict == 'pass':
        conf += 0.1  # critic confirmed
    elif verdict == 'pass_weak_norm':
        conf -= 0.1  # substance ok, norm weak

    if len(f.get('source_agents', [])) > 1:
        conf += 0.1  # multiple agents found same

    norm_conf = f.get('norm_confidence', 1.0)
    if norm_conf < 0.8:
        conf -= 0.1

    # Clamp
    conf = max(0.3, min(1.0, round(conf, 2)))
    f['confidence'] = conf

    # Downgrade critical with low confidence
    if f.get('category') == 'Критическое' and conf < 0.7:
        f['category'] = 'Экономическое'

# === Step 5: Norm quote enrichment ===
enriched_count = 0
not_found_count = 0

for f in deduped:
    norm_ref = f.get('norm_ref', '')
    if not norm_ref:
        continue

    if f.get('norm_quote'):
        continue

    # Try to find in norms_paragraphs
    # norms_paragraphs structure may vary — try common patterns
    found = False

    # Search by norm designation in keys
    for key, content in norms_paragraphs.items():
        if isinstance(content, dict):
            # Nested structure: {"СП 256": {"15.3.2": "text..."}}
            for para_key, para_text in content.items():
                if para_key in norm_ref:
                    f['norm_quote'] = str(para_text)[:500]
                    f['norm_confidence'] = max(f.get('norm_confidence', 0.5), 0.9)
                    enriched_count += 1
                    found = True
                    break
        elif isinstance(content, str) and key in norm_ref:
            f['norm_quote'] = content[:500]
            f['norm_confidence'] = max(f.get('norm_confidence', 0.5), 0.9)
            enriched_count += 1
            found = True
        if found:
            break

    if not found:
        f['norm_quote'] = ''
        not_found_count += 1

print(f'Step 5: {enriched_count} enriched, {not_found_count} not found in norms_paragraphs')

# === Step 6: Sort and number ===
CAT_ORDER = {'Критическое': 0, 'Экономическое': 1, 'Эксплуатационное': 2}

deduped.sort(key=lambda f: (
    CAT_ORDER.get(f.get('category', ''), 9),
    -f.get('confidence', 0)
))

for i, f in enumerate(deduped, 1):
    f['id'] = f'F-{i:03d}'
    # Remove temp_id from final output
    f.pop('temp_id', None)

# === Step 7: Build stats ===
total_from_agents = sum(len(p.get('findings', [])) for p in partials.values())
by_category = {}
for f in deduped:
    cat = f.get('category', 'Unknown')
    by_category[cat] = by_category.get(cat, 0) + 1

stats = {
    'total_from_agents': total_from_agents,
    'after_critic': len(accepted_findings),
    'after_dedup': len(deduped),
    'final': len(deduped),
    'merged': merge_count,
    'by_category': by_category
}

# === Step 8: Write outputs ===
findings_output = {
    'findings': deduped,
    'stats': stats
}

with open(os.path.join(output_dir, 'findings.json'), 'w', encoding='utf-8') as f:
    json.dump(findings_output, f, ensure_ascii=False, indent=2)

with open(os.path.join(output_dir, 'rejected.json'), 'w', encoding='utf-8') as f:
    json.dump(rejected_list, f, ensure_ascii=False, indent=2)

print(f'\nDone!')
print(f'  findings.json: {len(deduped)} findings')
print(f'  rejected.json: {len(rejected_list)} rejected')
print(f'  Stats: {json.dumps(stats, ensure_ascii=False)}')
