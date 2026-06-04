# PROTOCOL RECHECK FINAL REPORT
**Date**: 2026-06-04 17:23:46

## 1. Overall Status

| Metric | Value |
|---|---|
| Excel coverage | 4756/4756 = 100% |
| Missing genes | 0 |
| Total reports | 5770 |
| Scored | 3154 |
| Rejected | 2616 |
| /180 reports | 3969 |
| Harvest packets | 3655 |

## 2. Quality Issues

| Issue | Count |
|---|---|
| CRITICAL incomplete reports | 81 |
| HIGH incomplete reports | 786 |
| Short reports (<50L) | 1080 |
| Forbidden placeholders | 235 |
| Packet error in text | 0 |
| Data absence mismatch | 559 |
| CRITICAL false rejection | 57 |
| HIGH false rejection | 707 |
| Duplicates | 153 |
| Gate errors | 2573 |

## 3. Gate Error Types

| Type | Count |
|---|---|
| MISSING_IF_EMBED | 1843 |
| SCORE_FORMULA_MISMATCH | 486 |
| MISSING_PAE | 178 |
| OTHER | 54 |
| NUCLEAR_LE3_BUT_SCORED | 12 |

## 4. Acceptance Decision

**DO_NOT_ACCEPT_NEEDS_REPAIR**

57 CRITICAL false rejection risks remain. These are rejected genes with nuclear evidence in packets but thin reports. Recommend reopen before accepting.

## 5. Next Actions

| Priority | Task | Count |
|---|---|---|
| P0 | Fix 81 CRITICAL incomplete + 57 CRITICAL false rejection | 138 |
| P1 | Fix 786 HIGH incomplete reports | 786 |
| P2 | Resolve 153 duplicates | 153 |
| P3 | Gate error cleanup | 2573 |
