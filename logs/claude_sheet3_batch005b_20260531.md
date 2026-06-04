# Sheet3 batch005b 执行日志

- **Time**: 2026-05-31 16:25–16:35
- **Input genes** (Sheet3 rows 33–37): ANKRD36C, ANKRD39, ANKRD40, ANKRD42, ANKRD44
- **Harvest**: 4/5 OK; ANKRD36C STRING SSL EOF error (intermittent, all other sources OK)

## 结果

| # | Gene | Class | Key reason |
|---|---|---|---|
| 1 | ANKRD36C | rejected | No location; pLDDT 51.3; STRING SSL error |
| 2 | ANKRD39 | rejected | No location (0/10); PubMed strict=1 |
| 3 | ANKRD40 | rejected | No location; STRING SEC13/SAR1A COPII (ER) |
| 4 | ANKRD42 | rejected | GO nucleus IBA only (2/10 ≤3); SFRP Wnt network |
| 5 | ANKRD44 | rejected | No location despite strong PPP6 PPI (>0.9); PubMed 14 |

## Gate
Targeted: 0E/0W. Full: 0E/402W. Total: 1033+998=2031.

## Note
This batch was entirely rejected — all 5 ankyrin repeat proteins lacked nuclear localization evidence. ANKRD42 had a sole GO nucleus IBA annotation (≤3 threshold). ANKRD44 had the strongest PPI (PPP6R1/PPP6C/PPP6R2 >0.9) of any rejected protein but no location data.
