#!/usr/bin/env python3
"""Generate /180 re-evaluation reports for Batch 4 & 5 genes (MORN2 MOSPD1 MPHOSPH6 MPHOSPH9 MPND MPPE1 MRFAP1 MRGBP MRI1 MRPL44)."""
import json, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DETAIL = os.path.join(BASE, "detail")
PACKET_DIR = "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets"

GENES = [
    "MORN2", "MOSPD1", "MPHOSPH6", "MPHOSPH9", "MPND",
    "MPPE1", "MRFAP1", "MRGBP", "MRI1", "MRPL44",
]

# --- Scoring helpers (identical to gen_full_reeval.py) ---

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
    domain_count = domains_text.count("IPR") + domains_text.count("PF")
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
    if domains and plddt > 70: pts += 0.5
    if len(pdb_ids) >= 3: pts += 1.0
    return min(pts, 3.0)

def nuclear_score(uni_subcell, hpa_main, hpa_addl, hpa_rel, go_cc_terms, has_uni):
    nucleolus_kw = ["nucleol"]
    nucleus_kw = ["nucleus", "nucleoplasm", "nucleoli", "nuclear", "nucleolus"]
    non_nuc_kw = ["mitochondri", "cytosol", "cytoplasm", "golgi", "endoplasmic reticulum",
                  "membrane", "secreted", "cytoskeleton", "centrosome", "spindle",
                  "microtubule", "vesicle", "kinocilium", "lamellipodium",
                  "synapse", "postsynaptic", "cilia", "flagella"]

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
        go_text = " ".join(extract_go_terms(go_cc_terms)).lower()
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
        if go_nuc:
            return 4
        return 3

    if nuc_sources == 1 and non_sources == 1:
        return 4

    if nuc_sources >= 1 and non_sources > nuc_sources:
        return 4

    if non_sources >= 2 and nuc_sources == 0:
        return 2

    if non_sources == 1 and nuc_sources == 0:
        return 2

    return 3


def format_key_papers(papers):
    if not papers:
        return "无关键文献数据。"
    lines = []
    for i, p in enumerate(papers[:5], 1):
        title = p.get("title", "N/A")
        journal = p.get("journal", "N/A")
        pmid = p.get("pmid", "N/A")
        lines.append(f"{i}. {title}. *{journal}*. PMID: {pmid}")
    return "\n".join(lines)

def format_string_table(partners):
    if not partners:
        return "| — | — | — | — |"
    lines = []
    for p in partners[:10]:
        name = p.get("partner", "?")
        score = p.get("score", 0)
        exp = p.get("experimental", 0)
        lines.append(f"| {name} | {score:.3f} | {exp:.3f} | — |")
    return "\n".join(lines)

def format_intact_table(partners, gene):
    if not partners:
        return "| — | — | — |"
    seen = set()
    lines = []
    for p in partners:
        partner = p.get("partner", "")
        if partner.lower() in seen: continue
        seen.add(partner.lower())
        if len(seen) > 10: break
        method = p.get("method", "—")
        pmid = p.get("pmid", "—")
        lines.append(f"| {partner} | {method[:50]} | {pmid[:30]} |")
    return "\n".join(lines) if lines else "| — | — | — |"

def get_domain_text(uni_data):
    if not uni_data: return "暂无数据 (UniProt未获取)"
    interpro = uni_data.get("interpro", [])
    pfam = uni_data.get("pfam", [])
    ipr_ids = [i.get("id", "") for i in interpro]
    pf_ids = [p.get("id", "") for p in pfam]
    parts = []
    if ipr_ids: parts.append("InterPro: " + ", ".join(ipr_ids[:5]))
    if pf_ids: parts.append("Pfam: " + ", ".join(pf_ids[:3]))
    return "; ".join(parts) if parts else "无注释结构域"

def extract_go_terms(go_cc):
    if not go_cc: return []
    terms = []
    for cc in go_cc:
        if isinstance(cc, dict):
            terms.append(cc.get("term", str(cc)))
        else:
            terms.append(str(cc))
    return terms

def get_go_cc_text(uni_data):
    if not uni_data: return "- 无 GO-CC 注释 (UniProt未获取)"
    go_cc = uni_data.get("go_cc", [])
    if not go_cc: return "- 无 GO-CC 注释"
    return "\n".join(f"- {cc.get('term', str(cc))} ({cc.get('id','')})" for cc in go_cc[:6])

def get_reg_partner_info(string_partners, intact_partners, gene):
    reg_keywords = ["chromatin", "transcription", "histone", "dna", "rna polymer",
                    "helicase", "splicing", "rna", "trna", "rrna", "nucleolar",
                    "ribosome", "nucleosome", "mediator", "coactivator", "corepressor",
                    "deacetylase", "acetyltransferase", "methyltransferase",
                    "kinetochore", "centromere", "condensin", "cohesin", "smc",
                    "origin recognition", "replication factor", "eif4e", "translation",
                    "ubiquitin", "e3", "ligase"]
    reg_partners = []
    if string_partners:
        for p in string_partners[:20]:
            name = p.get("partner", "").lower()
            if any(kw in name for kw in reg_keywords):
                reg_partners.append(p.get("partner", "?"))
    return reg_partners


def generate_report(gene):
    packet_path = os.path.join(PACKET_DIR, f"{gene}.json")
    with open(packet_path) as f:
        pkt = json.load(f)

    uni = pkt.get("uniprot", {}).get("data") if pkt.get("uniprot", {}).get("ok") else None
    has_uni = uni is not None
    af = pkt.get("alphafold", {}).get("data") if pkt.get("alphafold", {}).get("ok") else None
    af_found = af and af.get("found")
    pubmed = pkt.get("pubmed", {}).get("data", {}) if pkt.get("pubmed", {}).get("ok") else {}
    string_p = pkt.get("string", {}).get("data", []) if pkt.get("string", {}).get("ok") else []
    intact_p = pkt.get("intact", {}).get("data", []) if pkt.get("intact", {}).get("ok") else []
    hpa = pkt.get("hpa", {}).get("data", {}) if pkt.get("hpa", {}).get("ok") else {}

    pubmed_strict = pubmed.get("strict_count", 0)
    key_papers = pubmed.get("key_papers", [])

    if has_uni:
        accession = uni.get("accession", gene)
        prot_name = uni.get("protein_name", f"{gene} protein")
        length_aa = uni.get("length_aa", 0)
        mass_kda = uni.get("mass_kda", round(length_aa * 0.11, 1))
        subcell = [s.get("location", "") for s in uni.get("subcellular_locations", [])]
        go_cc = uni.get("go_cc", [])
        function_text = uni.get("function", [])
        pdb_list = [p.get("id", "") for p in uni.get("pdb", [])]
        uniprot_interactions = uni.get("uniprot_interactions", [])
        aliases = uni.get("aliases", [])
    else:
        accession = gene
        prot_name = f"{gene} (UniProt未获取)"
        length_aa = 0
        mass_kda = 0
        subcell = []
        go_cc = []
        function_text = []
        pdb_list = []
        uniprot_interactions = []
        aliases = []

    if af_found:
        plddt = af.get("plddt_stats", {}).get("mean_plddt", 0)
        pct_gt_90 = af.get("plddt_stats", {}).get("pct_gt_90", 0)
        pct_70_90 = af.get("plddt_stats", {}).get("pct_70_90", 0)
        pct_50_70 = af.get("plddt_stats", {}).get("pct_50_70", 0)
        pct_lt_50 = af.get("plddt_stats", {}).get("pct_lt_50", 0)
        af_version = af.get("latest_version", "?")
        ordered_pct = round(pct_gt_90 + pct_70_90, 1)
    else:
        plddt = 0
        pct_gt_90 = 0
        pct_70_90 = 0
        pct_50_70 = 0
        pct_lt_50 = 0
        af_version = "?"
        ordered_pct = 0

    hpa_main = hpa.get("subcellular_main_location", [])
    hpa_addl = hpa.get("subcellular_additional_location", [])
    hpa_rel = hpa.get("reliability_if", "暂无数据")
    hpa_gene_url = hpa.get("hpa_gene_url", "")
    hpa_subcell_url = hpa.get("hpa_subcellular_url", "")
    hpa_status = hpa.get("status", "unknown")

    domain_text = get_domain_text(uni)

    # Calculate scores
    nuc = nuclear_score(subcell, hpa_main, hpa_addl, hpa_rel, go_cc, has_uni)
    sz = size_score(length_aa) if length_aa > 0 else 5
    nov = novelty_score(pubmed_strict)
    struct = struct_score(pdb_list, plddt) if af_found else 4
    dom = domain_score(domain_text, plddt)
    ppi = ppi_score(len(string_p), len(intact_p), string_p)
    cross = cross_validation(pdb_list, plddt, subcell, hpa_main, go_cc, len(string_p), len(intact_p), domain_text, has_uni)

    raw = nuc * 4 + sz * 1 + nov * 5 + struct * 3 + dom * 2 + ppi * 3 + cross
    norm = round(raw / 1.80, 1)

    rejected = nuc <= 3 or pubmed_strict > 100
    status = "rejected" if rejected else "scored"

    # Determine destination directory
    if rejected:
        dest = "rejected"
    else:
        hpa_loc_text = ", ".join(hpa_main + hpa_addl).lower()
        uni_loc_text = " ".join(subcell).lower()
        go_loc_text = " ".join(extract_go_terms(go_cc)).lower()
        all_loc = hpa_loc_text + " " + uni_loc_text + " " + go_loc_text
        if "nuclear bod" in all_loc or "nuclear speck" in all_loc:
            dest = "nuclear-body"
        elif "nucleolus" in all_loc or "fibrillar center" in all_loc:
            dest = "nucleolus"
        elif "nuclear envelope" in all_loc or "nuclear membrane" in all_loc or "nuclear pore" in all_loc:
            dest = "nuclear-envelope"
        elif "nucleoplasm" in all_loc:
            dest = "nucleoplasm"
        elif "chromatin" in all_loc or "chromosome" in all_loc:
            dest = "chromatin"
        else:
            dest = "nucleoplasm"

    nuc_desc_map = {
        9: "多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。",
        8: "主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。",
        7: "主要核定位，HPA 可靠性良好，有辅助数据源支持。",
        6: "存在核定位证据但部分来源支持较弱或缺失。",
        5: "核定位证据存在但较为混杂，部分数据源指向非核区室。",
        4: "核定位信号较弱，多个数据源显示混合定位或非核偏好。",
        3: "核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。",
        2: "核定位证据极弱，主要数据源均不指向细胞核。",
        1: "无核定位证据。",
    }
    nuc_desc = nuc_desc_map.get(nuc, "核定位不确定。")

    if sz >= 10: sz_desc = "大小适中（200-800 aa），适合常规生化实验和结构解析。"
    elif sz >= 8: sz_desc = "大小基本合适，可用于常规实验。"
    elif sz >= 5: sz_desc = "蛋白偏小/偏大，实验操作有一定难度。"
    else: sz_desc = "大小偏离理想范围，实验设计需特殊考虑。"

    if nov >= 10: nov_desc = "极度新颖，几乎未被系统研究（PubMed ≤20篇）。"
    elif nov >= 8: nov_desc = "非常新颖，仅有少数基础研究。"
    elif nov >= 6: nov_desc = "较新颖，有一定研究但存在未探索领域。"
    else: nov_desc = "有一定研究基础，但仍存在niche空间。"

    pdb_text = ", ".join(pdb_list[:10]) if pdb_list else "无"
    if struct >= 10:
        if plddt >= 85:
            struct_desc = f"PDB实验结构（{pdb_text[:60]}）+ AlphaFold极高置信度预测（pLDDT={plddt}），结构可信度极高。"
        else:
            struct_desc = f"PDB实验结构（{pdb_text[:60]}）+ AlphaFold预测（pLDDT={plddt}），实验结构可用。"
    elif struct >= 9:
        struct_desc = f"PDB实验结构（{pdb_text[:60]}）+ AlphaFold高质量预测（pLDDT={plddt}），结构可信度高。"
    elif struct >= 8:
        if plddt >= 85:
            struct_desc = f"AlphaFold 极高置信度预测（pLDDT={plddt}，有序区 {ordered_pct}%），结构可靠。"
        else:
            struct_desc = f"AlphaFold 高质量预测（pLDDT={round(plddt,1)}，有序区 {ordered_pct}%），结构可靠。"
    elif struct >= 7:
        struct_desc = f"AlphaFold 中等质量（pLDDT={round(plddt,1)}，有序区 {ordered_pct}%），结构基本可用。"
    else:
        struct_desc = f"AlphaFold 预测质量有限（pLDDT={round(plddt,1)}），有序残基占 {ordered_pct}%。"

    if dom >= 9:
        dom_desc = "含明确的核酸结合/染色质相关结构域，多库确认。"
    elif dom >= 8:
        dom_desc = "多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。"
    elif dom >= 7:
        dom_desc = f"存在已知结构域注释，可作为功能研究的结构基础。"
    elif dom >= 5:
        dom_desc = f"结构域注释有限，AlphaFold预测有可辨识折叠域。"
    else:
        dom_desc = "结构域注释稀疏，属新颖蛋白正常现象。"

    reg = get_reg_partner_info(string_p, intact_p, gene)
    reg_ratio = len(reg) / min(len(string_p), 20) * 100 if string_p else 0
    ppi_desc = f"STRING {len(string_p)} 个预测互作，IntAct {len(intact_p)} 个实验互作。调控相关配体占比 {reg_ratio:.0f}%。"

    if_status = hpa.get("image_status", "unknown")
    if if_status in ["no_image_detected", "unknown"]:
        if_note = "HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。"
    else:
        if_note = f"HPA IF 图像状态: {if_status}。"

    pae_note = "PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。"

    papers_text = format_key_papers(key_papers)
    string_table = format_string_table(string_p)
    intact_table = format_intact_table(intact_p, gene)
    go_cc_text = get_go_cc_text(uni)

    if has_uni:
        subcell_text = "; ".join(subcell) if subcell else "无注释"
    else:
        subcell_text = "暂无数据（UniProt获取失败）"

    hpa_loc_text = ", ".join(hpa_main) if hpa_main else ""
    if hpa_addl:
        hpa_loc_text += ("; 额外: " + ", ".join(hpa_addl)) if hpa_loc_text else ", ".join(hpa_addl)
    if not hpa_loc_text:
        hpa_loc_text = "暂无HPA定位数据"

    alias_text = ", ".join(aliases[:5]) if aliases else ""
    mass = mass_kda if mass_kda else (round(length_aa * 0.11, 1) if length_aa else "未知")
    uniprot_url = f"https://www.uniprot.org/uniprotkb/{accession}" if accession else ""

    nov_label = "≤20→10" if pubmed_strict <= 20 else ("≤40→8" if pubmed_strict <= 40 else ("≤60→6" if pubmed_strict <= 60 else ("≤80→4" if pubmed_strict <= 80 else ("≤100→2" if pubmed_strict <= 100 else ">100→REJECTED"))))

    # Build cross-validation details
    cross_details = []
    if pdb_list and plddt > 0: cross_details.append("PDB + AlphaFold 双源验证: +0.5")
    has_multi_nuc = 0
    if has_uni and subcell: has_multi_nuc += 1
    if hpa_main: has_multi_nuc += 1
    if go_cc: has_multi_nuc += 1
    if has_multi_nuc >= 2: cross_details.append(f"多库定位一致 ({has_multi_nuc}源): +0.5")
    elif has_multi_nuc == 1: cross_details.append("多库定位一致: +0 (仅1源)")
    else: cross_details.append("多库定位一致: +0")
    if string_p and intact_p: cross_details.append("STRING + IntAct 双源验证: +0.5")
    else: cross_details.append("STRING + IntAct 双源验证: +0")
    if domain_text and "暂无" not in domain_text and plddt > 70: cross_details.append("结构域 + AlphaFold 质量: +0.5")
    else: cross_details.append("结构域 + AlphaFold 质量: +0")
    if len(pdb_list) >= 3: cross_details.append("PDB 多条目覆盖 (≥3): +1.0")
    else: cross_details.append("PDB 多条目覆盖: +0")

    # Rejection reasons
    rejection_reasons = []
    if nuc <= 3:
        rejection_reasons.append(f"核定位证据不足 (核定位得分 {nuc}/10 ≤ 3)")
    if pubmed_strict > 100:
        rejection_reasons.append(f"研究热度过高 (PubMed strict={pubmed_strict}，超过100篇阈值)")

    if rejected:
        title_line = f"## {gene} — REJECTED ({'; '.join(rejection_reasons)})"
    else:
        title_line = f"## {gene} 核蛋白评估报告 (Full Re-evaluation)"

    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: 2026-06-03
tags: [protein-scout, {"rejected" if rejected else "nuclear-protein"}, evaluation]
status: {status}
---

{title_line}

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene}{f" / {alias_text}" if alias_text else ""} |
| 蛋白名称 | {prot_name} |
| 蛋白大小 | {length_aa if length_aa else "未知"} aa / {mass} kDa |
| UniProt ID | {accession} |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | {nuc}/10 | ×4 | {nuc*4} | HPA: {hpa_loc_text[:60]}; UniProt: {subcell_text[:60]} |
| 📏 蛋白大小 | {sz}/10 | ×1 | {sz} | {length_aa if length_aa else "未知"} aa / {mass} kDa |
| 🆕 研究新颖性 | {nov}/10 | ×5 | {nov*5} | PubMed strict={pubmed_strict} 篇 ({nov_label}) |
| 🏗️ 三维结构 | {struct}/10 | ×3 | {struct*3} | AlphaFold v{af_version} pLDDT={round(plddt,1)}; PDB: {pdb_text[:40]} |
| 🧬 调控结构域 | {dom}/10 | ×2 | {dom*2} | {domain_text[:60]} |
| 🔗 PPI 网络 | {ppi}/10 | ×3 | {ppi*3} | STRING {len(string_p)} partners; IntAct {len(intact_p)} interactions |
| ➕ 互证加分 | — | max +3 | {cross} | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **{raw}/180** | |
| **归一化总分** | | | **{norm}/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | {hpa_loc_text} | {hpa_rel if hpa_rel else "暂无"} |
| UniProt | {subcell_text[:80]}{"..." if len(subcell_text) > 80 else ""} | {"Swiss-Prot/TrEMBL" if has_uni else "获取失败"} |

**IF 图像说明**: {if_note}

**GO Cellular Component**:
{go_cc_text}

**结论**: {nuc_desc}

#### 3.2 蛋白大小评估

**评价**: {sz_desc}

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | {pubmed_strict} |
| PubMed broad count | {pubmed.get("broad_count", "N/A")} |
| 别名(未计入scoring) | {pubmed.get("alias_note", "无")} |

**关键文献**:
{papers_text}

**评价**: {nov_desc}

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v{af_version} |
| AlphaFold 平均 pLDDT | {round(plddt,1)} |
| 高置信度残基 (pLDDT>90) 占比 | {pct_gt_90}% |
| 置信残基 (pLDDT 70-90) 占比 | {pct_70_90}% |
| 中等置信 (pLDDT 50-70) 占比 | {pct_50_70}% |
| 低置信 (pLDDT<50) 占比 | {pct_lt_50}% |
| 有序区域 (pLDDT>70) 占比 | {ordered_pct}% |
| 可用 PDB 条目 | {pdb_text} |

**{pae_note}**

**评价**: {struct_desc}

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | {domain_text[:150]} |

**染色质调控潜力分析**: {dom_desc}

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
{string_table}

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
{intact_table}

**PPI 互证分析**:
- {"STRING + IntAct 均有数据" if string_p and intact_p else "仅STRING预测" if string_p else "仅IntAct实验" if intact_p else "无PPI数据"}
- STRING partners: {len(string_p)}，IntAct interactions: {len(intact_p)}
- 调控相关比例: {len(reg)} / {min(len(string_p), 20)} = {reg_ratio:.0f}%

**评价**: {ppi_desc}

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT={round(plddt,1)} + PDB: {pdb_text[:30]} | pLDDT={round(plddt,1)}, v{af_version} | {"预测+实验" if pdb_list else "仅预测"} |
| 定位 | UniProt + HPA | {subcell_text[:50]} / {hpa_loc_text[:50]} | {"一致" if has_multi_nuc >= 2 else "待确认"} |
| PPI | STRING + IntAct | {len(string_p)} + {len(intact_p)} interactions | {"数据充分" if string_p and intact_p else "数据有限"} |

**互证加分明细**:
{chr(10).join(f"- {d}" for d in cross_details)}
**总分**: +{cross} / max +3

### 4. 总体评价

**推荐等级**: {"⭐⭐⭐" if rejected else "⭐" * max(1, min(5, round(norm/20)))} {"(REJECTED)" if rejected else ""}

**核心优势**:
1. {gene} — {prot_name}，{nov_desc}
2. 蛋白大小{length_aa if length_aa else "未知"} aa，{sz_desc}

**风险/不确定性**:
1. {f"PubMed {pubmed_strict} 篇，研究基础极有限，功能注释不完整" if pubmed_strict <= 20 else f"PubMed {pubmed_strict} 篇，已有一定研究基础" if pubmed_strict <= 100 else f"PubMed {pubmed_strict} 篇，研究热度过高（>100），不符合新颖性要求"}
2. {"AlphaFold 预测质量一般（pLDDT=" + str(round(plddt,1)) + "），需要更多实验结构验证" if plddt < 70 else "结构数据质量可接受" if plddt >= 70 else "结构数据暂缺"}

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
{"- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**" if nuc <= 3 else ""}{"**该蛋白PubMed文献数 " + str(pubmed_strict) + " > 100，研究热度过高，不符合novelty筛选标准。**" if pubmed_strict > 100 and nuc > 3 else ""}

### 5. 数据来源
- UniProt: {uniprot_url}
- Protein Atlas: {hpa_subcell_url if hpa_subcell_url else "https://www.proteinatlas.org/search/" + gene}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term={gene}
- AlphaFold: https://alphafold.ebi.ac.uk/entry/{accession}
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: {pkt.get("timestamp", "N/A")}
"""
    return report, dest


# Generate all reports
print("Generating 10 full re-evaluation reports (/180 format) for Batch 4&5...")
print("=" * 60)
results = []
for gene in GENES:
    try:
        report, dest = generate_report(gene)
        report_dir = os.path.join(DETAIL, dest, gene)
        os.makedirs(report_dir, exist_ok=True)
        report_path = os.path.join(report_dir, f"{gene}-evaluation.md")
        with open(report_path, "w") as f:
            f.write(report)
        size = len(report.encode("utf-8"))
        has_180 = "/180" in report
        status = "OK" if size > 2000 and has_180 else ("SHORT" if size <= 2000 else "NO_180")
        print(f"  {gene:12s} -> {dest:20s}/{gene}/{gene}-evaluation.md ({size:5d} bytes) [{status}]")
        results.append({"gene": gene, "dest": dest, "size": size, "status": status})
    except Exception as e:
        print(f"  {gene:12s} -> ERROR: {e}")
        results.append({"gene": gene, "dest": "ERROR", "size": 0, "status": f"ERROR: {e}"})

print("=" * 60)
ok = sum(1 for r in results if r["status"] == "OK")
short = sum(1 for r in results if r["status"] == "SHORT")
no_180 = sum(1 for r in results if r["status"] == "NO_180")
err = sum(1 for r in results if r["status"].startswith("ERROR"))
print(f"Summary: {ok} OK, {short} SHORT, {no_180} NO_180, {err} ERROR")
print(f"Destinations: {', '.join(sorted(set(r['dest'] for r in results)))}")
print("\nDone.")
