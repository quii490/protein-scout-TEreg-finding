# Sheet3 Gap Next5b — Batch Log

**Batch**: C11orf42, C11orf71, C11orf96, C12orf57, C12orf60
**Source Sheet**: `研究很多` (Final_TE_finding.xlsx)
**Started**: 2026-06-01 03:03:00
**Completed**: 2026-06-01 03:30:00
**Agent**: Claude Code main agent

---

## Per-Gene Results

| Gene | Excel row | Category | Report | Rejected | HPA / IF status | PAE status | PubMed strict / novelty | PPI status | Targeted strict |
|---|---|---|---|---|---|---|---|---|---|
| C11orf42 | 124 | rejected | `detail/rejected/C11orf42/C11orf42-evaluation.md` | nuclear<=3 | HPA Approved; main=Plasma membrane, additional=Nuclear membrane; 2 IF display images embedded (A-431, U-2 OS) | PAE embedded (v6, 87KB) | 4 / 10 | IntAct: SNX2/SNX5 co-IP; STRING: 11 partners | PASS (0 errors) |
| C11orf71 | 125 | nucleoplasm | `detail/nucleoplasm/C11orf71/C11orf71-evaluation.md` | No | HPA Approved; main=Nucleoplasm, additional=Nuclear bodies; no IF display image; explicit HPA IF absence note | PAE embedded (v6, 65KB) | 0 / 10 | IntAct: TPPP2/MNAT1/USP34/NACC2 co-IP (Cell 2021); STRING: 15 partners textmining-only | PASS (0 errors) |
| C11orf96 | 126 | nucleus-cytoplasm | `detail/nucleus-cytoplasm/C11orf96/C11orf96-evaluation.md` | No | HPA Approved; main=Nucleoplasm+Cytosol (dual); no IF display image; explicit HPA IF absence note | PAE embedded (v6, 72KB) | 5 / 10 | IntAct: 0; STRING: 3 partners textmining-only | PASS (0 errors) |
| C12orf57 | 127 | nuclear-speckle | `detail/nuclear-speckle/C12orf57/C12orf57-evaluation.md` | No | HPA Enhanced; main=Nuclear speckles; no IF display image; explicit HPA IF absence note | PAE embedded (v6, 72KB) | 11 / 10 | IntAct: 12 partners (ANKK1 Y2H dual-source confirmed); STRING: ANKRD50 0.994 exp | PASS (0 errors) |
| C12orf60 | 128 | rejected | `detail/rejected/C12orf60/C12orf60-evaluation.md` | nuclear<=3 | HPA Approved; main=Cytosol, additional=Nucleoplasm; 2 IF display images embedded (A-431, U-2 OS) | PAE embedded (v6, 89KB) | 0 / 10 | IntAct: ERP27 Y2H, BMP4 MAPPIT; STRING: 7 partners | PASS (0 errors) |

---

## Scoring Summary

| Gene | Nuclear | Size | Novelty | Structure | Domain | PPI | Cross | Raw | Norm | Category |
|---|---|---|---|---|---|---|---|---|---|---|
| C12orf57 | 9 | 8 | 10 | 8 | 7 | 6 | +1.0 | 151 | 82.5 | nuclear-speckle |
| C11orf71 | 7 | 8 | 10 | 6 | 7 | 6 | 0.0 | 136 | 74.3 | nucleoplasm |
| C11orf96 | 6 | 8 | 10 | 6 | 7 | 2 | 0.0 | 120 | 65.6 | nucleus-cytoplasm |
| C11orf42 | 2 | 10 | 10 | 6 | 7 | 4 | 0.0 | — | — | rejected |
| C12orf60 | 2 | 10 | 10 | 8 | 7 | 4 | 0.0 | — | — | rejected |

---

## Gate Results

- **Targeted strict**: All 5 genes passed `validate_strict.py --gene <GENE>` with 0 errors each.
- **Full gate**: `python3 protein_gate.py --all`
  - `Errors: 0; warnings: 280`
  - Rebuilt summary: `1088 scored + 1048 eliminated = 2136 total`
  - Warnings are all historical. No new warnings from this batch.
- **Summary categories**: nuclear-body: 25, nucleus-cytoplasm: 194, nucleolus: 126, nuclear-envelope: 24, nucleoplasm: 598, chromatin: 86, nuclear-speckle: 35

---

## Rejected List
- C11orf42: nuclear score 2 (HPA main=Plasma membrane; nuclear membrane only additional)
- C12orf60: nuclear score 2 (HPA main=Cytosol; nucleoplasm only additional)

---

## Notes
- No species-restriction issues in this batch (all human genes with UniProt reviewed entries).
- C11orf71, C11orf96, C12orf57 had no IF display images (blue_red_green.jpg) — HPA absences were properly noted.
- C12orf57 was the strongest candidate: HPA Enhanced nuclear speckles, AlphaFold pLDDT 80.0, rich PPI with ANKK1 dual-source confirmation.
