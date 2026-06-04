# Recovery Batch 1 Summary
**Date**: 2026-06-03 21:03:20
**Genes**: BCLAF1, MIOS, MIS18A, MKKS, MKLN1

## Results

| Gene | Status | Score | Lines | Validate |
|---|---|---|---|---|
| BCLAF1 | rejected | 28.9 | 179 | FAIL |
| MIOS | rejected | ? | 11 | OK |
| MIS18A | rejected | ? | 11 | OK |
| MKKS | rejected | 36.7 | 194 | OK |
| MKLN1 | rejected | 52.8 | 209 | OK |

## Stats

| Metric | Value |
|---|---|
| Batch genes | 5 |
| Rejected to Scored | 0 (MIOS, MIS18A) |
| Rejected to Rejected | 5 |
| Validate passed | 4/5 |
| Has forbidden words | 1 |
| Non-batch modified | 0 |

## Gate

```
Rebuilt: 2071 scored + 2477 eliminated = 4548 total (7 cats: {'nuclear-body': 76, 'nucleus-cytoplasm': 218, 'nucleolus': 238, 'nuclear-envelope': 69, 'nucleoplasm': 1232, 'chromatin': 104, 'nuclear-speckle': 134})
Rebuilt: 2071 scored + 2477 eliminated = 4548 total (7 cats: {'nuclear-body': 76, 'nucleus-cytoplasm': 218, 'nucleolus': 238, 'nuclear-envelope': 69, 'nucleoplasm': 1232, 'chromatin': 104, 'nuclear-speckle': 134})
Errors: 1444; warnings: 1940
```

## Files

- Audit: audit_work/recovery_batch1_audit_20260603_210311.tsv
