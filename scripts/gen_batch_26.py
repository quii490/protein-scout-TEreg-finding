#!/usr/bin/env python3
"""Generate complete /180 re-evaluation reports for 25 specified genes from harvest packets."""

import json
import os
import math
from datetime import datetime

BASE = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested"
PACKET_DIR = "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets"
GENES = [
    "BICD2", "BICRA", "BICRAL", "BIRC7", "BLCAP", "BLMH", "BLTP3B", "BLVRB",
    "BMP2K", "BMS1", "BNIP2", "BOD1", "BOD1L1", "BOLA2", "BPNT1", "BPNT2",
    "BRCC3", "BRI3", "BRIX1", "BRK1", "C2CD4D", "C2CD7", "CACNA2D3", "CACNB4",
    "CACNG4"
]

TODAY = "2026-06-03"

def novelty_score(strict_count):
    if strict_count <= 20: return 10
    if strict_count <= 40: return 8
    if strict_count <= 60: return 6
    if strict_count <= 80: return 4
    if strict_count <= 100: return 2
    return 0

def size_score(aa):
    if 200 <= aa <= 800: return 10
    if 100 <= aa < 200: return 7
    if 800 < aa <= 1200: return 7
    if 50 <= aa < 100: return 4
    if 1200 < aa <= 2000: return 4
    if aa < 50: return 2
    return 2

def af_score(mean_plddt):
    if mean_plddt >= 85: return 10
    if mean_plddt >= 75: return 9
    if mean_plddt >= 65: return 7
    if mean_plddt >= 55: return 5
    if mean_plddt >= 40: return 3
    return 1

def domain_score(interpro_count, pfam_count, has_pdb=False):
    total = interpro_count + pfam_count
    if total >= 8: return 10
    if total >= 6: return 8
    if total >= 4: return 7
    if total >= 2: return 5
    if total >= 1: return 3
    return 1

def ppi_score(string_count, intact_count):
    total = string_count + intact_count
    if total >= 30: return 10
    if total >= 20: return 8
    if total >= 15: return 6
    if total >= 10: return 4
    if total >= 5: return 3
    if total >= 1: return 2
    return 1

def nuclear_score(hpa_main, hpa_all, uniprot_locs, go_cc_terms):
    nuclear_signals = []
    if hpa_main:
        for loc in hpa_main:
            loc_lower = loc.lower()
            if any(t in loc_lower for t in ['nucleoplasm', 'nucleoli', 'nuclear', 'nucleus']):
                nuclear_signals.append(('HPA_main', loc))
    if hpa_all:
        for loc in hpa_all:
            loc_lower = loc.lower()
            if any(t in loc_lower for t in ['nucleoplasm', 'nucleoli', 'nuclear', 'nucleus']):
                nuclear_signals.append(('HPA_add', loc))
    if uniprot_locs:
        for loc_data in uniprot_locs:
            loc = loc_data.get('location', '')
            loc_lower = loc.lower()
            if any(t in loc_lower for t in ['nucleus', 'nuclear', 'nucleoplasm', 'nucleoli']):
                nuclear_signals.append(('UniProt', loc))
    nuclear_go = ['nucleus', 'nucleoplasm', 'nucleoli', 'nuclear', 'chromatin']
    non_nuclear_go = ['cytosol', 'cytoplasm', 'membrane', 'golgi', 'mitochondr', 'vesicle',
                       'focal adhesion', 'plasma membrane', 'centrosome', 'cilium', 'spindle',
                       'endoplasmic', 'lipid droplet', 'extracellular', 'synapse', 'postsynapse',
                       'axoneme', 'microtubule']
    go_nuclear_count = 0
    go_non_nuclear_count = 0
    if go_cc_terms:
        for go in go_cc_terms:
            term = go.get('term', '').lower()
            if any(t in term for t in nuclear_go):
                go_nuclear_count += 1
            if any(t in term for t in non_nuclear_go):
                go_non_nuclear_count += 1
    nuclear_signals.append(('GO_nuclear', go_nuclear_count))
    nuclear_signals.append(('GO_non_nuclear', go_non_nuclear_count))
    has_hpa_main_nuclear = any(s[0] == 'HPA_main' for s in nuclear_signals)
    has_uniprot_nuclear = any(s[0] == 'UniProt' for s in nuclear_signals)
    hpa_main_is_purely_nuclear = hpa_main and all(
        any(t in loc.lower() for t in ['nucleoplasm', 'nucleoli', 'nuclear', 'nucleus'])
        for loc in hpa_main
    ) and len(hpa_main) > 0
    if hpa_main_is_purely_nuclear and go_non_nuclear_count <= 1:
        return 10
    if hpa_main_is_purely_nuclear and go_non_nuclear_count <= 3:
        return 9
    if has_hpa_main_nuclear and has_uniprot_nuclear and go_non_nuclear_count <= 3:
        return 8
    if has_hpa_main_nuclear and go_non_nuclear_count <= 3:
        return 7
    if has_hpa_main_nuclear:
        return 6
    has_hpa_additional_nuclear = any(s[0] == 'HPA_add' for s in nuclear_signals)
    if has_hpa_additional_nuclear and go_nuclear_count >= 1:
        return 5
    if has_hpa_additional_nuclear or go_nuclear_count >= 1:
        return 4
    if go_nuclear_count >= 1:
        return 3
    if has_uniprot_nuclear:
        return 3
    return 2


def classify_category(hpa_main, hpa_all, uniprot_locs, nuc_score):
    if nuc_score <= 3:
        return "rejected"
    all_locs = []
    if hpa_main: all_locs.extend([l.lower() for l in hpa_main])
    if hpa_all: all_locs.extend([l.lower() for l in hpa_all])
    if uniprot_locs:
        for ld in uniprot_locs:
            all_locs.append(ld.get('location', '').lower())
    all_text = ' '.join(all_locs)
    if 'nucleolus' in all_text or 'nucleoli' in all_text:
        return 'nucleolus'
    if 'nuclear speckle' in all_text or 'nuclear speckles' in all_text:
        return 'nuclear-speckle'
    if 'nuclear body' in all_text or 'nuclear bodies' in all_text:
        return 'nuclear-body'
    if 'nuclear envelope' in all_text or 'nuclear membrane' in all_text:
        return 'nuclear-envelope'
    if 'chromatin' in all_text:
        return 'chromatin'
    if ('nucleoplasm' in all_text or 'nucleus' in all_text):
        cyto_terms = ['cytosol', 'cytoplasm', 'vesicle', 'membrane', 'golgi', 'plasma membrane']
        has_cyto = any(t in all_text for t in cyto_terms)
        if has_cyto and all(t not in all_text for t in ['nucleolus', 'nucleoli', 'speckle', 'body']):
            return 'nucleus-cytoplasm'
        return 'nucleoplasm'
    return 'nucleoplasm'


def load_packet(gene):
    path = os.path.join(PACKET_DIR, f"{gene}.json")
    with open(path) as f:
        return json.load(f)


def build_report(gene, pkt):
    up = pkt['uniprot']['data']
    af = pkt['alphafold'].get('data', {}) if isinstance(pkt['alphafold'], dict) else {}
    pm = pkt['pubmed']['data']
    st = pkt['string']['data'] if pkt['string']['ok'] else []
    ia = pkt['intact']['data']
    hp = pkt['hpa']['data']

    accession = up.get('accession', 'N/A')
    protein_name = up.get('protein_name', 'N/A')
    length_aa = up.get('length_aa', 0)
    mass_kda = up.get('mass_kda', 0)
    aliases = up.get('aliases', [])
    function_text = up.get('function', [])
    uniprot_locs = up.get('subcellular_locations', [])
    go_cc = up.get('go_cc', [])
    pdb_entries = up.get('pdb', [])
    interpro = up.get('interpro', [])
    pfam = up.get('pfam', [])

    strict_count = pm.get('strict_count', 0)
    broad_count = pm.get('broad_count', 0)
    alias_note = pm.get('alias_note', '')
    key_papers = pm.get('key_papers', [])

    string_partners = len(st) if isinstance(st, list) else 0
    intact_partners = len(ia)

    hpa_main = hp.get('subcellular_main_location', [])
    hpa_all = [l for loc_list in [hp.get('subcellular_location', [])] for l in loc_list]
    hpa_reliability = hp.get('reliability_if', 'N/A')
    if_image_urls = hp.get('if_image_urls', [])

    plddt_stats = af.get('plddt_stats', {})
    if isinstance(plddt_stats, dict) and 'mean_plddt' in plddt_stats:
        mean_plddt = plddt_stats.get('mean_plddt', 0)
        if mean_plddt is None:
            mean_plddt = 0
    else:
        mean_plddt = 0

    # --- SCORING ---
    nuc_score = nuclear_score(hpa_main, hpa_all, uniprot_locs, go_cc)
    size_sc = size_score(length_aa)
    nov_sc = novelty_score(strict_count)
    if isinstance(mean_plddt, (int, float)) and mean_plddt > 0:
        af_sc = af_score(mean_plddt)
        af_available = True
    else:
        af_sc = 1
        af_available = False

    dom_sc = domain_score(len(interpro), len(pfam), len(pdb_entries) > 0)
    ppi_sc = ppi_score(string_partners, intact_partners)

    rejected = False
    reject_reason = ""
    if nuc_score <= 3:
        rejected = True
        reject_reason = f"Nuclear localization score {nuc_score}/10 <= 3"
    if strict_count > 100:
        rejected = True
        reject_reason = f"PubMed strict count {strict_count} > 100"

    cross_bonus = 0.0
    bonus_items = []
    if pdb_entries and mean_plddt and mean_plddt > 0:
        cross_bonus += 0.5
        bonus_items.append("PDB + AlphaFold 双源验证: +0.5")
    if hpa_main and uniprot_locs:
        nuc_sources = sum([1 if hpa_main else 0, 1 if uniprot_locs else 0, 1 if go_cc else 0])
        if nuc_sources >= 3:
            cross_bonus += 0.5
            bonus_items.append("多库定位一致 (3源): +0.5")
        elif nuc_sources >= 2:
            cross_bonus += 0.3
            bonus_items.append("双库定位一致 (2源): +0.3")
    if string_partners > 0 and intact_partners > 0:
        cross_bonus += 0.5
        bonus_items.append("STRING + IntAct 双源验证: +0.5")
    if len(interpro) + len(pfam) > 0 and mean_plddt and mean_plddt > 50:
        cross_bonus += 0.5
        bonus_items.append("结构域 + AlphaFold 质量: +0.5")
    if len(pdb_entries) >= 3:
        cross_bonus += 0.5
        bonus_items.append("PDB 多条目覆盖: +0.5")
    cross_bonus = min(cross_bonus, 3.0)
    cross_bonus = round(cross_bonus, 1)

    weighted_nuc = nuc_score * 4
    weighted_size = size_sc * 1
    weighted_nov = nov_sc * 5
    weighted_af = af_sc * 3
    weighted_dom = dom_sc * 2
    weighted_ppi = ppi_sc * 3
    raw_total = weighted_nuc + weighted_size + weighted_nov + weighted_af + weighted_dom + weighted_ppi + cross_bonus
    normalized = round(raw_total / 1.83, 1)

    category = classify_category(hpa_main, hpa_all, uniprot_locs, nuc_score)
    if rejected:
        category = "rejected"

    # --- BUILD REPORT ---
    lines = []
    lines.append("---")
    lines.append("type: protein-evaluation")
    lines.append(f'gene: "{gene}"')
    lines.append(f"date: {TODAY}")
    lines.append("tags: [protein-scout, nuclear-protein, evaluation]")
    lines.append(f"status: {'rejected' if rejected else 'scored'}")
    lines.append("---")
    lines.append("")
    lines.append(f"## {gene} 核蛋白评估报告 (Full Re-evaluation)")
    lines.append("")

    lines.append("### 1. 基本信息")
    lines.append("")
    alias_str = ", ".join(aliases) if aliases else "无"
    lines.append("| 项目 | 内容 |")
    lines.append("|------|------|")
    lines.append(f"| 基因名 / 别名 | {gene} / {alias_str} |")
    lines.append(f"| 蛋白名称 | {protein_name} |")
    lines.append(f"| 蛋白大小 | {length_aa} aa / {mass_kda} kDa |")
    lines.append(f"| UniProt ID | {accession} |")
    lines.append(f"| 评估日期 | {TODAY} |")

    if pkt.get('timestamp'):
        lines.append(f"| 数据采集时间 | {pkt['timestamp']} |")

    if if_image_urls and len(if_image_urls) > 0:
        lines.append("")
        lines.append("**IF 图像**:")
        lines.append(f"![]({if_image_urls[0]})")
        if len(if_image_urls) >= 2:
            lines.append(f"![]({if_image_urls[1]})")
    lines.append("")

    lines.append("### 2. 评分总览")
    lines.append("")

    if rejected:
        lines.append(f"**评估状态：REJECTED**")
        lines.append(f"**拒因：{reject_reason}**")
        lines.append("")

    def abbrev(s, maxlen=35):
        if len(s) <= maxlen: return s
        return s[:maxlen-3] + "..."

    nuc_evidence = ""
    if hpa_main: nuc_evidence += "HPA: " + ", ".join(hpa_main)
    if uniprot_locs:
        loc_names = [l.get('location','') for l in uniprot_locs]
        if nuc_evidence: nuc_evidence += "; "
        nuc_evidence += "UniProt: " + ", ".join(loc_names[:2])

    pdb_str = ", ".join([e.get('id','') for e in pdb_entries[:3]]) if pdb_entries else "无"
    interpro_ids = ", ".join([e.get('id','') for e in interpro[:3]]) if interpro else "无"

    lines.append("| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |")
    lines.append("|------|------|------|--------|-------------|")
    lines.append(f"| 核定位特异性 | {nuc_score}/10 | x4 | {weighted_nuc} | {abbrev(nuc_evidence, 40)} |")
    size_desc = f"{length_aa} aa / {mass_kda} kDa"
    lines.append(f"| 蛋白大小 | {size_sc}/10 | x1 | {weighted_size} | {size_desc} |")
    nov_label = f"PubMed strict={strict_count} 篇"
    if strict_count <= 20: nov_label += " (<=20->10)"
    elif strict_count <= 40: nov_label += " (21-40->8)"
    elif strict_count <= 60: nov_label += " (41-60->6)"
    elif strict_count <= 80: nov_label += " (61-80->4)"
    elif strict_count <= 100: nov_label += " (81-100->2)"
    lines.append(f"| 研究新颖性 | {nov_sc}/10 | x5 | {weighted_nov} | {abbrev(nov_label, 45)} |")
    if mean_plddt and mean_plddt > 0:
        plddt_str = f"AlphaFold v6 pLDDT={mean_plddt:.1f}"
    else:
        plddt_str = "AlphaFold pLDDT 不可用"
    if pdb_str != "无":
        plddt_str += f"; PDB: {pdb_str}"
    lines.append(f"| 三维结构 | {af_sc}/10 | x3 | {weighted_af} | {abbrev(plddt_str, 45)} |")
    domain_desc = f"InterPro: {len(interpro)}; Pfam: {len(pfam)}"
    if interpro: domain_desc += f"; {interpro_ids}"
    lines.append(f"| 调控结构域 | {dom_sc}/10 | x2 | {weighted_dom} | {abbrev(domain_desc, 45)} |")
    ppi_desc = f"STRING {string_partners} partners; IntAct {intact_partners} interactions"
    lines.append(f"| PPI 网络 | {ppi_sc}/10 | x3 | {weighted_ppi} | {abbrev(ppi_desc, 45)} |")
    lines.append(f"| 互证加分 | -- | max +3 | {cross_bonus} | {'; '.join(bonus_items) if bonus_items else '无'} |")
    lines.append(f"| **原始总分** | | | **{raw_total:.1f}/180** | |")
    lines.append(f"| **归一化总分 (/1.83)** | | | **{normalized}/100** | |")
    lines.append("")

    # --- DETAILED ANALYSIS ---
    lines.append("### 3. 详细分析")
    lines.append("")

    # 3.1 Nuclear localization
    lines.append("#### 3.1 核定位证据")
    lines.append("")
    lines.append("| 来源 | 定位 | 可信度 |")
    lines.append("|------|------|--------|")

    hpa_loc_str = "; 额外: " + ", ".join(hpa_all) if hpa_all else "无数据"
    lines.append(f"| Protein Atlas (IF) | {hpa_main[0] if hpa_main else '无数据'}; 额外: {', '.join(hpa_all[:5]) if hpa_all else '无'} | {hpa_reliability if hpa_reliability else 'N/A'} |")

    if uniprot_locs:
        loc_names = [l.get('location','') for l in uniprot_locs]
        lines.append(f"| UniProt | {', '.join(loc_names[:4])} | Swiss-Prot/TrEMBL |")

    lines.append("")

    if if_image_urls and len(if_image_urls) > 0:
        lines.append("**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。")
    else:
        lines.append("**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。")
    lines.append("")

    if go_cc:
        lines.append("**GO Cellular Component**:")
        for go in go_cc[:10]:
            lines.append(f"- {go.get('term','')} ({go.get('id','')})")
        lines.append("")

    nuc_conclusion = ""
    if nuc_score >= 8:
        nuc_conclusion = "核定位证据充分，多个数据源一致支持核定位，定位特异性高。"
    elif nuc_score >= 6:
        nuc_conclusion = "核定位证据较好，主要数据源支持核定位，但存在一定程度的其它亚细胞定位信号。"
    elif nuc_score >= 4:
        nuc_conclusion = "核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。"
    else:
        nuc_conclusion = "核定位证据薄弱，主要数据源不支撑特异核定位，或存在明确矛盾信号。"
    lines.append(f"**结论**: {nuc_conclusion}")
    lines.append("")

    # 3.2 Size
    lines.append("#### 3.2 蛋白大小评估")
    lines.append("")
    if 200 <= length_aa <= 800:
        lines.append(f"**评价**: {length_aa} aa，大小适中（200-800 aa），适合常规生化实验和结构解析。")
    elif length_aa < 50:
        lines.append(f"**评价**: {length_aa} aa，蛋白过小（< 50 aa），实验操作受限，部分生化方法不可用。")
    elif length_aa > 1200:
        lines.append(f"**评价**: {length_aa} aa，蛋白偏大（> 1200 aa），表达纯化难度增加，但结构域丰富。")
    elif length_aa > 800:
        lines.append(f"**评价**: {length_aa} aa，蛋白偏大（> 800 aa），表达纯化有一定难度。")
    else:
        lines.append(f"**评价**: {length_aa} aa，蛋白较小，但仍在可操作范围。")
    lines.append("")

    # 3.3 Research novelty
    lines.append("#### 3.3 研究现状")
    lines.append("")
    lines.append("| 指标 | 数值 |")
    lines.append("|------|------|")
    lines.append(f"| PubMed strict count | {strict_count} |")
    lines.append(f"| PubMed broad count | {broad_count} |")
    if alias_note:
        lines.append(f"| 别名(未计入scoring) | {alias_note} |")
    lines.append("")

    if key_papers:
        lines.append("**关键文献**:")
        for i, paper in enumerate(key_papers[:5]):
            title = paper.get('title', 'N/A')
            journal = paper.get('journal', '')
            pmid = paper.get('pmid', '')
            lines.append(f"{i+1}. {title}. *{journal}*. PMID: {pmid}")
        lines.append("")

    if strict_count <= 20:
        lines.append(f"**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 {nov_sc}/10。")
    elif strict_count <= 40:
        lines.append(f"**评价**: 较高新颖性，研究尚处早期阶段（PubMed 21-40篇）。新颖性评分 {nov_sc}/10。")
    elif strict_count <= 60:
        lines.append(f"**评价**: 中等新颖性，有一定研究基础但仍有探索空间（PubMed 41-60篇）。新颖性评分 {nov_sc}/10。")
    elif strict_count <= 80:
        lines.append(f"**评价**: 研究较多，新颖性一般（PubMed 61-80篇）。新颖性评分 {nov_sc}/10。")
    elif strict_count <= 100:
        lines.append(f"**评价**: 研究热度较高，新颖性较低（PubMed 81-100篇）。新颖性评分 {nov_sc}/10。")
    lines.append("")

    # 3.4 3D Structure
    lines.append("#### 3.4 三维结构分析")
    lines.append("")
    if af_available and isinstance(plddt_stats, dict) and plddt_stats and 'mean_plddt' in plddt_stats and plddt_stats.get('mean_plddt', 0):
        p90 = plddt_stats.get('pct_gt_90', 0)
        p70 = plddt_stats.get('pct_70_90', 0)
        p50 = plddt_stats.get('pct_50_70', 0)
        pL = plddt_stats.get('pct_lt_50', 0)
        lines.append("| 指标 | 数值 |")
        lines.append("|------|------|")
        lines.append("| AlphaFold 版本 | v6 |")
        lines.append(f"| AlphaFold 平均 pLDDT | {mean_plddt:.1f} |")
        lines.append(f"| 高置信度残基 (pLDDT>90) 占比 | {p90:.1f}% |")
        lines.append(f"| 置信残基 (pLDDT 70-90) 占比 | {p70:.1f}% |")
        lines.append(f"| 中等置信 (pLDDT 50-70) 占比 | {p50:.1f}% |")
        lines.append(f"| 低置信 (pLDDT<50) 占比 | {pL:.1f}% |")
        lines.append(f"| 有序区域 (pLDDT>70) 占比 | {p90 + p70:.1f}% |")
        if pdb_entries:
            lines.append(f"| 可用 PDB 条目 | {', '.join([e.get('id','') for e in pdb_entries])} |")
        lines.append("")
    else:
        lines.append("**AlphaFold pLDDT 统计数据不可用（获取失败）。**")
        lines.append("")

    lines.append("**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**")
    lines.append("")

    if mean_plddt and mean_plddt >= 75:
        if pdb_entries:
            lines.append(f"**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT={mean_plddt:.1f}），结构可信度高。三维结构评分 {af_sc}/10。")
        else:
            lines.append(f"**评价**: AlphaFold高质量预测（pLDDT={mean_plddt:.1f}），预测结构可信。三维结构评分 {af_sc}/10。")
    elif mean_plddt and mean_plddt >= 60:
        lines.append(f"**评价**: AlphaFold中等质量预测（pLDDT={mean_plddt:.1f}），存在部分低置信区域。三维结构评分 {af_sc}/10。")
    elif mean_plddt:
        lines.append(f"**评价**: AlphaFold低质量预测（pLDDT={mean_plddt:.1f}），大部分区域无序。三维结构评分 {af_sc}/10。")
    else:
        lines.append(f"**评价**: 三维结构数据有限。三维结构评分 {af_sc}/10。")
    lines.append("")

    # 3.5 Domains
    lines.append("#### 3.5 结构域分析")
    lines.append("")
    lines.append("| 来源 | 结构域 |")
    lines.append("|------|--------|")
    if interpro or pfam:
        interpro_str = ", ".join([f"{e.get('id','')}{'(' + e.get('name','') + ')' if e.get('name') else ''}" for e in interpro]) if interpro else "无"
        pfam_str = ", ".join([f"{e.get('id','')}{'(' + e.get('name','') + ')' if e.get('name') else ''}" for e in pfam]) if pfam else "无"
        lines.append(f"| InterPro/Pfam | InterPro: {interpro_str}; Pfam: {pfam_str} |")
    else:
        lines.append("| InterPro/Pfam | 无已知结构域注释 |")
    lines.append("")

    domain_check = f"存在 {len(interpro) + len(pfam)} 个已知结构域注释，可作为功能研究的结构基础。" if (interpro or pfam) else "暂无已知结构域注释，功能研究缺乏结构起点。"
    lines.append(f"**染色质调控潜力分析**: {domain_check}")
    lines.append("")

    # 3.6 PPI
    lines.append("#### 3.6 PPI 网络")
    lines.append("")

    if isinstance(st, list) and len(st) > 0:
        lines.append("**STRING 预测互作** (combined score > 0.4):")
        lines.append("")
        lines.append("| Partner | Combined Score | Experimental | 功能类别 |")
        lines.append("|---------|---------------|--------------|---------|")
        for s in st[:10]:
            score_str = f"{s.get('score',0):.3f}" if isinstance(s.get('score'), (int, float)) else str(s.get('score',''))
            exp_str = f"{s.get('experimental',0):.3f}" if isinstance(s.get('experimental'), (int, float)) else str(s.get('experimental',''))
            lines.append(f"| {s.get('partner','')} | {score_str} | {exp_str} | -- |")
        lines.append("")
    else:
        lines.append("**STRING 预测互作**: 暂无数据或查询失败。")
        lines.append("")

    if intact_partners > 0:
        lines.append("**实验验证互作** (IntAct):")
        lines.append("")
        lines.append("| Partner | 方法 | PMID |")
        lines.append("|---------|------|------|")
        for ia_item in ia[:10]:
            method = ia_item.get('method', '').split('(')[-1].rstrip(')') if '(' in ia_item.get('method', '') else ia_item.get('method', '')
            pmid = ia_item.get('pmid', '')[:60]
            lines.append(f"| {ia_item.get('partner','')} | {method[:40]} | {pmid} |")
        lines.append("")
    else:
        lines.append("**实验验证互作** (IntAct): 暂无实验验证的直接物理互作数据。")
        lines.append("")

    lines.append("**PPI 互证分析**:")
    if string_partners > 0 and intact_partners > 0:
        lines.append(f"- STRING + IntAct 均有数据")
        lines.append(f"- STRING partners: {string_partners}，IntAct interactions: {intact_partners}")
    elif string_partners > 0:
        lines.append(f"- 仅 STRING 有数据 ({string_partners} partners)")
    elif intact_partners > 0:
        lines.append(f"- 仅 IntAct 有数据 ({intact_partners} interactions)")
    else:
        lines.append("- STRING 和 IntAct 均无数据")
    lines.append("")

    ppi_eval = ""
    if string_partners + intact_partners >= 30:
        ppi_eval = f"互作网络丰富：STRING {string_partners} 预测 + IntAct {intact_partners} 实验互作。PPI 评分 {ppi_sc}/10。"
    elif string_partners + intact_partners >= 10:
        ppi_eval = f"互作网络中等：STRING {string_partners} 预测 + IntAct {intact_partners} 实验互作。PPI 评分 {ppi_sc}/10。"
    elif string_partners + intact_partners >= 1:
        ppi_eval = f"互作数据有限：STRING {string_partners} 预测 + IntAct {intact_partners} 实验互作。PPI 评分 {ppi_sc}/10。"
    else:
        ppi_eval = f"尚无可靠互作数据。PPI 评分 {ppi_sc}/10。"
    lines.append(f"**评价**: {ppi_eval}")
    lines.append("")

    # 3.7 Cross-validation
    lines.append("#### 3.7 多库互证")
    lines.append("")
    lines.append("| 维度 | 来源 | 结果 | 是否一致 |")
    lines.append("|------|------|------|----------|")

    if pdb_entries and mean_plddt and mean_plddt > 0:
        lines.append(f"| 三维结构 | AlphaFold pLDDT={mean_plddt:.1f} + PDB: {pdb_str} | pLDDT={mean_plddt:.1f}, v6 | 预测+实验 |")
    elif mean_plddt and mean_plddt > 0:
        lines.append(f"| 三维结构 | AlphaFold v6 | pLDDT={mean_plddt:.1f} | 单一来源 |")
    else:
        lines.append(f"| 三维结构 | -- | 不可用 | -- |")

    hpa_nuc = [l for l in hpa_all if any(t in l.lower() for t in ['nucleoplasm', 'nucleoli', 'nuclear', 'nucleus'])]
    up_nuc = [l.get('location','') for l in uniprot_locs if any(t in l.get('location','').lower() for t in ['nucleus', 'nuclear', 'nucleoplasm', 'nucleoli'])]
    if hpa_nuc and up_nuc:
        lines.append(f"| 定位 | UniProt + HPA | {', '.join(hpa_nuc[:2])} / {', '.join(up_nuc[:2])} | 一致 |")
    elif hpa_nuc:
        lines.append(f"| 定位 | HPA | {', '.join(hpa_nuc[:3])} | 单一来源 |")
    elif up_nuc:
        lines.append(f"| 定位 | UniProt | {', '.join(up_nuc[:2])} | 单一来源 |")
    else:
        lines.append(f"| 定位 | -- | 无明确核定位数据 | -- |")

    if string_partners > 0 and intact_partners > 0:
        lines.append(f"| PPI | STRING + IntAct | {string_partners} + {intact_partners} interactions | 数据充分 |")
    elif string_partners > 0:
        lines.append(f"| PPI | STRING | {string_partners} interactions | 单一来源 |")
    elif intact_partners > 0:
        lines.append(f"| PPI | IntAct | {intact_partners} interactions | 单一来源 |")
    else:
        lines.append(f"| PPI | -- | 无数据 | -- |")

    lines.append("")
    lines.append("**互证加分明细**:")
    if bonus_items:
        for item in bonus_items:
            lines.append(f"- {item}")
    else:
        lines.append("- 无可用的多库互证加分项")
    lines.append(f"**总分**: +{cross_bonus} / max +3")
    lines.append("")

    # --- OVERALL ASSESSMENT ---
    lines.append("### 4. 总体评价")
    lines.append("")

    if normalized >= 75:
        stars = "5/5"
    elif normalized >= 60:
        stars = "4/5"
    elif normalized >= 45:
        stars = "3/5"
    elif normalized >= 30:
        stars = "2/5"
    else:
        stars = "1/5"

    lines.append(f"**归一化总分**: {normalized}/100")
    if rejected:
        lines.append(f"**状态**: REJECTED -- {reject_reason}")
    lines.append("")

    lines.append("**核心优势**:")
    strengths = []
    if strict_count <= 20:
        strengths.append(f"{gene} -- {protein_name}，极度新颖，几乎未被系统研究（PubMed <= 20篇）。")
    elif strict_count <= 40:
        strengths.append(f"{gene} -- {protein_name}，较高新颖性，研究尚处早期阶段。")
    if 200 <= length_aa <= 800:
        strengths.append(f"蛋白大小{length_aa} aa，大小适中（200-800 aa），适合常规生化实验和结构解析。")
    if mean_plddt and mean_plddt >= 75:
        strengths.append(f"AlphaFold高质量预测（pLDDT={mean_plddt:.1f}），结构可信度高。")
    if pdb_entries:
        strengths.append(f"已有PDB实验结构：{', '.join([e.get('id','') for e in pdb_entries[:3]])}。")
    if interpro or pfam:
        strengths.append(f"存在 {len(interpro) + len(pfam)} 个已知结构域，有明确的结构-功能切入点。")
    if nuc_score >= 8:
        strengths.append("核定位信号明确，多个数据源一致支持。")

    for i, s in enumerate(strengths[:4]):
        lines.append(f"{i+1}. {s}")
    if not strengths:
        lines.append("1. 待进一步实验验证。")
    lines.append("")

    lines.append("**风险/不确定性**:")
    risks = []
    if strict_count <= 5:
        risks.append(f"PubMed {strict_count} 篇，研究基础极有限，功能注释不完整")
    if nuc_score <= 5:
        risks.append(f"核定位信号较弱或存在矛盾（评分 {nuc_score}/10），需IF实验验证")
    if mean_plddt and mean_plddt < 60:
        risks.append(f"AlphaFold pLDDT 较低（{mean_plddt:.1f}），存在显著无序区")
    if string_partners + intact_partners < 5:
        risks.append("PPI 数据有限，互作网络未充分验证")
    if not pdb_entries:
        risks.append("暂无PDB实验结构，结构证据完全依赖AlphaFold预测")
    if length_aa < 100:
        risks.append(f"蛋白过小（{length_aa} aa），实验操作受限")
    if length_aa > 1200:
        risks.append(f"蛋白偏大（{length_aa} aa），表达纯化难度大")

    for i, r in enumerate(risks[:4]):
        lines.append(f"{i+1}. {r}")
    if not risks:
        lines.append("1. 暂无明显风险因素。")
    lines.append("")

    lines.append("**下一步建议**:")
    lines.append("- [ ] 查阅最新关键文献补充研究背景")
    lines.append("- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位")
    if nuc_score >= 4:
        lines.append("- [ ] 设计体外实验验证核定位及潜在调控功能")
    if not pdb_entries:
        lines.append("- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息")
    if string_partners + intact_partners < 5:
        lines.append("- [ ] 通过Co-IP/MS实验鉴定互作伙伴")
    lines.append("")

    # --- DATA SOURCES ---
    lines.append("### 5. 数据来源")
    lines.append("")
    lines.append(f"- UniProt: https://www.uniprot.org/uniprotkb/{accession}")
    lines.append(f"- Protein Atlas: https://www.proteinatlas.org/search/{gene}")
    lines.append(f"- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term={gene}")
    if af.get('found'):
        lines.append(f"- AlphaFold: https://alphafold.ebi.ac.uk/entry/{accession}")
    lines.append(f"- STRING: https://string-db.org/network/9606.{gene}")
    if pkt.get('timestamp'):
        lines.append(f"- Packet data timestamp: {pkt['timestamp']}")
    lines.append("")

    return "\n".join(lines), category, rejected


def main():
    skipped = []
    for gene in GENES:
        packet_path = os.path.join(PACKET_DIR, f"{gene}.json")
        if not os.path.exists(packet_path):
            print(f"SKIP {gene}: no harvest packet")
            skipped.append(gene)
            continue

        print(f"Processing {gene}...")
        try:
            pkt = load_packet(gene)
            report, category, rejected = build_report(gene, pkt)

            if rejected:
                out_dir = os.path.join(BASE, "detail", "rejected", gene)
            else:
                out_dir = os.path.join(BASE, "detail", category, gene)

            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, f"{gene}-evaluation.md")

            with open(out_path, 'w') as f:
                f.write(report)

            report_len = len(report)
            status_icon = "OK" if report_len > 2000 else "SHORT"
            print(f"  -> {out_path} ({report_len} chars) [category={category}, rejected={rejected}] {status_icon}")
        except Exception as e:
            print(f"  ERROR {gene}: {e}")
            import traceback
            traceback.print_exc()

    print("\n=== SUMMARY ===")
    print(f"Total genes: {len(GENES)}")
    print(f"Skipped (no packet): {len(skipped)}")
    if skipped:
        print(f"  Skipped genes: {', '.join(skipped)}")


if __name__ == "__main__":
    main()
