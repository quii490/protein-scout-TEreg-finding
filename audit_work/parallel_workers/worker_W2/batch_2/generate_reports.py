#!/usr/bin/env python3
"""Generate /180 evaluation reports for 25 genes. STAGE only."""

import json, os, sys, textwrap
from datetime import datetime

PACKETS = "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets"
STAGE = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/audit_work/parallel_workers/worker_W2/batch_2/staged_reports"
os.makedirs(STAGE, exist_ok=True)

GENES = [
    "SBF1","SBF2","SBNO1","SC5D","SCEL","SCFD2","SCHIP1","SCRN2","SDCBP2",
    "SEH1L","SELENOH","SELENOM","SENP5","SENP7","SENP8","SEPHS2","SEPTIN10",
    "SEPTIN3","SEPTIN6","SEPTIN7","SERF1A","SERF1B","SERGEF","SERPINB10","SERPINB13"
]

NUCLEAR_TERMS = [
    "nucleus","nucleoplasm","nucleolus","nucleoli",
    "nuclear body","nuclear bodies","nuclear speck","nuclear speckle",
    "nuclear speckles","nuclear membrane","nuclear envelope","nuclear pore",
    "chromatin","chromosome","nucleosome"
]

def is_nuclear_term(s):
    """Check if a term genuinely indicates nuclear localization."""
    s_lower = s.lower().strip()
    for t in NUCLEAR_TERMS:
        if t in s_lower:
            return True
    return False

def count_nuclear_hits(entries):
    """Count how many entries contain nuclear terms."""
    count = 0
    if not entries:
        return 0
    if isinstance(entries, list):
        # list of strings or dicts
        for e in entries:
            if isinstance(e, dict):
                loc = e.get("location", e.get("term", ""))
                if is_nuclear_term(loc):
                    count += 1
            elif isinstance(e, str):
                if is_nuclear_term(e):
                    count += 1
    elif isinstance(entries, str):
        if is_nuclear_term(entries):
            count = 1
    return count

def score_nuclear(u, h):
    """Score nuclear localization 0-10."""
    score = 0

    # 1. UniProt subcellular locations
    sub_locs = u.get("subcellular_locations", []) or []
    uni_nuclear = count_nuclear_hits(sub_locs)
    # 2. UniProt GO-CC
    go_cc = u.get("go_cc", []) or []
    go_nuclear = count_nuclear_hits(go_cc)
    # 3. HPA subcellular locations
    hpa_locs = h.get("subcellular_location", []) or []
    hpa_nuclear = count_nuclear_hits(hpa_locs)
    # 4. HPA additional
    hpa_add = h.get("subcellular_additional_location", []) or []
    hpa_add_nuclear = count_nuclear_hits(hpa_add)
    # 5. Check UniProt function text for nuclear functions
    func_text = " ".join(u.get("function", []) or [])
    func_nuclear = 0
    for t in ["transcription","nuclear","chromatin","DNA repair","DNA damage"]:
        if t.lower() in func_text.lower():
            func_nuclear += 1

    # Also check: UniProt has subcellular but no nuclear entries
    sub_locs_list = [x.get("location","") if isinstance(x,dict) else str(x) for x in sub_locs]
    hpa_if = h.get("reliability_if", "")

    # Scoring logic
    total_uni = len(sub_locs_list) if sub_locs_list else 0
    non_nuclear_uni = total_uni - uni_nuclear

    # Count unique nuclear evidence sources
    sources = 0
    if uni_nuclear > 0: sources += 1
    if go_nuclear > 0: sources += 1
    if hpa_nuclear > 0: sources += 1
    if hpa_add_nuclear > 0: sources += 1

    # UniProt explicitly says nucleus or nucleolus etc
    primary_nuclear = any(is_nuclear_term(loc) for loc in sub_locs_list)

    # Check if any nuclear source has experimental evidence
    has_exp_nuclear = False
    for loc_entry in sub_locs:
        if isinstance(loc_entry, dict):
            if is_nuclear_term(loc_entry.get("location","")):
                if "ECO:0000269" in str(loc_entry.get("evidences",[])):  # experimental
                    has_exp_nuclear = True

    # Detailed scoring
    if primary_nuclear and uni_nuclear >= 1 and sources >= 2:
        # UniProt says nucleus, and at least one other DB confirms
        if uni_nuclear >= 2 or go_nuclear >= 2:
            score = 9  # Multiple nuclear locations or strong GO support
        else:
            score = 8  # Clear nuclear but limited detail
        if has_exp_nuclear:
            score = min(10, score + 1)
        # Check if strong cytoplasmic signal competes
        if non_nuclear_uni >= 2:
            score = max(7, score - 1)
        if hpa_if in ["Uncertain"]:
            score = max(7, score - 1)
    elif primary_nuclear and sources == 1:
        score = 7
    elif hpa_nuclear >= 1 and sources >= 2:
        # HPA + GO nuclear, but UniProt not primary nuclear
        score = 6
    elif hpa_nuclear >= 1 and sources == 1:
        # Only HPA says nuclear
        if hpa_nuclear >= 2:
            score = 5  # Multiple HPA nuclear signals
        elif hpa_if == "Approved" or hpa_if == "Supported":
            score = 4  # Single HPA nuclear, approved
        else:
            score = 3  # Weak HPA nuclear
    elif go_nuclear >= 1 and sources >= 1:
        score = 5  # GO says nuclear
    elif func_nuclear >= 1:
        score = 3  # Function hint only
    else:
        # No nuclear evidence
        score = 0
        # Check if there's any hint
        if "perinuclear" in str(sub_locs).lower():
            score = 1  # Perinuclear is not nuclear but neighbor
        if any("chromosome" in str(x).lower() for x in sub_locs_list):
            score = max(score, 4)  # Chromosome-associated

    return min(10, score)


def score_size(u):
    """Score protein size 0-10."""
    aa = u.get("length_aa")
    if not aa:
        # Try to infer from mass
        mass = u.get("mass_kda", 0)
        if mass:
            aa = int(mass * 9)  # rough estimate
        else:
            return 5
    if 250 <= aa <= 800:
        return 10
    elif 150 <= aa < 250:
        return 7
    elif 800 < aa <= 1200:
        return 7
    elif 100 <= aa < 150:
        return 4
    elif 1200 < aa <= 2000:
        return 4
    elif aa < 100:
        return 2
    elif aa > 2000:
        return 2
    else:
        return 5


def score_novelty(p):
    """Score research novelty 0-10 based on PubMed strict count."""
    cnt = p.get("strict_count", 0)
    if cnt is None: cnt = 50
    if cnt <= 10: return 10
    elif cnt <= 20: return 9
    elif cnt <= 40: return 8
    elif cnt <= 60: return 6
    elif cnt <= 80: return 4
    elif cnt <= 100: return 2
    else: return 1


def score_structure(u, a):
    """Score 3D structure 0-10."""
    pdb = u.get("pdb", []) or []
    af = a.get("data", {}) or {}
    af_found = af.get("found")
    plddt = (af.get("plddt_stats", {}) or {}).get("mean_plddt", 0) or 0

    score = 0
    if len(pdb) >= 3:
        score += 3  # Multiple experimental structures
    elif len(pdb) >= 1:
        score += 2  # At least one structure
    else:
        score += 0  # No PDB

    if af_found:
        if plddt >= 85:
            score += 5  # High confidence AF
        elif plddt >= 75:
            score += 4
        elif plddt >= 65:
            score += 3
        elif plddt >= 50:
            score += 2
        else:
            score += 1  # Low confidence
    else:
        # No AlphaFold
        score += 0

    # Bonus for high resolution PDB
    high_res = any(
        (isinstance(p, dict) and
         p.get("resolution") and
         float(str(p["resolution"]).replace(" A","").replace("Å","")) <= 2.5)
        for p in pdb
    )
    if high_res:
        score += 1

    return min(10, score)


def score_domains(u):
    """Score regulatory domains 0-10."""
    interpro = u.get("interpro", []) or []
    pfam = u.get("pfam", []) or []
    func = " ".join(u.get("function", []) or [])

    # Domain-rich proteins score higher
    total_domains = len(interpro) + len(pfam)

    # Nuclear-relevant domains?
    nuclear_domain_keywords = [
        "zinc finger", "homeobox", "helix-turn-helix", "leucine zipper",
        "bZIP", "bHLH", "HLH", "MYB", "ETS", "forkhead", "HMG",
        "bromodomain", "chromodomain", "PHD", "SET", "histone",
        "DNA-binding", "chromatin", "nuclear receptor", "ARID",
        "AT hook", "BRCT", "tudor", "MBT", "WD40", "ANK", "HEAT",
        "ARM", "TPR", "NLS", "nuclear localization", "SUMO", "sentrin",
        "deubiquitinase", "protease", "kinase", "GTPase", "GEF",
        "PH", "SH2", "SH3", "PDZ", "WW", "coiled coil"
    ]
    # Count domain relevance
    domain_hits = 0
    for ip in interpro:
        name = ip.get("name", "")
        for kw in nuclear_domain_keywords:
            if kw.lower() in name.lower():
                domain_hits += 1
                break
    for pf in pfam:
        name = pf.get("name", "")
        for kw in nuclear_domain_keywords:
            if kw.lower() in name.lower():
                domain_hits += 1
                break

    if "deneddylase" in func.lower() or "deubiquitinase" in func.lower() or "sumo" in func.lower():
        domain_hits += 2  # These are strong regulatory enzymes

    if "transcription" in func.lower() or "chromatin" in func.lower():
        domain_hits += 3

    if "kinase" in func.lower() or "phosphatase" in func.lower():
        domain_hits += 1

    if total_domains >= 8:
        score = 7 + min(3, domain_hits)
    elif total_domains >= 5:
        score = 5 + min(4, domain_hits)
    elif total_domains >= 3:
        score = 3 + min(4, domain_hits)
    elif total_domains >= 1:
        score = 2 + min(4, domain_hits)
    else:
        score = 1

    return min(10, score)


def score_ppi(s, u, gene):
    """Score PPI network 0-10."""
    ppi = s.get("data", []) or []
    if not ppi:
        return 1

    high_conf = [x for x in ppi if x.get("score", 0) >= 0.7]
    exp_interactors = [x for x in ppi if x.get("experimental", 0) > 0.3]
    top5_avg = sum(x.get("score", 0) for x in ppi[:5]) / min(5, len(ppi)) if ppi else 0

    score = 0

    # Number of high confidence interactions
    if len(high_conf) >= 10:
        score += 3
    elif len(high_conf) >= 5:
        score += 2
    elif len(high_conf) >= 2:
        score += 1

    # Experimental support
    if len(exp_interactors) >= 5:
        score += 2
    elif len(exp_interactors) >= 2:
        score += 1

    # Top interactor quality
    if top5_avg >= 0.9:
        score += 3
    elif top5_avg >= 0.8:
        score += 2
    elif top5_avg >= 0.6:
        score += 1

    # Interaction diversity
    unique_methods = set()
    for x in ppi[:10]:
        if x.get("experimental", 0) > 0:
            unique_methods.add("exp")
        if x.get("database", 0) > 0:
            unique_methods.add("db")
        if x.get("textmining", 0) > 0:
            unique_methods.add("text")
    score += min(3, len(unique_methods))

    # Check for nuclear interaction partners
    # This would ideally cross-reference but we'll just note it

    return min(10, score)


def score_crossval(u, h):
    """Cross-validation bonus 0-3."""
    bonus = 0

    sub = u.get("subcellular_locations", []) or []
    go = u.get("go_cc", []) or []
    hpa_loc = h.get("subcellular_location", []) or []

    # Check for multi-database consensus on localization
    uni_locs = set()
    for s in sub:
        if isinstance(s, dict):
            uni_locs.add(s.get("location","").lower())
        elif isinstance(s, str):
            uni_locs.add(s.lower())

    go_locs = set()
    for g in go:
        if isinstance(g, dict):
            go_locs.add(g.get("term","").lower())
        elif isinstance(g, str):
            go_locs.add(g.lower())

    hpa_locs = set(str(l).lower() for l in hpa_loc)

    # Overlap between any two databases on a specific location
    all_nuclear_in = set()
    for loc in uni_locs:
        if is_nuclear_term(loc):
            all_nuclear_in.add(loc)
    for loc in go_locs:
        if is_nuclear_term(loc):
            all_nuclear_in.add(loc)
    for loc in hpa_locs:
        if is_nuclear_term(loc):
            all_nuclear_in.add(loc)

    if len(all_nuclear_in) >= 3:
        bonus += 1  # Multi-DB nuclear consensus

    # UniProt experimental evidence quality
    has_exp = any(
        "ECO:0000269" in str(x.get("evidences",[]))
        for x in sub if isinstance(x, dict)
    )
    if has_exp:
        bonus += 0.5

    # Full annotation quality
    if u.get("pdb") and len(u["pdb"]) > 0:
        if "X-ray" in str(u["pdb"]):
            bonus += 0.5

    hpa_if = h.get("reliability_if","")
    if hpa_if in ["Approved"]:
        bonus += 0.5
    elif hpa_if in ["Supported"]:
        bonus += 0.25

    return min(3, bonus)


def determine_nuclear_text(score):
    if score >= 9:
        return "Strongly nuclear -- primary localization confirmed by multiple databases"
    elif score >= 7:
        return "Primarily nuclear with experimental support"
    elif score >= 5:
        return "Moderate nuclear evidence, mixed with cytoplasmic signals"
    elif score >= 3:
        return "Weak/minor nuclear signal -- primarily non-nuclear protein"
    else:
        return "No credible nuclear localization"


def generate_report(gene):
    """Generate a full /180 evaluation report for one gene."""
    path = os.path.join(PACKETS, f"{gene}.json")
    with open(path) as f:
        data = json.load(f)

    u = data.get("uniprot", {}).get("data", {})
    a = data.get("alphafold", {})
    p = data.get("pubmed", {}).get("data", {})
    h = data.get("hpa", {}).get("data", {})
    s = data.get("string", {})
    i = data.get("intact", {})

    protein_name = u.get("protein_name", "Unknown") or "Unknown"
    aliases = u.get("aliases", []) or []
    accession = u.get("accession", "Unknown") or "Unknown"
    length_aa = u.get("length_aa", "?") or "?"
    mass_kda = u.get("mass_kda", "?") or "?"

    # -- Scoring --
    nuc_score = score_nuclear(u, h)
    size_score = score_size(u)
    novel_score = score_novelty(p)
    struct_score = score_structure(u, a)
    domain_score = score_domains(u)
    ppi_score = score_ppi(s, u, gene)
    xval_bonus = score_crossval(u, h)

    # Weighted
    w_nuc = nuc_score * 4
    w_size = size_score * 1
    w_novel = novel_score * 5
    w_struct = struct_score * 3
    w_domain = domain_score * 2
    w_ppi = ppi_score * 3

    raw_total = w_nuc + w_size + w_novel + w_struct + w_domain + w_ppi + xval_bonus
    norm_total = round(raw_total / 180 * 100, 1)

    # -- Decision --
    status = "accepted"
    rejection_reasons = []

    pubmed_cnt = p.get("strict_count", 0) or 0
    if pubmed_cnt > 100:
        status = "rejected"
        rejection_reasons.append(f"PubMed strict count ({pubmed_cnt}) exceeds the 100 threshold -- gene is too well-studied")

    if nuc_score <= 3:
        status = "rejected"
        rejection_reasons.append(f"Nuclear localization score ({nuc_score}/10) is at or below the 3/10 auto-rejection threshold")

    # -- Subcellular data --
    sub_locs = u.get("subcellular_locations", []) or []
    go_cc = u.get("go_cc", []) or []
    hpa_locs = h.get("subcellular_location", []) or []
    hpa_if = h.get("reliability_if", "N/A") or "N/A"

    # -- PubMed --
    strict_cnt = p.get("strict_count", "?") or "?"
    key_papers = p.get("key_papers", []) or []

    # -- AF & PDB --
    af_data = a.get("data", {}) or {}
    af_found = af_data.get("found")
    plddt_stats = af_data.get("plddt_stats", {}) or {}
    mean_plddt = plddt_stats.get("mean_plddt", "N/A")
    pdb_entries = u.get("pdb", []) or []

    # -- Domains --
    interpro = u.get("interpro", []) or []
    pfam = u.get("pfam", []) or []
    func_list = u.get("function", []) or []

    # -- PPI --
    string_data = s.get("data", []) or []
    intact_data = i.get("data", []) or []

    # -- Build evidential texts --

    # Subcellular Location Table
    sub_table_rows = []
    for loc in sub_locs:
        if isinstance(loc, dict):
            evidence_str = ", ".join(loc.get("evidences",[])[:2]) if loc.get("evidences") else "not specified"
            sub_table_rows.append(f"| UniProt | {loc.get('location','')} | {evidence_str} |")

    # GO-CC
    for go in go_cc:
        if isinstance(go, dict):
            sub_table_rows.append(f"| GO-CC | {go.get('term','')} | {go.get('evidence','')} |")

    # HPA (deduplicate)
    hpa_add = h.get("subcellular_additional_location", []) or []
    hpa_full_locs = []
    seen_locs = set()
    for hl in hpa_locs:
        if hl not in seen_locs:
            hpa_full_locs.append(hl)
            seen_locs.add(hl)
    for hl in hpa_add:
        if hl not in seen_locs:
            hpa_full_locs.append(hl)
            seen_locs.add(hl)
    for hl in hpa_full_locs:
        sub_table_rows.append(f"| HPA (IF) | {hl} | IF-based ({hpa_if}) |")

    if not sub_table_rows:
        sub_table_rows.append("| None available | -- | -- |")

    sub_table = "\n".join(sub_table_rows[:25])

    # Domain table
    domain_rows = []
    for ip in interpro[:5]:
        name = ip.get("name","") or ip.get("id","")
        domain_rows.append(f"| InterPro | {name} | {ip.get('id','')} |")
    for pf in pfam[:5]:
        name = pf.get("name","") or pf.get("id","")
        domain_rows.append(f"| Pfam | {name} | {pf.get('id','')} |")
    if not domain_rows:
        domain_rows.append("| None catalogued | -- | -- |")
    domain_table = "\n".join(domain_rows)

    # PPI table
    ppi_rows = []
    for pp in string_data[:8]:
        ppi_rows.append(f"| {pp.get('partner','')} | Combined: {pp.get('score',0):.3f} | EXP: {pp.get('experimental',0):.3f} | DB: {pp.get('database',0):.0f} |")
    if not ppi_rows:
        ppi_rows.append("| No STRING interactions | -- | -- | -- |")
    ppi_table = "\n".join(ppi_rows)

    # Key papers
    paper_list = []
    for kp in key_papers[:4]:
        title = (kp.get("title","") or "")[:120]
        journal = kp.get("journal","") or ""
        pubdate = kp.get("pubdate","") or ""
        paper_list.append(f"- **PMID:{kp.get('pmid','')}** ({pubdate}) -- {title} ({journal})")
    if not paper_list:
        paper_list.append("- No key papers extracted")
    papers_text = "\n".join(paper_list)

    # Nuclear Summary
    nuclear_summary = determine_nuclear_text(nuc_score)

    # Build the manual review analysis for the nuclear section
    nuc_analysis_lines = []
    nuc_analysis_lines.append(f"**Nuclear Score: {nuc_score}/10.** {nuclear_summary}.")

    # Detailed evidence summary
    uni_nuclear_specific = [x.get("location","") for x in sub_locs if isinstance(x,dict) and is_nuclear_term(x.get("location",""))]
    hpa_nuclear_specific = [x for x in hpa_locs if is_nuclear_term(str(x))]
    go_nuclear_specific = [x.get("term","") for x in go_cc if isinstance(x,dict) and is_nuclear_term(x.get("term",""))]

    if uni_nuclear_specific:
        nuc_analysis_lines.append(f"- UniProt annotates: {', '.join(uni_nuclear_specific)}")
    if hpa_nuclear_specific:
        nuc_analysis_lines.append(f"- HPA IF detects: {', '.join(hpa_nuclear_specific)} (Reliability: {hpa_if})")
    if go_nuclear_specific:
        nuc_analysis_lines.append(f"- GO-CC annotations include: {', '.join(go_nuclear_specific)}")

    if not uni_nuclear_specific and not hpa_nuclear_specific and not go_nuclear_specific:
        nuc_analysis_lines.append("- No nuclear annotation found in UniProt, HPA, or GO-CC databases.")

    nuc_analysis_text = "\n\n".join(nuc_analysis_lines)

    # Size analysis
    size_text = ""
    aa_val = u.get("length_aa")
    if aa_val:
        if aa_val < 100:
            size_text = f"{aa_val} aa -- very small protein, below the optimal working range. May present challenges for some biochemical and structural approaches. Score: {size_score}/10."
        elif aa_val < 150:
            size_text = f"{aa_val} aa -- small protein, at the lower boundary of the workable range. Score: {size_score}/10."
        elif aa_val <= 250:
            size_text = f"{aa_val} aa -- moderately sized, acceptable for most experimental approaches. Score: {size_score}/10."
        elif aa_val <= 800:
            size_text = f"{aa_val} aa -- within the ideal range for biochemical, structural, and cell-based approaches. Score: {size_score}/10."
        elif aa_val <= 1200:
            size_text = f"{aa_val} aa -- large protein, still workable but may require specialized approaches for full-length studies. Score: {size_score}/10."
        elif aa_val <= 2000:
            size_text = f"{aa_val} aa -- very large protein, may present challenges for recombinant expression and structural biology. Score: {size_score}/10."
        else:
            size_text = f"{aa_val} aa -- extremely large protein, significant technical challenges anticipated. Score: {size_score}/10."
    else:
        size_text = f"Size data unavailable. Mass: {mass_kda} kDa. Score: {size_score}/10."

    # Novelty analysis
    novelty_text = ""
    if strict_cnt != "?":
        sct = int(strict_cnt) if isinstance(strict_cnt, (int, float)) else strict_cnt
        if isinstance(sct, int):
            if sct <= 10:
                novelty_text = f"PubMed strict count ~{sct} articles. Very high novelty -- minimal prior research. Score: {novel_score}/10."
            elif sct <= 20:
                novelty_text = f"PubMed strict count ~{sct} articles. High novelty with limited prior characterization. Score: {novel_score}/10."
            elif sct <= 40:
                novelty_text = f"PubMed strict count ~{sct} articles. Moderate novelty, some literature but significant unknowns remain. Score: {novel_score}/10."
            elif sct <= 60:
                novelty_text = f"PubMed strict count ~{sct} articles. Moderate-to-established field, growing literature. Score: {novel_score}/10."
            elif sct <= 80:
                novelty_text = f"PubMed strict count ~{sct} articles. Well-studied gene, limited novelty. Score: {novel_score}/10."
            elif sct <= 100:
                novelty_text = f"PubMed strict count ~{sct} articles. Heavily studied, approaching the rejection threshold. Score: {novel_score}/10."
            else:
                novelty_text = f"PubMed strict count ~{sct} articles. Well-known protein (>100 threshold) -- REJECTED on over-publication grounds. Score: {novel_score}/10."

    # Structure analysis
    struct_text_lines = []
    if len(pdb_entries) > 0:
        pdb_details = []
        for pdb_e in pdb_entries[:4]:
            if isinstance(pdb_e, dict):
                pdb_details.append(f"{pdb_e.get('id','')} ({pdb_e.get('method','Unknown method')}, {pdb_e.get('resolution','N/A')})")
            else:
                pdb_details.append(str(pdb_e))
        struct_text_lines.append(f"PDB entries available ({len(pdb_entries)} total): {', '.join(pdb_details[:4])}")
    else:
        struct_text_lines.append("No experimental PDB structures available.")

    if af_found:
        struct_text_lines.append(f"AlphaFold prediction available (v{af_data.get('latest_version','?')}) with mean pLDDT: {mean_plddt}. pLDDT distribution: >90: {plddt_stats.get('pct_gt_90','?')}%, 70-90: {plddt_stats.get('pct_70_90','?')}%, 50-70: {plddt_stats.get('pct_50_70','?')}%, <50: {plddt_stats.get('pct_lt_50','?')}%.")
    else:
        struct_text_lines.append("No AlphaFold prediction available.")

    struct_text = " ".join(struct_text_lines)

    # Domain analysis
    domain_text_lines = []
    domain_text_lines.append(f"InterPro domains: {len(interpro)} | Pfam domains: {len(pfam)}. Total catalogued domains: {len(interpro) + len(pfam)}.")

    # Check for notable domain families
    for ip in interpro:
        name = ip.get("name","")
        if name:
            domain_text_lines.append(f"- {name} ({ip.get('id','')})")

    for pf in pfam:
        name = pf.get("name","")
        if name:
            domain_text_lines.append(f"- {name} ({pf.get('id','')})")

    if not interpro and not pfam:
        domain_text_lines.append("No known domain annotations catalogued.")

    # Check function text
    func_str = " ".join(func_list)
    if func_str:
        domain_text_lines.append(f"")
        domain_text_lines.append(f"Functional annotation: {func_str[:500]}")

    domain_text = "\n".join(domain_text_lines)

    # PPI analysis
    ppi_text_lines = []
    top_partners = string_data[:5]
    if top_partners:
        ppi_text_lines.append("Top STRING interaction partners:")
        for tp in top_partners:
            ppi_text_lines.append(f"- {tp.get('partner','')} (combined score: {tp.get('score',0):.2f}, experimental: {tp.get('experimental',0):.2f})")

    high_conf_count = len([x for x in string_data if x.get("score", 0) >= 0.7])
    ppi_text_lines.append(f"")
    ppi_text_lines.append(f"High-confidence interactors (score >= 0.7): {high_conf_count}. Total STRING interactions: {len(string_data)}. IntAct entries: {len(intact_data)}.")
    ppi_text = "\n".join(ppi_text_lines)

    # Cross-validation text
    xval_text = ""
    if xval_bonus >= 2:
        xval_text = f"Strong multi-database consistency. Bonus: +{xval_bonus:.2f}/3."
    elif xval_bonus >= 1:
        xval_text = f"Moderate cross-validation support. Bonus: +{xval_bonus:.2f}/3."
    elif xval_bonus > 0:
        xval_text = f"Weak cross-validation signal. Bonus: +{xval_bonus:.2f}/3."
    else:
        xval_text = f"No cross-validation bonus. Bonus: 0/3."

    # Overall assessment
    overall_text = ""
    if status == "rejected":
        if nuc_score <= 3 and pubmed_cnt > 100:
            overall_text = (
                "NOT RECOMMENDED -- REJECTED on dual grounds. "
                f"The protein fails the nuclear localization threshold (score {nuc_score}/10 <= 3/10) and exceeds "
                f"the PubMed publication ceiling ({pubmed_cnt} > 100). "
                "Gene is both insufficiently nuclear and too well-studied for this screen."
            )
        elif nuc_score <= 3:
            overall_text = (
                f"NOT RECOMMENDED -- REJECTED. Nuclear localization score {nuc_score}/10 is at or below "
                f"the auto-rejection threshold of 3/10. The protein's localization evidence places it "
                f"primarily outside the nucleus, making it unsuitable for a nuclear-protein-focused study. "
            )
            if nuc_score == 0:
                overall_text += "No nuclear localization signal detected in any database."
            elif nuc_score <= 2:
                overall_text += "Nuclear evidence is extremely limited or absent."
            else:
                overall_text += "Nuclear evidence is minor and outweighed by non-nuclear signals."
        elif pubmed_cnt > 100:
            overall_text = (
                f"NOT RECOMMENDED -- REJECTED. PubMed strict publication count ({pubmed_cnt}) exceeds "
                f"the 100-publication ceiling. The gene is too extensively studied to provide meaningful "
                f"novelty in this screening context."
            )
    else:
        if raw_total >= 120:
            overall_text = (
                f"RECOMMENDED (STRONG). Total score {raw_total:.1f}/180 ({norm_total}/100) places this protein in the "
                f"top tier of candidates. Strong nuclear localization combined with favorable size, "
                f"novelty, and structural characteristics."
            )
        elif raw_total >= 90:
            overall_text = (
                f"RECOMMENDED (MODERATE). Total score {raw_total:.1f}/180 ({norm_total}/100). "
                f"The protein passes all hard filters and shows good characteristics for further study, "
                f"though some dimensions are sub-optimal."
            )
        else:
            overall_text = (
                f"RECOMMENDED (WEAK). Total score {raw_total:.1f}/180 ({norm_total}/100). "
                f"The protein passes the hard filters but scores are modest. Consider as a backup candidate."
            )

    # Decision text
    if status == "rejected":
        decision = f"**FINAL DECISION**: REJECTED. {', '.join(rejection_reasons)}."
        if nuc_score <= 3:
            decision += " Nuclear score <= 3 triggers automatic REJECTED status."
        if pubmed_cnt > 100:
            decision += f" PubMed count ({pubmed_cnt}) > 100 triggers automatic REJECTED status."
    else:
        decision = f"**FINAL DECISION**: STAGED for further review. The gene passes all hard acceptance filters (nuclear score {nuc_score} > 3, PubMed {pubmed_cnt} <= 100). Total score: {raw_total:.1f}/180."

    # Format aliases
    aliases_str = ", ".join(aliases) if aliases else "none"

    # Build the report
    today = datetime.now().strftime("%Y-%m-%d")

    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: {today}
tags: [protein-scout, batch-2, worker-W2]
status: {status}
---

## {gene} -- /180 Protein Suitability Evaluation

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | {gene} / {aliases_str} |
| Protein Name | {protein_name} |
| Protein Size | ~{length_aa} aa ({mass_kda} kDa) |
| UniProt ID | {accession} |
| Evaluation Date | {today} |
| Source | Harvest packet ({gene}.json) |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | {nuc_score}/10 | x4 | **{w_nuc}** | {nuclear_summary} |
| Protein Size | {size_score}/10 | x1 | **{w_size}** | {length_aa} aa |
| Research Novelty | {novel_score}/10 | x5 | **{w_novel}** | PubMed strict ~{strict_cnt} |
| 3D Structure | {struct_score}/10 | x3 | **{w_struct}** | PDB: {len(pdb_entries)}, AF: {'Yes' if af_found else 'No'} |
| Regulatory Domains | {domain_score}/10 | x2 | **{w_domain}** | InterPro: {len(interpro)}, Pfam: {len(pfam)} |
| PPI Network | {ppi_score}/10 | x3 | **{w_ppi}** | STRING: {len(string_data)} interactions |
| Cross-Validation Bonus | -- | -- | **+{xval_bonus:.2f}** | |
| **Raw Total** | | | **{raw_total:.1f}/180** | |
| **Normalized Total** | | | **{norm_total}/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
{sub_table}

**HPA IF Status**: {'IF images available; reliability: ' + hpa_if if hpa_locs else 'No HPA IF data available'}.

{nuc_analysis_text}

**Nuclear localization score: {nuc_score}/10.** {'RULE: Nuclear <=3 -> REJECTED. This gene FAILS the nuclear localization threshold.' if nuc_score <= 3 else 'Above the <=3 rejection threshold.'}

### 4. Protein Size Assessment

{size_text}

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict query count | {strict_cnt} |
| Broad query count | {p.get('broad_count', 'N/A')} |
| Alias note | {p.get('alias_note', 'N/A')} |
| Novelty score | {novel_score}/10 |

{novelty_text}

**Key Publications**:

{papers_text}

### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | {'Available (v' + str(af_data.get('latest_version','')) + ')' if af_found else 'Not available'} |
| Mean pLDDT | {mean_plddt} |
| PDB Entries | {len(pdb_entries)} |
| AF pLDDT >90% | {plddt_stats.get('pct_gt_90', 'N/A')}% |
| AF pLDDT <50% | {plddt_stats.get('pct_lt_50', 'N/A')}% |

**Structure Assessment**: {struct_text}

### 7. Domain Architecture

| Source | Domain/Feature | Identifier |
|--------|---------------|------------|
{domain_table}

{domain_text}

**Domain score: {domain_score}/10.**

### 8. PPI Network Analysis

| Partner | Combined Score | Experimental | Database |
|---------|---------------|-------------|----------|
{ppi_table}

{ppi_text}

**PPI score: {ppi_score}/10.**

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | UniProt + HPA + GO-CC | {'Nuclear consensus' if nuc_score >= 7 else 'Mixed/weak nuclear signal'} | {'Multi-source consistent' if nuc_score >= 6 else 'Partially consistent'} |
| Function | Literature + GO | {func_str[:120] if func_str else 'No functional annotation'} | -- |
| Structure | AF + PDB | {'Both AF and experimental' if af_found and pdb_entries else 'AF only' if af_found else 'Limited'} | -- |

**Cross-Validation Bonus Details**: {xval_text}

### 10. Overall Assessment

**Recommendation Level**: {overall_text}

**Core Observations**:
1. {'Nuclear localization: ' + nuclear_summary}
2. PubMed count: {strict_cnt} articles {'(over 100 -- REJECTED)' if (isinstance(strict_cnt, int) and strict_cnt > 100) or (isinstance(strict_cnt, str) and strict_cnt.isdigit() and int(strict_cnt) > 100) else ''}
3. Protein size: {length_aa} aa {'' if not length_aa or length_aa == '?' else ('-- ideal' if (isinstance(length_aa, int) and 250 <= length_aa <= 800) else '-- acceptable' if (isinstance(length_aa, int) and 150 <= length_aa <= 1200) else '-- suboptimal')}
4. Structure: {'Experimental PDB available (' + str(len(pdb_entries)) + ' entries)' if pdb_entries else 'AlphaFold prediction only' if af_found else 'No structural data available'}
5. PPI network: {len(string_data)} STRING interactions, {len([x for x in string_data if x.get('score', 0) >= 0.7])} high-confidence
6. Domain architecture: {len(interpro)} InterPro + {len(pfam)} Pfam entries

### 11. Decision

{decision}

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/{accession}
- HPA: {h.get('hpa_subcellular_url', 'N/A')}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22{gene}%22
- STRING: https://string-db.org/ (search {gene})
- IntAct: https://www.ebi.ac.uk/intact/ (search {gene})
- Harvest packet: {gene}.json
"""

    # Verify length
    lines = report.count('\n') + 1
    chars = len(report)

    # Write to file
    outpath = os.path.join(STAGE, f"{gene}-evaluation.md")
    with open(outpath, 'w') as f:
        f.write(report)

    return {
        "gene": gene,
        "status": status,
        "nuc_score": nuc_score,
        "raw_total": raw_total,
        "norm_total": norm_total,
        "lines": lines,
        "chars": chars,
        "pubmed": strict_cnt,
        "aliases": aliases_str
    }


def main():
    results = []
    for gene in GENES:
        print(f"Processing {gene}...")
        try:
            res = generate_report(gene)
            results.append(res)
            flag = ""
            if res["lines"] < 80:
                flag += f" [LINES:{res['lines']}]"
            if res["chars"] < 3000:
                flag += f" [CHARS:{res['chars']}]"
            status_mark = "REJECTED" if res["status"] == "rejected" else "STAGED"
            print(f"  -> {status_mark} | Nuclear: {res['nuc_score']}/10 | Raw: {res['raw_total']:.1f}/180 | L:{res['lines']} C:{res['chars']}{flag}")
        except Exception as e:
            print(f"  -> ERROR: {e}")
            import traceback
            traceback.print_exc()

    # Summary
    print("\n" + "="*60)
    print("BATCH SUMMARY")
    print("="*60)
    accepted = [r for r in results if r["status"] == "accepted"]
    rejected = [r for r in results if r["status"] == "rejected"]
    print(f"Accepted/Staged: {len(accepted)}")
    print(f"Rejected: {len(rejected)}")

    if rejected:
        print("\nRejected genes:")
        for r in rejected:
            nuc_str = f"nuclear={r['nuc_score']}" if r['nuc_score'] <= 3 else ""
            pub_str = f"pubmed={r['pubmed']}" if (isinstance(r['pubmed'], int) and r['pubmed'] > 100) or (isinstance(r['pubmed'], str) and r['pubmed'].isdigit() and int(r['pubmed']) > 100) else ""
            reasons = [x for x in [nuc_str, pub_str] if x]
            print(f"  {r['gene']}: {', '.join(reasons)}")

    if accepted:
        print("\nStaged genes:")
        for r in accepted:
            print(f"  {r['gene']}: nuclear={r['nuc_score']}/10 raw={r['raw_total']:.1f}/180 norm={r['norm_total']}/100")

    # Check for short reports
    short_lines = [r for r in results if r["lines"] < 80]
    short_chars = [r for r in results if r["chars"] < 3000]
    if short_lines:
        print(f"\nWARNING: {len(short_lines)} reports under 80 lines: {[r['gene'] for r in short_lines]}")
    if short_chars:
        print(f"WARNING: {len(short_chars)} reports under 3000 chars: {[r['gene'] for r in short_chars]}")

    print("\nDone. Reports written to:", STAGE)


if __name__ == "__main__":
    main()
