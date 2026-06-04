#!/usr/bin/env python3
"""V2: Improved report generator with proper scoring and data."""
import json, os, sys, urllib.request, time, glob, re

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")

def score_nuclear(locs, func_text, name_text):
    """Score nuclear localization. Returns (score, evidence)."""
    if not locs:
        return 0, "无亚细胞定位注释"

    loc_str = ";".join(locs).lower()
    func = (func_text or "").lower()
    name = (name_text or "").lower()

    has_nucleus = any("nucleus" in l.lower() for l in locs)
    has_cytoplasm = any("cytoplasm" in l.lower() for l in locs)
    has_cytoskeleton = any("cytoskeleton" in l.lower() for l in locs)
    has_secreted = any("secret" in l.lower() for l in locs)
    has_membrane = any("membrane" in l.lower() and "nuclear" not in l.lower() for l in locs)
    has_centrosome = any("centrosome" in l.lower() for l in locs)

    # Check for transcription factor / DNA binding protein
    tf_keywords = ["transcription factor", "homeobox", "homeodomain", "dna-binding",
                   "dna binding", "transcriptional repressor", "transcriptional activator",
                   "chromatin", "histone", "doublesex", "dachshund", "dorsal root ganglia homeobox"]
    is_tf = any(kw in (func + " " + name) for kw in tf_keywords)

    # Pure nuclear proteins (no cytoplasmic annotation)
    if has_nucleus and not has_cytoplasm:
        if is_tf:
            return 9, "UniProt Nucleus (唯一注释) + 转录因子/同源盒/DNA结合蛋白 — 高可信度核定位"
        return 7, "UniProt Nucleus (唯一注释)"

    # Nuclear + cytoplasmic dual localization
    if has_nucleus and has_cytoplasm:
        if is_tf:
            return 7, "UniProt Nucleus+Cytoplasm, 转录因子功能提示核为主定位"
        if has_cytoskeleton or has_centrosome or has_membrane:
            return 4, "UniProt Nucleus+胞质+其他区室, 非特异核定位"
        return 4, "UniProt Nucleus+Cytoplasm (核质双分布)"

    # Non-nuclear
    if has_cytoskeleton:
        return 0, "Cytoskeleton — 非核蛋白"
    if has_secreted:
        return 0, "Secreted — 非核蛋白"
    if has_cytoplasm and not has_nucleus:
        return 0, "Cytoplasm only — 非核蛋白"

    return 0, "无核定位证据"

def score_size(length):
    if length == 0: return 5, "未知大小"
    if 200 <= length <= 800: return 10, f"{length} aa (200–800 aa, 适宜生化实验)"
    elif 100 <= length < 200: return 8, f"{length} aa (100–200 aa)"
    elif 800 < length <= 1200: return 8, f"{length} aa (800–1200 aa)"
    elif 50 <= length < 100: return 5, f"{length} aa (50–100 aa)"
    elif 1200 < length <= 2000: return 5, f"{length} aa (1200–2000 aa)"
    elif length < 50: return 2, f"{length} aa (<50 aa)"
    elif 2000 < length <= 3000: return 2, f"{length} aa (2000–3000 aa)"
    else: return 0, f"{length} aa (>3000 aa)"

def score_domain(uniprot_data, func_text, pubmed_novel):
    domains = uniprot_data.get("domains", [])
    func = (func_text or "").lower()
    name = (uniprot_data.get("raw_name", "") or uniprot_data.get("name", "")).lower()

    full_text = func + " " + name + " " + ";".join(domains).lower()

    # Homeobox/DNA binding domains
    homeobox_kw = ["homeobox", "homeodomain"]
    dm_domain_kw = ["dm domain", "doublesex", "mab-3", "dmrt"]
    dach_kw = ["dachshund"]
    double_homeobox_kw = ["double homeobox"]

    if any(kw in full_text for kw in double_homeobox_kw):
        return 10, "双同源盒结构域 (Double homeobox) — 明确的DNA结合域"
    if any(kw in full_text for kw in homeobox_kw):
        return 10, f"同源盒结构域 (Homeobox) — 经典DNA结合/转录因子域"
    if any(kw in full_text for kw in dm_domain_kw):
        return 10, "DM DNA结合结构域 (DMRT家族) — 转录因子"
    if any(kw in full_text for kw in dach_kw):
        return 9, "Dachshund结构域 — 转录共抑制因子，含DNA结合能力"

    # Other chromatin domains
    chromatin_kw = ["zinc finger", "c2h2", "bromodomain", "chromodomain", "phd", "sant",
                    "tudor", "pwwp", "set domain", "jmjc", "bzip", "bhlh", "forkhead",
                    "at-hook", "hmg-box", "t-box", "mads-box", "myb", "cxxc"]
    if any(kw in full_text for kw in chromatin_kw):
        return 8, f"含chromatin/DNA相关结构域"

    # Nucleic acid binding
    na_kw = ["nucleic acid binding", "rna binding", "dna binding", "rna-binding", "dna-binding"]
    if any(kw in full_text for kw in na_kw):
        return 7, "核酸结合蛋白 (nucleic acid binding)"

    if pubmed_novel <= 50:
        return 7, "新颖蛋白 (PubMed≤50) — 无注释域基线, 可能存在新域"
    elif pubmed_novel <= 100:
        return 7, "PubMed≤100 — 无注释域基线"
    return 5, "无注释染色质调控结构域"

def score_structure(alphafold_data, pdb_list, pubmed_novel):
    pdbs = [p for p in (pdb_list or []) if p]
    af = alphafold_data or {}
    plddt_m = af.get("plddt_mean")
    plddt70 = af.get("plddt_gt70")

    has_af = plddt_m is not None
    has_pdb = len(pdbs) > 0

    if has_pdb and has_af and plddt_m and plddt_m > 70:
        return 10, f"PDB实验结构 ({len(pdbs)}条目) + AlphaFold高质量 (pLDDT={plddt_m})"
    elif has_pdb:
        if len(pdbs) >= 3:
            return 10, f"PDB实验结构 ({len(pdbs)}条目) — 实验验证"
        return 9, f"PDB实验结构 ({len(pdbs)}条目)"
    elif has_af and plddt_m:
        if plddt_m > 80:
            return 8, f"AlphaFold高质量 (pLDDT={plddt_m}, >70%={plddt70}%)"
        elif plddt_m > 65:
            return 7, f"AlphaFold中等 (pLDDT={plddt_m})"
        else:
            return 6, f"AlphaFold较低 (pLDDT={plddt_m}), 新颖蛋白正常"
    else:
        return 6, "新颖蛋白 (PubMed≤100) — 无结构基线, 不扣分"

def parse_intact_partners(intact_list, gene):
    """Parse IntAct data to extract meaningful partner info."""
    physical_methods = ["coimmunoprecipitation", "pull down", "two hybrid",
                        "anti tag", "anti bait", "cross-link"]
    results = []
    seen = set()
    for i in intact_list:
        method = i.get("method", "").lower()
        is_physical = any(m in method for m in physical_methods)
        if not is_physical:
            continue
        a = i.get("a", "").replace("uniprotkb:", "")
        b = i.get("b", "").replace("uniprotkb:", "")
        pmid_raw = i.get("pmid", "")
        type_info = i.get("type", "")

        # Extract PMID
        pmid_match = re.search(r'pubmed:(\d+)', type_info)
        pmid = pmid_match.group(1) if pmid_match else (pmid_raw if pmid_raw.isdigit() else "-")

        # Find the partner (not the query gene)
        partner_a = a.split("-")[0]
        partner_b = b.split("-")[0]
        if gene.upper() in partner_a.upper():
            partner = partner_b
        else:
            partner = partner_a

        # Simplify method
        method_clean = method.replace('psi-mi:"', '').replace('"mi:', '').replace('"', '')
        for tag in ['psi-mi:', '"(', ')"']:
            method_clean = method_clean.replace(tag, '')
        # Extract method name
        m2 = re.search(r'\(([^)]+)\)', method_clean)
        if m2:
            method_clean = m2.group(1)

        if partner and partner not in seen:
            seen.add(partner)
            results.append((partner, method_clean, pmid))
    return results

def determine_subloc(nuc_score, locs, func_text):
    if nuc_score <= 3:
        return "rejected"
    loc_str = ";".join(locs).lower()
    if "nucleolus" in loc_str:
        return "nucleolus"
    if "speckle" in loc_str:
        return "nuclear-speckle"
    if "nuclear body" in loc_str or "pml body" in loc_str or "cajal" in loc_str:
        return "nuclear-body"
    if "chromatin" in loc_str or "chromosome" in loc_str or "centromere" in loc_str or "kinetochore" in loc_str:
        return "chromatin"
    if "nuclear envelope" in loc_str or "lamina" in loc_str:
        return "nuclear-envelope"
    if "cytoplasm" in loc_str:
        return "nucleus-cytoplasm"
    return "nucleoplasm"

def generate_report(gene, data):
    u = data.get("uniprot", {})
    pubmed = data["pubmed_count"]
    nov_score = data["novelty_score"]
    nov_label = data["novelty_label"]
    intact = data.get("intact", [])
    string = data.get("string", [])
    af = data.get("alphafold", {})

    locs = u.get("locs", [])
    func_text = " ".join(u.get("funcs", [""]))
    name = u.get("name", gene)
    name_raw = u.get("raw_name", name)
    length = u.get("len", 0)
    acc = u.get("acc", "?")
    genes = u.get("genes", [gene])
    aliases = " | ".join(genes) if genes else gene
    pdbs = u.get("pdbs", [])
    domains = u.get("domains", [])
    gocc = u.get("gocc", [])

    # Scoring
    nuc_score, nuc_evidence = score_nuclear(locs, func_text, name_raw)
    size_score, size_evidence = score_size(length)
    dom_score, dom_evidence = score_domain(u, func_text, pubmed)
    struct_score, struct_evidence = score_structure(af, pdbs, pubmed)

    # PPI scoring
    physical_partners = parse_intact_partners(intact, gene)
    hi_string = [s for s in string if s.get("score", 0) > 0.5]
    chromatin_kw = ["transcription", "chromatin", "histone", "methyltransferase",
                    "acetyltransferase", "deacetylase", "hdac", "dna binding",
                    "homeobox", "chromodomain", "bromodomain", "setd", "kmt", "kdm"]

    reg_count = 0
    for s in hi_string:
        if any(kw in s.get("partner", "").lower() for kw in chromatin_kw):
            reg_count += 1

    if physical_partners:
        if len(physical_partners) >= 3:
            ppi_score = 6
            ppi_evidence = f"IntAct实验物理互作 ({len(physical_partners)}条co-IP/pull-down)"
        else:
            ppi_score = 4
            ppi_evidence = f"少量IntAct物理互作 ({len(physical_partners)}条)"
    elif hi_string:
        ppi_score = 4
        ppi_evidence = f"STRING预测互作 ({len(hi_string)}条>0.5)"
    elif string:
        ppi_score = 3
        ppi_evidence = f"低置信度STRING关联 ({len(string)}条)"
    else:
        ppi_score = 1
        ppi_evidence = "PPI数据极稀缺"

    # Cross-validation bonus
    cross_score = 0.0
    cross_details = []
    has_nucleus = any("nucleus" in l.lower() for l in locs)

    # TF + Nuclear = cross-validation
    is_tf = any(kw in func_text.lower() + name_raw.lower() for kw in
                ["transcription factor", "homeobox", "homeodomain", "dna-binding",
                 "doublesex", "dachshund", "transcriptional"])
    if has_nucleus and is_tf:
        cross_score += 1.0
        cross_details.append("核定位+转录因子功能一致 (+1.0)")

    if pdbs and len([p for p in pdbs if p]) >= 3:
        cross_score += 1.0
        cross_details.append(f"PDB多条目实验结构确认 (+1.0)")
    elif pdbs and len([p for p in pdbs if p]) > 0:
        cross_score += 0.5
        cross_details.append(f"PDB实验结构确认 (+0.5)")

    if physical_partners and len(physical_partners) >= 3:
        cross_score += 0.5
        cross_details.append(f"IntAct实验互作确认 (+0.5)")

    cross_str = f"+{cross_score}" if cross_score > 0 else "0"
    if isinstance(cross_score, float) and cross_score == int(cross_score):
        cross_str = f"+{int(cross_score)}"

    raw = (nuc_score * 4) + (size_score * 1) + (nov_score * 5) + (struct_score * 3) + (dom_score * 2) + (ppi_score * 3) + cross_score
    norm = round(raw / 1.83, 1)

    subloc = determine_subloc(nuc_score, locs, func_text)

    if nuc_score <= 3 or pubmed > 100:
        subloc = "rejected"
        status = "rejected"
    else:
        status = "scored"

    out_dir = os.path.join(DETAIL, subloc, gene)
    os.makedirs(out_dir, exist_ok=True)

    # PAE image
    pae_png = os.path.join(out_dir, f"{gene}-PAE.png")
    pae_embed = ""
    if os.path.exists(pae_png) and os.path.getsize(pae_png) > 500:
        pae_embed = f"\n![[Projects/TEreg-finding/protein-interested/detail/{subloc}/{gene}/{gene}-PAE.png]]\n"

    # IF images
    if_dir = os.path.join(out_dir, "IF_images")
    if_jpgs = (glob.glob(os.path.join(if_dir, "*.jpg")) if os.path.exists(if_dir) else [])
    if_embed = ""
    if if_jpgs:
        for jpg in sorted(if_jpgs)[:2]:
            fname = os.path.basename(jpg)
            cell_line = fname.replace(".jpg", "").replace("_red_green", "").replace("_", " ")
            if_embed += f"\n![[Projects/TEreg-finding/protein-interested/detail/{subloc}/{gene}/IF_images/{fname}|{cell_line}]]\n"
    else:
        if_embed = "\n暂无数据 (Pending cell analysis)，核定位基于 UniProt + GO 注释。\n"

    if status == "rejected":
        reason = f"核定位 ≤3 分 ({nuc_score}/10)" if nuc_score <= 3 else f"PubMed >100 ({pubmed}篇)"
        reason_detail = nuc_evidence if nuc_score <= 3 else f"PubMed={pubmed}>100, 研究过于拥挤"

        report = f"""---
type: protein-evaluation
gene: "{gene}"
date: 2026-05-29
tags: [protein-scout, rejected]
status: rejected
---

## {gene} 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene} / {aliases} |
| 蛋白大小 | {length} aa |
| UniProt ID | {acc} |
| 蛋白名称 | {name} |
| 评估日期 | 2026-05-29 |

### 2. 淘汰原因

**{reason}**

{reason_detail}

### 3. 基本数据

- PubMed 总数: {pubmed} 篇
- UniProt 定位: {"; ".join(locs) if locs else "无注释"}
- 蛋白功能: {func_text[:200] if func_text else "未知"}

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/{acc}
"""
        with open(os.path.join(out_dir, f"{gene}-evaluation.md"), 'w') as f:
            f.write(report)
        return subloc, gene, nuc_score, size_score, nov_score, struct_score, dom_score, ppi_score, cross_score, norm

    # Build report sections
    locs_str = "; ".join(locs[:5]) if locs else "无注释"

    # IntAct table
    intact_rows = ""
    for partner, method, pmid in physical_partners[:6]:
        intact_rows += f"| {partner[:30]} | {method[:35]} | {pmid[:12]} | - | - |\n"
    if not intact_rows:
        intact_rows = "| 无实验验证物理互作 | - | - | - | - |\n"

    # STRING table
    hi_str = [s for s in string if s.get("score", 0) > 0.4][:8]
    string_rows = ""
    for s in hi_str:
        partner = s.get("partner", "")
        sc = s.get("score", 0)
        exp_s = s.get("exp", 0)
        tag = "调控" if any(kw in partner.lower() for kw in chromatin_kw) else "-"
        string_rows += f"| {partner[:25]} | {sc} | - | {tag} |\n"
    if not string_rows:
        string_rows = "| 无高置信度STRING互作 | - | - | - |\n"

    gocc_text = "\n".join(f"- {g}" for g in gocc[:8]) if gocc else "- 无已知复合体注释"

    plddt_m_str = str(af.get("plddt_mean", "N/A"))
    plddt70_str = str(af.get("plddt_gt70", "N/A"))
    plddt90_str = str(af.get("plddt_gt90", "N/A"))
    pdbs_str = "; ".join(pdbs) if pdbs else "无"

    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## {gene} 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene} / {aliases} |
| 蛋白大小 | {length} aa |
| UniProt ID | {acc} |
| 蛋白名称 | {name_raw} |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | {nuc_score}/10 | ×4 | {nuc_score*4} | {nuc_evidence[:90]} |
| 📏 蛋白大小 | {size_score}/10 | ×1 | {size_score} | {size_evidence} |
| 🆕 研究新颖性 | {nov_score}/10 | ×5 | {nov_score*5} | PubMed={pubmed}篇 ({nov_label}) |
| 🏗️ 三维结构 | {struct_score}/10 | ×3 | {struct_score*3} | {struct_evidence[:90]} |
| 🧬 调控结构域 | {dom_score}/10 | ×2 | {dom_score*2} | {dom_evidence[:90]} |
| 🔗 PPI 网络 | {ppi_score}/10 | ×3 | {ppi_score*3} | {ppi_evidence[:90]} |
| ➕ 互证加分 | — | max +3 | {cross_str} | {'; '.join(cross_details) if cross_details else '无额外互证'} |
| **原始总分** | | | **{raw} / 183** | |
| **归一化总分** | | | **{norm} / 100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | {locs_str} | TrEMBL/Swiss-Prot |
| Protein Atlas (IF) | 暂无数据 | Pending cell analysis |

{'(暂无IF图片)' if not if_embed.strip() else if_embed}

**结论**: {nuc_evidence}

#### 3.2 蛋白大小评估

{length} aa 蛋白。**评价**: {size_evidence}

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | {pubmed} |
| 新颖性分级 | {nov_label} |

**评价**: PubMed 共 {pubmed} 篇文献，属于**{nov_label}**。研究空间充足，适合作为创新课题。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | {plddt_m_str} |
| 有序区域 (pLDDT>70) 占比 | {plddt70_str}% |
| 高置信度 (pLDDT>90) 占比 | {plddt90_str}% |
| 可用 PDB 条目 | {pdbs_str} |
{pae_embed}
**评价**: {struct_evidence}

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| UniProt | {'; '.join(domains[:5]) if domains else '无注释结构域'} |
| GO Molecular Function | {func_text[:150] if func_text else '无'} |

**染色质调控潜力分析**: {dom_evidence}

#### 3.6 PPI 网络

**实验验证互作** (IntAct physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
{intact_rows}
**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
{string_rows}
**已知复合体成员** (GO Cellular Component):
{gocc_text}

**评价**: {ppi_evidence}

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | pLDDT={plddt_m_str}, PDB:{len(pdbs)}条目 | {'一致' if pdbs else '无实验结构'} |
| 结构域 | UniProt | {len(domains)}个注释域 | {'一致' if domains else 'N/A'} |
| PPI | STRING + IntAct | IntAct:{len(intact)}, STRING:{len(string)} | 一致 |
| 定位 | UniProt | {'Nucleus' if has_nucleus else 'Non-nuclear'} | {'是' if has_nucleus else '否'} |

**互证加分明细**:
{chr(10).join(f'- {d}' for d in cross_details) if cross_details else '- 无额外互证加分'}
**总分**: {cross_str} / max +3

### 4. 总体评价

**推荐等级**: {'★' * min(5, max(1, int(norm/20 + 0.5)))} ({norm}/100)

**核心优势**:
1. {nov_label} (PubMed={pubmed}篇)
2. {nuc_evidence[:100]}
3. {dom_evidence[:100]}

**风险/不确定性**:
1. 无 Protein Atlas IF 实验验证
2. 无 AlphaFold 高质量结构或结构待验证

**下一步建议**:
- [ ] Protein Atlas IF 实验验证核定位
- [ ] AlphaFold 结构预测分析
- [ ] Co-IP/MS 验证PPI网络

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/{acc}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term={gene}
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
"""

    with open(os.path.join(out_dir, f"{gene}-evaluation.md"), 'w') as f:
        f.write(report)

    return subloc, gene, nuc_score, size_score, nov_score, struct_score, dom_score, ppi_score, cross_score, norm

def main():
    with open(os.path.join(BASE, "batch_results.json")) as f:
        content = f.read()
    idx = content.find('{')
    if idx > 0:
        content = content[idx:]
    data = json.loads(content)

    results = []
    for gene in sorted(data.keys()):
        print(f"Generating: {gene}...", file=sys.stderr)
        try:
            r = generate_report(gene, data[gene])
            results.append(r)
        except Exception as e:
            print(f"  ERROR: {gene}: {e}", file=sys.stderr)
            import traceback; traceback.print_exc()

    scored = [r for r in results if r[0] != "rejected"]
    rejected = [r for r in results if r[0] == "rejected"]

    print(f"\n=== SCORED: {len(scored)} ===")
    for cat, gene, nuc, sz, nov, struct, dom, ppi, cross, norm in sorted(scored, key=lambda x: -x[9]):
        print(f"  [{cat}] {gene}: {norm} (nuc={nuc}, nov={nov}, struct={struct}, dom={dom}, ppi={ppi}, cross={cross})")

    print(f"\n=== REJECTED: {len(rejected)} ===")
    for cat, gene, nuc, sz, nov, struct, dom, ppi, cross, norm in rejected:
        print(f"  {gene}: nuc={nuc}, PubMed={data[gene]['pubmed_count']}")

if __name__ == "__main__":
    main()
