# WEB_ATLAS_DATA_SCHEMA

Recommended generated outputs:

- `docs/data/protein_report_index.json` for browser search/filter.
- `data/summary/protein_report_index.tsv` for audit-friendly tabular review.
- `data/summary/protein_report_index.csv` for spreadsheet reuse.

## Fields

- `gene` (Reliable): From detail path parent directory; cross-check with report title/table.
- `status` (Reliable with default): `rejected` from `detail/rejected`; otherwise `scored`, with report text override if needed.
- `category` (Reliable): From detail category directory; normalize allowed category vocabulary.
- `score` (Medium): Prefer parsed `protein-finding.md` total score or existing normalized summary; detail parser fallback only.
- `nuclear_score` (Medium): Often available in report scoring tables but label formats vary.
- `report_path` (Reliable): Original `detail/.../*-evaluation.md` path.
- `docs_report_path` (Generated): `docs/reports/GENE.html`; collision handling needed for duplicates.
- `category_page` (Generated): `docs/category/CATEGORY.html`.
- `lines` (Reliable): File line count from detail report.
- `has_hpa` (Medium): Keyword evidence marker; verify in parser against section headings.
- `has_if_image` (Medium): Markdown image/IF keyword marker; separate "has HPA text" from "image embedded".
- `has_pae` (Medium): PAE keyword/image marker.
- `has_pdb` (Medium): PDB/RCSB/structure section marker.
- `has_ppi` (Medium): PPI/STRING/BioGRID/interaction table marker.
- `has_pubmed` (Medium): PubMed/PMID/key literature marker.
- `has_scoring_table` (Medium): Detect scoring table headings and score rows.
- `has_manual_review` (Medium): Manual review/backlog markers.
- `duplicate_count` (Parser needed): Requires duplicate audit or same-gene path scan.
- `duplicate_type` (Parser needed): Use duplicate audit if available; do not infer blindly.
- `is_primary_candidate` (Parser needed): From duplicate resolution or report status.
- `known_backlog_flags` (Parser needed): Combine audit files plus evidence marker gaps.

## Recommended JSON Shape

```json
{
  "generated_at": "20260605_015715",
  "source": {
    "primary_summary": "protein-finding.md",
    "detail_root": "detail/"
  },
  "records": [
    {
      "gene": "ALKBH6",
      "status": "scored",
      "category": "nucleoplasm",
      "score": 0.0,
      "nuclear_score": null,
      "report_path": "detail/nucleoplasm/ALKBH6/ALKBH6-evaluation.md",
      "docs_report_path": "reports/ALKBH6.html",
      "category_page": "category/nucleoplasm.html",
      "evidence": {
        "hpa": true,
        "if_image": true,
        "pae": false,
        "pdb": true,
        "ppi": true,
        "pubmed": true
      },
      "known_backlog_flags": []
    }
  ]
}
```
