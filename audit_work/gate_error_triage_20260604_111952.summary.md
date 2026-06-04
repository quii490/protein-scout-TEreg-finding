# Gate Error Triage
**Date**: 2026-06-04 11:19:57

## Distribution

| Category | Count | % |
|---|---|---|
| missing_IF_embed | 1394 | 67% |
| score_formula_mismatch | 436 | 21% |
| missing_PAE | 178 | 9% |
| other | 54 | 3% |
| nuclear<=3_bypass | 12 | 1% |

| **Total** | **2074** | **100%** |

## Origin Estimate

| Origin | Count | % |
|---|---|---|
| PRE_EXISTING (gen_all_180.py mass processing) | ~1762 | ~85% |
| VALIDATOR_RULE_COARSE | ~269 | ~13% |
| INTRODUCED_BY_RECOVERY | ~41 | ~2% |

## Key Categories
- score_formula_mismatch: 436 — gen_all_180.py uses different score format
- missing_IF_embed: 1394 — batch processing skipped IF embeds
- PubMed>100_bypass: 0 — gen_all_180.py may not enforce PubMed rules strictly
- nuclear<=3_bypass: 12 — same as above

## Recommendation

**FIX_REPORT** for formula mismatches + missing IF/PAE (can be automated).
**VALIDATOR_EXCEPTION** for legitimate PubMed>100 bypasses (alias collision cases).
**MANUAL_REVIEW** for nuclear<=3 bypasses (may indicate real false positives).
