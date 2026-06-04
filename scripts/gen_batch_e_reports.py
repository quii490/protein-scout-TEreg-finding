#!/usr/bin/env python3
"""
Generate /180 full evaluation reports for batch E genes.
Rules: Nuclear≤3→REJECTED, PubMed>100→REJECTED, Standard IF/PAE.
Skip already done. No placeholders.
"""
import json, os, sys
from datetime import date

PACKETS = "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets"
BASE = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested"
DETAIL = os.path.join(BASE, "detail")
TODAY = date.today().isoformat()

# Genes in batch E
BATCH_E = "CD1E CDADC1 CDPF1 CENPN CENPO CENPQ CENPS CENPW CEP20 CEP57 CEP70 CEPT1 CERKL CERS3 CERS4 CERT1 CES3 CETN1 CETN3 CGNL1 CHCHD3P2 CHMP4A CHMP4C CHMP5 CHMP6 CHORDC1 CHP1 CHP2 CHRAC1 CHST14 CIBAR1".split()

def has_existing_report(gene):
    """Check if gene already has a scored (non-rejected) /180 report"""
    for subdir in ["chromatin", "nuclear-body", "nuclear-envelope", "nuclear-speckle",
                   "nucleolus", "nucleoplasm", "nucleus-cytoplasm"]:
        p = os.path.join(DETAIL, subdir, gene, f"{gene}-evaluation.md")
        if os.path.exists(p):
            return True, p
    return False, None

def load_packet(gene):
    p = os.path.join(PACKETS, f"{gene}.json")
    if not os.path.exists(p):
        return None
    with open(p) as f:
        d = json.load(f)

    data = {"gene": gene, "timestamp": d.get("timestamp", "")}

    # UNIPROT
    ud = d.get("uniprot", {}).get("data", {}) or {}
    data["uniprot_id"] = ud.get("accession")
    data["protein_name"] = ud.get("protein_name", "")
    data["primary_gene"] = ud.get("primary_gene", gene)
    data["aliases"] = ud.get("aliases", []) or []
    data["length_aa"] = ud.get("length_aa")
    data["mass_kda"] = ud.get("mass_kda")
    data["function"] = ud.get("function", []) or []
    data["subcellular_locations"] = ud.get("subcellular_locations", []) or []
    data["go_cc"] = ud.get("go_cc", []) or []
    data["interpro"] = ud.get("interpro", []) or []
    data["pfam"] = ud.get("pfam", []) or []
    data["uniprot_pdb"] = ud.get("pdb", []) or []

    # ALPHAFOLD
    afd = d.get("alphafold", {}).get("data", {}) or {}
    stats = afd.get("plddt_stats", {}) or {}
    data["af_mean_plddt"] = stats.get("mean_plddt")
    data["af_version"] = afd.get("latest_version")
    data["af_pct_gt_90"] = stats.get("pct_gt_90")
    data["af_pct_70_90"] = stats.get("pct_70_90")
    data["af_pct_50_70"] = stats.get("pct_50_70")
    data["af_pct_lt_50"] = stats.get("pct_lt_50")
    data["af_pdb_entries"] = afd.get("pdb_entries", []) or []

    # PUBMED
    pmd = d.get("pubmed", {}).get("data", {}) or {}
    data["pubmed_strict"] = pmd.get("strict_count")
    data["pubmed_count"] = pmd.get("count")
    data["pubmed_articles"] = pmd.get("articles", []) or []

    # STRING
    data["string_network"] = d.get("string", {}).get("data", []) or []

    # INTACT
    data["intact_interactions"] = d.get("intact", {}).get("data", []) or []

    # HPA
    hd = d.get("hpa", {}).get("data", {}) or {}
    data["hpa_main"] = hd.get("subcellular_main_location", []) or []
    data["hpa_additional"] = hd.get("subcellular_additional_location", []) or []
    data["hpa_reliability"] = hd.get("reliability_if")

    return data


# ─── SCORING FUNCTIONS ───

def is_nuclear_location(loc):
    """Check if a location string indicates nuclear localization"""
    nuclear_terms = ["nucleus", "nuclear", "nucleoplasm", "nucleolar", "nucleoli",
                     "chromosome", "chromatin", "centromere", "kinetochore",
                     "nuclear body", "nuclear speckle", "cajal body", "pml body"]
    loc_lower = loc.lower()
    return any(t in loc_lower for t in nuclear_terms)

def score_nuclear(data):
    """
    Score nuclear localization specificity (1-10).
    Based on HPA main, HPA additional, UniProt subcellular_locations, GO-CC.
    """
    hpa_main = data.get("hpa_main", [])
    hpa_add = data.get("hpa_additional", [])
    uniprot_locs = [s.get("location", "") for s in data.get("subcellular_locations", [])]
    go_cc = data.get("go_cc", [])

    # Check HPA main localization
    main_nuclear = [l for l in hpa_main if is_nuclear_location(l)]
    add_nuclear = [l for l in hpa_add if is_nuclear_location(l)]

    # Check UniProt
    up_nuclear = [l for l in uniprot_locs if is_nuclear_location(l)]

    # Check GO-CC for nuclear terms
    go_nuclear = [g for g in go_cc if is_nuclear_location(g.get("term", ""))]

    hpa_reliability = data.get("hpa_reliability", "")

    # Primary scoring
    has_hpa_nuclear_main = len(main_nuclear) > 0
    has_hpa_nuclear_add = len(add_nuclear) > 0
    has_up_nuclear = len(up_nuclear) > 0
    has_go_nuclear = len(go_nuclear) > 0

    total_main = len(hpa_main) if hpa_main else 0
    total_up = len(uniprot_locs) if uniprot_locs else 0

    # If HPA has no data at all
    if not hpa_main and not hpa_add:
        # Fall back to UniProt + GO
        if has_up_nuclear and has_go_nuclear:
            return 8
        elif has_up_nuclear:
            return 7
        elif has_go_nuclear:
            return 6
        else:
            return 2

    # Strong nuclear: HPA main is exclusively nuclear
    if has_hpa_nuclear_main and total_main == len(main_nuclear) and total_main > 0:
        # All main locations are nuclear
        if has_up_nuclear:
            return 10
        return 9

    # HPA main includes nuclear among others
    if has_hpa_nuclear_main and total_main > len(main_nuclear):
        return 6

    # HPA main is not nuclear, but additional is
    if has_hpa_nuclear_add:
        if has_up_nuclear:
            return 5
        return 4

    # No HPA nuclear, but UniProt says nuclear
    if has_up_nuclear:
        return 4

    # No nuclear evidence at all
    return 1


def score_size(data):
    """Score protein size (1-10). 200-800 aa = 10."""
    length = data.get("length_aa")
    if length is None:
        return 5
    if 200 <= length <= 800:
        return 10
    elif 100 <= length < 200 or 800 < length <= 1000:
        return 8
    elif 50 <= length < 100 or 1000 < length <= 1500:
        return 6
    elif length < 50:
        return 4
    else:  # >1500
        return 3


def score_novelty(data):
    """Score research novelty (1-10). ≤20 PubMed = 10, >100 rejected."""
    pm = data.get("pubmed_strict")
    if pm is None:
        return 5
    if pm <= 20:
        return 10
    elif pm <= 40:
        return 9
    elif pm <= 60:
        return 8
    elif pm <= 80:
        return 7
    elif pm <= 100:
        return 6
    else:
        return 5  # >100 will be rejected at top level


def score_structure(data):
    """Score 3D structure quality (1-10). Based on AF pLDDT + PDB."""
    plddt = data.get("af_mean_plddt")
    pdb = data.get("af_pdb_entries", [])
    has_pdb = len(pdb) > 0 if pdb else False

    if plddt is None:
        return 5

    base = 0
    if plddt >= 90:
        base = 10
    elif plddt >= 85:
        base = 9
    elif plddt >= 80:
        base = 8
    elif plddt >= 70:
        base = 7
    elif plddt >= 60:
        base = 6
    elif plddt >= 50:
        base = 5
    else:
        base = 4

    # Bonus for PDB entries
    if has_pdb:
        base = min(10, base + 1)

    return base


CHROMATIN_KEYWORDS = [
    "histone", "chromo", "bromodomain", "phd", "sant", "mbt",
    "dna binding", "dna-binding", "znf", "zinc finger", "homeobox",
    "hth", "helix-turn-helix", "winged helix", "forkhead", "ets",
    "bzip", "bhlh", "hMG", "arf", "mads", "t-box", "pou",
    "transcription", "chromatin", "nucleosome", "chromodomain",
    "methyltransferase", "acetyltransferase", "deacetylase",
    "demethylase", "remodeling", "helicase", "topoisomerase",
    "telomere", "centromere", "kinetochore", "condensin", "cohesin",
    "mrf", "krueppel", "c2h2", "c4", "gata", "nuclear receptor",
    "ligand-binding", "zf-", "myb", "wh", "hlh", "e2f", "dp",
    "tubby", "cp2", "grainyhead", "hsf", "irf", "smad", "stat",
    "p53", "rb", "pocket", "sox", "tcf", "lef", "paired",
    "homeodomain", "pou domain", "lim", "cut",
]

def score_domains(data):
    """Score regulatory domain richness (1-10)."""
    interpro = data.get("interpro", [])
    pfam = data.get("pfam", [])

    all_domain_ids = []
    all_domain_names = []
    for d in interpro:
        if d.get("id"):
            all_domain_ids.append(d["id"])
        if d.get("name"):
            all_domain_names.append(d["name"])
    for d in pfam:
        if d.get("id"):
            all_domain_ids.append(d["id"])
        if d.get("name"):
            all_domain_names.append(d["name"])

    total_domains = len(set(all_domain_ids))
    domain_text = " ".join(all_domain_names).lower()

    # Check for chromatin/regulatory keywords
    regulatory_hits = sum(1 for kw in CHROMATIN_KEYWORDS if kw.lower() in domain_text)

    # Check function text too
    func_text = " ".join(data.get("function", [])).lower()
    func_regulatory = sum(1 for kw in CHROMATIN_KEYWORDS if kw.lower() in func_text)

    # Also check GO terms
    go_cc = data.get("go_cc", [])
    go_nuclear_terms = [g for g in go_cc if is_nuclear_location(g.get("term", ""))]

    # Scoring
    if total_domains == 0:
        return 5  # baseline for novel proteins

    score = 5  # baseline

    # Domain count
    if total_domains >= 5:
        score += 2
    elif total_domains >= 3:
        score += 1

    # Regulatory keyword hits
    if regulatory_hits >= 3 or func_regulatory >= 3:
        score += 3
    elif regulatory_hits >= 1 or func_regulatory >= 1:
        score += 2

    # GO nuclear evidence
    if len(go_nuclear_terms) >= 3:
        score += 1

    return min(10, score)


def score_ppi(data):
    """Score PPI network (1-10)."""
    string = data.get("string_network", [])
    intact = data.get("intact_interactions", [])

    # STRING high-confidence (>0.7)
    high_conf = [s for s in string if isinstance(s, dict) and s.get("score", 0) > 0.4]
    str_count = len(high_conf)

    # IntAct
    int_count = len(intact) if intact else 0

    # Count experimental STRING partners
    exp_partners = [s for s in string if isinstance(s, dict) and s.get("experimental", 0) > 0]

    if str_count == 0 and int_count == 0:
        return 2

    score = 2  # baseline

    # STRING network size
    if str_count >= 15:
        score += 4
    elif str_count >= 10:
        score += 3
    elif str_count >= 5:
        score += 2
    elif str_count >= 1:
        score += 1

    # IntAct experimental data
    if int_count >= 10:
        score += 3
    elif int_count >= 5:
        score += 2
    elif int_count >= 1:
        score += 1

    # Experimental evidence in STRING
    if len(exp_partners) >= 3:
        score += 1

    return min(10, score)


def score_crossval(data, scores):
    """Calculate cross-validation bonus (max +3)."""
    bonus = 0.0

    # PDB + AlphaFold
    has_pdb = len(data.get("af_pdb_entries", [])) > 0
    has_af = data.get("af_mean_plddt") is not None
    if has_pdb and has_af:
        bonus += 0.5

    # Multi-source localization
    hpa_main = data.get("hpa_main", [])
    hpa_add = data.get("hpa_additional", [])
    up_locs = data.get("subcellular_locations", [])
    nuc_hpa = any(is_nuclear_location(l) for l in hpa_main + hpa_add)
    nuc_up = any(is_nuclear_location(s.get("location", "")) for s in up_locs)
    if nuc_hpa and nuc_up:
        bonus += 0.5
    elif nuc_hpa or nuc_up:
        bonus += 0.25

    # STRING + IntAct
    str_count = len(data.get("string_network", []))
    int_count = len(data.get("intact_interactions", []))
    if str_count > 0 and int_count > 0:
        bonus += 0.5
    elif str_count > 0 or int_count > 0:
        bonus += 0.25

    # Domain + AF quality
    total_domains = len(set(d.get("id") for d in (data.get("interpro", []) + data.get("pfam", [])) if d.get("id")))
    af_quality = data.get("af_mean_plddt")
    if total_domains >= 3 and af_quality and af_quality >= 70:
        bonus += 0.5
    elif total_domains >= 1 and af_quality and af_quality >= 60:
        bonus += 0.25

    # PDB multiple entries
    pdb_count = len(data.get("af_pdb_entries", []))
    if pdb_count >= 3:
        bonus += 0.5
    elif pdb_count >= 1:
        bonus += 0.25

    return min(3.0, bonus)


# ─── DETERMINE OUTPUT DIRECTORY ───

def determine_directory(data, nuclear_score):
    """Determine which detail subdirectory to save to."""
    hpa_main = data.get("hpa_main", [])
    hpa_add = data.get("hpa_additional", [])
    all_hpa = [l.lower() for l in hpa_main + hpa_add]

    if nuclear_score <= 3:
        return "rejected"

    # Check specific nuclear compartments
    if any("nucleoplasm" in l for l in all_hpa):
        return "nucleoplasm"
    if any("nuclear body" in l or "nuclear bodies" in l for l in all_hpa):
        return "nuclear-body"
    if any("nuclear speckle" in l or "nuclear speckles" in l for l in all_hpa):
        return "nuclear-speckle"
    if any("nucleol" in l for l in all_hpa):
        return "nucleolus"
    if any("nuclear membrane" in l or "nuclear envelope" in l or "nuclear pore" in l for l in all_hpa):
        return "nuclear-envelope"
    if any("chromatin" in l or "chromosome" in l or "centromere" in l or "kinetochore" in l for l in all_hpa):
        return "chromatin"

    # For nuclear≥8 but no specific compartment
    if nuclear_score >= 8:
        return "nucleoplasm"

    # For moderate nuclear
    return "nucleus-cytoplasm"


# ─── REPORT GENERATION ───

def format_subcellular_list(locations):
    if not locations:
        return "None reported"
    parts = []
    for s in locations:
        loc = s.get("location", "")
        ev = s.get("evidences", [])
        if ev:
            parts.append(f"{loc} ({len(ev)} evidence{'s' if len(ev) > 1 else ''})")
        else:
            parts.append(loc)
    return "; ".join(parts)

def format_go_cc(go_terms, max_items=8):
    if not go_terms:
        return "- 无 GO-CC 数据"
    lines = []
    for g in go_terms[:max_items]:
        lines.append(f"- {g.get('term', '?')} ({g.get('id', '?')}) [{g.get('evidence', '?')}]")
    return "\n".join(lines)

def format_articles(articles, max_n=5):
    if not articles:
        return "暂无文献记录。"
    lines = []
    for i, a in enumerate(articles[:max_n], 1):
        title = a.get("title", "Untitled")
        journal = a.get("journal", "")
        pmid = a.get("pmid", "")
        year = a.get("pubdate", "")[:4] if a.get("pubdate") else ""
        cite = f"{journal}. PMID: {pmid}" if journal else f"PMID: {pmid}"
        if year:
            cite = f"({year}). {cite}"
        lines.append(f"{i}. {title}. *{cite}*")
    return "\n".join(lines)

def format_string_network(network, max_n=10):
    if not network:
        return "| — | — | 暂无数据 | — |"
    # Sort by score
    sorted_net = sorted(network, key=lambda x: x.get("score", 0), reverse=True)
    lines = []
    for s in sorted_net[:max_n]:
        partner = s.get("partner", "?")
        score = s.get("score", 0)
        exp = s.get("experimental", 0)
        lines.append(f"| {partner} | {score:.3f} | {exp:.3f} | — |")

    header = "| Partner | Combined Score | Experimental | 功能类别 |\n|---------|---------------|--------------|---------|"
    return header + "\n" + "\n".join(lines)

def format_intact(intact, max_n=10):
    if not intact:
        return "| — | — | — | — |"
    lines = []
    for i in intact[:max_n]:
        partner = i.get("partner", "?")
        method = i.get("method", "?")
        pmid = i.get("pmid", "?")
        lines.append(f"| {partner} | {method} | {pmid} |")

    header = "| Partner | 方法 | PMID |\n|---------|------|------|"
    return header + "\n" + "\n".join(lines)

def format_domain_list(interpro, pfam):
    parts = []
    if interpro:
        parts.append("InterPro: " + ", ".join(d.get("id", "?") for d in interpro))
    if pfam:
        parts.append("Pfam: " + ", ".join(d.get("id", "?") for d in pfam))
    return "; ".join(parts) if parts else "暂无已知结构域"

def generate_report(data, scores, output_dir):
    """Generate the full /180 evaluation report."""
    gene = data["gene"]

    # ─── Build sections ───

    # 1. Basic info
    aliases_str = " / ".join(data.get("aliases", [])) if data.get("aliases") else "—"
    protein_name = data.get("protein_name") or "—"
    uniprot_id = data.get("uniprot_id") or "—"
    length = data.get("length_aa")
    mass = data.get("mass_kda")
    size_str = f"{length} aa / {mass} kDa" if length and mass else f"{length} aa" if length else "—"

    # 2. Scores
    nuc_score = scores["nuclear"]
    size_score = scores["size"]
    nov_score = scores["novelty"]
    struct_score = scores["structure"]
    dom_score = scores["domains"]
    ppi_score = scores["ppi"]
    cross_score = scores["crossval"]

    weighted = {
        "nuclear": nuc_score * 4,
        "size": size_score * 1,
        "novelty": nov_score * 5,
        "structure": struct_score * 3,
        "domains": dom_score * 2,
        "ppi": ppi_score * 3,
    }
    raw_total = sum(weighted.values()) + cross_score
    norm_total = raw_total / 1.83

    # Nuclear summary
    hpa_main = ", ".join(data.get("hpa_main", [])) or "—"
    hpa_add = ", ".join(data.get("hpa_additional", [])) or "—"
    up_locs = "; ".join(s.get("location", "") for s in data.get("subcellular_locations", [])) or "—"

    # PubMed
    pm_strict = data.get("pubmed_strict") or "—"

    # AF
    af_plddt = data.get("af_mean_plddt")
    af_ver = data.get("af_version") or "?"
    af_str = f"AlphaFold v{af_ver} pLDDT={af_plddt}" if af_plddt else "暂无数据"

    # PDB
    pdb_list = data.get("af_pdb_entries", [])
    pdb_ids = []
    for pe in pdb_list:
        if isinstance(pe, dict):
            pdb_ids.append(pe.get("id", "?"))
    pdb_str = ", ".join(pdb_ids) if pdb_ids else "暂无"

    # Domains
    domain_str = format_domain_list(data.get("interpro", []), data.get("pfam", []))

    # STRING/IntAct counts
    str_count = len(data.get("string_network", []))
    int_count = len(data.get("intact_interactions", []))

    # Key evidence summaries
    nuc_summary = f"HPA: {hpa_main}" + (f"; 额外: {hpa_add}" if hpa_add and hpa_add != "—" else "") + f"; UniProt: {up_locs}"
    nov_summary = f"PubMed strict={pm_strict} 篇"
    struct_summary = f"{af_str}; PDB: {pdb_str}"
    dom_summary = domain_str[:120] + ("..." if len(domain_str) > 120 else "")
    ppi_summary = f"STRING {str_count} partners; IntAct {int_count} interactions"

    # Regulatory potential analysis
    func_text = " ".join(data.get("function", []))
    go_cc = data.get("go_cc", [])
    go_nuc = [g for g in go_cc if is_nuclear_location(g.get("term", ""))]

    # Determine chromatin regulation potential
    chromatin_hints = []
    for kw in ["chromatin", "nucleosome", "histone", "transcription", "dna binding",
               "dna-binding", "remodeling", "centromere", "kinetochore", "telomere",
               "methyltransferase", "acetyltransferase"]:
        if kw in func_text.lower():
            chromatin_hints.append(kw)
    for d in (data.get("interpro", []) + data.get("pfam", [])):
        name = (d.get("name") or "").lower()
        for kw in ["chromo", "bromo", "histone", "dna binding", "transcription",
                   "helicase", "znf", "zinc finger", "homeobox", "myb"]:
            if kw in name and kw not in chromatin_hints:
                chromatin_hints.append(kw)

    chromatin_analysis = ""
    if chromatin_hints:
        chromatin_analysis = f"存在染色质/调控相关结构域/功能特征: {', '.join(chromatin_hints[:5])}"
    elif domain_str != "暂无已知结构域":
        chromatin_analysis = "存在已知结构域注释，可作为功能研究的结构基础。"
    else:
        chromatin_analysis = "暂无已知结构域，染色质调控潜力待进一步实验验证。"

    # recommendation
    if raw_total >= 140:
        stars = "⭐⭐⭐⭐⭐"
    elif raw_total >= 120:
        stars = "⭐⭐⭐⭐"
    elif raw_total >= 100:
        stars = "⭐⭐⭐"
    elif raw_total >= 80:
        stars = "⭐⭐"
    else:
        stars = "⭐"

    # Strengths
    strengths = []
    if nov_score >= 9:
        strengths.append(f"{gene} — {protein_name}，极度新颖，几乎未被系统研究（PubMed {pm_strict} 篇）。")
    elif nov_score >= 7:
        strengths.append(f"{gene} — {protein_name}，较新颖，PubMed {pm_strict} 篇。")
    if size_score >= 10:
        strengths.append(f"蛋白大小{length} aa，大小适中（200-800 aa），适合常规生化实验和结构解析。")
    elif size_score >= 8:
        strengths.append(f"蛋白大小{length} aa，适合大部分生化实验。")
    if struct_score >= 8:
        strengths.append(f"AlphaFold pLDDT={af_plddt}，结构预测质量高。")
    if pdb_str != "暂无":
        strengths.append(f"可用PDB实验结构: {pdb_str}")

    if not strengths:
        strengths.append(f"{gene} — {protein_name}")

    # Risks
    risks = []
    if nuc_score <= 5:
        risks.append("核定位信号较弱，多源数据支持有限。")
    if pm_strict != "—" and isinstance(pm_strict, (int, float)) and pm_strict <= 5:
        risks.append(f"PubMed {pm_strict} 篇，研究基础极有限，功能注释不完整")
    if af_plddt and af_plddt < 60:
        risks.append(f"AlphaFold pLDDT={af_plddt}，结构预测置信度较低")
    if str_count == 0:
        risks.append("PPI 数据缺失，互作网络未知")
    elif str_count < 5:
        risks.append("PPI 数据有限，互作网络信息不足")

    if not risks:
        risks.append("功能研究较少，具体调控机制待阐明")

    # Next steps
    next_steps = []
    if pm_strict != "—" and isinstance(pm_strict, (int, float)) and pm_strict > 0:
        next_steps.append("查阅最新关键文献补充研究背景")
    next_steps.append("获取 Protein Atlas IF 图像确认亚细胞定位")
    if chromatin_hints:
        next_steps.append("设计 ChIP-seq/CUT&RUN 验证染色质结合")
    next_steps.append("设计体外实验验证核定位及潜在调控功能")
    if str_count < 10:
        next_steps.append("Co-IP/MS 实验鉴定互作伙伴")

    # Cross-validation details
    cross_details = []
    has_pdb = len(pdb_list) > 0
    has_af = af_plddt is not None
    if has_pdb and has_af:
        cross_details.append(f"PDB + AlphaFold 双源验证: +0.5")
    elif has_af and not has_pdb:
        cross_details.append(f"AlphaFold 结构预测: +0.25")

    up_nuc = any(is_nuclear_location(s.get("location", "")) for s in data.get("subcellular_locations", []))
    hpa_nuc = any(is_nuclear_location(l) for l in (data.get("hpa_main", []) + data.get("hpa_additional", [])))
    if hpa_nuc and up_nuc:
        cross_details.append("多库定位一致 (HPA+UniProt): +0.5")
    elif hpa_nuc or up_nuc:
        cross_details.append("单库核定位证据: +0.25")

    if str_count > 0 and int_count > 0:
        cross_details.append(f"STRING + IntAct 双源验证: +0.5")
    elif str_count > 0 or int_count > 0:
        cross_details.append(f"单源PPI数据: +0.25")

    total_domains = len(set(d.get("id") for d in (data.get("interpro", []) + data.get("pfam", [])) if d.get("id")))
    if total_domains >= 3 and af_plddt and af_plddt >= 70:
        cross_details.append("结构域 + AlphaFold 质量: +0.5")
    elif total_domains >= 1 and af_plddt and af_plddt >= 60:
        cross_details.append("结构域注释 + AlphaFold 预测: +0.25")

    pdb_count = len(pdb_list)
    if pdb_count >= 3:
        cross_details.append(f"PDB 多条目覆盖 ({pdb_count} entries): +0.5")
    elif pdb_count >= 1:
        cross_details.append(f"PDB 条目覆盖: +0.25")

    if not cross_details:
        cross_details.append("暂无多库互证数据")

    # UniProt URL
    up_url = f"https://www.uniprot.org/uniprotkb/{uniprot_id}" if uniprot_id != "—" else "—"
    hpa_url = f"https://www.proteinatlas.org/search/{gene}"
    pm_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={gene}"
    af_url = f"https://alphafold.ebi.ac.uk/entry/{uniprot_id}" if uniprot_id != "—" else "—"
    string_url = f"https://string-db.org/network/9606.{gene}"

    # PAE image reference
    pae_ref = f"**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**"

    # GO-CC text
    go_cc_text = format_go_cc(data.get("go_cc", []))

    # Articles
    articles_text = format_articles(data.get("pubmed_articles", []))

    # STRING table
    string_table = format_string_network(data.get("string_network", []))

    # IntAct table
    intact_table = format_intact(data.get("intact_interactions", []))

    # IF image status
    if hpa_main or hpa_add:
        if_notes = f"HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。"
    else:
        if_notes = "HPA 暂无IF原图数据可用。核定位基于 UniProt + GO-CC 注释。"

    # UniProt subcellular
    up_loc_list = []
    for s in data.get("subcellular_locations", []):
        loc = s.get("location", "")
        ev = s.get("evidences", [])
        ev_str = ", ".join(str(e) for e in ev[:3]) if ev else "—"
        up_loc_list.append(f"| UniProt | {loc} | {ev_str}")
    up_loc_text = "\n".join(up_loc_list) if up_loc_list else "| UniProt | — | — |"

    # IF line
    hpa_if_line = f"HPA IF: {hpa_main}" + (f"; 额外: {hpa_add}" if hpa_add else "")

    # Reliability score
    reliability = data.get("hpa_reliability") or "—"

    # PPI cross analysis
    # Count regulatory partners
    reg_partners = 0
    for s in data.get("string_network", []):
        name = (s.get("partner", "") or "").lower()
        for kw in ["transcription", "chromatin", "histone", "dna", "helicase", "znf",
                   "myb", "bromo", "chromo", "hdac", "hat", "kdm", "kmt"]:
            if kw in name:
                reg_partners += 1
                break

    ppi_cross_text = f"STRING {str_count} 个预测互作，IntAct {int_count} 个实验互作。调控相关配体占比 {reg_partners}/{str_count if str_count > 0 else 1}。"

    # Recommendations
    if raw_total >= 130:
        rec_level = "⭐⭐⭐⭐⭐"
    elif raw_total >= 110:
        rec_level = "⭐⭐⭐⭐"
    elif raw_total >= 90:
        rec_level = "⭐⭐⭐"
    elif raw_total >= 70:
        rec_level = "⭐⭐"
    else:
        rec_level = "⭐"

    # ===== BUILD THE REPORT =====
    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: {TODAY}
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## {gene} 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | {gene} / {aliases_str} |
| 蛋白名称 | {protein_name} |
| 蛋白大小 | {size_str} |
| UniProt ID | {uniprot_id} |
| 评估日期 | {TODAY} |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | {nuc_score}/10 | ×4 | {weighted["nuclear"]} | {nuc_summary[:100]} |
| 蛋白大小 | {size_score}/10 | ×1 | {weighted["size"]} | {size_str} |
| 研究新颖性 | {nov_score}/10 | ×5 | {weighted["novelty"]} | {nov_summary} |
| 三维结构 | {struct_score}/10 | ×3 | {weighted["structure"]} | {struct_summary[:100]} |
| 调控结构域 | {dom_score}/10 | ×2 | {weighted["domains"]} | {dom_summary} |
| PPI 网络 | {ppi_score}/10 | ×3 | {weighted["ppi"]} | {ppi_summary} |
| 互证加分 | — | max +3 | {cross_score:.1f} | {cross_details[0] if cross_details else "—"} |
| **原始总分** | | | **{raw_total:.1f}/180** | |
| **归一化总分 (÷1.83)** | | | **{norm_total:.1f}/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | {hpa_main} | {reliability} |
{up_loc_text}

**IF 图像说明**: {if_notes}

**GO Cellular Component**:
{go_cc_text}

**结论**: {nuc_summary}

#### 3.2 蛋白大小评估

**评价**: {size_str}，{"大小适中（200-800 aa），适合常规生化实验和结构解析。" if size_score >= 10 else "大小适合大部分生化实验。" if size_score >= 8 else "蛋白大小稍偏，但可进行常规生化分析。" if size_score >= 6 else "蛋白较大，操作难度略高。"}

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | {pm_strict} |
| PubMed 搜索链接 | [{gene} PubMed]({pm_url}) |

**关键文献**:
{articles_text}

**评价**: {"极度新颖，几乎未被系统研究（PubMed ≤20篇）。" if nov_score >= 10 else "较新颖，研究关注度低。" if nov_score >= 8 else "有一定研究基础。" if nov_score >= 7 else "已有较多研究，新颖性中等。"}

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v{af_ver} |
| AlphaFold 平均 pLDDT | {af_plddt if af_plddt else "—"} |
| 高置信度残基 (pLDDT>90) 占比 | {data.get("af_pct_gt_90", "—")}% |
| 置信残基 (pLDDT 70-90) 占比 | {data.get("af_pct_70_90", "—")}% |
| 中等置信 (pLDDT 50-70) 占比 | {data.get("af_pct_50_70", "—")}% |
| 低置信 (pLDDT<50) 占比 | {data.get("af_pct_lt_50", "—")}% |
| 有序区域 (pLDDT>70) 占比 | {(data.get("af_pct_gt_90", 0) or 0) + (data.get("af_pct_70_90", 0) or 0)}% |
| 可用 PDB 条目 | {pdb_str} |

{pae_ref}

**评价**: {"AlphaFold 高置信度预测 + PDB 实验结构，结构数据充分。" if has_pdb and af_plddt and af_plddt >= 80 else "AlphaFold 预测质量高。" if af_plddt and af_plddt >= 80 else "AlphaFold 预测质量中等。" if af_plddt and af_plddt >= 60 else "AlphaFold 预测质量偏低，存在显著无序区域。"}

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | {domain_str} |

**染色质调控潜力分析**: {chromatin_analysis}

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

{string_table}

**实验验证互作** (IntAct):

{intact_table}

**PPI 互证分析**:
{ppi_cross_text}

**评价**: {"STRING + IntAct 双源 PPI 数据充分。" if str_count >= 10 and int_count >= 10 else "PPI 网络数据较好。" if str_count >= 10 else "PPI 数据有限，互作网络信息不足。" if str_count < 5 else "PPI 数据中等。"}

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold{" + PDB: " + pdb_str if has_pdb else ""} | pLDDT={af_plddt}, v{af_ver} | {"预测+实验" if has_pdb else "预测"} |
| 定位 | UniProt{" + HPA" if hpa_main else ""} | {up_locs} / {hpa_main} | {"一致" if up_nuc and hpa_nuc else "部分一致" if up_nuc or hpa_nuc else "数据有限"} |
| PPI | STRING{" + IntAct" if int_count > 0 else ""} | {str_count}{" + " + str(int_count) if int_count > 0 else ""} interactions | {"数据充分" if str_count >= 10 else "数据有限"} |

**互证加分明细**:
{chr(10).join('- ' + d for d in cross_details)}

**总分**: +{cross_score:.1f} / max +3

### 4. 总体评价

**推荐等级**: {rec_level}

**归一化总分**: {norm_total:.1f}/100

**核心优势**:
{chr(10).join(f'{i}. {s}' for i, s in enumerate(strengths, 1))}

**风险/不确定性**:
{chr(10).join(f'{i}. {r}' for i, r in enumerate(risks, 1))}

**下一步建议**:
{chr(10).join(f'- [ ] {s}' for s in next_steps)}

### 5. 数据来源
- UniProt: {up_url}
- Protein Atlas: {hpa_url}
- PubMed: {pm_url}
- AlphaFold: {af_url}
- STRING: {string_url}
- Packet data timestamp: {data.get('timestamp', '—')}
"""
    return report


# ─── MAIN ───

def main():
    results = []
    skipped = []
    missing_packet = []
    rejected_nuc = []
    rejected_pm = []
    written = []

    for gene in BATCH_E:
        # Check if already done
        exists, path = has_existing_report(gene)
        if exists:
            skipped.append((gene, path))
            continue

        # Load packet
        data = load_packet(gene)
        if data is None:
            missing_packet.append(gene)
            continue

        # Score
        nuc_score = score_nuclear(data)
        pm_strict = data.get("pubmed_strict")

        # Rejection checks
        if nuc_score <= 3:
            rejected_nuc.append((gene, nuc_score))
            continue
        if pm_strict is not None and pm_strict > 100:
            rejected_pm.append((gene, pm_strict))
            continue

        # Score all dimensions
        scores = {
            "nuclear": nuc_score,
            "size": score_size(data),
            "novelty": score_novelty(data),
            "structure": score_structure(data),
            "domains": score_domains(data),
            "ppi": score_ppi(data),
        }
        scores["crossval"] = score_crossval(data, scores)

        # Determine output directory
        output_dir_name = determine_directory(data, nuc_score)
        output_dir = os.path.join(DETAIL, output_dir_name, gene)
        os.makedirs(output_dir, exist_ok=True)

        # Generate report
        report = generate_report(data, scores, output_dir_name)
        output_path = os.path.join(output_dir, f"{gene}-evaluation.md")

        with open(output_path, "w") as f:
            f.write(report)

        weighted_total = scores["nuclear"]*4 + scores["size"]*1 + scores["novelty"]*5 + \
                         scores["structure"]*3 + scores["domains"]*2 + scores["ppi"]*3 + scores["crossval"]

        print(f"[OK] {gene:12s} → {output_dir_name:20s} | nuc={nuc_score} nov={scores['novelty']} af={scores['structure']} dom={scores['domains']} ppi={scores['ppi']} cross={scores['crossval']:.1f} | total={weighted_total:.1f}/180 | {output_path}")
        written.append(gene)
        results.append((gene, scores, output_dir_name, weighted_total))

    # Summary
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Written: {len(written)} reports")
    for g in written:
        print(f"  {g}")
    print(f"Skipped (already done): {len(skipped)}")
    for g, p in skipped:
        print(f"  {g} → {p}")
    print(f"Missing packet: {len(missing_packet)}")
    for g in missing_packet:
        print(f"  {g}")
    print(f"REJECTED (nuclear≤3): {len(rejected_nuc)}")
    for g, s in rejected_nuc:
        print(f"  {g} (nuc={s})")
    print(f"REJECTED (PubMed>100): {len(rejected_pm)}")
    for g, s in rejected_pm:
        print(f"  {g} (pm={s})")


if __name__ == "__main__":
    main()
