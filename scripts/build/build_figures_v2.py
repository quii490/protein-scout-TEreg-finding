#!/usr/bin/env python3
"""Generate publication-grade figures for protein screening workflow.

Design philosophy: Nature / Cell / Science editorial style.
High data-ink ratio, restrained palette, typographic hierarchy, zero chartjunk.
Each figure is a standalone PDF, sized for journal column widths.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.font_manager import FontProperties

# ── Paths ──────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]
SUMMARY = ROOT / "protein-finding.md"
OUT_DIR = ROOT / "docs" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Journal-grade colour palette ───────────────────────────────
# Based on Paul Tol's muted qualitative scheme + sequential blues
C = {
    "bg":        "#FFFFFF",
    "fg":        "#222222",
    "muted":     "#666666",
    "accent":    "#4477AA",
    "accent_dk": "#225588",
    "red":       "#CC3311",
    "green":     "#228833",
    "orange":    "#EE7733",
    "blue_lt":   "#CCDDEE",
    "blue_md":   "#6699CC",
    "grey_lt":   "#EEEEEE",
    "grey_md":   "#BBBBBB",
    "grey_dk":   "#555555",

    # Category colours (Tol bright)
    "chromatin":          "#DD4444",
    "nucleolus":          "#4477AA",
    "nuclear-speckle":    "#44AA88",
    "nucleus-cytoplasm":  "#9955BB",
    "nucleoplasm":        "#EE8833",
    "nuclear-envelope":   "#AA7744",
    "nuclear-body":       "#EE6677",
}

CAT_ORDER = [
    "chromatin", "nucleolus", "nuclear-speckle",
    "nucleus-cytoplasm", "nucleoplasm", "nuclear-envelope", "nuclear-body",
]

CAT_LABEL = {
    "chromatin": "Chromatin",
    "nucleolus": "Nucleolus",
    "nuclear-speckle": "Nuclear speckle",
    "nucleus-cytoplasm": "Nucleus–cytoplasm",
    "nucleoplasm": "Nucleoplasm",
    "nuclear-envelope": "Nuclear envelope",
    "nuclear-body": "Nuclear body",
}

CAT_COLOR = {c: C[c] for c in CAT_ORDER}


# ── Matplotlib rc (journal defaults) ───────────────────────────
matplotlib.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 7,
    "axes.titlesize": 8.5,
    "axes.labelsize": 7.5,
    "xtick.labelsize": 6.5,
    "ytick.labelsize": 6.5,
    "legend.fontsize": 6.5,
    "legend.title_fontsize": 7,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.08,
    "pdf.fonttype": 42,
    "pdf.compression": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.5,
    "xtick.major.width": 0.4,
    "ytick.major.width": 0.4,
    "xtick.major.size": 2.5,
    "ytick.major.size": 2.5,
    "grid.alpha": 0.25,
    "grid.linewidth": 0.3,
    "lines.linewidth": 1.0,
    "lines.markersize": 3,
})


@dataclass
class Protein:
    gene: str = ""
    category: str = ""
    score: float | None = None
    nuc: int | None = None
    size: int | None = None
    nov: int | None = None
    struct: int | None = None
    dom: int | None = None
    ppi: int | None = None
    cross: str = ""
    stars: str = ""
    rejected_reason: str = ""
    pubmed: str = ""


def parse_data() -> tuple[list[Protein], list[Protein]]:
    text = SUMMARY.read_text(encoding="utf-8")
    scored_cats = CAT_ORDER
    scored: list[Protein] = []
    rejected: list[Protein] = []

    sections = {}
    for cat in scored_cats:
        m = re.search(rf"\n## {cat}\n", text)
        if m:
            sections[cat] = m.start()
    elim_m = re.search(r"\n## 已淘汰\n", text)
    elim_start = elim_m.start() if elim_m else len(text)
    ordered = sorted(sections.items(), key=lambda x: x[1])

    for i, (cat, start) in enumerate(ordered):
        end = ordered[i + 1][1] if i + 1 < len(ordered) else elim_start
        for line in text[start:end].splitlines():
            line = line.strip()
            if not line.startswith("| ") or "---" in line or "基因" in line:
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 11:
                continue
            try:
                scored.append(Protein(
                    gene=cells[1], category=cat,
                    nuc=int(cells[2]), size=int(cells[3]),
                    nov=int(cells[4]), struct=int(cells[5]),
                    dom=int(cells[6]), ppi=int(cells[7]),
                    cross=cells[8], score=float(cells[9]),
                    stars=cells[10],
                ))
            except (ValueError, IndexError):
                continue

    if elim_m:
        for line in text[elim_start:].splitlines():
            line = line.strip()
            if not line.startswith("| ") or "---" in line or "基因" in line:
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 4:
                continue
            try:
                rejected.append(Protein(
                    gene=cells[1], category="rejected",
                    rejected_reason=cells[2], pubmed=cells[3],
                ))
            except (ValueError, IndexError):
                continue

    return scored, rejected


# ═══════════════════════════════════════════════════════════════
# FIGURE 1 — Screening pipeline schematic
# ═══════════════════════════════════════════════════════════════

def fig1_screening_flow(scored, rejected) -> Path:
    """Horizontal flow diagram. Single-column width (88 mm)."""
    nuc_r = sum(1 for p in rejected if "核定位" in p.rejected_reason)
    pub_r = sum(1 for p in rejected if "PubMed" in p.rejected_reason)
    n_scored = len(scored)

    # Single-column width for journals
    fig, ax = plt.subplots(figsize=(3.46, 4.0))  # 88 mm wide
    fig.patch.set_facecolor("white")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    def box(x, y, w, h, label_top, label_bot, sub, color, alpha=1.0):
        rect = mpatches.FancyBboxPatch(
            (x - w / 2, y), w, h,
            boxstyle="round,pad=0.06",
            facecolor=color, edgecolor="none", alpha=alpha,
        )
        ax.add_patch(rect)
        ax.text(x, y + h / 2 + 0.22, label_top, ha="center", va="bottom",
                fontsize=6.5, fontweight="bold", color="white")
        ax.text(x, y + h / 2 - 0.18, label_bot, ha="center", va="center",
                fontsize=8.5, fontweight="bold", color="white")
        if sub:
            ax.text(x, y + h / 2 - 0.58, sub, ha="center", va="top",
                    fontsize=4.8, color="white", alpha=0.85)

    def arrow(x, y1, y2, label=""):
        ax.annotate("", xy=(x, y2), xytext=(x, y1),
                    arrowprops=dict(arrowstyle="->", color=C["grey_dk"], lw=0.9))
        if label:
            ax.text(x + 0.3, (y1 + y2) / 2, label, ha="left", va="center",
                    fontsize=5.5, color=C["red"], fontstyle="italic", fontweight="bold")

    y = 0.8

    # Step 1
    box(5, y, 4.8, 1.4, "Input", "4,756 genes",
        "Final_TE_finding.xlsx", C["accent_dk"])
    y1 = y + 1.4

    # Step 2
    y += 2.0
    arrow(5, y1, y)
    box(5, y, 4.8, 1.2, "Evaluation reports", "5,647 reports",
        "86 duplicates across categories", C["accent"])
    y2 = y + 1.2

    # Gates
    y += 1.85
    arrow(5, y2, y, "Gate")

    # Left gate: nuclear
    gw = 2.6
    gx_l, gx_r = 2.6, 7.4
    ax.annotate("", xy=(gx_r - gw / 2, y + 0.5), xytext=(3.5, y),
                arrowprops=dict(arrowstyle="->", color=C["grey_md"], lw=0.6))
    box(gx_l, y + 0.5, gw, 0.8, f"Nuclear score ≤ 3",
        f"{nuc_r:,} eliminated", None, C["red"])
    ax.text(gx_l, y + 0.5 + 0.8 + 0.1,
            "Non-nuclear: mitochondrial,\nGolgi, ER, lysosomal, secreted",
            ha="center", va="top", fontsize=4.5, color=C["muted"])

    # Right gate: PubMed
    ax.annotate("", xy=(gx_r + gw / 2, y + 0.5), xytext=(6.5, y),
                arrowprops=dict(arrowstyle="->", color=C["grey_md"], lw=0.6))
    box(gx_r, y + 0.5, gw, 0.8, f"PubMed > 100",
        f"{pub_r:,} eliminated", None, C["orange"])
    ax.text(gx_r, y + 0.5 + 0.8 + 0.1,
            "Heavily studied proteins\n(low research novelty)",
            ha="center", va="top", fontsize=4.5, color=C["muted"])

    # Step 4
    y += 2.0
    arrow(5, y + 0.5 + 0.8, y)
    box(5, y, 4.8, 1.2, "Passed screening",
        f"{n_scored:,} proteins", "Seven subcellular categories", C["green"])

    # Title
    ax.text(5, 9.5,
            "Screening pipeline for TE-regulation\nnuclear protein candidates",
            ha="center", va="top", fontsize=8, fontweight="bold",
            color=C["fg"])

    path = OUT_DIR / "fig1_screening_flow.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# FIGURE 2 — Scoring system (weights + formula)
# ═══════════════════════════════════════════════════════════════

def fig2_scoring_system() -> Path:
    """Double-column width (178 mm). Two panels."""
    fig = plt.figure(figsize=(7.0, 2.2))
    fig.patch.set_facecolor("white")

    # ── Left panel: bar chart ──
    ax1 = fig.add_axes([0.06, 0.22, 0.38, 0.70])

    dims = ["Nuclear\nlocalization", "Protein\nsize", "Research\nnovelty",
            "3D\nstructure", "Regulatory\ndomains", "PPI\nnetwork",
            "Cross-\nvalidation"]
    weights = [4, 1, 5, 3, 2, 3, 0]
    bar_colors = [C["accent_dk"]] + [C["accent"]] * 5 + [C["orange"]]

    bars = ax1.barh(range(7), weights, color=bar_colors, edgecolor="none",
                    height=0.55)
    ax1.set_yticks(range(7))
    ax1.set_yticklabels(dims, fontsize=5.5)
    ax1.set_xlabel("Weight multiplier", fontsize=6)
    ax1.set_xlim(0, 6.8)
    ax1.invert_yaxis()
    ax1.set_title("a  Dimension weights", fontsize=7.5, fontweight="bold",
                  color=C["fg"], loc="left", pad=4)
    ax1.tick_params(axis="x", labelsize=5.5)

    for w, bar in zip(weights, bars):
        if w > 0:
            ax1.text(w + 0.12, bar.get_y() + bar.get_height() / 2,
                     f"×{w}", va="center", fontsize=6.5,
                     fontweight="bold", color=C["fg"])

    # ── Right panel: formula ──
    ax2 = fig.add_axes([0.52, 0.22, 0.44, 0.70])
    ax2.axis("off")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_title("b  Normalized score calculation", fontsize=7.5,
                  fontweight="bold", color=C["fg"], loc="left", pad=4)

    # Formula box
    r = mpatches.FancyBboxPatch(
        (0.2, 0.6), 9.6, 7.5, boxstyle="round,pad=0.25",
        facecolor=C["blue_lt"], edgecolor=C["accent"], lw=0.8, alpha=0.5,
    )
    ax2.add_patch(r)

    formula_lines = [
        ("Raw weighted sum", 8.2, 8.5, "bold"),
        ("  = (Nuc × 4) + (Size × 1) + (Novelty × 5)", 7.0, 7.0, "normal"),
        ("    + (Structure × 3) + (Domains × 2) + (PPI × 3)", 6.2, 7.0, "normal"),
        ("    + Cross-validation bonus", 5.4, 7.0, "normal"),
        ("", 4.5, 7.0, "normal"),
        ("Normalized score = Raw sum / 1.83", 3.6, 7.5, "bold"),
        ("", 2.85, 7.0, "normal"),
        ("Each dimension 0-10, cross-validation 0 to +3", 2.05, 6.5, "normal"),
        ("Theoretical maximum 183, normalized to 0-100", 1.4, 6.5, "normal"),
    ]

    for label, y_pos, size, weight in formula_lines:
        if not label:
            continue
        ax2.text(5, y_pos, label, ha="center", va="center",
                 fontsize=size, fontweight=weight if weight == "bold" else "normal",
                 color=C["accent_dk"] if weight == "bold" else C["fg"],
                 family="monospace" if "×" in label else "sans-serif")

    path = OUT_DIR / "fig2_scoring_system.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# FIGURE 3 — Score distribution + category boxplots
# ═══════════════════════════════════════════════════════════════

def fig3_distribution(scored) -> Path:
    """Double-column width."""
    fig = plt.figure(figsize=(7.0, 3.8))
    fig.patch.set_facecolor("white")

    all_scores = np.array([p.score for p in scored if p.score is not None])

    # ── Top: histogram ──
    ax1 = fig.add_axes([0.08, 0.56, 0.88, 0.38])
    ax1.hist(all_scores, bins=80, color=C["accent"], alpha=0.28,
             edgecolor="white", lw=0.2, zorder=1)

    # Smoothed overlay
    hist, edges = np.histogram(all_scores, bins=120, density=True)
    centers = (edges[:-1] + edges[1:]) / 2
    kernel = np.ones(9) / 9
    smooth = np.convolve(hist, kernel, mode="same")
    scale = len(all_scores) * (edges[1] - edges[0])

    ax1_twin = ax1.twinx()
    ax1_twin.plot(centers, smooth * scale, color=C["accent_dk"], lw=1.2, zorder=2)
    ax1_twin.fill_between(centers, smooth * scale, alpha=0.08,
                          color=C["accent_dk"], zorder=1)
    ax1_twin.set_ylabel("Density", fontsize=6, color=C["muted"], labelpad=2)
    ax1_twin.tick_params(axis="y", colors=C["muted"], labelsize=5.5)

    m = np.median(all_scores)
    q1, q3 = np.percentile(all_scores, 25), np.percentile(all_scores, 75)
    for val, ls, alpha, lbl in [
        (m, "--", 0.7, f"Median = {m:.1f}"),
        (q1, ":", 0.4, None),
        (q3, ":", 0.4, None),
    ]:
        ax1.axvline(val, color=C["red"], lw=0.8, ls=ls, alpha=alpha)

    ax1.text(m + 0.5, ax1.get_ylim()[1] * 0.94, f"Median = {m:.1f}",
             fontsize=6, color=C["red"], fontweight="bold")
    ax1.text(m + 18, ax1.get_ylim()[1] * 0.94,
             f"IQR: {q1:.1f} – {q3:.1f}", fontsize=5.5, color=C["muted"])

    ax1.set_xlabel("Normalized score", fontsize=6, labelpad=2)
    ax1.set_ylabel("Protein count", fontsize=6, labelpad=2)
    ax1.set_title(
        f"a  Score distribution across {len(scored):,} scored proteins",
        fontsize=7.5, fontweight="bold", color=C["fg"], loc="left", pad=4,
    )
    ax1.tick_params(labelsize=5.5)

    # ── Bottom: boxplots ──
    ax2 = fig.add_axes([0.08, 0.06, 0.88, 0.42])

    cat_scores = []
    cat_names = []
    cat_cols = []
    for cat in CAT_ORDER:
        s = [p.score for p in scored if p.category == cat and p.score is not None]
        if s:
            cat_scores.append(s)
            cat_names.append(CAT_LABEL[cat])
            cat_cols.append(CAT_COLOR[cat])

    bp = ax2.boxplot(cat_scores, vert=False, patch_artist=True,
                     medianprops=dict(color="white", lw=1.0),
                     flierprops=dict(marker=".", markersize=1.2,
                                     alpha=0.25, markeredgewidth=0),
                     whiskerprops=dict(lw=0.5, color=C["grey_dk"]),
                     capprops=dict(lw=0.5, color=C["grey_dk"]),
                     widths=0.55)
    for patch, col in zip(bp["boxes"], cat_cols):
        patch.set_facecolor(col)
        patch.set_alpha(0.80)
        patch.set_edgecolor("none")

    ax2.set_yticklabels(cat_names, fontsize=6)
    ax2.set_xlabel("Normalized score", fontsize=6, labelpad=2)
    ax2.set_title(
        "b  Score distribution by subcellular localization",
        fontsize=7.5, fontweight="bold", color=C["fg"], loc="left", pad=4,
    )
    ax2.tick_params(labelsize=5.5)
    ax2.grid(axis="x", alpha=0.2, lw=0.3)

    # Mean annotations
    for i, s in enumerate(cat_scores):
        mu = np.mean(s)
        ax2.text(ax2.get_xlim()[1] - 0.4, i + 1,
                 r"$\bf{\bar{x}}$" + f"={mu:.1f}", va="center",
                 fontsize=5, color=C["muted"])

    path = OUT_DIR / "fig3_distribution.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# FIGURE 4 — Category breakdown + radar
# ═══════════════════════════════════════════════════════════════

def fig4_category_panels(scored) -> Path:
    """Double-column. Left: horizontal bars. Right: radar."""
    fig = plt.figure(figsize=(7.0, 2.8))
    fig.patch.set_facecolor("white")

    # ── Left: bar chart ──
    ax1 = fig.add_axes([0.06, 0.12, 0.38, 0.78])

    counts = []
    labels = []
    cols = []
    for cat in CAT_ORDER:
        c = sum(1 for p in scored if p.category == cat)
        if c > 0:
            counts.append(c)
            labels.append(CAT_LABEL[cat])
            cols.append(CAT_COLOR[cat])

    bars = ax1.barh(labels, counts, color=cols, edgecolor="none", height=0.55)
    ax1.invert_yaxis()
    ax1.set_xlabel("Protein count", fontsize=6, labelpad=2)
    ax1.set_title(
        f"a  {len(scored):,} proteins by localization",
        fontsize=7.5, fontweight="bold", color=C["fg"], loc="left", pad=4,
    )
    ax1.tick_params(labelsize=5.5)

    for bar, count in zip(bars, counts):
        pct = count / len(scored) * 100
        ax1.text(bar.get_width() + 20, bar.get_y() + bar.get_height() / 2,
                 f"{count:,}  ({pct:.0f}%)", va="center",
                 fontsize=5.5, fontweight="bold", color=C["muted"])

    # ── Right: radar ──
    ax2 = fig.add_axes([0.55, 0.12, 0.42, 0.78], projection="polar")
    ax2.set_facecolor("white")

    dims = ["Nuclear\nlocalization", "Protein\nsize", "Research\nnovelty",
            "3D\nstructure", "Regulatory\ndomains", "PPI\nnetwork"]
    dim_keys = ["nuc", "size", "nov", "struct", "dom", "ppi"]
    n_dims = len(dims)
    angles = np.linspace(0, 2 * np.pi, n_dims, endpoint=False).tolist()
    angles += angles[:1]

    ax2.set_theta_offset(np.pi / 2)
    ax2.set_theta_direction(-1)

    for cat in CAT_ORDER:
        cat_prots = [p for p in scored if p.category == cat]
        meds = []
        for dk in dim_keys:
            vs = [getattr(p, dk) for p in cat_prots if getattr(p, dk) is not None]
            meds.append(np.median(vs) if vs else 0)
        meds += meds[:1]
        ax2.fill(angles, meds, alpha=0.06, color=CAT_COLOR[cat], zorder=1)
        ax2.plot(angles, meds, "o-", lw=0.9, color=CAT_COLOR[cat],
                 markersize=2.5, label=CAT_LABEL[cat], zorder=2)

    ax2.set_xticks(angles[:-1])
    ax2.set_xticklabels(dims, fontsize=5.5, color=C["fg"])
    ax2.set_ylim(0, 10)
    ax2.set_yticks([3, 6, 9])
    ax2.set_yticklabels(["3", "6", "9"], fontsize=5, color=C["muted"])
    ax2.set_rlabel_position(30)
    ax2.grid(alpha=0.15, lw=0.3)
    ax2.legend(loc="upper right", bbox_to_anchor=(1.45, 1.05),
               fontsize=5, frameon=False, ncol=1,
               title="Category", title_fontsize=5.5)
    ax2.set_title("b  Median dimension scores", fontsize=7.5,
                  fontweight="bold", color=C["fg"], loc="left", pad=14)

    path = OUT_DIR / "fig4_category_panels.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# FIGURE 5 — Scoring dimensions reference table
# ═══════════════════════════════════════════════════════════════

def fig5_scoring_table() -> Path:
    """Full double-column width, pure table figure."""
    fig, ax = plt.subplots(figsize=(7.0, 2.8))
    fig.patch.set_facecolor("white")
    ax.axis("off")

    rows = [
        ("Nuclear localization", "×4",
         "UniProt subcellular location, HPA IF images, GO-CC\n(IDA/IMP evidence). Nucleus + chromatin specificity."),
        ("Protein size", "×1",
         "Amino acid length from UniProt. Optimal range\n300–800 aa scored highest (experimental tractability)."),
        ("Research novelty", "×5",
         "PubMed publication count. < 50 papers = high novelty.\nPrioritizes under-studied candidates."),
        ("3D structure", "×3",
         "AlphaFold pLDDT confidence, PDB entries,\ndomain-level structural quality assessment."),
        ("Regulatory domains", "×2",
         "InterPro / SMART / Pfam annotation. Chromatin-binding,\nDNA-binding, and enzymatic domains scored highest."),
        ("PPI network", "×3",
         "IntAct / STRING / BioGRID interaction data. Weighted\nby regulatory partner enrichment in chromatin/RNA."),
        ("Cross-validation", "bonus",
         "0 to +3 concordance bonus for multi-source agreement\nacross all databases (UniProt, HPA, GO, PDB)."),
    ]

    # Column layout
    col_x = [0.04, 0.28, 0.38]  # label start, weight start, desc start
    row_h = 0.28
    header_y = 0.94

    # Title
    ax.text(0.5, 1.0,
            "Scoring dimensions: definitions and data sources",
            ha="center", va="bottom", fontsize=9, fontweight="bold",
            color=C["fg"])

    # Header row
    for x, label in zip(col_x, ["Dimension", "Weight", "Description & data sources"]):
        ax.text(x, header_y, label, ha="left", va="center",
                fontsize=6.5, fontweight="bold", color="white",
                bbox=dict(facecolor=C["accent_dk"], edgecolor="none",
                          boxstyle="round,pad=0.1"))

    # Data rows
    for i, (dim, weight, desc) in enumerate(rows):
        y = header_y - (i + 1) * row_h
        bg = C["grey_lt"] if i % 2 == 0 else "white"

        # Row background
        ax.axhspan(y - row_h / 2, y + row_h / 2, facecolor=bg,
                   edgecolor="none", alpha=0.6, zorder=0)

        ax.text(col_x[0] + 0.01, y, dim, ha="left", va="center",
                fontsize=6.5, fontweight="bold", color=C["fg"])
        ax.text(col_x[1] + 0.01, y, weight, ha="left", va="center",
                fontsize=7.5, fontweight="bold",
                color=C["accent_dk"] if weight != "bonus" else C["orange"])
        ax.text(col_x[2] + 0.01, y, desc, ha="left", va="center",
                fontsize=5.5, color=C["muted"], linespacing=1.3)

    path = OUT_DIR / "fig5_scoring_table.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# FIGURE 6 — Star rating key
# ═══════════════════════════════════════════════════════════════

def fig6_star_key() -> Path:
    """Single-column. Simple key."""
    fig, ax = plt.subplots(figsize=(3.46, 1.6))
    fig.patch.set_facecolor("white")
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    rows_data = [
        ("85-100", "Exceptional: top priority for experimental validation"),
        ("75-84", "Strong: well-supported across most dimensions"),
        ("65-74", "Good: solid scores, some dimension gaps"),
        ("55-64", "Moderate: merits further investigation"),
        ("< 55", "Baseline: review before prioritization"),
    ]
    star_labels = ["5 stars", "4 stars",
                   "3 stars", "2 stars", "1 star"]
    star_colors = [C["accent_dk"], C["accent"], C["grey_dk"], C["grey_md"], C["grey_md"]]

    for i, ((rng, desc), stars, sc) in enumerate(
        zip(rows_data, star_labels, star_colors)
    ):
        y = 8.5 - i * 1.4
        bg = C["grey_lt"] if i % 2 == 0 else "white"
        ax.axhspan(y - 0.55, y + 0.55, facecolor=bg,
                   edgecolor="none", alpha=0.5, zorder=0)
        ax.text(1.0, y, rng, ha="left", va="center",
                fontsize=7.5, fontweight="bold", color=C["fg"])
        ax.text(3.0, y, stars, ha="center", va="center",
                fontsize=11, color=sc)
        ax.text(5.5, y, desc, ha="left", va="center",
                fontsize=6.5, color=C["muted"])

    ax.text(5, 9.7, "Candidate prioritization: star rating key",
            ha="center", va="bottom", fontsize=8,
            fontweight="bold", color=C["fg"])

    # Column headers
    ax.text(0.5, 9.1, "Score", ha="center", va="center",
            fontsize=5.5, fontweight="bold", color=C["muted"])
    ax.text(3.0, 9.1, "Rating", ha="center", va="center",
            fontsize=5.5, fontweight="bold", color=C["muted"])
    ax.text(6.5, 9.1, "Interpretation", ha="left", va="center",
            fontsize=5.5, fontweight="bold", color=C["muted"])

    path = OUT_DIR / "fig6_star_rating.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    scored, rejected = parse_data()
    nuc_r = sum(1 for p in rejected if "核定位" in p.rejected_reason)
    pub_r = sum(1 for p in rejected if "PubMed" in p.rejected_reason)
    print(f"Data: {len(scored):,} scored + {len(rejected):,} rejected "
          f"({nuc_r} nuclear, {pub_r} PubMed)")

    figures = [
        ("fig1_screening_flow",   fig1_screening_flow,   scored, rejected),
        ("fig2_scoring_system",   fig2_scoring_system),
        ("fig3_distribution",     fig3_distribution,     scored),
        ("fig4_category_panels",  fig4_category_panels,  scored),
        ("fig5_scoring_table",    fig5_scoring_table),
        ("fig6_star_rating",      fig6_star_key),
    ]

    for entry in figures:
        name = entry[0]
        func = entry[1]
        args = entry[2:] if len(entry) > 2 else ()
        path = func(*args)
        print(f"  {name}.pdf")

    print(f"\nSaved to: {OUT_DIR}/")
    print(f"  " + "\n  ".join(sorted(f.name for f in OUT_DIR.glob("*.pdf"))))


if __name__ == "__main__":
    main()
