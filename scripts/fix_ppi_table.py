#!/usr/bin/env python3
"""Fix scoring table format issues:
Pattern A: | score | /10 | ×weight [= result] | → | score/10 | ×weight | weighted | (missing weighted value)
Pattern B: | score | /10 | ×weight = result | → | score/10 | ×weight | weighted |
Pattern C: | score/10 | 10 | **weighted** | → | score/10 | ×weight | weighted | (wrong weight column)
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")

WEIGHTS = {
    '核定位': 4,
    '蛋白大小': 1,
    '新颖性': 5,
    '三维结构': 3,
    '调控结构域': 2,
    'PPI': 3,
}

def get_weight(dimension_text):
    """Find the weight for a given dimension from the text."""
    for key, w in WEIGHTS.items():
        if key in dimension_text:
            return w
    return None


def fix_scoring_table(content):
    """Fix broken scoring table rows."""
    lines = content.split('\n')
    new_lines = []
    changed = False
    in_scoring_section = False
    table_header_seen = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Detect scoring section start
        if '评分总览' in stripped:
            in_scoring_section = True
            new_lines.append(line)
            i += 1
            continue

        # Detect table header row in scoring section
        if in_scoring_section and stripped.startswith('| 维度') and '得分' in stripped:
            table_header_seen = True
            new_lines.append(line)
            i += 1
            continue

        # Detect end of scoring section (next major section like "### 3." or blank line after end)
        if in_scoring_section and table_header_seen:
            if stripped == '':
                # Look ahead: if next non-blank line starts with ### or ##, end scoring
                j = i + 1
                while j < len(lines) and lines[j].strip() == '':
                    j += 1
                if j < len(lines):
                    nxt = lines[j].strip()
                    if nxt.startswith('### ') or nxt.startswith('## '):
                        in_scoring_section = False
                        table_header_seen = False
                new_lines.append(line)
                i += 1
                continue
            elif stripped.startswith('### ') or stripped.startswith('## '):
                in_scoring_section = False
                table_header_seen = False
                new_lines.append(line)
                i += 1
                continue

        # Fix data rows in the scoring table
        if in_scoring_section and table_header_seen and stripped.startswith('|') and '---' not in stripped:
            cells = [c.strip() for c in stripped.split('|')]

            # Skip summary rows like **原始总分**, **归一化总分**, 互证加分
            dim_text = cells[1] if len(cells) > 1 else ''
            if '原始总分' in dim_text or '归一化总分' in dim_text or '互证加分' in dim_text:
                new_lines.append(line)
                i += 1
                continue

            # Skip rows without dimension content
            if not dim_text or dim_text == '':
                new_lines.append(line)
                i += 1
                continue

            # --- Pattern A & B: | score | /10 | ×weight [= result] | [evidence] | ---
            # cells[2] = score (e.g. "5"), cells[3] = "/10"
            if len(cells) >= 5 and cells[3] == '/10':
                try:
                    score = int(cells[2])
                except ValueError:
                    new_lines.append(line)
                    i += 1
                    continue

                weight_cell = cells[4] if len(cells) > 4 else ''
                # Parse weight from "×4" or "×4 = 20" or "x4 = 20"
                weight_match = re.search(r'[×xX](\d+)', weight_cell)
                if not weight_match:
                    # Fallback: determine weight from dimension name
                    w = get_weight(dim_text)
                    if w is None:
                        new_lines.append(line)
                        i += 1
                        continue
                else:
                    w = int(weight_match.group(1))

                weighted_val = score * w

                # Evidence is after the weight cell
                evidence = ''
                if len(cells) > 5:
                    evidence = cells[5]

                new_cells = ['', dim_text, f'{score}/10', f'×{w}', str(weighted_val), evidence]
                new_line = '| ' + ' | '.join(new_cells[1:]) + ' |'
                new_lines.append(new_line)
                changed = True
                i += 1
                continue

            # --- Pattern C: | score/10 | 10 | **weighted** | evidence | ---
            # cells[2] = "score/10", cells[3] = "10" (wrong weight), cells[4] = weighted val
            if len(cells) >= 5 and '/' in cells[2] and re.match(r'^\d+/\d+$', cells[2]):
                weight_cell = cells[3] if len(cells) > 3 else ''
                # Check if weight column is just a number (not ×N format)
                if re.match(r'^\d+$', weight_cell):
                    try:
                        score_val = int(cells[2].split('/')[0])
                    except (ValueError, IndexError):
                        new_lines.append(line)
                        i += 1
                        continue

                    w = get_weight(dim_text)
                    if w is None:
                        new_lines.append(line)
                        i += 1
                        continue

                    # Evidence is after the old weighted value column
                    evidence = cells[5] if len(cells) > 5 else ''

                    new_cells = ['', dim_text, f'{score_val}/10', f'×{w}', str(score_val * w), evidence]
                    new_line = '| ' + ' | '.join(new_cells[1:]) + ' |'
                    new_lines.append(new_line)
                    changed = True
                    i += 1
                    continue

        new_lines.append(line)
        i += 1

    return '\n'.join(new_lines), changed


def main():
    fixed_count = 0

    for root, dirs, files in os.walk(DETAIL):
        for f in files:
            if not f.endswith('-evaluation.md'):
                continue
            path = os.path.join(root, f)
            gene = os.path.basename(os.path.dirname(path))
            cat = os.path.basename(os.path.dirname(os.path.dirname(path)))
            if cat == 'rejected':
                continue

            with open(path) as fh:
                content = fh.read()

            new_content, changed = fix_scoring_table(content)

            if changed:
                with open(path, 'w') as fh:
                    fh.write(new_content)
                fixed_count += 1
                # Print less frequently for large batches
                if fixed_count <= 20 or fixed_count % 50 == 0:
                    print(f"  FIXED [{fixed_count}]: {cat}/{gene}")

    print(f"\nTotal scoring table fixes: {fixed_count}")


if __name__ == "__main__":
    main()
