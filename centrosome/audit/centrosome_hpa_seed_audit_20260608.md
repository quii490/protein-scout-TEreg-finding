# HPA Centrosome Seed List Audit

**Date:** 2026-06-08
**Fetch method:** HPA JSON API (`?format=json`)

## Source URLs

- Centrosome: `https://www.proteinatlas.org/search/subcell_location%3ACentrosome?format=json&size=500`
- Centriolar satellite: `https://www.proteinatlas.org/search/subcell_location%3ACentriolar+satellite?format=json`

## Counts

| Category | Count |
|----------|-------|
| Centrosome source | 513 |
| Centriolar satellite source | 228 |
| Both sources | 25 |
| Centrosome only | 488 |
| Satellite only | 203 |
| **Total unique seed genes** | **716** |

## Fetch Warnings

- None. Both pages returned clean JSON arrays. All entries have `Gene` fields.
- Some entries have ENSG identifiers instead of standard gene symbols (e.g., ENSG00000144785).
- TP53TG3 family has multiple paralogs (TP53TG3, TP53TG3B-F) which may need deduplication during evaluation.
- ERVV-1 and ERVV-2 are endogenous retrovirus elements - may need manual review.

## Output Files

- `centrosome/data/centrosome_hpa_seed.tsv` — 717 lines (header + 716 genes)
- `centrosome/data/centrosome_hpa_seed.json` — Full seed data with metadata
