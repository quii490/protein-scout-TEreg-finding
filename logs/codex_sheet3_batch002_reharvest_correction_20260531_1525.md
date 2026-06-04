# Sheet3 batch002 reharvest correction log

- Time: 2026-05-31 15:25 Asia/Shanghai
- Supervisor: Codex top-level
- Input genes: ANP32D, ACBD6, ACYP1, ACYP2, AP5S1

## Correction reason

The first batch002 reports were generated from packets harvested without network access. Those packets contained DNS/URLError failures for all sources and produced invalid all-rejected reports. I re-ran `protein_scout_harvest.py` with network permission and confirmed all five new packets have `ok=True` for UniProt, HPA, AlphaFold, STRING, IntAct, and PubMed. The invalid DNS-failure reports were overwritten.

## Final results

| Gene | Final class | Report path | Status | HPA IF status | Decision |
|---|---|---|---|---|---|
| ANP32D | nucleoplasm | `detail/nucleoplasm/ANP32D/ANP32D-evaluation.md` | scored | IF unavailable; HPA has only non-original 60x60 thumbnails | Kept as low-confidence nuclear candidate due ANP32 nuclear phosphoprotein naming and PMID:26112988; UniProt/GO/HPA IF evidence absent |
| ACBD6 | nucleus-cytoplasm | `detail/nucleus-cytoplasm/ACBD6/ACBD6-evaluation.md` | scored | IF unavailable; no reliable original IF image | Kept; UniProt and GO-CC provide experimental nucleus + cytoplasm evidence |
| ACYP1 | rejected | `detail/rejected/ACYP1/ACYP1-evaluation.md` | rejected | IF unavailable; no reliable original IF image | Rejected; no UniProt/GO nuclear evidence |
| ACYP2 | rejected | `detail/rejected/ACYP2/ACYP2-evaluation.md` | rejected | IF unavailable; only 60x60 IF thumbnail, no original IF image | Rejected; no reliable nuclear evidence, GO points to mitochondrion |
| AP5S1 | nucleus-cytoplasm | `detail/nucleus-cytoplasm/AP5S1/AP5S1-evaluation.md` | scored | IF unavailable; no reliable original IF image | Kept as low-medium confidence; GO nucleoplasm IDA:HPA and DNA repair annotation, but main UniProt/PPI signal is endosome/lysosome/AP-5 |

## PubMed and PPI summary

| Gene | PubMed strict/broad | PPI coverage |
|---|---:|---|
| ANP32D | 1 / 7 | STRING textmining only; IntAct none |
| ACBD6 | 21 / 25 | Strong NMT1/NMT2 support across UniProt, STRING, IntAct |
| ACYP1 | 13 / 19 | STRING metabolic/database network; IntAct 1 record |
| ACYP2 | 39 / 72 | STRING metabolic/database network; IntAct high-throughput records |
| AP5S1 | 0 / 0 | Strong AP-5 complex support across STRING and IntAct |

## Gate

- Targeted strict validation for these five genes: 0 errors, 0 warnings.
- Full gate: 1024 scored + 982 eliminated = 2006 total.
- Full strict validation: 0 errors, 402 historical warnings.
- Total table updated in `protein-finding.md`.

