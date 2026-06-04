#!/usr/bin/env python3
"""Generate /180 full reports for D batch genes from harvest packets."""
import json, os

BASE = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested"
DETAIL = os.path.join(BASE, "detail")
PACKETS = "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets"
TODAY = "2026-06-02"

GENES = [
    "CAPS2", "CARD8", "CARF", "CASD1", "CASKIN1", "CBLC", "CBR3", "CC2D1B",
    "CCDC110", "CCDC112", "CCDC117", "CCDC12", "CCDC122", "CCDC141", "CCDC148",
    "CCDC159", "CCDC169", "CCDC39", "CCDC59", "CCDC61", "CCDC74A", "CCDC77",
    "CCDC8", "CCDC85B", "CCDC88B", "CCDC91", "CCDC97", "CCDC9B", "CCER1", "CCT8"
]

def load_packet(gene):
    path = os.path.join(PACKETS, f"{gene}.json")
    with open(path) as f:
        return json.load(f)

def score_nuclear(uniprot_data, hpa_data):
    """Score nuclear localization 0-10."""
    locs = []
    if uniprot_data:
        subcell = uniprot_data.get("subcellular_locations", [])
        for s in subcell:
            locs.append(s.get("location", "").lower())
    loc_str = " ".join(locs)

    hpa_locs = []
    if hpa_data:
        hpa_locs = [l.lower() for l in hpa_data.get("subcellular_location", [])]
        hpa_main = [l.lower() for l in hpa_data.get("subcellular_main_location", [])]
        hpa_addl = [l.lower() for l in hpa_data.get("subcellular_additional_location", [])]

    hpa_loc_str = " ".join(hpa_locs)
    hpa_main_str = " ".join(hpa_main)

    # Check HPA first
    hpa_nuclear = any(kw in hpa_main_str for kw in ["nucleoplasm", "nucleoli", "nucleus", "nuclear"])
    hpa_nuclear_addl = any(kw in hpa_loc_str for kw in ["nucleoplasm", "nucleoli", "nucleus", "nuclear"])

    # Check UniProt
    uni_nuclear = any("nucleus" in l or "nucleoplasm" in l or "nucleoli" in l or "nuclear" in l for l in locs)
    uni_cyto = any("cytoplasm" in l or "cytosol" in l for l in locs)
    uni_other = any("membrane" in l and "nuclear" not in l for l in locs) or \
                any("secreted" in l for l in locs) or \
                any("mitochond" in l for l in locs) or \
                any("endoplasmic" in l for l in locs)

    # Function text hints
    func_text = ""
    if uniprot_data:
        funcs = uniprot_data.get("function", [])
        func_text = " ".join(funcs).lower()
    is_tf = any(kw in func_text for kw in ["transcription factor", "homeobox", "dna-binding",
                                            "dna binding", "transcriptional repressor",
                                            "transcriptional activator", "chromatin"])

    # Scoring logic
    if hpa_nuclear and not hpa_nuclear_addl:
        # HPA primary nuclear
        if is_tf:
            return 9, "HPA主定位核 + UniProt转录因子/DNA结合功能"
        return 8, "HPA主定位核（Nucleoplasm/Nucleoli），UniProt确认"

    if hpa_nuclear:
        # HPA main nuclear but has additional non-nuclear
        has_hpa_cyto = any("cytosol" in l or "cytoplasm" in l for l in hpa_addl)
        if is_tf:
            return 8, "HPA主定位核 + 转录因子功能，附加胞质信号"
        if has_hpa_cyto:
            return 6, "HPA主定位核，附加Cytosol/Vesicles"
        return 7, "HPA主定位核"

    if hpa_nuclear_addl:
        # HPA has nuclear as additional
        if is_tf:
            return 6, "HPA附加核定位 + 转录因子功能提示核为主"
        return 4, "HPA核为附加定位，主定位非核"

    # No HPA nuclear
    if uni_nuclear and not uni_cyto and not uni_other:
        if is_tf:
            return 7, "UniProt单一核定位 + 转录因子/DNA结合功能"
        return 5, "UniProt单一核定位，但无HPA IF核验证"

    if uni_nuclear and uni_cyto:
        if is_tf:
            return 5, "UniProt Nucleus+Cytoplasm + 转录因子功能提示核为主"
        return 3, "UniProt Nucleus+Cytoplasm (核质双分布)"

    if uni_nuclear and uni_other:
        return 3, "UniProt Nucleus+其他区室，非特异核定位"

    if uni_cyto and not uni_nuclear:
        return 1, "UniProt Cytoplasm only"

    if uni_other:
        return 0, "Primary non-nuclear location"

    return 2, "无明确核定位证据"


def score_size(length):
    if 200 <= length <= 800:
        return 10, f"{length} aa (200-800 aa ideal range)"
    elif 100 <= length < 200 or 800 < length <= 1200:
        return 8, f"{length} aa (acceptable range)"
    elif 50 <= length < 100 or 1200 < length <= 2000:
        return 5, f"{length} aa (small or large)"
    elif length < 50:
        return 2, f"{length} aa (<50 aa, very small)"
    elif 2000 < length <= 3000:
        return 2, f"{length} aa (2000-3000 aa, very large)"
    else:
        return 0, f"{length} aa (>3000 aa)"


def novelty_score(pubmed):
    if pubmed <= 20:
        return 10
    elif pubmed <= 50:
        return 8
    elif pubmed <= 100:
        return 6
    return 4


def score_structure(af_data, pdb_list, pubmed):
    plddt_m = af_data.get("mean_plddt", 0) if af_data else 0
    pct_gt70 = (af_data.get("pct_gt_90", 0) + af_data.get("pct_70_90", 0)) if af_data else 0
    pdb_count = len([p for p in (pdb_list or []) if p])

    if pdb_count >= 5 and plddt_m >= 70:
        return 10, f"PDB实验结构({pdb_count}条目) + AlphaFold高质量(pLDDT={plddt_m})"
    elif pdb_count >= 2 and plddt_m >= 70:
        return 9, f"PDB实验结构({pdb_count}条目) + AlphaFold质量(pLDDT={plddt_m})"
    elif pdb_count >= 1 and plddt_m >= 70:
        return 8, f"PDB实验结构({pdb_count}条目) + AlphaFold(pLDDT={plddt_m})"
    elif plddt_m >= 85:
        return 8, f"AlphaFold高质量(pLDDT={plddt_m}, >70%={pct_gt70}%)"
    elif plddt_m >= 70:
        return 7, f"AlphaFold中等(pLDDT={plddt_m}, >70%={pct_gt70}%)"
    elif plddt_m >= 50:
        return 6, f"AlphaFold低置信(pLDDT={plddt_m})，新颖蛋白基线"
    elif pubmed <= 100:
        return 6, "新颖蛋白基线，无可靠结构"
    return 5, "无可靠结构数据"


def score_domain(interpro, pfam, func_text, pubmed):
    """Score domain/chromatin potential."""
    domains = []
    for ip in (interpro or []):
        name = ip.get("name", "")
        if name:
            domains.append(name)
    for pf in (pfam or []):
        name = pf.get("name", "")
        if name:
            domains.append(name)

    dom_text = " ".join(domains).lower() + " " + (func_text or "").lower()

    chromatin_kw = ["homeobox", "homeodomain", "zinc finger", "c2h2", "at-hook", "hmg",
                    "bromodomain", "chromodomain", "phd finger", "sant", "whd", "tudor",
                    "mbt", "pwwp", "swi/snf", "iswi", "cxxc", "t-box", "mads-box",
                    "myb", "forkhead", "bzip", "bhlh", "dm domain", "dachshund",
                    "set domain", "jumanji", "jmjc", "macro domain", "dmrt",
                    "dna-binding", "nucleic acid binding", "transcription",
                    "histone", "chromatin", "helicase", "rna-binding",
                    "rrm", "kh domain", "cold shock", "dsrm", "pumilio"]

    has_chromatin = any(kw in dom_text for kw in chromatin_kw)

    if "homeobox" in dom_text or "homeodomain" in dom_text:
        return 10, "明确的DNA结合同源盒结构域"
    elif "dmrt" in dom_text or "dm domain" in dom_text:
        return 10, "明确的DM DNA结合结构域"
    elif has_chromatin:
        return 8, f"DNA/chromatin相关结构域: {[d for d in domains if any(k in d.lower() for k in chromatin_kw)][:3]}"
    elif domains:
        if pubmed <= 100:
            return 7, f"存在注释结构域({len(domains)}个)，新颖蛋白基线"
        return 6, f"存在注释结构域({len(domains)}个)"
    elif pubmed <= 50:
        return 7, "新颖蛋白基线，无注释结构域"
    elif pubmed <= 100:
        return 7, "PubMed≤100基线，无注释结构域"
    else:
        return 5, "无注释结构域"


def score_ppi(intact_data, string_data):
    """Score PPI network 0-10."""
    intact = intact_data or []
    string = string_data or []

    physical_methods = ["coimmunoprecipitation", "pull down", "two hybrid",
                        "anti tag coimmunoprecipitation", "anti bait coimmunoprecipitation",
                        "cross-linking", "two hybrid array", "two hybrid fragment pooling"]

    physical_intact = [i for i in intact if any(m in i.get("method", "").lower() for m in physical_methods)]

    hi_string = [s for s in string if s.get("score", 0) > 0.7]
    hi_exp = [s for s in string if s.get("experimental", 0) > 0.5]

    chromatin_kw = ["transcription", "chromatin", "histone", "methyltransferase",
                    "acetyltransferase", "deacetylase", "hdac", "swi/snf", "nurd",
                    "polycomb", "trithorax", "mll", "setd", "kmt", "kdm", "dnmt",
                    "baf", "pba", "ino80", "iswi", "chd", "smarca", "arid",
                    "bromodomain", "chromodomain", "homeobox", "dna binding",
                    "splicing", "spliceosom", "rna polymerase", "mediator",
                    "helicase", "centromere", "kinetochore", "condensin", "cohesin",
                    "origin recognition", "replication factor"]

    all_partners = set()
    reg_partners = set()
    for i in physical_intact:
        partner = i.get("partner", "").lower()
        all_partners.add(partner)
        if any(kw in partner for kw in chromatin_kw):
            reg_partners.add(partner)

    for s in hi_string:
        partner = s.get("partner", "").lower()
        all_partners.add(partner)
        if any(kw in partner for kw in chromatin_kw):
            reg_partners.add(partner)

    if physical_intact and len(reg_partners) > 0:
        reg_ratio = len(reg_partners) / max(len(all_partners), 1) * 100
        if reg_ratio > 40:
            return 10, f"物理互作 + >40%调控因子({len(physical_intact)}物理互作, {reg_ratio:.0f}%调控)"
        elif reg_ratio > 20:
            return 8, f"物理互作 + 20-40%调控因子({len(physical_intact)}物理互作, {reg_ratio:.0f}%调控)"
        else:
            return 6, f"有物理互作({len(physical_intact)}条)，调控邻居占比低"
    elif hi_exp:
        return 6, f"STRING实验分>0.5 ({len(hi_exp)}条)"
    elif hi_string:
        return 4, f"STRING综合分>0.7 ({len(hi_string)}条)，主要为预测"
    elif string:
        return 3, f"仅有低置信度STRING关联 ({len(string)}条)"
    else:
        return 1, "PPI数据极少"


def determine_subloc(hpa_data, uniprot_data, nuc_score):
    """Determine sublocalization category."""
    if nuc_score <= 3:
        return "rejected"

    hpa_locs = []
    hpa_main = []
    hpa_main_str = ""
    if hpa_data:
        hpa_locs = [l.lower() for l in hpa_data.get("subcellular_location", [])]
        hpa_main = [l.lower() for l in hpa_data.get("subcellular_main_location", [])]
        hpa_main_str = " ".join(hpa_main)

    locs = []
    if uniprot_data:
        for s in uniprot_data.get("subcellular_locations", []):
            locs.append(s.get("location", "").lower())

    all_loc_str = " ".join(locs + hpa_locs + hpa_main)

    if "nucleolus" in all_loc_str or "nucleoli" in all_loc_str:
        # Check if nucleolus is main HPA location
        if any("nucleoli" in l for l in hpa_main):
            return "nucleolus"
        return "nucleoplasm"
    elif "nuclear speckle" in all_loc_str or "speckle" in all_loc_str:
        return "nuclear-speckle"
    elif "nuclear body" in all_loc_str or "pml body" in all_loc_str or "cajal" in all_loc_str:
        return "nuclear-body"
    elif "chromatin" in all_loc_str or "chromosome" in all_loc_str or "centromere" in all_loc_str:
        return "chromatin"
    elif "nuclear envelope" in all_loc_str or "nuclear membrane" in all_loc_str or "lamina" in all_loc_str or "nuclear envelope" in hpa_main_str:
        return "nuclear-envelope"
    elif ("nucleus" in all_loc_str or "nucleoplasm" in all_loc_str) and ("cytosol" in all_loc_str or "cytoplasm" in all_loc_str):
        return "nucleus-cytoplasm"
    elif "nucleoplasm" in all_loc_str or "nucleus" in all_loc_str:
        return "nucleoplasm"
    else:
        return "nucleoplasm"


def generate_report(gene, pkt):
    u = pkt.get("uniprot", {}).get("data", {})
    af_raw = pkt.get("alphafold", {}).get("data", {})
    pub_d = pkt.get("pubmed", {}).get("data", {})
    string_d = pkt.get("string", {}).get("data", [])
    intact_d = pkt.get("intact", {}).get("data", [])
    hpa_d = pkt.get("hpa", {}).get("data", {})

    # Basic info
    acc = u.get("accession", "?")
    name = u.get("protein_name", gene)
    aliases_list = u.get("aliases", [gene])
    aliases = " | ".join(aliases_list) if aliases_list else gene
    length = u.get("length_aa", 0)
    mass = u.get("mass_kda", 0) or round(length * 0.11, 1)

    # AlphaFold
    af = {}
    if af_raw:
        plddt_stats = af_raw.get("plddt_stats", {})
        af = {
            "mean_plddt": plddt_stats.get("mean_plddt", 0) or 0,
            "pct_gt_90": plddt_stats.get("pct_gt_90", 0) or 0,
            "pct_70_90": plddt_stats.get("pct_70_90", 0) or 0,
            "pct_50_70": plddt_stats.get("pct_50_70", 0) or 0,
            "pct_lt_50": plddt_stats.get("pct_lt_50", 0) or 0,
            "version": af_raw.get("latest_version", "?")
        }
    pct_ordered = af.get("pct_gt_90", 0) + af.get("pct_70_90", 0)

    # PubMed
    pubmed_strict = pub_d.get("strict_count", 0)
    pubmed_broad = pub_d.get("broad_count", 0)
    pubmed_symbol = pub_d.get("symbol_only_count", 0)
    alias_note = pub_d.get("alias_note", "")
    key_papers = pub_d.get("key_papers", [])[:5]

    # HPA
    hpa_status = hpa_d.get("status", "no_hpa_data")
    hpa_subcell = hpa_d.get("subcellular_location", [])
    hpa_main = hpa_d.get("subcellular_main_location", [])
    hpa_addl = hpa_d.get("subcellular_additional_location", [])
    hpa_rel = hpa_d.get("reliability_if", "Unknown")
    hpa_if_urls = hpa_d.get("if_image_urls", [])

    # UniProt locations
    subcell_locs = []
    for s in u.get("subcellular_locations", []):
        loc = s.get("location", "")
        ev = ";".join(s.get("evidences", []))
        subcell_locs.append(f"{loc}" + (f" ({ev})" if ev else ""))
    go_cc = [f"{g.get('term','')} ({g.get('evidence','')})" for g in u.get("go_cc", [])]

    # Functions
    func_text = " ".join(u.get("function", [""]))

    # PDB
    pdb_raw = u.get("pdb", [])
    pdbs = []
    for p in pdb_raw:
        if isinstance(p, dict):
            pdb_id = p.get("id", "")
            pdb_method = p.get("method", "")
            pdb_res = p.get("resolution", "")
            pdb_chains = p.get("chains", "")
            pdbs.append(f"{pdb_id} ({pdb_method}, {pdb_res}, {pdb_chains})")
        elif isinstance(p, str):
            pdbs.append(p)
    pdb_ids_only = [p.get("id", "") for p in pdb_raw if isinstance(p, dict)] if pdb_raw else []

    # Domains
    interpro = u.get("interpro", [])
    pfam = u.get("pfam", [])

    # Scoring
    nuc_score, nuc_evidence = score_nuclear(u, hpa_d)
    size_score, size_evidence = score_size(length)
    pub_for_novel = min(pubmed_strict, pubmed_broad) if pubmed_strict > 0 else pubmed_broad
    nov_score = novelty_score(pubmed_strict)
    nov_label = "Extremely novel" if pubmed_strict <= 20 else "Very novel" if pubmed_strict <= 50 else "Moderately novel" if pubmed_strict <= 100 else "Well studied"
    struct_score, struct_evidence = score_structure(af, pdbs, pubmed_strict)
    dom_score, dom_evidence = score_domain(interpro, pfam, func_text, pubmed_strict)
    ppi_score, ppi_evidence = score_ppi(intact_d, string_d)

    # Cross validation
    cross_score = 0.0
    cross_details = []

    has_nucleus_loc = False
    for s in u.get("subcellular_locations", []):
        if "nucleus" in s.get("location", "").lower() or "nucleoplasm" in s.get("location", "").lower():
            has_nucleus_loc = True
            break
    hpa_nuclear = any("nucleoplasm" in l.lower() or "nucleoli" in l.lower() for l in hpa_subcell)

    if has_nucleus_loc and hpa_nuclear:
        cross_score += 1.0
        cross_details.append("UniProt核定位 + HPA IF核验证一致 (+1.0)")
    elif has_nucleus_loc:
        cross_score += 0.5
        cross_details.append("UniProt核定位 (+0.5)")

    if pdbs and len([p for p in pdbs if p]) > 0:
        cross_score += 1.0
        cross_details.append(f"PDB实验结构({len(pdbs)}条目) (+1.0)")

    if intact_d and len(intact_d) > 5:
        cross_score += 0.5
        cross_details.append(f"IntAct实验互作丰富({len(intact_d)}条) (+0.5)")

    if string_d and any(s.get("experimental", 0) > 0.7 for s in string_d if isinstance(s, dict)):
        cross_score += 0.5
        cross_details.append("STRING实验分>0.7 (+0.5)")

    if interpro and len(interpro) >= 3:
        cross_score += 0.5
        cross_details.append(f"InterPro注释丰富({len(interpro)}个结构域) (+0.5)")

    raw = (nuc_score * 4) + (size_score * 1) + (nov_score * 5) + (struct_score * 3) + (dom_score * 2) + (ppi_score * 3) + cross_score
    norm = round(raw / 1.83, 1)

    # Determine subloc
    subloc = determine_subloc(hpa_d, u, nuc_score)

    # Rejection check
    if nuc_score <= 3:
        subloc = "rejected"
        status = "rejected"
        reject_reason = f"核定位≤3 ({nuc_score}/10)"
    elif pubmed_strict > 100:
        subloc = "rejected"
        status = "rejected"
        reject_reason = f"PubMed >100 ({pubmed_strict}篇)"
    else:
        status = "scored"

    out_dir = os.path.join(DETAIL, subloc, gene)
    os.makedirs(out_dir, exist_ok=True)

    # IF images
    if_dir = os.path.join(out_dir, "IF_images")
    os.makedirs(if_dir, exist_ok=True)

    # PAE
    pae_path = os.path.join(out_dir, f"{gene}-PAE.png")
    pae_embed = ""
    if os.path.exists(pae_path) and os.path.getsize(pae_path) > 500:
        pae_embed = f"![[Projects/TEreg-finding/protein-interested/detail/{subloc}/{gene}/{gene}-PAE.png]]\n"
    else:
        pae_embed = "暂无PAE图\n"

    # IF embed
    if_embed = ""
    if hpa_if_urls:
        if_embed = f"HPA IF 图像可用 ({len(hpa_if_urls)}张)，待下载。\n"
    else:
        if_embed = "暂无HPA IF图像数据。\n"

    if status == "rejected":
        return write_rejected(gene, u, hpa_d, subloc, acc, length, name, aliases,
                             pubmed_strict, pubmed_broad, nuc_score, nuc_evidence,
                             reject_reason, subcell_locs, go_cc)

    return write_scored(gene, u, hpa_d, subloc, acc, length, mass, name, aliases,
                        pubmed_strict, pubmed_broad, pubmed_symbol, alias_note,
                        key_papers, af, pct_ordered, pdbs, interpro, pfam,
                        func_text, subcell_locs, go_cc, string_d, intact_d,
                        hpa_subcell, hpa_main, hpa_addl, hpa_rel, hpa_if_urls,
                        nuc_score, nuc_evidence, size_score, size_evidence,
                        nov_score, nov_label, struct_score, struct_evidence,
                        dom_score, dom_evidence, ppi_score, ppi_evidence,
                        cross_score, cross_details, raw, norm, pae_embed, if_embed)


def write_rejected(gene, u, hpa_d, subloc, acc, length, name, aliases,
                   pubmed_strict, pubmed_broad, nuc_score, nuc_evidence,
                   reject_reason, subcell_locs, go_cc):
    out_dir = os.path.join(DETAIL, subloc, gene)
    os.makedirs(out_dir, exist_ok=True)

    loc_text = "; ".join(subcell_locs[:5]) or "无定位信息"
    gocc_text = "; ".join(go_cc[:5]) or "无"

    report = f"""---
type: protein-evaluation
gene: \"{gene}\"
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

**淘汰理由**: {reject_reason}

| 维度 | 证据 |
|------|------|
| UniProt 亚细胞定位 | {loc_text} |
| GO Cellular Component | {gocc_text} |
| PubMed strict | {pubmed_strict} |
| PubMed broad | {pubmed_broad} |
| 核定位得分 | {nuc_score}/10 |
| 核定位证据 | {nuc_evidence} |

**结论**: {reject_reason}，不属于核蛋白范畴，不进入评分流程。

### 3. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/{acc}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term={gene}
"""

    path = os.path.join(out_dir, f"{gene}-evaluation.md")
    with open(path, "w") as f:
        f.write(report)
    return gene, "rejected", nuc_score, 0, 0, 0, 0, 0, 0, 0


def write_scored(gene, u, hpa_d, subloc, acc, length, mass, name, aliases,
                 pubmed_strict, pubmed_broad, pubmed_symbol, alias_note,
                 key_papers, af, pct_ordered, pdbs, interpro, pfam,
                 func_text, subcell_locs, go_cc, string_d, intact_d,
                 hpa_subcell, hpa_main, hpa_addl, hpa_rel, hpa_if_urls,
                 nuc_score, nuc_evidence, size_score, size_evidence,
                 nov_score, nov_label, struct_score, struct_evidence,
                 dom_score, dom_evidence, ppi_score, ppi_evidence,
                 cross_score, cross_details, raw, norm, pae_embed, if_embed):
    out_dir = os.path.join(DETAIL, subloc, gene)
    os.makedirs(out_dir, exist_ok=True)

    # Format subcellular locations
    uni_loc_text = "; ".join(subcell_locs[:8]) if subcell_locs else "无UniProt注释"
    gocc_text = "\n".join(f"- {g}" for g in go_cc[:10]) if go_cc else "- 无GO-CC注释"

    # Format HPA
    hpa_main_str = ", ".join(hpa_main) if hpa_main else "无"
    hpa_addl_str = ", ".join(hpa_addl) if hpa_addl else "无"
    hpa_all_str = ", ".join(hpa_subcell) if hpa_subcell else "无"

    # Format domains
    interpro_names = [ip.get("name", "") for ip in (interpro or []) if ip.get("name")]
    pfam_names = [pf.get("name", "") for pf in (pfam or []) if pf.get("name")]
    all_dom_names = interpro_names + pfam_names
    dom_text = "; ".join(all_dom_names[:8]) if all_dom_names else "无注释结构域"

    # Format PDB
    pdb_text = "; ".join(pdbs[:10]) if pdbs else "无"

    # AF data
    plddt_m = af.get("mean_plddt", 0)
    pct_gt90 = af.get("pct_gt_90", 0)
    pct_70_90 = af.get("pct_70_90", 0)
    pct_50_70 = af.get("pct_50_70", 0)
    pct_lt50 = af.get("pct_lt_50", 0)
    af_ver = af.get("version", "?")

    # Key papers
    paper_text = ""
    for i, kp in enumerate(key_papers):
        pmid = kp.get("pmid", "")
        title = kp.get("title", "")
        journal = kp.get("journal", "")
        pubdate = kp.get("pubdate", "")
        authors = kp.get("authors", [])
        first_author = authors[0] if authors else ""
        paper_text += f"{i+1}. **{title}** "
        if journal:
            paper_text += f"*{journal}* "
        if pubdate:
            paper_text += f"({pubdate}) "
        if pmid:
            paper_text += f"PMID:{pmid} "
        if first_author:
            paper_text += f"-- {first_author} et al."
        paper_text += "\n"

    if not paper_text:
        paper_text = "无关键文献（文献数据未获取）。\n"

    # STRING table
    string_rows = ""
    string_filt = [s for s in (string_d or []) if isinstance(s, dict) and s.get("score", 0) > 0.4]
    string_filt.sort(key=lambda x: x.get("score", 0), reverse=True)
    for s in string_filt[:10]:
        partner = s.get("partner", "?")
        score = s.get("score", 0)
        exp_s = s.get("experimental", 0)
        reg_kw = ["transcription", "chromatin", "histone", "dna", "splicing", "rna", "helicase",
                  "methyltransferase", "acetyltransferase", "deacetylase", "homeobox",
                  "bromodomain", "chromodomain", "nucleolar", "ribosome", "mediator",
                  "centromere", "kinetochore", "cohesin", "condensin", "swi/snf",
                  "polycomb", "trithorax", "setd", "kmt", "kdm", "dnmt"]
        is_reg = "是" if any(kw in partner.lower() for kw in reg_kw) else "—"
        string_rows += f"| {partner} | {score:.3f} | {exp_s:.3f} | {is_reg} |\n"
    if not string_rows:
        string_rows = "| — | — | — | — |\n"

    # IntAct table
    intact_rows = ""
    physical_methods = ["coimmunoprecipitation", "pull down", "two hybrid",
                        "anti tag coimmunoprecipitation", "anti bait coimmunoprecipitation"]
    phys_intact = [i for i in (intact_d or []) if isinstance(i, dict) and
                    any(m in i.get("method", "").lower() for m in physical_methods)]
    seen = set()
    for i in phys_intact:
        partner = i.get("partner", "")
        if partner in seen or len(seen) >= 10:
            continue
        seen.add(partner)
        method = i.get("method", "").replace("psi-mi:", "").replace('"MI:', "").replace('"', "")[:40]
        pmid = i.get("pmid", "")[:20]
        reg_kw = ["transcription", "chromatin", "histone", "dna", "splicing", "rna",
                  "methyltransferase", "acetyltransferase", "deacetylase", "homeobox",
                  "helicase", "nucleolar", "centromere", "kinetochore"]
        is_reg = "是" if any(kw in partner.lower() for kw in reg_kw) else "—"
        intact_rows += f"| {partner} | {method} | {pmid} | {is_reg} |\n"
    if not intact_rows:
        intact_rows = "| — | — | — | — |\n"

    # PPI regulatory stats
    reg_keywords = ["transcription", "chromatin", "histone", "helicase", "rna", "dna",
                    "splicing", "nucleolar", "ribosome", "mediator", "deacetylase",
                    "methyltransferase", "acetyltransferase", "kinetochore", "centromere",
                    "condensin", "cohesin", "swi/snf", "polycomb", "trithorax"]
    reg_count = sum(1 for s in string_filt if any(kw in s.get("partner", "").lower() for kw in reg_keywords))
    reg_ratio = (reg_count / max(len(string_filt), 1) * 100)

    # Cross validation string
    cross_str = f"+{cross_score:.1f}" if cross_score > 0 else "0"
    cross_details_str = "; ".join(cross_details) if cross_details else "无额外互证加分"

    # Size description
    if length <= 800:
        size_desc = f"{length} aa / {mass} kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。"
    elif length <= 1200:
        size_desc = f"{length} aa / {mass} kDa，偏大蛋白，但仍在可操作范围内。"
    else:
        size_desc = f"{length} aa / {mass} kDa，大蛋白，实验操作有一定挑战。"

    # Novelty description
    if pubmed_strict <= 20:
        nov_desc = f"仅 PubMed {pubmed_strict} 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。"
    elif pubmed_strict <= 50:
        nov_desc = f"PubMed {pubmed_strict} 篇 (strict)，非常新颖。仅有少数基础研究，研究空间充足。"
    elif pubmed_strict <= 100:
        nov_desc = f"PubMed {pubmed_strict} 篇 (strict)，中等新颖度。已有一部分研究基础，但仍有较大探索空间。"
    else:
        nov_desc = f"PubMed {pubmed_strict} 篇 (strict)，研究相对充分。需确认独特研究角度。"

    # Structure description
    pct_ordered_total = af.get("pct_gt_90", 0) + af.get("pct_70_90", 0)
    if struct_score >= 9:
        struct_desc = f"优异的实验结构覆盖 + AlphaFold 补充（pLDDT={plddt_m:.1f}，有序区域 {pct_ordered_total:.0f}%）。"
    elif struct_score >= 8:
        if pdbs:
            struct_desc = f"实验结构（PDB: {pdb_text}）提供可靠信息；AlphaFold pLDDT={plddt_m:.1f}，有序区域 {pct_ordered_total:.0f}%。"
        else:
            struct_desc = f"AlphaFold 高质量预测（pLDDT={plddt_m:.1f}，有序区域 {pct_ordered_total:.0f}%）。"
    elif struct_score >= 7:
        struct_desc = f"AlphaFold 中等质量（pLDDT={plddt_m:.1f}，有序区域 {pct_ordered_total:.0f}%）。作为新颖蛋白，此水平可接受。"
    else:
        struct_desc = f"AlphaFold 预测置信度偏低（pLDDT={plddt_m:.1f}，有序区域 {pct_ordered_total:.0f}%）。作为新颖蛋白，属正常现象。"

    # Domain description
    if dom_score >= 8:
        dom_desc = f"含明确的DNA/染色质相关结构域：{dom_text[:100]}。"
    elif dom_score >= 7:
        dom_desc = f"存在注释结构域（{len(all_dom_names)}个），但未发现明确染色质/DNA结合域。新颖蛋白基线不扣分。"
    else:
        dom_desc = "结构域注释有限。作为新颖蛋白（PubMed≤100），无注释域属于该阶段的正常现象。"

    # PPI description
    ppi_count_str = f"STRING {len(string_filt)} 个预测互作 (score>0.4), IntAct {len(phys_intact)} 个实验物理互作"

    report = f"""---
type: protein-evaluation
gene: \"{gene}\"
date: {TODAY}
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## {gene} 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene} / {aliases} |
| 蛋白全名 | {name} |
| 蛋白大小 | {length} aa / {mass} kDa |
| UniProt ID | {acc} |
| 子定位分类 | {subloc} |
| HPA IF 主定位 | {hpa_main_str} |
| HPA IF 附加定位 | {hpa_addl_str} |
| HPA Reliability | {hpa_rel} |
| 评估日期 | {TODAY} |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | {nuc_score}/10 | x4 | {nuc_score*4} | {nuc_evidence[:80]} |
| 蛋白大小 | {size_score}/10 | x1 | {size_score} | {size_evidence[:80]} |
| 研究新颖性 | {nov_score}/10 | x5 | {nov_score*5} | PubMed={pubmed_strict} ({nov_label}) |
| 三维结构 | {struct_score}/10 | x3 | {struct_score*3} | {struct_evidence[:80]} |
| 调控结构域 | {dom_score}/10 | x2 | {dom_score*2} | {dom_evidence[:80]} |
| PPI网络 | {ppi_score}/10 | x3 | {ppi_score*3} | {ppi_evidence[:80]} |
| 互证加分 | — | max+3 | {cross_str} | {cross_details_str[:80]} |
| **加权总分** | | | **{raw}/180** | |
| **归一化总分 (÷1.83)** | | | **{norm}/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | {hpa_all_str} | {hpa_rel} |
| UniProt | {uni_loc_text[:120]} | Swiss-Prot/TrEMBL |
| GO-CC | {'; '.join(go_cc[:5]) if go_cc else '无'} | |

{pae_embed}
{if_embed}
**结论**: {nuc_evidence}

#### 3.2 蛋白大小评估

{size_evidence}

**评价**: {size_desc}

**评分: {size_score}/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | {pubmed_strict} |
| PubMed symbol_only | {pubmed_symbol} |
| PubMed broad | {pubmed_broad} |
| 别名 | {aliases} |
| 新颖性分级 | {nov_label} |

**评价**: {nov_desc}

**评分: {nov_score}/10**。

**关键文献**:
{paper_text}

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | {plddt_m:.1f} |
| pLDDT > 90 (Very High) | {pct_gt90:.1f}% |
| pLDDT 70-90 (High) | {pct_70_90:.1f}% |
| pLDDT 50-70 (Medium) | {pct_50_70:.1f}% |
| pLDDT < 50 (Low) | {pct_lt50:.1f}% |
| 有序区域 (pLDDT>70) 占比 | {pct_ordered_total:.1f}% |
| AlphaFold 版本 | v{af_ver} |
| 实验结构 (PDB) | {pdb_text} |

{pae_embed}
**评价**: {struct_desc}

**评分: {struct_score}/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | {'; '.join(interpro_names[:5]) if interpro_names else '无注释'} |
| Pfam | {'; '.join(pfam_names[:5]) if pfam_names else '无注释'} |

**染色质调控潜力分析**: {dom_desc}

**评分: {dom_score}/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
{string_rows}

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
{intact_rows}

**已知复合体成员** (GO Cellular Component):
{gocc_text}

**PPI 互证分析**:
- STRING partners (score>0.4): {len(string_filt)}
- IntAct 物理互作: {len(phys_intact)}
- 调控相关比例: {reg_count}/{max(len(string_filt),1)} ({reg_ratio:.0f}%)

**评价**: {ppi_evidence}

**评分: {ppi_score}/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | {'Nucleus' if any('nucleus' in s.get('location','').lower() or 'nucleoplasm' in s.get('location','').lower() for s in u.get('subcellular_locations',[])) else 'Non-nuclear'} + {'Nucleoplasm/Nucleoli' if hpa_subcell else 'No HPA nuclear'} | {'一致' if any('nucleus' in s.get('location','').lower() for s in u.get('subcellular_locations',[])) and hpa_subcell else '待确认'} |
| 结构域 | InterPro + Pfam | {len(all_dom_names)}个域 | {'注释存在' if all_dom_names else '无注释'} |
| PPI | STRING + IntAct | {len(string_filt)} + {len(phys_intact)} | {'数据充分' if string_filt and phys_intact else '数据有限'} |

**互证加分明细**:
{chr(10).join(f'- {d}' for d in cross_details) if cross_details else '- 无额外互证加分'}
**总分**: {cross_str} / max +3

### 4. 总体评价

**推荐等级**: {'⭐' * max(1, min(5, round(norm/20 + 1)))} ({norm}/100)

**核心优势**:
1. {nov_label} -- PubMed={pubmed_strict}篇
2. {nuc_evidence[:100]}

**风险/不确定性**:
1. {"HPA IF 待下载验证核定位" if not hpa_subcell else "HPA IF图像可进一步分析"}
2. {"AlphaFold预测质量待提升" if plddt_m < 70 else "结构数据可接受"}

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/{acc}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term={gene}
- AlphaFold: https://alphafold.ebi.ac.uk/entry/{acc}
- STRING: https://string-db.org/cgi/network?identifiers={gene}&species=9606
"""

    path = os.path.join(out_dir, f"{gene}-evaluation.md")
    with open(path, "w") as f:
        f.write(report)

    return gene, subloc, nuc_score, size_score, nov_score, struct_score, dom_score, ppi_score, cross_score, norm


def main():
    results = []
    for gene in GENES:
        print(f"Generating {gene}...")
        try:
            pkt = load_packet(gene)
            r = generate_report(gene, pkt)
            results.append(r)
            gene_name, cat, nuc, sz, nov, st, dom, ppi, cross, norm = r
            print(f"  {gene} -> {cat} norm={norm} (nuc={nuc}, nov={nov}, struct={st}, dom={dom}, ppi={ppi})")
        except Exception as e:
            print(f"  ERROR {gene}: {e}")
            import traceback
            traceback.print_exc()

    print("\n=== Summary ===")
    scored = [r for r in results if r[1] != "rejected"]
    rejected = [r for r in results if r[1] == "rejected"]

    print(f"\nScored: {len(scored)} proteins")
    for gene, cat, nuc, sz, nov, st, dom, ppi, cross, norm in sorted(scored, key=lambda x: -x[9]):
        print(f"  [{cat}] {gene}: norm={norm} (nuc={nuc}, nov={nov}, struct={st}, dom={dom}, ppi={ppi}, cross={cross})")

    print(f"\nRejected: {len(rejected)} proteins")
    for gene, cat, nuc, sz, nov, st, dom, ppi, cross, norm in rejected:
        print(f"  {gene}: nuc={nuc}")

    print(f"\nTotal: {len(results)} reports generated.")


if __name__ == "__main__":
    main()
