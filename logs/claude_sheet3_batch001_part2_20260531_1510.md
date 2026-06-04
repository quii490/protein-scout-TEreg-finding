# Sheet3 batch001 part2 supervision log

- Time: 2026-05-31 15:10 Asia/Shanghai
- Supervisor: Codex top-level; Claude Code middle agent used for packet-based draft reports.
- Input genes: OGFOD2, OGFOD3, FSAF1, NT5DC1, ABRACL
- Data packets: `/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/{gene}.json`

## Results

| Gene | Final class | Report path | Status | HPA IF status | Key notes |
|---|---|---|---|---|---|
| OGFOD2 | rejected | `detail/rejected/OGFOD2/OGFOD2-evaluation.md` | rejected | IF unavailable; only 60x60 thumbnail detected, no reliable original IF image | No UniProt/GO-CC nuclear evidence; PubMed strict=3; AlphaFold pLDDT 93.7; PDB none; STRING textmining only; IntAct Y2H/high-throughput |
| OGFOD3 | rejected | `detail/rejected/OGFOD3/OGFOD3-evaluation.md` | rejected | IF unavailable; only 60x60 thumbnail detected, no reliable original IF image | UniProt/GO-CC membrane; PubMed strict=5; AlphaFold pLDDT 85.5; PDB none; PPI supports membrane/ER/Golgi context |
| FSAF1 | nucleolus | `detail/nucleolus/FSAF1/FSAF1-evaluation.md` | scored | IF unavailable; HPA no reliable IF original image | UniProt/GO-CC experimental nucleolus/processome evidence; PubMed strict=0; PDB 7MQ8/7MQ9; AlphaFold pLDDT 68.1; STRING no data; IntAct/UniProt include NPM1/KAT5/CDC73-related interactions |
| NT5DC1 | rejected | `detail/rejected/NT5DC1/NT5DC1-evaluation.md` | rejected | IF unavailable; HPA page has non-standard images but no standard subcellular IF original | No UniProt/GO-CC nuclear evidence; PubMed strict=11; AlphaFold pLDDT 88.4; PDB none; IntAct mixed interactions without nuclear support |
| ABRACL | rejected | `detail/rejected/ABRACL/ABRACL-evaluation.md` | rejected | IF unavailable; only 60x60 thumbnail detected, no reliable original IF image | No nuclear evidence; function literature points to actin/cytoskeleton/cell migration; PubMed strict=12; PDB 2L2O; IntAct cytoskeleton/centrosome proximity partners |

## Supervision fixes

- Claude Code produced the five reports but stalled before logging and gate completion; stuck process was terminated by PID only.
- Corrected IF classification for OGFOD2, OGFOD3, and ABRACL: 60x60 thumbnails are not treated as acquired IF originals.
- Added explicit standard IF absence wording where needed: `暂无数据（HPA IF 原图未可靠获取），核定位基于 UniProt + GO-CC`.
- Added parseable rejected nuclear score rows for rejected reports.
- Added explicit FSAF1 PAE absence note because no PAE image file is present.

## Gate

- Targeted strict validation for all five genes: 0 errors, 0 warnings.
- Full gate: rebuilt summary to 1021 scored + 980 eliminated = 2001 total.
- Full strict validation: 0 errors, 402 historical warnings.
- Total table updated in `protein-finding.md`.

