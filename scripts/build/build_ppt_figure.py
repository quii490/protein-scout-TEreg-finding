#!/usr/bin/env python3
"""PPT-grade figure: screening atlas (main + centrosome) with candidate callouts."""
from __future__ import annotations

import json, re, textwrap
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

ROOT = Path(__file__).resolve().parents[2]
SUMMARY = ROOT / "protein-finding.md"
CENTRO_JSON = ROOT / "centrosome" / "data" / "centrosome_report_index.json"
OUT = ROOT / "docs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

P = {
    "bg": "#FFFFFF", "fg": "#111111", "muted": "#6B7280",
    "accent": "#2563EB", "gold": "#D1910A", "gold_lt": "#F5D04E",
    "red": "#C0392B", "grey_lt": "#F3F4F6", "grey_md": "#D1D5DB",
}

CAT_COLOR = {
    "chromatin": "#DC2626", "nucleolus": "#2563EB",
    "nuclear-speckle": "#16A34A", "nucleus-cytoplasm": "#9333EA",
    "nucleoplasm": "#EA580C", "nuclear-envelope": "#A16207",
    "nuclear-body": "#DB2777", "rejected": "#9CA3AF",
}
CAT_LABEL = {
    "chromatin": "Chromatin", "nucleolus": "Nucleolus",
    "nuclear-speckle": "Nuclear speckle", "nucleus-cytoplasm": "Nucl-cyto",
    "nucleoplasm": "Nucleoplasm", "nuclear-envelope": "Nucl-envelope",
    "nuclear-body": "Nuclear body",
}
CAT_ORDER = [c for c in CAT_LABEL if c != "rejected"]

CANDIDATES_MAIN = {
    "AKAP8L": "Nuclear speckles; rRNA; zinc finger",
    "PM20D2": "Nuclear dipeptidase; chromatin substrates",
    "TBRG1": "411 aa; FY-rich; INO80 interaction",
    "EEF1AKMT3": "Elongation factor methylation",
    "EEF1AKMT4": "Elongation factor methylation family",
    "DGCR6L": "Strong PPI network",
    "C2orf42": "Zinc finger; AGO2 interaction",
    "TEX52": "300 aa; aromatic-rich; testis",
    "SPANXC": "SPANX family; sperm; LaminA/C",
    "SPANXA2": "SPANX family; sperm; LaminA/C",
    "RIPOR3": "RHO GTPase pathway",
    "FAM228A": "201 aa; SPANXN3 interaction",
    "PRAC2": "90 aa; Tudor domain",
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
}
CANDIDATES_CENTRO = {
    "C11orf80": "TOP6BL; SPO11 complex; topoisomerase",
    "C1orf146": "SPO16 homolog; MSH4/5; SPO11 interactor",
    "C20orf96": "SHLD family; dsDNA break repair",
    "FAM117B": "589 aa; centrosome-related",
}

matplotlib.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["Helvetica"],
    "font.size": 8, "figure.dpi": 300, "savefig.dpi": 300,
    "pdf.fonttype": 42, "pdf.compression": 9,
    "axes.linewidth": 0.6,
})


def parse_main():
    text = SUMMARY.read_text(encoding="utf-8")
    scored, rejected = [], []
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
                scored.append({"gene": cs[1], "cat": cat,
                    "score": float(cs[9])})
            except (ValueError, IndexError): continue
    if em:
        for ln in text[em_end:].splitlines():
            ln = ln.strip()
            if not ln.startswith("| ") or "---" in ln or "基因" in ln: continue
            cs = [c.strip() for c in ln.strip("|").split("|")]
            if len(cs) < 4: continue
            try: rejected.append({"gene": cs[1]})
            except (ValueError, IndexError): continue
    return scored, rejected


def parse_centrosome():
    if not CENTRO_JSON.exists():
        return []
    with open(CENTRO_JSON) as fh:
        data = json.load(fh)
    result = []
    for r in data.get("records", []):
        sc = r.get("final_centrosome_score")
        if sc:
            result.append({"gene": r["gene"], "score": float(sc), "status": r.get("status", "?")})
    result.sort(key=lambda x: x["score"], reverse=True)
    return result


def build(scored, rejected, centro):
    scored_s = sorted(scored, key=lambda p: p["score"] or 0, reverse=True)
    n_scored = len(scored_s)
    all_scores = np.array([p["score"] for p in scored_s])
    s_min, s_max = all_scores.min(), all_scores.max()

    # ── FIGURE ──
    w, h = 16.0, 9.0
    fig = plt.figure(figsize=(w, h), facecolor=P["bg"])

    fig.text(0.04, 0.98,
        "Protein Scout  ·  Screening Atlas with Manually Selected Candidates",
        fontsize=13, fontweight="bold", color=P["fg"], ha="left", va="top")
    fig.text(0.04, 0.95,
        f"{n_scored:,} scored across 7 categories  |  "
        f"{len(rejected):,} eliminated  |  "
        f"{len(CANDIDATES_MAIN)} main + {len(CANDIDATES_CENTRO)} centrosome candidates",
        fontsize=8.5, color=P["muted"], ha="left", va="top")

    # ── LEFT 55%: Category density strips ──
    ax = fig.add_axes([0.04, 0.05, 0.54, 0.87])
    ax.set_facecolor("#FAFBFC")

    # Gather per-category scores
    cat_data = {}
    for cat in CAT_ORDER:
        ss = np.array([p["score"] for p in scored_s if p["cat"] == cat])
        if len(ss):
            cat_data[cat] = ss
    cat_order_disp = sorted(cat_data, key=lambda c: np.median(cat_data[c]), reverse=True)

    y_positions = []

    for ci, cat in enumerate(cat_order_disp):
        ss = cat_data[cat]
        n_ss = len(ss)
        # Smoothed density strip
        bins = np.linspace(s_min, s_max, 120)
        hist, edges = np.histogram(ss, bins=bins, density=True)
        centers = (edges[:-1] + edges[1:]) / 2
        smooth = np.convolve(hist, np.ones(7) / 7, mode="same")
        max_h = smooth.max()
        if max_h > 0:
            smooth = smooth / max_h * 0.38

        yb = ci
        for j in range(len(centers) - 1):
            ax.add_patch(mpatches.Rectangle(
                (centers[j], yb - smooth[j] / 2), centers[j + 1] - centers[j], smooth[j],
                facecolor=CAT_COLOR[cat], edgecolor="none", alpha=0.82, zorder=2))

        ax.text(s_min - 1.5, yb, CAT_LABEL[cat],
                ha="right", va="center", fontsize=7.5, fontweight="bold", color=CAT_COLOR[cat])
        ax.text(s_max + 1, yb, f"n = {n_ss:,}",
                ha="left", va="center", fontsize=6.5, color=P["muted"])

        # Gold markers for candidates in this category
        cands = [p for p in scored_s if p["cat"] == cat and p["gene"] in CANDIDATES_MAIN]
        for cp in cands:
            sc = cp["score"]
            ax.plot([sc, sc], [yb - 0.32, yb + 0.32],
                    color=P["gold"], lw=1.5, zorder=10, solid_capstyle="round")
            ax.scatter([sc], [yb], s=35, color=P["gold"],
                       edgecolors="white", linewidth=0.8, zorder=11)
            ax.text(sc, yb + 0.45, cp["gene"],
                    fontsize=5.5, fontweight="bold", color=P["gold"],
                    ha="center", va="bottom", rotation=60, zorder=12)

        y_positions.append(yb)

    # Centrosome strip
    if centro:
        centro_scores = np.array([c["score"] for c in centro])
        c_s_min, c_s_max = centro_scores.min(), centro_scores.max()

        yc = len(cat_order_disp)
        bins_c = np.linspace(c_s_min, c_s_max, 60)
        hist_c, edges_c = np.histogram(centro_scores, bins=bins_c, density=True)
        centers_c = (edges_c[:-1] + edges_c[1:]) / 2
        smooth_c = np.convolve(hist_c, np.ones(5) / 5, mode="same")
        max_h_c = smooth_c.max()
        if max_h_c > 0:
            smooth_c = smooth_c / max_h_c * 0.38

        for j in range(len(centers_c) - 1):
            ax.add_patch(mpatches.Rectangle(
                (centers_c[j], yc - smooth_c[j] / 2),
                centers_c[j + 1] - centers_c[j], smooth_c[j],
                facecolor="#0891B2", edgecolor="none", alpha=0.70, zorder=2))

        ax.text(s_min - 1.5, yc, "Centrosome",
                ha="right", va="center", fontsize=7, fontweight="bold",
                color="#0891B2", fontstyle="italic")
        ax.text(s_max + 1, yc, f"n = {len(centro):,}",
                ha="left", va="center", fontsize=5.8, color=P["muted"])

        for cg in CANDIDATES_CENTRO:
            hits = [c for c in centro if c["gene"] == cg]
            for h in hits:
                sc = h["score"]
                ax.plot([sc, sc], [yc - 0.28, yc + 0.28],
                        color=P["gold"], lw=1.3, zorder=10, solid_capstyle="round")
                ax.scatter([sc], [yc], s=28, color=P["gold"],
                           edgecolors="white", linewidth=0.7, zorder=11)
                ax.text(sc, yc + 0.42, cg,
                        fontsize=5, fontweight="bold", color=P["gold"],
                        ha="center", va="bottom", rotation=55, zorder=12)

        y_positions.append(yc)
        y_max = yc + 0.3
    else:
        y_max = len(cat_order_disp) - 0.2

    ax.set_yticks(y_positions)
    ax.set_yticklabels([])
    ax.set_xlabel("Normalized score", fontsize=8, color=P["muted"], labelpad=6)
    ax.set_xlim(s_min - 7, s_max + 5)
    ax.set_ylim(-0.8, y_max)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="x", labelsize=7, colors=P["muted"])
    ax.tick_params(axis="y", left=False, labelleft=False)
    ax.grid(axis="x", alpha=0.15, lw=0.4)

    leg = [mpatches.Patch(color=P["gold"], label="Manually selected candidate")]
    if centro:
        leg.append(mpatches.Patch(color="#0891B2", alpha=0.7,
                    label="Centrosome module (independent scoring)"))
    ax.legend(handles=leg, loc="lower right", fontsize=6.5,
              frameon=True, facecolor="white", edgecolor=P["grey_md"], framealpha=0.9)

    # ── RIGHT 38%: Candidate table ──
    ax2 = fig.add_axes([0.61, 0.05, 0.36, 0.90])
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")
    ax2.add_patch(mpatches.FancyBboxPatch(
        (0, 0), 10, 10, boxstyle="round,pad=0.15",
        facecolor="#F8F9FB", edgecolor=P["grey_md"], lw=0.6, zorder=0))

    ax2.text(0.4, 9.65, "Selected Candidates",
             fontsize=11, fontweight="bold", color=P["fg"], ha="left", va="top")
    ax2.text(0.4, 9.30,
             f"{len(CANDIDATES_MAIN)} main atlas + {len(CANDIDATES_CENTRO)} centrosome module",
             fontsize=7.5, color=P["muted"], ha="left", va="top")

    # Main candidates list
    main_list = sorted(
        [p for p in scored_s if p["gene"] in CANDIDATES_MAIN],
        key=lambda p: p["score"] or 0, reverse=True,
    )

    y = 8.80
    dy = 0.35
    def add_row(rank, gene, score, tag, tag_color, note, y_pos):
        if y_pos < 0.3 or rank > 28:
            return y_pos
        if rank % 2 == 1:
            ax2.add_patch(mpatches.Rectangle(
                (0.05, y_pos - dy * 0.4), 9.9, dy * 0.86,
                facecolor="white", edgecolor="none", alpha=0.55, zorder=1))
        ax2.text(0.35, y_pos, str(rank), fontsize=7.5, fontweight="bold",
                 color=P["grey_md"], ha="right", va="center", zorder=5)
        ax2.scatter([0.55], [y_pos], s=12, color=P["gold"],
                    edgecolors="white", linewidth=0.5, zorder=10)
        ax2.text(0.75, y_pos, gene, fontsize=8, fontweight="bold",
                 color=P["fg"], ha="left", va="center", zorder=5)
        sc_clr = P["accent"] if score >= 75 else P["muted"]
        sc_str = f"{score:.1f}" if score is not None else "-"
        ax2.text(2.85, y_pos, sc_str, fontsize=7.5, fontweight="bold",
                 color=sc_clr, ha="left", va="center", zorder=5)
        tag_w = len(tag) * 0.46 + 0.70
        ax2.add_patch(mpatches.FancyBboxPatch(
            (3.40, y_pos - 0.09), tag_w, 0.18,
            boxstyle="round,pad=0.03", facecolor=tag_color,
            edgecolor="none", alpha=0.12, zorder=2))
        ax2.text(3.40 + tag_w / 2, y_pos, tag, fontsize=5.3,
                 color=tag_color, ha="center", va="center", fontweight="bold", zorder=5)
        n_short = textwrap.shorten(note, width=48, placeholder=" ...")
        ax2.text(3.40 + tag_w + 0.35, y_pos, n_short, fontsize=5.8,
                 color=P["muted"], ha="left", va="center", fontstyle="italic", zorder=5)
        return y_pos - dy

    for ci, cp in enumerate(main_list):
        y = add_row(ci + 1, cp["gene"], cp["score"],
                     CAT_LABEL.get(cp["cat"], cp["cat"]),
                     CAT_COLOR.get(cp["cat"], P["grey_md"]),
                     CANDIDATES_MAIN.get(cp["gene"], ""), y)

    # Separator
    ax2.axhline(y + 0.05, xmin=0.15, xmax=0.85, color=P["grey_md"], lw=0.5, alpha=0.4)
    ax2.text(0.4, y - 0.08, "Centrosome Module",
             fontsize=7.5, fontweight="bold", color="#0891B2",
             ha="left", va="top", fontstyle="italic")
    y -= 0.28

    # Centrosome candidates
    centro_cand_list = []
    for cg, note in CANDIDATES_CENTRO.items():
        hits = [c for c in centro if c["gene"] == cg]
        sc = hits[0]["score"] if hits else None
        centro_cand_list.append((cg, sc, note))
    centro_cand_list.sort(key=lambda x: x[1] or 0, reverse=True)

    for ci, (cg, sc, note) in enumerate(centro_cand_list):
        rank = len(main_list) + ci + 1
        y = add_row(rank, cg, sc, "centrosome", "#0891B2", note, y)

    ax2.text(5.0, 0.10,
             "Scores > 75 in blue  |  Centrosome: independent 0-100 scale",
             fontsize=5.5, color=P["grey_md"], ha="center", va="center",
             fontstyle="italic")

    # ── SAVE ──
    fig_w, fig_h = 16.0, 9.0
    dpi = 300
    fig.set_size_inches(fig_w, fig_h, forward=True)
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    buf = np.asarray(canvas.buffer_rgba())
    from PIL import Image
    img = Image.fromarray(buf)
    png_path = OUT / "screening_atlas_candidates.png"
    img.save(png_path, format="PNG")
    pdf_path = OUT / "screening_atlas_candidates.pdf"
    fig.savefig(pdf_path, facecolor=P["bg"], edgecolor="none", dpi=dpi,
                format="pdf", bbox_inches="tight", pad_inches=0.2)
    plt.close(fig)
    h_buf, w_buf = buf.shape[:2]
    print(f"Output: {w_buf}x{h_buf} px, aspect: {w_buf/h_buf:.3f} (16:9=1.778)")
    print(f"  {png_path}  |  {pdf_path}")


def main():
    scored, rejected = parse_main()
    centro = parse_centrosome()
    print(f"Main: {len(scored):,} scored + {len(rejected):,} rejected")
    print(f"Centrosome: {len(centro)} scored records  |  "
          f"Candidates: {len(CANDIDATES_MAIN)} main + {len(CANDIDATES_CENTRO)} centro")
    build(scored, rejected, centro)


if __name__ == "__main__":
    main()
