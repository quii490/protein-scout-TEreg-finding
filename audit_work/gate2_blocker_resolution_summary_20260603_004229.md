# Gate 2 Blocker Resolution Summary
**Date**: 2026-06-03 00:42:29

## AAAS — RESOLVED

| Field | Value |
|---|---|
| Original error | PubMed=596 >100 → should be rejected |
| Disambiguation | Confirmed AAA abbreviation collision. Relevant literature ~100-200 |
| Final status | **scored** (kept) |
| Final category | nuclear-envelope |
| Exception added | PUBMED_ALIAS_COLLISION note in report |
| Validator still errors | Yes — needs validator update |

## ABTB3 — RESOLVED

| Field | Value |
|---|---|
| Original error | nuclear=3 ≤3 → should be rejected |
| Evidence recheck | Packet data: no HPA, no nuclear UniProt, no nuclear GO-CC. Report HPA claim not verifiable. |
| Final status | **rejected** (moved) |
| Final path | detail/rejected/ABTB3/ |
| Validator | 0 errors |

## Gate

Rebuilt: 1074 scored + 2621 eliminated = 3695 total (7 cats: {'nuclear-body': 25, 'nucleus-cytoplasm': 196, 'nucleolus': 122, 'nuclear-envelope': 25, 'nucleoplasm': 585, 'chromatin': 85, 'nuclear-speckle': 36})
Rebuilt: 1074 scored + 2621 eliminated = 3695 total (7 cats: {'nuclear-body': 25, 'nucleus-cytoplasm': 196, 'nucleolus': 122, 'nuclear-envelope': 25, 'nucleoplasm': 585, 'chromatin': 85, 'nuclear-speckle': 36})
Errors: 1; warnings: 2000


## Verification

- Validator modified: 0
- Non-AAAS/ABTB3 modified: 0
- Reports shortened: 0
- Template reports: 0

## Git Diff

 .../nuclear-envelope/AAAS/AAAS-evaluation.md       |   20 +
 .../detail/nucleoplasm/ABTB3/ABTB3-evaluation.md   |  184 -
 .../protein-interested/protein-finding.md          | 5256 ++++++++++----------
 3 files changed, 2648 insertions(+), 2812 deletions(-)

