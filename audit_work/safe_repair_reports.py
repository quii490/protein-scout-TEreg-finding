#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from collections import defaultdict, Counter

BASE = Path(__file__).resolve().parents[1]
DETAIL = BASE / 'detail'
if str(BASE) not in sys.path:
    sys.path.insert(0, str(BASE))
import validate_strict as vs

VAULT_PREFIX = 'Projects/TEreg-finding/protein-interested/'
IF_NOTE = '> Protein Atlas IF: 暂无数据（Pending cell analysis），核定位基于 UniProt + GO。'
PAE_NOTE = '> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。'


def report_paths():
    return sorted(DETAIL.glob('*/*/*-evaluation.md'))


def split_embed_inner(inner: str):
    if '\\|' in inner:
        path, alias = inner.split('\\|', 1)
        sep = '|'
    elif '|' in inner:
        path, alias = inner.split('|', 1)
        sep = '|'
    else:
        path, alias, sep = inner, None, ''
    return path.rstrip('\\').strip(), alias, sep


def vault_rel(path: Path) -> str:
    return VAULT_PREFIX + str(path.relative_to(BASE))


def find_existing_asset(gene: str, basename: str, report_dir: Path) -> Path | None:
    candidates = []
    candidates.append(report_dir / 'IF_images' / basename)
    candidates.append(report_dir / basename)
    for c in candidates:
        if c.exists():
            return c
    matches = list(DETAIL.glob(f'*/{gene}/IF_images/{basename}')) + list(DETAIL.glob(f'*/{gene}/{basename}'))
    return matches[0] if matches else None


def repair_embeds(content: str, path: Path, changes: list[str]) -> str:
    gene = path.parent.name
    missing_if_count = 0

    def repl(m):
        nonlocal missing_if_count
        inner = m.group(1)
        raw_path, alias, _ = split_embed_inner(inner)
        clean = raw_path.replace('\\', '')
        if 'IF_images/' not in clean and not clean.endswith('.jpg') and not clean.endswith('.jpeg'):
            return m.group(0)
        # only repair image embeds that point into this vault/project
        if not (clean.startswith(VAULT_PREFIX) or clean.startswith('/')):
            return m.group(0)
        file_path = vs.vault_path_to_file(raw_path)
        if file_path and file_path.exists():
            fixed_path = vault_rel(file_path) if BASE in file_path.parents else clean
            suffix = f'|{alias}' if alias else ''
            if fixed_path != raw_path or '\\|' in inner:
                changes.append('normalized existing image wikilink')
            return f'![[{fixed_path}{suffix}]]'
        basename = Path(clean).name
        found = find_existing_asset(gene, basename, path.parent)
        if found:
            suffix = f'|{alias}' if alias else ''
            changes.append(f'fixed broken image path {basename}')
            return f'![[{vault_rel(found)}{suffix}]]'
        if 'IF_images/' in clean:
            missing_if_count += 1
            changes.append(f'removed broken IF embed {basename}')
            return ''
        return m.group(0)

    content = re.sub(r'!\[\[([^\]]+)\]\]', repl, content)
    if missing_if_count and not vs.has_explicit_absence(content, vs.IF_ABSENCE_PATTERNS):
        content = insert_after_section(content, '3.1', IF_NOTE)
        changes.append('added explicit IF absence note after removing broken embeds')
    return content


def insert_after_section(content: str, section_marker: str, note: str) -> str:
    if note in content:
        return content
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if section_marker in line and ('核定位' in line or section_marker == '3.4'):
            insert_at = i + 1
            while insert_at < len(lines) and lines[insert_at].strip() == '':
                insert_at += 1
            lines.insert(insert_at, note)
            return '\n'.join(lines) + ('\n' if content.endswith('\n') else '')
    # fallback after frontmatter/title
    lines.insert(min(len(lines), 8), note)
    return '\n'.join(lines) + ('\n' if content.endswith('\n') else '')


def patch_table_line(line: str, score: int | None = None, weighted: float | None = None) -> str:
    if not line.strip().startswith('|'):
        return line
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if len(cells) < 5:
        return line
    if score is not None:
        cells[1] = f'{score}/10'
    if weighted is not None:
        cells[3] = str(int(weighted)) if float(weighted).is_integer() else f'{weighted:.1f}'
    return '| ' + ' | '.join(cells) + ' |'


def repair_scores(content: str, cat: str, changes: list[str]) -> str:
    pubmed = vs.extract_pubmed_total(content)
    lines = content.splitlines()
    changed = False
    # fix novelty bucket for scored reports only
    if cat != 'rejected' and pubmed is not None and pubmed <= 100:
        expected = vs.expected_novelty(pubmed)
        current = vs.extract_score(content, 'novelty')
        if expected is not None and current is not None and current != expected:
            new_lines = []
            for line in lines:
                if line.strip().startswith('|') and any(alias in line for alias in vs.DIM_PATTERNS['novelty']):
                    line = patch_table_line(line, expected, expected * vs.WEIGHTS['novelty'])
                    changed = True
                new_lines.append(line)
            lines = new_lines
            content = '\n'.join(lines) + ('\n' if content.endswith('\n') else '')
            changes.append(f'fixed novelty score {current}->{expected} for PubMed={pubmed}')

    scores = {dim: vs.extract_score(content, dim) for dim in vs.WEIGHTS}
    if cat == 'rejected' or any(v is None for v in scores.values()):
        return content
    cross = vs.extract_cross(content)
    raw = sum(scores[d] * w for d, w in vs.WEIGHTS.items()) + cross
    norm = raw / 1.83
    lines = content.splitlines()
    out = []
    raw_done = norm_done = False
    for line in lines:
        if line.strip().startswith('|') and '原始总分' in line:
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            while len(cells) < 5:
                cells.append('')
            cells[3] = f'**{raw:.1f}/183**' if raw % 1 else f'**{int(raw)}/183**'
            line = '| ' + ' | '.join(cells) + ' |'
            raw_done = True
            changed = True
        elif line.strip().startswith('|') and '归一化总分' in line:
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            while len(cells) < 5:
                cells.append('')
            cells[3] = f'**{norm:.1f}/100**'
            line = '| ' + ' | '.join(cells) + ' |'
            norm_done = True
            changed = True
        out.append(line)
    if changed:
        changes.append('recomputed raw/normalized score from score table')
    return '\n'.join(out) + ('\n' if content.endswith('\n') else '')


def ensure_absence_notes(content: str, path: Path, changes: list[str]) -> str:
    cat = path.parent.parent.name
    if_dir = path.parent / 'IF_images'
    if_files = list(if_dir.glob('*.jpg')) + list(if_dir.glob('*.jpeg')) if if_dir.exists() else []
    if cat != 'rejected' and not if_files and not vs.has_explicit_absence(content, vs.IF_ABSENCE_PATTERNS):
        content = insert_after_section(content, '3.1', IF_NOTE)
        changes.append('added explicit IF absence note')
    gene = path.parent.name
    pae = path.parent / f'{gene}-PAE.png'
    if cat != 'rejected' and not (pae.exists() and pae.stat().st_size > 500) and not vs.has_explicit_absence(content, vs.PAE_ABSENCE_PATTERNS):
        # warning-only gate, but note helps completeness
        content = insert_after_section(content, '3.4', PAE_NOTE)
        changes.append('added explicit PAE absence note')
    return content


def main():
    summary = Counter()
    touched = []
    for path in report_paths():
        old = path.read_text(encoding='utf-8', errors='replace')
        content = old
        changes = []
        content = repair_embeds(content, path, changes)
        content = ensure_absence_notes(content, path, changes)
        content = repair_scores(content, path.parent.parent.name, changes)
        if content != old:
            path.write_text(content, encoding='utf-8')
            touched.append((str(path.relative_to(BASE)), changes))
            for c in changes:
                summary[c] += 1
    out = {
        'files_touched': len(touched),
        'change_counts': dict(summary.most_common()),
        'files': [{'path': p, 'changes': c} for p, c in touched],
    }
    out_path = BASE / 'audit_work' / 'safe_repair_report.json'
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'files_touched': len(touched), 'change_counts': dict(summary.most_common(20))}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
