#!/usr/bin/env python3
"""Generate publication-grade figures for the protein screening workflow, each as a standalone PDF."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# ── Paths ──────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]
SUMMARY = ROOT / "protein-finding.md"
OUT_DIR = ROOT / "docs" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Colour palette (publication-grade) ─────────────────────────
PALETTE = {
    "bg": "#FFFFFF",
    "text": "#1a1a1a",
    "muted": "#555555",
    "accent": "#2171b5",
    "accent2": "#08519c",
    "gold": "#b8860b",
    "red": "#c0392b",
    "green": "#27ae60",
    "orange": "#e67e22",
    "blue_light": "#deebf7",
    "gray_light": "#f0f0f0",
    "gray_mid": "#cccccc",
    "chromatin": "#e41a1c",
    "nucleolus": "#377eb8",
    "nuclear_speckle": "#4daf4a",
    "nucleus_cytoplasm": "#984ea3",
    "nucleoplasm": "#ff7f00",
    "nuclear_envelope": "#a65628",
    "nuclear_body": "#f781bf",
    "rejected": "#999999",
}

CAT_COLORS = [
    PALETTE["chromatin"], PALETTE["nucleolus"], PALETTE["nuclear_speckle"],
    PALETTE["nucleus_cytoplasm"], PALETTE["nucleoplasm"],
    PALETTE["nuclear_envelope"], PALETTE["nuclear_body"],
]

CAT_LABELS = {
    "chromatin": "Chromatin",
    "nucleolus": "Nucleolus",
    "nuclear-speckle": "Nuclear Speckle",
    "nucleus-cytoplasm": "Nucleus–Cytoplasm",
    "nucleoplasm": "Nucleoplasm",
    "nuclear-envelope": "Nuclear Envelope",
    "nuclear-body": "Nuclear Body",
}

# ── Matplotlib rc ──────────────────────────────────────────────
matplotlib.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 9,
    "axes.titlesize": 11,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 7,
    "figure.dpi": 200,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.2,
    "pdf.fonttype": 42,
    "pdf.compression": 9,
})


@dataclass
class Protein:
    gene: str
    category: str
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
    """Parse protein-finding.md → (scored, rejected)."""
    text = SUMMARY.read_text(encoding="utf-8")
    scored_cats = [
        "chromatin", "nucleolus", "nuclear-speckle",
        "nucleus-cytoplasm", "nucleoplasm", "nuclear-envelope", "nuclear-body",
    ]
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
# FIGURE 1 — Screening Pipeline Funnel
# ═══════════════════════════════════════════════════════════════

def fig1_funnel(scored: list[Protein], rejected: list[Protein]) -> Path:
    nuc_rejects = sum(1 for p in rejected if "核定位" in p.rejected_reason)
    pub_rejects = sum(1 for p in rejected if "PubMed" in p.rejected_reason)
    n_scored = len(scored)

    fig, ax = plt.subplots(figsize=(8.5, 3.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_facecolor("white")

    def draw_box(x, y, w, h, label, value, sub, color):
        rect = mpatches.FancyBboxPatch(
            (x - w / 2, y), w, h,
            boxstyle="round,pad=0.08", facecolor=color, edgecolor="white",
            alpha=0.92, lw=0.5,
        )
        ax.add_patch(rect)
        ax.text(x, y + h / 2 + 0.38, label, ha="center", va="bottom",
                fontsize=8, fontweight="bold", color="white")
        ax.text(x, y + h / 2 - 0.12, value, ha="center", va="center",
                fontsize=12, fontweight="bold", color="white")
        if sub:
            ax.text(x, y + h / 2 - 0.68, sub, ha="center", va="top",
                    fontsize=6.5, color="white", alpha=0.85)

    def draw_arrow(x, y1, y2, label=""):
        ax.annotate("", xy=(x, y2), xytext=(x, y1),
                    arrowprops=dict(arrowstyle="->", color="#666", lw=1.3))
        if label:
            ax.text(x + 0.3, (y1 + y2) / 2, label, ha="left", va="center",
                    fontsize=6.5, color=PALETTE["red"], fontstyle="italic", fontweight="bold")

    y = 1.0

    # Step 1: Input
    draw_box(5, y, 4.2, 1.6, "Excel Gene List", "4,756 genes",
             "Final_TE_finding.xlsx", PALETTE["accent2"])
    y1 = y + 1.6

    # Step 2: Reports
    y += 2.4
    draw_arrow(5, y1, y)
    draw_box(5, y, 4.2, 1.4, "Evaluation Reports", "5,647 reports",
             "86 duplicate genes (multi-category)", PALETTE["accent"])
    y2 = y + 1.4

    # Step 3: Split into two gates
    y += 2.2
    draw_arrow(5, y2, y, "Filter")

    # Gate A: Nuclear ≤ 3
    nuc_x, nuc_w = 2.2, 3.2
    ax.annotate("", xy=(nuc_x + nuc_w / 2, y + 0.6), xytext=(3.8, y),
                arrowprops=dict(arrowstyle="->", color="#888", lw=0.8))
    draw_box(nuc_x, y + 0.6, nuc_w, 0.95,
             f"Nuclear Score <= 3", f"{nuc_rejects} eliminated",
             None, PALETTE["red"])
    ax.text(nuc_x, y + 0.6 + 0.95 + 0.18,
            "Mitochondrial / Golgi / ER / Lysosomal / Secreted",
            ha="center", va="top", fontsize=5.5, color=PALETTE["muted"])

    # Gate B: PubMed > 100
    pub_x, pub_w = 7.8, 3.2
    ax.annotate("", xy=(pub_x - pub_w / 2, y + 0.6), xytext=(6.2, y),
                arrowprops=dict(arrowstyle="->", color="#888", lw=0.8))
    draw_box(pub_x, y + 0.6, pub_w, 0.95,
             f"PubMed > 100", f"{pub_rejects} eliminated",
             None, PALETTE["orange"])
    ax.text(pub_x, y + 0.6 + 0.95 + 0.18,
            "Heavily studied proteins (low novelty)",
            ha="center", va="top", fontsize=5.5, color=PALETTE["muted"])

    # Step 4: Scored
    y += 2.6
    draw_arrow(5, y + 0.6 + 0.95, y)
    draw_box(5, y, 4.2, 1.4, "Passed Screening",
             f"{n_scored} proteins",
             "7 subcellular localization categories", PALETTE["green"])

    # Category legend below
    cat_counts = {}
    for p in scored:
        cat_counts[p.category] = cat_counts.get(p.category, 0) + 1
    cat_str = "  ·  ".join(
        f"{CAT_LABELS[c]} ({n})" for c, n in
        sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
    )
    ax.text(5, y + 1.4 + 0.45, cat_str, ha="center", va="top",
            fontsize=5.8, color=PALETTE["muted"])

    # Title
    ax.set_title(
        "Screening Pipeline for TE-Regulation Nuclear Protein Candidates",
        fontsize=11, fontweight="bold", pad=6, color=PALETTE["text"],
        loc="center",
    )

    path = OUT_DIR / "fig1_screening_funnel.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# FIGURE 2 — Scoring System
# ═══════════════════════════════════════════════════════════════

def fig2_scoring() -> Path:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3.8),
                                    gridspec_kw={"width_ratios": [1.2, 1]})
    fig.patch.set_facecolor("white")

    # ── Left: Weight bar chart ──
    dims = ["Nuclear\nLocalization", "Protein\nSize", "Research\nNovelty",
            "3D\nStructure", "Regulatory\nDomains", "PPI\nNetwork",
            "Cross-\nValidation"]
    weights = [4, 1, 5, 3, 2, 3, 0]
    colors_bar = [PALETTE["accent2"]] + [PALETTE["accent"]] * 5 + [PALETTE["gold"]]
    colors_bar[5] = PALETTE["accent"]

    bars = ax1.barh(range(7), weights, color=colors_bar, edgecolor="white",
                    lw=0.5, height=0.68)
    ax1.set_yticks(range(7))
    ax1.set_yticklabels(dims, fontsize=7.5)
    ax1.set_xlabel("Multiplier", fontsize=8)
    ax1.set_xlim(0, 6.5)
    ax1.invert_yaxis()
    ax1.set_title("Dimension Weights", fontsize=10, fontweight="bold",
                  color=PALETTE["text"])
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    for i, (w, bar) in enumerate(zip(weights, bars)):
        if w > 0:
            ax1.text(w + 0.12, bar.get_y() + bar.get_height() / 2,
                     f"x{w}", va="center", fontsize=8.5, fontweight="bold",
                     color=colors_bar[i])

    # ── Right: Formula box ──
    ax2.axis("off")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_title("Normalized Score", fontsize=10, fontweight="bold",
                  color=PALETTE["text"])

    bbox = mpatches.FancyBboxPatch(
        (0.5, 2.0), 9, 5.8, boxstyle="round,pad=0.4",
        facecolor="#f7f9fc", edgecolor=PALETTE["accent"], lw=1.5,
    )
    ax2.add_patch(bbox)

    ax2.text(5, 6.9, "Raw Weighted Sum", ha="center", fontsize=9.5,
             fontweight="bold", color=PALETTE["text"])
    formula = (
        "(Nuc x 4) + (Size x 1) + (Novelty x 5)\n"
        "+ (Structure x 3) + (Domains x 2)\n"
        "+ (PPI x 3) + Cross-Validation"
    )
    ax2.text(5, 5.7, formula, ha="center", va="top", fontsize=8.5,
             family="monospace", color=PALETTE["accent2"],
             bbox=dict(facecolor="white", edgecolor="none", pad=4))

    ax2.text(5, 4.1, "/ 1.83", ha="center", fontsize=13, fontweight="bold",
             color=PALETTE["red"])

    ax2.text(5, 3.1, "= Normalized Score   (0 -- 100)", ha="center",
             fontsize=9.5, color=PALETTE["text"], fontweight="bold")

    # Additional dims inside the box
    ax2.text(5, 2.4,
             "Each dimension scored 0--10  |  Cross-validation: +0 to +3",
             ha="center", fontsize=7, color=PALETTE["muted"])

    fig.tight_layout()
    path = OUT_DIR / "fig2_scoring_system.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# FIGURE 3 — Score Distribution
# ═══════════════════════════════════════════════════════════════

def fig3_distribution(scored: list[Protein]) -> Path:
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 5.4),
                                    gridspec_kw={"height_ratios": [1.2, 1]})
    fig.patch.set_facecolor("white")

    all_scores = np.array([p.score for p in scored if p.score is not None])

    # ── Top: Histogram + density ──
    ax1.hist(all_scores, bins=70, color=PALETTE["accent"], alpha=0.25,
             edgecolor="white", lw=0.3)

    # Smoothed density via histogram convolution
    hist, bin_edges = np.histogram(all_scores, bins=100, density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    kernel = np.ones(7) / 7
    smoothed = np.convolve(hist, kernel, mode="same")
    scale = len(all_scores) * (bin_edges[1] - bin_edges[0])
    ax1_twin = ax1.twinx()
    ax1_twin.plot(bin_centers, smoothed * scale, color=PALETTE["accent2"],
                  lw=2.0)
    ax1_twin.fill_between(bin_centers, smoothed * scale, alpha=0.12,
                          color=PALETTE["accent2"])
    ax1_twin.set_ylabel("Density", fontsize=8, color=PALETTE["muted"])
    ax1_twin.set_ylim(bottom=0)
    ax1_twin.tick_params(axis="y", colors=PALETTE["muted"], labelsize=7)

    median = np.median(all_scores)
    q1 = np.percentile(all_scores, 25)
    q3 = np.percentile(all_scores, 75)
    ax1.axvline(median, color=PALETTE["red"], lw=1.3, ls="--", alpha=0.7)
    ax1.axvline(q1, color=PALETTE["gray_mid"], lw=0.8, ls=":", alpha=0.5)
    ax1.axvline(q3, color=PALETTE["gray_mid"], lw=0.8, ls=":", alpha=0.5)

    # Annotation
    ax1.text(median + 0.6, ax1.get_ylim()[1] * 0.92,
             f"Median = {median:.1f}", fontsize=8,
             color=PALETTE["red"], fontweight="bold")
    ax1.text(median + 22, ax1.get_ylim()[1] * 0.92,
             f"  (IQR: {q1:.1f} -- {q3:.1f})", fontsize=7,
             color=PALETTE["muted"])

    ax1.set_xlabel("Normalized Score", fontsize=8)
    ax1.set_ylabel("Gene Count", fontsize=8)
    ax1.set_title(
        f"Score Distribution Across All {len(scored):,} Scored Proteins",
        fontsize=10, fontweight="bold", color=PALETTE["text"],
    )
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # ── Bottom: Boxplot per category ──
    cat_order = ["chromatin", "nucleolus", "nuclear-speckle", "nucleus-cytoplasm",
                 "nucleoplasm", "nuclear-envelope", "nuclear-body"]
    cat_scores = []
    cat_names = []
    for cat in cat_order:
        s = [p.score for p in scored if p.category == cat and p.score is not None]
        if s:
            cat_scores.append(s)
            cat_names.append(CAT_LABELS[cat])

    bp = ax2.boxplot(cat_scores, vert=False, patch_artist=True,
                     medianprops=dict(color="white", lw=1.3),
                     flierprops=dict(marker=".", markersize=1.8, alpha=0.25),
                     widths=0.62)
    for patch, color in zip(bp["boxes"], CAT_COLORS[:len(cat_names)]):
        patch.set_facecolor(color)
        patch.set_alpha(0.78)

    ax2.set_yticklabels(cat_names, fontsize=8)
    ax2.set_xlabel("Normalized Score", fontsize=8)
    ax2.set_title("Score Distribution by Subcellular Localization",
                  fontsize=10, fontweight="bold", color=PALETTE["text"])
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    # Mean labels
    for i, (s, name) in enumerate(zip(cat_scores, cat_names)):
        m = np.mean(s)
        ax2.text(ax2.get_xlim()[1] - 0.5, i + 1,
                 f"  mu={m:.1f}", va="center", fontsize=6.5,
                 color=PALETTE["muted"], fontstyle="italic")

    fig.tight_layout(pad=1.5)
    path = OUT_DIR / "fig3_score_distribution.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# FIGURE 4 — Category Composition
# ═══════════════════════════════════════════════════════════════

def fig4_category_breakdown(scored: list[Protein]) -> Path:
    fig, ax = plt.subplots(figsize=(8.5, 2.8))
    fig.patch.set_facecolor("white")

    cat_order = ["chromatin", "nucleolus", "nuclear-speckle", "nucleus-cytoplasm",
                 "nucleoplasm", "nuclear-envelope", "nuclear-body"]
    counts = []
    labels = []
    colors_use = []
    for cat in cat_order:
        c = sum(1 for p in scored if p.category == cat)
        if c > 0:
            counts.append(c)
            labels.append(CAT_LABELS[cat])
            colors_use.append(CAT_COLORS[len(counts) - 1])

    bars = ax.barh(labels, counts, color=colors_use, edgecolor="white",
                   lw=0.5, height=0.68)
    ax.invert_yaxis()
    ax.set_xlabel("Protein Count", fontsize=9)
    ax.set_title(
        f"Scored Proteins by Subcellular Localization ({len(scored):,} total)",
        fontsize=11, fontweight="bold", color=PALETTE["text"],
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for bar, count in zip(bars, counts):
        pct = count / len(scored) * 100
        ax.text(bar.get_width() + 25, bar.get_y() + bar.get_height() / 2,
                f"{count:,}  ({pct:.1f}%)", va="center",
                fontsize=8.5, fontweight="bold", color=PALETTE["muted"])

    fig.tight_layout()
    path = OUT_DIR / "fig4_category_breakdown.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# FIGURE 5 — Radar / Spider Chart
# ═══════════════════════════════════════════════════════════════

def fig5_radar(scored: list[Protein]) -> Path:
    dims = ["Nuclear\nLocalization", "Protein\nSize", "Research\nNovelty",
            "3D\nStructure", "Regulatory\nDomains", "PPI\nNetwork"]
    dim_keys = ["nuc", "size", "nov", "struct", "dom", "ppi"]
    cat_order = ["chromatin", "nucleolus", "nuclear-speckle", "nucleus-cytoplasm",
                 "nucleoplasm", "nuclear-envelope", "nuclear-body"]

    fig, ax = plt.subplots(figsize=(5.5, 5.5), subplot_kw={"projection": "polar"})
    fig.patch.set_facecolor("white")

    n_dims = len(dims)
    angles = np.linspace(0, 2 * np.pi, n_dims, endpoint=False).tolist()
    angles += angles[:1]

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    for cat, color in zip(cat_order, CAT_COLORS):
        cat_proteins = [p for p in scored if p.category == cat]
        medians = []
        for dk in dim_keys:
            vals = [getattr(p, dk) for p in cat_proteins if getattr(p, dk) is not None]
            medians.append(np.median(vals) if vals else 0)
        medians += medians[:1]
        ax.fill(angles, medians, alpha=0.07, color=color)
        ax.plot(angles, medians, "o-", lw=1.6, color=color, markersize=3.5,
                label=CAT_LABELS[cat])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dims, fontsize=7.5, color=PALETTE["text"])
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=6.5,
                       color=PALETTE["muted"])
    ax.set_rlabel_position(30)

    # Custom legend outside
    ax.legend(loc="upper right", bbox_to_anchor=(1.42, 1.08),
              fontsize=6.5, frameon=False, ncol=1,
              title="Category", title_fontsize=7)

    ax.set_title("Median Dimension Scores by Subcellular Localization",
                 fontsize=10, fontweight="bold", pad=22,
                 color=PALETTE["text"])

    path = OUT_DIR / "fig5_category_radar.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# FIGURE 6 — Scoring Summary Table (matplotlib table)
# ═══════════════════════════════════════════════════════════════

def fig6_scoring_table() -> Path:
    fig, ax = plt.subplots(figsize=(8.5, 3.2))
    fig.patch.set_facecolor("white")
    ax.axis("off")

    col_labels = ["Dimension", "Weight", "Scoring Basis", "Data Sources"]
    rows = [
        ["Nuclear Localization", "x4",
         "0-10: UniProt evidence (0) / GO-only (3) / HPA correlative (6) / HPA approved + IDA (10)",
         "UniProt subcellular location, HPA IF images, GO-CC (IDA/IMP)"],
        ["Protein Size", "x1",
         "0-10: <100 aa (2) / 100-300 (5) / 300-800 (10) / 800-1000 (7) / >1000 (4)",
         "UniProt sequence length, molecular weight (kDa)"],
        ["Research Novelty", "x5",
         "0-10: PubMed >500 (0) / 100-500 (3) / 50-100 (6) / <50 (10)",
         "PubMed publication count, targeted literature search relevance"],
        ["3D Structure", "x3",
         "0-10: pLDDT confidence + PDB entries + domain-level structure quality",
         "AlphaFold pLDDT, PDB, domain architecture"],
        ["Regulatory Domains", "x2",
         "0-10: none (0) / generic (4) / chromatin/DNA-binding (7) / TE-related (10)",
         "InterPro, SMART, Pfam domain annotation"],
        ["PPI Network", "x3",
         "0-10: <5 partners (2) / 5-20 (5) / 20-50 (7) / >50 + regulatory enrichment (10)",
         "IntAct, STRING, BioGRID; weighted by regulatory partner fraction"],
        ["Cross-Validation", "bonus",
         "0 to +3: concordance bonus for multi-source agreement across databases",
         "All sources above"],
    ]

    # Manual table drawing
    n_rows = len(rows) + 1
    n_cols = 4
    col_widths = [0.18, 0.08, 0.48, 0.26]

    # Header
    header_color = PALETTE["accent2"]
    header_props = dict(facecolor=header_color, edgecolor="white", lw=0.5,
                        boxstyle="round,pad=0.08")
    for j, label in enumerate(col_labels):
        x_start = sum(col_widths[:j])
        ax.text(x_start + col_widths[j] / 2, 0.92, label,
                ha="center", va="center", fontsize=7.5, fontweight="bold",
                color="white",
                bbox=dict(facecolor=header_color, edgecolor="white", lw=0.5,
                          boxstyle="round,pad=0.12"))

    for i, row in enumerate(rows):
        y = 0.92 - (i + 1) * 0.12
        bg = "#fafafa" if i % 2 == 0 else "white"
        for j, cell in enumerate(row):
            x_start = sum(col_widths[:j])
            fontsize = 7 if j < 2 else 6
            weight = "bold" if j < 2 else "normal"
            color = PALETTE["accent2"] if j == 1 else PALETTE["text"]
            ax.text(x_start + 0.01, y, cell,
                    ha="left", va="center", fontsize=fontsize,
                    fontweight=weight, color=color,
                    bbox=dict(facecolor=bg, edgecolor="#eeeeee", lw=0.3,
                              boxstyle="square,pad=0.15"))
        # Row separator
        ax.axhline(y - 0.06, xmin=0, xmax=1, color="#eeeeee", lw=0.5)

    ax.set_title("Scoring Dimensions: Definitions and Data Sources",
                 fontsize=11, fontweight="bold", color=PALETTE["text"], pad=6)

    path = OUT_DIR / "fig6_scoring_table.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# FIGURE 7 — Star Rating Key
# ═══════════════════════════════════════════════════════════════

def fig7_star_key() -> Path:
    fig, ax = plt.subplots(figsize=(8.5, 2.3))
    fig.patch.set_facecolor("white")
    ax.axis("off")

    rows = [
        ("85 -- 100", "5 stars  (Top tier)", "Exceptional: top priority for experimental validation"),
        ("75 -- 84", "4 stars", "Strong: well-supported across most dimensions"),
        ("65 -- 74", "3 stars", "Good: solid scores with some dimension gaps"),
        ("55 -- 64", "2 stars", "Moderate: merits further investigation"),
        ("< 55", "1 star", "Baseline: review before prioritization"),
    ]
    star_colors = ["#b8860b", "#b8860b", "#888888", "#888888", "#999999"]

    # Header
    hx = [0.05, 0.22, 0.58]
    for hx_pos, label in zip(hx, ["Score Range", "Rating", "Interpretation"]):
        ax.text(hx_pos, 0.96, label,
                ha="left", va="center", fontsize=7.5, fontweight="bold",
                color="white",
                bbox=dict(facecolor=PALETTE["accent2"], edgecolor="white",
                          lw=0.5, boxstyle="round,pad=0.12"))

    for i, ((rng, stars, interp), sc) in enumerate(zip(rows, star_colors)):
        y = 0.93 - (i + 1) * 0.16
        bg = "#fafafa" if i % 2 == 0 else "white"
        ax.text(hx[0] + 0.01, y, rng, ha="left", va="center",
                fontsize=8.5, fontweight="bold", color=PALETTE["text"],
                bbox=dict(facecolor=bg, edgecolor="#eeeeee", lw=0.3, boxstyle="square,pad=0.12"))
        ax.text(hx[1] + 0.01, y, stars, ha="left", va="center",
                fontsize=15, color=sc,
                bbox=dict(facecolor=bg, edgecolor="#eeeeee", lw=0.3, boxstyle="square,pad=0.12"))
        ax.text(hx[2] + 0.01, y, interp, ha="left", va="center",
                fontsize=7.5, color=PALETTE["muted"],
                bbox=dict(facecolor=bg, edgecolor="#eeeeee", lw=0.3, boxstyle="square,pad=0.12"))

    for y_line in [0.93 - (j + 1) * 0.16 - 0.08 for j in range(5)]:
        ax.axhline(y_line, xmin=0, xmax=1, color="#eeeeee", lw=0.5)

    ax.set_title("Candidate Prioritization: Star Rating Key",
                 fontsize=11, fontweight="bold", color=PALETTE["text"], pad=8)

    path = OUT_DIR / "fig7_star_rating_key.pdf"
    with PdfPages(path) as pdf:
        pdf.savefig(fig, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def main() -> None:
    scored, rejected = parse_data()
    nuc_r = sum(1 for p in rejected if "核定位" in p.rejected_reason)
    pub_r = sum(1 for p in rejected if "PubMed" in p.rejected_reason)
    print(f"Data parsed: {len(scored):,} scored + {len(rejected):,} rejected "
          f"({nuc_r} nuclear <=3 + {pub_r} PubMed >100)")

    figures = [
        ("Figure 1: Screening Pipeline", fig1_funnel, scored, rejected),
        ("Figure 2: Scoring System", fig2_scoring),
        ("Figure 3: Score Distribution", fig3_distribution, scored),
        ("Figure 4: Category Breakdown", fig4_category_breakdown, scored),
        ("Figure 5: Category Radar", fig5_radar, scored),
        ("Figure 6: Scoring Table", fig6_scoring_table),
        ("Figure 7: Star Rating Key", fig7_star_key),
    ]

    for entry in figures:
        label = entry[0]
        func = entry[1]
        args = entry[2:] if len(entry) > 2 else ()
        path = func(*args)
        print(f"  {label}  →  {path.name}")

    print(f"\nAll figures saved to: {OUT_DIR}/")
    print("  " + "\n  ".join(sorted(f.name for f in OUT_DIR.glob("*.pdf"))))


if __name__ == "__main__":
    main()
