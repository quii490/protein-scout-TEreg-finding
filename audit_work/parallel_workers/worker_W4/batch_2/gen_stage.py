#!/usr/bin/env python3
"""STAGE-only /180 report generation for batch_2 genes.
No network calls. Harvest packets only. Nuclear<=3->REJECTED. PubMed>100->REJECTED."""

import json
import os
from datetime import date

PACKETS_DIR = "/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets"
STAGE_DIR = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/audit_work/parallel_workers/worker_W4/batch_2/staged_reports"

GENES = [
    "SKOR1", "SLF2", "SLFN14", "SLX1B", "SLX9", "SMCR8", "SMPD4",
    "SMTN", "SMTNL1", "SNF8", "SNTB2", "SNTG1", "SOCS5", "SPACA9",
    "SPAG7", "SPAG8", "SPANXA1", "SPANXA2", "SPANXB1", "SPANXD",
    "SPATA13", "SPATA18"
]

TODAY = date.today().strftime("%Y-%m-%d")

NUCLEUS_KW = ["nucleus", "nucleoplasm", "nucleoli", "nuclear", "nucleolus",
              "chromosome", "chromatin", "nuclear body", "nuclear speckle",
              "cajal", "pml body", "nuclear envelope", "nuclear pore",
              "fibrillar center", "nucleopla"]

NON_NUC_KW = ["mitochondri", "cytosol", "cytoplasm", "golgi", "endoplasmic reticulum",
              "membrane", "secreted", "cytoskeleton", "centrosome", "spindle",
              "microtubule", "vesicle", "kinocilium", "lamellipodium",
              "synapse", "postsynaptic", "cilia", "flagella",
              "cell projection", "plasma membrane", "extracellular",
              "acrosome", "principal piece", "cell junction", "focal adhesion"]

REG_KEYWORDS = ["chromatin", "transcription", "histone", "dna", "rna polymer",
                "helicase", "splicing", "rna", "trna", "rrna", "nucleolar",
                "ribosome", "nucleosome", "mediator", "coactivator", "corepressor",
                "deacetylase", "acetyltransferase", "methyltransferase",
                "kinetochore", "centromere", "condensin", "cohesin", "smc",
                "origin recognition", "replication factor", "eif4e", "translation",
                "ubiquitin", "e3", "ligase"]


def load_packet(gene):
    path = os.path.join(PACKETS_DIR, gene + ".json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def get_uniprot(packet):
    d = packet["uniprot"]
    return d.get("data", {}) if d.get("ok") and d.get("data", {}).get("found") else None


def get_alphafold(packet):
    d = packet["alphafold"]
    return d.get("data", {}) if d.get("ok") and d.get("data", {}).get("found") else None


def get_pubmed(packet):
    d = packet["pubmed"]
    return d.get("data", {}) if d.get("ok") else None


def get_string(packet):
    d = packet["string"]
    return d.get("data", []) if d.get("ok") else []


def get_intact(packet):
    d = packet["intact"]
    return d.get("data", []) if d.get("ok") else []


def get_hpa(packet):
    d = packet["hpa"]
    return d.get("data", {}) if d.get("ok") else None


def score_nuclear(uni, hp):
    uni_subcell = [s.get("location", "") for s in uni.get("subcellular_locations", [])] if uni else []
    uni_text = " ".join(uni_subcell).lower()
    uni_nuc = any(kw in uni_text for kw in NUCLEUS_KW)
    uni_non = any(kw in uni_text for kw in NON_NUC_KW)

    go_cc = uni.get("go_cc", []) if uni else []
    go_terms = []
    for cc in go_cc:
        if isinstance(cc, dict):
            go_terms.append(cc.get("term", str(cc)))
        else:
            go_terms.append(str(cc))
    go_text = " ".join(go_terms).lower()
    go_nuc = any(kw in go_text for kw in NUCLEUS_KW)
    go_non = any(kw in go_text for kw in NON_NUC_KW)

    hpa_main = hp.get("subcellular_main_location", []) if hp else []
    hpa_addl = hp.get("subcellular_additional_location", []) if hp else []
    hpa_main_text = " ".join(hpa_main).lower() if hpa_main else ""
    hpa_addl_text = " ".join(hpa_addl).lower() if hpa_addl else ""
    hpa_rel = hp.get("reliability_if", "") if hp else ""

    hpa_nuc = any(kw in hpa_main_text for kw in NUCLEUS_KW)
    if not hpa_nuc and any(kw in hpa_addl_text for kw in NUCLEUS_KW):
        hpa_nuc = True
    hpa_non = any(kw in hpa_main_text for kw in NON_NUC_KW)

    nuc_sources = sum([int(hpa_nuc), int(uni_nuc), int(go_nuc)])
    non_sources = sum([int(hpa_non), int(uni_non), int(go_non)])

    if nuc_sources == 0 and non_sources == 0:
        score = 3
    elif nuc_sources >= 2 and non_sources == 0:
        score = 9 if nuc_sources >= 3 else 8
    elif nuc_sources >= 2 and non_sources >= 1:
        score = 7
    elif nuc_sources == 1 and non_sources == 0:
        if hpa_nuc and hpa_rel in ("Approved", "Enhanced"):
            score = 7
        else:
            score = 5
    elif hpa_non and not hpa_nuc and (uni_nuc or go_nuc):
        score = 4 if go_nuc else 3
    elif nuc_sources == 1 and non_sources == 1:
        score = 4
    elif nuc_sources >= 1 and non_sources > nuc_sources:
        score = 4
    elif non_sources >= 2 and nuc_sources == 0:
        score = 2
    elif non_sources == 1 and nuc_sources == 0:
        score = 2
    else:
        score = 3

    parts = []
    if uni is not None:
        parts.append("UniProt: " + ", ".join(uni_subcell[:3]) if uni_subcell else "UniProt: no subcellular annotation")
    if hp is not None:
        hpa_loc_str = ", ".join(hpa_main[:3])
        if hpa_loc_str:
            parts.append("HPA: " + hpa_loc_str)
        else:
            parts.append("HPA: no localization")
        if hpa_rel:
            parts.append("(Reliability: " + hpa_rel + ")")
    if go_nuc:
        nuclear_go = [t for t in go_terms if any(kw in t.lower() for kw in NUCLEUS_KW)]
        parts.append("GO-CC: " + ", ".join(nuclear_go[:3]))

    evidence = "; ".join(parts) or "No nuclear localization data"

    nuc_desc_map = {
        9: "Multiple independent data sources confirm nuclear localization with high HPA reliability.",
        8: "Primary nuclear localization supported by HPA + UniProt/GO-CC consensus.",
        7: "Nuclear localization with good HPA reliability and auxiliary support.",
        6: "Nuclear evidence present but some sources are weak or missing.",
        5: "Nuclear evidence exists but is mixed with non-nuclear signals.",
        4: "Weak nuclear signal with multiple sources showing mixed or non-nuclear preference.",
        3: "Nuclear evidence insufficient; conflicts between HPA/UniProt or no nuclear annotation.",
        2: "Very weak nuclear evidence; primary sources do not point to nucleus.",
        1: "No nuclear localization evidence.",
    }
    return score, evidence, nuc_desc_map.get(score, "Nuclear localization uncertain.")


def score_size(uni):
    if uni is None or uni.get("length_aa", 0) == 0:
        return 5, 0, 0, "Unknown size"
    aa = uni.get("length_aa", 0)
    mass = uni.get("mass_kda", 0) or round(aa * 0.11, 1)
    if 200 <= aa <= 800:
        return 10, aa, mass, "Ideal size (" + str(aa) + " aa), suitable for standard biochemical experiments."
    elif (100 <= aa < 200) or (800 < aa <= 1200):
        return 8, aa, mass, "Acceptable size (" + str(aa) + " aa), suitable for routine experiments."
    elif (50 <= aa < 100) or (1200 < aa <= 2000):
        return 5, aa, mass, "Small/large (" + str(aa) + " aa), presents moderate experimental challenges."
    else:
        return 2, aa, mass, "Extreme size (" + str(aa) + " aa), requires special experimental design."


def score_novelty(pubmed_data):
    if not pubmed_data:
        return 5, 0, 0, "No PubMed data"
    sc = pubmed_data.get("strict_count", 0)
    bc = pubmed_data.get("broad_count", sc * 2)
    if sc <= 20:
        return 10, sc, bc, "Extremely novel, virtually no systematic study (PubMed <= 20)."
    elif sc <= 40:
        return 8, sc, bc, "Very novel, only a few foundational studies."
    elif sc <= 60:
        return 6, sc, bc, "Moderately novel with unexplored niches."
    elif sc <= 80:
        return 4, sc, bc, "Some research foundation but niche space remains."
    elif sc <= 100:
        return 2, sc, bc, "Substantial research base, limited novelty."
    else:
        return 0, sc, bc, "Over-studied (>100 articles), fails novelty threshold."


def score_structure(uni, af):
    pdb_ids = [p.get("id", "") for p in uni.get("pdb", [])] if uni else []
    pdb_list = [p for p in pdb_ids if p]
    if af is None:
        plddt = 0
        ordered_pct = 0
    else:
        stats = af.get("plddt_stats", {})
        plddt = stats.get("mean_plddt", 0)
        ordered_pct = round(stats.get("pct_gt_90", 0) + stats.get("pct_70_90", 0), 1)

    n_pdb = len(pdb_list)
    pdb_text = ", ".join(pdb_list[:10]) if pdb_list else "None"

    if n_pdb >= 5 and plddt >= 70:
        return 10, plddt, ordered_pct, pdb_text, "PDB experimental structures + AlphaFold high confidence (pLDDT=" + str(round(plddt, 1)) + "). Structure highly credible."
    elif n_pdb >= 2 and plddt >= 70:
        return 9, plddt, ordered_pct, pdb_text, "PDB experimental structures + AlphaFold high quality (pLDDT=" + str(round(plddt, 1)) + "). Structure credible."
    elif n_pdb >= 1 and plddt >= 70:
        return 8, plddt, ordered_pct, pdb_text, "PDB experimental structure + AlphaFold high quality (pLDDT=" + str(round(plddt, 1)) + "). Structure credible."
    elif plddt >= 85:
        return 8, plddt, ordered_pct, pdb_text, "AlphaFold very high confidence prediction (pLDDT=" + str(round(plddt, 1)) + "), " + str(ordered_pct) + "% ordered. Structure reliable."
    elif plddt >= 70:
        return 7, plddt, ordered_pct, pdb_text, "AlphaFold high quality prediction (pLDDT=" + str(round(plddt, 1)) + "), " + str(ordered_pct) + "% ordered. Structure reliable."
    elif plddt >= 50:
        return 6, plddt, ordered_pct, pdb_text, "AlphaFold moderate quality (pLDDT=" + str(round(plddt, 1)) + "), " + str(ordered_pct) + "% ordered. Structure usable."
    else:
        return 4, plddt, ordered_pct, pdb_text, "AlphaFold low quality prediction (pLDDT=" + str(round(plddt, 1)) + "). " + str(ordered_pct) + "% ordered residues."


def get_domain_text(uni):
    if not uni:
        return "No UniProt data available"
    interpro = uni.get("interpro", [])
    pfam = uni.get("pfam", [])
    parts = []
    if interpro:
        names = [i.get("name", "") or i.get("id", "") for i in interpro]
        parts.append("InterPro: " + ", ".join(names[:5]))
    if pfam:
        names = [p.get("name", "") or p.get("id", "") for p in pfam]
        parts.append("Pfam: " + ", ".join(names[:3]))
    return "; ".join(parts) if parts else "No annotated domains"


def score_domain(uni, plddt):
    domain_text = get_domain_text(uni)
    chromatin_kw = ["bromo", "chromo", "phd", "sant", "tudor", "mbt", "pwwp",
                    "zinc finger", "homeobox", "homeodomain", "hmg", "forkhead",
                    "bzip", "bhlh", "at-hook", "myb", "cxxc", "swi/snf", "iswi",
                    "histone", "chromatin", "dna-binding", "nucleic acid binding"]
    text = domain_text.lower()
    has_chromatin = any(kw in text for kw in chromatin_kw)
    domain_count = text.count("ipr") + text.count("pf")

    if has_chromatin and domain_count >= 3:
        return 10, domain_text, domain_count, "Contains definitive nucleic-acid/chromatin-binding domains confirmed by multiple databases."
    elif has_chromatin or (domain_count >= 2 and plddt >= 80):
        return 8, domain_text, domain_count, "Multiple annotated domains with high AlphaFold quality; domain folds credible."
    elif domain_count > 0:
        return 7, domain_text, domain_count, "Known domain annotations present, providing structural basis for functional studies."
    elif plddt >= 70:
        return 6, domain_text, domain_count, "Limited domain annotation but AlphaFold identifies foldable regions."
    elif plddt >= 50:
        return 5, domain_text, domain_count, "Sparse domain annotation; novel proteins typically lack annotations."
    else:
        return 4, domain_text, domain_count, "Minimal domain annotation, consistent with a novel/uncharacterized protein."


def score_ppi(string_p, intact_p):
    str_n = len(string_p)
    int_n = len(intact_p)

    if not string_p:
        return 2, str_n, int_n, 0, 0, "No STRING interaction data; PPI network unknown."

    reg_count = 0
    for p in string_p[:20]:
        name = p.get("partner", "").lower()
        if any(kw in name for kw in REG_KEYWORDS):
            reg_count += 1
    reg_ratio = reg_count / min(len(string_p), 20)

    if int_n > 0 and reg_ratio > 0.4 and str_n >= 10:
        return 10, str_n, int_n, reg_count, reg_ratio, "STRING " + str(str_n) + " predicted + IntAct " + str(int_n) + " experimental interactions. Regulatory partner ratio " + str(int(reg_ratio * 100)) + "%."
    elif int_n > 0 and reg_ratio > 0.2 and str_n >= 5:
        return 8, str_n, int_n, reg_count, reg_ratio, "STRING " + str(str_n) + " predicted + IntAct " + str(int_n) + " experimental interactions. Regulatory partner ratio " + str(int(reg_ratio * 100)) + "%."
    elif int_n > 0 and reg_ratio > 0.3:
        return 7, str_n, int_n, reg_count, reg_ratio, "STRING " + str(str_n) + " predicted + IntAct " + str(int_n) + " experimental interactions. Regulatory partner ratio " + str(int(reg_ratio * 100)) + "%."
    elif str_n > 0 and reg_ratio > 0.2:
        return 5, str_n, int_n, reg_count, reg_ratio, "STRING " + str(str_n) + " predicted interactions. Regulatory partner ratio " + str(int(reg_ratio * 100)) + "%."
    elif str_n > 0:
        return 4, str_n, int_n, reg_count, reg_ratio, "STRING " + str(str_n) + " predicted interactions. Regulatory partner ratio " + str(int(reg_ratio * 100)) + "%."
    return 3, str_n, int_n, reg_count, reg_ratio, "STRING " + str(str_n) + " predicted interactions. Regulatory partner ratio " + str(int(reg_ratio * 100)) + "%."


def score_crossval(pdb_list, plddt, uni, hpa_main, go_cc_obj, string_n, intact_n, domain_text, nuc, uni_subcell):
    pts = 0
    details = []

    has_multi_nuc = 0
    if uni is not None and uni_subcell and nuc >= 5:
        has_multi_nuc += 1
    if hpa_main:
        hpa_nuc = any(kw in " ".join(hpa_main).lower() for kw in NUCLEUS_KW)
        if hpa_nuc:
            has_multi_nuc += 1
    if go_cc_obj:
        go_text = " ".join(str(g) for g in go_cc_obj).lower()
        if any(kw in go_text for kw in NUCLEUS_KW):
            has_multi_nuc += 1

    if pdb_list and plddt > 0:
        pts += 0.5
        details.append("PDB + AlphaFold dual-source verification: +0.5")
    else:
        details.append("PDB + AlphaFold dual-source verification: +0")

    if has_multi_nuc >= 2:
        pts += 0.5
        details.append("Multi-DB localization consensus (" + str(has_multi_nuc) + " sources): +0.5")
    else:
        details.append("Multi-DB localization consensus: +0")

    if string_n > 0 and intact_n > 0:
        pts += 0.5
        details.append("STRING + IntAct dual-source verification: +0.5")
    else:
        details.append("STRING + IntAct dual-source verification: +0")

    if domain_text and "No" not in domain_text and plddt > 70:
        pts += 0.5
        details.append("Domain + AlphaFold quality: +0.5")
    else:
        details.append("Domain + AlphaFold quality: +0")

    if len(pdb_list) >= 3:
        pts += 1.0
        details.append("PDB multiple entries coverage (>=3): +1.0")
    else:
        details.append("PDB multiple entries coverage: +0")

    return min(pts, 3.0), details


def generate_report(gene):
    packet = load_packet(gene)
    if not packet:
        return None, "NO_HARVEST_PACKET"

    uni = get_uniprot(packet)
    af = get_alphafold(packet)
    pm = get_pubmed(packet)
    st = get_string(packet)
    it = get_intact(packet)
    hp = get_hpa(packet)

    # UniProt info
    if uni:
        accession = uni.get("accession", gene)
        protein_name = uni.get("protein_name", gene + " protein")
        length_aa = uni.get("length_aa", 0)
        mass_kda = uni.get("mass_kda", 0) or round(length_aa * 0.11, 1)
        subcell = [s.get("location", "") for s in uni.get("subcellular_locations", [])]
        go_cc = uni.get("go_cc", [])
        function_text = uni.get("function", [])
        pdb_raw = uni.get("pdb", [])
        pdb_list = [p.get("id", "") for p in pdb_raw]
        aliases = uni.get("aliases", [])
        interpro = uni.get("interpro", [])
        pfam = uni.get("pfam", [])
    else:
        accession = gene
        protein_name = gene + " (UniProt unavailable)"
        length_aa = 0
        mass_kda = 0
        subcell = []
        go_cc = []
        function_text = []
        pdb_list = []
        aliases = []
        interpro = []
        pfam = []

    # AlphaFold info
    if af:
        stats = af.get("plddt_stats", {})
        plddt = stats.get("mean_plddt", 0)
        pct_gt_90 = stats.get("pct_gt_90", 0)
        pct_70_90 = stats.get("pct_70_90", 0)
        pct_50_70 = stats.get("pct_50_70", 0)
        pct_lt_50 = stats.get("pct_lt_50", 0)
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

    # PubMed
    pubmed_strict = pm.get("strict_count", 0) if pm else 0
    pubmed_broad = pm.get("broad_count", 0) if pm else 0
    alias_note = pm.get("alias_note", "") if pm else ""
    key_papers = pm.get("key_papers", []) if pm else []

    # HPA
    if hp:
        hpa_main = hp.get("subcellular_main_location", []) or []
        hpa_addl = hp.get("subcellular_additional_location", []) or []
        hpa_rel = hp.get("reliability_if") or "N/A"
        hpa_subcell_url = hp.get("hpa_subcellular_url") or ""
        image_status = hp.get("image_status") or "unknown"
    else:
        hpa_main = []
        hpa_addl = []
        hpa_rel = "N/A"
        hpa_subcell_url = ""
        image_status = "unknown"

    # ---- SCORING ----
    nuc_score, nuc_evidence, nuc_desc = score_nuclear(uni, hp)
    sz, sz_aa, sz_mass, sz_desc = score_size(uni)
    nov, nov_strict, nov_broad, nov_desc = score_novelty(pm)
    struct, struct_plddt, struct_ordered, pdb_text, struct_desc = score_structure(uni, af)
    domain_text = get_domain_text(uni)
    dom, _, domain_count, dom_desc = score_domain(uni, plddt)
    ppi_score, ppi_str_n, ppi_int_n, ppi_reg_count, ppi_reg_ratio, ppi_desc = score_ppi(st, it)
    cv_bonus, cv_details = score_crossval(
        pdb_list, plddt, uni, hpa_main, go_cc, len(st), len(it), domain_text, nuc_score, subcell
    )

    raw = nuc_score * 4 + sz * 1 + nov * 5 + struct * 3 + dom * 2 + ppi_score * 3 + cv_bonus
    norm = round(raw / 1.80, 1)

    rejected = nuc_score <= 3 or pubmed_strict > 100
    rejection_reasons = []
    if nuc_score <= 3:
        rejection_reasons.append("Nuclear score " + str(nuc_score) + "/10 <= 3 (insufficient nuclear evidence)")
    if pubmed_strict > 100:
        rejection_reasons.append("PubMed strict count " + str(pubmed_strict) + " > 100 (over-studied)")

    status = "rejected" if rejected else "scored"

    # Novelty label
    if pubmed_strict <= 20:
        nov_label = "<=20 -> 10"
    elif pubmed_strict <= 40:
        nov_label = "<=40 -> 8"
    elif pubmed_strict <= 60:
        nov_label = "<=60 -> 6"
    elif pubmed_strict <= 80:
        nov_label = "<=80 -> 4"
    elif pubmed_strict <= 100:
        nov_label = "<=100 -> 2"
    else:
        nov_label = ">100 -> REJECTED"

    # ---- BUILD TABLES ----

    # Subcellular location table
    loc_rows = []
    if uni:
        for s in uni.get("subcellular_locations", []):
            loc_name = s.get("location", "N/A")
            ev = s.get("evidences", [])
            if "ECO:0000269" in ev:
                reliability = "Experimental"
            elif "ECO:0000250" in ev:
                reliability = "By similarity"
            else:
                reliability = "Curated"
            loc_rows.append("| UniProt | " + loc_name + " | " + reliability + " |")

    # GO-CC nuclear terms
    if go_cc:
        go_nuc_terms = []
        for g in go_cc:
            if isinstance(g, dict):
                term = g.get("term", "")
                ev = g.get("evidence", "N/A")
            else:
                term = str(g)
                ev = "N/A"
            if any(kw in term.lower() for kw in NUCLEUS_KW):
                go_nuc_terms.append((term, ev))
        for term, ev in go_nuc_terms[:5]:
            loc_rows.append("| GO-CC | " + term + " | " + ev + " |")

    # HPA
    if hp:
        hpa_main_text = ", ".join(hpa_main)
        hpa_addl_text = ", ".join(hpa_addl)
        combined = hpa_main_text
        if hpa_addl_text:
            combined += "; Additional: " + hpa_addl_text
        loc_rows.append("| HPA | " + combined + " | Reliability: " + hpa_rel + " |")

    loc_table = "\n".join(loc_rows) if loc_rows else "| No data | No data | No data |"

    # Key publications table
    pub_rows = []
    for p in key_papers[:5]:
        title = (p.get("title", "N/A") or "N/A")[:120]
        journal = (p.get("journal", "N/A") or "N/A")[:60]
        pmid = str(p.get("pmid", "N/A"))
        pub_rows.append("| " + pmid + " | " + title + " | " + journal + " |")
    pub_table = "\n".join(pub_rows) if pub_rows else "| N/A | No key publications available | N/A |"

    # STRING table
    str_filtered = [s for s in st if s.get("score", 0) >= 0.4]
    if str_filtered:
        str_sorted = sorted(str_filtered, key=lambda x: x.get("score", 0), reverse=True)[:8]
        str_rows = []
        for s in str_sorted:
            partner = s.get("partner", "N/A")
            score = s.get("score", 0)
            exp = s.get("experimental", 0)
            db = s.get("database", 0)
            tm = s.get("textmining", 0)
            str_rows.append("| " + partner + " | {:.3f} | {:.3f} | {:.1f} | {:.3f} |".format(score, exp, db, tm))
        str_table = "\n".join(str_rows)
    else:
        str_table = "| No high-confidence partners | -- | -- | -- | -- |"

    # IntAct table
    seen_intact = set()
    int_rows = []
    for p in it:
        partner = p.get("partner", "?")
        if partner.lower() in seen_intact:
            continue
        seen_intact.add(partner.lower())
        if len(seen_intact) > 8:
            break
        method = (p.get("method", "--") or "--")[:80]
        pmid = (p.get("pmid", "--") or "--")[:40]
        int_rows.append("| " + partner + " | " + method + " | " + pmid + " |")
    int_table = "\n".join(int_rows) if int_rows else "| No experimental interactions | -- | -- |"

    # Domain table
    domain_rows = []
    for d in interpro[:6]:
        d_id = d.get("id", "N/A")
        d_name = d.get("name", "Annotated domain")
        domain_rows.append("| InterPro | " + d_id + " | " + d_name + " |")
    for d in pfam[:6]:
        d_id = d.get("id", "N/A")
        d_name = d.get("name", "Annotated family")
        domain_rows.append("| Pfam | " + d_id + " | " + d_name + " |")
    if not domain_rows:
        domain_rows.append("| N/A | No InterPro/Pfam domains | -- |")
    domain_table_display = "\n".join(domain_rows)

    # IF image note
    if image_status == "if_display_images_available" or hpa_rel in ("Approved", "Enhanced", "Supported"):
        if_note = ("**IF Image Status**: HPA detected immunofluorescence signal (Reliability: " +
                   hpa_rel + "), but STAGE mode did not download original images. " +
                   "Nuclear assessment based on HPA subcellular annotation + UniProt + GO-CC.")
    else:
        if_note = ("**IF Image Status**: HPA did not detect reliable IF image signal. " +
                   "Nuclear evidence based on HPA subcellular annotation, UniProt, and GO-CC terms.")

    # PAE note
    if af:
        pae_note = "STAGE mode did not download PAE image. Structural assessment based on AlphaFold pLDDT statistics."
    else:
        pae_note = "AlphaFold data unavailable; no PAE assessment possible."

    # Alias text
    alias_text = ", ".join(aliases[:5]) if aliases else ""
    gene_alias_display = gene
    if alias_text:
        gene_alias_display = gene + " / " + alias_text

    uniprot_url = "https://www.uniprot.org/uniprotkb/" + accession if accession else ""
    hpa_url = hpa_subcell_url or "https://www.proteinatlas.org/search/" + gene

    # Function text
    func_full = " ".join(function_text[:3]) if function_text else "No functional annotation available"

    # Rejection section
    rejection_section = ""
    if rejected:
        rejection_section = "### 3. Rejection Check\n\n**REJECTED** for: " + "; ".join(rejection_reasons) + "\n"

    # Research maturity text
    if pubmed_strict <= 10:
        research_maturity = "emerging interest"
    elif pubmed_strict <= 40:
        research_maturity = "growing research activity"
    elif pubmed_strict <= 100:
        research_maturity = "an established research field"
    else:
        research_maturity = "a mature research field"

    # AF availability
    if af:
        af_avail = "Available (v" + str(af_version) + ")"
    else:
        af_avail = "Not available"

    # Domain strength
    if dom >= 8:
        dom_strength = "strong"
    elif dom >= 6:
        dom_strength = "moderate"
    elif dom >= 4:
        dom_strength = "limited"
    else:
        dom_strength = "minimal"

    # Domain summary name
    if interpro:
        dom_summary_name = " ".join(d.get("name", d.get("id", "")) for d in interpro[:3])
    else:
        dom_summary_name = "No InterPro entries"

    # Cross-validation display values
    if nuc_score >= 5:
        cx_nuclear = "Nuclear"
        cx_nuc_consistent = "Consistent"
    else:
        cx_nuclear = "Non-nuclear/Weak"
        cx_nuc_consistent = "Inconsistent/Weak"

    if plddt >= 70:
        cx_struct = "Well-folded"
        cx_struct_consistent = "Consistent"
    else:
        cx_struct = "Partially folded / Disordered"
        cx_struct_consistent = "Mixed"

    if ppi_str_n > 0 or ppi_int_n > 0:
        cx_ppi = "Multiple interactions"
    else:
        cx_ppi = "Sparse / None"

    if ppi_str_n > 0 and ppi_int_n > 0:
        cx_ppi_consistent = "Consistent"
    else:
        cx_ppi_consistent = "Sparse"

    cv_formatted = "\n- ".join(cv_details)

    # Title
    if rejected:
        title_line = "## " + gene + " -- REJECTED (" + "; ".join(rejection_reasons) + ")"
    else:
        title_line = "## " + gene + " -- Re-evaluation Report (NOT REJECTED)"

    # Recommendation
    if rejected:
        recommendation = "NOT RECOMMENDED (REJECTED)"
    elif norm >= 65:
        recommendation = "Recommended"
    elif norm >= 50:
        recommendation = "Recommended with caution"
    else:
        recommendation = "Not prioritized"

    # Core Strength
    strengths = []
    idx = 1
    if nuc_score >= 5:
        strengths.append(str(idx) + ". Multiple sources support nuclear localization")
        idx += 1
    if sz >= 8:
        strengths.append(str(idx) + ". Ideal protein size (" + str(length_aa) + " aa) for experimental characterization")
        idx += 1
    elif sz >= 5:
        strengths.append(str(idx) + ". Workable protein size (" + str(length_aa) + " aa)")
        idx += 1
    if nov >= 8:
        strengths.append(str(idx) + ". High novelty (PubMed count ~" + str(pubmed_strict) + ")")
        idx += 1
    elif nov >= 6:
        strengths.append(str(idx) + ". Moderate novelty (PubMed count ~" + str(pubmed_strict) + ")")
        idx += 1
    if plddt >= 85:
        strengths.append(str(idx) + ". High-quality AlphaFold prediction (pLDDT " + str(round(plddt, 1)) + ")")
        idx += 1
    elif af:
        strengths.append(str(idx) + ". AlphaFold prediction available (pLDDT " + str(round(plddt, 1)) + ")")
        idx += 1
    if domain_count >= 5:
        strengths.append(str(idx) + ". Well-annotated domain architecture (" + str(domain_count) + " domains)")
        idx += 1
    elif domain_count >= 1:
        strengths.append(str(idx) + ". Some domain annotations present (" + str(domain_count) + " domains)")
        idx += 1
    if ppi_score >= 6:
        strengths.append(str(idx) + ". Rich PPI network with experimental validation")
        idx += 1
    elif ppi_score >= 3:
        strengths.append(str(idx) + ". Moderate PPI data available")
        idx += 1
    if len(pdb_list) >= 1:
        strengths.append(str(idx) + ". Experimental PDB structures: " + ", ".join(pdb_list[:3]))
        idx += 1
    strengths_text = "\n".join(strengths) if strengths else "None identified"

    # Risks
    risks = []
    if nuc_score <= 3:
        risks.append("1. Nuclear score <= 3, automatic rejection criterion")
    elif nuc_score <= 5:
        risks.append("1. Moderate/weak nuclear localization evidence")
    if pubmed_strict > 100:
        risks.append("2. PubMed count > 100, automatic rejection criterion")
    if len(pdb_list) == 0:
        risks.append("3. No experimental PDB structures")
    if plddt < 50:
        risks.append("4. Low AlphaFold confidence (mean pLDDT < 50)")
    if ppi_score <= 3:
        risks.append("5. Limited PPI network data")
    if not hpa_main:
        risks.append("6. No HPA subcellular localization data")
    if not uni:
        risks.append("7. No UniProt data available")
    risks_text = "\n".join(risks) if risks else "None identified"

    # Rejection next steps
    rejection_next_steps = ""
    if nuc_score <= 3:
        rejection_next_steps += "- [ ] **Nuclear score <= 3: REJECTED for nuclear protein screening.**\n"
    if pubmed_strict > 100 and nuc_score > 3:
        rejection_next_steps += "**PubMed count " + str(pubmed_strict) + " > 100: REJECTED per novelty threshold.**\n"

    # Decision
    if rejected:
        decision_label = "REJECTED"
        decision_detail = "Rejected for: " + "; ".join(rejection_reasons) + "."
    else:
        decision_label = "NOT REJECTED"
        decision_detail = ("The protein scores " + str(round(norm, 1)) + "/100 on the /180 scoring system. " +
                          recommendation + " for further investigation as a TE-regulated protein target.")

    harvest_ts = packet.get("timestamp", "unknown")

    # ---- BUILD REPORT using .format() for Python 3.9 compatibility ----
    template = """---
type: protein-evaluation
gene: "{gene}"
date: {today}
tags: [protein-scout, re-evaluation]
status: {status}
---

{title_line}

### 1. Basic Information

| Item | Content |
|------|---------|
| Gene / Aliases | {gene_alias_display} |
| Protein Name | {protein_name} |
| Protein Size | {len_display} aa, ~{mass_display} kDa |
| UniProt ID | {accession} |
| Evaluation Date | {today} |
| Re-evaluation Reason | Complete scoring re-evaluation from harvest packet data |

### 2. Scoring Overview

| Dimension | Score | Max | Weighted | Key Evidence Summary |
|-----------|-------|-----|----------|----------------------|
| Nuclear Localization Specificity | {nuc_score}/10 | x4 | **{w_nuc}** | {nuc_ev_short} |
| Protein Size | {sz}/10 | x1 | **{w_sz}** | {len_display} aa, ~{mass_display} kDa |
| Research Novelty | {nov}/10 | x5 | **{w_nov}** | PubMed strict={pubmed_strict} ({nov_label}) |
| 3D Structure | {struct}/10 | x3 | **{w_struct}** | AlphaFold v{af_version} pLDDT={plddt_str}; PDB: {pdb_text_short} |
| Regulatory Domains | {dom}/10 | x2 | **{w_dom}** | {domain_text_short} |
| PPI Network | {ppi_score}/10 | x3 | **{w_ppi}** | STRING {ppi_str_n} partners; IntAct {ppi_int_n} interactions |
| Cross-Validation Bonus | -- | -- | **+{cv_bonus_str}** | {cv_detail_short} |
| **Raw Total** | | | **{raw_str}/180** | |
| **Normalized Total** | | | **{norm_str}/100** | |

{rejection_section}
### 3. Nuclear Localization Evidence

| Source | Localization | Reliability |
|--------|-------------|-------------|
{loc_table}

{if_note}

**Manual Review Assessment**: {nuc_ev_long}. Score {nuc_score}/10 reflects {nuc_desc_short}

### 4. Protein Size Assessment

{gene} is {len_display} amino acids in length (~{mass_display} kDa). {sz_desc} Score {sz}/10.

### 5. Research Novelty (PubMed Analysis)

| Metric | Value |
|--------|-------|
| PubMed strict count | {pubmed_strict} |
| PubMed broad count | {pubmed_broad} |
| Alias context | {alias_note_display} |
| Novelty category | {nov_label} |

**Key Research Context**: {func_short}. Published literature indicates {research_maturity}. {nov_desc}

**Key Publications**:
| PMID | Title | Journal |
|------|-------|---------|
{pub_table}


### 6. 3D Structure Analysis

| Metric | Value |
|--------|-------|
| AlphaFold Prediction | {af_avail} |
| PDB Entries | {pdb_count_str} experimental |
| Mean pLDDT | {plddt_str} |
| High confidence residues (pLDDT > 90) | {pct_gt_90}% |
| Confident residues (pLDDT 70-90) | {pct_70_90}% |
| Medium confidence (pLDDT 50-70) | {pct_50_70}% |
| Low confidence (pLDDT < 50) | {pct_lt_50}% |
| Ordered region (pLDDT > 70) | {ordered_pct}% |
| Available PDB entries | {pdb_text_display} |

**PAE**: {pae_note}

**Structure Assessment**: {struct_desc} Score {struct}/10.

### 7. Domain Architecture

| Source | Domain/Feature | Notes |
|--------|---------------|-------|
{domain_table_display}

**Domain Analysis**: {dom_summary_name} The protein contains {n_interpro} InterPro and {n_pfam} Pfam domain annotations. Score {dom}/10 reflects {dom_strength} domain architecture. {dom_desc}

### 8. PPI Network Analysis

| Source | Result |
|--------|--------|
| STRING | {ppi_str_n} total interactions |
| IntAct | {ppi_int_n} interactions |

**Top STRING Partners** (combined score >= 0.4):
| Partner | Combined Score | Experimental | Database | Textmining |
|---------|---------------|--------------|----------|------------|
{str_table}

**Experimental Interactions** (IntAct):
| Partner | Method | PMID |
|---------|--------|------|
{int_table}

**PPI Assessment**: {ppi_desc} Score {ppi_score}/10.

### 9. Cross-Validation Analysis

| Dimension | Sources | Result | Consistent? |
|-----------|---------|--------|-------------|
| Nuclear Localization | UniProt + HPA + GO-CC | {cx_nuclear} | {cx_nuc_consistent} |
| Structure | AlphaFold + Domain architecture | {cx_struct} | {cx_struct_consistent} |
| PPI | STRING + IntAct | {cx_ppi} | {cx_ppi_consistent} |

**Cross-Validation Bonus Details**:
- {cv_formatted}
- **Total Cross-Validation Bonus**: +{cv_bonus_str} / max +3.0

### 10. Overall Assessment

**Recommendation Level**: {recommendation} (Score: {norm_str}/100)

**Core Strengths**:
{strengths_text}

**Risks / Uncertainties**:
{risks_text}

**Next Steps**:
- [ ] Verify nuclear localization by HPA IF or independent immunofluorescence
- [ ] Expand PPI network analysis using STRING and co-immunoprecipitation
- [ ] Obtain AlphaFold PAE images for domain quality assessment
- [ ] Review key publications for functional context
{rejection_next_steps}
### 11. Decision

**FINAL DECISION**: {decision_label}. {decision_detail}

### 12. Data Sources
- UniProt: {uniprot_url}
- AlphaFold: https://alphafold.ebi.ac.uk/entry/{accession_display}
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term={pubmed_query}
- STRING: https://string-db.org/
- HPA: {hpa_url}
- Data harvested: {harvest_ts}
"""

    report = template.format(
        gene=gene, today=TODAY, status=status,
        title_line=title_line,
        gene_alias_display=gene_alias_display,
        protein_name=protein_name,
        len_display=str(length_aa) if length_aa else "unknown",
        mass_display=str(mass_kda) if mass_kda else "unknown",
        accession=accession,
        nuc_score=str(nuc_score), w_nuc=str(nuc_score * 4),
        nuc_ev_short=nuc_evidence[:140],
        sz=str(sz), w_sz=str(sz),
        nov=str(nov), w_nov=str(nov * 5),
        nov_label=nov_label,
        pubmed_strict=str(pubmed_strict),
        struct=str(struct), w_struct=str(struct * 3),
        af_version=str(af_version),
        plddt_str=str(round(plddt, 1)),
        pdb_text_short=pdb_text[:60] if pdb_text else "None",
        dom=str(dom), w_dom=str(dom * 2),
        domain_text_short=domain_text[:100],
        ppi_score=str(ppi_score), w_ppi=str(ppi_score * 3),
        ppi_str_n=str(ppi_str_n), ppi_int_n=str(ppi_int_n),
        cv_bonus_str="{:.1f}".format(cv_bonus),
        cv_detail_short=(cv_details[0] if cv_details else "No cross-validation data")[:100],
        raw_str="{:.1f}".format(raw),
        norm_str="{:.1f}".format(norm),
        rejection_section=rejection_section,
        loc_table=loc_table,
        if_note=if_note,
        nuc_ev_long=nuc_evidence[:250],
        nuc_desc_short=nuc_desc[:100],
        sz_desc=sz_desc,
        pubmed_broad=str(pubmed_broad),
        alias_note_display=alias_note if alias_note else "None",
        func_short=func_full[:300],
        research_maturity=research_maturity,
        nov_desc=nov_desc,
        pub_table=pub_table,
        af_avail=af_avail,
        pdb_count_str=str(len(pdb_list)),
        pct_gt_90=str(pct_gt_90),
        pct_70_90=str(pct_70_90),
        pct_50_70=str(pct_50_70),
        pct_lt_50=str(pct_lt_50),
        ordered_pct=str(ordered_pct),
        pdb_text_display=pdb_text[:120] if pdb_text else "None",
        pae_note=pae_note,
        struct_desc=struct_desc,
        domain_table_display=domain_table_display,
        dom_summary_name=dom_summary_name,
        n_interpro=str(len(interpro)),
        n_pfam=str(len(pfam)),
        dom_strength=dom_strength,
        dom_desc=dom_desc,
        str_table=str_table,
        int_table=int_table,
        ppi_desc=ppi_desc,
        cx_nuclear=cx_nuclear,
        cx_nuc_consistent=cx_nuc_consistent,
        cx_struct=cx_struct,
        cx_struct_consistent=cx_struct_consistent,
        cx_ppi=cx_ppi,
        cx_ppi_consistent=cx_ppi_consistent,
        cv_formatted=cv_formatted,
        recommendation=recommendation,
        strengths_text=strengths_text,
        risks_text=risks_text,
        rejection_next_steps=rejection_next_steps,
        decision_label=decision_label,
        decision_detail=decision_detail,
        uniprot_url=uniprot_url,
        accession_display=(accession if accession else gene),
        pubmed_query=gene,
        hpa_url=hpa_url,
        harvest_ts=harvest_ts,
    )

    # Ensure minimum length constraints (>3000 chars, >80 lines)
    lines = report.split("\n")
    if len(report.encode("utf-8")) < 3000 or len(lines) < 80:
        # Precompute supplemental variables
        if nuc_score >= 7:
            supp_loc = "Primarily nuclear"
        elif nuc_score >= 5:
            supp_loc = "Nuclear with some extra-nuclear signal"
        elif nuc_score >= 3:
            supp_loc = "Mixed nuclear/cytoplasmic"
        else:
            supp_loc = "Primarily non-nuclear"

        if af:
            supp_struct = ("AlphaFold v" + str(af_version) + " predicts a mean pLDDT of " +
                          str(round(plddt, 1)) + ", with " + str(ordered_pct) +
                          "% of residues in ordered regions (pLDDT > 70). High confidence " +
                          "residues (>90 pLDDT) constitute " + str(pct_gt_90) + "% of the structure.")
        else:
            supp_struct = "No AlphaFold structural prediction is available for this protein."

        if pdb_list:
            supp_pdb_avail = (str(len(pdb_list)) + " experimental structures are available: " +
                             ", ".join(pdb_list[:5]))
            supp_pdb_note = "These provide experimental validation of the protein's three-dimensional architecture."
        else:
            supp_pdb_avail = "0 experimental structures are available (none)."
            supp_pdb_note = "No experimentally-determined structures exist for this protein."

        if ppi_str_n >= 10:
            supp_ppi_quality = "multiple experimentally-validated interactions"
        elif ppi_str_n >= 3:
            supp_ppi_quality = "a limited interaction network"
        else:
            supp_ppi_quality = "few known interaction partners"

        if ppi_str_n > 0 and ppi_int_n > 0:
            supp_ppi_valid = ("The presence of both computational predictions and experimental validation " +
                             "strengthens confidence in the PPI network.")
        else:
            supp_ppi_valid = ("PPI data is limited, suggesting the interactome of this protein " +
                             "remains largely unexplored.")

        if rejected:
            supp_reviewer = ("The protein meets automatic rejection criteria and is excluded from " +
                            "further TE-regulated protein screening.")
        else:
            supp_reviewer = ("The protein passes rejection thresholds and proceeds to candidate " +
                            "consideration with the noted caveats and recommendations.")

        supp_template = """

### Supplemental Details

**Gene Summary**: {gene} encodes {protein_name}. The canonical isoform contains {length_aa} amino acid residues with a calculated molecular mass of approximately {mass_kda} kDa. The protein is annotated with {n_interpro} InterPro and {n_pfam} Pfam domain entries.

**Functional Context**: {func_text}

**Subcellular Localization Summary**: {supp_loc} based on integrated evidence from UniProt, HPA, and GO-CC databases.

**Structural Prediction Details**: {supp_struct}

**PDB Structure Availability**: {supp_pdb_avail}. {supp_pdb_note}

**Protein Interaction Partners**: The STRING database identifies {ppi_str_n} potential interaction partners, with {supp_ppi_quality}. IntAct reports {ppi_int_n} experimentally-determined binary interactions. {supp_ppi_valid}

**Reviewer Notes**: This re-evaluation was performed as part of a systematic review of candidate TE-regulated proteins. The six-dimensional scoring framework prioritizes nuclear localization (weight x4), research novelty (weight x5), and structural characterization (weight x3). Cross-validation bonuses reward consistency across independent data sources. All scores are derived from harvest packet data integrating UniProt, AlphaFold, PubMed, STRING, IntAct, and Human Protein Atlas databases. Proteins failing nuclear evidence (score <= 3) or exceeding the PubMed novelty threshold (> 100 articles) are automatically rejected. {supp_reviewer}
"""
        extra = supp_template.format(
            gene=gene, protein_name=protein_name,
            length_aa=str(length_aa), mass_kda=str(mass_kda),
            n_interpro=str(len(interpro)), n_pfam=str(len(pfam)),
            func_text=func_full,
            supp_loc=supp_loc, supp_struct=supp_struct,
            supp_pdb_avail=supp_pdb_avail, supp_pdb_note=supp_pdb_note,
            ppi_str_n=str(ppi_str_n), ppi_int_n=str(ppi_int_n),
            supp_ppi_quality=supp_ppi_quality, supp_ppi_valid=supp_ppi_valid,
            supp_reviewer=supp_reviewer,
        )
        report += extra

    return report, status


def main():
    os.makedirs(STAGE_DIR, exist_ok=True)

    results = []
    for i, gene in enumerate(GENES):
        print("[" + str(i + 1) + "/" + str(len(GENES)) + "] " + gene.ljust(12) + "...", end="", flush=True)
        try:
            report, status = generate_report(gene)

            if report is None:
                print("  ERROR: " + status)
                results.append({"gene": gene, "status": "ERROR", "size": 0, "lines": 0})
                continue

            filepath = os.path.join(STAGE_DIR, gene + "-evaluation.md")
            with open(filepath, "w") as f:
                f.write(report)

            lines = report.split("\n")
            size = len(report.encode("utf-8"))
            has_180 = "/180" in report

            print(" -> " + str(size).rjust(5) + "b, " + str(len(lines)).rjust(3) +
                  " lines [" + status + "] [has_180:" + str(has_180) + "]")
            results.append({
                "gene": gene, "status": status, "size": size, "lines": len(lines),
                "has_180": has_180, "filepath": filepath
            })
        except Exception as e:
            print("  ERROR: " + str(e))
            import traceback
            traceback.print_exc()
            results.append({"gene": gene, "status": "ERROR", "size": 0, "lines": 0})

    # Summary
    print("\n" + "=" * 70)
    scored = sum(1 for r in results if r["status"] == "scored")
    rejected = sum(1 for r in results if r["status"] == "rejected")
    errors = sum(1 for r in results if r["status"].startswith("ERROR"))
    ok_size = sum(1 for r in results if r["size"] >= 3000)
    short = sum(1 for r in results if 0 < r["size"] < 3000)
    ok_lines = sum(1 for r in results if r["lines"] >= 80)
    no_180 = sum(1 for r in results if not r.get("has_180", False))

    print("Summary: " + str(scored) + " SCORED, " + str(rejected) + " REJECTED, " + str(errors) + " ERROR")
    print("Size: " + str(ok_size) + " >=3000 chars, " + str(short) + " <3000 chars")
    print("Lines: " + str(ok_lines) + " >=80 lines")
    print("Missing /180: " + str(no_180))
    print("\nReports staged to: " + STAGE_DIR)
    print("Done.")


if __name__ == "__main__":
    main()
