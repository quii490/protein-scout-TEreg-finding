#!/usr/bin/env python3
"""Generate 25 evaluation reports for batch 2 genes from harvest packets."""
import json
import os
from datetime import date

PACKETS_DIR = "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets"
STAGE_DIR = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/audit_work/parallel_workers/worker_W3/batch_2/staged_reports"

GENES = [
    "SERPINB9", "SERTAD2", "SERTAD3", "SERTAD4", "SFT2D1",
    "SGK2", "SGSM2", "SGTB", "SHFL", "SHISA2",
    "SHISA6", "SHLD2", "SHLD3", "SHOC1", "SHPK",
    "SHROOM4", "SHTN1", "SIGIRR", "SIGLEC15", "SIRAL1",
    "SIVA1", "SKA3", "SKAP1", "SKAP2", "SKIDA1"
]

TODAY = "2026-06-04"


def load_packet(gene):
    path = os.path.join(PACKETS_DIR, f"{gene}.json")
    with open(path) as f:
        return json.load(f)


def safe_get(d, *keys, default=None):
    for k in keys:
        if isinstance(d, dict):
            d = d.get(k, default)
        else:
            return default
    return d if d is not None else default


def count_phys_intact(intact_data):
    """Count physical association interactions (MI:0915 or MI:0407)."""
    if not intact_data or not isinstance(intact_data, list):
        return []
    physical = []
    for entry in intact_data:
        itype = entry.get("interaction_type", "")
        if "MI:0915" in itype or "MI:0407" in itype:
            physical.append(entry)
    return physical


def score_nuclear(packet):
    """Score nuclear localization 0-10. ≤3 = REJECTED."""
    u = safe_get(packet, "uniprot", "data", default={})
    h = safe_get(packet, "hpa", "data", default={})

    # Check if found in UniProt
    uniprot_found = u.get("found", False)
    hpa_status = h.get("status", "")
    hpa_main = [x.lower() for x in h.get("subcellular_main_location", [])]
    hpa_all = [x.lower() for x in h.get("subcellular_location", [])]
    hpa_reliability = h.get("reliability_if", "")
    uniprot_locs = [x.get("location", "").lower() for x in u.get("subcellular_locations", [])]
    go_cc_terms = [x.get("term", "").lower() for x in u.get("go_cc", [])]

    nuclear_keywords = ["nucleus", "nucleoplasm", "nucleoli", "nuclear", "chromosome", "chromatin"]
    non_nuclear_keywords = ["cytoplasm", "cytosol", "membrane", "plasma", "secreted",
                           "extracellular", "mitochondrion", "er", "endoplasmic",
                           "golgi", "vesicle", "cytoskeleton", "actin", "microtubule",
                           "centrosome", "centromere", "spindle", "kinetochore",
                           "melanosome", "p-body", "filopodium", "lamellipodium",
                           "growth cone", "axon", "synapse", "postsynaptic",
                           "cell junction", "focal adhesion", "cilium", "basal body",
                           "perikaryon", "exosome"]

    has_hpa_nuclear = any(kw in loc for loc in hpa_all for kw in nuclear_keywords) if hpa_all else False
    has_uniprot_nuclear = any(kw in loc for loc in uniprot_locs for kw in nuclear_keywords)
    has_go_nuclear = any(kw in term for term in go_cc_terms for kw in nuclear_keywords)
    has_any_non_nuclear = any(kw in loc for loc in hpa_all for kw in non_nuclear_keywords) if hpa_all else True

    # Default alignment information
    has_nucleus = has_uniprot_nuclear or has_go_nuclear

    # SPECIAL CASE: SIRAL1 - no data at all
    if not uniprot_found and not hpa_all:
        return 0, "No UniProt entry found; no HPA data; gene symbol unrecognized in major databases"

    # Genes with no nuclear in UniProt but HPA says nuclear
    # Special handling for each gene based on actual data

    # Score based on HPA reliability + UniProt consistency
    if hpa_reliability == "Enhanced":
        if has_hpa_nuclear and has_uniprot_nuclear:
            if not has_any_non_nuclear or (len(hpa_all) <= 2 and hpa_main and all("nuc" in m for m in hpa_main)):
                return 10, f"HPA {hpa_reliability} + UniProt Nucleus; primarily nuclear"
            else:
                return 8, f"HPA {hpa_reliability} + UniProt Nucleus; nuclear with some non-nuclear signal"
        elif has_hpa_nuclear and not has_uniprot_nuclear:
            return 6, f"HPA {hpa_reliability} nuclear; UniProt lacks nuclear annotation; potential artifact"
        elif not has_hpa_nuclear and has_uniprot_nuclear:
            return 5, f"HPA {hpa_reliability} no nuclear; UniProt Nucleus; conflicting"
        else:
            return 3, f"HPA {hpa_reliability}; nuclear signal absent or minimal"

    elif hpa_reliability == "Supported":
        if has_hpa_nuclear and has_uniprot_nuclear:
            if not has_any_non_nuclear or (len(hpa_all) <= 2 and all("nuc" in m for m in (hpa_main or []))):
                return 9, f"HPA {hpa_reliability} + UniProt Nucleus; primarily nuclear"
            else:
                return 7, f"HPA {hpa_reliability} + UniProt Nucleus; nuclear with other locations"
        elif has_hpa_nuclear and not has_uniprot_nuclear:
            return 5, f"HPA {hpa_reliability} nuclear; UniProt lacks nuclear annotation"
        elif not has_hpa_nuclear and has_uniprot_nuclear:
            return 5, f"HPA {hpa_reliability} no nuclear; UniProt Nucleus; conflicting"
        else:
            return 3, f"HPA {hpa_reliability}; nuclear signal minimal"

    elif hpa_reliability == "Approved":
        if has_hpa_nuclear and has_uniprot_nuclear:
            if not has_any_non_nuclear or (len(hpa_all) <= 2 and all("nuc" in m for m in (hpa_main or []))):
                return 9, f"HPA {hpa_reliability} + UniProt Nucleus; nuclear focused"
            else:
                return 7, f"HPA {hpa_reliability} + UniProt Nucleus; nuclear with additional locations"
        elif has_hpa_nuclear and not has_uniprot_nuclear:
            # Check if UniProt GO-CC has nuclear
            if has_go_nuclear:
                return 6, f"HPA {hpa_reliability} nuclear; GO-CC has nuclear terms; UniProt subcellular_location lacks explicit nucleus"
            return 5, f"HPA {hpa_reliability} nuclear; UniProt lacks nuclear annotation"
        elif not has_hpa_nuclear and has_uniprot_nuclear:
            return 5, f"HPA {hpa_reliability} no nuclear; UniProt Nucleus; conflicting"
        else:
            return 2, f"HPA {hpa_reliability}; no nuclear signal"

    elif hpa_reliability == "Uncertain":
        if has_hpa_nuclear:
            return 3, f"HPA {hpa_reliability}; nuclear signal present but uncertain"
        elif has_uniprot_nuclear:
            return 3, f"HPA {hpa_reliability}; UniProt says Nucleus but HPA uncertain"
        else:
            return 1, f"HPA {hpa_reliability}; no convincing nuclear localization"

    else:
        if has_uniprot_nuclear:
            return 4, "HPA data unavailable; UniProt Nucleus annotation"
        elif has_go_nuclear:
            return 3, "HPA data unavailable; GO-CC nuclear terms only"
        else:
            return 1, "No nuclear localization data available"


def score_size(length_aa):
    if length_aa is None:
        return 5, "Unknown size"
    if 200 <= length_aa <= 800:
        return 10, f"{length_aa} aa; ideal range"
    elif (100 <= length_aa < 200) or (800 < length_aa <= 1200):
        return 8, f"{length_aa} aa; acceptable range"
    elif (50 <= length_aa < 100) or (1200 < length_aa <= 2000):
        return 5, f"{length_aa} aa; suboptimal range"
    elif length_aa < 50 or (2000 < length_aa <= 3000):
        return 2, f"{length_aa} aa; challenging size"
    else:
        return 0, f"{length_aa} aa; extreme size"


def score_novelty(pubmed_count):
    if pubmed_count is None or pubmed_count == 0:
        return 10, "~0 publications; extremely novel"
    if pubmed_count <= 20:
        return 10, f"{pubmed_count} publications; extremely novel (≤20)"
    elif pubmed_count <= 50:
        return 8, f"{pubmed_count} publications; very novel (21-50)"
    elif pubmed_count <= 100:
        return 6, f"{pubmed_count} publications; moderate novelty (51-100)"
    else:
        return 0, f"{pubmed_count} publications; REJECTED (>100)"  # Will be caught by caller


def score_structure(packet):
    """Score 3D structure quality."""
    af = safe_get(packet, "alphafold", "data", default={})
    u = safe_get(packet, "uniprot", "data", default={})
    pdb_entries = u.get("pdb", [])
    plddt_stats = af.get("plddt_stats", {})
    mean_plddt = plddt_stats.get("mean_plddt", 0)

    has_pdb = len(pdb_entries) > 0 if pdb_entries else False
    pdb_count = len(pdb_entries) if pdb_entries else 0

    if has_pdb and mean_plddt >= 80:
        return 10, f"PDB ({pdb_count} entries) + AlphaFold high quality (pLDDT={mean_plddt:.1f})"
    elif has_pdb and mean_plddt >= 70:
        return 9, f"PDB ({pdb_count} entries) + AlphaFold good quality (pLDDT={mean_plddt:.1f})"
    elif has_pdb and mean_plddt >= 50:
        return 8, f"PDB ({pdb_count} entries) + AlphaFold moderate (pLDDT={mean_plddt:.1f})"
    elif has_pdb:
        return 7, f"PDB ({pdb_count} entries); AlphaFold low confidence (pLDDT={mean_plddt:.1f})"
    elif mean_plddt >= 80:
        return 8, f"AlphaFold high quality (pLDDT={mean_plddt:.1f}); no PDB"
    elif mean_plddt >= 70:
        return 7, f"AlphaFold moderate quality (pLDDT={mean_plddt:.1f}); no PDB"
    elif mean_plddt >= 60:
        return 6, f"AlphaFold marginal (pLDDT={mean_plddt:.1f}); novel protein baseline"
    elif mean_plddt >= 50:
        return 5, f"AlphaFold low (pLDDT={mean_plddt:.1f}); largely disordered"
    else:
        return 4, f"AlphaFold poor (pLDDT={mean_plddt:.1f}); mostly disordered"


def score_domains(packet):
    """Score regulatory domain potential."""
    u = safe_get(packet, "uniprot", "data", default={})
    interpro = u.get("interpro", [])
    pfam = u.get("pfam", [])
    function = u.get("function", [])

    domain_count = len(interpro) + len(pfam)

    # Check for chromatin/DNA-related keywords in function
    func_text = " ".join(function).lower() if function else ""
    chromatin_kw = ["chromatin", "dna", "transcription", "histone", "nucleosome",
                    "methylation", "acetylation", "remodeling", "epigenetic"]
    has_chromatin_func = any(kw in func_text for kw in chromatin_kw)

    if has_chromatin_func and domain_count >= 3:
        return 10, f"{domain_count} domains; chromatin/DNA-related function. Direct regulatory potential."
    elif has_chromatin_func and domain_count >= 1:
        return 9, f"{domain_count} domains; chromatin/DNA-related function. Moderate regulatory potential."
    elif has_chromatin_func:
        return 8, f"No annotated domains but chromatin/DNA-related function suggests regulatory role."

    if domain_count >= 4:
        return 8, f"{domain_count} annotated domains; some domain richness."
    elif domain_count >= 2:
        return 7, f"{domain_count} domains; novel protein baseline, possible uncharacterized domains."
    elif domain_count >= 1:
        return 7, f"1 annotated domain; novel protein baseline."
    else:
        return 7, "No annotated domains; novel protein baseline, structure may harbor uncharacterized domains."


def score_ppi(packet):
    """Score PPI network quality and regulatory relevance."""
    intact_data = safe_get(packet, "intact", "data", default=[])
    string_data = safe_get(packet, "string", "data", default=[])
    u = safe_get(packet, "uniprot", "data", default={})
    go_cc = u.get("go_cc", [])

    physical_intact = count_phys_intact(intact_data) if isinstance(intact_data, list) else []
    string_high = [x for x in (string_data or []) if x.get("score", 0) >= 0.7] if isinstance(string_data, list) else []
    string_experimental = [x for x in (string_data or []) if x.get("experimental", 0) >= 0.3] if isinstance(string_data, list) else []

    # Check for chromatin regulatory partners
    chromatin_partners = ["EZH2", "SUZ12", "EED", "RBBP", "MTF2", "PHF19", "SMARC",
                         "KDM", "HDAC", "TP53", "BRCA", "RIF1", "MAD2L2", "CTBP",
                         "KAT5", "HELLS", "CHD", "MBD", "DNMT", "SETD", "KMT",
                         "PRC", "COMPASS", "SWI/SNF", "NuRD", "SAGA", "TFIID",
                         "MED", "POLR", "DAXX", "ATRX", "HIRA", "SMCHD1"]
    chromatin_reg = [x for x in physical_intact if any(cp in x.get("partner", "").upper() for cp in chromatin_partners)]
    chromatin_string = [x for x in string_high if any(cp in x.get("partner", "").upper() for cp in chromatin_partners)]

    total_cr_partners = len(set([x.get("partner", "") for x in chromatin_reg] +
                                [x.get("partner", "") for x in chromatin_string]))

    has_physical = len(physical_intact) > 0
    has_string_high = len(string_high) > 0
    has_string_exp = len(string_experimental) > 0

    if has_physical and total_cr_partners >= 3:
        reg_pct = min(total_cr_partners * 10, 40)
        return 10, f"Physical interactions (IntAct) + {total_cr_partners} chromatin-regulatory partners; high regulatory relevance"
    elif has_physical and total_cr_partners >= 1:
        return 8, f"Physical interactions (IntAct) + {total_cr_partners} chromatin-regulatory partner(s); regulatory relevance"
    elif has_physical and not total_cr_partners:
        return 6, f"Physical interactions present ({len(physical_intact)} partners) but no chromatin regulatory partners"
    elif has_string_exp and total_cr_partners >= 1:
        return 5, f"No IntAct; STRING experimental + {total_cr_partners} chromatin-regulatory partner(s)"
    elif has_string_high:
        return 4, f"No physical interactions; STRING predicted partners present"
    elif string_data and len(string_data) > 0:
        return 3, f"Limited STRING associations; weak PPI evidence"
    elif go_cc:
        return 2, f"GO-CC annotations only; no direct interaction data"
    else:
        return 1, f"No PPI data available"


def score_cross_validation(packet):
    """Score cross-validation bonus."""
    u = safe_get(packet, "uniprot", "data", default={})
    h = safe_get(packet, "hpa", "data", default={})

    bonus = 0
    details = []

    # Check multi-DB localization consistency
    hpa_main = [x.lower() for x in h.get("subcellular_main_location", [])]
    uniprot_locs = [x.get("location", "").lower() for x in u.get("subcellular_locations", [])]
    nuclear_kw = ["nucleus", "nucleoplasm", "nucleoli", "nuclear", "chromosome", "chromatin"]

    hpa_nuclear = any(kw in loc for loc in hpa_main for kw in nuclear_kw) if hpa_main else False
    uniprot_nuclear = any(kw in loc for loc in uniprot_locs for kw in nuclear_kw)

    if hpa_nuclear and uniprot_nuclear:
        bonus += 0.5
        details.append("HPA + UniProt nuclear localization agreement (+0.5)")

    # Check if PDB + AlphaFold consistency
    pdb = u.get("pdb", [])
    af = safe_get(packet, "alphafold", "data", default={})
    if pdb and af.get("found"):
        bonus += 0.5
        details.append("PDB + AlphaFold structural data agreement (+0.5)")

    # Check if STRING + IntAct overlap
    intact_data = safe_get(packet, "intact", "data", default=[])
    string_data = safe_get(packet, "string", "data", default=[])
    if intact_data and string_data:
        intact_partners = set()
        string_partners = set()
        for e in intact_data:
            p = e.get("partner", "")
            if p:
                intact_partners.add(p.upper())
        for e in string_data:
            p = e.get("partner", "")
            if p:
                string_partners.add(p.upper())
        overlap = intact_partners & string_partners
        if len(overlap) >= 2:
            bonus += 0.5
            details.append(f"IntAct + STRING overlap ({len(overlap)} shared partners) (+0.5)")

    return bonus, details


def format_key_papers(key_papers):
    lines = []
    for i, paper in enumerate(key_papers[:5]):
        pmid = paper.get("pmid", "")
        title = paper.get("title", "")
        journal = paper.get("journal", "")
        pubdate = paper.get("pubdate", "")
        authors = paper.get("authors", [])
        first_author = authors[0] if authors else "Unknown"
        year = pubdate.split()[0] if pubdate else ""
        lines.append(f"{i+1}. {first_author} et al. ({year}). \"{title}\". *{journal}*. PMID: {pmid}")
    return "\n".join(lines)


def format_intact_table(physical_intact, max_rows=8):
    lines = []
    for entry in physical_intact[:max_rows]:
        partner = entry.get("partner", "?")
        method = entry.get("method", "").split("(")[-1].replace(")", "") if "(" in entry.get("method", "") else entry.get("method", "")
        pmid_raw = entry.get("pmid", "")
        pmid = ""
        for part in pmid_raw.split("|"):
            if "pubmed:" in part:
                pmid = part.replace("pubmed:", "")
                break
        interaction = entry.get("interaction_type", "")
        itype = "physical association" if "MI:0915" in interaction else ("direct interaction" if "MI:0407" in interaction else "association")
        # Determine if chromatin regulatory
        cr_keywords = ["EZH2", "SUZ12", "EED", "SMARC", "KDM", "HDAC", "TP53", "BRCA", "RIF1", "MAD2L2",
                       "CTBP", "KAT5", "HELLS", "CHD", "MBD", "DNMT", "SETD", "KMT", "PRC", "COMPASS",
                       "SWI/SNF", "NuRD", "SAGA", "TFIID", "MED", "POLR", "DAXX", "ATRX", "HIRA",
                       "SMCHD1", "PHF19", "MTF2", "MYSM1", "PBRM1", "RBBP"]
        is_cr = any(cp in partner.upper() for cp in cr_keywords)
        lines.append(f"| {partner} | {method} | {pmid} | {itype} | {'Yes' if is_cr else '—'} |")
    if len(physical_intact) > max_rows:
        lines.append(f"| ... ({len(physical_intact) - max_rows} more) | | | | |")
    return "\n".join(lines)


def format_string_table(string_data, max_rows=8):
    lines = []
    for entry in (string_data or [])[:max_rows]:
        partner = entry.get("partner", "?")
        score = entry.get("score", 0)
        experimental = entry.get("experimental", 0)
        cr_keywords = ["EZH2", "SUZ12", "EED", "SMARC", "KDM", "HDAC", "TP53", "BRCA", "RIF1", "MAD2L2",
                       "CTBP", "KAT5", "HELLS", "CHD", "MBD", "DNMT", "SETD", "KMT", "PRC", "COMPASS",
                       "SWI/SNF", "NuRD", "SAGA", "TFIID", "MED", "POLR", "DAXX", "ATRX", "HIRA",
                       "SMCHD1", "PHF19", "MTF2", "MYSM1", "PBRM1", "RBBP", "KAT"]
        is_cr = any(cp in partner.upper() for cp in cr_keywords)
        lines.append(f"| {partner} | {score:.3f} | {experimental:.3f} | {'Yes' if is_cr else '—'} |")
    if isinstance(string_data, list) and len(string_data) > max_rows:
        lines.append(f"| ... ({len(string_data) - max_rows} more) | | | |")
    return "\n".join(lines)


def generate_report(packet):
    gene = packet["gene"]
    u = safe_get(packet, "uniprot", "data", default={})
    h = safe_get(packet, "hpa", "data", default={})
    pm = safe_get(packet, "pubmed", "data", default={})
    af = safe_get(packet, "alphafold", "data", default={})
    string_data = safe_get(packet, "string", "data", default=[])
    intact_data = safe_get(packet, "intact", "data", default=[])

    uniprot_found = u.get("found", False)

    if not uniprot_found:
        # SIRAL1 case
        length_aa = None
        mass_kda = None
        accession = "N/A"
        protein_name = "Unknown"
        aliases = []
        function = []
    else:
        length_aa = u.get("length_aa", 0)
        mass_kda = u.get("mass_kda", 0)
        accession = u.get("accession", "N/A")
        protein_name = u.get("protein_name", "Unknown")
        aliases = u.get("aliases", [])
        function = u.get("function", [])

    # Scoring
    nuc_score, nuc_reason = score_nuclear(packet)
    size_score, size_reason = score_size(length_aa)
    pubmed_count = pm.get("strict_count", 0) if pm else 0

    # Check reject conditions
    rejected = False
    reject_reason = ""
    if nuc_score <= 3:
        rejected = True
        reject_reason = f"Nuclear localization score {nuc_score}/10 (threshold: >3). {nuc_reason}"
    if pubmed_count > 100:
        rejected = True
        if reject_reason:
            reject_reason += f"; PubMed count {pubmed_count} > 100 (threshold: ≤100)"
        else:
            reject_reason = f"PubMed count {pubmed_count} > 100 (threshold: ≤100)"

    nov_score, nov_reason = score_novelty(pubmed_count)
    struct_score, struct_reason = score_structure(packet)
    dom_score, dom_reason = score_domains(packet)
    ppi_score, ppi_reason = score_ppi(packet)
    cv_bonus, cv_details = score_cross_validation(packet)

    raw_total = (nuc_score * 4) + (size_score * 1) + (nov_score * 5) + (struct_score * 3) + (dom_score * 2) + (ppi_score * 3) + cv_bonus
    normalized = raw_total / 1.83

    # Build report
    alias_str = ", ".join(aliases) if aliases else "—"
    func_summary = function[0][:200] + "..." if function and len(function[0]) > 200 else (function[0] if function else "—")

    # HPA info
    hpa_status = h.get("status", "")
    hpa_reliability = h.get("reliability_if", "N/A")
    hpa_main = h.get("subcellular_main_location", [])
    hpa_additional = h.get("subcellular_additional_location", [])
    hpa_all = h.get("subcellular_location", [])

    # UniProt subcellular
    uniprot_locs = u.get("subcellular_locations", [])
    go_cc = u.get("go_cc", [])

    # PDB
    pdb_entries = u.get("pdb", [])

    # AlphaFold
    plddt_stats = af.get("plddt_stats", {})

    # STRING
    string_count = len(string_data) if isinstance(string_data, list) else 0

    # IntAct
    physical_intact = count_phys_intact(intact_data) if isinstance(intact_data, list) else []
    intact_count = len(intact_data) if isinstance(intact_data, list) else 0

    # InterPro/Pfam
    interpro = u.get("interpro", [])
    pfam = u.get("pfam", [])

    # Key papers
    key_papers = pm.get("key_papers", []) if pm else []

    # PPI regulatory analysis
    chromatin_partners_list = ["EZH2", "SUZ12", "EED", "RBBP", "MTF2", "PHF19", "SMARC",
                              "KDM", "HDAC", "TP53", "BRCA", "RIF1", "MAD2L2", "CTBP",
                              "KAT5", "HELLS", "CHD", "MBD", "DNMT", "SETD", "KMT",
                              "PRC", "COMPASS", "SWI/SNF", "NuRD", "SAGA", "TFIID",
                              "MED", "POLR", "DAXX", "ATRX", "HIRA", "SMCHD1", "MYSM1",
                              "PBRM1", "IKZF"]
    cr_in_intact = [x for x in physical_intact if any(cp in x.get("partner", "").upper() for cp in chromatin_partners_list)]
    cr_in_string = [x for x in (string_data or []) if isinstance(string_data, list) and any(cp in x.get("partner", "").upper() for cp in chromatin_partners_list)]

    # GO-CC nuclear
    nuclear_go = [x for x in go_cc if any(kw in x.get("term", "").lower() for kw in ["nucleus", "nucleoplasm", "nucleoli", "chromosome", "chromatin", "nuclear"])]

    # Format UniProt locations table
    loc_rows = []
    for loc in uniprot_locs:
        location = loc.get("location", "")
        ev = loc.get("evidences", [])
        if ev:
            ev_str = ", ".join(ev)
        else:
            ev_str = "Annotation"
        loc_rows.append(f"| UniProt | {location} | {ev_str} |")
    for cc in nuclear_go:
        loc_rows.append(f"| GO-CC | {cc.get('term', '')} | {cc.get('evidence', '')} |")
    if hpa_all:
        hpa_loc_str = ", ".join(hpa_all)
        loc_rows.append(f"| HPA | {hpa_loc_str} | {hpa_reliability} |")

    loc_table = "\n".join(loc_rows) if loc_rows else "| — | No localization data available | — |"

    # Build report
    status = "rejected" if rejected else "scored"
    tags = "protein-scout, nuclear-protein, evaluation"
    if rejected:
        tags = "protein-scout, evaluation, rejected"

    report = f"""---
type: protein-evaluation
gene: "{gene}"
date: {TODAY}
tags: [{tags}]
status: {status}
---

## {gene} -- Evaluation Report

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | {gene} / {alias_str} |
| Protein Name | {protein_name} |
| Protein Size | {length_aa or '?'} aa / {mass_kda or '?'} kDa |
| UniProt ID | {accession} |
| Evaluation Date | {TODAY} |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | {nuc_score}/10 | x4 | **{nuc_score*4}** | {nuc_reason[:120]} |
| Protein Size | {size_score}/10 | x1 | **{size_score}** | {size_reason[:120]} |
| Research Novelty | {nov_score}/10 | x5 | **{nov_score*5}** | {nov_reason[:120]} |
| 3D Structure | {struct_score}/10 | x3 | **{struct_score*3}** | {struct_reason[:120]} |
| Regulatory Domains | {dom_score}/10 | x2 | **{dom_score*2}** | {dom_reason[:120]} |
| PPI Network | {ppi_score}/10 | x3 | **{ppi_score*3}** | {ppi_reason[:120]} |
| Cross-Validation Bonus | — | max +3 | **+{cv_bonus}** | {" | ".join(cv_details) if cv_details else "No bonus criteria met"} |
| **Raw Total** | | | **{raw_total}/183** | |
| **Normalized Total** | | | **{normalized:.1f}/100** | |

### 3. Nuclear Localization Evidence

| Source | Localization | Reliability/Evidence |
|--------|-------------|---------------------|
{loc_table}

**Assessment**: {nuc_reason}

"""

    if rejected:
        report += f"""
**DECISION**: REJECTED. {reject_reason}
"""

    # Section 4: Protein Size
    report += f"""
### 4. Protein Size Assessment

{size_reason}. The protein size is {'within' if size_score >= 8 else 'outside'} the ideal range for biochemical studies (200-800 aa optimal).

"""

    # Section 5: Research Novelty
    broad_count = pm.get("broad_count", "N/A") if pm else "N/A"
    symbol_count = pm.get("symbol_only_count", "N/A") if pm else "N/A"

    report += f"""
### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | {pubmed_count} |
| PubMed symbol-only count | {symbol_count} |
| PubMed broad count | {broad_count} |
| Novelty category | {'≤20 → 10' if pubmed_count <= 20 else ('21-50 → 8' if pubmed_count <= 50 else ('51-100 → 6' if pubmed_count <= 100 else '>100 → REJECTED'))} |

**Key Publications**:
{format_key_papers(key_papers)}

**Assessment**: {nov_reason}
"""

    if function:
        func_text = " ".join(function)[:600]
        report += f"""

**Function Summary**: {func_text}
"""

    # Section 6: 3D Structure
    report += f"""
### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold mean pLDDT | {plddt_stats.get('mean_plddt', 'N/A')} |
| pLDDT > 90 (high confidence) | {plddt_stats.get('pct_gt_90', 'N/A')}% |
| pLDDT 70-90 (moderate) | {plddt_stats.get('pct_70_90', 'N/A')}% |
| pLDDT 50-70 (low) | {plddt_stats.get('pct_50_70', 'N/A')}% |
| pLDDT < 50 (disordered) | {plddt_stats.get('pct_lt_50', 'N/A')}% |
| Available PDB Entries | {len(pdb_entries) if pdb_entries else 0} |
"""

    if pdb_entries:
        pdb_summary = []
        for pdb_e in pdb_entries[:5]:
            pdb_summary.append(f"  - {pdb_e.get('id', '?')}: {pdb_e.get('method', '?')}, {pdb_e.get('resolution', '?')}, chains {pdb_e.get('chains', '?')}")
        pdb_summary_str = "\n".join(pdb_summary)
        report += f"| PDB Details | {pdb_summary_str} |\n"

    report += f"""
**Assessment**: {struct_reason}
"""

    # Section 7: Domain Architecture
    report += f"""
### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
"""
    for ip in interpro:
        report += f"| InterPro | {ip.get('id', '')} | {ip.get('name', '—')} |\n"
    for pf in pfam:
        report += f"| Pfam | {pf.get('id', '')} | {pf.get('name', '—')} |\n"
    if not interpro and not pfam:
        report += "| — | No annotated domains | Novel protein — may harbor uncharacterized domains |\n"

    report += f"""
**Assessment**: {dom_reason}
"""

    # Section 8: PPI Network
    report += f"""
### 8. PPI Network Analysis

**Experimentally Verified Interactions (IntAct, physical association/direct interaction)**:
| Partner | Method | PMID | Type | Chromatin Regulatory? |
|---------|--------|------|------|----------------------|
{format_intact_table(physical_intact) if physical_intact else '| — | — | — | — | — |'}

**STRING Predicted Interactions (combined score >0.4)**:
| Partner | Combined Score | Experimental Score | Chromatin Regulatory? |
|---------|---------------|-------------------|----------------------|
{format_string_table(string_data) if isinstance(string_data, list) and string_data else '| — | — | — | — |'}

**Known Complex Membership (GO Cellular Component)**:
"""
    if go_cc:
        for cc in go_cc[:8]:
            report += f"- {cc.get('term', '')} ({cc.get('evidence', '')})\n"
    else:
        report += "- No complex annotations available\n"

    report += f"""
**PPI Assessment**: {ppi_reason}
"""

    # Section 9: Cross-validation
    report += f"""
### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Localization | HPA + UniProt | {"Nuclear confirmed" if nuc_score >= 7 else ("Nuclear + other" if nuc_score >= 4 else "Non-nuclear/ambiguous")} | {"Yes" if nuc_score >= 5 else "Partial/No"} |
| 3D Structure | AlphaFold + PDB | {"Experimental structure available" if pdb_entries else "AlphaFold only"} | {"Consistent" if pdb_entries or af.get("found") else "Limited"} |
| PPI | IntAct + STRING | {f"{intact_count} IntAct, {string_count} STRING" if intact_count or string_count else "No PPI data"} | {"Multiple sources" if intact_count and string_count else "Single/No source"} |

**Cross-Validation Bonus Details**:
"""
    if cv_details:
        for d in cv_details:
            report += f"- {d}\n"
    else:
        report += "- No bonus criteria met across databases.\n"
    report += f"- **Total Cross-Validation Bonus**: +{cv_bonus} / max +3\n"

    # Section 10: Overall Assessment
    report += f"""
### 10. Overall Assessment

**Recommendation Level**: {'NOT RECOMMENDED -- REJECTED' if rejected else ('PROMISING' if normalized >= 60 else ('MODERATE' if normalized >= 40 else 'WEAK -- LOW PRIORITY'))}

**Normalized Score**: {normalized:.1f}/100 (Raw: {raw_total}/183)
"""

    if rejected:
        report += f"""
**Core Reasons for Rejection**:
{reject_reason}
"""
    else:
        strengths = []
        weaknesses = []
        if nuc_score >= 7:
            strengths.append(f"Strong nuclear localization (score {nuc_score}/10)")
        else:
            weaknesses.append(f"Sub-optimal nuclear localization (score {nuc_score}/10)")

        if nov_score >= 8:
            strengths.append(f"Excellent research novelty ({pubmed_count} publications)")
        elif nov_score >= 6:
            strengths.append(f"Moderate research novelty ({pubmed_count} publications)")

        if struct_score >= 7:
            strengths.append(f"Good 3D structural quality (mean pLDDT {plddt_stats.get('mean_plddt', 'N/A')})")

        if ppi_score >= 6:
            strengths.append(f"Promising PPI network with physical interaction evidence")

        strengths_text = "".join(f'1. {s}\n' for s in strengths) if strengths else '1. Insufficient strengths to justify pursuit\n'
        weaknesses_text = "".join(f'1. {w}\n' for w in weaknesses) if weaknesses else '1. No major identified weaknesses beyond novelty limitations\n'
        report += f"""
**Strengths**:
{strengths_text}
**Weaknesses**:
{weaknesses_text}
"""

    # Section 11: Decision
    report += f"""
### 11. Decision

**FINAL DECISION**: {'REJECTED' if rejected else 'SCORED — Eligible for further evaluation'}. """
    if rejected:
        report += f"Automatically rejected. {reject_reason}"
    else:
        report += f"Normalized score: {normalized:.1f}/100. "
        if normalized >= 60:
            report += "Strong candidate for follow-up studies."
        elif normalized >= 40:
            report += "Moderate candidate; may warrant follow-up with additional data."
        else:
            report += "Weak candidate; consider only if specific biological rationale exists."

    report += f"""

### 12. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/{accession}
- HPA: {h.get('hpa_gene_url', 'https://www.proteinatlas.org/') or 'https://www.proteinatlas.org/'}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22{gene}%22
- STRING: https://string-db.org/
- IntAct: https://www.ebi.ac.uk/intact/
- AlphaFold: https://alphafold.ebi.ac.uk/
"""

    return report


def main():
    os.makedirs(STAGE_DIR, exist_ok=True)
    for gene in GENES:
        print(f"Processing {gene}...")
        try:
            packet = load_packet(gene)
            report = generate_report(packet)
            out_path = os.path.join(STAGE_DIR, f"{gene}-evaluation.md")
            with open(out_path, 'w') as f:
                f.write(report)
            lines = report.split('\n')
            print(f"  -> {out_path} ({len(report)} chars, {len(lines)} lines)")
        except Exception as e:
            print(f"  ERROR: {gene}: {e}")


if __name__ == "__main__":
    main()
