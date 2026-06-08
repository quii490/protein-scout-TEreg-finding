---
type: centrosome-protein-evaluation
gene: "MDM1"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# MDM1 — 中心体模块评估

## 1. 基本信息

- **基因:** MDM1
- **Ensembl:** ENSG00000111554
- **HPA 来源:** 中心粒卫星
- **HPA 抗体:** HPA040411, HPA041594
- **IF 可靠性:** Approved
- **PubMed 文献总数:** 62 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心粒卫星 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000111554-MDM1
- **HPA 定位:** Centriolar satellite, Cytosol
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Centriolar satellite, Cytosol。HPA IF 可靠性: approved。
来源: https://www.proteinatlas.org/ENSG00000111554-MDM1/subcellular

![](https://images.proteinatlas.org/41594/539_E4_6_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心粒卫星 定位。

## 4. PubMed 文献证据

- **文献总数:** 62 篇
- **研究量评估:** 较多文献
- 1. PMID 39543170: An interaction network of inner centriole proteins organised by POC1A-POC1B heterodimer crosslinks ensures centriolar integrity. (2024 Nov 14) *Nat Commun*
2. PMID 26337392: MDM1 is a microtubule-binding protein that negatively regulates centriole duplication. (2015 Nov 1) *Mol Biol Cell*
3. PMID 27658201: Molecular Evolution of MDM1, a "Duplication-Resistant" Gene in Vertebrates. (2016) *PLoS One*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q8TC05)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q8TC05-F1-model_v6.pdb

*InterPro: MDM1*
*Pfam: MDM1*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| SNX13 | 0.813 | 0.000 | 0.000 | 0.000 |
| SNX14 | 0.696 | 0.000 | 0.000 | 0.000 |
| MDM1 | 0.678 | 0.000 | 0.000 | 0.000 |
| MDM1 | 0.669 | 0.000 | 0.000 | 0.000 |
| SNX13 | 0.620 | 0.000 | 0.000 | 0.000 |
| SNX25 | 0.614 | 0.000 | 0.000 | 0.000 |
| ACSL3 | 0.570 | 0.000 | 0.000 | 0.000 |
| MDM1 | 0.567 | 0.000 | 0.000 | 0.000 |
| SNX25 | 0.559 | 0.000 | 0.000 | 0.000 |
| MDM1 | 0.545 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 14/20 | HPA 标注 |
| PubMed/文献 | 6/20 | 62 篇文献 |
| PPI/互作网络 | 12/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 4/10 | 中等研究量 |

- **最终评分:** **52/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

## 9. 人工复核备注

- HPA 来源: 中心粒卫星
- 抗体: HPA040411, HPA041594（IF 可靠性: Approved）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
