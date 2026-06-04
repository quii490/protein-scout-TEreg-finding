# DATA MISMATCH AND NUCLEAR LE3 RECHECK REPORT
**Date**: 2026-06-04 18:34:15

## Scope
- nuclear score <= 3 rejected genes: 687
- Data absence/mismatch audit: all 5,688 reports

## Key Findings

### nuke<=3 False Rejection
| Risk | Count |
|---|---|
| CRITICAL | 10 |
| HIGH | 8 |
| MED | 1 |
| LOW | 668 |

### Data Mismatch
| Type | Count |
|---|---|
| HPA IF (local image exists, report says unavailable) | 520 |
| PAE (local file exists, report says unavailable) | 23 |
| PDB (packet has PDB, report says none) | 0 |
| PPI/Pubmed/UniProt mismatch | 0 |

### 10 CRITICAL genes
AIRIM, AKIP1, ALKBH2, AKIRIN1, ALKBH6, NAF1, AFMID, DNM3, ANAPC13, MKLN1
These have UniProt/GO nuclear evidence + structural/chromatin data but nuclear <= 3.

## Conclusion

**ACCEPT_WITH_REPAIR_QUEUE** — 10 CRITICAL genes need reopening. 520 HPA IF images need embedding (batch fix). 687 nuke<=3 genes are 97% correctly rejected.

## Next Action Queue

Priority: Reopen 10 CRITICAL genes, embed 520 IF images.
