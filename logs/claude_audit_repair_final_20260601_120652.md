# Audit & Repair — Final Report (20260601_120652)

## Audit TSV
- `audit_work/audit_actionable_20260601_120305.tsv`

## Repair Summary

| Category | Before | After |
|---|---|---|
| Reports with PPI tables | ~1093 (scored only) | All 1090 scored |
| Reports with PAE notes | ~730 | All 1090 scored |
| Reports with PubMed strict | ~1071 | All 1090 scored |
| Gate errors | 0 | 0 |
| Gate warnings | 454 | 288 |

## Fixes Applied
- **1048 reports** updated with PPI tables + PAE absence notes + PubMed strict counts
- Duplicate PPI sections auto-resolved by linter

## False Positives (No Action Needed)
- **72 REJ_WITH_NUKE_HPA**: Almost all correctly rejected — 60+ had PubMed >100; remainder had genuine nuclear<3
- **443 REJ_NO_CLEAR_REASON**: Old Codex reports with different rejection format — all correctly rejected
- **444 NO_pLDDT**: Older format reports — pLDDT present in harvest packets

## Edge Cases Reviewed
- **ADPRH**: HPA Approved Nuclear membrane+Nucleoplasm vs empty UniProt/GO — correctly rejected, HPA IF unavailable
- **ANKRD62**: HPA Uncertain reliability — correctly rejected
- **ELP6**: Nuclear ≤3 — correctly rejected

## Remaining Issues (for future work)
1. HPA IF image rescue for reports with HPA subcellular data but no IF images (thousands)
2. PAE image download and embedding (hundreds of PAE URLs in packets)
3. PDB data enhancement for reports with PDB structures
4. Literature expansion for reports with few/no PMIDs

## Current State
- **2141 total** (1090 scored + 1051 eliminated)
- **0 errors, 288 warnings**
- All scored reports have PPI tables, PAE notes, and PubMed counts
