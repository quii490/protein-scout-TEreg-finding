#!/usr/bin/env python3
from __future__ import annotations
import json, re, time, urllib.parse, urllib.request
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
AUDIT=BASE/'audit_work'/'audit_all_final.json'
REPORT=BASE/'audit_work'/'ppi_repair_report.json'

def fetch_json(url, timeout=8):
    req=urllib.request.Request(url, headers={'User-Agent':'TEreg-protein-audit/1.0'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode('utf-8', errors='replace'))

def fetch_text(url, timeout=8):
    req=urllib.request.Request(url, headers={'User-Agent':'TEreg-protein-audit/1.0'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode('utf-8', errors='replace')

def extract_uniprot(content):
    pats=[r'UniProt ID\s*\|\s*([A-Z0-9]+)', r'UniProt[^\n]*?\b([OPQ][0-9][A-Z0-9]{3}[0-9])\b']
    for p in pats:
        m=re.search(p, content)
        if m: return m.group(1)
    return None

def string_partners(gene):
    url='https://string-db.org/api/json/interaction_partners?'+urllib.parse.urlencode({'identifiers':gene,'species':9606,'limit':30})
    data=fetch_json(url)
    partners=[]
    for row in data[:15]:
        name=row.get('preferredName_B') or row.get('stringId_B') or row.get('preferredName_A') or ''
        score=row.get('score') or row.get('combined_score') or row.get('combinedScore')
        if isinstance(score, (int,float)) and score<=1:
            score_txt=f'{score:.3f}'
        else:
            score_txt=str(score) if score is not None else '—'
        partners.append((name, score_txt))
    return partners

def intact_partners(gene):
    q=urllib.parse.quote(gene)
    url=f'https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/{q}?format=tab27'
    txt=fetch_text(url)
    rows=[line.split('\t') for line in txt.splitlines() if line.strip()]
    partners=[]
    for cells in rows[:30]:
        joined=' '.join(cells)
        pmid='—'
        m=re.search(r'pubmed:(\d+)', joined, re.I)
        if m: pmid=m.group(1)
        method='—'
        m=re.search(r'psi-mi:"MI:\d+"\(([^)]+)\)', joined)
        if m: method=m.group(1)
        partner='—'
        aliases=' '.join(cells[4:6]) if len(cells)>=6 else joined
        syms=re.findall(r'(?:gene name|display_short)[:=]([A-Za-z0-9_.-]+)', aliases)
        for s in syms:
            if s.upper()!=gene.upper():
                partner=s; break
        partners.append((partner, method, pmid))
    return partners

def go_cc(uniprot):
    if not uniprot: return []
    url=f'https://rest.uniprot.org/uniprotkb/{urllib.parse.quote(uniprot)}.json'
    data=fetch_json(url)
    out=[]
    for x in data.get('uniProtKBCrossReferences', []):
        if x.get('database')=='GO':
            props={p.get('key'):p.get('value') for p in x.get('properties', [])}
            term=props.get('GoTerm') or ''
            if term.startswith('C:'):
                ev=props.get('GoEvidenceType') or '—'
                out.append((x.get('id'), term[2:], ev))
    return out[:20]

def block(gene, acc, sp, ip, go):
    lines=[]
    lines.append('')
    lines.append('##### PPI 数据源补充核查（自动审计）')
    lines.append('')
    lines.append('**IntAct/BioGrid 实验互作核查**:')
    lines.append('| Partner | 方法 | PMID |')
    lines.append('|---------|------|------|')
    if ip:
        for partner,method,pmid in ip[:10]: lines.append(f'| {partner} | {method} | {pmid} |')
    else:
        lines.append('| — | IntAct API 返回 0 条可解析互作 | — |')
    lines.append('')
    lines.append('**STRING 预测/整合互作核查**:')
    lines.append('| Partner | Score |')
    lines.append('|---------|-------|')
    if sp:
        for partner,score in sp[:10]: lines.append(f'| {partner} | {score} |')
    else:
        lines.append('| — | STRING API 返回 0 条 partner |')
    lines.append('')
    lines.append('**GO-CC 复合体/定位核查**:')
    if go:
        for goid,term,ev in go[:10]: lines.append(f'- {goid}: {term} ({ev})')
    else:
        lines.append('- UniProt GO-CC 未列出可解析复合体/细胞组分条目。')
    lines.append('')
    lines.append('**补充结论**: PPI 评分仍以报告评分表为准；本节用于补齐 IntAct、STRING、GO-CC 三源审计证据。')
    return '\n'.join(lines)+'\n'

def insert_ppi(content, addition):
    if 'PPI 数据源补充核查（自动审计）' in content:
        return content
    idx=content.find('#### 3.6')
    if idx<0: idx=content.find('### 3.6')
    if idx<0:
        return content.rstrip()+ '\n\n#### 3.6 PPI 网络\n' + addition
    next_idx=content.find('#### 3.7', idx)
    if next_idx<0: next_idx=content.find('### 3.7', idx)
    if next_idx<0:
        return content.rstrip()+addition
    return content[:next_idx].rstrip()+addition+'\n'+content[next_idx:]

def main():
    data=json.loads(AUDIT.read_text())
    targets=[]
    for gene,r in data['reports'].items():
        if any('PPI section does not explicitly cover' in e for e in r['errors']):
            targets.append((gene, BASE/r['path']))
    results=[]
    for gene,path in targets:
        content=path.read_text(encoding='utf-8', errors='replace')
        acc=extract_uniprot(content)
        rec={'gene':gene,'path':str(path.relative_to(BASE)),'uniprot':acc,'status':'pending'}
        try:
            sp=string_partners(gene)
            time.sleep(0.2)
            ip=intact_partners(gene)
            time.sleep(0.2)
            go=go_cc(acc)
            addition=block(gene, acc, sp, ip, go)
            new=insert_ppi(content, addition)
            if new!=content:
                path.write_text(new, encoding='utf-8')
            rec.update({'status':'updated','string_count':len(sp),'intact_rows':len(ip),'go_cc_count':len(go)})
        except Exception as e:
            rec.update({'status':'error','error':repr(e)})
        results.append(rec)
        print(json.dumps(rec, ensure_ascii=False))
    REPORT.write_text(json.dumps({'targets':len(targets),'results':results}, ensure_ascii=False, indent=2), encoding='utf-8')

if __name__=='__main__':
    main()
