#!/usr/bin/env python3
"""Harvest + write /180 evaluation reports for 63 remaining C/D genes."""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data")
from protein_scout_harvest import (
    uniprot_entry, alphafold, pubmed, string_partners, intact_partners, hpa_probe,
    safe_call,
)

BASE = Path("/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested")
DETAIL = BASE / "detail"
PACKET_DIR = Path("/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets")
TODAY = "2026-06-03"

TODO = [
    "CNPY1", "CNPY3", "CNTFR", "COA3", "COA5", "COA6", "COA7", "COG7", "COLCA2",
    "COMTD1", "COPS7A", "COPS7B", "COPS8", "COPS9", "COQ4", "COQ9", "CORO1C", "COX14",
    "CPLX2", "CPNE5", "CPSF4", "CPSF6", "CPSF7", "CRACR2A", "CRBN", "CREB1",
    "CRK", "CRLF3", "CRLS1", "CRNKL1", "CRY1", "CRY2", "CRYM", "CRYBG2", "CSAD", "CSDE1",
    "CSTF2", "CSTPP1", "CTAGE6", "CTCF", "CTR9", "CTTNBP2",
    "CXXC4", "CXorf56", "CYB5R1", "CYB5R3", "DACH1", "DAGLA", "DBNDD2",
    "DCAF1", "DCAF16", "DCAF4L1", "DCLRE1C", "DCTN1", "DDAH2", "DDX55",
    "DELE1", "DENND10", "DGCR14"
]

def harvest_gene(gene):
    packet = {"gene": gene, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}
    print(f"  UniProt...", end=" ", flush=True)
    uni = safe_call(uniprot_entry, gene)
    packet["uniprot"] = uni
    accession = uni.get("data", {}).get("accession") if uni.get("ok") else None
    aliases = uni.get("data", {}).get("aliases", []) if uni.get("ok") else []

    print(f"AF...", end=" ", flush=True)
    packet["alphafold"] = safe_call(alphafold, accession, retries=2)
    time.sleep(0.1)

    print(f"PubMed...", end=" ", flush=True)
    packet["pubmed"] = safe_call(pubmed, gene, aliases, retries=3)
    time.sleep(0.1)

    print(f"STRING...", end=" ", flush=True)
    packet["string"] = safe_call(string_partners, gene, retries=3)
    time.sleep(0.1)

    print(f"IntAct...", end=" ", flush=True)
    packet["intact"] = safe_call(intact_partners, gene, retries=2)
    time.sleep(0.1)

    print(f"HPA...", end=" ", flush=True)
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
    subcell = "; ".join([s.get("location", "") for s in get_subcell(packet)[:5]]) or "N/A"
    go_cc = "; ".join([g.get("term", "") for g in get_go_cc(packet)[:5]]) or "N/A"
    hpa = get_hpa(packet)
    hpa_locs = "; ".join(hpa.get("subcellular_location", [])) or "N/A"
    hpa_rel = hpa.get("reliability_if", "")
    papers = get_papers(packet)
    af = get_af(packet)
    plddt = (af.get("plddt_stats", {}).get("mean_plddt", 0) or 0)
    pdb = get_pdb(packet)
    pdb_text = ", ".join([str(p.get("id", "")) for p in pdb[:5]]) or "N/A"
    string_p = get_string(packet)
    intact_p = get_intact(packet)
    interpro = get_interpro(packet)
    pfam = get_pfam(packet)

    if pm > 100:
        reject_main = "PubMed >100 one-vote rejection (strict=" + str(pm) + " papers). This gene has extensive literature, does not meet novel nuclear protein screening criteria."
    elif nuc_score <= 3:
        reject_main = "Insufficient nuclear localization (nuclear_score=" + str(nuc_score) + "). UniProt: " + subcell + ". Does not meet nuclear protein screening criteria."
    else:
        reject_main = reason

    paper_txt = ""
    for p in papers[:3]:
        paper_txt += "- PMID:" + str(p.get("pmid","?")) + " -- " + str(p.get("title","")) + " (" + str(p.get("journal","")) + ", " + str(p.get("pubdate","")) + ")\n"

    domain_txt = "; ".join([str(d.get("name", d.get("id", ""))) for d in interpro[:4] if d.get("name")])
    if not domain_txt:
        domain_txt = "; ".join([str(d.get("name", d.get("id", ""))) for d in pfam[:2] if d.get("name")]) or "N/A"

    string_list = [str(p.get("partner","?")) + "(" + str(p.get("score",0)) + ")" for p in string_p[:6]]

    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: {TODAY}
tags: [protein-scout, rejected]
status: rejected
---

## {gene} -- Evaluation Report (REJECTED)

### 1. Basic Info

| Property | Value |
|------|-----|
| **Gene** | {gene} |
| **Aliases** | {ali} |
| **Protein** | {prot} |
| **Length** | {length} aa |
| **Mass** | {mass} kDa |
| **UniProt ID** | {acc} |
| **PubMed strict** | {pm} |

### 2. Rejection Reason

**Core Reason: {reject_main}**

| Metric | Value | Threshold |
|------|------|------|
| Nuclear Score | {nuc_score} | >3 required |
| PubMed strict | {pm} | <=100 required |

### 3. Data Snapshot

| Dimension | Data |
|------|------|
| Nuclear Localization (UniProt) | {subcell[:120]} |
| GO Cellular Component | {go_cc[:120]} |
| HPA Localization | {hpa_locs} (Reliability: {hpa_rel}) |
| AlphaFold pLDDT | {plddt} |
| PDB | {pdb_text} |
| InterPro/Pfam | {domain_txt[:120]} |
| STRING | {", ".join(string_list[:5])} |
| IntAct | {len(intact_p)} interactions |
| Function | {func[:200]} |

### 4. Key Literature
{paper_txt or "No key papers"}

### 5. Conclusion
{reject_main}

Not entered into scoring process."""
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
    subcell_text = "; ".join([s.get("location", "") for s in subcell_list[:5]]) or "No UniProt annotation"
    go_cc_list = get_go_cc(packet)
    go_cc_text = "; ".join([g.get("term","") + " (" + g.get("evidence","") + ")" for g in go_cc_list[:8]]) or "N/A"
    hpa = get_hpa(packet)
    hpa_main = "; ".join(hpa.get("subcellular_main_location", [])) or "N/A"
    hpa_add = "; ".join(hpa.get("subcellular_additional_location", [])) or ""
    hpa_all = "; ".join(hpa.get("subcellular_location", [])) or "N/A"
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
    domain_text = "; ".join(all_doms[:10]) or "No annotated domains"
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
        af_desc = f"High quality (pLDDT {mean_plddt}), {int(pct_gt90)}% high confidence, {int(pct_lt50)}% disordered"
    elif mean_plddt >= 70:
        af_desc = f"Good quality (pLDDT {mean_plddt}), {int(pct_gt90)}% high confidence, {int(pct_lt50)}% disordered"
    else:
        af_desc = f"Moderate quality (pLDDT {mean_plddt}), {int(pct_gt90)}% high confidence, {int(pct_lt50)}% disordered"

    if length <= 100:
        sz_desc = f"Very small ({length} aa), limited domains"
    elif length <= 200:
        sz_desc = f"Small ({length} aa), suitable for structural studies"
    elif length <= 800:
        sz_desc = f"Medium ({length} aa), convenient for biochemical experiments"
    elif length <= 1200:
        sz_desc = f"Large ({length} aa), manageable"
    else:
        sz_desc = f"Very large ({length} aa), challenging for experiments"

    if nov >= 10:
        nov_desc = f"Extremely novel (PubMed={pm} papers), nearly unstudied, huge exploration space"
    elif nov >= 8:
        nov_desc = f"Very novel (PubMed={pm} papers), only limited foundational research"
    else:
        nov_desc = f"Some research (PubMed={pm} papers), but nuclear function may be underexplored"

    if struct >= 10:
        struct_desc = f"PDB experimental structures ({pdb_count} entries) + high-quality AlphaFold, very high confidence"
    elif struct >= 8:
        extra = f", PDB {pdb_count} entries verified" if pdb_count > 0 else ""
        struct_desc = f"High-quality AlphaFold prediction (pLDDT {mean_plddt}), fold confidence high{extra}"
    elif struct >= 7:
        struct_desc = f"AlphaFold moderate quality (pLDDT {mean_plddt}), ordered region {int(pct_gt90 + pct_70_90)}%"
    else:
        struct_desc = f"AlphaFold low confidence (pLDDT {mean_plddt}), normal for novel proteins"

    if dom >= 10:
        dom_desc = "Rich chromatin/transcription regulatory domains, InterPro+Pfam multi-db confirmed"
    elif dom >= 8:
        dom_desc = "Clear nucleic acid binding/signal transduction domains"
    elif dom >= 7:
        dom_desc = f"Annotated domains present: {domain_text[:80]}... Novel protein baseline"
    elif dom >= 5:
        dom_desc = "Limited domain annotation, but AlphaFold predicts identifiable fold domains"
    else:
        dom_desc = "Sparse domain annotation, normal for novel proteins"

    if ppi >= 8:
        ppi_desc = f"PPI network enriched with regulators ({reg_count} regulatory partners), physical interaction evidence clear"
    elif ppi >= 6:
        ppi_desc = f"PPI network has regulatory links ({reg_count}), {len(intact_p)} experimental interactions"
    elif ppi >= 4:
        ppi_desc = f"PPI network mainly functional associations ({len(string_p)} STRING partners), {reg_count} regulatory links"
    else:
        ppi_desc = f"Sparse PPI network ({len(string_p)} STRING partners), possibly independent function protein"

    if nuc_score >= 8:
        nuc_desc = "Clear nuclear localization, multi-db cross-validated"
    elif nuc_score >= 6:
        nuc_desc = "Mainly nuclear localization, some cytoplasmic signal"
    elif nuc_score >= 5:
        nuc_desc = "Nucleo-cytoplasmic distribution, possibly shuttling protein"
    else:
        nuc_desc = "Weak nuclear localization evidence"

    # Pre-compute table rows
    go_cc_rows = "\n".join("- **" + g.get("term", "?") + "** (" + g.get("evidence", "?") + ")" for g in go_cc_list[:8]) if go_cc_list else "- No GO-CC annotation"

    pdb_rows = ""
    for p in pdb_list[:10]:
        pdb_rows += "| " + str(p.get("id","?")) + " | " + str(p.get("method","?")) + " | " + str(p.get("resolution","?")) + " | " + str(p.get("chains","?")) + " |\n"
    if not pdb_rows:
        pdb_rows = "| None | -- | -- | -- |\n"

    interpro_rows = ""
    for d in interpro[:10]:
        interpro_rows += "| " + str(d.get("id","?")) + " | " + str(d.get("name","?")) + " |\n"
    if not interpro_rows:
        interpro_rows = "| None | None |\n"

    pfam_rows = ""
    for d in pfam[:5]:
        pfam_rows += "| " + str(d.get("id","?")) + " | " + str(d.get("name","?")) + " |\n"
    if not pfam_rows:
        pfam_rows = "| None | None |\n"

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
    if not intact_rows:
        intact_rows = "| -- | -- | -- | -- | -- |\n"

    uni_int_rows = ""
    for ui in uni_int[:10]:
        uni_int_rows += "- " + str(ui.get("gene","?")) + " (" + str(ui.get("experiments","?")) + " experiments)\n"
    if not uni_int_rows:
        uni_int_rows = "- No UniProt interaction annotations\n"

    paper_txt = ""
    for p in papers[:5]:
        paper_txt += "- PMID:" + str(p.get("pmid","?")) + " -- " + str(p.get("title",""))[:120] + " (" + str(p.get("journal","")) + ", " + str(p.get("pubdate","")) + ")\n"

    # PAE
    pae_embed = ""
    pae_path = rd / (gene + "-PAE.png")
    if pae_path.exists() and pae_path.stat().st_size > 500:
        pae_embed = "![[Projects/TEreg-finding/protein-interested/detail/" + category + "/" + gene + "/" + gene + "-PAE.png]]\n\n"
    else:
        pae_embed = "PAE image data not yet available (local image not generated or not reliably fetched), structural assessment based on AlphaFold pLDDT statistics.\n"

    # IF
    if_embed = ""
    if_dir = rd / "IF_images"
    if if_dir.exists():
        jpgs = sorted([f for f in if_dir.iterdir() if f.suffix == ".jpg"])
        for jpg in jpgs[:2]:
            if_embed += "![[Projects/TEreg-finding/protein-interested/detail/" + category + "/" + gene + "/IF_images/" + jpg.name + "|HPA IF]]\n"
    if not if_embed:
        if_embed = "No data (Pending cell analysis), nuclear localization based on UniProt + GO + HPA annotations.\n"

    if hpa_status == "if_display_images_available":
        hpa_if_note = f"HPA IF display images available, reliability: {hpa_rel}."
    elif hpa_status == "no_image_detected":
        hpa_if_note = "HPA IF images not reliably obtained (no subcellular IF images available on HPA search page). Nuclear localization based on HPA localization/reliability + UniProt + GO-CC."
    else:
        hpa_if_note = f"HPA data status: {hpa_status}, reliability: {hpa_rel}."

    hpa_yesno = "YES" if hpa_status == "if_display_images_available" else "NO"

    research_vol = "Very low (<10 papers), nearly unstudied, excellent candidate for exploring novel nuclear protein function"
    if 10 < pm <= 50:
        research_vol = "Low (<50 papers), ample research space"
    elif 50 < pm <= 100:
        research_vol = "Moderate (<100 papers), some research foundation but unexplored niches remain"
    elif pm > 100:
        research_vol = "High (>100 papers), extensive literature accumulation"

    if norm >= 50:
        final_decision = "VALIDATED CANDIDATE"
    elif norm >= 35:
        final_decision = "BORDERLINE CANDIDATE, RETAINED CONDITIONALLY"
    else:
        final_decision = "LOW PRIORITY"

    nov_strength = "Extremely high research novelty" if nov >= 8 else "Some research space"
    struct_strength = "Sufficient structural data (PDB experimental + AlphaFold)" if struct >= 8 else "AlphaFold structure usable"
    nuc_weakness = "Nuclear localization evidence weak, HPA IF validation needed" if nuc_score < 6 else "Nuclear localization needs further HPA confirmation"
    dom_weakness = "- Limited domain annotation\n" if dom < 7 else ""
    ppi_weakness = "- Sparse PPI network\n" if ppi < 5 else ""
    no_data_row = "| -- | -- | -- | -- |\n"

    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: {TODAY}
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: {nuc_score}
---

## {gene} ({prot}) -- Evaluation Report

### 1. Basic Info

| Property | Value |
|------|-----|
| **UniProt ID** | {acc} |
| **Protein Name** | {prot} |
| **Aliases** | {ali} |
| **Length** | {length} aa |
| **Mass** | {mass} kDa |
| **AlphaFold mean pLDDT** | {mean_plddt} |
| **AlphaFold pLDDT >90** | {pct_gt90}% |
| **AlphaFold pLDDT <50** | {pct_lt50}% |
| **PubMed (strict)** | {pm} |
| **Function** | {func[:300]} |

### 2. Nuclear Localization Evidence

#### UniProt Subcellular Location
{subcell_text}

#### GO Cellular Component
{go_cc_rows}

#### HPA Subcellular Localization
- **Main location**: {hpa_main}
- **Additional locations**: {hpa_add or "None"}
- **Reliability (IF)**: {hpa_rel}
- **IF Display Images Available**: {hpa_yesno}

{hpa_if_note}

### 3. HPA Immunofluorescence

{if_embed}
{hpa_if_note}

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | {pm} |

**Key Papers:**
{paper_txt or "No key literature data"}

**Research Volume Assessment**: {research_vol}

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: {mean_plddt}
- pLDDT >90: {pct_gt90}%, 70-90: {pct_70_90}%, 50-70: {pct_50_70}%, <50: {pct_lt50}%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
{pdb_rows}**Structure Assessment**: {struct_desc}

{pae_embed}
### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
{interpro_rows}
| Pfam | Description |
|------|-------------|
{pfam_rows}
**Domain Assessment**: {dom_desc}

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
{string_rows or no_data_row}
#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
{intact_rows}
#### UniProt Interactions
{uni_int_rows}
**PPI Assessment**: {ppi_desc}

### 8. Scoring Overview

| Dimension | Score | Weight | Weighted | Summary |
|------|------|------|------|------|
| Nuclear Localization | {nuc_score}/10 | x4 | {nuc_score*4} | {nuc_desc} |
| Protein Size | {sz}/10 | x1 | {sz} | {sz_desc} |
| Research Novelty | {nov}/10 | x5 | {nov*5} | {nov_desc} |
| 3D Structure | {struct}/10 | x3 | {struct*3} | {af_desc} |
| Regulatory Domains | {dom}/10 | x2 | {dom*2} | {dom_desc[:60]} |
| PPI Network | {ppi}/10 | x3 | {ppi*3} | {ppi_desc[:60]} |
| **Weighted Total** | | | **{raw}/180** | |
| **Normalized Total** | | | **{norm}/100** | |

### 9. Final Decision

**SCORED: {norm}/100 -- {final_decision}**

**Strengths:**
- PubMed {pm} papers, {nov_strength}
- {sz_desc}
- {struct_strength}

**Weaknesses:**
- {nuc_weakness}
{dom_weakness}{ppi_weakness}
### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/{acc}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22{gene}%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/{acc}
- STRING: https://string-db.org/cgi/network?identifiers={gene}&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/{gene}
"""
    with open(rd / (gene + "-evaluation.md"), "w") as f:
        f.write(report)
    return category


def main():
    print(f"=== Processing {len(TODO)} genes ===")
    results = {"rejected": [], "scored": [], "errors": []}

    for i, gene in enumerate(TODO):
        print(f"\n[{i+1}/{len(TODO)}] {gene}...", end=" ", flush=True)

        packet_path = PACKET_DIR / (gene + ".json")
        if packet_path.exists():
            print("packet cached", end=" ")
            try:
                with open(packet_path) as f:
                    packet = json.load(f)
            except Exception:
                print("PARSE ERROR, re-harvesting")
                packet = harvest_gene(gene)
                with open(packet_path, "w") as f:
                    json.dump(packet, f, ensure_ascii=False, indent=2)
                    f.write("\n")
        else:
            print("harvesting...", end=" ", flush=True)
            try:
                packet = harvest_gene(gene)
                with open(packet_path, "w") as f:
                    json.dump(packet, f, ensure_ascii=False, indent=2)
                    f.write("\n")
            except Exception as e:
                print(f"HARVEST ERROR: {e}")
                results["errors"].append((gene, str(e)))
                continue

        pm = get_pubmed_count(packet)
        nuc_score, category = compute_nuc_score(packet)

        print(f"PubMed={pm} Nuc={nuc_score}", end=" ", flush=True)

        if pm > 100:
            write_rejected(gene, packet, f"PubMed >100 (strict={pm})", nuc_score, pm)
            results["rejected"].append(f"{gene}(PubMed>{pm})")
            print("REJECTED (PubMed>100)")
        elif nuc_score <= 3:
            subcell = "; ".join([s.get("location", "") for s in get_subcell(packet)[:3]]) or ""
            write_rejected(gene, packet, f"Nuclear score <=3 ({nuc_score}), subcell={subcell}", nuc_score, pm)
            results["rejected"].append(f"{gene}(nuc={nuc_score})")
            print(f"REJECTED (nuc<={nuc_score})")
        else:
            write_scored(gene, packet, nuc_score, category, pm)
            results["scored"].append(f"{gene}({category},nuc={nuc_score})")
            print(f"SCORED -> {category}")

        time.sleep(0.15)

    print("\n" + "=" * 60)
    print(f"COMPLETE: {len(results['scored'])} scored, {len(results['rejected'])} rejected, {len(results['errors'])} errors")
    print(f"\nScored ({len(results['scored'])}):")
    for s in results["scored"]:
        print(f"  {s}")
    print(f"\nRejected ({len(results['rejected'])}):")
    for r in results["rejected"]:
        print(f"  {r}")
    if results["errors"]:
        print(f"\nErrors ({len(results['errors'])}):")
        for e in results["errors"]:
            print(f"  {e[0]}: {e[1]}")

if __name__ == "__main__":
    main()
