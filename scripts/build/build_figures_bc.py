#!/usr/bin/env python3
"""Generate Figures B (candidate dimension heatmap) and C (stacked contribution bars)."""
from __future__ import annotations

import re, json, textwrap
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap, to_hex

ROOT = Path(__file__).resolve().parents[2]
SUMMARY = ROOT / "protein-finding.md"
CENTRO_JSON = ROOT / "centrosome" / "data" / "centrosome_report_index.json"
OUT = ROOT / "docs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

P = {
    "bg": "#FFFFFF", "fg": "#111111", "muted": "#6B7280",
    "accent": "#2563EB", "gold": "#D1910A", "red": "#C0392B",
    "grey_lt": "#F3F4F6", "grey_md": "#D1D5DB",
}

DIM_KEYS = ["nuc", "size", "nov", "struct", "dom", "ppi"]
DIM_LABELS = ["Nuclear\nlocalization", "Protein\nsize", "Research\nnovelty",
              "3D\nstructure", "Regulatory\ndomains", "PPI\nnetwork"]
DIM_WEIGHTS = [4, 1, 5, 3, 2, 3]

CAT_ORDER = ["chromatin", "nucleolus", "nuclear-speckle", "nucleus-cytoplasm",
             "nucleoplasm", "nuclear-envelope", "nuclear-body"]
CAT_COLOR = {
    "chromatin": "#DC2626", "nucleolus": "#2563EB",
    "nuclear-speckle": "#16A34A", "nucleus-cytoplasm": "#9333EA",
    "nucleoplasm": "#EA580C", "nuclear-envelope": "#A16207",
    "nuclear-body": "#DB2777",
}
CAT_LABEL = {
    "chromatin": "Chromatin", "nucleolus": "Nucleolus",
    "nuclear-speckle": "Nuc-speckle", "nucleus-cytoplasm": "Nuc-cyto",
    "nucleoplasm": "Nucleoplasm", "nuclear-envelope": "Nuc-envelope",
    "nuclear-body": "Nuclear body",
}

CANDIDATES_MAIN = {
    "AKAP8L", "PM20D2", "TBRG1", "EEF1AKMT3", "EEF1AKMT4",
    "DGCR6L", "C2orf42", "TEX52", "SPANXC", "SPANXA2",
    "RIPOR3", "FAM228A", "PRAC2", "FAM78A", "C17orf50",
    "C2orf78", "C5orf24", "FAM181A", "FAM227A", "FAM227B",
    "FAM214A", "C11orf71", "KIAA1614",
}

matplotlib.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["Helvetica"],
    "font.size": 7.5, "figure.dpi": 300, "savefig.dpi": 300,
    "pdf.fonttype": 42, "pdf.compression": 9,
    "axes.linewidth": 0.6,
})


def parse_main():
    text = SUMMARY.read_text(encoding="utf-8")
    scored = []
    secs = {c: m.start() for c in CAT_ORDER if (m := re.search(rf"\n## {c}\n", text))}
    em = re.search(r"\n## 已淘汰\n", text)
    em_end = em.start() if em else len(text)
    ordered = sorted(secs.items(), key=lambda x: x[1])
    for i, (cat, s) in enumerate(ordered):
        e = ordered[i + 1][1] if i + 1 < len(ordered) else em_end
        for ln in text[s:e].splitlines():
            ln = ln.strip()
            if not ln.startswith("| ") or "---" in ln or "基因" in ln: continue
            cs = [c.strip() for c in ln.strip("|").split("|")]
            if len(cs) < 11: continue
            try:
                scored.append({
                    "gene": cs[1], "cat": cat,
                    "nuc": int(cs[2]), "size": int(cs[3]),
                    "nov": int(cs[4]), "struct": int(cs[5]),
                    "dom": int(cs[6]), "ppi": int(cs[7]),
                    "cross": cs[8], "score": float(cs[9]),
                })
            except (ValueError, IndexError): continue
    return scored


def parse_centrosome():
    if not CENTRO_JSON.exists():
        return {}
    with open(CENTRO_JSON) as fh:
        data = json.load(fh)
    # Map centro candidates to their dimension scores
    # Centrosome uses different dimensions; we extract what we can
    gene_map = {}
    for r in data.get("records", []):
        g = r["gene"]
        gene_map[g] = {
            "cent_score": r.get("final_centrosome_score"),
            "cent_evidence": r.get("centrosome_evidence_score"),
            "ppi_score": r.get("ppi_score"),
            "structure_domain": r.get("structure_domain_score"),
            "novelty": r.get("novelty_specificity_score"),
        }
    return gene_map


def build_figure_b(scored):
    """Figure B: Candidate dimension heatmap (27 genes x 6 dimensions)."""
    # Filter to candidates with full dimension data
    candidates = [p for p in scored if p["gene"] in CANDIDATES_MAIN]
    # Sort by total score desc
    candidates.sort(key=lambda p: p["score"], reverse=True)

    genes = [c["gene"] for c in candidates]
    n_genes = len(genes)
    n_dims = 6

    # Build data matrix
    data = np.zeros((n_genes, n_dims))
    for i, cp in enumerate(candidates):
        for j, dk in enumerate(DIM_KEYS):
            data[i, j] = cp.get(dk, 0)

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor(P["bg"])

    # Custom colormap: light grey -> blue -> dark blue
    cmap = LinearSegmentedColormap.from_list("score_cmap", [
        "#F5F5F5", "#DEEBF7", "#9ECAE1", "#4292C6", "#2171B5", "#084594",
    ])

    im = ax.pcolormesh(data, cmap=cmap, vmin=0, vmax=10, edgecolors="white", linewidth=2, shading="flat", rasterized=False, snap=True)

    # Axis labels
    ax.set_xticks(range(n_dims))
    ax.set_xticklabels(DIM_LABELS, fontsize=7.5, ha="center")
    ax.set_yticks(range(n_genes))
    ax.set_yticklabels(genes, fontsize=7, fontweight="bold")

    # Annotate each cell with value
    for i in range(n_genes):
        for j in range(n_dims):
            val = data[i, j]
            text_color = "white" if val >= 8 else ("#222222" if val >= 4 else P["muted"])
            ax.text(j, i, f"{int(val)}", ha="center", va="center",
                    fontsize=7.5, fontweight="bold", color=text_color)

    # Category color strip on right
    for i, cp in enumerate(candidates):
        cat = cp["cat"]
        color = CAT_COLOR.get(cat, P["grey_md"])
        ax.add_patch(mpatches.Rectangle(
            (n_dims + 0.3, i - 0.45), 0.6, 0.9,
            facecolor=color, edgecolor="none", alpha=0.7,
            clip_on=False, zorder=5,
        ))
        # Score
        ax.text(n_dims + 0.65, i, f"{cp['score']:.1f}",
                ha="left", va="center", fontsize=7, fontweight="bold",
                color=P["fg"], clip_on=False)

    # Colorbar
    cbar = fig.colorbar(im, ax=ax, fraction=0.02, pad=0.02)
    cbar.set_label("Score (0-10)", fontsize=7, color=P["muted"])
    cbar.ax.tick_params(labelsize=6.5)
    # Prevent colorbar from being rasterized
    cbar.solids.set_rasterized(False)
    cbar.solids.set_snap(True)

    ax.set_title("Candidate Protein Dimension Scores (0-10)",
                 fontsize=11, fontweight="bold", color=P["fg"], pad=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(top=False, right=False)

    # Total score column label
    ax.text(n_dims + 0.65, -1.2, "Total", ha="left", va="top",
            fontsize=6.5, color=P["muted"], fontstyle="italic", clip_on=False)

    fig.tight_layout()
    out = OUT / "figB_candidate_heatmap.png"
    fig.savefig(out, facecolor=P["bg"], edgecolor="none", dpi=300, bbox_inches="tight", pad_inches=0.15)
    fig.savefig(OUT / "figB_candidate_heatmap.pdf", facecolor=P["bg"], edgecolor="none", dpi=300,
                format="pdf", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print(f"  figB_candidate_heatmap.png + .pdf")
    return out


def build_figure_c(scored):
    """Figure C: Stacked contribution bars for top candidates."""
    candidates = [p for p in scored if p["gene"] in CANDIDATES_MAIN]
    candidates.sort(key=lambda p: p["score"], reverse=True)
    # Take top 15 + rest
    top_n = min(18, len(candidates))
    top = candidates[:top_n]

    genes = [c["gene"] for c in top]
    n_genes = len(genes)

    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    fig.patch.set_facecolor(P["bg"])

    # Build stacked data: each bar segment = weighted dimension contribution
    # Raw weighted contributions
    dim_colors = ["#DC2626", "#F59E0B", "#10B981", "#6366F1", "#EC4899", "#0891B2"]
    # Lighter versions for low-weight dims
    dim_alphas = [1.0, 0.6, 1.0, 0.85, 0.7, 0.85]

    y_pos = range(n_genes)
    for i, cp in enumerate(reversed(top)):  # reversed so top gene at top
        left = 0
        for j, dk in enumerate(DIM_KEYS):
            raw = cp.get(dk, 0)
            weighted = raw * DIM_WEIGHTS[j] / 1.83  # normalized contribution
            ax.barh(y_pos[n_genes - 1 - i], weighted, left=left,
                    color=dim_colors[j], alpha=dim_alphas[j],
                    edgecolor="white", lw=0.3, height=0.65)
            left += weighted

    ax.set_yticks(range(n_genes))
    ax.set_yticklabels([c["gene"] for c in reversed(top)], fontsize=7.5, fontweight="bold")
    ax.set_xlabel("Weighted score contribution", fontsize=8, color=P["muted"])
    ax.set_title("Top Candidate Protein Score Composition",
                 fontsize=11, fontweight="bold", color=P["fg"], pad=8)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Legend
    legend_patches = []
    for j, (dk, dl) in enumerate(zip(DIM_KEYS, DIM_LABELS)):
        label_short = dl.replace("\n", " ")
        legend_patches.append(
            mpatches.Patch(color=dim_colors[j], alpha=dim_alphas[j],
                           label=f"{label_short} (x{DIM_WEIGHTS[j]})")
        )
    ax.legend(handles=legend_patches, loc="lower right", fontsize=6,
              ncol=2, frameon=True, facecolor="white", edgecolor=P["grey_md"],
              framealpha=0.85)

    # Category color dots
    for i, cp in enumerate(reversed(top)):
        cat = cp["cat"]
        ax.scatter([cp["score"] * 1.02], [y_pos[n_genes - 1 - i]],
                   s=60, color=CAT_COLOR.get(cat, P["grey_md"]),
                   edgecolors="white", linewidth=1, zorder=10, clip_on=False)
        ax.text(cp["score"] * 1.02 + 1.2, y_pos[n_genes - 1 - i],
                f"{cp['score']:.1f}", fontsize=6.5, fontweight="bold",
                color=P["muted"], va="center", clip_on=False)

    fig.tight_layout()
    out = OUT / "figC_score_breakdown.png"
    fig.savefig(out, facecolor=P["bg"], edgecolor="none", dpi=300, bbox_inches="tight", pad_inches=0.15)
    fig.savefig(OUT / "figC_score_breakdown.pdf", facecolor=P["bg"], edgecolor="none", dpi=300,
                format="pdf", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print(f"  figC_score_breakdown.png + .pdf")
    return out


def main():
    scored = parse_main()
    print(f"Parsed: {len(scored):,} scored proteins")
    n_cand = sum(1 for p in scored if p["gene"] in CANDIDATES_MAIN)
    print(f"Candidates with dimension data: {n_cand}")

    build_figure_b(scored)
    build_figure_c(scored)


if __name__ == "__main__":
    main()
