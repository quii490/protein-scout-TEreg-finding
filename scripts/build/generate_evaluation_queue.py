#!/usr/bin/env python3
"""Generate evaluation queue from nuclear_proteins_classified_human.xlsx.

Reads the unclassified_core_nuclear and unclassified_bare sheets, filters out
already-evaluated genes, and outputs a priority-sorted queue TSV.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import sys
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
EXCEL = ROOT / "all_nuclear" / "nuclear_proteins_classified_human.xlsx"
AUDIT = ROOT / "audit_work"
DATA = ROOT / "data" / "summary"
CENTRO = ROOT / "centrosome" / "data"
SPERM = ROOT / "sperm" / "data"

TARGET_SHEETS = ["unclassified_core_nuclear", "unclassified_bare"]

FIELD_ORDER = [
    "priority_rank", "gene_symbol", "full_name", "citations", "hotness",
    "hpa_nuclear", "hpa_locations", "hpa_reliability", "tier",
    "evidence_quality", "uniprot_length", "Combined_BS_Human_Degree",
    "Has_Any_Human_PPI", "uniprot_accession", "uniprot_subcellular",
    "category_reason", "ChIP_Atlas_class", "ENCODE_ChIP_WT",
    "combined_nuclear_ppi", "STRING_Human_Nuclear_Degree",
    "BioGRID_Human_Nuclear_Degree", "sheet",
]


def _int_or(v: Any, default: int = 0) -> int:
    try:
        return int(v)
    except (ValueError, TypeError):
        return default


def collect_evaluated() -> set[str]:
    genes: set[str] = set()
    for path in [
        DATA / "protein_report_index.tsv",
        CENTRO / "centrosome_report_index.tsv",
        SPERM / "sperm_report_index.tsv",
    ]:
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            for row in reader:
                g = (row.get("gene") or "").strip()
                if g:
                    genes.add(g)
    return genes


def read_target_sheets() -> pd.DataFrame:
    frames = []
    for sheet in TARGET_SHEETS:
        df = pd.read_excel(EXCEL, sheet_name=sheet)
        df["sheet"] = sheet
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def priority_sort_key(row: pd.Series) -> tuple[int, int, int, int, int]:
    eq = -_int_or(row.get("evidence_quality"), 0)
    pm = int(row.get("citations", 0) or 0)
    novel = 1 if 0 < pm <= 100 else 0
    hpa = 1 if row.get("hpa_nuclear") else 0
    ppi = _int_or(row.get("Combined_BS_Human_Degree"), 0)
    tier = _int_or(row.get("tier"), 99)
    return (eq, -novel, -hpa, -ppi, tier)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate new-protein evaluation queue")
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--sort-by", choices=["priority", "ppi", "citations", "hpa"], default="priority")
    args = parser.parse_args()

    excel = EXCEL
    if not excel.exists():
        raise SystemExit(f"Excel not found: {excel}")

    evaluated = collect_evaluated()
    print(f"Collected {len(evaluated)} already-evaluated genes from report indexes.", file=sys.stderr)

    df = read_target_sheets()
    print(f"Read {len(df)} rows from sheets: {TARGET_SHEETS}", file=sys.stderr)

    remaining = df[~df["gene_symbol"].isin(evaluated)]
    print(f"Remaining after filtering evaluated: {len(remaining)}", file=sys.stderr)

    remaining = remaining.copy()
    remaining["combined_nuclear_ppi"] = (
        remaining["STRING_Human_Nuclear_Degree"].fillna(0).astype(int)
        + remaining["BioGRID_Human_Nuclear_Degree"].fillna(0).astype(int)
    )

    if args.sort_by == "ppi":
        remaining = remaining.sort_values("Combined_BS_Human_Degree", ascending=False)
    elif args.sort_by == "citations":
        remaining = remaining.sort_values("citations", ascending=True)
    elif args.sort_by == "hpa":
        remaining = remaining.sort_values(
            ["hpa_nuclear", "Combined_BS_Human_Degree"],
            ascending=[False, False],
        )
    else:
        remaining["_sort_key"] = remaining.apply(priority_sort_key, axis=1)
        remaining = remaining.sort_values("_sort_key")

    batch = remaining.head(args.batch_size).copy()
    batch["priority_rank"] = range(1, len(batch) + 1)

    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = args.output or (AUDIT / f"new_pool_queue_{ts}.tsv")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    out_cols = [c for c in FIELD_ORDER if c in batch.columns]
    batch[out_cols].to_csv(out_path, sep="\t", index=False)

    print(f"\nQueue written: {out_path}  ({len(batch)} genes)", file=sys.stderr)
    print(f"Genes:", file=sys.stderr)
    for _, r in batch.iterrows():
        ppi = _int_or(r.get("Combined_BS_Human_Degree"), 0)
        cit = _int_or(r.get("citations"), 0)
        print(
            f"  {r['gene_symbol']:15s}  evidence={r.get('evidence_quality','?')}  "
            f"citations={cit}  hpa_nuc={r.get('hpa_nuclear','?')}  "
            f"ppi={ppi}  tier={r.get('tier','?')}  "
            f"sheet={r.get('sheet','?')}",
            file=sys.stderr,
        )

    # Print TSV path for scripting
    print(str(out_path))


if __name__ == "__main__":
    main()
