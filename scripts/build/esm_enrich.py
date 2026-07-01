#!/usr/bin/env python3
"""
ESM fold and analysis for proteins lacking structural data.
Targets: proteins with pLDDT < 70 or no AlphaFold data, no PDB, length < 2000 aa.
Runs ESM API to get PDB structures, extracts pLDDT, and enriches evaluation reports.
"""
import os, json, re, time, urllib.request, urllib.error, sys, subprocess
from pathlib import Path

PROJECT = '/Users/quii/Desktop/projects/protein-scout-TEreg-finding'
ESM_URL = 'https://api.esmatlas.com/foldSequence/v1/pdb/'
MAX_SEQ_LEN = 400  # ESM API hard limit: 400 amino acids
BATCH_SIZE = 5
SLEEP_BETWEEN = 2  # seconds between API calls

os.chdir(PROJECT)


def get_uniprot_sequence(accession):
    """Fetch protein sequence from UniProt or from the Excel file."""
    if not accession:
        return None
    acc = str(accession).strip()
    if not acc or len(acc) < 6 or acc.startswith('[NA:') or '_HUMAN' in acc:
        return None
    # Allow standard UniProt accessions (including TrEMBL A0A* etc.)
    if not re.match(r'^[A-Z][0-9][A-Z0-9]{3}[0-9]$', acc) and not re.match(r'^[A-Z0-9]{6,10}$', acc):
        return None
    try:
        url = f'https://rest.uniprot.org/uniprotkb/{acc}.json'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=30)
        data = json.loads(resp.read())
        seq = data.get('sequence', {}).get('value', '')
        return seq if 30 < len(seq) <= MAX_SEQ_LEN else None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        # Retry once for transient errors
        time.sleep(2)
        try:
            resp = urllib.request.urlopen(req, timeout=30)
            data = json.loads(resp.read())
            seq = data.get('sequence', {}).get('value', '')
            return seq if 30 < len(seq) <= MAX_SEQ_LEN else None
        except Exception:
            return None
    except Exception:
        return None
    try:
        url = f'https://rest.uniprot.org/uniprotkb/{acc}.json'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=30)
        data = json.loads(resp.read())
        seq = data.get('sequence', {}).get('value', '')
        if not seq:
            return None
        # ESM API can handle up to ~1000aa reliably
        if len(seq) > 500:
            print(f'  Sequence too long for ESM ({len(seq)} aa > 500), skipping')
            return None
        if len(seq) < 30:
            return None
        return seq
    except Exception:
        return None


def run_esm_fold(sequence, output_pdb_path):
    """Run ESM fold API and save PDB. Handles timeouts for long sequences."""
    try:
        seq = sequence.strip()
        if len(seq) > 400:
            print(f'  Sequence too long ({len(seq)} aa > 400 ESM hard limit), skipping')
            return False

        # Shorter timeout for longer sequences, but minimum 60s
        timeout = min(120, 30 + int(len(seq) * 0.15))

        req = urllib.request.Request(ESM_URL, data=seq.encode(), method='POST')
        resp = urllib.request.urlopen(req, timeout=timeout)
        pdb_data = resp.read()
        if len(pdb_data) > 5000 and b'ATOM' in pdb_data:
            with open(output_pdb_path, 'wb') as f:
                f.write(pdb_data)
            return True
        return False
    except urllib.error.HTTPError as e:
        msg = e.read().decode()[:200] if hasattr(e, 'read') else str(e)
        print(f'  ESM HTTP {e.code}: {msg[:100]}')
        return False
    except Exception as e:
        msg = str(e)[:120]
        print(f'  ESM error: {msg}')
        return False


def extract_esm_plddt(pdb_path):
    """Extract per-residue pLDDT from ESM PDB (B-factor column)."""
    bfactors = []
    try:
        with open(pdb_path) as f:
            for line in f:
                if line.startswith('ATOM') and line[13:16].strip() == 'CA':
                    b = float(line[60:66].strip())
                    bfactors.append(b)
    except Exception:
        pass
    if not bfactors:
        return None
    mean_plddt = sum(bfactors) / len(bfactors)
    high_pct = sum(1 for b in bfactors if b > 0.9) / len(bfactors) * 100
    low_pct = sum(1 for b in bfactors if b < 0.5) / len(bfactors) * 100
    return {
        'mean_plddt': round(mean_plddt, 2),
        'very_high_pct': round(high_pct, 1),
        'very_low_pct': round(low_pct, 1),
        'residues': len(bfactors),
    }


def find_reports_needing_esm():
    """Find evaluation reports that would benefit from ESM analysis.

    Focus: proteins in TE-relevant categories (chromatin, nucleoplasm, nucleolus)
    with no PDB experimental structure AND pLDDT < 70 or missing.
    """
    TE_CATEGORIES = {'chromatin', 'nucleoplasm', 'nucleolus', 'nuclear-body'}

    candidates = []
    for root, dirs, files in os.walk('detail'):
        for f in files:
            if not f.endswith('-evaluation.md'):
                continue
            rp = os.path.join(root, f)
            content = open(rp).read()
            gene = os.path.basename(os.path.dirname(rp))

            # Skip rejected
            if 'status: rejected' in content[:500]:
                continue

            # Only TE-relevant categories
            cat = root.split('/')[1]
            if cat not in TE_CATEGORIES:
                continue

            # Already has ESM section?
            if 'ESMFold' in content or 'esmatlas' in content.lower():
                continue

            # Check existing structural data
            has_pdb = False
            pdb_match = re.search(r'(?:PDB|可用 PDB 条目)[^|]*\|\s*(\S+)', content)
            if pdb_match and pdb_match.group(1) not in ('无', '0', '0.', ''):
                has_pdb = True

            af_plddt = None
            m = re.search(r'(?:AlphaFold|AF)\s*(?:平均\s*)?pLDDT\s*[=＝]\s*(\d+\.?\d*)', content)
            if m:
                af_plddt = float(m.group(1))

            # Priority: no structure data at all > low pLDDT > just missing PDB
            if has_pdb and af_plddt and af_plddt > 80:
                continue  # Good structural data, skip

            priority = 0
            if not af_plddt and not has_pdb:
                priority = 10
            elif af_plddt and af_plddt < 50:
                priority = 9  # Very low AF confidence - ESM might help
            elif not af_plddt:
                priority = 8
            elif af_plddt < 70:
                priority = 6
            elif not has_pdb:
                priority = 4
            else:
                continue  # Skip if AF > 70 and has PDB

            # Extract UniProt accession
            accession = None
            for pat in [
                r'UniProt ID.*?([A-Z][0-9][A-Z0-9]{3}[0-9])',
                r'UniProt\s+ID\s*\|\s*([A-Z][0-9][A-Z0-9]{3}[0-9])',
                r'https://www\.uniprot\.org/uniprotkb/([A-Z][0-9][A-Z0-9]{3}[0-9])',
            ]:
                m = re.search(pat, content)
                if m:
                    accession = m.group(1)
                    break

            # Also check Excel for accession
            if not accession:
                candidates.append((gene, rp, priority, None))
                continue

            candidates.append((gene, rp, priority, accession))

    candidates.sort(key=lambda x: (-x[2], x[0]))
    return candidates


def enrich_report(report_path, esm_stats, esm_pdb_path):
    """Add ESM analysis section to an evaluation report."""
    content = open(report_path).read()

    esm_section = f"""
### ESM 结构预测补充 (ESMFold Analysis)

**方法**: 使用 Meta ESM Metagenomic Atlas API 对全长蛋白序列进行 ab initio 折叠预测。
**PDB 文件**: `{os.path.relpath(esm_pdb_path, PROJECT)}`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | {esm_stats['mean_plddt']} |
| pLDDT > 0.9 占比 | {esm_stats['very_high_pct']}% |
| pLDDT < 0.5 占比 | {esm_stats['very_low_pct']}% |
| 建模残基数 | {esm_stats['residues']} |

**与 AlphaFold 对比**:

"""
    # Find AF pLDDT for comparison
    m = re.search(r'(?:AlphaFold|AF)\s*(?:平均\s*)?pLDDT\s*[=＝]\s*(\d+\.?\d*)', content)
    if m:
        af_plddt = float(m.group(1))
        delta = esm_stats['mean_plddt'] - af_plddt
        direction = '高于' if delta > 0 else '低于'
        esm_section += f'ESMFold pLDDT ({esm_stats["mean_plddt"]}) {direction} AlphaFold pLDDT ({af_plddt}) {abs(delta):.1f}。'
    else:
        esm_section += '无 AlphaFold 数据可对比。ESMFold 提供独立的从头折叠验证。'

    esm_section += '\n\nESMFold 基于进化规模语言模型，对序列空间进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证和补充。\n'

    # Insert before "### 数据来源" or "### 5." or at the end of the report
    insert_points = [
        '\n### 数据来源',
        '\n### 5. 数据来源',
        '\n## 5.',
        '\n### 6.',
        '\n## 6.',
    ]

    inserted = False
    for pt in insert_points:
        idx = content.find(pt)
        if idx > 500:  # Don't insert too early
            content = content[:idx] + esm_section + '\n' + content[idx:]
            inserted = True
            break

    if not inserted:
        # Append near the end before any closing tags
        content = content.rstrip() + '\n' + esm_section + '\n'

    with open(report_path, 'w') as f:
        f.write(content)


def main():
    import pandas as pd

    # Parse args
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    dry_run = '--dry-run' in sys.argv

    candidates = find_reports_needing_esm()
    print(f'Found {len(candidates)} candidates needing ESM analysis')
    print(f'Processing top {min(limit, len(candidates))}...')

    esm_dir = 'detail/_esm_structures'
    os.makedirs(esm_dir, exist_ok=True)

    processed = 0
    for gene, rp, priority, accession in candidates[:limit]:
        print(f'\n[{priority}] {gene} ({accession})')

        if dry_run:
            continue

        # Get sequence
        if not accession:
            print('  No accession, skipping')
            continue

        seq = get_uniprot_sequence(accession)
        if not seq:
            print('  No sequence, skipping')
            continue

        print(f'  Sequence: {len(seq)} aa, running ESMFold...')

        pdb_path = f'{esm_dir}/{gene}_esmfold.pdb'
        if os.path.exists(pdb_path):
            print('  PDB already exists, using cached')
        else:
            if not run_esm_fold(seq, pdb_path):
                print('  ESM fold failed')
                continue
            time.sleep(SLEEP_BETWEEN)

        stats = extract_esm_plddt(pdb_path)
        if not stats:
            print('  Could not extract pLDDT')
            continue

        print(f'  ESM pLDDT: {stats["mean_plddt"]}, >0.9: {stats["very_high_pct"]}%')
        enrich_report(rp, stats, pdb_path)
        processed += 1

    print(f'\nProcessed {processed} reports')

    if processed > 0:
        print('Running rebuild...')
        subprocess.run(['python3', 'rebuild_summary.py'], capture_output=True, timeout=60)
        subprocess.run(['python3', 'scripts/build/build_report_index.py'], capture_output=True, timeout=120)


if __name__ == '__main__':
    main()
