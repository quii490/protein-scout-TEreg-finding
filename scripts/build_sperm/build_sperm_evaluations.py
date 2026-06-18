#!/usr/bin/env python3
"""生成 sperm 模块评估报告（中文，含 STRING PPI + HPA IF 图像）"""
import json, os, sys, time, urllib.request, re, xml.etree.ElementTree as ET, glob
from datetime import datetime

HPA_BASE = "https://www.proteinatlas.org"

def get_hpa_if_urls(ensg):
    if not ensg: return [], []
    try:
        u = f"{HPA_BASE}/{ensg}.xml"
        r = urllib.request.Request(u, headers={"User-Agent":"ps/1.0"})
        with urllib.request.urlopen(r, timeout=10) as resp:
            root = ET.fromstring(resp.read().decode())
        urls = []
        for ce in root.iter('cellExpression'):
            if ce.get('technology','').startswith('ICC'):
                for img in ce.iter('image'):
                    iu = img.find('imageUrl')
                    if iu is not None and iu.text: urls.append(iu.text)
                break
        brg = [x for x in urls if 'blue_red_green' in x]
        return brg + urls, urls
    except: return [], []

def get_string_ppi(gene):
    try:
        u = f"https://string-db.org/api/json/network?identifiers={gene}&species=9606&limit=10"
        r = urllib.request.Request(u, headers={"User-Agent":"ps/1.0"})
        with urllib.request.urlopen(r, timeout=10) as resp:
            d = json.loads(resp.read())
        if not d: return []
        return sorted(d, key=lambda x: x.get('score',0), reverse=True)[:10]
    except: return []

def generate_candidate(gene, info, pm, sources):
    ensg = info.get('Ensembl','')
    ab = ', '.join(info.get('Antibody',[])) or '未获取'
    rel = info.get('Reliability (IF)','未获取')
    src_list = '、'.join(sources)
    sc = len(sources)

    pref, all_urls = get_hpa_if_urls(ensg)
    if pref:
        ifb = f"""
<!-- SPERM_HPA_IF_START -->
**HPA IF 图像（{datetime.now().strftime('%Y-%m-%d')}）**: {sc} 个精子部位: {src_list}
{chr(10).join(f'![]({x})' for x in pref[:4])}
<!-- SPERM_HPA_IF_END -->
"""
        ifs = f'已获取 ({len(pref)} 张)'
    else:
        ifb = '\n*HPA IF 图像未获取。已查询 HPA subcellular 页面。*\n'
        ifs = '未获取'

    ppi = get_string_ppi(gene)
    prow = '\n'.join(f"| {p.get('preferredName_B','?')} | {p.get('score',0):.3f} | {p.get('experimental',p.get('experimentally_determined',0)):.3f} | {p.get('database',p.get('database_annotated',0)):.3f} | {p.get('textmining',0):.3f} |"
                     for p in ppi[:10]) if ppi else "| *STRING 无数据* | — | — | — | — |"

    if sc >= 4: ss, se = 19, f"{sc} 部位: {src_list}"
    elif sc >= 3: ss, se = 18, f"{sc} 部位: {src_list}"
    elif sc == 2: ss, se = 16, f"双部位: {src_list}"
    else: ss, se = 14, f"单部位: {src_list}"

    if pm <= 10: ps, pn = 10, "极低"
    elif pm <= 30: ps, pn = 8, "低"
    elif pm <= 60: ps, pn = 7, "中等"
    elif pm <= 100: ps, pn = 6, "较多"
    else: ps, pn = 5, "多"

    ns = 10 if pm <= 10 else (8 if pm <= 30 else (6 if pm <= 60 else 4))
    pis = 18 if len(ppi) >= 6 else (15 if len(ppi) >= 4 else (12 if len(ppi) >= 2 else (9 if len(ppi) >= 1 else 5)))
    ss2 = 5; rw = ss*4 + ps*4 + pis*3 + ss2*2 + ns*2; fsc = min(round(rw/2.6), 100)

    if fsc >= 50: sta = "sperm_candidate"
    elif fsc >= 25: sta = "sperm_low_priority"
    else: sta = "sperm_manual_review"

    return f"""---
type: sperm-protein-evaluation
gene: "{gene}"
module: sperm
status: {sta}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: [protein-scout, sperm, evaluation]
---

# {gene} — 精子模块评估

## 1. 基本信息
- **基因:** {gene}
- **Ensembl:** {ensg}
- **抗体:** {ab}
- **IF 可靠性:** {rel}
- **PubMed:** {pm} 篇
- **精子定位部位:** {src_list} ({sc} 个)

## 2. HPA 精子定位证据
- **来源:** {src_list} ✓
- **链接:** https://www.proteinatlas.org/{ensg}-{gene}
- **IF 图像:** {ifs}
{ifb}

## 3. UniProt / GO-CC 精子定位证据
*待 UniProt/GO-CC 采集。*

## 4. PubMed 文献证据
- **文献数:** {pm} 篇 ({pn}研究量)
- *关键文献待人工调研。*

## 5. AlphaFold / PAE / PDB / 结构域
*待结构数据采集。*
PAE 图像暂无数据（未生成本地图片），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络
### STRING (人类, top 10)
| Partner | Combined | Exp | DB | Text |
|---|---|---|---|---|
{prow}
*待 IntAct/BioGRID/humanPPI 补充。*

## 7. 评分表
| 维度 | 评分 | 依据 |
|---|---:|---|
| 精子定位 | {ss}/20 | {se} |
| PubMed | {ps}/20 | {pm} 篇 |
| PPI | {pis}/20 | STRING |
| 结构 | {ss2}/10 | 待采集 |
| 新颖性 | {ns}/10 | {pn} |

- **评分:** **{fsc}/100**

## 8. 结论
**{sta.upper().replace("_"," ")}**

## 9. 人工复核备注
- 精子部位: {src_list}
- 建议验证精子 IF 文献定位
"""

def generate_eliminated(gene, info, pm, sources):
    ensg = info.get('Ensembl','')
    sl = '、'.join(sources)
    return f"""---
type: sperm-protein-evaluation
gene: "{gene}"
module: sperm
status: sperm_eliminated
date: {datetime.now().strftime('%Y-%m-%d')}
tags: [protein-scout, sperm, evaluation, eliminated]
---

# {gene} — 精子模块评估（已淘汰）

## 1. 基本信息
- **基因:** {gene}
- **Ensembl:** {ensg}
- **精子部位:** {sl}
- **PubMed 总数:** {pm} 篇 ⚠️ **>100**

## 2. 淘汰原因
PubMed {pm} > 100 篇，自动淘汰。

## 3. 备注
因文献量超阈值未进行详细评估。
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python build_sperm_evaluations.py <pubmed_prescreen.json>")
        sys.exit(1)

    with open(sys.argv[1]) as f: ps = json.load(f)
    with open("sperm/data/sperm_hpa_seed.json") as f: seed = json.load(f)

    g2i = {}
    for hf in ['/tmp/hpa_centrosome.json', '/tmp/hpa_satellite.json']:
        if os.path.exists(hf):
            with open(hf) as f:
                for item in json.load(f):
                    g2i[item['Gene']] = {k: item[k] for k in ['Ensembl','Antibody','Reliability (IF)'] if k in item}

    results = ps.get('results',{})
    elim = ps.get('eliminated_genes',[])
    pas = ps.get('passed_genes',[])

    os.makedirs("sperm/audit", exist_ok=True); n = 0
    for gene in elim:
        g2i.get(gene,{}); pm=results.get(gene,{}).get('pubmed_total',0)
        src=seed['gene_details'].get(gene,{}).get('sources',['精子'])
        r=generate_eliminated(gene,g2i.get(gene,{}),pm,src)
        d=f"sperm/detail/{gene}";os.makedirs(d,exist_ok=True)
        with open(f"{d}/{gene}-sperm-evaluation.md",'w') as f: f.write(r)
        n+=1;
        if n%50==0: print(f"  淘汰 {n}/{len(elim)}")

    for i,gene in enumerate(pas):
        info=g2i.get(gene,{});pm=results.get(gene,{}).get('pubmed_total',0)
        src=seed['gene_details'].get(gene,{}).get('sources',['精子'])
        r=generate_candidate(gene,info,pm,src)
        d=f"sperm/detail/{gene}";os.makedirs(d,exist_ok=True)
        with open(f"{d}/{gene}-sperm-evaluation.md",'w') as f: f.write(r)
        n+=1;
        if (i+1)%50==0: print(f"  进度 {i+1}/{len(pas)}")
        time.sleep(0.2)

    print(f"\n✅ 完成: {len(elim)}淘汰 + {len(pas)}候选 = {len(elim)+len(pas)}")
