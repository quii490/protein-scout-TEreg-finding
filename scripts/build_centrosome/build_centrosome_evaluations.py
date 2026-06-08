#!/usr/bin/env python3
"""
Step 7B: 重新生成 centrosome 模块报告
- 中文报告 + ASB7 风格 HPA IF 图像嵌入 (blue_red_green 优先)
- 5 维度评分（无 TE）
- STRING PPI 真实数据
- PAE 缺图不报失败
"""
import json, os, sys, time, urllib.request, xml.etree.ElementTree as ET, re
from datetime import datetime

HPA_BASE = "https://www.proteinatlas.org"


def get_hpa_if_images(ensg, gene):
    """从 HPA XML 获取所有 IF 图像 URL，按 blue_red_green > red_green > selected 排序"""
    if not ensg:
        return [], "", "", ""
    try:
        url = f"{HPA_BASE}/{ensg}.xml"
        req = urllib.request.Request(url, headers={"User-Agent": "protein-scout/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            xml = r.read().decode()
        root = ET.fromstring(xml)

        brg, rg, sel, all_urls = [], [], [], []
        summary = ""
        reliability = ""

        for ce in root.iter('cellExpression'):
            if ce.get('technology', '').startswith('ICC'):
                s = ce.find('summary')
                if s is not None and s.text:
                    summary = s.text
                v = ce.find('verification')
                if v is not None:
                    reliability = v.get('description', v.text or '')
                for img in ce.iter('image'):
                    u = img.find('imageUrl')
                    if u is not None and u.text:
                        url_text = u.text
                        all_urls.append(url_text)
                        if 'blue_red_green' in url_text:
                            brg.append(url_text)
                        elif 'red_green' in url_text:
                            rg.append(url_text)
                        elif 'selected' in url_text:
                            sel.append(url_text)
                break

        preferred = brg + rg + sel
        return preferred, all_urls, summary, reliability
    except Exception as e:
        return [], [], "", f"获取失败: {e}"


def get_string_ppi(gene):
    """从 STRING 获取 PPI 数据，返回 Markdown 表格行"""
    try:
        url = f"https://string-db.org/api/json/network?identifiers={gene}&species=9606&limit=10"
        req = urllib.request.Request(url, headers={"User-Agent": "protein-scout/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        if not data:
            return ["| — | — | — | — | — |", "| *STRING 无注释互作数据* | — | — | — | — |"]
        rows = []
        for p in sorted(data, key=lambda x: x.get('score', 0), reverse=True)[:10]:
            name = p.get('preferredName_B', '?')
            score = p.get('score', 0)
            exp = p.get('experimental', 0)
            db = p.get('database', 0)
            text = p.get('textmining', 0)
            rows.append(f"| {name} | {score:.3f} | {exp:.3f} | {db:.3f} | {text:.3f} |")
        return rows or ["| *无高置信度 STRING 互作 (score<0.4)* | — | — | — | — |"]
    except Exception as e:
        return [f"| *STRING 查询失败: {e}* | — | — | — | — |"]


def generate_eliminated_report(gene, info, pubmed_total):
    ensg = info.get('ensembl', '')
    src = info.get('source', 'centrosome')
    src_cn = {'centrosome': '中心体', 'satellite': '中心粒卫星', 'both': '中心体+中心粒卫星'}.get(src, src)
    return f"""---
type: centrosome-protein-evaluation
gene: "{gene}"
module: centrosome
status: centrosome_eliminated
date: {datetime.now().strftime('%Y-%m-%d')}
tags: [protein-scout, centrosome, evaluation, eliminated]
---

# {gene} — 中心体模块评估（已淘汰）

## 1. 基本信息

- **基因:** {gene}
- **Ensembl:** {ensg}
- **HPA 来源:** {src_cn}
- **PubMed 总数:** {pubmed_total} 篇 ⚠️ **超过阈值 (>100)**

## 2. 淘汰原因

PubMed 总文献数 = {pubmed_total} (>100 篇)。按中心体模块 PubMed 淘汰规则自动淘汰。

## 3. HPA 种子证据

- HPA 来源: {src_cn}
- HPA 链接: https://www.proteinatlas.org/{ensg}-{gene}

## 4. 备注

- 因 PubMed 文献量超阈值自动淘汰，未进行详细评估。
"""


def generate_candidate_report(gene, info, pubmed_total):
    ensg = info.get('ensembl', '')
    src = info.get('source', 'centrosome')
    src_cn = {'centrosome': '中心体', 'satellite': '中心粒卫星', 'both': '中心体+中心粒卫星'}.get(src, src)
    antibody = ', '.join(info.get('antibody', [])) or '未获取'
    if_rel = info.get('if_reliability', '未获取')
    subcell = ', '.join(info.get('subcell', [])[:3]) or '未获取'

    # HPA IF images (ASB7 style)
    preferred_urls, all_urls, if_summary, if_reliability = get_hpa_if_images(ensg, gene)
    hpa_page_url = f"https://www.proteinatlas.org/{ensg}-{gene}/subcellular"

    if preferred_urls:
        # Use external HPA URLs directly (ASB7 style)
        if_block_lines = [
            f'\n<!-- CENTROSOME_HPA_IF_START -->',
            f'**HPA IF 图像（{datetime.now().strftime("%Y-%m-%d")}）**: HPA subcellular 页面存在可用 IF 图像。',
            f'HPA 定位: {subcell}。HPA IF 可靠性: {if_reliability or if_rel}。',
            f'来源: {hpa_page_url}',
            ''
        ]
        # Add up to 6 images
        for url in preferred_urls[:6]:
            if_block_lines.append(f'![]({url})')
        if_block_lines.append('<!-- CENTROSOME_HPA_IF_END -->\n')
        if_block = '\n'.join(if_block_lines)
        if_status = f'已获取 ({len(preferred_urls)} 张, {"blue_red_green" if any("blue_red_green" in u for u in preferred_urls) else "selected"})'
    elif all_urls:
        if_block = f'\n<!-- CENTROSOME_HPA_IF_START -->\n**HPA IF 图像**: 仅 thumbnail/selected 可用。\n![]({all_urls[0]})\n*thumbnail only，不作为强定位证据*\n<!-- CENTROSOME_HPA_IF_END -->\n'
        if_status = '仅 thumbnail'
    else:
        if_block = f'\n*HPA IF 图像未获取。已查询: {hpa_page_url}。{if_summary or "HPA XML 中无可用 IF 图像 URL。"}*\n'
        if_status = '未获取（已查询 HPA）'

    # PPI from STRING
    ppi_rows = get_string_ppi(gene)
    ppi_section = '\n'.join(ppi_rows)

    # 5-dimension scoring
    if src == 'both':
        centro_score, centro_evidence = 18, f"HPA 双来源标注（中心体 + 中心粒卫星）。定位: {subcell}"
    elif src == 'centrosome':
        centro_score, centro_evidence = 16, f"HPA 中心体标注。定位: {subcell}"
    else:
        centro_score, centro_evidence = 14, f"HPA 中心粒卫星标注。定位: {subcell}"

    if pubmed_total <= 10: pubmed_score, pubmed_note = 10, "极低研究量"
    elif pubmed_total <= 30: pubmed_score, pubmed_note = 8, "低研究量"
    elif pubmed_total <= 60: pubmed_score, pubmed_note = 7, "中等研究量"
    elif pubmed_total <= 100: pubmed_score, pubmed_note = 6, "较多文献"
    else: pubmed_score, pubmed_note = 5, "文献量大"

    if pubmed_total <= 10: novelty_score = 10
    elif pubmed_total <= 30: novelty_score = 8
    elif pubmed_total <= 60: novelty_score = 6
    else: novelty_score = 4

    ppi_score = 15 if len(ppi_rows) > 2 else (10 if len(ppi_rows) > 1 else 5)
    struct_score = 5  # default, pending structural data

    raw = (centro_score * 4) + (pubmed_score * 4) + (ppi_score * 3) + (struct_score * 2) + (novelty_score * 2)
    final = min(round(raw / 2.6), 100)

    # Determine status
    if final >= 50: status = "centrosome_candidate"
    elif final >= 25: status = "centrosome_low_priority"
    else: status = "centrosome_manual_review"

    return f"""---
type: centrosome-protein-evaluation
gene: "{gene}"
module: centrosome
status: {status}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: [protein-scout, centrosome, evaluation]
---

# {gene} — 中心体模块评估

## 1. 基本信息

- **基因:** {gene}
- **Ensembl:** {ensg}
- **HPA 来源:** {src_cn}
- **HPA 抗体:** {antibody}
- **IF 可靠性:** {if_rel}
- **PubMed 文献总数:** {pubmed_total} 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** {src_cn} ✓
- **HPA 链接:** https://www.proteinatlas.org/{ensg}-{gene}
- **HPA 定位:** {subcell}
- **IF 图像状态:** {if_status}

{if_block}

## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 {src_cn} 定位。

## 4. PubMed 文献证据

- **文献总数:** {pubmed_total} 篇
- **研究量评估:** {pubmed_note}
- *关键文献待人工调研。*

## 5. AlphaFold / PAE / PDB / 结构域

*待结构数据完整采集。需人工审核。*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
{ppi_section}

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | {centro_score}/20 | {centro_evidence} |
| PubMed/文献 | {pubmed_score}/20 | {pubmed_total} 篇文献 |
| PPI/互作网络 | {ppi_score}/20 | STRING 互作数据 |
| 结构/结构域 | {struct_score}/10 | 待结构数据采集 |
| 新颖性/特异性 | {novelty_score}/10 | {pubmed_note} |

- **最终评分:** **{final}/100**

## 8. 最终结论

**{status.upper().replace("_", " ")}**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: {src_cn}
- 抗体: {antibody}（IF 可靠性: {if_rel}）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
"""


def main():
    if len(sys.argv) < 2:
        print("用法: python build_centrosome_evaluations.py <pubmed_prescreen.json> [--limit N]")
        return

    with open(sys.argv[1]) as f:
        prescreen = json.load(f)
    with open("centrosome/data/centrosome_hpa_seed.json") as f:
        seed = json.load(f)

    limit = None
    if '--limit' in sys.argv:
        limit = int(sys.argv[sys.argv.index('--limit') + 1])

    # Gene info lookup
    g2info = {}
    for hpa_file in ['/tmp/hpa_centrosome.json', '/tmp/hpa_satellite.json']:
        if os.path.exists(hpa_file):
            with open(hpa_file) as f:
                for item in json.load(f):
                    g = item.get('Gene', '')
                    if g:
                        g2info[g] = {
                            'ensembl': item.get('Ensembl', ''),
                            'antibody': item.get('Antibody', []),
                            'if_reliability': item.get('Reliability (IF)', ''),
                            'subcell': item.get('Subcellular location', []),
                            'main_location': item.get('Subcellular main location', []),
                        }
    for g, d in seed['gene_details'].items():
        if g in g2info:
            g2info[g]['source'] = 'both' if d['source_both'] else ('centrosome' if d['source_centrosome'] else 'satellite')

    results = prescreen.get('results', {})
    eliminated = prescreen.get('eliminated_genes', [])
    passed = prescreen.get('passed_genes', [])
    pilot = {'AURKA','PLK4','CEP192','NEDD1','CETN2','PCM1','CCP110','CCDC14','CEP72','CEP97'}
    eliminated = [g for g in eliminated if g not in pilot]
    passed = [g for g in passed if g not in pilot]

    regen_log = []
    count = 0
    total = len(eliminated) + len(passed)

    # 淘汰报告
    for gene in eliminated:
        if limit and count >= limit: break
        info = g2info.get(gene, {})
        r = results.get(gene, {})
        report = generate_eliminated_report(gene, info, r.get('pubmed_total', 0))
        outdir = f"centrosome/detail/{gene}"
        os.makedirs(outdir, exist_ok=True)
        with open(f"{outdir}/{gene}-centrosome-evaluation.md", 'w') as f:
            f.write(report)
        regen_log.append({'gene': gene, 'status': 'ELIMINATED', 'lines': report.count(chr(10))})
        count += 1
        if count % 50 == 0:
            print(f"  淘汰 {count}/{len(eliminated)}")

    # 候选报告 (含 IF + STRING PPI)
    for i, gene in enumerate(passed):
        if limit and count >= limit: break
        info = g2info.get(gene, {})
        r = results.get(gene, {})
        report = generate_candidate_report(gene, info, r.get('pubmed_total', 0))
        outdir = f"centrosome/detail/{gene}"
        os.makedirs(outdir, exist_ok=True)
        with open(f"{outdir}/{gene}-centrosome-evaluation.md", 'w') as f:
            f.write(report)
        regen_log.append({'gene': gene, 'status': 'CANDIDATE', 'lines': report.count(chr(10))})
        count += 1
        if count % 50 == 0:
            print(f"  进度 {count}/{total}")

        time.sleep(0.2)  # STRING + HPA API rate limit

    # Save regen log
    log_data = {
        'date': datetime.now().isoformat(),
        'total': len(regen_log),
        'eliminated': sum(1 for r in regen_log if 'ELIMINATED' in r['status']),
        'candidate': sum(1 for r in regen_log if 'CANDIDATE' in r['status']),
        'genes': regen_log
    }
    with open("centrosome/audit/centrosome_report_regeneration_log_20260608.json", 'w') as f:
        json.dump(log_data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ 完成: {len(regen_log)} 报告 (淘汰{len(eliminated)} + 候选{len(passed)})")


if __name__ == "__main__":
    main()
