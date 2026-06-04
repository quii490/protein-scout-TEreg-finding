# Sheet3 batch004b 执行日志

- **Time**: 2026-05-31 16:07–16:15 Asia/Shanghai
- **Supervisor**: Claude Code main agent
- **Input genes** (Sheet3 rows 23–27): ANAPC16, ANKAR, ANKDD1A, ASB10, ASB13
- **Data packets**: `/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets/{gene}.json`

## 角色审查记录

| 角色 | 结论 |
|---|---|
| Data Harvester | 5/5 harvested; ALL OK (no DNS/URI failures) |
| Evidence Writer | 5 reports written from packets only |
| Localization Judge | 2 scored (ANAPC16 nucleoplasm, ASB10 nucleus-cytoplasm), 3 rejected |
| HPA IF Auditor | All 5 IF unavailable (60x60 thumbnails only or no IF images) |
| Summary/Gate Agent | Targeted 0E/0W; Full 0E/402W (historical) |
| Final Audit | DNS check ✓; IF check ✓; total table updated ✓; no new warnings |

## 结果

| # | Gene | Class | Report | Status | HPA IF | PubMed s/b | PPI |
|---|---|---|---|---|---|---|---|
| 1 | ANAPC16 | nucleoplasm | `detail/nucleoplasm/ANAPC16/ANAPC16-evaluation.md` | scored (86.6) | unavailable (no IF images) | 2/5 | Ultra-strong APC/C (14 STRING >0.99); 22 PDB |
| 2 | ANKAR | rejected | `detail/rejected/ANKAR/ANKAR-evaluation.md` | rejected (0/10) | unavailable (60x60) | 4/59 | Weak (STRING textmining) |
| 3 | ANKDD1A | rejected | `detail/rejected/ANKDD1A/ANKDD1A-evaluation.md` | rejected (0/10) | unavailable (60x60) | 5/6 | Very weak (STRING HIF1AN only) |
| 4 | ASB10 | nucleus-cytoplasm | `detail/nucleus-cytoplasm/ASB10/ASB10-evaluation.md` | scored (72.7) | unavailable (no IF images) | 11/13 | ECS E3 ligase (CUL5/ELOB/RNF7) |
| 5 | ASB13 | rejected | `detail/rejected/ASB13/ASB13-evaluation.md` | rejected (0/10) | unavailable (no IF images) | 6/12 | ECS E3 ligase (CUL5/ELOB/RNF7); IntAct TARDBP |

## 分类理由

- **ANAPC16 → nucleoplasm (86.6)**: UniProt experimental Nucleus + Chromosome/centromere/kinetochore (ECO:0000269); CENP-27 alias; 22 PDB structures; ultra-strong APC/C PPI. **最高分记录。**
- **ANKAR → rejected**: UniProt Membrane only (ECO:0000305); GO membrane IEA; 1434 aa large structural protein.
- **ANKDD1A → rejected**: UniProt 无定位; GO-CC 完全为空; death domain + ankyrin repeat protein of unknown function.
- **ASB10 → nucleus-cytoplasm (72.7)**: UniProt Cytoplasm + Nucleus (ECO:0000269); GO cytoplasm IDA + nucleus IDA; SOCS box E3 ligase.
- **ASB13 → rejected**: UniProt 无定位; GO 仅 cytosol; SOCS box family (paralog of ASB10 but no nuclear evidence).

## Gate

- Targeted: 0 errors, 0 warnings
- Full: 0 errors, 402 historical warnings
- Total: 1031 scored + 990 eliminated = 2021

## 2-Batch Audit (batch004a + batch004b)

| 检查项 | 状态 |
|---|---|
| DNS failure 残留 | 无（仅 AMMECR1L STRING 502 server-side, 非 DNS） |
| 60x60 缩略图误判 IF acquired | 无 — 全部正确标记 IF unavailable |
| 总表包含本批蛋白 | ✓ (2021 total covers both sub-batches) |
| 本批新增 strict warnings | 0 |
| 连续网络失败 | 无 |

## 需要人工判断

- **ANAPC16 (86.6)** 和 **ANAPC15 (82.0)** 同为 APC/C 小亚基，得分极高。两者的核定位证据均主要来自 UniProt 实验级 Nucleus + APC/C 功能背景，但 HPA IF 均 unavailable。建议批量补齐 HPA IF 原图。
- **ASB10 vs ASB13**: 同家族 SOCS box 蛋白，ASB10 有明确的实验级双定位（nucleus + cytoplasm IDA），ASB13 却无。可能反映真实的亚细胞定位分化，也可能 ASB13 尚未被充分研究。
