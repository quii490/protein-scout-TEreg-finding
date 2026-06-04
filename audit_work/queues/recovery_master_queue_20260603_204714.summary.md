# Recovery Master Queue Summary
**Date**: 2026-06-03 20:47:14

## Stats

| Metric | Count |
|---|---|
| Harvest gap genes | 635 |
| False rejection high-risk genes | 687 |
| Merged unique genes | 687 |
| Both reharvest + reevaluate | 635 |
| Reharvest only | 0 |
| Reevaluate only | 52 |
| Total batches | 138 |

## Priority Distribution

| Priority | Count | Description |
|---|---|---|
| P0 | 635 | Both HARVEST_GAP + FALSE_REJECTION |
| P1 | 34 | Rejected due to missing harvest OR HPA/UniProt/GO nuclear |
| P2 | 0 | Chromatin/RNA/DNA/PPI related |
| P3 | 0 | PubMed relevant |
| P4 | 18 | Other HIGH risk |
| P5 | 0 | Other |

## Batch 1 (first 5 genes)

- BCLAF1
- MIOS
- MIS18A
- MKKS
- MKLN1

## Files

- Harvest gap queue: audit_work/recovery_harvest_gap_queue_20260603_204714.tsv
- False rejection queue: audit_work/recovery_false_rejection_queue_20260603_204714.tsv
- Master queue: audit_work/recovery_master_queue_20260603_204714.tsv
