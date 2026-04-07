"""
Build norms_subset.json — extract only norms mentioned in partial_*.json findings.
This subset replaces full norms_db.json for the R2 critic, saving ~100K tokens.

Usage:
    python build_norms_subset.py <project_path>

Example:
    python build_norms_subset.py projects/EOM/133_23-ГК-ГРЩ
"""

import sys, os, io, json, re, argparse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

parser = argparse.ArgumentParser(description='Build norms subset from partial findings')
parser.add_argument('project_path', help='Path to project folder (contains _output/)')
args = parser.parse_args()

project_path = args.project_path.rstrip('/\\')
output_dir = os.path.join(project_path, '_output')
norms_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'norms')

# === Step 1: Collect all norm_ref from partial_*.json ===
all_norm_refs = set()

for fname in os.listdir(output_dir):
    if fname.startswith('partial_') and fname.endswith('.json'):
        with open(os.path.join(output_dir, fname), 'r', encoding='utf-8') as f:
            data = json.load(f)
        for finding in data.get('findings', []):
            norm_ref = finding.get('norm_ref', '')
            if norm_ref:
                all_norm_refs.add(norm_ref)

print(f'Collected {len(all_norm_refs)} unique norm_ref values from findings')

# === Step 2: Normalize norm designations ===
# Extract document designations (СП 256.1325800.2016, ГОСТ 32144-2013, etc.)
norm_designations = set()

patterns = [
    r'СП\s*[\d\.]+',           # СП 256.1325800.2016
    r'ГОСТ\s*(?:Р\s*)?[\d\.\-]+',  # ГОСТ Р 50462-2009, ГОСТ 32144-2013
    r'ГОСТ\s*IEC\s*[\d\.\-]+',     # ГОСТ IEC 60335-1-2015
    r'ФЗ\s*№?\s*\d+',         # ФЗ №123
    r'ПУЭ(?:-7)?',            # ПУЭ, ПУЭ-7
    r'СНиП\s*[\d\.\-]+',      # СНиП
    r'РД\s*[\d\.\-]+',        # РД
]

for ref in all_norm_refs:
    for pattern in patterns:
        matches = re.findall(pattern, ref, re.IGNORECASE)
        for m in matches:
            # Normalize whitespace
            norm = re.sub(r'\s+', ' ', m.strip())
            norm_designations.add(norm)

print(f'Extracted {len(norm_designations)} unique norm designations')

# === Step 3: Filter norms_db.json ===
norms_db_path = os.path.join(norms_dir, 'norms_db.json')
with open(norms_db_path, 'r', encoding='utf-8') as f:
    norms_db_raw = json.load(f)

# norms_db structure: {"meta": {...}, "norms": {"СП 256...": {...}, ...}, "replacements": {...}}
norms_dict = norms_db_raw.get('norms', norms_db_raw)
if not isinstance(norms_dict, dict):
    print(f'ERROR: unexpected norms_db structure: {type(norms_dict)}')
    sys.exit(1)

replacements = norms_db_raw.get('replacements', {})
total_norms = len(norms_dict)

# Match norm designations against norms_dict keys
subset_norms = {}
matched_keys = set()

for doc_key, doc_value in norms_dict.items():
    doc_key_lower = doc_key.lower().strip()
    doc_number = doc_value.get('doc_number', doc_key).lower().strip() if isinstance(doc_value, dict) else doc_key.lower().strip()

    for nd in norm_designations:
        nd_lower = nd.lower().strip()
        # Direct substring match
        if nd_lower in doc_key_lower or nd_lower in doc_number:
            subset_norms[doc_key] = doc_value
            matched_keys.add(doc_key)
            break
        # Match by primary digits (e.g. "256" in "СП 256.1325800.2016")
        nd_digits = re.findall(r'\d+', nd)
        if nd_digits:
            primary = nd_digits[0]
            if len(primary) >= 3 and primary in doc_key:
                subset_norms[doc_key] = doc_value
                matched_keys.add(doc_key)
                break

# Also include replacement docs for matched norms
for key in list(matched_keys):
    doc = subset_norms.get(key, {})
    if isinstance(doc, dict):
        repl = doc.get('replacement_doc', '')
        if repl and repl in norms_dict and repl not in subset_norms:
            subset_norms[repl] = norms_dict[repl]

# Filter replacements to only include relevant ones
subset_replacements = {}
for key, val in replacements.items():
    if key in subset_norms or (isinstance(val, str) and val in subset_norms):
        subset_replacements[key] = val

# Build subset output in same structure as original
subset_output = {
    'meta': {
        'description': 'Subset of norms_db.json for R2 critic — only norms mentioned in findings',
        'total_norms': len(subset_norms),
        'source_total': total_norms
    },
    'norms': subset_norms,
    'replacements': subset_replacements
}

# === Step 4: Write subset ===
subset_path = os.path.join(output_dir, 'norms_subset.json')
with open(subset_path, 'w', encoding='utf-8') as f:
    json.dump(subset_output, f, ensure_ascii=False, indent=2)

original_size = os.path.getsize(norms_db_path)
subset_size = os.path.getsize(subset_path)
reduction = (1 - subset_size / original_size) * 100

print(f'\nDone!')
print(f'  norms_db.json:     {original_size:>8,} bytes ({original_size//4000:>5}K tokens)')
print(f'  norms_subset.json: {subset_size:>8,} bytes ({subset_size//4000:>5}K tokens)')
print(f'  Reduction: {reduction:.0f}%')
print(f'  Norms matched: {len(subset_norms)} / {total_norms}')
