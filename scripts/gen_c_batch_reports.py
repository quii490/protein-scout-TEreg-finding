#!/usr/bin/env python3
"""Harvest packets + write /180 evaluation reports for all remaining C-genes."""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

# Add harvest script path
sys.path.insert(0, "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data")
from protein_scout_harvest import (
    uniprot_entry, alphafold, pubmed, string_partners, intact_partners, hpa_probe,
    safe_call,
)

BASE = Path("/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested")
DETAIL = BASE / "detail"
PACKET_DIR = Path("/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets")
TODAY = "2026-06-02"

DONE_GENES = {
    "CLK2", "CLK3", "CLK4", "CLMN", "CLNS1A", "COG3", "COG5", "COMMD10",
    "CPED1", "CRIPT", "CSRNP1", "CSTF2T", "CTNNBIP1", "CTNNBL1", "CTPS2",
    "CUTC", "CUX1"
}

ALL_GENES = [
    "CILP2","CIMIP2B","CIR1","CKAP2","CKAP2L","CLCN6","CLDN15","CLEC18A","CLEC18C",
    "CLEC19A","CLIC4","CLIP3","CLK2","CLK3","CLK4","CLMN","CLNS1A","CLP1","CLPB","CLPTM1",
    "CLRN3","CLSTN3","CLTA","CLTB","CLYBL","CMC2","CMBL","CMTM5","CNBD2","CNGA4",
    "CNMD","CNOT11","CNOT6L","CNOT7","CNOT8","CNPPD1","CNPY1","CNPY3","CNTFR",
    "COA3","COA5","COA6","COA7","COG3","COG5","COG7","COLCA2","COMMD10","COMTD1",
    "COPS7A","COPS7B","COPS8","COPS9","COQ4","COQ9","CORO1C","COX14","CPED1",
    "CPLX2","CPNE5","CPSF4","CPSF6","CPSF7","CRACR2A","CRBN","CREB1","CRIPT",
    "CRK","CRLF3","CRLS1","CRNKL1","CRY1","CRY2","CRYM","CRYBG2","CSAD","CSDE1",
    "CSRNP1","CSTF2","CSTF2T","CSTPP1","CTAGE6","CTCF","CTNNBIP1","CTNNBL1",
    "CTPS2","CTR9","CTTNBP2","CUTC","CUX1","CXXC4","CXorf56","CYB5R1","CYB5R3",
]

TODO = [g for g in ALL_GENES if g not in DONE_GENES]

def harvest_gene(gene):
    packet = {"gene": gene, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}
    uni = safe_call(uniprot_entry, gene)
    packet["uniprot"] = uni
    accession = uni.get("data", {}).get("accession") if uni.get("ok") else None
    aliases = uni.get("data", {}).get("aliases", []) if uni.get("ok") else []
    packet["alphafold"] = safe_call(alphafold, accession, retries=2)
    time.sleep(0.2)
    packet["pubmed"] = safe_call(pubmed, gene, aliases, retries=3)
    time.sleep(0.2)
    packet["string"] = safe_call(string_partners, gene, retries=3)
    time.sleep(0.2)
    packet["intact"] = safe_call(intact_partners, gene, retries=2)
    time.sleep(0.2)
    packet["hpa"] = safe_call(hpa_probe, gene, retries=2)
    return packet

# ---- Extractors ----
def get_pubmed_count(packet):
    pub = packet.get("pubmed", {})
    if pub.get("ok"):
        return pub.get("data", {}).get("strict_count", 0)
    return 0

def get_length(packet):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        return uni.get("data", {}).get("length_aa", 0)
    return 0

def get_mass(packet, length):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        m = uni.get("data", {}).get("mass_kda")
        if m:
            return m
    return round(length * 0.11, 1)

def get_acc(packet):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        return uni.get("data", {}).get("accession", "")
    return ""

def get_prot_name(packet):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        return uni.get("data", {}).get("protein_name", "")
    return ""

def get_func(packet):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        funcs = uni.get("data", {}).get("function", [])
        if funcs:
            return funcs[0]
    return ""

def get_aliases(packet):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        return uni.get("data", {}).get("aliases", [])
    return []

def get_subcell(packet):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        return uni.get("data", {}).get("subcellular_locations", [])
    return []

def get_go_cc(packet):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        return uni.get("data", {}).get("go_cc", [])
    return []

def get_pdb(packet):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        return uni.get("data", {}).get("pdb", [])
    return []

def get_interpro(packet):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        return uni.get("data", {}).get("interpro", [])
    return []

def get_pfam(packet):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        return uni.get("data", {}).get("pfam", [])
    return []

def get_uni_int(packet):
    uni = packet.get("uniprot", {})
    if uni.get("ok"):
        return uni.get("data", {}).get("uniprot_interactions", [])
    return []

def get_af(packet):
    af = packet.get("alphafold", {})
    if af.get("ok"):
        return af.get("data", {})
    return {}

def get_string(packet):
    st = packet.get("string", {})
    if st.get("ok"):
        return st.get("data", [])
    return []

def get_intact(packet):
    ia = packet.get("intact", {})
    if ia.get("ok"):
        return ia.get("data", [])
    return []

def get_hpa(packet):
    hp = packet.get("hpa", {})
    if hp.get("ok"):
        return hp.get("data", {})
    return {}

def get_papers(packet):
    pub = packet.get("pubmed", {})
    if pub.get("ok"):
        return pub.get("data", {}).get("key_papers", [])
    return []

# ---- Nuclear scoring ----
NUC_WORDS = ["nucleus", "nucleoplasm", "nucleoli", "nucleolus", "nuclear",
             "chromosome", "chromatin", "centromere", "kinetochore", "telomere",
             "nuclear speckle", "nuclear body", "cajal body", "pml body",
             "spliceosome", "dna repair", "nuclear envelope", "nuclear pore"]

CYT_WORDS = ["cytoplasm", "cytosol", "extracellular", "secreted", "plasma membrane",
             "cell membrane", "lysosome", "endosome", "golgi", "endoplasmic reticulum",
             "er", "mitochondrion", "mitochondria", "peroxisome", "vesicle", "cilium",
             "flagellum", "synapse", "cytoskeleton", "centrosome", "spindle"]

def compute_nuc_score(packet):
    subcell = get_subcell(packet)
    go_cc = get_go_cc(packet)
    hpa = get_hpa(packet)

    loc_texts = [s.get("location", "").lower() for s in subcell]
    go_cc_terms = [g.get("term", "").lower() for g in go_cc]
    hpa_locs = [l.lower() for l in hpa.get("subcellular_location", [])]
    hpa_main = [l.lower() for l in hpa.get("subcellular_main_location", [])]

    all_locs = loc_texts + go_cc_terms + hpa_locs

    nuc_count = sum(1 for loc in all_locs if any(w in loc for w in NUC_WORDS))
    cyt_count = sum(1 for loc in all_locs if any(w in loc for w in CYT_WORDS))

    hpa_nuc = any(any(w in l for w in NUC_WORDS) for l in hpa_main)
    hpa_cyt = any(any(w in l for w in CYT_WORDS) for l in hpa_main)
    hpa_rel = hpa.get("reliability_if", "")

    has_nuc = nuc_count > 0 or hpa_nuc

    if not has_nuc:
        if cyt_count > 0 and nuc_count == 0 and not hpa_nuc:
            return (0, "rejected")
        return (2, "rejected")

    if nuc_count <= 1 and cyt_count >= 3:
        return (2, "rejected")

    if hpa_nuc and not hpa_cyt and hpa_rel in ("Approved", "Enhanced"):
        if nuc_count >= 4:
            return (9, "nucleoplasm")
        elif nuc_count >= 2:
            return (8, "nucleoplasm")
        return (7, "nucleoplasm")

    if hpa_nuc:
        if hpa_rel == "Supported":
            if nuc_count >= 2:
                return (7, "nucleoplasm")
            return (6, "nucleus-cytoplasm")

    if nuc_count > cyt_count * 2:
        return (7, "nucleoplasm")
    elif nuc_count > cyt_count:
        return (6, "nucleoplasm")
    elif nuc_count == cyt_count and nuc_count > 0:
        return (5, "nucleus-cytoplasm")
    elif nuc_count > 0 and cyt_count > nuc_count:
        return (4, "nucleus-cytoplasm")
    elif hpa_nuc and hpa_cyt:
        return (5, "nucleus-cytoplasm")

    if nuc_count == 1:
        return (3, "rejected")
    return (3, "rejected")

# ---- Scoring functions ----
def novelty_scr(pm):
    if pm <= 20: return 10
    elif pm <= 50: return 8
    elif pm <= 100: return 6
    return 0

def size_scr(aa):
    if 200 <= aa <= 800: return 10
    elif (100 <= aa < 200) or (800 < aa <= 1200): return 8
    elif (50 <= aa < 100) or (1200 < aa <= 2000): return 5
    elif aa < 50 or (2000 < aa <= 3000): return 2
    return 0

def struct_scr(packet):
    af = get_af(packet)
    pdb = get_pdb(packet)
    plddt = (af.get("plddt_stats", {}).get("mean_plddt", 0) or 0)
    pdb_n = len(pdb)
    if pdb_n >= 5 and plddt >= 70: return 10
    if pdb_n >= 2 and plddt >= 70: return 9
    if pdb_n >= 1 and plddt >= 70: return 8
    if plddt >= 85: return 8
    if plddt >= 70: return 7
    if plddt >= 50: return 6
    return 4

def domain_scr(packet):
    interpro = get_interpro(packet)
    pfam = get_pfam(packet)
    af = get_af(packet)
    plddt = (af.get("plddt_stats", {}).get("mean_plddt", 0) or 0)

    all_doms = [d.get("name", "") for d in interpro if d.get("name")]
    all_doms += [d.get("name", "") for d in pfam if d.get("name")]
    n_dom = len(all_doms)
    dom_text = " ".join(all_doms).lower()

    chrom_kw = ["bromo", "chromo", "phd", "sant", "tudor", "mbt", "pwwp",
                "zinc finger", "homeobox", "homeodomain", "hmg", "forkhead",
                "bzip", "bhlh", "at-hook", "myb", "cxxc", "histone",
                "chromatin", "dna-binding", "dna binding", "kinase",
                "rna recognition", "rrm", "kh domain", "dead/deah",
                "helicase", "ring", "f-box", "wdr", "ubiquitin", "set",
                "jmjc", "methyltransferase", "acetyltransferase"]

    has_chrom = any(kw in dom_text for kw in chrom_kw)
    if has_chrom and n_dom >= 3: return 10
    if has_chrom or (n_dom >= 2 and plddt >= 80): return 8
    if n_dom > 0: return 7
    if plddt >= 70: return 6
    return 4

REG_KW = [
    "transcription", "chromatin", "histone", "dna", "rna polymer",
    "helicase", "splicing", "rna", "nucleolar", "ribosome",
    "mediator", "coactivator", "corepressor", "deacetylase",
    "acetyltransferase", "methyltransferase", "kinetochore",
    "centromere", "condensin", "cohesin", "smc", "telomere", "repair",
    "topoisomerase", "homeobox", "forkhead", "sox", "pax",
    "zinc finger", "bromodomain", "chromodomain", "set domain",
    "ring finger", "f-box", "kinase", "phosphatase",
]

def ppi_scr(packet):
    string_p = get_string(packet)
    intact_p = get_intact(packet)
    total_s = len(string_p)
    total_i = len(intact_p)

    reg_count = 0
    for p in string_p[:20]:
        partner = (p.get("partner", "") or "").lower()
        exp = float(p.get("experimental", 0) or 0)
        if exp > 0 and any(kw in partner for kw in REG_KW):
            reg_count += 1

    reg_ratio = reg_count / max(min(len(string_p), 20), 1)
    has_phys = total_i > 0
    has_s = total_s > 0

    if has_phys and reg_ratio > 0.4 and total_s >= 10: return (10, reg_count, reg_ratio)
    if has_phys and reg_ratio > 0.2 and total_s >= 5: return (8, reg_count, reg_ratio)
    if has_phys and reg_ratio > 0.3: return (6, reg_count, reg_ratio)
    if has_s and reg_ratio > 0.2: return (4, reg_count, reg_ratio)
    if has_s: return (3, reg_count, reg_ratio)
    return (2, 0, 0.0)

def cross_scr(packet):
    af = get_af(packet)
    pdb = get_pdb(packet)
    string_p = get_string(packet)
    intact_p = get_intact(packet)
    subcell = get_subcell(packet)
    go_cc = get_go_cc(packet)
    domains = get_interpro(packet) + get_pfam(packet)
    plddt = (af.get("plddt_stats", {}).get("mean_plddt", 0) or 0)
    pts = 0.0
    if len(pdb) > 0 and plddt > 0: pts += 0.5
    if subcell and go_cc: pts += 0.5
    if string_p and intact_p: pts += 0.5
    if domains and plddt > 70: pts += 0.5
    if len(pdb) >= 3: pts += 1.0
    return min(pts, 3.0)

# ---- Report writers ----
def write_rejected(gene, packet, reason, nuc_score, pm):
    cat = "rejected"
    rd = DETAIL / cat / gene
    rd.mkdir(parents=True, exist_ok=True)

    length = get_length(packet)
    mass = get_mass(packet, length)
    acc = get_acc(packet)
    prot = get_prot_name(packet)
    ali = "; ".join(get_aliases(packet)[:4]) or gene
    func = get_func(packet)
    subcell = "; ".join([s.get("location", "") for s in get_subcell(packet)[:5]]) or "无"
    go_cc = "; ".join([g.get("term", "") for g in get_go_cc(packet)[:5]]) or "无"
    hpa = get_hpa(packet)
    hpa_locs = "; ".join(hpa.get("subcellular_location", [])) or "无"
    hpa_rel = hpa.get("reliability_if", "")
    papers = get_papers(packet)
    af = get_af(packet)
    plddt = (af.get("plddt_stats", {}).get("mean_plddt", 0) or 0)
    pdb = get_pdb(packet)
    pdb_text = ", ".join([str(p.get("id", "")) for p in pdb[:5]]) or "无"
    string_p = get_string(packet)
    intact_p = get_intact(packet)
    interpro = get_interpro(packet)
    pfam = get_pfam(packet)

    if pm > 100:
        reject_main = "PubMed >100 一票否决（strict=" + str(pm) + "篇文献）。该基因已有大量研究，不符合新颖核蛋白筛选标准。"
    elif nuc_score <= 3:
        reject_main = "核定位信号不足（nuclear_score=" + str(nuc_score) + "）。UniProt定位: " + subcell + "。不符合核蛋白筛选标准，一票否决。"
    else:
        reject_main = reason

    paper_txt = ""
    for p in papers[:3]:
        paper_txt += "- PMID:" + str(p.get("pmid","?")) + " -- " + str(p.get("title","")) + " (" + str(p.get("journal","")) + ", " + str(p.get("pubdate","")) + ")\n"

    domain_txt = "; ".join([str(d.get("name", d.get("id", ""))) for d in interpro[:4] if d.get("name")])
    if not domain_txt:
        domain_txt = "; ".join([str(d.get("name", d.get("id", ""))) for d in pfam[:2] if d.get("name")]) or "无"

    string_list = [str(p.get("partner","?")) + "(" + str(p.get("score",0)) + ")" for p in string_p[:6]]

    report = """---
type: protein-evaluation
gene: \"""" + gene + """"
date: """ + TODAY + """
tags: [protein-scout, rejected]
status: rejected
---

## """ + gene + """ -- 评估报告（REJECTED）

### 1. 基本信息

| 属性 | 值 |
|------|-----|
| **Gene** | """ + gene + """ |
| **Aliases** | """ + ali + """ |
| **Protein** | """ + prot + """ |
| **Length** | """ + str(length) + """ aa |
| **Mass** | """ + str(mass) + """ kDa |
| **UniProt ID** | """ + acc + """ |
| **PubMed strict** | """ + str(pm) + """ |

### 2. 拒绝原因

**核心原因: """ + reject_main + """**

| 指标 | 数值 | 阈值 |
|------|------|------|
| Nuclear Score | """ + str(nuc_score) + """ | >3 required |
| PubMed strict | """ + str(pm) + """ | <=100 required |

### 3. 数据快照

| 维度 | 数据 |
|------|------|
| 核定位 (UniProt) | """ + subcell[:120] + """ |
| GO Cellular Component | """ + go_cc[:120] + """ |
| HPA Localization | """ + hpa_locs + """ (Reliability: """ + str(hpa_rel) + """) |
| AlphaFold pLDDT | """ + str(plddt) + """ |
| PDB | """ + pdb_text + """ |
| InterPro/Pfam | """ + domain_txt[:120] + """ |
| STRING | """ + ", ".join(string_list[:5]) + """ |
| IntAct | """ + str(len(intact_p)) + """ 条互作 |
| Function | """ + func[:200] + """ |

### 4. 关键文献
""" + (paper_txt or "无关键文献") + """

### 5. 评估结论
""" + reject_main + """

不进入评分流程。"""
    with open(rd / (gene + "-evaluation.md"), "w") as f:
        f.write(report)
    return cat


def write_scored(gene, packet, nuc_score, category, pm):
    rd = DETAIL / category / gene
    rd.mkdir(parents=True, exist_ok=True)

    length = get_length(packet)
    mass = get_mass(packet, length)
    acc = get_acc(packet)
    prot = get_prot_name(packet)
    ali = "; ".join(get_aliases(packet)[:4]) or gene
    func = get_func(packet)
    subcell_list = get_subcell(packet)
    subcell_text = "; ".join([s.get("location", "") for s in subcell_list[:5]]) or "无UniProt注释"
    go_cc_list = get_go_cc(packet)
    go_cc_text = "; ".join([g.get("term","") + " (" + g.get("evidence","") + ")" for g in go_cc_list[:8]]) or "无"
    hpa = get_hpa(packet)
    hpa_main = "; ".join(hpa.get("subcellular_main_location", [])) or "无"
    hpa_add = "; ".join(hpa.get("subcellular_additional_location", [])) or ""
    hpa_all = "; ".join(hpa.get("subcellular_location", [])) or "无"
    hpa_rel = hpa.get("reliability_if", "N/A")
    hpa_status = hpa.get("image_status", "no_image_detected")
    papers = get_papers(packet)
    af = get_af(packet)
    plddt_stats = af.get("plddt_stats", {})
    mean_plddt = plddt_stats.get("mean_plddt", 0) or 0
    pct_gt90 = plddt_stats.get("pct_gt_90", 0) or 0
    pct_70_90 = plddt_stats.get("pct_70_90", 0) or 0
    pct_50_70 = plddt_stats.get("pct_50_70", 0) or 0
    pct_lt50 = plddt_stats.get("pct_lt_50", 0) or 0
    pdb_list = get_pdb(packet)
    pdb_count = len(pdb_list)
    interpro = get_interpro(packet)
    pfam = get_pfam(packet)
    all_doms = [d.get("name", d.get("id", "")) for d in interpro if d.get("name")]
    all_doms += [d.get("name", d.get("id", "")) for d in pfam if d.get("name")]
    domain_text = "; ".join(all_doms[:10]) or "无注释域"
    string_p = get_string(packet)
    intact_p = get_intact(packet)
    uni_int = get_uni_int(packet)

    sz = size_scr(length)
    nov = novelty_scr(pm)
    struct = struct_scr(packet)
    dom = domain_scr(packet)
    ppi, reg_count, reg_ratio = ppi_scr(packet)
    cross = cross_scr(packet)

    raw = nuc_score * 4 + sz * 1 + nov * 5 + struct * 3 + dom * 2 + ppi * 3 + cross
    norm = round(raw / 1.83, 1)

    # Descriptions
    if mean_plddt > 80:
        af_desc = "高质量预测（pLDDT " + str(mean_plddt) + "），" + str(int(pct_gt90)) + "%高置信度，" + str(int(pct_lt50)) + "%无序"
    elif mean_plddt >= 70:
        af_desc = "良好质量（pLDDT " + str(mean_plddt) + "），" + str(int(pct_gt90)) + "%高置信度，" + str(int(pct_lt50)) + "%无序"
    else:
        af_desc = "中等质量（pLDDT " + str(mean_plddt) + "），" + str(int(pct_gt90)) + "%高置信度，" + str(int(pct_lt50)) + "%无序"

    if length <= 100:
        sz_desc = "极小蛋白（" + str(length) + " aa），结构域有限"
    elif length <= 200:
        sz_desc = "小蛋白（" + str(length) + " aa），适合结构解析"
    elif length <= 800:
        sz_desc = "中等大小（" + str(length) + " aa），生化实验操作便利"
    elif length <= 1200:
        sz_desc = "偏大蛋白（" + str(length) + " aa），可操作"
    else:
        sz_desc = "大蛋白（" + str(length) + " aa），实验操作有挑战"

    if nov >= 10:
        nov_desc = "极度新颖（PubMed=" + str(pm) + "篇），几乎未被研究，探索空间巨大"
    elif nov >= 8:
        nov_desc = "非常新颖（PubMed=" + str(pm) + "篇），仅有少量基础研究"
    else:
        nov_desc = "有一定研究（PubMed=" + str(pm) + "篇），但核功能可能未被充分探索"

    if struct >= 10:
        struct_desc = "PDB实验结构（" + str(pdb_count) + "个条目）+ AlphaFold高质量预测，结构可信度极高"
    elif struct >= 8:
        extra = "，PDB " + str(pdb_count) + "个条目验证" if pdb_count > 0 else ""
        struct_desc = "AlphaFold高质量预测（pLDDT " + str(mean_plddt) + "），折叠域置信度高" + extra
    elif struct >= 7:
        struct_desc = "AlphaFold中等质量（pLDDT " + str(mean_plddt) + "），有序区" + str(int(pct_gt90 + pct_70_90)) + "%"
    else:
        struct_desc = "AlphaFold低置信度（pLDDT " + str(mean_plddt) + "），作为新颖蛋白属正常现象"

    if dom >= 10:
        dom_desc = "含丰富染色质/转录调控结构域，InterPro+Pfam多库确认"
    elif dom >= 8:
        dom_desc = "含明确核酸结合/信号转导结构域"
    elif dom >= 7:
        dom_desc = "存在注释结构域: " + domain_text[:80] + "... 新颖蛋白基线"
    elif dom >= 5:
        dom_desc = "结构域注释有限，但AlphaFold预测有可辨识折叠域"
    else:
        dom_desc = "结构域注释稀疏，作为新颖蛋白属正常"

    if ppi >= 8:
        ppi_desc = "PPI网络富含调控因子（" + str(reg_count) + "个调控相关），物理互作证据明确"
    elif ppi >= 6:
        ppi_desc = "PPI网络有调控关联（" + str(reg_count) + "个），" + str(len(intact_p)) + "个实验互作"
    elif ppi >= 4:
        ppi_desc = "PPI网络以功能关联为主（" + str(len(string_p)) + "个STRING伙伴），调控关联" + str(reg_count) + "个"
    else:
        ppi_desc = "PPI网络稀薄（" + str(len(string_p)) + "个STRING伙伴），可能为独立功能蛋白"

    if nuc_score >= 8:
        nuc_desc = "明确核定位，多库交叉验证一致"
    elif nuc_score >= 6:
        nuc_desc = "主要核定位，部分胞质信号"
    elif nuc_score >= 5:
        nuc_desc = "核-质分布，可能为穿梭蛋白"
    else:
        nuc_desc = "核定位证据较弱"

    # Pre-compute table rows
    go_cc_rows = "\n".join("- **" + g.get("term", "?") + "** (" + g.get("evidence", "?") + ")" for g in go_cc_list[:8]) if go_cc_list else "- 无 GO-CC 注释"

    pdb_rows = ""
    for p in pdb_list[:10]:
        pdb_rows += "| " + str(p.get("id","?")) + " | " + str(p.get("method","?")) + " | " + str(p.get("resolution","?")) + " | " + str(p.get("chains","?")) + " |\n"
    if not pdb_rows:
        pdb_rows = "| 无 | -- | -- | -- |\n"

    interpro_rows = ""
    for d in interpro[:10]:
        interpro_rows += "| " + str(d.get("id","?")) + " | " + str(d.get("name","?")) + " |\n"
    if not interpro_rows:
        interpro_rows = "| 无 | 无 |\n"

    pfam_rows = ""
    for d in pfam[:5]:
        pfam_rows += "| " + str(d.get("id","?")) + " | " + str(d.get("name","?")) + " |\n"
    if not pfam_rows:
        pfam_rows = "| 无 | 无 |\n"

    string_rows = ""
    sorted_string = sorted(string_p, key=lambda x: float(x.get("score", 0) or 0), reverse=True)[:10]
    for p in sorted_string:
        partner = str(p.get("partner", "?"))
        score = p.get("score", 0)
        exp = float(p.get("experimental", 0) or 0)
        is_reg = "Yes" if any(kw in partner.lower() for kw in REG_KW) else "--"
        string_rows += "| " + partner + " | " + str(round(score, 3)) + " | " + str(round(exp, 3)) + " | " + is_reg + " |\n"

    intact_top = []
    seen = set()
    for p in intact_p:
        partner = str(p.get("partner", "?"))
        if partner in seen:
            continue
        seen.add(partner)
        method = str(p.get("method", "--"))[:40]
        pmid = str(p.get("pmid", "--"))[:25]
        itype = str(p.get("interaction_type", "--"))[:30]
        is_reg = "Yes" if any(kw in partner.lower() for kw in REG_KW) else "--"
        intact_top.append((partner, method, pmid, itype, is_reg))
        if len(intact_top) >= 8:
            break

    intact_rows = ""
    for (partner, method, pmid, itype, is_reg) in intact_top:
        intact_rows += "| " + partner + " | " + method + " | " + pmid + " | " + itype + " | " + is_reg + " |\n"

    uni_int_rows = ""
    for ui in uni_int[:10]:
        uni_int_rows += "- " + str(ui.get("gene","?")) + " (" + str(ui.get("experiments","?")) + " experiments)\n"
    if not uni_int_rows:
        uni_int_rows = "- 无 UniProt 互作注释\n"

    paper_txt = ""
    for p in papers[:5]:
        paper_txt += "- PMID:" + str(p.get("pmid","?")) + " -- " + str(p.get("title",""))[:120] + " (" + str(p.get("journal","")) + ", " + str(p.get("pubdate","")) + ")\n"

    # PAE
    pae_embed = ""
    pae_path = rd / (gene + "-PAE.png")
    if pae_path.exists() and pae_path.stat().st_size > 500:
        pae_embed = "![[Projects/TEreg-finding/protein-interested/detail/" + category + "/" + gene + "/" + gene + "-PAE.png]]\n\n"
    else:
        pae_embed = "PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。\n"

    # IF
    if_embed = ""
    if_dir = rd / "IF_images"
    if if_dir.exists():
        jpgs = sorted([f for f in if_dir.iterdir() if f.suffix == ".jpg"])
        for jpg in jpgs[:2]:
            if_embed += "![[Projects/TEreg-finding/protein-interested/detail/" + category + "/" + gene + "/IF_images/" + jpg.name + "|HPA IF]]\n"
    if not if_embed:
        if_embed = "暂无数据（Pending cell analysis），核定位基于 UniProt + GO + HPA 注释。\n"

    if hpa_status == "if_display_images_available":
        hpa_if_note = "HPA IF 可显示图像可用，可靠性: " + str(hpa_rel) + "。"
    elif hpa_status == "no_image_detected":
        hpa_if_note = "HPA IF 原图未可靠获取（HPA 检索页无可用的 subcellular IF 原图）。核定位基于 HPA localization/reliability + UniProt + GO-CC。"
    else:
        hpa_if_note = "HPA 数据状态: " + str(hpa_status) + "，可靠性: " + str(hpa_rel) + "。"

    hpa_yesno = "YES" if hpa_status == "if_display_images_available" else "NO"

    research_vol = "非常低（<10篇），几乎未被研究，是探索新型核蛋白功能的绝佳候选"
    if 10 < pm <= 50:
        research_vol = "较低（<50篇），研究空间充足"
    elif 50 < pm <= 100:
        research_vol = "中等（<100篇），已有一定研究基础但仍存在未探索的niche"
    elif pm > 100:
        research_vol = "高（>100篇），大量文献积累"

    if norm >= 50:
        final_decision = "VALIDATED CANDIDATE"
    elif norm >= 35:
        final_decision = "BORDERLINE CANDIDATE, RETAINED CONDITIONALLY"
    else:
        final_decision = "LOW PRIORITY"

    nov_strength = "研究新颖性极高" if nov >= 8 else "有一定研究空间"
    struct_strength = "结构数据充分（PDB实验结构+AlphaFold）" if struct >= 8 else "AlphaFold结构可用"
    nuc_weakness = "核定位证据较弱，需HPA IF验证" if nuc_score < 6 else "核定位需HPA进一步确认"
    dom_weakness = "- 结构域注释有限\n" if dom < 7 else ""
    ppi_weakness = "- PPI网络稀薄\n" if ppi < 5 else ""

    report = """---
type: protein-evaluation
gene: \"""" + gene + """"
date: """ + TODAY + """
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: """ + str(nuc_score) + """
---

## """ + gene + """ (""" + prot + """) -- 评估报告

### 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | """ + acc + """ |
| **Protein Name** | """ + prot + """ |
| **Aliases** | """ + ali + """ |
| **Length** | """ + str(length) + """ aa |
| **Mass** | """ + str(mass) + """ kDa |
| **AlphaFold mean pLDDT** | """ + str(mean_plddt) + """ |
| **AlphaFold pLDDT >90** | """ + str(pct_gt90) + """% |
| **AlphaFold pLDDT <50** | """ + str(pct_lt50) + """% |
| **PubMed (strict)** | """ + str(pm) + """ |
| **Function** | """ + func[:300] + """ |

### 2. 核定位证据

#### UniProt Subcellular Location
""" + subcell_text + """

#### GO Cellular Component
""" + go_cc_rows + """

#### HPA Subcellular Localization
- **Main location**: """ + hpa_main + """
- **Additional locations**: """ + (hpa_add or "无") + """
- **Reliability (IF)**: """ + str(hpa_rel) + """
- **IF Display Images Available**: """ + hpa_yesno + """

""" + hpa_if_note + """

### 3. HPA Immunofluorescence

""" + if_embed + """
""" + hpa_if_note + """

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | """ + str(pm) + """ |

**Key Papers:**
""" + (paper_txt or "无关键文献数据") + """

**Research Volume Assessment**: """ + research_vol + """

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: """ + str(mean_plddt) + """
- pLDDT >90: """ + str(pct_gt90) + """%, 70-90: """ + str(pct_70_90) + """%, 50-70: """ + str(pct_50_70) + """%, <50: """ + str(pct_lt50) + """%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
""" + pdb_rows + """**Structure Assessment**: """ + struct_desc + """

""" + pae_embed + """
### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
""" + interpro_rows + """
| Pfam | Description |
|------|-------------|
""" + pfam_rows + """
**Domain Assessment**: """ + dom_desc + """

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
""" + (string_rows or "| -- | -- | -- | -- |\\n") + """
#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
""" + (intact_rows or "| -- | -- | -- | -- | -- |\\n") + """
#### UniProt Interactions
""" + uni_int_rows + """
**PPI Assessment**: """ + ppi_desc + """

### 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | """ + str(nuc_score) + """/10 | x4 | """ + str(nuc_score*4) + """ | """ + nuc_desc + """ |
| 蛋白大小 | """ + str(sz) + """/10 | x1 | """ + str(sz) + """ | """ + sz_desc + """ |
| 研究新颖性 | """ + str(nov) + """/10 | x5 | """ + str(nov*5) + """ | """ + nov_desc + """ |
| 三维结构 | """ + str(struct) + """/10 | x3 | """ + str(struct*3) + """ | """ + af_desc + """ |
| 调控结构域 | """ + str(dom) + """/10 | x2 | """ + str(dom*2) + """ | """ + dom_desc[:60] + """ |
| PPI 网络 | """ + str(ppi) + """/10 | x3 | """ + str(ppi*3) + """ | """ + ppi_desc[:60] + """ |
| **加权总分** | | | **""" + str(raw) + """/180** | |
| **归一化总分** | | | **""" + str(norm) + """/100** | |

### 9. Final Decision

**SCORED: """ + str(norm) + """/100 -- """ + final_decision + """**

**Strengths:**
- PubMed """ + str(pm) + """ 篇，""" + nov_strength + """
- """ + sz_desc + """
- """ + struct_strength + """

**Weaknesses:**
- """ + nuc_weakness + """
""" + dom_weakness + ppi_weakness + """
### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/""" + acc + """
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22""" + gene + """%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/""" + acc + """
- STRING: https://string-db.org/cgi/network?identifiers=""" + gene + """&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/""" + gene + """
"""
    with open(rd / (gene + "-evaluation.md"), "w") as f:
        f.write(report)
    return category


def main():
    print("=== Processing " + str(len(TODO)) + " genes: " + " ".join(TODO[:5]) + "... ===")
    results = {"rejected": [], "scored": [], "errors": []}

    for i, gene in enumerate(TODO):
        print("\n[" + str(i+1) + "/" + str(len(TODO)) + "] " + gene + "...", end=" ", flush=True)

        packet_path = PACKET_DIR / (gene + ".json")
        if packet_path.exists():
            print("packet cached", end=" ")
            try:
                with open(packet_path) as f:
                    packet = json.load(f)
            except Exception:
                print("PARSE ERROR, re-harvesting")
                packet = harvest_gene(gene)
                packet_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")
        else:
            print("harvesting...", end=" ", flush=True)
            try:
                packet = harvest_gene(gene)
                packet_path.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")
            except Exception as e:
                print("HARVEST ERROR: " + str(e))
                results["errors"].append((gene, str(e)))
                continue

        pm = get_pubmed_count(packet)
        nuc_score, category = compute_nuc_score(packet)

        print("PubMed=" + str(pm) + " Nuc=" + str(nuc_score), end=" ", flush=True)

        if pm > 100:
            write_rejected(gene, packet, "PubMed >100 (strict=" + str(pm) + ")", nuc_score, pm)
            results["rejected"].append(gene + "(PubMed>" + str(pm) + ")")
            print("REJECTED (PubMed>100)")
        elif nuc_score <= 3:
            subcell = "; ".join([s.get("location", "") for s in get_subcell(packet)[:3]]) or ""
            write_rejected(gene, packet, "Nuclear score <=3 (" + str(nuc_score) + "), subcell=" + subcell, nuc_score, pm)
            results["rejected"].append(gene + "(nuc=" + str(nuc_score) + ")")
            print("REJECTED (nuc<=" + str(nuc_score) + ")")
        else:
            write_scored(gene, packet, nuc_score, category, pm)
            results["scored"].append(gene + "(" + category + ",nuc=" + str(nuc_score) + ")")
            print("SCORED -> " + category)

        time.sleep(0.3)

    print("\n" + "=" * 60)
    print("COMPLETE: " + str(len(results["scored"])) + " scored, " + str(len(results["rejected"])) + " rejected, " + str(len(results["errors"])) + " errors")
    print("\nScored (" + str(len(results["scored"])) + "):")
    for s in results["scored"]:
        print("  " + s)
    print("\nRejected (" + str(len(results["rejected"])) + "):")
    for r in results["rejected"]:
        print("  " + r)
    if results["errors"]:
        print("\nErrors (" + str(len(results["errors"])) + "):")
        for e in results["errors"]:
            print("  " + str(e[0]) + ": " + str(e[1]))

if __name__ == "__main__":
    main()
