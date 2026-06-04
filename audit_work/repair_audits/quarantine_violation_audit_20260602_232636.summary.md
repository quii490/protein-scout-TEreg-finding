# Quarantine Violation Audit Summary
**Date**: 2026-06-02 23:26:36

## Scope

| Metric | Value |
|---|---|
| Target genes (KEEP_SCORED_DISCARD_REJECTED) | 10 |
| Stale rejected MOVE-ONLY target | 10 |
| Stale rejected actually moved | 10 |
| Canonical scored modified (VIOLATION) | **8** |
| Status changed (scored→rejected) | **2** |
| Content modified (scored→scored) | **6** |
| Unchanged (OK) | 2 (ABRAXAS1, ABRAXAS2) |
| Non-target genes modified | **0** |

## Violation Classification

### MUST_RESTORE_FROM_PRE_QUARANTINE (2)

| Gene | Problem |
|---|---|
| **AAAS** | Canonical scored (nuclear-envelope) was moved to rejected/ during quarantine. This status change was triggered by PubMed=596>100, but reclassification is OUT OF SCOPE for stale duplicate quarantine. The stale rejected was correctly quarantined but the canonical should NOT have been touched. |
| **ABTB3** | Canonical scored (nucleoplasm) was moved to rejected/ during quarantine. This status change was triggered by nuclear=3, but reclassification is OUT OF SCOPE for stale duplicate quarantine. The stale rejected was correctly quarantined. |

**Pre-quarantine source**: git commit `65887db4` (2026-06-02 22:25)

### REVIEW_PATCH_ONLY (6)

| Gene | Modification |
|---|---|
| AATF | Novelty score corrected (10→2), doubly escaped markdown fixed |
| ABITRAM | IF absence statement added (validator requirement) |
| AAMDC | Novelty/PAE/IF fixes from earlier scoring batch |
| ABLIM3 | Novelty/PAE/IF fixes from earlier scoring batch |
| ABTB2 | Novelty/PAE/IF fixes from earlier scoring batch |
| ACBD4 | Novelty/PAE/IF fixes from earlier scoring batch |

All 6 remain scored, no status/category change. Content changes are validator-driven fixes.

### OK_QUARANTINE_MOVE_ONLY (2)

| Gene | Status |
|---|---|
| ABRAXAS1 | Scored canonical untouched; stale rejected moved ✅ |
| ABRAXAS2 | Scored canonical untouched; stale rejected moved ✅ |

## Git Diff

```
git diff --stat 65887db4..HEAD -- detail/
```

Only files under detail/rejected/AAAS, detail/rejected/AATF, etc. show as deleted (quarantined stale).  
AAAS canonical (nuclear-envelope) + ABTB3 canonical (nucleoplasm) moved to rejected/.  
6 scored reports have minor content changes.

## Recommendations

1. **IMMEDIATE**: Restore AAAS to `detail/nuclear-envelope/AAAS/` (scored) from commit `65887db4`
2. **IMMEDIATE**: Restore ABTB3 to `detail/nucleoplasm/ABTB3/` (scored) from commit `65887db4`
3. **REVIEW**: 6 content-changed reports — likely benign but user should confirm
4. **CORRECT**: The stale rejected quarantining itself was performed correctly for all 10 genes

The root cause: validator errors (PubMed>100, nuclear≤3) triggered an automatic "fix" response during quarantine step, which violated the constraint that only stale rejected duplicates should be moved.
