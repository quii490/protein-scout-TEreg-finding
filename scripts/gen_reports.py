#!/usr/bin/env python3
"""Generate evaluation reports for all 34 C proteins from collected data."""
import json, os, glob
from datetime import date

BASE = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail"
TODAY = str(date.today())

# === DATA ===
# UniProt data (from batch_uniprot.py output)
UNIPROT = {}
for f in glob.glob("/tmp/prot_*.json"):
    with open(f) as fh:
        d = json.load(fh)
        UNIPROT[d["gene"]] = d

# AlphaFold data (from json files in detail dirs)
AF_DATA = {}
for root, dirs, files in os.walk(BASE):
    for f in files:
        if f.endswith("-af_data.json"):
            gene = os.path.basename(root)
            with open(os.path.join(root, f)) as fh:
                AF_DATA[gene] = json.load(fh)

# STRING data
STRING = {}
for f in glob.glob("/tmp/string_*.json"):
    gene = f.replace("/tmp/string_", "").replace(".json", "")
    with open(f) as fh:
        STRING[gene] = json.load(fh)

# IntAct data
INTACT = {}
for f in glob.glob("/tmp/intact_*.json"):
    gene = f.replace("/tmp/intact_", "").replace(".json", "")
    with open(f) as fh:
        INTACT[gene] = json.load(fh)

# User-provided PubMed counts
PUBMED = {
    "CCDC174": 2, "CSRNP3": 3, "CYB561A3": 4, "CCDC82": 4, "CSRNP2": 4,
    "CCDC85C": 6, "CPNE4": 8, "CARNMT1": 9, "CRAMP1": 9, "CABLES2": 9,
    "CWC15": 12, "CCDC86": 13, "CGRRF1": 15, "CREBL2": 15, "CENPP": 16,
    "COLGALT2": 17, "CAMTA2": 19, "CSTF1": 20, "COMMD10": 21, "CCDC92": 23,
    "CWC27": 26, "COMMD3": 29, "CEBPZ": 30, "CRIPT": 31, "CHML": 34,
    "CSTF3": 34, "CHMP7": 36, "CYREN": 36, "CRIP2": 37, "CSRNP1": 37,
    "C12orf43": 37, "CREB3L4": 38, "CBFA2T2": 39, "COG5": 39,
}

def nov_score(pubmed_count):
    if pubmed_count <= 20: return 10
    elif pubmed_count <= 50: return 8
    elif pubmed_count <= 100: return 6
    return "REJECT"

def classify_nuclear(gene, up):
    """Determine nuclear localization score."""
    subcell = up.get("subcell", [])
    go_cc = up.get("go_cc", [])
    subcell_lower = [s.lower() for s in subcell]
    go_cc_lower = [g.lower() for g in go_cc]

    nucleus_terms = ["nucleus", "nucleoplasm", "nucleolar", "nucleolus", "chromatin", "chromosome", "nuclear speck", "nuclear body"]
    cyto_terms = ["cytoplasm", "cytosol", "plasma membrane", "membrane", "extracellular", "synapse"]
    organelle = ["endoplasmic reticulum", "golgi", "mitochondrion", "lysosome", "endosome", "peroxisome"]

    has_nucleus = any(any(t in s for t in nucleus_terms) for s in subcell_lower + go_cc_lower)
    has_cyto = any(any(t in s for t in cyto_terms) for s in subcell_lower + go_cc_lower)
    has_organelle = any(any(t in s for t in organelle) for s in subcell_lower + go_cc_lower)

    # Special cases for rejected
    rejected_genes = {
        "CPNE4": "胞外泌体/质膜/突触，无非核相关定位",
        "CABLES2": "胞质定位，无核信号",
        "COLGALT2": "内质网腔体，分泌途径",
        "CRIPT": "胞质/突触/树突棘，无核定位",
        "CRIP2": "细胞皮层，无核定位",
        "COG5": "高尔基体/胞质，无核定位",
    }
    return rejected_genes.get(gene, None)

def calc_scores(gene, pubmed_count, up, af):
    """Calculate all scores for a protein."""
    # Nuclear location (simplified - need HPA for final)
    nuclen = len(up.get("subcell", []))
    # We'll set nuclear score based on UniProt data, HPA would refine
    nuc_score = 7  # default for nuclear proteins

    # Size score
    length = up.get("length", 0)
    if 200 <= length <= 800:
        size_score = 10
    elif 100 <= length < 200 or 800 < length <= 1200:
        size_score = 8
    elif 50 <= length < 100 or 1200 < length <= 2000:
        size_score = 5
    elif length < 50 or 2000 < length <= 3000:
        size_score = 2
    else:
        size_score = 0

    # Novelty score
    nov = nov_score(pubmed_count)
    if nov == "REJECT":
        return None

    # Structure score
    if af:
        avg_plddt = af.get("avg_plddt", 0)
        above70 = af.get("plddt_above70", 0)
        if avg_plddt > 80 and above70 > 80:
            struct_score = 8
        elif avg_plddt > 70 and above70 > 60:
            struct_score = 8
        elif avg_plddt >= 65 and above70 > 40:
            struct_score = 7
        else:
            struct_score = 6  # baseline for novel proteins
    else:
        struct_score = 6  # baseline

    # Domain score - baseline for novel proteins
    dom_score = 7

    # PPI score - baseline
    ppi_score = 4

    return {
        "nuc": nuc_score, "size": size_score, "nov": nov,
        "struct": struct_score, "dom": dom_score, "ppi": ppi_score
    }

# === Build all reports ===
for gene in sorted(UNIPROT.keys()):
    up = UNIPROT[gene]
    af = AF_DATA.get(gene, {})
    pm = PUBMED.get(gene, 0)
    st = STRING.get(gene, [])
    ia = INTACT.get(gene, [])

    # Determine category
    cat = "nucleoplasm"  # default
    for c in ["nucleoplasm", "nucleolus", "chromatin", "nucleus-cytoplasm", "nuclear-envelope", "rejected", "nuclear-speckle"]:
        if os.path.exists(os.path.join(BASE, c, gene)):
            cat = c
            break

    skip = False
    # rejected check
    rejected_reason = classify_nuclear(gene, up)
    if rejected_reason:
        skip = True

    # Not needed - let me just write each report individually below
    print(f"{gene}: cat={cat}, pm={pm}, len={up.get('length', 0)}")
