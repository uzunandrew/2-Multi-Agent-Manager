"""
Build norm_finding_checks.json — normalize and pre-verify norm references used by R1 findings.
Creates a per-finding summary for the R2 critic without forcing the critic to inspect the
entire norms database from scratch.

Usage:
    python build_norm_finding_checks.py <project_path>

Example:
    python build_norm_finding_checks.py projects/EOM/133_23-ГК-ГРЩ
"""

import sys, os, io, json, re, argparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

parser = argparse.ArgumentParser(description='Build per-finding norm verification summary')
parser.add_argument('project_path', help='Path to project folder (contains _output/)')
args = parser.parse_args()

project_path = args.project_path.rstrip('/\\')
output_dir = os.path.join(project_path, '_output')
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
norms_dir = os.path.join(repo_root, 'norms')

subset_path = os.path.join(output_dir, 'norms_subset.json')
paragraphs_path = os.path.join(norms_dir, 'norms_paragraphs.json')


def normalize_text(value):
    return re.sub(r'\s+', ' ', str(value or '')).strip()


def normalize_designation(value):
    value = normalize_text(value).upper()
    value = value.replace('№', '')
    value = value.replace('–', '-').replace('—', '-')
    return value


def dedupe_keep_order(items):
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


DOC_PATTERNS = [
    r'СП\s*[\d\.]+',
    r'ГОСТ\s*(?:Р\s*)?(?:IEC\s*|МЭК\s*)?[\d\.\-]+',
    r'ФЗ\s*№?\s*\d+(?:\s*-\s*ФЗ)?',
    r'ПУЭ(?:-7)?',
    r'СНиП\s*[\d\.\-]+',
    r'РД\s*[\d\.\-]+',
]

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


def extract_doc_designations(text):
    found = []
    for pattern in DOC_PATTERNS:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            found.append(normalize_text(match.group(0)))
    return dedupe_keep_order(found)


def extract_paragraph_tokens(text):
    tokens = []
    for match in re.finditer(
        r'(?:п\.|пп\.|разд\.|гл\.|табл\.|таблица)\s*([0-9A-Za-zА-Яа-я\.\-, ]+)',
        text,
        re.IGNORECASE,
    ):
        raw = normalize_text(match.group(1)).rstrip('.,;:')
        for part in re.split(r'\s*,\s*', raw):
            part = normalize_text(part)
            if re.search(r'\d', part):
                tokens.append(part)
    return dedupe_keep_order(tokens)


def simplify_paragraph_token(token):
    token = normalize_text(token)
    token = re.sub(r'^(п\.|пп\.|разд\.|гл\.|табл\.|таблица)\s*', '', token, flags=re.IGNORECASE)
    return token.replace(' ', '')


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


subset_data = load_json(subset_path, {})
norms_dict = subset_data.get('norms', subset_data) if isinstance(subset_data, dict) else {}
paragraphs_data = load_json(paragraphs_path, {})
paragraphs_dict = paragraphs_data.get('norms', paragraphs_data) if isinstance(paragraphs_data, dict) else {}


def build_search_entries(norms_dict):
    entries = []
    if not isinstance(norms_dict, dict):
        return entries

    for key, value in norms_dict.items():
        doc = value if isinstance(value, dict) else {}
        doc_number = normalize_text(doc.get('doc_number', key))
        aliases = doc.get('aliases', []) if isinstance(doc.get('aliases'), list) else []
        tokens = {
            normalize_designation(key),
            normalize_designation(doc_number),
        }
        for alias in aliases:
            tokens.add(normalize_designation(alias))

        entries.append({
            'key': key,
            'doc_number': doc_number,
            'status': normalize_text(doc.get('status', 'unknown')).lower() or 'unknown',
            'replacement_doc': normalize_text(doc.get('replacement_doc', '')) or None,
            'tokens': {token for token in tokens if token},
        })

    return entries


search_entries = build_search_entries(norms_dict)


def find_doc_match(cited_doc):
    cited_norm = normalize_designation(cited_doc)
    cited_digits = re.findall(r'\d+', cited_norm)
    best = None
    best_score = -1

    for entry in search_entries:
        for token in entry['tokens']:
            score = None
            if cited_norm == token:
                score = 100 + len(token)
            elif cited_norm in token or token in cited_norm:
                score = 50 + len(token)
            else:
                token_digits = re.findall(r'\d+', token)
                if cited_digits and token_digits and cited_digits[0] == token_digits[0]:
                    score = 10 + len(token)

            if score is not None and score > best_score:
                best = entry
                best_score = score

    return best


def iter_paragraph_sources(cited_doc, matched_entry):
    targets = {normalize_designation(cited_doc)}
    if matched_entry:
        targets.add(normalize_designation(matched_entry['key']))
        targets.add(normalize_designation(matched_entry['doc_number']))
        if matched_entry.get('replacement_doc'):
            targets.add(normalize_designation(matched_entry['replacement_doc']))

    for key, content in paragraphs_dict.items():
        key_norm = normalize_designation(key)
        if any(target and (target == key_norm or target in key_norm or key_norm in target) for target in targets):
            yield key, content


def find_quote(cited_doc, matched_entry, paragraph_tokens):
    normalized_paras = [simplify_paragraph_token(token) for token in paragraph_tokens]

    for key, content in iter_paragraph_sources(cited_doc, matched_entry):
        if isinstance(content, dict):
            for para_key, para_text in content.items():
                para_norm = simplify_paragraph_token(str(para_key))
                if normalized_paras:
                    if any(
                        para_norm == token or para_norm in token or token in para_norm
                        for token in normalized_paras
                    ):
                        return str(para_text)[:500], f'{key}#{para_key}', True
                elif isinstance(para_text, str):
                    return para_text[:500], f'{key}#{para_key}', True
        elif isinstance(content, str) and not normalized_paras:
            return content[:500], key, True

    return '', None, False


def build_corrected_norm_ref(original_ref, doc_checks):
    corrected = original_ref
    changed = False

    for check in doc_checks:
        cited_doc = check.get('cited_doc')
        replacement_doc = check.get('replacement_doc')
        if cited_doc and replacement_doc and cited_doc != replacement_doc:
            corrected = corrected.replace(cited_doc, replacement_doc)
            changed = True

    return corrected if changed else None


def aggregate_doc_status(doc_checks):
    statuses = {
        check['doc_status']
        for check in doc_checks
        if check.get('doc_status') and check['doc_status'] != 'unknown'
    }
    if len(statuses) == 1:
        return next(iter(statuses))
    if len(statuses) > 1:
        return 'mixed'
    return 'unknown'


def build_reasoning(norm_check_status, doc_checks, quote_text, norm_role):
    if norm_check_status == 'not_needed':
        return 'Finding does not rely on a norm and does not require normative verification.'
    if norm_check_status == 'unsupported':
        return 'No resolved active norm/paragraph was found that structurally supports the cited reference.'
    if norm_check_status == 'corrected':
        replacements = [check['replacement_doc'] for check in doc_checks if check.get('replacement_doc')]
        replacements = dedupe_keep_order([item for item in replacements if item])
        if replacements:
            return f'Cited norm requires replacement or correction: {", ".join(replacements)}.'
        return 'Cited norm requires correction before the finding can be treated as fully normative.'
    if norm_check_status == 'weak_support':
        return 'The cited norm was structurally resolved, but no exact paragraph quote was found.'
    if norm_check_status == 'needs_human_review':
        return 'The finding requires an exact quote or manual normative review before full acceptance.'
    if quote_text:
        return 'Exact paragraph quote was found for the cited norm.'
    if norm_role == 'core':
        return 'Resolved active norm found, but support remains contextual.'
    return 'Resolved active norm found with contextual support.'


def apply_agent_defaults(agent_name, finding):
    defaults = AGENT_DEFAULTS.get(agent_name, {})
    has_norm_ref = bool(normalize_text(finding.get('norm_ref', '')))
    return {
        'norm_role': finding.get('norm_role', defaults.get('norm_role', 'supporting' if has_norm_ref else 'none')),
        'claim_basis': finding.get('claim_basis', defaults.get('claim_basis', 'mixed')),
        'requires_exact_quote': bool(
            finding.get('requires_exact_quote', defaults.get('requires_exact_quote', False))
        ),
        'needs_norm_verification': bool(
            finding.get(
                'needs_norm_verification',
                has_norm_ref or defaults.get('norm_role', 'none') != 'none' or defaults.get('claim_basis') == 'normative',
            )
        ),
    }


def build_finding_check(agent_name, finding):
    finding_id = finding.get('temp_id', '')
    norm_ref = normalize_text(finding.get('norm_ref', ''))
    defaults = apply_agent_defaults(agent_name, finding)
    norm_role = defaults['norm_role']
    claim_basis = defaults['claim_basis']
    requires_exact_quote = defaults['requires_exact_quote']
    needs_norm_verification = defaults['needs_norm_verification']

    if not needs_norm_verification and norm_role == 'none' and not norm_ref:
        return {
            'finding_id': finding_id,
            'source_agent': agent_name,
            'norm_check_status': 'not_needed',
            'resolved_norm_ref': '',
            'corrected_norm_ref': None,
            'doc_status': 'unknown',
            'paragraph_exists': False,
            'norm_applicability': 'not_needed',
            'support_level': 'unsupported',
            'quote_text': '',
            'quote_anchor': None,
            'reasoning': build_reasoning('not_needed', [], '', norm_role),
            'confidence': 1.0,
            'doc_checks': [],
        }

    if not norm_ref:
        status = 'unsupported' if norm_role == 'core' or requires_exact_quote else 'needs_human_review'
        return {
            'finding_id': finding_id,
            'source_agent': agent_name,
            'norm_check_status': status,
            'resolved_norm_ref': '',
            'corrected_norm_ref': None,
            'doc_status': 'unknown',
            'paragraph_exists': False,
            'norm_applicability': 'not_resolved',
            'support_level': 'unsupported',
            'quote_text': '',
            'quote_anchor': None,
            'reasoning': build_reasoning(status, [], '', norm_role),
            'confidence': 0.6,
            'doc_checks': [],
        }

    doc_checks = []
    quote_text = ''
    quote_anchor = None
    any_active = False
    any_quote = False
    any_replacement = False
    any_unresolved = False
    any_paragraph = False

    for ref_segment in re.split(r'\s*;\s*', norm_ref):
        ref_segment = normalize_text(ref_segment)
        if not ref_segment:
            continue

        docs = extract_doc_designations(ref_segment)
        paragraph_tokens = extract_paragraph_tokens(ref_segment)

        if not docs:
            any_unresolved = True
            doc_checks.append({
                'cited_ref_segment': ref_segment,
                'cited_doc': None,
                'resolved_doc_number': None,
                'doc_status': 'unknown',
                'replacement_doc': None,
                'paragraph_tokens': paragraph_tokens,
                'paragraph_exists': False,
                'quote_anchor': None,
            })
            continue

        for cited_doc in docs:
            matched = find_doc_match(cited_doc)
            doc_status = matched['status'] if matched else 'unknown'
            replacement_doc = matched['replacement_doc'] if matched else None
            resolved_doc_number = matched['doc_number'] if matched else None

            quote_candidate = ''
            anchor_candidate = None
            paragraph_exists = False

            if matched:
                quote_candidate, anchor_candidate, paragraph_exists = find_quote(cited_doc, matched, paragraph_tokens)
                if doc_status == 'active':
                    any_active = True
                if replacement_doc:
                    any_replacement = True
            else:
                any_unresolved = True

            if paragraph_exists:
                any_paragraph = True
            if quote_candidate and not quote_text:
                quote_text = quote_candidate
                quote_anchor = anchor_candidate
                any_quote = True

            doc_checks.append({
                'cited_ref_segment': ref_segment,
                'cited_doc': cited_doc,
                'resolved_doc_number': resolved_doc_number,
                'doc_status': doc_status,
                'replacement_doc': replacement_doc,
                'paragraph_tokens': paragraph_tokens,
                'paragraph_exists': paragraph_exists,
                'quote_anchor': anchor_candidate,
            })

    corrected_norm_ref = build_corrected_norm_ref(norm_ref, doc_checks)
    doc_status = aggregate_doc_status(doc_checks)

    if corrected_norm_ref:
        norm_check_status = 'corrected'
        support_level = 'direct' if any_quote else 'context_only'
        confidence = 0.92
    elif any_active and any_quote:
        norm_check_status = 'verified'
        support_level = 'direct'
        confidence = 0.95
    elif any_active:
        norm_check_status = 'weak_support'
        support_level = 'context_only'
        confidence = 0.78
    elif any_unresolved:
        norm_check_status = 'unsupported'
        support_level = 'unsupported'
        confidence = 0.7
    else:
        norm_check_status = 'unsupported'
        support_level = 'unsupported'
        confidence = 0.65

    if requires_exact_quote and not any_quote and norm_check_status in {'verified', 'weak_support'}:
        norm_check_status = 'needs_human_review'
        support_level = 'context_only'
        confidence = min(confidence, 0.72)

    return {
        'finding_id': finding_id,
        'source_agent': agent_name,
        'norm_check_status': norm_check_status,
        'resolved_norm_ref': norm_ref,
        'corrected_norm_ref': corrected_norm_ref,
        'doc_status': doc_status,
        'paragraph_exists': any_paragraph,
        'norm_applicability': 'not_evaluated',
        'support_level': support_level,
        'quote_text': quote_text,
        'quote_anchor': quote_anchor,
        'reasoning': build_reasoning(norm_check_status, doc_checks, quote_text, norm_role),
        'confidence': confidence,
        'doc_checks': doc_checks,
    }


checks = []

for fname in sorted(os.listdir(output_dir)):
    if not (fname.startswith('partial_') and fname.endswith('.json')):
        continue

    with open(os.path.join(output_dir, fname), 'r', encoding='utf-8') as f:
        data = json.load(f)

    agent_name = data.get('agent', fname.replace('partial_', '').replace('.json', ''))
    for finding in data.get('findings', []):
        checks.append(build_finding_check(agent_name, finding))


status_counts = {}
for check in checks:
    status = check['norm_check_status']
    status_counts[status] = status_counts.get(status, 0) + 1

output = {
    'meta': {
        'description': 'Per-finding normative verification summary for R2 critic',
        'total_checks': len(checks),
        'norms_subset_loaded': os.path.exists(subset_path),
        'norms_paragraphs_loaded': os.path.exists(paragraphs_path),
        'by_status': status_counts,
    },
    'checks': checks,
}

output_path = os.path.join(output_dir, 'norm_finding_checks.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print('Done!')
print(f'  Checks: {len(checks)}')
print(f'  Output: {output_path}')
print(f'  Statuses: {json.dumps(status_counts, ensure_ascii=False)}')
