# Sheet3 batch004a 执行日志

- **Time**: 2026-05-31 15:55–16:05 Asia/Shanghai
- **Supervisor**: Claude Code main agent
- **Input genes** (Sheet3 rows 17–22, skip row 18 MOUSE_ONLY): ALG1L2, NPEPL1, AMMECR1, AMMECR1L, ANAPC15
- **Data packets**: `/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/{gene}.json`

## 角色审查记录

| 角色 | 结论 |
|---|---|
| Data Harvester | 5/5 harvested; AMMECR1L STRING HTTP 502 (server-side, non-DNS, proceedable) |
| Evidence Writer | 5 reports written from packets only |
| Localization Judge | 2 scored (nucleoplasm), 3 rejected |
| HPA IF Auditor | All 5 IF unavailable (60x60 thumbnails only, no original IF images) |
| Summary/Gate Agent | Targeted 0E/0W; Full 0E/402W (historical) |
| Final Audit | DNS check ✓; IF check ✓; total table updated ✓; no new warnings |

## 结果

| # | Gene | Class | Report | Status | HPA IF | PubMed s/b | PPI |
|---|---|---|---|---|---|---|---|
| 1 | ALG1L2 | rejected | `detail/rejected/ALG1L2/ALG1L2-evaluation.md` | rejected (0/10) | unavailable | 2/2 | Weak (STRING metabolic) |
| 2 | NPEPL1 | rejected | `detail/rejected/NPEPL1/NPEPL1-evaluation.md` | rejected (1/10) | unavailable (60x60) | 12/15 | Moderate (STRING + IntAct mixed) |
| 3 | AMMECR1 | nucleoplasm | `detail/nucleoplasm/AMMECR1/AMMECR1-evaluation.md` | scored (73.0) | unavailable (60x60) | 19/25 | HNRNPF co-IP; HOXA1 two-hybrid |
| 4 | AMMECR1L | rejected | `detail/rejected/AMMECR1L/AMMECR1L-evaluation.md` | rejected (2/10) | unavailable (60x60); STRING 502 | 3/3 | Limited (IntAct only) |
| 5 | ANAPC15 | nucleoplasm | `detail/nucleoplasm/ANAPC15/ANAPC15-evaluation.md` | scored (82.0) | unavailable (60x60) | 3/11 | Ultra-strong APC/C (15 STRING >0.99) |

## 分类理由

- **ALG1L2 → rejected**: UniProt 无定位; GO 仅 ER; putative glycosyltransferase.
- **NPEPL1 → rejected**: UniProt 无定位; GO nucleus HDA only (weak); cytoplasmic aminopeptidase function.
- **AMMECR1 → nucleoplasm**: UniProt Nucleus ECO:0000269; GO nucleoplasm IDA:HPA; protein name "Nuclear protein"; HNRNPF co-IP.
- **AMMECR1L → rejected**: UniProt 无定位; GO nucleus IBA only (paralog inference); no experimental localization.
- **ANAPC15 → nucleoplasm**: GO nucleoplasm TAS; APC/C mitotic E3 ligase; 18 PDB EM structures; ultra-strong PPI.

## Gate

- Targeted: 0 errors, 0 warnings
- Full: 0 errors, 402 historical warnings
- Total: 1029 scored + 987 eliminated = 2016

## 需要人工判断

- **AMMECR1L** 是 AMMECR1 的旁系同源物，共享 PF01871 结构域。如未来有实验定位数据支持核定位可重新评估。
- **ANAPC15** 归一化 82.0 为近期最高分之一，但核定位证据依赖 TAS:Reactome 而非 IDA，建议后续优先获取 HPA IF 原图。
