# Centrosome Module — Pilot 10 Final Report

**Date:** 2026-06-08
**Status:** PILOT COMPLETE

---

## HPA Seed Statistics

| Metric | Count |
|--------|-------|
| HPA seed total unique genes | 716 |
| Centrosome source | 513 |
| Centriolar satellite source | 228 |
| Both sources | 25 |
| Centrosome only | 488 |
| Satellite only | 203 |

## Pilot 10 Gene List

| Gene | Source | In Main Atlas | Score | Status |
|------|--------|:---:|:---:|--------|
| CETN2 | Centrosome | Yes | 76 | CENTROSOME_CANDIDATE |
| PLK4 | Centrosome | Yes | 63 | CENTROSOME_CANDIDATE |
| CEP192 | Centrosome | No | 63 | CENTROSOME_CANDIDATE |
| AURKA | Centrosome | Yes | 62 | CENTROSOME_LOW_PRIORITY |
| CCP110 | Satellite | Yes | 62 | CENTROSOME_CANDIDATE |
| PCM1 | Satellite | No | 62 | CENTROSOME_CANDIDATE |
| CEP97 | Both | No | 62 | CENTROSOME_CANDIDATE |
| NEDD1 | Centrosome | Yes | 62 | CENTROSOME_CANDIDATE |
| CEP72 | Both | No | 58 | CENTROSOME_CANDIDATE |
| CCDC14 | Satellite | No | 26 | CENTROSOME_MANUAL_REVIEW |

## Pilot Harvest Results

| Metric | Count |
|--------|-------|
| PubMed data harvested | 10/10 |
| HPA seed evidence present | 10/10 |
| Structure/domain analyzed | 10/10 |
| PPI data present | 10/10 |
| TE relevance assessed | 10/10 |

## Pilot QA

| Metric | Count |
|--------|-------|
| QA PASS | 10 |
| QA FAIL | 0 |
| Reports with ≥100 lines | 10/10 |
| Contains prohibited language | 0/10 |

## Status Distribution

| Status | Count |
|--------|-------|
| CENTROSOME_CANDIDATE | 8 |
| CENTROSOME_LOW_PRIORITY | 1 |
| CENTROSOME_MANUAL_REVIEW | 1 |

## Main Atlas Overlap

| Metric | Count |
|--------|-------|
| Pilot genes in main atlas | 5 (AURKA, PLK4, NEDD1, CETN2, CCP110) |
| Pilot genes not in main atlas | 5 (CEP192, PCM1, CCDC14, CEP72, CEP97) |
| Main atlas total unchanged? | ✅ Yes (5,647 records) |

## docs/centrosome/ Generation

| Page | Status |
|------|--------|
| `docs/centrosome/index.html` | ✅ Built |
| `docs/centrosome/protein_index.html` | ✅ Built |
| `docs/centrosome/reports/GENE.html` | ✅ 10 pages built |
| `docs/centrosome/data/centrosome_report_index.json` | ✅ Built |

## Scoring Policy

- ✅ No nuclear_score-based rejection
- ✅ Independent centrosome scoring (6 dimensions, 0-100)
- ✅ Does not modify main atlas
- ✅ Does not count in main total/scored/rejected

## Outstanding Issues

- CCDC14: very low score (26), manual review recommended — extremely novel (7 papers) but weak evidence
- AURKA: high PubMed volume (3,081) limits novelty despite excellent centrosome evidence
- ~706 un-evaluated centrosome seed genes remain for full evaluation

## Main Atlas Pollution Check

✅ **PASSED** — All record counts unchanged. No centrosome data in main directories.

## Final Decision

**READY_FOR_FULL_CENTROSOME_EVALUATION**

The pilot demonstrates the centrosome module is:
1. Technically functional (scripts, indices, HTML generation all working)
2. Methodologically sound (independent scoring, no nuclear bias)
3. Well-documented (audit trail, QA metrics, scoring policy)
4. Fully isolated from main atlas (zero pollution)

**Recommendation:** Proceed to full centrosome evaluation of all 716 seed genes, contingent on user approval.

---

## Pilot Score Summary

| Rank | Gene | Score | Status |
|:---:|------|:---:|--------|
| 1 | CETN2 | 76 | CENTROSOME_CANDIDATE |
| 2 | PLK4 | 63 | CENTROSOME_CANDIDATE |
| 3 | CEP192 | 63 | CENTROSOME_CANDIDATE |
| 4 | AURKA | 62 | CENTROSOME_LOW_PRIORITY |
| 5 | CCP110 | 62 | CENTROSOME_CANDIDATE |
| 6 | PCM1 | 62 | CENTROSOME_CANDIDATE |
| 7 | CEP97 | 62 | CENTROSOME_CANDIDATE |
| 8 | NEDD1 | 62 | CENTROSOME_CANDIDATE |
| 9 | CEP72 | 58 | CENTROSOME_CANDIDATE |
| 10 | CCDC14 | 26 | CENTROSOME_MANUAL_REVIEW |
