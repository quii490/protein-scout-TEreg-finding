# Repair Round 1 Summary
**Date**: 2026-06-02 20:03:22

## Round Stats

| Metric | Value |
|---|---|
| Genes in round | 7 |
| Reports modified | 7 |
| Genes scored | 2 (AATF, AAGAB) |
| Genes rejected | 5 (AARS1, ABI1, ABLIM2, ATXN2L, C12orf60) |
| Classification changes | 0 (all preserved) |

## Modules Added Per Gene

| Gene | Modules Added |
|---|---|
| AATF | UniProt/GO-CC detail, PDB (3 structures), PubMed note, Literature (2 PMIDs), PPI (16 partners), Manual review note |
| AAGAB | PDB (3 structures), Literature (2 PMIDs), PPI table (6 partners), Manual review note |
| AARS1 | PDB (6 structures), Clarified rejection reason format |
| ABI1 | PDB (none), PubMed strict note, IntAct note |
| ABLIM2 | PubMed strict (19), PDB (none), STRING/IntAct note |
| ATXN2L | PubMed strict note, PDB (none) |
| C12orf60 | PDB (none), Score totals filled in |

## Gate Results

| Metric | Value |
|---|---|
| validate_strict.py --all Errors | 0 |
| validate_strict.py --all Warnings | 1998 |
| Targeted audit: missing HPA | 0 |
| Targeted audit: missing PubMed | 0 |
| Targeted audit: missing AlphaFold/PDB | 0 |
| Targeted audit: missing PPI | 0 |
| Reports shortened | 0 |
| Reports fully rewritten | 0 |
| Non-round genes modified | 0 |

## Remaining Warnings (minor format)

- AAGAB: PPI section should explicitly name IntAct/BioGrid + STRING
- AARS1/ABI1/ABLIM2: Rejection reason format (reports use "核定位特异性 N 分 → 淘汰" which is semantically correct but not parsed by validator regex)

## Git Diff

```
 .../nuclear-speckle/AAGAB/AAGAB-evaluation.md       | 14 ++++++++++++++
 .../detail/nucleoplasm/AATF/AATF-evaluation.md      | 21 ++++++++++++++++++++-
 .../detail/rejected/AARS1/AARS1-evaluation.md       |  3 ++-
 .../detail/rejected/ABI1/ABI1-evaluation.md         |  5 +++--
 .../detail/rejected/ABLIM2/ABLIM2-evaluation.md     |  5 ++++-
 .../detail/rejected/ATXN2L/ATXN2L-evaluation.md     |  6 +++++-
 .../detail/rejected/C12orf60/C12orf60-evaluation.md |  8 +++++---
 7 files changed, 53 insertions(+), 9 deletions(-)

```

## Files Modified

```
Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/AAGAB/AAGAB-evaluation.md
Projects/TEreg-finding/protein-interested/detail/nucleoplasm/AATF/AATF-evaluation.md
Projects/TEreg-finding/protein-interested/detail/rejected/AARS1/AARS1-evaluation.md
Projects/TEreg-finding/protein-interested/detail/rejected/ABI1/ABI1-evaluation.md
Projects/TEreg-finding/protein-interested/detail/rejected/ABLIM2/ABLIM2-evaluation.md
Projects/TEreg-finding/protein-interested/detail/rejected/ATXN2L/ATXN2L-evaluation.md
Projects/TEreg-finding/protein-interested/detail/rejected/C12orf60/C12orf60-evaluation.md

```
