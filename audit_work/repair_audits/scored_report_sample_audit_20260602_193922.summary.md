# Scored Report Sample Audit Summary
**Date**: 2026-06-02 19:39:22
**Source**: audit_work/scored_report_sample_audit_20260602_193922.tsv

## Sample Overview

| Metric | Value |
|---|---|
| Total scored in quality audit | 607 |
| Sample size | 80 (60 random + 20 high-risk) |
| Needs repair | 2 |
| Repair ratio | 2.5% |

## Missing Core Modules

| Module | Missing Count | Missing % |
|---|---|---|
| HPA / IF | 0 | 0.0% |
| PubMed | 1 | 1.2% |
| AlphaFold/pLDDT/PAE | 0 | 0.0% |
| PDB / no-PDB explanation | 7 | 8.8% |
| PPI | 0 | 0.0% |
| Key Literature | 3 | 3.8% |
| Final Decision Reason | 1 | 1.2% |

## Repair Priority Distribution

| Priority | Count |
|---|---|
| HIGH | 1 |
| MED | 1 |
| LOW | 7 |
| OK | 71 |

## Trust Recommendation

| Question | Answer |
|---|---|
| Should we trust the remaining scored reports? | **YES** |
| Repair ratio | 2.5% |
| Recommendation | Proceed with confidence — most scored reports are complete |

## Worst Scored Reports (needs_repair=True)

| Gene | Lines | Missing Modules |
|---|---|---|
| AATF | 517 | UniProt/GO, PubMed, PDB, Literature |
| AAGAB | 965 | PDB, Literature |
