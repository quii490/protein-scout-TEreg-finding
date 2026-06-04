# Sheet3 batch006a 执行日志

- **Time**: 2026-05-31 17:00–17:15
- **Input genes** (rows 38–42): ANKRD49, ANKRD50, ANKRD61, ANKRD62, ANKRD65
- **Harvest**: 4/5 OK; ANKRD50 PubMed timeout (non-DNS)

## 结果

| # | Gene | Class | Score | Key reason |
|---|---|---|---|---|
| 1 | ANKRD49 | nucleoplasm | 67.2 | GO nucleus IC + UniProt Nucleus ECO:0000250; low confidence |
| 2 | ANKRD50 | rejected | — | Endosome only; retromer STRING network |
| 3 | ANKRD61 | nucleoplasm | 69.4 | GO nucleoplasm IDA:HPA (direct experiment!); PubMed strict=0 |
| 4 | ANKRD62 | rejected | — | No location |
| 5 | ANKRD65 | rejected | — | No location; PubMed strict=0 |

## Highlights
- **ANKRD61**: GO nucleoplasm IDA:HPA — only ankyrin repeat protein in this region with direct experimental nuclear evidence. PubMed strict=0 (extremely novel).
- ANKRD49-ANKRD65 all ankyrin repeat proteins. ANKRD50 was the only one with non-nuclear primary localization (endosome).

## Gate
Targeted: 0E/0W (fixed IF absence statement + IntAct). Full: 0E/402W. Total: 1035+1001=2036.
