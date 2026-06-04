#!/usr/bin/env python3
from pathlib import Path
import re, json
BASE=Path(__file__).resolve().parents[1]
DETAIL=BASE/'detail'
changed=[]
for path in sorted(DETAIL.glob('*/*/*-evaluation.md')):
    text=path.read_text(encoding='utf-8', errors='replace')
    lines=text.splitlines()
    out=[]; did=False
    for i,line in enumerate(lines):
        stripped=line.strip()
        # Historical malformed rows, e.g. | | | | **137/183** | and | | | | **74.9/100** |
        if stripped.startswith('|') and '原始总分' not in stripped and re.search(r'\*\*\s*\d+(?:\.\d+)?\s*/\s*183\s*\*\*', stripped):
            m=re.search(r'\*\*\s*(\d+(?:\.\d+)?)\s*/\s*183\s*\*\*', stripped)
            line=f'| **原始总分** | | | **{m.group(1)}/183** | |'
            did=True
        elif stripped.startswith('|') and '归一化总分' not in stripped and re.search(r'\*\*\s*\d+(?:\.\d+)?\s*/\s*100\s*\*\*', stripped):
            m=re.search(r'\*\*\s*(\d+(?:\.\d+)?)\s*/\s*100\s*\*\*', stripped)
            line=f'| **归一化总分** | | | **{m.group(1)}/100** | |'
            did=True
        out.append(line)
    if did:
        path.write_text('\n'.join(out)+('\n' if text.endswith('\n') else ''), encoding='utf-8')
        changed.append(str(path.relative_to(BASE)))
(BASE/'audit_work'/'fix_unlabeled_score_rows_report.json').write_text(json.dumps({'files_touched':len(changed),'files':changed}, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'files_touched':len(changed)}, ensure_ascii=False))
