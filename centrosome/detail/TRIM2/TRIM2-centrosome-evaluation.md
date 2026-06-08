---
type: centrosome-protein-evaluation
gene: "TRIM2"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# TRIM2 — 中心体模块评估

## 1. 基本信息

- **基因:** TRIM2
- **Ensembl:** ENSG00000109654
- **HPA 来源:** 中心体
- **HPA 抗体:** HPA035853, HPA035854
- **IF 可靠性:** Uncertain
- **PubMed 文献总数:** 93 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000109654-TRIM2
- **HPA 定位:** Centrosome
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Centrosome。HPA IF 可靠性: uncertain。
来源: https://www.proteinatlas.org/ENSG00000109654-TRIM2/subcellular

![](https://images.proteinatlas.org/35854/569_A5_2_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体 定位。

## 4. PubMed 文献证据

- **文献总数:** 93 篇
- **研究量评估:** 较多文献
- *PubMed 文献待查询*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q9C040)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q9C040-F1-model_v6.pdb

*InterPro: 6-blade_b-propeller_TolB-like, Bbox_C, Filamin/ABP280_repeat-like, Filamin/ABP280_rpt, Ig-like_fold, Ig_E-set, NHL_repeat, TRIM-NHL_E3_ligases*
*Pfam: Filamin, NHL, zf-B_box, zf-RING_UBOX*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| UBE2D1 | 0.993 | 0.000 | 0.000 | 0.000 |
| NEFL | 0.724 | 0.000 | 0.000 | 0.000 |
| TRIM3 | 0.709 | 0.000 | 0.000 | 0.000 |
| SIRPA | 0.674 | 0.000 | 0.000 | 0.000 |
| TRIM2 | 0.666 | 0.000 | 0.000 | 0.000 |
| LRRC8E | 0.650 | 0.000 | 0.000 | 0.000 |
| UBE2D1 | 0.627 | 0.000 | 0.000 | 0.000 |
| TRIM3 | 0.622 | 0.000 | 0.000 | 0.000 |
| TRIM3 | 0.621 | 0.000 | 0.000 | 0.000 |
| TRIM44 | 0.608 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 16/20 | HPA 标注 |
| PubMed/文献 | 6/20 | 93 篇文献 |
| PPI/互作网络 | 15/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 4/10 | 中等研究量 |

- **最终评分:** **59/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体
- 抗体: HPA035853, HPA035854（IF 可靠性: Uncertain）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
