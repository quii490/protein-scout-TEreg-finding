#!/usr/bin/env python3
"""Create directories for all 34 C proteins based on current classification."""
import os

BASE = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail"

# Classification based on UniProt data analysis
CLASSIFICATION = {
    # Strong nuclear/nucleoplasm
    "CCDC174": "nucleoplasm",
    "CSRNP3": "nucleoplasm",
    "CSRNP2": "nucleoplasm",
    "CWC15": "nucleoplasm",
    "CCDC86": "nucleoplasm",
    "CGRRF1": "nucleoplasm",
    "CREBL2": "nucleoplasm",
    "CENPP": "nucleoplasm",
    "CAMTA2": "nucleoplasm",
    "CSTF1": "nucleoplasm",
    "CWC27": "nucleoplasm",
    "CEBPZ": "nucleoplasm",
    "CSTF3": "nucleoplasm",
    "CSRNP1": "nucleoplasm",
    "CBFA2T2": "nucleoplasm",
    "CCDC82": "nucleoplasm",
    # Nucleus-cytoplasm
    "CARNMT1": "nucleus-cytoplasm",
    "COMMD10": "nucleus-cytoplasm",
    "COMMD3": "nucleus-cytoplasm",
    "CYREN": "nucleus-cytoplasm",
    # Nuclear envelope
    "C12orf43": "nuclear-envelope",
    "CHMP7": "nuclear-envelope",
    # Chromatin-related
    "CRAMP1": "chromatin",
    "CREB3L4": "chromatin",
    # Nucleolus-related
    "CYB561A3": "nucleoplasm",  # GO has nucleolus but mainly lysosome
    # Weak nuclear - needs closer look
    "CCDC85C": "nucleoplasm",  # GO: nuclear speck
    "CCDC92": "nucleoplasm",   # GO: nucleoplasm
    "CHML": "nucleoplasm",     # GO: nucleoplasm/nucleus
    # Rejected (not nuclear)
    "CPNE4": "rejected",
    "CABLES2": "rejected",
    "COLGALT2": "rejected",
    "CRIPT": "rejected",
    "CRIP2": "rejected",
    "COG5": "rejected",
}

for gene, cat in CLASSIFICATION.items():
    d = os.path.join(BASE, cat, gene)
    os.makedirs(d, exist_ok=True)
    if_dir = os.path.join(d, "IF_images")
    os.makedirs(if_dir, exist_ok=True)
    print(f"Created: {cat}/{gene}")
print(f"\nDone: {len(CLASSIFICATION)} directories")
