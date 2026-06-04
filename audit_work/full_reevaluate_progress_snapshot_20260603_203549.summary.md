# FULL_REEVALUATE Progress Snapshot
**Date**: 2026-06-03 20:36:18

## Key Metrics

| Metric | Value |
|---|---|
| Original FULL_REEVALUATE in recovery plan | 1370 |
| Queue genes (batches) | 1360 in 272 batches |
| Total reports | 4546 |
| /180 complete reports | 2184 |
| Scored | 2069 |
| Rejected | 2477 |
| Harvest packets | 1988 |
| Queue processed | 0/1360 |
| Queue needs harvest | 635 |
| **Non-queue genes processed** | **3186** ⚠️ |
| MANUAL_REVIEW conflicts processed | 47 |
| ≤12L templates | 634 |
| 13-24L thin | 94 |
| 25-49L medium | 913 |
| ≥50L good | 2905 |
| Packet error in text | 0 |
| No nuclear evidence shorthand | 0 |
| Forbidden placeholder words | 673 |
| Gate errors | 1443 |
| Gate warnings | 1939 |

## Critical Findings

- **3186 genes were processed that are NOT in the FULL_REEVALUATE queue** — possible scope violation
- **635 queue genes still lack harvest data** — cannot be evaluated
- **634 template reports (<12 lines) still exist** — quality gap
- **1443 validation errors** — need investigation

## Files

- Snapshot TSV: audit_work/full_reevaluate_progress_snapshot_20260603_203549.tsv
- Latest batch queue: audit_work/full_reevaluate_batches_20260603_005337.tsv
