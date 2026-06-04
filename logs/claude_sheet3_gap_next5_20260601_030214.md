# Sheet3 Gap Next5 — Batch Log

**Batch**: CEP162, CEP164, C1orf94, C10orf62, C11orf21
**Source Sheet**: `研究很多` (Final_TE_finding.xlsx)
**Started**: 2026-06-01 03:02:14
**Agent**: Claude Code mid-level orchestrator

---

## Execution Summary

**Ended / audited by Codex**: 2026-06-01 03:18:36 CST

Claude Code completed harvest packets, image/PAE assets, and reports for all 5 genes, but stalled before writing per-gene log details. Codex stopped the stalled Claude process, fixed one parseability issue in `CEP162` (`交叉验证加分` -> `互证加分`), extended `validate_strict.py` to accept the standard HPA IF absence phrase, rebuilt the summary, and ran final gates.

## Per-Gene Results

| Gene | Excel row | Category | Report | HPA / IF status | PAE status | PubMed strict / novelty | PPI status | Audit |
|---|---:|---|---|---|---|---|---|---|
| CEP162 | 104 | nucleus-cytoplasm | `detail/nucleus-cytoplasm/CEP162/CEP162-evaluation.md` | HPA Approved; Nucleoplasm + Cytosol; 2 IF images embedded | PAE embedded | 11 / 10 | STRING + IntAct tables present | PASS |
| CEP164 | 105 | nucleus-cytoplasm | `detail/nucleus-cytoplasm/CEP164/CEP164-evaluation.md` | HPA Approved; primary cilium/centrosome main, nucleoplasm additional; 2 IF images embedded | PAE embedded | 73 / 4 | STRING/IntAct/GO-CC covered | PASS |
| C1orf94 | 121 | rejected | `detail/rejected/C1orf94/C1orf94-evaluation.md` | HPA Approved cytosol main + nucleoplasm additional; no IF display image; explicit absence note | PAE embedded | 0 / 10 | STRING + IntAct tables present | PASS; rejected for nuclear score 3 |
| C10orf62 | 122 | rejected | `detail/rejected/C10orf62/C10orf62-evaluation.md` | HPA Approved cytosol main + weak nucleoplasm additional; no IF display image; explicit absence note | PAE embedded | 0 / 10 | STRING + IntAct sections present | PASS; rejected for nuclear score 3 |
| C11orf21 | 123 | nucleoplasm | `detail/nucleoplasm/C11orf21/C11orf21-evaluation.md` | HPA Approved nucleoplasm main; IF original not reliably acquired; explicit absence note | PAE embedded | 3 / 10 | IntAct 0 + STRING partners reported | PASS |

## Gate Results

- Targeted strict validation: `python3 validate_strict.py --gene CEP162 --gene CEP164 --gene C1orf94 --gene C10orf62 --gene C11orf21`
  - Result: `Errors: 0; warnings: 0`
- Full gate: `python3 protein_gate.py --all`
  - Result: `Errors: 0; warnings: 280`
  - Rebuilt summary: `1085 scored + 1046 eliminated = 2131 total`
  - Warnings are historical: mainly older reports with PPI source coverage not explicit or rejected reason not machine-parseable. No hard errors.

## Summary Update

All 5 genes now appear in `protein-finding.md`:
- CEP162: nucleus-cytoplasm, 66.7
- CEP164: nucleus-cytoplasm, 50.8
- C11orf21: nucleoplasm, 67.2
- C1orf94: rejected
- C10orf62: rejected

Top summary statistics were rebuilt without quote-only blank-line accumulation.

## Process Notes

- The next unprocessed `研究很多` sheet rows after this batch start at row 124: `C11orf42`, `C11orf71`, `C11orf96`, `C12orf57`, `C12orf60`.
- For future Claude runs, require per-gene log writes immediately after each report. This run showed Claude can produce reports and assets, but still tends to postpone logging until the end.
