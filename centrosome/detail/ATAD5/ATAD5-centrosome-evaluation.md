---
type: centrosome-protein-evaluation
gene: "ATAD5"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# ATAD5 — 中心体模块评估

## 1. 基本信息

- **基因:** ATAD5
- **Ensembl:** ENSG00000176208
- **HPA 来源:** 中心粒卫星
- **HPA 抗体:** HPA066823
- **IF 可靠性:** Approved
- **PubMed 文献总数:** 68 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000176208-ATAD5
- **HPA 定位:** Nucleoplasm, Cytokinetic bridge, Centriolar satellite
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Nucleoplasm, Cytokinetic bridge, Centriolar satellite。HPA IF 可靠性: approved。
来源: https://www.proteinatlas.org/ENSG00000176208-ATAD5/subcellular

![](https://images.proteinatlas.org/66823/1802_B10_2_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 68 篇
- **研究量评估:** 较多文献
- 1. PMID 32594826: ATAD5 suppresses centrosome over-duplication by regulating UAF1 and ID1. (2020 Aug) *Cell Cycle*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q96QE3)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q96QE3-F1-model_v6.pdb

*InterPro: AAA+_ATPase, ATPase_AAA_core, P-loop_NTPase*
*Pfam: AAA*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| RFC5 | 0.999 | 0.000 | 0.000 | 0.000 |
| RFC1 | 0.999 | 0.000 | 0.000 | 0.000 |
| RFC4 | 0.999 | 0.000 | 0.000 | 0.000 |
| PCNA | 0.999 | 0.000 | 0.000 | 0.000 |
| RFC3 | 0.999 | 0.000 | 0.000 | 0.000 |
| RAD17 | 0.999 | 0.000 | 0.000 | 0.000 |
| ATAD5 | 0.999 | 0.000 | 0.000 | 0.000 |
| RFC4 | 0.999 | 0.000 | 0.000 | 0.000 |
| RFC3 | 0.999 | 0.000 | 0.000 | 0.000 |
| RFC4 | 0.999 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 14/20 | HPA 标注 |
| PubMed/文献 | 6/20 | 68 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 4/10 | 中等研究量 |

- **最终评分:** **59/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心粒卫星
- 抗体: HPA066823（IF 可靠性: Approved）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
