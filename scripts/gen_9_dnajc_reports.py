#!/usr/bin/env python3
"""Generate /180 reports for 9 DNAJC genes from harvest packets.
Rules: Nuclear <=3 -> REJECTED. PubMed >100 -> REJECTED. Skip if report exists."""

import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")
VAULT_PREFIX = "Projects/TEreg-finding/protein-interested/detail"
PACKET_DIR = "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets"
TODAY = "2026-06-03"

GENES = [
    "DNAJC1", "DNAJC11", "DNAJC13", "DNAJC16", "DNAJC17",
    "DNAJC19", "DNAJC2", "DNAJC21", "DNAJC22",
]

# ============================================================
# SCORING FUNCTIONS (from gen_113_reports.py)
# ============================================================

def novelty_score(pubmed_strict):
    if pubmed_strict <= 20: return 10
    if pubmed_strict <= 40: return 8
    if pubmed_strict <= 60: return 6
    if pubmed_strict <= 80: return 4
    if pubmed_strict <= 100: return 2
    return 0

def size_score(aa):
    if 200 <= aa <= 800: return 10
    if (100 <= aa < 200) or (800 < aa <= 1200): return 8
    if (50 <= aa < 100) or (1200 < aa <= 2000): return 5
    if aa < 50 or (2000 < aa <= 3000): return 2
    return 0

def struct_score(pdb_ids, plddt):
    n_pdb = len(pdb_ids) if pdb_ids else 0
    if n_pdb >= 5 and plddt >= 70: return 10
    if n_pdb >= 2 and plddt >= 70: return 9
    if n_pdb >= 1 and plddt >= 70: return 8
    if plddt >= 85: return 8
    if plddt >= 70: return 7
    if plddt >= 50: return 6
    if plddt < 40: return 4
    return 6

def domain_score(domains_text, plddt):
    chromatin_kw = ["bromo", "chromo", "phd", "sant", "tudor", "mbt", "pwwp",
                    "zinc finger", "homeobox", "homeodomain", "hmg", "forkhead",
                    "bzip", "bhlh", "at-hook", "myb", "cxxc", "swi/snf", "iswi",
                    "histone", "chromatin", "dna-binding", "nucleic acid binding"]
    text = domains_text.lower()
    has_chromatin = any(kw in text for kw in chromatin_kw)
    domain_count = text.count("ipr") + text.count("pf")
    if has_chromatin and domain_count >= 3: return 10
    if has_chromatin or (domain_count >= 2 and plddt >= 80): return 8
    if domain_count > 0: return 7
    if plddt >= 70: return 6
    if plddt >= 50: return 5
    return 4

def ppi_score(string_n, intact_n, string_partners):
    reg_keywords = ["chromatin", "transcription", "histone", "dna", "rna polymer",
                    "helicase", "splicing", "rna", "trna", "rrna", "nucleolar",
                    "ribosome", "nucleosome", "mediator", "coactivator", "corepressor",
                    "deacetylase", "acetyltransferase", "methyltransferase",
                    "kinetochore", "centromere", "condensin", "cohesin", "smc",
                    "origin recognition", "replication factor"]
    if not string_partners:
        return 2
    reg_count = 0
    for p in string_partners[:20]:
        name = p.get("partner", "").lower()
        if any(kw in name for kw in reg_keywords):
            reg_count += 1
    reg_ratio = reg_count / min(len(string_partners), 20)
    has_physical = intact_n > 0
    has_string = string_n > 0
    if has_physical and reg_ratio > 0.4 and string_n >= 10: return 10
    if has_physical and reg_ratio > 0.2 and string_n >= 5: return 8
    if has_physical and reg_ratio > 0.3: return 6
    if has_string and reg_ratio > 0.2: return 4
    if has_string: return 3
    return 2

def cross_validation(pdb_ids, plddt, uni_loc, hpa_loc, go_cc, string_n, intact_n, domains, has_uni):
    pts = 0
    if pdb_ids and plddt > 0: pts += 0.5
    has_multi_nuc = 0
    if has_uni and uni_loc: has_multi_nuc += 1
    if hpa_loc: has_multi_nuc += 1
    if go_cc: has_multi_nuc += 1
    if has_multi_nuc >= 2: pts += 0.5
    if string_n > 0 and intact_n > 0: pts += 0.5
    if domains and "暂无" not in domains and plddt > 70: pts += 0.5
    if len(pdb_ids) >= 3: pts += 1.0
    return min(pts, 3.0)

def nuclear_score(uni_subcell, hpa_main, hpa_addl, hpa_rel, go_cc_terms, has_uni):
    nucleolus_kw = ["nucleol"]
    nucleus_kw = ["nucleus", "nucleoplasm", "nucleoli", "nuclear", "nucleolus"]
    non_nuc_kw = ["mitochondri", "cytosol", "cytoplasm", "golgi", "endoplasmic reticulum",
                  "membrane", "secreted", "cytoskeleton", "centrosome", "spindle",
                  "microtubule", "vesicle", "kinocilium", "lamellipodium",
                  "synapse", "postsynaptic", "cilia", "flagella",
                  "cell projection", "plasma membrane", "extracellular",
                  "acrosome", "principal piece"]

    hpa_nuc = False
    hpa_non = False
    hpa_main_text = " ".join(hpa_main).lower()
    hpa_addl_text = " ".join(hpa_addl).lower()

    if any(kw in hpa_main_text for kw in nucleolus_kw):
        hpa_nuc = True
    elif any(kw in hpa_main_text for kw in nucleus_kw):
        hpa_nuc = True
    if any(kw in hpa_addl_text for kw in nucleus_kw) and not any(kw in hpa_main_text for kw in nucleus_kw):
        hpa_nuc = True
    if any(kw in hpa_main_text for kw in non_nuc_kw):
        hpa_non = True

    uni_nuc = False
    uni_non = False
    if has_uni:
        uni_text = " ".join(uni_subcell).lower()
        if any(kw in uni_text for kw in nucleus_kw):
            uni_nuc = True
        if any(kw in uni_text for kw in non_nuc_kw):
            uni_non = True

    go_nuc = False
    go_non = False
    if go_cc_terms:
        go_terms = []
        for cc in go_cc_terms:
            if isinstance(cc, dict):
                go_terms.append(cc.get("term", ""))
            else:
                go_terms.append(str(cc))
        go_text = " ".join(go_terms).lower()
        if any(kw in go_text for kw in nucleus_kw):
            go_nuc = True
        if any(kw in go_text for kw in non_nuc_kw):
            go_non = True

    nuc_sources = sum([hpa_nuc, uni_nuc, go_nuc])
    non_sources = sum([hpa_non, uni_non, go_non])

    if nuc_sources == 0 and non_sources == 0:
        return 3
    if nuc_sources >= 2 and non_sources == 0:
        return 9 if nuc_sources >= 3 else 8
    if nuc_sources >= 2 and non_sources >= 1:
        return 7
    if nuc_sources == 1 and non_sources == 0:
        if hpa_nuc and hpa_rel in ["Approved", "Enhanced"]:
            return 7
        return 5
    if hpa_non and not hpa_nuc and (uni_nuc or go_nuc):
        if go_nuc and not uni_non:
            return 5
        return 4
    if non_sources >= 1 and nuc_sources == 0:
        if not uni_nuc and not hpa_nuc and not go_nuc:
            return 0
        return 2
    if nuc_sources >= 1 and non_sources >= 1:
        if nuc_sources >= non_sources:
            return 6
        return 4
    return 3


# ============================================================
# REPORT WRITING
# ============================================================

def load_packet(gene):
    path = os.path.join(PACKET_DIR, f"{gene}.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)

def write_rejected(gene, reason, uni_result, pubmed_result):
    cat = "rejected"
    rd = os.path.join(DETAIL, cat, gene)
    os.makedirs(rd, exist_ok=True)

    acc = uni_result.get("accession", gene) if uni_result else gene
    length = uni_result.get("length_aa", 0) if uni_result else 0
    aliases = ", ".join((uni_result.get("aliases") or [])[:4]) if uni_result else gene
    name = uni_result.get("protein_name", "") if uni_result else ""
    subcell = "; ".join([s.get("location", "") for s in (uni_result.get("subcellular_locations") or [])][:5]) if uni_result else "N/A"
    go_cc_str = "; ".join([g.get("term", "") for g in (uni_result.get("go_cc") or [])][:5]) if uni_result else "N/A"
    pm = pubmed_result.get("strict_count", "N/A") if pubmed_result else "N/A"

    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: {TODAY}
tags: [protein-scout, rejected]
status: rejected
---

## {gene} 核蛋白评估报告（已淘汰）

### 1. 基本信息
| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene} / {aliases} |
| 蛋白全名 | {name} |
| 蛋白大小 | {length} aa |
| UniProt ID | {acc} |
| 评估日期 | {TODAY} |

### 2. 淘汰原因

**淘汰理由**: {reason}

| 维度 | 证据 |
|------|------|
| UniProt 亚细胞定位 | {subcell} |
| GO Cellular Component | {go_cc_str} |
| PubMed strict count | {pm} |

**结论**: {reason}，不进入评分流程。

### 3. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/{acc}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22{gene}%22%5BTitle/Abstract%5D
"""
    with open(os.path.join(rd, f"{gene}-evaluation.md"), "w") as f:
        f.write(report)
    print(f"  REJECTED: {gene} ({reason})")

def write_scored(gene, cat, nuc_score, nuc_evidence, uni_result, af_result, pubmed_result, hpa_data, string_result, intact_result, af_found):
    rd = os.path.join(DETAIL, cat, gene)
    os.makedirs(rd, exist_ok=True)

    acc = uni_result.get("accession", gene) if uni_result else gene
    length = uni_result.get("length_aa", 0) if uni_result else 0
    mass = uni_result.get("mass_kda", 0) if uni_result else 0
    aliases = ", ".join((uni_result.get("aliases") or [])[:3]) if uni_result else gene
    name = uni_result.get("protein_name", gene) if uni_result else gene
    func = "; ".join((uni_result.get("function") or [])[:2]) if uni_result else "N/A"
    subcell = [s.get("location", "") for s in (uni_result.get("subcellular_locations") or [])] if uni_result else []
    go_cc = uni_result.get("go_cc", []) if uni_result else []
    pdb_ids = [p.get("id", "") for p in (uni_result.get("pdb") or [])]
    interpro = uni_result.get("interpro", [])
    pfam = uni_result.get("pfam", [])

    pm_strict = pubmed_result.get("strict_count", 0) if pubmed_result else 0
    pm_broad = pubmed_result.get("broad_count", 0) if pubmed_result else 0
    key_papers = pubmed_result.get("key_papers", []) if pubmed_result else []

    plddt_stats = af_result.get("plddt_stats", {}) if af_result else {}
    plddt = plddt_stats.get("mean_plddt", 0)
    gt90 = plddt_stats.get("pct_gt_90", 0)
    r70_90 = plddt_stats.get("pct_70_90", 0)
    r50_70 = plddt_stats.get("pct_50_70", 0)
    lt50 = plddt_stats.get("pct_lt_50", 0)
    af_ver = af_result.get("latest_version", 4) if af_result else 4

    hpa_main = hpa_data.get("subcellular_main_location", []) if hpa_data else []
    hpa_addl = hpa_data.get("subcellular_additional_location", []) if hpa_data else []
    hpa_rel = hpa_data.get("reliability_if", "No data") if hpa_data else "No data"
    hpa_all = hpa_data.get("subcellular_location", []) if hpa_data else []

    string_partners = string_result or []
    intact_partners = intact_result or []

    # Calculate scores
    sz = size_score(length)
    nov = novelty_score(pm_strict)
    struct = struct_score(pdb_ids, plddt)

    # Domain score
    dom_text = "; ".join([str(d.get('name', d.get('id', ''))) for d in interpro]) if interpro else ""
    dom = domain_score(dom_text, plddt)

    ppi = ppi_score(len(string_partners), len(intact_partners), string_partners)

    cross = cross_validation(pdb_ids, plddt, subcell, hpa_all if hpa_all else hpa_main, go_cc,
                             len(string_partners), len(intact_partners), dom_text, bool(uni_result))

    raw = nuc_score*4 + sz*1 + nov*5 + struct*3 + dom*2 + ppi*3 + cross
    norm = round(raw / 1.83, 1)

    # Build strings
    subcell_str = "; ".join(subcell[:5]) if subcell else "无UniProt注释"
    hpa_str = "; ".join(hpa_all[:8]) if hpa_all else "暂无HPA数据"
    if not hpa_all and hpa_main:
        hpa_str = "; ".join(hpa_main[:5])

    go_cc_str = "; ".join([g.get("term", g) if isinstance(g, dict) else str(g) for g in go_cc[:8]]) if go_cc else "无"
    pdb_str = ", ".join(pdb_ids[:10]) if pdb_ids else "无"

    # Size desc
    if sz >= 10: sz_desc = f"{length} aa / ~{mass} kDa (200-800, 最适实验大小)"
    elif sz >= 8: sz_desc = f"{length} aa / ~{mass} kDa (可操作范围)"
    elif sz >= 5: sz_desc = f"{length} aa / ~{mass} kDa (偏大/偏小)"
    else: sz_desc = f"{length} aa / ~{mass} kDa (大小不理想)"

    # Novelty desc
    if nov >= 10: nov_desc = f"极度新颖 (PubMed strict={pm_strict})"
    elif nov >= 8: nov_desc = f"非常新颖 (PubMed strict={pm_strict})"
    elif nov >= 6: nov_desc = f"较新颖 (PubMed strict={pm_strict})"
    else: nov_desc = f"有研究基础 (PubMed strict={pm_strict})"

    # Struct desc
    if struct >= 9: struct_desc = f"PDB实验结构+高质量AF预测 (pLDDT={plddt})"
    elif struct >= 8: struct_desc = f"AlphaFold高质量预测 (pLDDT={plddt}, pct>90={gt90}%)"
    elif struct >= 7: struct_desc = f"AlphaFold中等质量 (pLDDT={plddt}, ordered={gt90+r70_90:.0f}%)"
    else: struct_desc = f"AlphaFold预测 (pLDDT={plddt}, ordered={gt90+r70_90:.0f}%)"

    # Domain desc
    if dom >= 8: dom_desc = f"含染色质/DNA相关域: {dom_text[:100]}"
    elif dom >= 7: dom_desc = f"注释域: {dom_text[:100] or '暂无详细注释'}"
    else: dom_desc = f"结构域有限 ({dom_text[:80] or '无注释'})，新颖蛋白基线"

    # PPI desc
    str_top5 = sorted(string_partners, key=lambda x: x.get("score", 0), reverse=True)[:5]
    # Count regulatory partners
    reg_kw = ["chromatin", "transcription", "histone", "dna", "rna polymer", "helicase",
              "splicing", "rna", "nucleolar", "ribosome", "nucleosome", "mediator",
              "deacetylase", "acetyltransferase", "methyltransferase", "kinetochore",
              "centromere", "condensin", "cohesin"]
    reg_count = 0
    for p in string_partners:
        if any(kw in p.get("partner", "").lower() for kw in reg_kw):
            reg_count += 1
    reg_ratio = reg_count / max(len(string_partners), 1)

    # HPA IF image status
    if_image_status = hpa_data.get("image_status", "no_image") if hpa_data else "no_data"
    hpa_if_url = hpa_data.get("hpa_subcellular_url", "") if hpa_data else ""

    # Build report
    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: {TODAY}
tags: [protein-scout, evaluation, {cat}]
status: scored
---

## {gene} 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene} / {aliases} |
| 蛋白大小 | {length} aa / {mass} kDa |
| UniProt ID | {acc} |
| 蛋白全名 | {name} |
| 子定位分类 | {cat} |
| 评估日期 | {TODAY} |
| 功能描述 | {func[:200]} |

**HPA IF 图像**: {hpa_if_url if hpa_if_url else 'No IF images available for this gene.'}

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | {nuc_score}/10 | x4 | {nuc_score*4} | {nuc_evidence[:80]} |
| 蛋白大小 | {sz}/10 | x1 | {sz} | {sz_desc[:80]} |
| 研究新颖性 | {nov}/10 | x5 | {nov*5} | PubMed strict={pm_strict} |
| 三维结构 | {struct}/10 | x3 | {struct*3} | AlphaFold pLDDT={plddt} (pct>70={gt90+r70_90:.0f}%); PDB: {len(pdb_ids)} entries |
| 调控结构域 | {dom}/10 | x2 | {dom*2} | {dom_text[:60]} |
| PPI 网络 | {ppi}/10 | x3 | {ppi*3} | IntAct {len(intact_partners)} interactions; STRING {len(string_partners)} partners |
| 互证加分 | — | max +3 | {cross} | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **{raw:.1f}/183** | |
| **归一化总分** | | | **{norm}/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | {hpa_str[:80]} | {hpa_rel} |
| UniProt | {subcell_str[:80]} | Swiss-Prot/TrEMBL |

**GO Cellular Component**:
"""
    if go_cc:
        for g in go_cc[:5]:
            t = g.get("term", str(g)) if isinstance(g, dict) else str(g)
            e = g.get("evidence", "") if isinstance(g, dict) else ""
            report += f"- {t}{' (' + e + ')' if e else ''}\n"
    else:
        report += "- 无 GO-CC 注释\n"
    report += f"""
**结论**: {nuc_evidence}

#### 3.2 蛋白大小评估

**评价**: {sz_desc}

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | {pm_strict} |
| PubMed broad count | {pm_broad} |

"""
    if key_papers:
        report += "**关键文献**:\n"
        for pp in key_papers[:3]:
            report += f"- [{pp.get('pmid', '')}] {pp.get('title', '')} ({pp.get('journal', '')}, {pp.get('pubdate', '')})\n"
        report += "\n"

    report += f"""**评价**: {nov_desc}

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v{af_ver} |
| AlphaFold 平均 pLDDT | {plddt} |
| pLDDT > 90 占比 | {gt90}% |
| pLDDT 70-90 占比 | {r70_90}% |
| pLDDT 50-70 占比 | {r50_70}% |
| pLDDT < 50 占比 | {lt50}% |
| 有序区域 (pLDDT>70) 占比 | {gt90+r70_90:.1f}% |
| 可用 PDB 条目 | {pdb_str} |

**评价**: {struct_desc}

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | {dom_text[:200] or '暂无数据'} |

**染色质调控潜力分析**: {dom_desc}

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关? |
|---------|-------|---------|-----------|
"""
    if str_top5:
        for p in str_top5:
            partner = p.get("partner", "?")
            score = p.get("score", 0)
            is_reg = "Yes" if any(kw in partner.lower() for kw in reg_kw) else "—"
            report += f"| {partner} | {score:.3f} | — | {is_reg} |\n"
    else:
        report += "| — | — | — | — |\n"

    # IntAct
    intact_dedup = []
    seen_intact = set()
    for p in intact_partners:
        partner = p.get("partner", "")
        if partner and partner not in seen_intact:
            seen_intact.add(partner)
            intact_dedup.append(p)
        if len(intact_dedup) >= 5:
            break

    report += f"""
**实验验证互作** (IntAct):

| Partner | 方法 | PMID | 功能类别 | 调控相关? |
|---------|------|------|---------|-----------|
"""
    if intact_dedup:
        for p in intact_dedup[:5]:
            partner = p.get("partner", "?")
            method = p.get("method", "—")
            pmid = p.get("pmid", "—")
            is_reg = "Yes" if any(kw in partner.lower() for kw in reg_kw) else "—"
            report += f"| {partner} | {method} | {pmid} | — | {is_reg} |\n"
    else:
        report += "| — | — | — | — | — |\n"

    report += f"""
**已知复合体成员** (GO Cellular Component):
- {go_cc_str}

**PPI 互证分析**:
- STRING + IntAct 共同确认: 待交叉比对
- 仅 STRING 预测: {len(string_partners)} 个伙伴
- 仅 IntAct 实验: {len(intact_partners)} 个互作
- 调控相关比例: {reg_count}/{max(len(string_partners), 1)} ({reg_ratio*100:.0f}%)

**评价**: {ppi_desc()}

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT={plddt} + PDB: {pdb_str} | pLDDT={plddt}, v{af_ver} | {'预测+实验' if pdb_ids else '仅预测'} |
| 定位 | UniProt + HPA | {subcell_str[:50]} / {hpa_str[:50]} | {'一致' if hpa_str and '暂无' not in hpa_str else '待确认'} |
| PPI | STRING + IntAct | {len(string_partners)} + {len(intact_partners)} interactions | {'数据充分' if string_partners and intact_partners else '数据有限'} |

**互证加分**: {cross} / max +3

### 4. 总体评价

**归一化总分**: **{norm}/100**

**核心优势**:
1. {gene} — {name}，{nov_desc}
2. 蛋白大小{length} aa，{sz_desc}

**风险/不确定性**:
1. {'PubMed ' + str(pm_strict) + ' 篇，研究基础有限' if pm_strict <= 50 else '已有一定研究基础'}
2. {'AlphaFold 预测质量一般 (pLDDT=' + str(plddt) + ')' if plddt < 70 and not pdb_ids else '结构数据可接受'}

**下一步建议**:
- [ ] 查阅关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/{acc}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22{gene}%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/{acc}
- STRING: https://string-db.org/cgi/network?identifiers={gene}&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/{gene}
"""

    with open(os.path.join(rd, f"{gene}-evaluation.md"), "w") as f:
        f.write(report)
    print(f"  SCORED: {cat}/{gene} norm={norm} (nuc={nuc_score}, sz={sz}, nov={nov}, struct={struct}, dom={dom}, ppi={ppi})")

def ppi_desc():
    return f"STRING + IntAct analysis"

def get_nuc_evidence_str(nuc_score, uni_subcell, hpa_main, hpa_addl, hpa_rel, go_cc):
    nucleus_kw = ["nucleus", "nucleoplasm", "nucleoli", "nuclear", "nucleolus"]
    non_nuc_kw = ["mitochondri", "cytosol", "cytoplasm", "golgi", "endoplasmic reticulum",
                  "membrane", "cytoskeleton", "centrosome", "microtubule", "vesicle"]

    hpa_text = " ".join(hpa_main + hpa_addl).lower()
    uni_text = " ".join(uni_subcell).lower()

    parts = []
    if any(kw in hpa_text for kw in nucleus_kw):
        parts.append("HPA: nuclear signal detected")
    elif any(kw in hpa_text for kw in non_nuc_kw):
        parts.append("HPA: non-nuclear main signal")
    elif hpa_main:
        parts.append(f"HPA: {', '.join(hpa_main[:2])}")

    if any(kw in uni_text for kw in nucleus_kw):
        parts.append("UniProt: nuclear annotation")
    elif any(kw in uni_text for kw in non_nuc_kw):
        parts.append(f"UniProt: {uni_subcell[0][:30] if uni_subcell else 'no annotation'}")

    if not parts:
        parts.append("No clear nuclear annotation")

    return "; ".join(parts[:2])


# ============================================================
# MAIN
# ============================================================

def main():
    print("=== Generating 9 DNAJC reports ===")
    for gene in GENES:
        # Skip if report already exists
        report_paths = []
        for cat in ["nucleoplasm", "nucleolus", "chromatin", "nucleus-cytoplasm",
                     "nuclear-envelope", "nuclear-speckle", "nuclear-body", "rejected"]:
            p = os.path.join(DETAIL, cat, gene, f"{gene}-evaluation.md")
            if os.path.exists(p):
                report_paths.append(p)

        if report_paths:
            print(f"  SKIP {gene}: report(s) already exist: {', '.join(report_paths)}")
            continue

        # Load harvest packet
        pkt = load_packet(gene)
        if not pkt:
            print(f"  SKIP {gene}: no harvest packet")
            continue

        # Extract data
        uni_raw = pkt.get("uniprot", {})
        uni_data = uni_raw.get("data", {}) if uni_raw.get("ok") else {}
        has_uni = uni_raw.get("ok", False)

        af_raw = pkt.get("alphafold", {})
        af_data = af_raw.get("data", {}) if af_raw.get("ok") else {}
        af_found = af_raw.get("ok", False)

        pm_raw = pkt.get("pubmed", {})
        pm_data = pm_raw.get("data", {}) if pm_raw.get("ok") else {}

        hpa_raw = pkt.get("hpa", {})
        hpa_data = hpa_raw.get("data", {}) if hpa_raw.get("ok") else {}

        str_raw = pkt.get("string", {})
        str_data = str_raw.get("data", []) if str_raw.get("ok") else []

        inta_raw = pkt.get("intact", {})
        inta_data = inta_raw.get("data", []) if inta_raw.get("ok") else []

        # Extract scoring inputs
        uni_subcell = [s.get("location", "") for s in (uni_data.get("subcellular_locations") or [])]
        go_cc = uni_data.get("go_cc", [])
        hpa_main = hpa_data.get("subcellular_main_location", [])
        hpa_addl = hpa_data.get("subcellular_additional_location", [])
        hpa_rel = hpa_data.get("reliability_if", "No data")
        pm_strict = pm_data.get("strict_count", 0)

        # Nuclear score
        nuc = nuclear_score(uni_subcell, hpa_main, hpa_addl, hpa_rel, go_cc, has_uni)
        nuc_evidence = get_nuc_evidence_str(nuc, uni_subcell, hpa_main, hpa_addl, hpa_rel, go_cc)

        # REJECTION RULES
        if nuc <= 3:
            reason = f"核定位评分={nuc}/10，HPA主要定位={'/'.join(hpa_main) if hpa_main else '无数据'}，UniProt={'/'.join(uni_subcell[:3]) if uni_subcell else '无注释'}，非核蛋白"
            write_rejected(gene, reason, uni_data, pm_data)
            continue

        if pm_strict > 100:
            reason = f"PubMed strict count={pm_strict} > 100，研究过热"
            write_rejected(gene, reason, uni_data, pm_data)
            continue

        # Determine category
        hpa_all = hpa_data.get("subcellular_location", [])
        hpa_text = " ".join(hpa_all + hpa_main + hpa_addl).lower()

        nucleus_kw = ["nucleus", "nucleoplasm", "nucleoli", "nuclear", "nucleolus"]
        non_nuc_kw = ["mitochondri", "cytosol", "cytoplasm", "golgi", "endoplasmic reticulum",
                       "cytoskeleton", "centrosome", "microtubule", "vesicle",
                       "cell projection", "plasma membrane", "extracellular",
                       "cilia", "flagella", "synapse", "postsynaptic"]

        uni_text = " ".join(uni_subcell).lower()
        has_nuc = any(kw in hpa_text or kw in uni_text for kw in nucleus_kw)
        has_non = any(kw in hpa_text or kw in uni_text for kw in non_nuc_kw)

        if has_nuc and not has_non:
            cat = "nucleoplasm"
        elif has_nuc and has_non:
            cat = "nucleus-cytoplasm"
        elif has_non and not has_nuc:
            cat = "rejected"
            write_rejected(gene, f"无非核定位证据，定位: HPA={'/'.join(hpa_main) if hpa_main else '无数据'}, UniProt={'/'.join(uni_subcell[:3]) if uni_subcell else '无数据'}", uni_data, pm_data)
            continue
        else:
            cat = "nucleoplasm"  # default

        write_scored(gene, cat, nuc, nuc_evidence, uni_data, af_data, pm_data, hpa_data, str_data, inta_data, af_found)

    print("\n=== Done ===")

if __name__ == "__main__":
    main()
