#!/usr/bin/env python3
"""Generate a publication-grade PDF illustrating the protein screening workflow and scoring system."""
from __future__ import annotations

import io
import math
import re
from dataclasses import dataclass
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import numpy as np
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak,
    Table, TableStyle, KeepTogether,
)
from reportlab.platypus.flowables import HRFlowable

# ── Paths ──────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]
SUMMARY = ROOT / "protein-finding.md"
OUTPUT = ROOT / "docs" / "protein_screening_workflow.pdf"
CHART_DIR = ROOT / "docs" / "assets" / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

# ── Colour palette (publication-grade) ─────────────────────────
PALETTE = {
    "bg": "#FFFFFF",
    "text": "#1a1a1a",
    "muted": "#666666",
    "accent": "#2171b5",
    "accent2": "#08519c",
    "gold": "#d4a017",
    "red": "#c0392b",
    "green": "#27ae60",
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
    "nucleus-cytoplasm": "Nucleus-Cytoplasm",
    "nucleoplasm": "Nucleoplasm",
    "nuclear-envelope": "Nuclear Envelope",
    "nuclear-body": "Nuclear Body",
}

CAT_LABELS_CN = {
    "chromatin": "染色质",
    "nucleolus": "核仁",
    "nuclear-speckle": "核斑点",
    "nucleus-cytoplasm": "核-质",
    "nucleoplasm": "核质",
    "nuclear-envelope": "核膜",
    "nuclear-body": "核体",
}

# ── Matplotlib config ─────────────────────────────────────────
matplotlib.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 9,
    "axes.titlesize": 11,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 7.5,
    "figure.dpi": 200,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.15,
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

    # Scored sections
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

    # Rejected section
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
# FIGURE GENERATION (matplotlib)
# ═══════════════════════════════════════════════════════════════


def fig_screening_funnel(scored: list[Protein], rejected: list[Protein]) -> Path:
    """Figure 1: Screening funnel flowchart."""
    fig, ax = plt.subplots(figsize=(8.5, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_facecolor("white")

    nuc_rejects = sum(1 for p in rejected if "核定位" in p.rejected_reason)
    pub_rejects = sum(1 for p in rejected if "PubMed" in p.rejected_reason)
    n_scored = len(scored)

    def draw_step(x, y, w, h, label, value, sub, color=PALETTE["accent"]):
        rect = mpatches.FancyBboxPatch(
            (x - w / 2, y), w, h,
            boxstyle="round,pad=0.08", facecolor=color, edgecolor="white",
            alpha=0.92, lw=0.5,
        )
        ax.add_patch(rect)
        ax.text(x, y + h / 2 + 0.35, label, ha="center", va="bottom",
                fontsize=7.5, fontweight="bold", color="white")
        ax.text(x, y + h / 2 - 0.12, value, ha="center", va="center",
                fontsize=11, fontweight="bold", color="white")
        if sub:
            ax.text(x, y + h / 2 - 0.65, sub, ha="center", va="top",
                    fontsize=6.5, color="white", alpha=0.85)
        return x, y + h

    def draw_arrow(x, y1, y2, label=""):
        ax.annotate("", xy=(x, y2), xytext=(x, y1),
                    arrowprops=dict(arrowstyle="->", color="#555", lw=1.2))
        if label:
            ax.text(x + 0.35, (y1 + y2) / 2, label, ha="left", va="center",
                    fontsize=6.5, color=PALETTE["red"], fontstyle="italic")

    y_pos = 1.2

    # Step 1: Excel input
    _, y1 = draw_step(5, y_pos, 4.0, 1.6, "Excel 基因列表", "4,756 genes",
                      "Final_TE_finding.xlsx", PALETTE["accent2"])
    y_step2 = y1 + 0.7

    # Step 2: Reports generated
    draw_arrow(5, y1, y_step2)
    _, y2 = draw_step(5, y_step2, 4.0, 1.4, "蛋白质评估报告", "5,647 reports",
                      "含 86 个重复基因 (多定位分类)", PALETTE["accent"])

    # Step 3: Two elimination branches
    y_cut = y2 + 0.8
    draw_arrow(5, y2, y_cut, "筛选")

    # Nuclear ≤3
    nuc_x, nuc_w = 2.2, 3.2
    draw_arrow(3.8, y_cut - 0.5, y_cut + 0.2)
    _, _ = draw_step(nuc_x, y_cut + 0.2, nuc_w, 0.9,
                     f"核定位 ≤3 淘汰", f"{nuc_rejects} genes",
                     None, PALETTE["red"])
    ax.text(nuc_x, y_cut + 0.2 + 0.45 + 0.15, "线粒体 / 高尔基体 / 内质网 / 分泌 / 胞质蛋白",
            ha="center", va="top", fontsize=5.5, color=PALETTE["muted"])

    # PubMed >100
    pub_x, pub_w = 7.8, 3.2
    draw_arrow(6.2, y_cut - 0.5, y_cut + 0.2)
    _, _ = draw_step(pub_x, y_cut + 0.2, pub_w, 0.9,
                     f"PubMed >100 淘汰", f"{pub_rejects} genes",
                     None, "#e67e22")
    ax.text(pub_x, y_cut + 0.2 + 0.45 + 0.15, "高度研究的蛋白（缺乏新颖性）",
            ha="center", va="top", fontsize=5.5, color=PALETTE["muted"])

    # Step 4: Scored
    y_scored = y_cut + 2.1
    draw_arrow(5, y_cut + 0.2 + 0.9, y_scored)
    _, y_final = draw_step(5, y_scored, 4.0, 1.4, "通过评分",
                           f"{n_scored} proteins",
                           "7 个亚细胞定位分类", PALETTE["green"])

    # Category distribution under scored
    cat_counts = {}
    for p in scored:
        cat_counts[p.category] = cat_counts.get(p.category, 0) + 1
    cat_items = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
    cat_str = " · ".join(f"{CAT_LABELS_CN.get(c, c)} {n}" for c, n in cat_items)
    ax.text(5, y_final + 0.35, cat_str, ha="center", va="top",
            fontsize=6, color=PALETTE["muted"])

    ax.set_title("Screening Pipeline for TE-Regulation Nuclear Protein Candidates",
                 fontsize=12, fontweight="bold", pad=8, color=PALETTE["text"])

    path = CHART_DIR / "fig1_funnel.png"
    fig.savefig(path, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


def fig_scoring_system() -> Path:
    """Figure 2: Scoring system — dimension weights and formula."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3.6),
                                    gridspec_kw={"width_ratios": [1.2, 1]})
    fig.patch.set_facecolor("white")

    # ── Left: Weight bar chart ──
    dims = ["核定位\nNuclear\nLocalization",
            "蛋白大小\nProtein\nSize",
            "新颖性\nResearch\nNovelty",
            "三维结构\n3D\nStructure",
            "调控结构域\nRegulatory\nDomains",
            "PPI\nNetwork",
            "互证加分\nCross-\nValidation"]
    weights = [4, 1, 5, 3, 2, 3, 0]
    colors_bar = [PALETTE["accent2"], PALETTE["accent"]] * 3 + [PALETTE["accent2"]]
    colors_bar[6] = PALETTE["gold"]

    bars = ax1.barh(range(7), weights, color=colors_bar, edgecolor="white", lw=0.5, height=0.7)
    ax1.set_yticks(range(7))
    ax1.set_yticklabels(dims, fontsize=7.5)
    ax1.set_xlabel("Weight", fontsize=8)
    ax1.set_xlim(0, 6)
    ax1.invert_yaxis()
    ax1.set_title("Dimension Weights", fontsize=10, fontweight="bold", color=PALETTE["text"])
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    for i, (w, bar) in enumerate(zip(weights, bars)):
        if w > 0:
            ax1.text(w + 0.1, bar.get_y() + bar.get_height() / 2,
                     f"×{w}", va="center", fontsize=8, fontweight="bold",
                     color=colors_bar[i])

    # ── Right: Formula box ──
    ax2.axis("off")
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_title("Normalized Score Formula", fontsize=10, fontweight="bold",
                  color=PALETTE["text"])

    formula_bbox = mpatches.FancyBboxPatch(
        (0.5, 2.5), 9, 5, boxstyle="round,pad=0.3",
        facecolor="#f8f9fa", edgecolor=PALETTE["accent"], lw=1.5,
    )
    ax2.add_patch(formula_bbox)

    ax2.text(5, 6.3, "Score =", ha="center", fontsize=10, fontweight="bold",
             color=PALETTE["text"])
    formula = (
        "(Nuc × 4) + (Size × 1) + (Novelty × 5) + (Structure × 3)\n"
        "+ (Domains × 2) + (PPI × 3) + Cross-Validation"
    )
    ax2.text(5, 5.3, formula, ha="center", va="top", fontsize=8.5,
             family="monospace", color=PALETTE["accent2"],
             bbox=dict(facecolor="white", edgecolor="none", pad=3))

    ax2.text(5, 4.0, "÷ 1.83", ha="center", fontsize=12, fontweight="bold",
             color=PALETTE["red"])

    ax2.text(5, 3.0, "→ 0–100 Normalized Score", ha="center", fontsize=9,
             color=PALETTE["text"], fontweight="bold")

    path = CHART_DIR / "fig2_scoring.png"
    fig.savefig(path, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


def fig_score_distribution(scored: list[Protein]) -> Path:
    """Figure 3: Score distribution — histogram + boxplot per category."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 4.8),
                                    gridspec_kw={"height_ratios": [1.2, 1]})
    fig.patch.set_facecolor("white")

    all_scores = [p.score for p in scored if p.score is not None]

    # ── Top: Overall histogram + density ──
    ax1.hist(all_scores, bins=60, color=PALETTE["accent"], alpha=0.3, edgecolor="white", lw=0.3)
    # KDE-like fill using numpy histogram
    try:
        hist, bin_edges = np.histogram(all_scores, bins=80, density=True)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        # Smooth with a simple rolling average
        kernel = np.ones(5) / 5
        smoothed = np.convolve(hist, kernel, mode='same')
        # Scale to match histogram
        scale = len(all_scores) * (bin_edges[1] - bin_edges[0])
        ax1_twin = ax1.twinx()
        ax1_twin.plot(bin_centers, smoothed * scale, color=PALETTE["accent2"], lw=1.8)
        ax1_twin.fill_between(bin_centers, smoothed * scale, alpha=0.12, color=PALETTE["accent2"])
        ax1_twin.set_ylabel("Density", fontsize=8, color=PALETTE["muted"])
        ax1_twin.set_ylim(bottom=0)
    except Exception:
        pass

    median = np.median(all_scores)
    ax1.axvline(median, color=PALETTE["red"], lw=1.2, ls="--", alpha=0.7)
    ax1.text(median + 0.5, ax1.get_ylim()[1] * 0.92, f"Median = {median:.1f}",
             fontsize=7.5, color=PALETTE["red"])

    ax1.set_xlabel("Normalized Score", fontsize=8)
    ax1.set_ylabel("Gene Count", fontsize=8)
    ax1.set_title("Score Distribution (All 4,128 Scored Proteins)", fontsize=10,
                  fontweight="bold", color=PALETTE["text"])
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
                     medianprops=dict(color="white", lw=1.2),
                     flierprops=dict(marker=".", markersize=2, alpha=0.3),
                     widths=0.65)
    for patch, color in zip(bp["boxes"], CAT_COLORS):
        patch.set_facecolor(color)
        patch.set_alpha(0.75)

    ax2.set_yticklabels(cat_names, fontsize=7.5)
    ax2.set_xlabel("Normalized Score", fontsize=8)
    ax2.set_title("Score Distribution by Subcellular Localization Category",
                  fontsize=10, fontweight="bold", color=PALETTE["text"])
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    # Add mean labels
    for i, (s, name) in enumerate(zip(cat_scores, cat_names)):
        m = np.mean(s)
        ax2.text(m + 0.3, i + 1, f"{m:.1f}", va="center", fontsize=6.5,
                 color=PALETTE["muted"])

    fig.tight_layout()
    path = CHART_DIR / "fig3_distribution.png"
    fig.savefig(path, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


def fig_radar(scored: list[Protein]) -> Path:
    """Figure 4: Radar/spider chart — median dimension scores per category."""
    dims = ["Nuclear\nLocalization", "Protein\nSize", "Research\nNovelty",
            "3D\nStructure", "Regulatory\nDomains", "PPI\nNetwork"]
    dim_keys = ["nuc", "size", "nov", "struct", "dom", "ppi"]
    cat_order = ["chromatin", "nucleolus", "nuclear-speckle", "nucleus-cytoplasm",
                 "nucleoplasm", "nuclear-envelope", "nuclear-body"]

    fig, ax = plt.subplots(figsize=(5.5, 5), subplot_kw={"projection": "polar"})
    fig.patch.set_facecolor("white")

    n_dims = len(dims)
    angles = np.linspace(0, 2 * np.pi, n_dims, endpoint=False).tolist()
    angles += angles[:1]

    for cat, color in zip(cat_order, CAT_COLORS):
        cat_proteins = [p for p in scored if p.category == cat]
        medians = []
        for dk in dim_keys:
            vals = [getattr(p, dk) for p in cat_proteins if getattr(p, dk) is not None]
            medians.append(np.median(vals) if vals else 0)
        medians += medians[:1]
        ax.fill(angles, medians, alpha=0.08, color=color)
        ax.plot(angles, medians, "o-", lw=1.5, color=color, markersize=3,
                label=CAT_LABELS_CN.get(cat, cat))

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dims, fontsize=7)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=6, color=PALETTE["muted"])
    ax.set_title("Median Dimension Scores by Category", fontsize=10, fontweight="bold",
                 pad=18, color=PALETTE["text"])
    ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.1), fontsize=6.5,
              frameon=False)

    path = CHART_DIR / "fig4_radar.png"
    fig.savefig(path, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


def fig_pp_panel(scored: list[Protein]) -> Path:
    """Figure 5: Elimination breakdown as a two-panel bar chart."""
    fig, ax = plt.subplots(figsize=(8.5, 2.8))
    fig.patch.set_facecolor("white")

    # Category counts
    cat_order = ["chromatin", "nucleolus", "nuclear-speckle", "nucleus-cytoplasm",
                 "nucleoplasm", "nuclear-envelope", "nuclear-body"]
    counts = []
    labels = []
    for cat in cat_order:
        c = sum(1 for p in scored if p.category == cat)
        if c > 0:
            counts.append(c)
            labels.append(CAT_LABELS_CN.get(cat, cat))

    bars = ax.barh(labels, counts, color=CAT_COLORS[:len(labels)], edgecolor="white", lw=0.5, height=0.7)
    ax.invert_yaxis()
    ax.set_xlabel("Gene Count", fontsize=8)
    ax.set_title("Scored Proteins by Subcellular Localization (4,128 total)", fontsize=10,
                 fontweight="bold", color=PALETTE["text"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for bar, count in zip(bars, counts):
        ax.text(bar.get_width() + 15, bar.get_y() + bar.get_height() / 2,
                f"{count}", va="center", fontsize=8, fontweight="bold",
                color=PALETTE["muted"])

    path = CHART_DIR / "fig5_categories.png"
    fig.savefig(path, facecolor="white", edgecolor="none")
    plt.close(fig)
    return path


# ═══════════════════════════════════════════════════════════════
# PDF BUILDING (reportlab)
# ═══════════════════════════════════════════════════════════════

A4_W, A4_H = A4

def build_pdf(scored: list[Protein], rejected: list[Protein]) -> None:
    """Assemble all figures into a publication-grade PDF."""

    nuc_rejects = sum(1 for p in rejected if "核定位" in p.rejected_reason)
    pub_rejects = sum(1 for p in rejected if "PubMed" in p.rejected_reason)
    n_scored = len(scored)

    # Styles
    styles = {
        "title": ParagraphStyle(
            "CoverTitle", fontName="Helvetica-Bold", fontSize=22,
            textColor=HexColor(PALETTE["text"]), alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "subtitle": ParagraphStyle(
            "CoverSubtitle", fontName="Helvetica", fontSize=11,
            textColor=HexColor(PALETTE["muted"]), alignment=TA_CENTER,
            spaceAfter=24,
        ),
        "h1": ParagraphStyle(
            "H1", fontName="Helvetica-Bold", fontSize=14,
            textColor=HexColor(PALETTE["accent2"]), spaceBefore=18, spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "H2", fontName="Helvetica-Bold", fontSize=11,
            textColor=HexColor(PALETTE["text"]), spaceBefore=12, spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "Body", fontName="Helvetica", fontSize=9,
            textColor=HexColor(PALETTE["text"]), alignment=TA_JUSTIFY,
            spaceBefore=2, spaceAfter=6, leading=13,
        ),
        "caption": ParagraphStyle(
            "Caption", fontName="Helvetica-Oblique", fontSize=7.5,
            textColor=HexColor(PALETTE["muted"]), alignment=TA_LEFT,
            spaceBefore=2, spaceAfter=10,
        ),
        "small": ParagraphStyle(
            "Small", fontName="Helvetica", fontSize=7.5,
            textColor=HexColor(PALETTE["muted"]),
        ),
        "stat_label": ParagraphStyle(
            "StatLabel", fontName="Helvetica", fontSize=8,
            textColor=HexColor(PALETTE["muted"]), alignment=TA_CENTER,
        ),
        "stat_value": ParagraphStyle(
            "StatValue", fontName="Helvetica-Bold", fontSize=18,
            textColor=HexColor(PALETTE["accent2"]), alignment=TA_CENTER,
        ),
    }

    story = []

    # ── COVER ──────────────────────────────────────────────────
    story.append(Spacer(1, 80))
    story.append(Paragraph("Protein Screening Workflow &amp; Scoring System",
                           styles["title"]))
    story.append(Spacer(1, 4))
    story.append(Paragraph("TE-Regulation Nuclear Protein Candidate Atlas",
                           styles["subtitle"]))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="60%", thickness=1.5,
                             color=HexColor(PALETTE["accent"]),
                             spaceAfter=20))

    # Stats row
    stat_data = [
        ["4,756", "5,647", "4,128", "1,470", "7"],
        ["Input Genes", "Reports Generated", "Scored (Passed)", "Eliminated", "Categories"],
    ]
    stat_table = Table(stat_data, colWidths=[90, 90, 90, 90, 70])
    stat_table.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 16),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor(PALETTE["accent2"])),
        ("FONTNAME", (0, 1), (-1, 1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, 1), 8),
        ("TEXTCOLOR", (0, 1), (-1, 1), HexColor(PALETTE["muted"])),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(stat_table)
    story.append(Spacer(1, 16))

    story.append(Paragraph(
        "A systematic screening pipeline for identifying nuclear protein candidates "
        "relevant to transposable element (TE) regulation. Starting from 4,756 human "
        "genes, we applied a multi-dimensional scoring system across 7 subcellular "
        "localization categories to prioritize candidates for experimental validation.",
        styles["body"],
    ))
    story.append(Paragraph(
        f"Date: June 2026 · {n_scored} scored + {nuc_rejects + pub_rejects} eliminated",
        styles["small"],
    ))

    story.append(PageBreak())

    # ── FIGURE 1: SCREENING FUNNEL ─────────────────────────────
    story.append(Paragraph("1. Screening Pipeline Overview", styles["h1"]))
    story.append(Paragraph(
        "The screening process begins with all 4,756 genes from the TE-regulated protein "
        "finding Excel sheet. Each gene is evaluated across 7 dimensions and assigned "
        "to a subcellular localization category. Two elimination gates remove non-nuclear "
        "proteins and proteins with excessive literature coverage (PubMed &gt; 100).",
        styles["body"],
    ))

    # Generate figures
    fig_paths = {
        "funnel": fig_screening_funnel(scored, rejected),
        "scoring": fig_scoring_system(),
        "distribution": fig_score_distribution(scored),
        "radar": fig_radar(scored),
        "categories": fig_pp_panel(scored),
    }

    img = Image(str(fig_paths["funnel"]), width=A4_W - 4 * cm, height=(A4_W - 4 * cm) * 0.38)
    story.append(img)
    story.append(Paragraph(
        "<b>Figure 1.</b> Screening pipeline from Excel gene list to scored proteins. "
        "Two independent elimination gates operate in parallel: nuclear localization "
        "score ≤ 3 and PubMed publication count > 100.",
        styles["caption"],
    ))

    # Elimination detail table
    story.append(Paragraph("Elimination Summary", styles["h2"]))
    elim_data = [
        ["Gate", "Criterion", "Count", "Description"],
        ["Nuclear ≤ 3", "核定位 score ≤ 3 / 10", str(nuc_rejects),
         "Mitochondrial, Golgi, ER, lysosomal, secreted, and other non-nuclear proteins. "
         "Nuclear score derived from UniProt subcellular location + HPA IF + GO annotations."],
        ["PubMed > 100", "PubMed publications > 100", str(pub_rejects),
         "Proteins with extensive existing literature are excluded due to low "
         "research novelty; the pipeline prioritizes under-studied candidates."],
        ["Scored", "Passes both gates", str(n_scored),
         "7 subcellular localization categories, ranked by composite score."],
    ]
    elim_table = Table(elim_data, colWidths=[2.5 * cm, 3.5 * cm, 1.8 * cm, 8 * cm])
    elim_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor(PALETTE["accent"])),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("BACKGROUND", (0, 1), (-1, -1), HexColor("#fafafa")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#fafafa"), white]),
    ]))
    story.append(elim_table)
    story.append(Paragraph(
        "<b>Table 1.</b> Screening gates and their elimination criteria.",
        styles["caption"],
    ))

    story.append(PageBreak())

    # ── FIGURE 2: SCORING SYSTEM ───────────────────────────────
    story.append(Paragraph("2. Multi-Dimensional Scoring System", styles["h1"]))
    story.append(Paragraph(
        "Each candidate protein is scored on 6 core dimensions (0–10 scale) plus "
        "a cross-validation bonus. Dimensions are weighted to reflect their relative "
        "importance for TE regulation research. The final normalized score (0–100) "
        "enables direct comparison across all categories.",
        styles["body"],
    ))

    img2 = Image(str(fig_paths["scoring"]), width=A4_W - 4 * cm, height=(A4_W - 4 * cm) * 0.43)
    story.append(img2)
    story.append(Paragraph(
        "<b>Figure 2.</b> (Left) Dimension weight distribution. Nuclear localization (×4) "
        "and research novelty (×5) carry the highest weights, reflecting their primacy "
        "in candidate prioritization. (Right) Normalization formula. The divisor 1.83 "
        "maps the theoretical maximum of 183 to a 0–100 scale.",
        styles["caption"],
    ))

    # Dimension description table
    story.append(Paragraph("Dimension Definitions", styles["h2"]))
    dim_data = [
        ["Dimension", "CN", "Weight", "Data Sources"],
        ["Nuclear Localization", "核定位特异性", "×4",
         "UniProt subcellular location, HPA IF images, GO cellular component (IDA/IMP)"],
        ["Protein Size", "蛋白大小", "×1",
         "Amino acid length, molecular weight (kDa). Optimal range: 300–800 aa"],
        ["Research Novelty", "研究新颖性", "×5",
         "PubMed publication count (favoring &lt; 50), targeted literature search relevance"],
        ["3D Structure", "三维结构", "×3",
         "AlphaFold pLDDT, PDB entries, domain-level structural confidence"],
        ["Regulatory Domains", "调控结构域", "×2",
         "InterPro/SMART domain annotation, chromatin/DNA-binding domains, enzymatic domains"],
        ["PPI Network", "PPI 网络", "×3",
         "IntAct, STRING, BioGRID interaction data. Weighted by regulatory partner enrichment"],
        ["Cross-Validation", "互证加分", "bonus",
         "Concordance across databases (0 to +3). Rewards multi-source agreement"],
    ]
    dim_table = Table(dim_data, colWidths=[3 * cm, 2.2 * cm, 1.2 * cm, 9.3 * cm])
    dim_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor(PALETTE["accent"])),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("BACKGROUND", (0, 1), (-1, -1), HexColor("#fafafa")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#fafafa"), white]),
    ]))
    story.append(dim_table)
    story.append(Paragraph(
        "<b>Table 2.</b> Scoring dimensions with data sources and weight justification.",
        styles["caption"],
    ))

    story.append(PageBreak())

    # ── FIGURE 3: SCORE DISTRIBUTION ───────────────────────────
    story.append(Paragraph("3. Score Distribution Analysis", styles["h1"]))
    story.append(Paragraph(
        "The overall score distribution and per-category breakdown reveal the "
        "statistical properties of the scoring system. The boxplots enable direct "
        "comparison of score medians, spreads, and outliers across subcellular "
        "localization categories.",
        styles["body"],
    ))
    img3 = Image(str(fig_paths["distribution"]), width=A4_W - 4 * cm, height=(A4_W - 4 * cm) * 0.56)
    story.append(img3)
    story.append(Paragraph(
        "<b>Figure 3.</b> (Top) Overall normalized score histogram with kernel density "
        "estimate overlay. Dashed red line indicates the median. (Bottom) Boxplot "
        "comparison across 7 subcellular localization categories, showing distribution "
        "spread, quartiles, and outlier patterns.",
        styles["caption"],
    ))

    # ── FIGURE 4: CATEGORY BAR CHART ──────────────────────────
    story.append(Paragraph("4. Category Composition", styles["h1"]))
    img5 = Image(str(fig_paths["categories"]), width=A4_W - 4 * cm, height=(A4_W - 4 * cm) * 0.33)
    story.append(img5)
    story.append(Paragraph(
        "<b>Figure 4.</b> Breakdown of 4,128 scored proteins across 7 subcellular "
        "localization categories. Nucleoplasm is the largest category (2,890 proteins), "
        "followed by Nucleolus (400), Nuclear Speckle (329), and Chromatin (138).",
        styles["caption"],
    ))

    story.append(PageBreak())

    # ── FIGURE 5: RADAR ────────────────────────────────────────
    story.append(Paragraph("5. Category Phenotypic Fingerprints", styles["h1"]))
    story.append(Paragraph(
        "Median dimension scores reveal distinct phenotypic profiles for each "
        "subcellular localization category. These 'fingerprints' help identify "
        "category-level biases — for instance, Chromatin proteins tend to score "
        "higher on regulatory domains, while Nucleolus proteins show stronger "
        "PPI networks.",
        styles["body"],
    ))
    img4 = Image(str(fig_paths["radar"]), width=10.5 * cm, height=10.5 * cm)
    story.append(img4)
    story.append(Paragraph(
        "<b>Figure 5.</b> Radar chart of median dimension scores (0–10) per category. "
        "Each axis represents one scoring dimension. Chromatin proteins (red) show "
        "elevated nuclear localization and regulatory domain scores. Nuclear Speckle "
        "proteins (green) show higher PPI network richness.",
        styles["caption"],
    ))

    # Star rating key
    story.append(Paragraph("Star Rating Key", styles["h2"]))
    star_data = [
        ["Score Range", "Stars", "Interpretation"],
        ["85–100", "⭐⭐⭐⭐⭐", "Exceptional candidate — top priority for experimental validation"],
        ["75–84", "⭐⭐⭐⭐", "Strong candidate — well-supported across most dimensions"],
        ["65–74", "⭐⭐⭐", "Good candidate — solid scores with some dimension gaps"],
        ["55–64", "⭐⭐", "Moderate candidate — merits further investigation"],
        ["&lt; 55", "⭐", "Baseline candidate — review before prioritization"],
    ]
    star_table = Table(star_data, colWidths=[3 * cm, 3 * cm, 9.8 * cm])
    star_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor(PALETTE["accent"])),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("BACKGROUND", (0, 1), (-1, -1), HexColor("#fafafa")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#fafafa"), white]),
    ]))
    story.append(star_table)
    story.append(Paragraph(
        "<b>Table 3.</b> Star rating system for candidate prioritization.",
        styles["caption"],
    ))

    # ── BUILD ──────────────────────────────────────────────────
    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=A4,
        leftMargin=2 * cm, rightMargin=2 * cm,
        topMargin=1.5 * cm, bottomMargin=1.5 * cm,
        title="Protein Screening Workflow & Scoring System",
        author="Protein Scout / TEreg Finding",
        subject="Nuclear Protein Candidate Screening",
    )
    doc.build(story)
    print(f"PDF written: {OUTPUT}")


def main() -> None:
    scored, rejected = parse_data()
    nuc_r = sum(1 for p in rejected if "核定位" in p.rejected_reason)
    pub_r = sum(1 for p in rejected if "PubMed" in p.rejected_reason)
    print(f"Scored: {len(scored)}, Rejected: {len(rejected)} ({nuc_r} nuc ≤3 + {pub_r} PubMed >100)")
    build_pdf(scored, rejected)


if __name__ == "__main__":
    main()
