#!/usr/bin/env python3
"""Move IF images from wrong dirs and fix report embed paths in-place."""

import os, sys

DETAIL = "/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail"

# Genes from gen_180_ready.py that had images in wrong location
BUG_AFFECTED = {
    "EIF3L": "nucleolus",
    "EME1": "nucleolus",
    "ESF1": "nucleolus",
    "EXOSC2": "nucleolus",
    "EXOSC3": "nucleolus",
    "EXOSC4": "nucleolus",
    "EXOSC5": "nucleolus",
    "EXOSC8": "nucleolus",
    "EXOSC9": "nucleolus",
    "EIF4H": "nuclear-body",
    "ELOA": "nuclear-body",
    "ENOPH1": "nuclear-body",
    "EPC1": "nuclear-body",
    "ERCC8": "nuclear-body",
    "ETAA1": "nuclear-body",
    "EXOC6B": "nuclear-body",
    "EXOSC1": "nuclear-body",
    "EXOSC7": "nuclear-body",
    "ELOF1": "chromatin",
    "EME2": "chromatin",
    "EXD2": "chromatin",
    "ENY2": "nuclear-envelope",
}

for gene, correct_dest in BUG_AFFECTED.items():
    wrong_dir = os.path.join(DETAIL, "nucleoplasm", gene, "IF_images")
    correct_dir = os.path.join(DETAIL, correct_dest, gene, "IF_images")

    # Move IF images
    if os.path.isdir(wrong_dir):
        os.makedirs(correct_dir, exist_ok=True)
        moved = 0
        for fname in os.listdir(wrong_dir):
            src = os.path.join(wrong_dir, fname)
            dst = os.path.join(correct_dir, fname)
            if not os.path.exists(dst):
                os.rename(src, dst)
                moved += 1
            else:
                os.remove(src)
        print(f"{gene}: moved {moved} IF images nucleoplasm -> {correct_dest}")
        try:
            os.rmdir(wrong_dir)
        except OSError:
            pass

    # Move PAE
    wrong_pae = os.path.join(DETAIL, "nucleoplasm", gene, f"{gene}-PAE.png")
    if os.path.exists(wrong_pae):
        correct_d = os.path.join(DETAIL, correct_dest, gene)
        os.makedirs(correct_d, exist_ok=True)
        dst = os.path.join(correct_d, f"{gene}-PAE.png")
        os.rename(wrong_pae, dst)
        print(f"{gene}: moved PAE nucleoplasm -> {correct_dest}")

    # Update report embed paths
    report_path = os.path.join(DETAIL, correct_dest, gene, f"{gene}-evaluation.md")
    if os.path.exists(report_path):
        with open(report_path) as f:
            content = f.read()
        old_pref = f"detail/nucleoplasm/{gene}"
        new_pref = f"detail/{correct_dest}/{gene}"
        if old_pref in content:
            content = content.replace(old_pref, new_pref)
            with open(report_path, "w") as f:
                f.write(content)
            print(f"{gene}: updated report embed paths")

    # Clean up empty nucleoplasm gene directory
    np_dir = os.path.join(DETAIL, "nucleoplasm", gene)
    if os.path.isdir(np_dir):
        for f in list(os.listdir(np_dir)):
            fp = os.path.join(np_dir, f)
            if os.path.isdir(fp):
                try: os.rmdir(fp)
                except OSError: pass
            else:
                os.remove(fp)
        try: os.rmdir(np_dir)
        except OSError: pass

print("\nFix complete.")
