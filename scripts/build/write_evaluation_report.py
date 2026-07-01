#!/usr/bin/env python3
"""Generate evaluation reports for a given gene using harvest data + Excel.

Writes to the correct detail/<category>/<GENE>/<GENE>-evaluation.md path.
Scoring follows the established 6+1 dimension system.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
EXCEL = ROOT / "all_nuclear" / "nuclear_proteins_classified_human.xlsx"
DETAIL = ROOT / "detail"

TODAY = dt.date.today().isoformat()


def _get(d: dict, *keys: str, default: Any = "") -> Any:
    for k in keys:
        v = d.get(k)
        if v is not None and v != "":
            return v
    return default


def _int(v: Any, default: int = 0) -> int:
    try:
        return int(v)
    except (ValueError, TypeError):
        return default


def _float(v: Any, default: float = 0.0) -> float:
    try:
        return float(v)
    except (ValueError, TypeError):
        return default


def read_excel_row(gene: str) -> dict[str, Any] | None:
    sheets = ["unclassified_core_nuclear", "unclassified_bare",
              "families", "suspicious_nonfamily"]
    for s in sheets:
        df = pd.read_excel(EXCEL, sheet_name=s)
        m = df[df["gene_symbol"].str.upper() == gene.upper()]
        if len(m) == 0:
            continue
        r = m.iloc[0].to_dict()
        for k, v in r.items():
            if isinstance(v, (pd.Timestamp,)):
                r[k] = str(v)
            elif not isinstance(v, (int, float, str, bool, type(None))):
                r[k] = str(v)
        r["_sheet"] = s
        return r
    return None


def classify(meta: dict, uniprot: dict, hpa: dict, nuc_score: int) -> str:
    if nuc_score <= 3:
        return "rejected"
    hpa_locs = str(meta.get("hpa_locations", ""))
    up_sub = str(meta.get("uniprot_subcellular", ""))

    # Also check hpa probe data
    hpa_main = ""
    if hpa:
        hpa_main = "; ".join(hpa.get("subcellular_main_location", []) or [])
    locs = (hpa_locs + " " + hpa_main + " " + up_sub).lower()

    rules = [
        ("chromatin", ["chromatin", "chromosome", "dna binding"]),
        ("nucleolus", ["nucleoli"]),
        ("nuclear-speckle", ["nuclear speckle", "speckles"]),
        ("nuclear-body", ["nuclear bod"]),
        ("nuclear-envelope", ["nuclear membrane", "nuclear envelope", "lamina"]),
    ]
    for cat, kwlist in rules:
        if any(kw in locs for kw in kwlist):
            return cat

    nuc_hits = sum(1 for t in ["nucleoplasm", "nucleus"] if t in locs)
    cyt_hits = sum(1 for t in ["cytosol", "cytoplasm"] if t in locs)
    if nuc_hits and cyt_hits:
        return "nucleus-cytoplasm"
    return "nucleoplasm"


# ── scoring ────────────────────────────────────────────────────────

def score_nuclear(meta: dict, uniprot: dict, hpa: dict) -> tuple[int, str]:
    hpa_nuc = meta.get("hpa_nuclear")
    hpa_rel = str(meta.get("hpa_reliability", "") or "")
    hpa_locs = str(meta.get("hpa_locations", "") or "")
    if hpa:
        hpa_locs = hpa_locs or "; ".join(hpa.get("subcellular_main_location", []) or [])

    comp_ev = str(meta.get("compartments_nuclear_evidence", "") or "")
    has_ida = "IDA" in comp_ev
    if not has_ida and isinstance(uniprot, dict):
        for sl in uniprot.get("subcellular_locations", []) or []:
            if isinstance(sl, dict) and "IDA" in str(sl.get("evidences", "")):
                has_ida = True
                break

    if hpa_nuc and hpa_rel == "Approved":
        return (9, f"HPA Approved+{'IDA' if has_ida else ''}; {hpa_locs}")
    elif hpa_nuc and hpa_rel in ("Supported", "Enhanced"):
        if has_ida:
            return (8, f"HPA {hpa_rel}+UniProt IDA; {hpa_locs}")
        return (7, f"HPA {hpa_rel}; {hpa_locs}")
    elif hpa_nuc:
        return (6, f"HPA {hpa_rel}; {hpa_locs}")
    elif has_ida:
        return (4, "UniProt IDA 实验证据确认 nucleus (HPA 无核定位)")
    elif "nucleus" in str(meta.get("uniprot_subcellular", "")).lower():
        return (3, "UniProt 标注 nucleus (预测/HDA)")
    else:
        return (2, "核定位证据薄弱，需人工复核")


def score_size(meta: dict) -> tuple[int, str]:
    length = _int(meta.get("uniprot_length"), 0)
    if not length:
        return (5, "大小未知")
    if 300 <= length <= 800:
        return (9, f"{length} aa, 实验优势区间")
    elif 150 <= length < 300:
        return (7, f"{length} aa, 偏小")
    elif 800 < length <= 1200:
        return (7, f"{length} aa, 偏大")
    elif length < 150:
        return (4, f"{length} aa, 太小")
    else:
        return (4, f"{length} aa, 太大")


def score_novelty(meta: dict, pubmed: dict) -> tuple[int, str, bool]:
    strict = _int(pubmed.get("strict_count", -1), -1)
    citations = _int(meta.get("citations", 0), 0)
    if strict < 0:
        strict = citations

    if strict > 100:
        return (0, f"PubMed strict={strict} 篇 >100，触发淘汰", True)
    elif strict == 0:
        return (10, "PubMed 0 篇，极度新颖", False)
    elif strict <= 10:
        return (10, f"PubMed strict={strict} 篇，极度新颖", False)
    elif strict <= 30:
        return (9, f"PubMed strict={strict} 篇，非常新颖", False)
    elif strict <= 50:
        return (8, f"PubMed strict={strict} 篇，新颖", False)
    elif strict <= 75:
        return (7, f"PubMed strict={strict} 篇", False)
    elif strict <= 100:
        return (6, f"PubMed strict={strict} 篇", False)
    else:
        return (0, f"PubMed strict={strict} 篇 >100，触发淘汰", True)


def score_structure(uniprot: dict, alphafold: dict) -> tuple[int, str]:
    pdb = uniprot.get("pdb", []) or []
    has_exp = any(
        isinstance(e, dict) and e.get("method", "") in ("X-ray", "NMR", "EM")
        for e in (pdb if isinstance(pdb, list) else [])
    )
    plddt = alphafold.get("plddt_stats", {}) if alphafold else {}
    mean = _float(plddt.get("mean_plddt", 0))

    if has_exp and mean >= 85:
        return (10, f"PDB实验结构 + AF pLDDT={mean}")
    elif has_exp:
        return (8, f"PDB实验结构; AF pLDDT={mean}")
    elif mean >= 85:
        return (7, f"AF pLDDT={mean}, 高质量预测")
    elif mean >= 70:
        return (5, f"AF pLDDT={mean}, 中等")
    elif mean > 0:
        return (3, f"AF pLDDT={mean}, 低质量")
    else:
        return (2, "无结构数据")


def score_domains(uniprot: dict) -> tuple[int, str]:
    interpro = uniprot.get("interpro", []) or []
    pfam = uniprot.get("pfam", []) or []
    names = " ".join(
        (d.get("name", "") if isinstance(d, dict) else str(d)).lower()
        for d in (interpro + pfam)
    )
    kw = ["chromatin", "histone", "bromodomain", "chromodomain", "phd", "homeobox",
          "homeodomain", "winged helix", "bzip", "zinc finger", "myb", "hth",
          "ets", "forkhead", "dna-binding", "at-hook", "hmg", "sant", "hlh",
          "bhlh", "leucine zipper", "transcription", "coactivator", "corepressor",
          "nuclear receptor", "p53", "ctcf"]
    hits = sum(1 for k in kw if k in names)
    total = len(interpro) + len(pfam)

    if hits >= 3:
        return (9, f"{hits} 个调控相关 domain 命中")
    elif hits >= 2:
        return (8, f"{hits} 个调控相关 domain 命中")
    elif hits >= 1:
        return (7, f"{hits} 个调控相关 domain 命中")
    elif total > 0:
        return (5, f"{total} 个 domain, 非经典调控类型")
    else:
        return (3, "未检测到已知 domain")


def score_ppi(meta: dict) -> tuple[int, str]:
    combined = _int(meta.get("Combined_BS_Human_Degree"), 0)
    if combined >= 500:
        return (10, f"Combined PPI degree={combined} (极高)")
    elif combined >= 200:
        return (9, f"Combined PPI degree={combined} (很高)")
    elif combined >= 100:
        return (8, f"Combined PPI degree={combined} (高)")
    elif combined >= 50:
        return (7, f"Combined PPI degree={combined} (中等)")
    elif combined >= 20:
        return (6, f"Combined PPI degree={combined} (中等偏低)")
    elif combined > 0:
        return (4, f"Combined PPI degree={combined} (低)")
    else:
        return (3, "无 PPI 数据")


def score_cross(nuc: int, meta: dict) -> tuple[int, str]:
    points = 0
    notes = []
    if nuc >= 7 and str(meta.get("hpa_nuclear", "")) == "True":
        points += 1
        notes.append("HPA+UniProt一致")
    if _int(meta.get("evidence_quality"), 0) >= 3:
        points += 1
        notes.append("多源证据")
    if _int(meta.get("tier"), 0) <= 1:
        points += 1
        notes.append("Tier 1强证据")
    return (min(points, 3), "; ".join(notes) if notes else "无额外互证")


# ── markdown report ─────────────────────────────────────────────────

def generate(
    gene: str,
    meta: dict,
    uniprot: dict,
    alphafold: dict,
    pubmed: dict,
    hpa: dict,
    string_ppi: list,
) -> str:
    nuc, nuc_ev = score_nuclear(meta, uniprot, hpa)
    size, size_ev = score_size(meta)
    nov, nov_ev, rejected = score_novelty(meta, pubmed)
    stru, stru_ev = score_structure(uniprot, alphafold)
    dom, dom_ev = score_domains(uniprot)
    ppi_s, ppi_ev = score_ppi(meta)
    cross, cross_note = score_cross(nuc, meta)
    category = classify(meta, uniprot, hpa, nuc)
    if rejected:
        category = "rejected"
    is_rejected = category == "rejected"
    status = "shortlisted" if not is_rejected else "rejected"

    up_name = _get(uniprot, "protein_name") or _get(meta, "full_name", "")
    aliases = _get(meta, "aliases", "")
    aliases_d = f" / {aliases}" if aliases else ""
    acc = _get(meta, "uniprot_accession") or _get(uniprot, "accession", "")
    length = _get(meta, "uniprot_length") or _get(uniprot, "length_aa", "?")
    mass = _get(uniprot, "mass_kda", "")
    mass_d = f" / {mass} kDa" if mass else ""

    out = []
    out.append("---")
    out.append("type: protein-evaluation")
    out.append(f'gene: "{gene}"')
    out.append(f"date: {TODAY}")
    out.append(f"tags: [protein-scout, nuclear-protein, evaluation, {'rejected' if is_rejected else 'shortlisted'}]")
    out.append(f"status: {status}")
    out.append("---\n")

    out.append(f"## {gene} 核蛋白评估报告\n")
    out.append("### 1. 基本信息")
    out.append("| 项目 | 内容 |")
    out.append("|---|---|")
    out.append(f"| 基因名 / 别名 | {gene}{aliases_d} |")
    out.append(f"| 蛋白大小 | {length} aa{mass_d} |")
    out.append(f"| UniProt ID | {acc} |")
    out.append(f"| 评估日期 | {TODAY} |\n")

    raw_total = nuc * 4 + size + nov * 5 + stru * 3 + dom * 2 + ppi_s * 3
    norm = round((raw_total + cross) / 1.83, 1)
    norm_display = f"{norm:.1f}/100" if not is_rejected else "淘汰"

    # Scoring overview table
    out.append("### 2. 评分总览 (新权重)\n")
    if is_rejected:
        reason = "PubMed >100, 研究过于成熟" if rejected else f"核定位 ≤3: {nuc_ev}"
        out.append(f"**淘汰原因**: {reason}\n")

    out.append("| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |")
    out.append("|---|---|---|---|---|")
    out.append(f"| 🔴 核定位特异性 | {nuc}/10 | ×4 | {nuc*4:.1f} | {nuc_ev} |")
    out.append(f"| 📏 蛋白大小 | {size}/10 | ×1 | {size:.1f} | {size_ev} |")
    out.append(f"| 🆕 研究新颖性 | {nov}/10 | ×5 | {nov*5:.1f} | {nov_ev} |")
    out.append(f"| 🏗️ 三维结构 | {stru}/10 | ×3 | {stru*3:.1f} | {stru_ev} |")
    out.append(f"| 🧬 调控结构域 | {dom}/10 | ×2 | {dom*2:.1f} | {dom_ev} |")
    out.append(f"| 🔗 PPI | {ppi_s}/10 | ×3 | {ppi_s*3:.1f} | {ppi_ev} |")
    out.append(f"| **加权总分** | | | **{raw_total}/180**** | |")
    out.append(f"| **归一化总分 (÷1.83)** | | | **{norm_display}**** | 互证: +{cross} ({cross_note}) |\n")

    # 3.1 Nuclear localization
    out.append("### 3. 详细分析\n")
    out.append("#### 3.1 核定位证据")
    out.append("| 来源 | 定位 | 可信度 |")
    out.append("|---|---|---|")
    hpa_locs = str(meta.get("hpa_locations", "") or "")
    hpa_rel = str(meta.get("hpa_reliability", "") or "")
    if hpa:
        hpa_locs = hpa_locs or "; ".join(hpa.get("subcellular_main_location", []) or [])
        hpa_rel = hpa_rel or str(hpa.get("reliability_if", "") or "")
    if hpa_locs:
        out.append(f"| Protein Atlas (IF) | {hpa_locs} | {hpa_rel} |")
    else:
        out.append(f"| Protein Atlas (IF) | 无数据 | — |")

    up_sub = str(meta.get("uniprot_subcellular", "") or "")
    up_sub_short = ""
    for part in up_sub.split(". "):
        if "nucleus" in part.lower() or "nucleoplasm" in part.lower() or "chromos" in part.lower() or "nuclear" in part.lower():
            if len(up_sub_short) + len(part) < 300:
                up_sub_short += part + ". "
    if not up_sub_short:
        up_sub_short = up_sub[:250] if up_sub else "—"
    up_sub_display = up_sub_short.strip() or "—"
    up_ev = "实验证据(IDA/IMP)" if ("IDA" in up_sub or "IMP" in up_sub) else "已标注"
    out.append(f"| UniProt | {up_sub_display} | {up_ev} |")
    out.append("")

    comp_ev = str(meta.get("compartments_nuclear_evidence", "") or "")
    if comp_ev:
        out.append(f"COMPARTMENTS nuclear_score={meta.get('compartments_nuclear_score','?')}: {comp_ev[:100]}\n")

    go_cc = uniprot.get("go_cc", []) or []
    if go_cc:
        out.append("**GO 定位/功能**:")
        for g in go_cc[:10]:
            if isinstance(g, dict):
                out.append(f"- {g.get('id','')}: {g.get('term','')} ({g.get('evidence','')})")
        out.append("")

    if_urls = (hpa or {}).get("if_image_urls", []) or []
    if if_urls:
        out.append("**IF 图像**:")
        for u in if_urls:
            out.append(f"![]({u})")
        out.append("")
    sub_url = (hpa or {}).get("hpa_subcellular_url", "")
    if sub_url and not if_urls:
        out.append(f"IF 图像请参见: [{sub_url}]({sub_url})\n")

    pae = alphafold.get("pae_image_url", "") if alphafold else ""
    if pae:
        out.append(f"**PAE 图**: ![]({pae})\n")

    out.append(f"**结论**: {nuc_ev}。**评分: {nuc}**。\n")

    # 3.2 Size
    out.append(f"#### 3.2 蛋白大小评估\n{size_ev}。**评分: {size}**。\n")

    # 3.3 PubMed
    out.append("#### 3.3 研究现状")
    out.append("| 指标 | 数值 |")
    out.append("|---|---|")
    out.append(f"| PubMed strict | {pubmed.get('strict_count','?')} |")
    out.append(f"| PubMed broad | {pubmed.get('broad_count','?')} |")
    out.append(f"| Hotness | {meta.get('hotness','?')} |")
    papers = pubmed.get("key_papers", []) or []
    if papers:
        out.append("\n**关键文献**:")
        for i, pp in enumerate(papers[:5], 1):
            title = pp.get("title", "?") if isinstance(pp, dict) else str(pp)
            pmid = pp.get("pmid", "") if isinstance(pp, dict) else ""
            journal = pp.get("journal", "") if isinstance(pp, dict) else ""
            authors = pp.get("authors", []) if isinstance(pp, dict) else []
            a = (authors[0] if authors else "?") + (" et al." if len(authors) > 1 else "")
            out.append(f"{i}. {a}. \"{title}\". *{journal}*. PMID: {pmid}")
    out.append(f"\n**评价**: {nov_ev}。**评分: {nov}**。\n")

    # 3.4 Structure
    out.append("#### 3.4 三维结构分析")
    plddt = alphafold.get("plddt_stats", {}) if alphafold else {}
    if plddt:
        out.append("| 指标 | 数值 |")
        out.append("|---|---|")
        out.append(f"| AlphaFold 平均 pLDDT | {plddt.get('mean_plddt','?')} |")
        out.append(f"| >90% | {plddt.get('pct_gt_90','?')}% |")
        out.append(f"| 70-90% | {plddt.get('pct_70_90','?')}% |")
        out.append(f"| 50-70% | {plddt.get('pct_50_70','?')}% |")
        out.append(f"| <50% | {plddt.get('pct_lt_50','?')}% |")
        out.append("")
    pdb = uniprot.get("pdb", []) or []
    if pdb and isinstance(pdb, list):
        for p in pdb[:5]:
            if isinstance(p, dict):
                out.append(f"PDB {p.get('id','?')}: {p.get('method','?')}, resolution={p.get('resolution','?')}\n")
    out.append(f"**评价**: {stru_ev}。**评分: {stru}**。\n")

    # 3.5 Domains
    out.append("#### 3.5 结构域分析")
    interpro = uniprot.get("interpro", []) or []
    pfam = uniprot.get("pfam", []) or []
    if interpro:
        names = "; ".join(
            d.get("name", "") if isinstance(d, dict) else str(d)
            for d in interpro[:5]
        )
        if names.strip():
            out.append(f"- **InterPro**: {names}")
    if pfam:
        names = "; ".join(
            d.get("name", "") if isinstance(d, dict) else str(d)
            for d in pfam[:5]
        )
        if names.strip():
            out.append(f"- **Pfam**: {names}")
    if not interpro and not pfam:
        out.append("- 未检测到已知结构域")
    out.append(f"\n**评价**: {dom_ev}。**评分: {dom}**。\n")

    # 3.6 PPI
    out.append("#### 3.6 PPI 互作网络")
    combined = _int(meta.get("Combined_BS_Human_Degree"), 0)
    out.append(f"Combined PPI degree (human): {combined}")
    string_nuc = _int(meta.get("STRING_Human_Nuclear_Degree"), 0)
    bg_nuc = _int(meta.get("BioGRID_Human_Nuclear_Degree"), 0)
    total_nuc_ppi = string_nuc + bg_nuc
    out.append(f"Total nuclear PPI degree: {total_nuc_ppi}  (STRING Nuclear: {string_nuc} + BioGRID Nuclear: {bg_nuc})")
    out.append(f"\n**评价**: {ppi_ev}。**评分: {ppi_s}**。\n")

    # 3.7 Cross-validation
    out.append("#### 3.7 多库互证")
    out.append("| 维度 | 来源 | 结果 |")
    out.append("|---|---|---|")
    out.append(f"| 核定位 | HPA + UniProt + GO-CC | {'一致' if nuc>=7 else '部分'} |")
    out.append(f"| 结构域 | InterPro + Pfam | {'一致' if interpro or pfam else '有限'} |")
    out.append(f"| PPI | STRING + BioGRID | {'有数据' if combined>0 else '有限'} |")
    out.append(f"\n**互证加分**: +{cross} ({cross_note})\n")

    # 4. Overall
    out.append("### 4. 总体评价\n")
    if is_rejected:
        reason = "PubMed >100" if rejected else f"核定位 ≤3"
        out.append(f"**淘汰**: {reason}。完整评估记录保留供审计。")
    else:
        stars = "⭐" * min(5, max(1, int(norm / 20) + 1))
        out.append(f"**推荐等级**: {stars}")
        out.append(f"\n**归一化总分**: {norm}/100")
        out.append(f"\n**定位分类**: {category}")
        chips = []
        if meta.get("ChIP_Atlas_class") and str(meta["ChIP_Atlas_class"]) != "nan":
            chips.append(f"ChIP: {meta['ChIP_Atlas_class']}")
        if chips:
            out.append(f"\n**额外标签**: {'; '.join(chips)}")
    out.append("")

    # 5. Data sources
    out.append("### 5. 数据来源\n")
    out.append("- UniProt REST API")
    out.append("- AlphaFold Protein Structure Database")
    out.append("- PubMed E-utilities")
    out.append("- STRING/BioGRID protein-protein interaction")
    out.append("- Human Protein Atlas (HPA)")
    out.append("")

    return "\n".join(out)


def main() -> None:
    p = argparse.ArgumentParser(description="Generate evaluation report")
    p.add_argument("--gene", required=True)
    p.add_argument("--harvest", type=Path, help="Harvest packet JSON file")
    p.add_argument("--output", type=Path, help="Output .md path")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    if args.harvest:
        with open(args.harvest) as f:
            packet = json.load(f)
    else:
        print("ERROR: --harvest required", file=sys.stderr)
        sys.exit(1)

    meta = packet.get("meta", {})
    uniprot = packet.get("uniprot", {})
    alphafold = packet.get("alphafold", {})
    pubmed = packet.get("pubmed", {})
    hpa = packet.get("hpa", {})
    string_ppi = packet.get("string_ppi", [])

    report = generate(args.gene, meta, uniprot, alphafold, pubmed, hpa, string_ppi)

    if args.dry_run:
        print(report)
    elif args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        (args.output.parent / "IF_images").mkdir(exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(report)


if __name__ == "__main__":
    main()