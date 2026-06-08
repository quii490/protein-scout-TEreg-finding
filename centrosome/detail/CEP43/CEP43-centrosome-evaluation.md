---
type: centrosome-protein-evaluation
gene: "CEP43"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# CEP43 — 中心体模块评估

## 1. 基本信息

- **基因:** CEP43
- **Ensembl:** ENSG00000213066
- **HPA 来源:** 中心体+中心粒卫星
- **HPA 抗体:** HPA071876
- **IF 可靠性:** Supported
- **PubMed 文献总数:** 26 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体+中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000213066-CEP43
- **HPA 定位:** Centriolar satellite, Centrosome, Basal body
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Centriolar satellite, Centrosome, Basal body。HPA IF 可靠性: supported。
来源: https://www.proteinatlas.org/ENSG00000213066-CEP43/subcellular

![](https://images.proteinatlas.org/71876/1406_B3_7_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体+中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 26 篇
- **研究量评估:** 低研究量
- 1. PMID 38991980: Architecture of RabL2-associated complexes at the ciliary base: A structural modeling perspective: Deciphering the structural organization of ciliary RabL2 complexes. (2024 Sep) *Bioessays*
2. PMID 23554904: FOP is a centriolar satellite protein involved in ciliogenesis. (2013) *PLoS One*
3. PMID 26905588: Polymorphisms of the centrosomal gene (FGFR1OP) and lung cancer risk: a meta-analysis of 14,463 cases and 44,188 controls. (2016 Mar) *Carcinogenesis*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: O95684)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-O95684-F1-model_v6.pdb

*InterPro: FOP_dimerisation-dom_N, LisH*
*Pfam: FOP_dimer*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| FGFR1OP | 0.994 | 0.000 | 0.000 | 0.000 |
| PPP2CA | 0.994 | 0.000 | 0.000 | 0.000 |
| PPP2CA | 0.986 | 0.000 | 0.000 | 0.000 |
| CEP350 | 0.977 | 0.000 | 0.000 | 0.000 |
| CEP19 | 0.952 | 0.000 | 0.000 | 0.000 |
| PPP2R3C | 0.891 | 0.000 | 0.000 | 0.000 |
| FGFR1 | 0.886 | 0.000 | 0.000 | 0.000 |
| RNASET2 | 0.885 | 0.000 | 0.000 | 0.000 |
| CEP19 | 0.877 | 0.000 | 0.000 | 0.000 |
| MYO18A | 0.869 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 18/20 | HPA 双来源标注（中心体 + 中心粒卫星）。定位: Centriolar satellite, Centrosome, Basal body |
| PubMed/文献 | 8/20 | 26 篇文献 |
| PPI/互作网络 | 15/20 | STRING 互作数据 |
| 结构/结构域 | 5/10 | 待结构数据采集 |
| 新颖性/特异性 | 8/10 | 低研究量 |

- **最终评分:** **67/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体+中心粒卫星
- 抗体: HPA071876（IF 可靠性: Supported）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
