# FULL_REEVALUATE Pause and Diagnosis
**Date**: 2026-06-03 20:39:59

## 1. Can FULL_REEVALUATE be accepted as complete?

**NO.** While all 1,360 queue genes have reports, quality is insufficient:

| Issue | Severity |
|---|---|
| 687 HIGH false rejection risks | 🔴 Requires reopening |
| 71% quality failure in sample (89 genes) | 🔴 Widespread quality issues |
| 635 missing harvest packets | 🟡 Blocks complete evaluation |
| 1,443 gate errors | 🔴 Format/validation issues |
| 3,186 non-queue genes processed | 🟡 Scope creep (mostly pre-existing) |

## 2. Actual vs Queue Gene Count

| Metric | Value |
|---|---|
| Queue genes (FULL_REEVALUATE) | 1,360 |
| Queue processed (have reports) | 1,360 (100%) |
| Non-queue genes processed | 3,186 |
| Of non-queue: in original recovery plan | 292 |
| Of non-queue: NOT in recovery plan | 2,894 (pre-existing reports) |

**Conclusion**: Queue is 100% covered. Non-queue genes are pre-existing reports from earlier project phases, NOT from current processing.

## 3. Scope Violations

| Type | Count |
|---|---|
| DELETE genes processed | 7 |
| MANUAL_REVIEW genes processed | 47 |
| Multi-scored conflict genes processed | Included in above |

These are from the gen_all_180.py batch processor which processed ALL genes with harvest packets, not just queue genes.

## 4. Harvest Gap

| Metric | Count |
|---|---|
| Queue genes without harvest packets | 635 |
| Has report but no packet | 635 |
| Rejected due to missing harvest | 635 |

These 635 genes have THIN rejected reports that need proper evaluation after harvest.

## 5. False Rejection Risk

| Risk Level | Count |
|---|---|
| CRITICAL | 0 |
| HIGH | 687 |
| MED | 0 |
| LOW | 16 |

687 HIGH-risk genes have nuclear evidence in their harvest packets (HPA/UniProt/GO) but were placed in rejected/ with thin reports. Many may be genuine nuclear proteins that the mass-batch processing did not properly evaluate.

## 6. Sample Quality

| Metric | Value |
|---|---|
| Sampled | 89 (50 rejected + 20 scored + 19 short) |
| Quality pass | 26 (29%) |
| Quality fail | 63 (71%) |

Primary failure modes: missing PPI/PDB/HPA sections, template reports (<25 lines).

## 7. Remaining Templates

| Type | Count |
|---|---|
| ≤12 line templates | 1,189 |
| Packet error in text | 1,899 |
| No nuclear evidence shorthand | 1,899 |

Many are from pre-existing reports, not just FULL_REEVALUATE.

## 8. Gate Status

| Metric | Value |
|---|---|
| Errors | 1,443 |
| Warnings | 1,939 |

High error count from format differences between gen_all_180.py output and validate_strict.py expectations.

## 9. Recommendations

### IMMEDIATE: DO NOT continue FULL_REEVALUATE

### Recommended next steps (in order):

1. **REOPEN_FALSE_REJECTION_RISK**: 687 HIGH-risk genes need proper evaluation after re-harvest
2. **CONTINUE_HARVEST_ONLY**: 635 genes need harvest data (network-intensive)
3. **FIX_GATE_ERRORS**: 1,443 format errors from gen_all_180.py need systematic fix
4. **AUDIT_NON_QUEUE**: Verify 3,186 non-queue genes are pre-existing, not overwritten

### Genes requiring reopening:
- 687 HIGH-risk rejected genes (see `full_reevaluate_false_rejection_risk_audit_*.tsv`)
- These have nuclear evidence in packets but thin rejected reports

### Genes only waiting for harvest:
- 635 genes (see `full_reevaluate_harvest_gap_audit_*.tsv`)
- Already have thin reports, need proper evaluation after packet data

### Scope risk genes:
- 7 DELETE genes were processed
- 47 MANUAL_REVIEW genes were processed
- These need verification they weren't overwritten

## 10. Decision

**Recommendation: REOPEN_FALSE_REJECTION_RISK + CONTINUE_HARVEST_ONLY**

- Do NOT accept current state as complete
- Minimum next step: harvest 635 genes, then reopen 687 HIGH-risk genes
- Estimated effort: ~5 hours harvest + 2 hours re-evaluation

## Files Generated

| Step | File |
|---|---|
| Snapshot | audit_work/full_reevaluate_progress_snapshot_20260603_203549.tsv |
| Queue audit | audit_work/full_reevaluate_queue_consistency_audit_20260603_203649.tsv |
| Harvest gap | audit_work/full_reevaluate_harvest_gap_audit_20260603_203823.tsv |
| False rejection | audit_work/full_reevaluate_false_rejection_risk_audit_20260603_203855.tsv |
| Sample quality | audit_work/full_reevaluate_sample_quality_audit_20260603_203926.tsv |
