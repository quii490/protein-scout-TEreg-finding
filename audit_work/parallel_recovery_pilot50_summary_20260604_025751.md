# Parallel Recovery Pilot50 Summary
**Date**: 2026-06-04 02:57:51

## Results

| Metric | Value |
|---|---|
| Pilot genes | 50 |
| Harvest success | 50/50 (100%) |
| Staged reports | 50/50 (100%) |
| QA PASS | 35/50 (70%) |
| Committed to detail/ | 35 |
| New scored | 31 |
| New rejected | 4 |
| Avg report size | 153 lines |
| Workers used | 4 eval + 2 harvest |

## Worker Performance

| Worker | Total | Pass | Pass% |
|---|---|---|---|
| worker_W1 | 13 | 12 | 92% |
| worker_W2 | 13 | 11 | 85% |
| worker_W3 | 12 | 9 | 75% |
| worker_W4 | 12 | 3 | 25% |

## QA Failure Reasons

| Issue | Count |
|---|---|
| Missing HPA | 9 |
| Missing PDB | 1 |
| Forbidden words | 0 |

## Key Findings

- Harvest parallelization worked: 50 genes in ~26s average
- Evaluation parallelization: 4 workers completed in parallel
- 15 QA failures mostly from REJECTED genes missing HPA/PDB sections
- 0 forbidden placeholder words found
- No concurrent write conflicts
- No lock violations

## Recommendation

✅ **Continue parallel loop** — pipeline works. QA failures need HPA/PDB section improvements in rejected reports.

## Files

- Queue: audit_work/parallel_recovery_queue_20260604_013811.tsv
- QA: audit_work/parallel_recovery_pilot50_qa_20260604_025720.tsv
