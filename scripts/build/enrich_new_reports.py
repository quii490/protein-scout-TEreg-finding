#!/usr/bin/env python3
"""
Threaded batch enrich: PPI tables, IF images, ESMFold, Domain sections.
Processes all NEW scored reports with concurrent HTTP requests.
"""
import os, re, time, urllib.request, urllib.error, json, sys
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

PROJECT = Path('/Users/quii/Desktop/projects/protein-scout-TEreg-finding')
DETAIL = PROJECT / 'detail'
PPI_BIOGRID = Path('/Users/quii/Desktop/projects/GraphTEBind/protein_data/data-finding/ppi_data/biogrid_human_ppi.tab3.txt')
PPI_NUCLEAR = Path('/Users/quii/Desktop/projects/GraphTEBind/protein_data/data-finding/ppi_data/nuclear_ppi_human.tsv')
ESM_DIR = PROJECT / 'detail' / '_esm_structures'
ESM_URL = 'https://api.esmatlas.com/foldSequence/v1/pdb/'
MAX_ESM_LEN = 400
UA = 'Mozilla/5.0 (compatible; protein-scout/1.0)'
WORKERS = 8

ESM_DIR.mkdir(parents=True, exist_ok=True)
stats_lock = Lock()
stats = {'ppi': 0, 'if': 0, 'esm': 0, 'domain': 0, 'errors': 0, 'skipped_esm_len': 0}
print_lock = Lock()


def log(msg):
    with print_lock:
        print(msg, flush=True)

# ── Data loading ──

def load_ppi_data():
    bg_map = defaultdict(list)
    string_map = defaultdict(list)
    with open(PPI_BIOGRID) as f:
        for i, line in enumerate(f):
            if i == 0: continue
            p = line.strip().split('\t')
            if len(p) >= 4:
                a, b, method, pmid = p[0], p[1], p[2], p[3]
                bg_map[a.upper()].append((b, method, pmid))
                bg_map[b.upper()].append((a, method, pmid))
    with open(PPI_NUCLEAR) as f:
        for i, line in enumerate(f):
            if i == 0: continue
            p = line.strip().split('\t')
            if len(p) >= 4:
                a, b, src, score = p[0], p[1], p[2], p[3]
                if src == 'STRING':
                    string_map[a.upper()].append((b, int(score)))
                    string_map[b.upper()].append((a, int(score)))
                else:
                    bg_map[a.upper()].append((b, src, score))
                    bg_map[b.upper()].append((a, src, score))
    return bg_map, string_map


# ── API helpers ──

def _get(url, timeout=20):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode('utf-8', errors='replace')

def _post(url, data, timeout=120):
    req = urllib.request.Request(url, data=data.encode(), method='POST', headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

def fetch_string_partners(gene, limit=15):
    try:
        url = f'https://string-db.org/api/tsv/network?identifiers={urllib.request.quote(gene)}&species=9606&limit={limit}'
        text = _get(url, 15)
        partners = []
        for line in text.strip().split('\n')[1:]:
            cols = line.split('\t')
            if len(cols) >= 6:
                partners.append((cols[2], cols[5]))  # (partner, combined_score)
        return partners
    except Exception:
        return []

def resolve_and_fetch_if(gene):
    """Resolve ENSG from gene name, then fetch IF images from subcellular page."""
    try:
        # Step 1: Search HPA for ENSG
        search_url = f'https://www.proteinatlas.org/search/{urllib.request.quote(gene)}'
        page = _get(search_url, 15)
        ensg = None
        for pat in [
            rf'/(ENSG\d+-{re.escape(gene)})["\'/<]',
            rf'/(ENSG\d+[^"\'/<]*-{re.escape(gene)})["\'/<]',
        ]:
            m = re.search(pat, page, re.I)
            if m:
                ensg = m.group(1)
                break
        if not ensg:
            return [], None

        # Step 2: Fetch subcellular page
        sub_url = f'https://www.proteinatlas.org/{ensg}/subcellular'
        page2 = _get(sub_url, 15)
        images = []
        for m in re.finditer(r'(?:https?:)?//images\.proteinatlas\.org/\d+/\d+_[A-Za-z0-9_]+_blue_red_green\.jpg', page2):
            url = m.group(0)
            if url.startswith('//'): url = 'https:' + url
            if url not in images: images.append(url)
        images = images[:6]
        return images, ensg
    except Exception:
        return [], None

def get_uniprot_seq(accession):
    if not accession: return None
    acc = accession.strip()
    if not re.match(r'^[A-Z][0-9][A-Z0-9]{3}[0-9]$', acc):
        return None
    try:
        url = f'https://rest.uniprot.org/uniprotkb/{acc}.json'
        data = json.loads(_get(url, 30))
        seq = data.get('sequence', {}).get('value', '')
        if 30 < len(seq) <= MAX_ESM_LEN:
            return seq
        return None
    except Exception:
        return None

def run_esm(seq, pdb_path):
    try:
        data = _post(ESM_URL, seq.strip(), 30 + int(len(seq)*0.15))
        if len(data) > 5000 and b'ATOM' in data:
            with open(pdb_path, 'wb') as f:
                f.write(data)
            return True
        return False
    except Exception:
        return False

def extract_plddt(pdb_path):
    bf = []
    with open(pdb_path) as f:
        for line in f:
            if line.startswith('ATOM') and line[13:16].strip() == 'CA':
                try: bf.append(float(line[60:66].strip()))
                except: pass
    if not bf: return None
    m = sum(bf)/len(bf)
    return {'mean': round(m,2), 'high': round(sum(1 for b in bf if b>0.9)/len(bf)*100,1), 'low': round(sum(1 for b in bf if b<0.5)/len(bf)*100,1), 'n': len(bf)}


# ── Single report processor ──
def process_report(rec):
    """Process one NEW report: PPI + IF + ESM + Domain. Thread-safe."""
    rp = rec['path']
    gene = rec['gene']
    content = rp.read_text(encoding='utf-8', errors='replace')
    changed = False

    result = {'gene': gene, 'ppi': False, 'if': False, 'esm': False, 'domain': False}

    try:
        # 1. PPI - if missing AND gene not accession-like
        if not rec['has_ppi']:
            # Build using local data + STRING API
            g = gene.upper()
            partners = []
            seen = set()
            for p, s in sorted(string_map.get(g, []), key=lambda x: -x[1])[:15]:
                if p.upper() not in seen:
                    partners.append((p, 'STRING', str(s))); seen.add(p.upper())
            for p, src, ev in bg_map.get(g, [])[:10]:
                if p.upper() not in seen:
                    partners.append((p, src.split(':')[0] if ':' in src else src, str(ev)[:40])); seen.add(p.upper())
            if not partners:
                api = fetch_string_partners(gene)
                for p, s in api[:15]:
                    if p.upper() not in seen:
                        partners.append((p, 'STRING', str(int(float(s)*1000)))); seen.add(p.upper())
            if partners:
                lines = ['\n### PPI 互作网络\n', '| 互作伙伴 | 来源 | 评分 |', '|---|---|---|']
                for p, src, s in partners[:20]:
                    lines.append(f'| {p} | {src} | {s} |')
                block = '\n'.join(lines)
                # Insert before TE section
                m = re.search(r'\n###\s+TE\s+调控', content)
                if m:
                    content = content[:m.start()] + block + '\n' + content[m.start():]
                else:
                    content = content.rstrip() + '\n' + block + '\n'
                changed = True; result['ppi'] = True

        # 2. IF images
        if not rec['has_if']:
            try:
                images, ensg = resolve_and_fetch_if(gene)
                if images and ensg:
                    lines = [
                        '\n### HPA IF 图像\n',
                        f'HPA: https://www.proteinatlas.org/{ensg}',
                        '',
                    ]
                    for img in images:
                        lines.append(f'![]({img})')
                    block = '\n'.join(lines)
                    for marker in ['\n### PPI 互作网络', '\n### TE 调控', '\n### PubMed']:
                        idx = content.rfind(marker)
                        if idx > 500:
                            content = content[:idx] + block + '\n' + content[idx:]
                            changed = True; result['if'] = True
                            break
                    if not result['if']:
                        content = content.rstrip() + '\n' + block + '\n'
                        changed = True; result['if'] = True
                    time.sleep(0.1)
            except Exception as e:
                result['if_error'] = str(e)[:80]

        # 3. ESMFold
        if not rec['has_esm'] and rec['accession']:
            seq = get_uniprot_seq(rec['accession'])
            if seq:
                pdb_path = ESM_DIR / f'{gene}_esmfold.pdb'
                if not pdb_path.exists():
                    time.sleep(1.5)  # Rate limit
                    if not run_esm(seq, str(pdb_path)):
                        if changed:
                            rp.write_text(content, encoding='utf-8')
                        return result
                st = extract_plddt(str(pdb_path))
                if st:
                    section = f"""
### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `{pdb_path.relative_to(PROJECT)}`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | {st['mean']} |
| pLDDT > 0.9 | {st['high']}% |
| pLDDT < 0.5 | {st['low']}% |
| 残基数 | {st['n']} |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。
"""
                    for marker in ['\n### 数据来源', '\n### 5.', '\n### 6.']:
                        idx = content.find(marker)
                        if idx > 500:
                            content = content[:idx] + section + '\n' + content[idx:]
                            changed = True; result['esm'] = True
                            break
                    if not result['esm']:
                        content = content.rstrip() + '\n' + section + '\n'
                        changed = True; result['esm'] = True

        # 4. Domain section (only if completely missing)
        if not rec['has_domain']:
            try:
                url = f'https://rest.uniprot.org/uniprotkb/search?query=gene_exact:{gene}+AND+organism_id:9606&format=tsv&fields=accession,xref_smart,ft_domain,xref_interpro,xref_pfam'
                text = _get(url, 15)
                lines = text.strip().split('\n')
                if len(lines) >= 2:
                    h = lines[0].split('\t')
                    v = lines[1].split('\t')
                    row = dict(zip(h, v))
                    smart = row.get('SMART',''); interpro = row.get('InterPro','')
                    pfam = row.get('Pfam',''); dom = row.get('Domain [FT]','')
                    if any([smart, interpro, pfam, dom]):
                        section = f"""
### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | {smart or '未检出'} |
| InterPro | {interpro or '未检出'} |
| Pfam | {pfam or '未检出'} |
| UniProt Domain | {dom or '未检出'} |
"""
                        for marker in ['\n### PPI 互作网络', '\n### TE 调控', '\n### PubMed']:
                            idx = content.rfind(marker)
                            if idx > 500:
                                content = content[:idx] + section + '\n' + content[idx:]
                                changed = True; result['domain'] = True
                                break
            except Exception:
                pass

        if changed:
            rp.write_text(content, encoding='utf-8')

    except Exception as e:
        result['error'] = str(e)[:100]

    return result


# ── Main ──

def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 0
    workers = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else WORKERS

    global string_map, bg_map
    log('Loading PPI data...')
    bg_map, string_map = load_ppi_data()
    log(f'  BioGRID: {len(bg_map)} genes, STRING: {len(string_map)} genes')

    log('Finding NEW reports...')
    todo = []
    for root, dirs, files in os.walk(str(DETAIL)):
        for f in files:
            if not f.endswith('-evaluation.md'): continue
            rp = Path(root) / f
            content = rp.read_text(encoding='utf-8', errors='replace')
            date_match = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', content[:1000])
            if not date_match or date_match.group(1) < '2026-06-26': continue
            if 'status: rejected' in content[:500]: continue
            gene = rp.parent.name
            # Extract accession
            acc = None
            for pat in [r'UniProt ID.*?([A-Z][0-9][A-Z0-9]{3}[0-9])', r'UniProt\s+ID\s*\|\s*([A-Z][0-9][A-Z0-9]{3}[0-9])']:
                m = re.search(pat, content)
                if m: acc = m.group(1); break
            todo.append({
                'path': rp, 'gene': gene, 'accession': acc,
                'has_ppi': bool(re.search(r'互作伙伴', content)),
                'has_if': 'images.proteinatlas.org' in content,
                'has_esm': 'ESMFold' in content,
                'has_domain': bool(re.search(r'SMART.*UniProt domain|Domain/SMART', content)),
            })
    if limit:
        todo = todo[:limit]
    log(f'  Processing {len(todo)} reports with {workers} workers')

    missing = {'ppi': 0, 'if': 0, 'esm': 0, 'domain': 0}
    for r in todo:
        if not r['has_ppi']: missing['ppi'] += 1
        if not r['has_if']: missing['if'] += 1
        if not r['has_esm'] and r['accession']: missing['esm'] += 1
        if not r['has_domain']: missing['domain'] += 1
    log(f'  Missing: PPI={missing["ppi"]}, IF={missing["if"]}, ESM={missing["esm"]}, Domain={missing["domain"]}')

    t0 = time.time()
    done = [0]
    done_lock = Lock()

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(process_report, r): r for r in todo}
        for i, fut in enumerate(as_completed(futures)):
            r = fut.result()
            with done_lock:
                done[0] += 1
            with stats_lock:
                for k in ['ppi', 'if', 'esm', 'domain']:
                    if r.get(k): stats[k] += 1
            if done[0] % 100 == 0 or done[0] == len(todo):
                elapsed = time.time() - t0
                rate = done[0] / elapsed
                eta = (len(todo) - done[0]) / rate if rate > 0 else 0
                log(f'  [{done[0]}/{len(todo)}] {rate:.1f}/s ETA={eta:.0f}s PPI={stats["ppi"]} IF={stats["if"]} ESM={stats["esm"]} Domain={stats["domain"]}')

    log(f'\n=== Done in {time.time()-t0:.0f}s ===')
    log(f'PPI: {stats["ppi"]}  IF: {stats["if"]}  ESM: {stats["esm"]}  Domain: {stats["domain"]}')


if __name__ == '__main__':
    main()
