#!/usr/bin/env python3
"""Rebuild ALL figures as true-editable SVG for Illustrator — plus PDF fallback.
Pure SVG: text stays as <text>, shapes as <path>/<rect>, no raster."""
from __future__ import annotations

import re, json, textwrap
from dataclasses import dataclass, field
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("SVG")  # <-- critical: SVG backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap, to_hex
import matplotlib.cm as cm
import matplotlib.ticker as mticker

ROOT = Path(__file__).resolve().parents[2]
SUMMARY = ROOT / "protein-finding.md"
CENTRO_JSON = ROOT / "centrosome" / "data" / "centrosome_report_index.json"
OUT = ROOT / "docs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# ── Palette ───────────────────────────────────────────────────
P = {
    "bg": "#FFFFFF", "fg": "#111111", "muted": "#6B7280",
    "accent": "#2563EB", "accent_dk": "#1E3A5F",
    "gold": "#B8860B", "red": "#C0392B", "green": "#1B7A3D",
    "orange": "#E67E22",
    "blue_lt": "#D6E4F0", "grey_lt": "#F3F4F6", "grey_md": "#D1D5DB",
}
CAT_COLOR = {
    "chromatin": "#DC2626", "nucleolus": "#2563EB",
    "nuclear-speckle": "#16A34A", "nucleus-cytoplasm": "#9333EA",
    "nucleoplasm": "#EA580C", "nuclear-envelope": "#A16207",
    "nuclear-body": "#DB2777",
}
CAT_LABEL = {
    "chromatin": "Chromatin", "nucleolus": "Nucleolus",
    "nuclear-speckle": "Nuclear speckle", "nucleus-cytoplasm": "Nucleus-cytoplasm",
    "nucleoplasm": "Nucleoplasm", "nuclear-envelope": "Nuclear envelope",
    "nuclear-body": "Nuclear body",
}
CAT_ORDER = list(CAT_LABEL.keys())

CANDIDATES_MAIN = {
    "AKAP8L", "PM20D2", "TBRG1", "EEF1AKMT3", "EEF1AKMT4",
    "DGCR6L", "C2orf42", "TEX52", "SPANXC", "SPANXA2",
    "RIPOR3", "FAM228A", "PRAC2", "FAM78A", "C17orf50",
    "C2orf78", "C5orf24", "FAM181A", "FAM227A", "FAM227B",
    "FAM214A", "C11orf71", "KIAA1614",
}
CANDIDATES_CENTRO = {"C11orf80", "C1orf146", "C20orf96", "FAM117B"}
CANDIDATE_NOTES = {
    "AKAP8L": "Nuclear speckles; rRNA-related; zinc finger",
    "PM20D2": "Nuclear dipeptidase; chromatin substrates",
    "TBRG1": "411 aa; FY-rich domain; INO80 interaction",
    "EEF1AKMT3": "Elongation factor methylation",
    "EEF1AKMT4": "Elongation factor methylation family",
    "DGCR6L": "Strong PPI network",
    "C2orf42": "Zinc finger; AGO2 interaction",
    "TEX52": "300 aa; aromatic-rich N-term; testis",
    "SPANXC": "SPANX family; sperm-specific; LaminA/C",
    "SPANXA2": "SPANX family; sperm-specific; LaminA/C",
    "RIPOR3": "RHO GTPase pathway",
    "FAM228A": "201 aa; SPANXN3 interaction",
    "PRAC2": "90 aa; Tudor domain-related",
    "FAM78A": "283 aa; nucleoplasm uncertain",
    "C17orf50": "174 aa",
    "C2orf78": "922 aa; nucleoplasm; HNRNP; testis",
    "C5orf24": "188 aa; STK11; homeobox binding",
    "FAM181A": "TEAD4 complex; TF binding",
    "FAM227A": "Zinc finger; Atos domain",
    "FAM227B": "Zinc finger; Atos domain",
    "FAM214A": "ATOS family",
    "C11orf71": "121 aa; unknown domain",
    "KIAA1614": "1190 aa; MLL/PAPOLA; nuclear lamina",
    "C11orf80": "TOP6BL; SPO11 complex; topoisomerase",
    "C1orf146": "SPO16 homolog; MSH4/5; SPO11 interactor",
    "C20orf96": "SHLD family; dsDNA break repair",
    "FAM117B": "589 aa; centrosome-related",
}

matplotlib.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial"],
    "font.size": 7,
    "figure.dpi": 150,
    "savefig.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
    "svg.fonttype": "none",            # <-- Key: embed text as <text> not paths
    "svg.image_inline": False,
    "axes.linewidth": 0.6,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "pdf.fonttype": 42,
})

# ── Utility: save both SVG and PDF ────────────────────────────
def save(fig, stem: str):
    svg_path = OUT / f"{stem}.svg"
    pdf_path = OUT / f"{stem}.pdf"
    fig.savefig(svg_path, format="svg", facecolor=P["bg"], edgecolor="none",
                bbox_inches="tight", pad_inches=0.1)
    fig.savefig(pdf_path, format="pdf", facecolor=P["bg"], edgecolor="none",
                dpi=150, bbox_inches="tight", pad_inches=0.1)
    kb = svg_path.stat().st_size / 1024
    print(f"  {stem}.svg ({kb:.0f}KB)  +  .pdf")
    return svg_path


# ═══════════════════════════════════════════════════════════════
# PARSE
# ═══════════════════════════════════════════════════════════════

def parse_main():
    text = SUMMARY.read_text(encoding="utf-8")
    scored = []
    secs = {c: m.start() for c in CAT_ORDER if (m := re.search(rf"\n## {c}\n", text))}
    em = re.search(r"\n## 已淘汰\n", text)
    em_end = em.start() if em else len(text)
    ordered = sorted(secs.items(), key=lambda x: x[1])
    for i, (cat, s) in enumerate(ordered):
        e = ordered[i+1][1] if i+1 < len(ordered) else em_end
        for ln in text[s:e].splitlines():
            ln = ln.strip()
            if not ln.startswith("| ") or "---" in ln or "基因" in ln: continue
            cs = [c.strip() for c in ln.strip("|").split("|")]
            if len(cs) < 11: continue
            try:
                scored.append({"gene": cs[1], "cat": cat,
                    "nuc": int(cs[2]), "size": int(cs[3]), "nov": int(cs[4]),
                    "struct": int(cs[5]), "dom": int(cs[6]), "ppi": int(cs[7]),
                    "cross": cs[8], "score": float(cs[9]), "stars": cs[10]})
            except (ValueError, IndexError): continue
    rejected = []
    if em:
        for ln in text[em_end:].splitlines():
            ln = ln.strip()
            if not ln.startswith("| ") or "---" in ln or "基因" in ln: continue
            cs = [c.strip() for c in ln.strip("|").split("|")]
            if len(cs) < 4: continue
            try: rejected.append({"gene": cs[1], "reason": cs[2], "pubmed": cs[3]})
            except (ValueError, IndexError): continue
    return scored, rejected

def parse_centrosome():
    if not CENTRO_JSON.exists(): return []
    data = json.loads(CENTRO_JSON.read_text())
    return [{"gene": r["gene"], "score": float(r["final_centrosome_score"])}
            for r in data.get("records", []) if r.get("final_centrosome_score")]


# ═══════════════════════════════════════════════════════════════
# FIGURE 1 — Screening Flow
# ═══════════════════════════════════════════════════════════════

def fig1(scored, rejected):
    nuc_r = sum(1 for r in rejected if "核定位" in r.get("reason",""))
    pub_r = sum(1 for r in rejected if "PubMed" in r.get("reason",""))
    fig, ax = plt.subplots(figsize=(5.0, 5.5))
    fig.patch.set_facecolor("white")
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")

    def box(x, y, w, h, top, bot, sub, color):
        r = mpatches.FancyBboxPatch((x-w/2, y), w, h, boxstyle="round,pad=0.06",
                                     facecolor=color, edgecolor="none", alpha=0.92)
        ax.add_patch(r)
        ax.text(x, y+h/2+0.22, top, ha="center", va="bottom", fontsize=7, fontweight="bold", color="white")
        ax.text(x, y+h/2-0.18, bot, ha="center", va="center", fontsize=9, fontweight="bold", color="white")
        if sub: ax.text(x, y+h/2-0.58, sub, ha="center", va="top", fontsize=5, color="white", alpha=0.85)

    def arrow(x, y1, y2, label=""):
        ax.annotate("", xy=(x, y2), xytext=(x, y1),
                    arrowprops=dict(arrowstyle="->", color=P["muted"], lw=1.0))
        if label: ax.text(x+0.3, (y1+y2)/2, label, ha="left", va="center",
                          fontsize=5.5, color=P["red"], fontstyle="italic", fontweight="bold")

    y = 0.8
    box(5, y, 5.0, 1.4, "Input", "4,756 genes", "Final_TE_finding.xlsx", P["accent_dk"])
    y1 = y+1.4
    y += 2.0; arrow(5, y1, y)
    box(5, y, 5.0, 1.2, "Evaluation reports", "5,647 reports", "86 duplicates across categories", P["accent"])
    y2 = y+1.2
    y += 1.85; arrow(5, y2, y, "Gate")
    gw = 2.6; gx_l, gx_r = 2.6, 7.4
    ax.annotate("", xy=(gx_r-gw/2, y+0.5), xytext=(3.5, y), arrowprops=dict(arrowstyle="->", color=P["grey_md"], lw=0.6))
    box(gx_l, y+0.5, gw, 0.8, "Nuclear score <= 3", f"{nuc_r:,} eliminated", None, P["red"])
    ax.text(gx_l, y+0.5+0.8+0.1, "Non-nuclear: mitochondrial,\nGolgi, ER, lysosomal, secreted",
            ha="center", va="top", fontsize=4.5, color=P["muted"])
    ax.annotate("", xy=(gx_r+gw/2, y+0.5), xytext=(6.5, y), arrowprops=dict(arrowstyle="->", color=P["grey_md"], lw=0.6))
    box(gx_r, y+0.5, gw, 0.8, "PubMed > 100", f"{pub_r:,} eliminated", None, P["orange"])
    ax.text(gx_r, y+0.5+0.8+0.1, "Heavily studied proteins\n(low research novelty)",
            ha="center", va="top", fontsize=4.5, color=P["muted"])
    y += 2.0; arrow(5, y+0.5+0.8, y)
    box(5, y, 5.0, 1.2, "Passed screening", f"{len(scored):,} proteins", "7 subcellular categories", P["green"])
    ax.text(5, 9.5, "Screening pipeline for TE-regulation\nnuclear protein candidates",
            ha="center", va="top", fontsize=9, fontweight="bold", color=P["fg"])
    save(fig, "fig1_screening_flow"); plt.close(fig)


# ═══════════════════════════════════════════════════════════════
# FIGURE 2 — Scoring System
# ═══════════════════════════════════════════════════════════════

def fig2():
    fig = plt.figure(figsize=(7.0, 2.5))
    fig.patch.set_facecolor("white")
    ax1 = fig.add_axes([0.06, 0.20, 0.38, 0.70])
    dims = ["Nuclear\nlocalization", "Protein\nsize", "Research\nnovelty",
            "3D\nstructure", "Regulatory\ndomains", "PPI\nnetwork", "Cross-\nvalidation"]
    weights = [4, 1, 5, 3, 2, 3, 0]
    bar_colors = [P["accent_dk"]] + [P["accent"]]*5 + [P["orange"]]
    bars = ax1.barh(range(7), weights, color=bar_colors, edgecolor="none", height=0.55)
    ax1.set_yticks(range(7)); ax1.set_yticklabels(dims, fontsize=5.5)
    ax1.set_xlabel("Weight multiplier", fontsize=6); ax1.set_xlim(0, 6.8); ax1.invert_yaxis()
    ax1.set_title("a  Dimension weights", fontsize=7.5, fontweight="bold", color=P["fg"], loc="left", pad=4)
    ax1.tick_params(axis="x", labelsize=5.5)
    for w, bar in zip(weights, bars):
        if w > 0: ax1.text(w+0.12, bar.get_y()+bar.get_height()/2, f"x{w}", va="center", fontsize=6.5, fontweight="bold", color=P["fg"])

    ax2 = fig.add_axes([0.52, 0.20, 0.44, 0.70]); ax2.axis("off"); ax2.set_xlim(0,10); ax2.set_ylim(0,10)
    ax2.set_title("b  Normalized score calculation", fontsize=7.5, fontweight="bold", color=P["fg"], loc="left", pad=4)
    rp = mpatches.FancyBboxPatch((0.2, 0.6), 9.6, 7.5, boxstyle="round,pad=0.25",
                                  facecolor=P["blue_lt"], edgecolor=P["accent"], lw=0.8, alpha=0.5)
    ax2.add_patch(rp)
    lines = [("Raw weighted sum", 8.2, 8.5, "bold"),
             ("  = (Nuc x 4) + (Size x 1) + (Novelty x 5)", 7.0, 7.0, "normal"),
             ("    + (Structure x 3) + (Domains x 2) + (PPI x 3)", 6.2, 7.0, "normal"),
             ("    + Cross-validation bonus", 5.4, 7.0, "normal"),
             ("", 4.5, 7.0, "normal"),
             ("Normalized score = Raw sum / 1.83", 3.6, 7.5, "bold"),
             ("", 2.85, 7.0, "normal"),
             ("Each dimension 0-10, cross-validation 0 to +3", 2.05, 6.5, "normal"),
             ("Theoretical maximum 183, normalized to 0-100", 1.4, 6.5, "normal")]
    for label, yp, sz, wt in lines:
        if label: ax2.text(5, yp, label, ha="center", va="center",
                           fontsize=sz, fontweight=wt if wt=="bold" else "normal",
                           color=P["accent_dk"] if wt=="bold" else P["fg"],
                           family="monospace" if "x" in label else "sans-serif")
    save(fig, "fig2_scoring_system"); plt.close(fig)


# ═══════════════════════════════════════════════════════════════
# FIGURE 3 — Distribution
# ═══════════════════════════════════════════════════════════════

def fig3(scored):
    all_scores = np.array([p["score"] for p in scored if p["score"] is not None])
    fig = plt.figure(figsize=(7.0, 4.0)); fig.patch.set_facecolor("white")
    ax1 = fig.add_axes([0.08, 0.56, 0.88, 0.38])
    ax1.hist(all_scores, bins=70, color=P["accent"], alpha=0.25, edgecolor="white", lw=0.2, zorder=1)
    hist, edges = np.histogram(all_scores, bins=120, density=True)
    centers = (edges[:-1]+edges[1:])/2
    smooth = np.convolve(hist, np.ones(9)/9, mode="same")
    scale = len(all_scores)*(edges[1]-edges[0])
    ax1_twin = ax1.twinx()
    ax1_twin.plot(centers, smooth*scale, color=P["accent_dk"], lw=1.2, zorder=2)
    ax1_twin.fill_between(centers, smooth*scale, alpha=0.08, color=P["accent_dk"], zorder=1)
    ax1_twin.set_ylabel("Density", fontsize=6, color=P["muted"], labelpad=2)
    ax1_twin.tick_params(axis="y", colors=P["muted"], labelsize=5.5)
    m = np.median(all_scores); q1, q3 = np.percentile(all_scores, 25), np.percentile(all_scores, 75)
    for val, ls, a in [(m,"--",0.7),(q1,":",0.4),(q3,":",0.4)]:
        ax1.axvline(val, color=P["red"], lw=0.8, ls=ls, alpha=a)
    ax1.text(m+0.5, ax1.get_ylim()[1]*0.94, f"Median = {m:.1f}", fontsize=6, color=P["red"], fontweight="bold")
    ax1.text(m+18, ax1.get_ylim()[1]*0.94, f"IQR: {q1:.1f} - {q3:.1f}", fontsize=5.5, color=P["muted"])
    ax1.set_xlabel("Normalized score", fontsize=6, labelpad=2)
    ax1.set_ylabel("Protein count", fontsize=6, labelpad=2)
    ax1.set_title(f"a  Score distribution across {len(scored):,} scored proteins",
                  fontsize=7.5, fontweight="bold", color=P["fg"], loc="left", pad=4)
    ax1.tick_params(labelsize=5.5)

    ax2 = fig.add_axes([0.08, 0.06, 0.88, 0.42])
    cat_scores, cat_names, cat_cols = [], [], []
    for cat in CAT_ORDER:
        s = [p["score"] for p in scored if p["cat"]==cat and p["score"] is not None]
        if s: cat_scores.append(s); cat_names.append(CAT_LABEL[cat]); cat_cols.append(CAT_COLOR[cat])
    bp = ax2.boxplot(cat_scores, vert=False, patch_artist=True,
                     medianprops=dict(color="white", lw=1.0),
                     flierprops=dict(marker=".", markersize=1.2, alpha=0.25, markeredgewidth=0),
                     whiskerprops=dict(lw=0.5, color=P["muted"]),
                     capprops=dict(lw=0.5, color=P["muted"]), widths=0.55)
    for patch, col in zip(bp["boxes"], cat_cols):
        patch.set_facecolor(col); patch.set_alpha(0.80); patch.set_edgecolor("none")
    ax2.set_yticklabels(cat_names, fontsize=6)
    ax2.set_xlabel("Normalized score", fontsize=6, labelpad=2)
    ax2.set_title("b  Score distribution by subcellular localization",
                  fontsize=7.5, fontweight="bold", color=P["fg"], loc="left", pad=4)
    ax2.tick_params(labelsize=5.5); ax2.grid(axis="x", alpha=0.2, lw=0.3)
    for i, s in enumerate(cat_scores):
        mu = np.mean(s)
        ax2.text(ax2.get_xlim()[1]-0.4, i+1, "x̄" + f"={mu:.1f}", va="center",
                 fontsize=5, color=P["muted"])
    save(fig, "fig3_distribution"); plt.close(fig)


# ═══════════════════════════════════════════════════════════════
# FIGURE 4 — Category Panels
# ═══════════════════════════════════════════════════════════════

def fig4(scored):
    fig = plt.figure(figsize=(7.0, 2.8)); fig.patch.set_facecolor("white")
    ax1 = fig.add_axes([0.06, 0.12, 0.38, 0.78])
    counts, labels, cols = [], [], []
    for cat in CAT_ORDER:
        c = sum(1 for p in scored if p["cat"]==cat)
        if c > 0: counts.append(c); labels.append(CAT_LABEL[cat]); cols.append(CAT_COLOR[cat])
    bars = ax1.barh(labels, counts, color=cols, edgecolor="none", height=0.55)
    ax1.invert_yaxis(); ax1.set_xlabel("Protein count", fontsize=6, labelpad=2)
    ax1.set_title(f"a  {len(scored):,} proteins by localization",
                  fontsize=7.5, fontweight="bold", color=P["fg"], loc="left", pad=4)
    ax1.tick_params(labelsize=5.5)
    for bar, count in zip(bars, counts):
        pct = count/len(scored)*100
        ax1.text(bar.get_width()+20, bar.get_y()+bar.get_height()/2,
                 f"{count:,}  ({pct:.0f}%)", va="center", fontsize=5.5, fontweight="bold", color=P["muted"])

    ax2 = fig.add_axes([0.55, 0.12, 0.42, 0.78], projection="polar")
    ax2.set_facecolor("white")
    dims = ["Nuclear\nlocalization", "Protein\nsize", "Research\nnovelty",
            "3D\nstructure", "Regulatory\ndomains", "PPI\nnetwork"]
    dim_keys = ["nuc","size","nov","struct","dom","ppi"]
    n_dims = len(dims)
    angles = np.linspace(0, 2*np.pi, n_dims, endpoint=False).tolist()+[0]
    ax2.set_theta_offset(np.pi/2); ax2.set_theta_direction(-1)
    for cat in CAT_ORDER:
        cps = [p for p in scored if p["cat"]==cat]
        meds = []
        for dk in dim_keys:
            vs = [p[dk] for p in cps if p[dk] is not None]
            meds.append(np.median(vs) if vs else 0)
        meds += meds[:1]
        ax2.fill(angles, meds, alpha=0.06, color=CAT_COLOR[cat], zorder=1)
        ax2.plot(angles, meds, "o-", lw=0.9, color=CAT_COLOR[cat], markersize=2.5, label=CAT_LABEL[cat], zorder=2)
    ax2.set_xticks(angles[:-1]); ax2.set_xticklabels(dims, fontsize=5.5, color=P["fg"])
    ax2.set_ylim(0,10); ax2.set_yticks([3,6,9]); ax2.set_yticklabels(["3","6","9"], fontsize=5, color=P["muted"])
    ax2.set_rlabel_position(30); ax2.grid(alpha=0.15, lw=0.3)
    ax2.legend(loc="upper right", bbox_to_anchor=(1.45, 1.05), fontsize=5, frameon=False, ncol=1, title="Category", title_fontsize=5.5)
    ax2.set_title("b  Median dimension scores", fontsize=7.5, fontweight="bold", color=P["fg"], loc="left", pad=14)
    save(fig, "fig4_category_panels"); plt.close(fig)


# ═══════════════════════════════════════════════════════════════
# FIGURE 5 — Scoring Table
# ═══════════════════════════════════════════════════════════════

def fig5():
    fig, ax = plt.subplots(figsize=(7.0, 2.8)); fig.patch.set_facecolor("white"); ax.axis("off")
    rows = [
        ("Nuclear localization", "x4", "UniProt subcellular location, HPA IF images, GO-CC\n(IDA/IMP evidence). Nucleus + chromatin specificity."),
        ("Protein size", "x1", "Amino acid length from UniProt. Optimal range\n300-800 aa scored highest (experimental tractability)."),
        ("Research novelty", "x5", "PubMed publication count. < 50 papers = high novelty.\nPrioritizes under-studied candidates."),
        ("3D structure", "x3", "AlphaFold pLDDT confidence, PDB entries,\ndomain-level structural quality assessment."),
        ("Regulatory domains", "x2", "InterPro / SMART / Pfam annotation. Chromatin-binding,\nDNA-binding, and enzymatic domains scored highest."),
        ("PPI network", "x3", "IntAct / STRING / BioGRID interaction data. Weighted\nby regulatory partner enrichment in chromatin/RNA."),
        ("Cross-validation", "bonus", "0 to +3 concordance bonus for multi-source agreement\nacross all databases (UniProt, HPA, GO, PDB)."),
    ]
    col_x = [0.04, 0.28, 0.38]; row_h = 0.28; header_y = 0.94
    ax.text(0.5, 1.0, "Scoring dimensions: definitions and data sources",
            ha="center", va="bottom", fontsize=9, fontweight="bold", color=P["fg"])
    for x, label in zip(col_x, ["Dimension", "Weight", "Description & data sources"]):
        ax.text(x, header_y, label, ha="left", va="center", fontsize=6.5, fontweight="bold", color="white",
                bbox=dict(facecolor=P["accent_dk"], edgecolor="none", boxstyle="round,pad=0.1"))
    for i, (dim, weight, desc) in enumerate(rows):
        y = header_y-(i+1)*row_h
        bg = P["grey_lt"] if i%2==0 else "white"
        ax.axhspan(y-row_h/2, y+row_h/2, facecolor=bg, edgecolor="none", alpha=0.6, zorder=0)
        ax.text(col_x[0]+0.01, y, dim, ha="left", va="center", fontsize=6.5, fontweight="bold", color=P["fg"])
        ax.text(col_x[1]+0.01, y, weight, ha="left", va="center", fontsize=7.5, fontweight="bold",
                color=P["accent_dk"] if weight!="bonus" else P["orange"])
        ax.text(col_x[2]+0.01, y, desc, ha="left", va="center", fontsize=5.5, color=P["muted"], linespacing=1.3)
    save(fig, "fig5_scoring_table"); plt.close(fig)


# ═══════════════════════════════════════════════════════════════
# FIGURE 6 — Star Key
# ═══════════════════════════════════════════════════════════════

def fig6():
    fig, ax = plt.subplots(figsize=(3.8, 1.8)); fig.patch.set_facecolor("white"); ax.axis("off")
    ax.set_xlim(0,10); ax.set_ylim(0,10)
    rows = [("85-100", "5 stars", "Exceptional: top priority for experimental validation"),
            ("75-84", "4 stars", "Strong: well-supported across most dimensions"),
            ("65-74", "3 stars", "Good: solid scores, some dimension gaps"),
            ("55-64", "2 stars", "Moderate: merits further investigation"),
            ("< 55", "1 star", "Baseline: review before prioritization")]
    for i, (rng, stars, desc) in enumerate(rows):
        y = 8.5-i*1.4; bg = P["grey_lt"] if i%2==0 else "white"
        ax.axhspan(y-0.55, y+0.55, facecolor=bg, edgecolor="none", alpha=0.5, zorder=0)
        ax.text(1.0, y, rng, ha="left", va="center", fontsize=7.5, fontweight="bold", color=P["fg"])
        ax.text(2.8, y, stars, ha="center", va="center", fontsize=11, color=P["accent"] if i<2 else P["muted"])
        ax.text(5.2, y, desc, ha="left", va="center", fontsize=6.5, color=P["muted"])
    ax.text(5, 9.7, "Candidate prioritization: star rating key",
            ha="center", va="bottom", fontsize=8, fontweight="bold", color=P["fg"])
    save(fig, "fig6_star_rating"); plt.close(fig)


# ═══════════════════════════════════════════════════════════════
# FIGURE B — Candidate Heatmap
# ═══════════════════════════════════════════════════════════════

DIM_KEYS_B = ["nuc","size","nov","struct","dom","ppi"]
DIM_LABELS_B = ["Nuclear\nlocalization", "Protein\nsize", "Research\nnovelty",
                "3D\nstructure", "Regulatory\ndomains", "PPI\nnetwork"]

def figB(scored):
    candidates = sorted(
        [p for p in scored if p["gene"] in CANDIDATES_MAIN],
        key=lambda p: p["score"], reverse=True)
    genes = [c["gene"] for c in candidates]
    n_genes = len(genes)
    data = np.array([[c.get(dk, 0) for dk in DIM_KEYS_B] for c in candidates])
    n_dims = len(DIM_KEYS_B)

    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    fig.patch.set_facecolor("white")

    cmap = LinearSegmentedColormap.from_list("b", ["#F5F5F5","#DEEBF7","#9ECAE1","#4292C6","#2171B5","#084594"])
    im = ax.pcolormesh(data, cmap=cmap, vmin=0, vmax=10, edgecolors="white",
                       linewidth=2, shading="flat", rasterized=False, snap=True)

    ax.set_xticks(np.arange(n_dims)+0.5)
    ax.set_xticklabels(DIM_LABELS_B, fontsize=7, ha="center")
    ax.set_yticks(np.arange(n_genes)+0.5)
    ax.set_yticklabels(genes, fontsize=7, fontweight="bold")
    ax.tick_params(top=False, right=False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for i in range(n_genes):
        for j in range(n_dims):
            val = data[i, j]
            tc = "white" if val >= 8 else ("#222222" if val >= 4 else P["muted"])
            ax.text(j+0.5, i+0.5, f"{int(val)}", ha="center", va="center",
                    fontsize=7.5, fontweight="bold", color=tc)

    # Category color strip + score on right
    for i, cp in enumerate(candidates):
        color = CAT_COLOR.get(cp["cat"], P["grey_md"])
        ax.add_patch(mpatches.Rectangle((n_dims+0.3, i+0.1), 0.6, 0.8,
                     facecolor=color, edgecolor="none", alpha=0.7, clip_on=False, zorder=5))
        ax.text(n_dims+0.65, i+0.5, f"{cp['score']:.1f}", ha="left", va="center",
                fontsize=7, fontweight="bold", color=P["fg"], clip_on=False)

    cbar = fig.colorbar(im, ax=ax, fraction=0.02, pad=0.02)
    cbar.set_label("Score (0-10)", fontsize=7, color=P["muted"])
    cbar.ax.tick_params(labelsize=6)
    cbar.solids.set_rasterized(False); cbar.solids.set_snap(True)

    ax.set_title("Candidate Protein Dimension Scores (0-10)",
                 fontsize=10, fontweight="bold", color=P["fg"], pad=8)
    ax.text(n_dims+0.65, -0.6, "Total", ha="left", va="top", fontsize=6.5, color=P["muted"],
            fontstyle="italic", clip_on=False)

    save(fig, "figB_candidate_heatmap"); plt.close(fig)


# ═══════════════════════════════════════════════════════════════
# FIGURE C — Stacked Contribution
# ═══════════════════════════════════════════════════════════════

DIM_WEIGHTS = [4, 1, 5, 3, 2, 3]

def figC(scored):
    candidates = sorted(
        [p for p in scored if p["gene"] in CANDIDATES_MAIN],
        key=lambda p: p["score"], reverse=True)
    top_n = min(18, len(candidates))
    top = candidates[:top_n]
    genes = [c["gene"] for c in top]

    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    fig.patch.set_facecolor("white")

    dim_colors = ["#DC2626","#F59E0B","#10B981","#6366F1","#EC4899","#0891B2"]
    dim_alphas = [1.0, 0.6, 1.0, 0.85, 0.7, 0.85]
    DIM_LEGEND = ["Nuclear loc. (x4)","Protein size (x1)","Research novelty (x5)",
                  "3D structure (x3)","Reg. domains (x2)","PPI network (x3)"]

    n_genes = len(genes)
    for i, cp in enumerate(reversed(top)):
        left = 0
        for j, dk in enumerate(DIM_KEYS_B):
            raw = cp.get(dk, 0)
            weighted = raw * DIM_WEIGHTS[j] / 1.83
            ax.barh(n_genes-1-i, weighted, left=left, color=dim_colors[j],
                    alpha=dim_alphas[j], edgecolor="white", lw=0.3, height=0.65)
            left += weighted

    ax.set_yticks(range(n_genes))
    ax.set_yticklabels(reversed(genes), fontsize=7.5, fontweight="bold")
    ax.set_xlabel("Weighted score contribution", fontsize=8, color=P["muted"])
    ax.set_title("Top Candidate Protein Score Composition",
                 fontsize=10, fontweight="bold", color=P["fg"], pad=8)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    # Score labels
    for i, cp in enumerate(reversed(top)):
        sc = cp["score"]
        ax.scatter([sc*1.02 if sc else 0], [n_genes-1-i],
                   s=60, color=CAT_COLOR.get(cp["cat"], P["grey_md"]),
                   edgecolors="white", linewidth=1, zorder=10, clip_on=False)
        ax.text(sc*1.02+1.2, n_genes-1-i, f"{sc:.1f}",
                fontsize=6.5, fontweight="bold", color=P["muted"], va="center", clip_on=False)

    patches = [mpatches.Patch(color=dim_colors[j], alpha=dim_alphas[j], label=DIM_LEGEND[j])
               for j in range(6)]
    ax.legend(handles=patches, loc="lower right", fontsize=6, ncol=2,
              frameon=True, facecolor="white", edgecolor=P["grey_md"], framealpha=0.85)

    save(fig, "figC_score_breakdown"); plt.close(fig)


# ═══════════════════════════════════════════════════════════════
# FIGURE D — Screening Atlas (main + centro)
# ═══════════════════════════════════════════════════════════════

def figD(scored, centro):
    scored_s = sorted(scored, key=lambda p: p["score"] or 0, reverse=True)
    scores = np.array([p["score"] for p in scored_s])
    s_min, s_max = scores.min(), scores.max()

    w, h_img = 16.0, 9.0
    fig = plt.figure(figsize=(w, h_img), facecolor=P["bg"])
    fig.text(0.04, 0.98, "Protein Scout  ·  Screening Atlas with Manually Selected Candidates",
             fontsize=13, fontweight="bold", color=P["fg"], ha="left", va="top")
    fig.text(0.04, 0.95,
             f"{len(scored_s):,} scored across 7 categories  |  {len(CANDIDATES_MAIN)} main + {len(CANDIDATES_CENTRO)} centro candidates",
             fontsize=8.5, color=P["muted"], ha="left", va="top")

    # ── Left: density strips ──
    ax = fig.add_axes([0.04, 0.05, 0.54, 0.87])
    ax.set_facecolor("#FAFBFC")

    cat_data = {}
    for cat in CAT_ORDER:
        ss = np.array([p["score"] for p in scored_s if p["cat"]==cat])
        if len(ss): cat_data[cat] = ss
    cat_order_disp = sorted(cat_data, key=lambda c: np.median(cat_data[c]), reverse=True)

    y_positions = []
    for ci, cat in enumerate(cat_order_disp):
        ss = cat_data[cat]
        bins = np.linspace(s_min, s_max, 120)
        hist, edges = np.histogram(ss, bins=bins, density=True)
        centers = (edges[:-1]+edges[1:])/2
        smooth_h = np.convolve(hist, np.ones(7)/7, mode="same")
        max_h = smooth_h.max()
        if max_h > 0: smooth_h = smooth_h / max_h * 0.38

        for j in range(len(centers)-1):
            ax.add_patch(mpatches.Rectangle(
                (centers[j], ci-smooth_h[j]/2), centers[j+1]-centers[j], smooth_h[j],
                facecolor=CAT_COLOR[cat], edgecolor="none", alpha=0.82, zorder=2))
        ax.text(s_min-1.5, ci, CAT_LABEL[cat], ha="right", va="center",
                fontsize=7.5, fontweight="bold", color=CAT_COLOR[cat])
        ax.text(s_max+1, ci, f"n={len(ss):,}", ha="left", va="center",
                fontsize=6.5, color=P["muted"])

        for cp in [p for p in scored_s if p["cat"]==cat and p["gene"] in CANDIDATES_MAIN]:
            sc = cp["score"]
            ax.plot([sc, sc], [ci-0.32, ci+0.32], color=P["gold"], lw=1.5, zorder=10, solid_capstyle="round")
            ax.scatter([sc], [ci], s=35, color=P["gold"], edgecolors="white", linewidth=0.8, zorder=11)
            ax.text(sc, ci+0.45, cp["gene"], fontsize=5.5, fontweight="bold", color=P["gold"],
                    ha="center", va="bottom", rotation=60, zorder=12)
        y_positions.append(ci)

    # Centrosome strip
    if centro:
        cs_arr = np.array([c["score"] for c in centro])
        cs_min, cs_max = cs_arr.min(), cs_arr.max()
        yc = len(cat_order_disp)
        bins_c = np.linspace(cs_min, cs_max, 60)
        hist_c, edges_c = np.histogram(cs_arr, bins=bins_c, density=True)
        centers_c = (edges_c[:-1]+edges_c[1:])/2
        smooth_c = np.convolve(hist_c, np.ones(5)/5, mode="same")
        max_h_c = smooth_c.max()
        if max_h_c > 0: smooth_c = smooth_c / max_h_c * 0.38
        for j in range(len(centers_c)-1):
            ax.add_patch(mpatches.Rectangle(
                (centers_c[j], yc-smooth_c[j]/2), centers_c[j+1]-centers_c[j], smooth_c[j],
                facecolor="#0891B2", edgecolor="none", alpha=0.70, zorder=2))
        ax.text(s_min-1.5, yc, "Centrosome", ha="right", va="center",
                fontsize=7, fontweight="bold", color="#0891B2", fontstyle="italic")
        ax.text(s_max+1, yc, f"n={len(centro):,}", ha="left", va="center", fontsize=5.8, color=P["muted"])
        for cg in CANDIDATES_CENTRO:
            for h in [c for c in centro if c["gene"]==cg]:
                sc = h["score"]
                ax.plot([sc, sc], [yc-0.28, yc+0.28], color=P["gold"], lw=1.3, zorder=10)
                ax.scatter([sc], [yc], s=28, color=P["gold"], edgecolors="white", linewidth=0.7, zorder=11)
                ax.text(sc, yc+0.42, cg, fontsize=5, fontweight="bold", color=P["gold"],
                        ha="center", va="bottom", rotation=55, zorder=12)
        y_positions.append(yc)
        y_max = yc+0.3
    else:
        y_max = len(cat_order_disp)-0.2

    ax.set_yticks(y_positions); ax.set_yticklabels([])
    ax.set_xlabel("Normalized score", fontsize=8, color=P["muted"], labelpad=6)
    ax.set_xlim(s_min-7, s_max+5); ax.set_ylim(-0.8, y_max)
    for sp in ["left","top","right"]: ax.spines[sp].set_visible(False)
    ax.tick_params(axis="x", labelsize=7, colors=P["muted"])
    ax.tick_params(axis="y", left=False, labelleft=False); ax.grid(axis="x", alpha=0.15, lw=0.4)

    leg = [mpatches.Patch(color=P["gold"], label="Manually selected candidate")]
    if centro: leg.append(mpatches.Patch(color="#0891B2", alpha=0.7, label="Centrosome module"))
    ax.legend(handles=leg, loc="lower right", fontsize=6.5,
              frameon=True, facecolor="white", edgecolor=P["grey_md"], framealpha=0.9)

    # ── Right: detail panels ──
    ax2 = fig.add_axes([0.61, 0.05, 0.36, 0.90])
    ax2.set_xlim(0,10); ax2.set_ylim(0,10); ax2.axis("off")
    ax2.add_patch(mpatches.FancyBboxPatch((0,0), 10,10, boxstyle="round,pad=0.15",
                  facecolor="#F8F9FB", edgecolor=P["grey_md"], lw=0.6, zorder=0))
    ax2.text(0.4, 9.65, "Selected Candidates", fontsize=11, fontweight="bold", color=P["fg"], ha="left", va="top")
    ax2.text(0.4, 9.30, f"{len(CANDIDATES_MAIN)} main + {len(CANDIDATES_CENTRO)} centrosome",
             fontsize=7.5, color=P["muted"], ha="left", va="top")

    main_list = sorted([p for p in scored_s if p["gene"] in CANDIDATES_MAIN],
                       key=lambda p: p["score"], reverse=True)

    y = 8.80; dy = 0.35
    def add_row(rank, gene, score, tag, tag_color, note, y_pos):
        if y_pos < 0.3: return y_pos
        if rank%2==1:
            ax2.add_patch(mpatches.Rectangle((0.05, y_pos-dy*0.4), 9.9, dy*0.86,
                          facecolor="white", edgecolor="none", alpha=0.55, zorder=1))
        ax2.text(0.35, y_pos, str(rank), fontsize=7.5, fontweight="bold",
                 color=P["grey_md"], ha="right", va="center", zorder=5)
        ax2.scatter([0.55], [y_pos], s=12, color=P["gold"], edgecolors="white", linewidth=0.5, zorder=10)
        ax2.text(0.75, y_pos, gene, fontsize=8, fontweight="bold", color=P["fg"], ha="left", va="center", zorder=5)
        sc_str = f"{score:.1f}" if score is not None else "-"
        sc_clr = P["accent"] if (score or 0) >= 75 else P["muted"]
        ax2.text(2.85, y_pos, sc_str, fontsize=7.5, fontweight="bold", color=sc_clr, ha="left", va="center", zorder=5)
        tag_w = len(tag)*0.46+0.70
        ax2.add_patch(mpatches.FancyBboxPatch(
            (3.40, y_pos-0.09), tag_w, 0.18, boxstyle="round,pad=0.03",
            facecolor=tag_color, edgecolor="none", alpha=0.12, zorder=2))
        ax2.text(3.40+tag_w/2, y_pos, tag, fontsize=5.3, color=tag_color, ha="center", va="center", fontweight="bold", zorder=5)
        n_short = textwrap.shorten(note, width=48, placeholder=" ...")
        ax2.text(3.40+tag_w+0.35, y_pos, n_short, fontsize=5.8, color=P["muted"], ha="left", va="center", fontstyle="italic", zorder=5)
        return y_pos-dy

    for ci, cp in enumerate(main_list):
        y = add_row(ci+1, cp["gene"], cp["score"], CAT_LABEL.get(cp["cat"], cp["cat"]),
                     CAT_COLOR.get(cp["cat"], P["grey_md"]), CANDIDATE_NOTES.get(cp["gene"], ""), y)

    ax2.axhline(y+0.05, xmin=0.15, xmax=0.85, color=P["grey_md"], lw=0.5, alpha=0.4)
    ax2.text(0.4, y-0.08, "Centrosome Module", fontsize=7.5, fontweight="bold",
             color="#0891B2", ha="left", va="top", fontstyle="italic")
    y -= 0.28

    for ci, cg in enumerate(sorted(CANDIDATES_CENTRO, key=lambda g: next((c["score"] for c in centro if c["gene"]==g), 0), reverse=True)):
        hits = [c for c in centro if c["gene"]==cg]
        sc = hits[0]["score"] if hits else None
        note = CANDIDATE_NOTES.get(cg, "")
        rank = len(main_list)+ci+1
        y = add_row(rank, cg, sc, "centrosome", "#0891B2", note, y)

    ax2.text(5.0, 0.10, "Scores > 75 in blue  |  Centrosome: independent 0-100 scale",
             fontsize=5.5, color=P["grey_md"], ha="center", va="center", fontstyle="italic")

    save(fig, "screening_atlas_candidates"); plt.close(fig)


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    scored, rejected = parse_main()
    centro = parse_centrosome()
    nuc_r = sum(1 for r in rejected if "核定位" in r.get("reason",""))
    pub_r = sum(1 for r in rejected if "PubMed" in r.get("reason",""))
    print(f"Main: {len(scored):,} scored, {nuc_r}+{pub_r} rejected")
    print(f"Centrosome: {len(centro)} scored")
    print(f"Candidates: {len(CANDIDATES_MAIN)} main + {len(CANDIDATES_CENTRO)} centro")
    print(f"Output: {OUT}/")
    print()

    fig1(scored, rejected)
    fig2()
    fig3(scored)
    fig4(scored)
    fig5()
    fig6()
    figB(scored)
    figC(scored)
    figD(scored, centro)

    # List all outputs
    for f in sorted(OUT.glob("*.svg")):
        kb = f.stat().st_size / 1024
        print(f"  {f.name} ({kb:.0f}KB)")


if __name__ == "__main__":
    main()
