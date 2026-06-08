---
type: centrosome-protein-evaluation
gene: "RTTN"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# RTTN — 中心体模块评估

## 1. 基本信息

- **基因:** RTTN
- **Ensembl:** ENSG00000176225
- **HPA 来源:** 中心体
- **HPA 抗体:** HPA041343, HPA041967, HPA075089
- **IF 可靠性:** Uncertain
- **PubMed 文献总数:** 38 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000176225-RTTN
- **HPA 定位:** Centrosome, Basal body, Cytosol
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Centrosome, Basal body, Cytosol。HPA IF 可靠性: uncertain。
来源: https://www.proteinatlas.org/ENSG00000176225-RTTN/subcellular

![](https://images.proteinatlas.org/75089/1914_B4_19_cr5c866b98464b5_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体 定位。

## 4. PubMed 文献证据

- **文献总数:** 38 篇
- **研究量评估:** 中等研究量
- 1. PMID 39680576: A Taybi-Linder syndrome-related RTTN variant impedes neural rosette formation in human cortical organoids. (2024 Dec) *PLoS Genet*
2. PMID 38796459: 9-fold symmetry is not essential for centriole elongation and formation of new centriole-like structures. (2024 May 25) *Nat Commun*
3. PMID 30879067: Heterogeneous clinical phenotypes and cerebral malformations reflected by rotatin cellular dynamics. (2019 Apr 1) *Brain*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q86VV8)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q86VV8-F1-model_v6.pdb

*InterPro: ARM-like, ARM-type_fold, Rotatin, Rotatin_N*
*Pfam: RTTN_N*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| STIL | 0.963 | 0.000 | 0.000 | 0.000 |
| CEP295 | 0.936 | 0.000 | 0.000 | 0.000 |
| CEP192 | 0.910 | 0.000 | 0.000 | 0.000 |
| CEP192 | 0.859 | 0.000 | 0.000 | 0.000 |
| WDR62 | 0.858 | 0.000 | 0.000 | 0.000 |
| CEP192 | 0.856 | 0.000 | 0.000 | 0.000 |
| RTTN | 0.850 | 0.000 | 0.000 | 0.000 |
| CEP120 | 0.785 | 0.000 | 0.000 | 0.000 |
| WDR62 | 0.772 | 0.000 | 0.000 | 0.000 |
| POC5 | 0.757 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 16/20 | HPA 中心体标注。定位: Centrosome, Basal body, Cytosol |
| PubMed/文献 | 7/20 | 38 篇文献 |
| PPI/互作网络 | 15/20 | STRING 互作数据 |
| 结构/结构域 | 5/10 | 待结构数据采集 |
| 新颖性/特异性 | 6/10 | 中等研究量 |

- **最终评分:** **61/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心体
- 抗体: HPA041343, HPA041967, HPA075089（IF 可靠性: Uncertain）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
