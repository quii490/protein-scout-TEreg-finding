---
type: centrosome-protein-evaluation
gene: "MZT2A"
module: centrosome
status: centrosome_candidate
date: 2026-06-08
tags: [protein-scout, centrosome, evaluation]
---

# MZT2A — 中心体模块评估

## 1. 基本信息

- **基因:** MZT2A
- **Ensembl:** ENSG00000173272
- **HPA 来源:** 中心体
- **HPA 抗体:** HPA051758, HPA052623
- **IF 可靠性:** Approved
- **PubMed 文献总数:** 14 篇

## 2. HPA 中心体 / 中心粒卫星证据

- **HPA 来源:** 中心体 ✓
- **HPA 链接:** https://www.proteinatlas.org/ENSG00000173272-MZT2A
- **HPA 定位:** Centrosome, Cytosol
- **IF 图像状态:** 已获取 (1 张, selected)


<!-- CENTROSOME_HPA_IF_START -->
**HPA IF 图像（2026-06-08）**: HPA subcellular 页面存在可用 IF 图像。
HPA 定位: Centrosome, Cytosol。HPA IF 可靠性: approved。
来源: https://www.proteinatlas.org/ENSG00000173272-MZT2A/subcellular

![](https://images.proteinatlas.org/51758/987_D8_2_selected.jpg)
<!-- CENTROSOME_HPA_IF_END -->


## 3. UniProt / GO-CC 中心体证据

*待 UniProt/GO-CC 完整采集。需人工审核。*

- 初步: HPA 标注支持 中心体 定位。

## 4. PubMed 文献证据

- **文献总数:** 14 篇
- **研究量评估:** 低研究量
- 1. PMID 20861304: The gammaTuRC revisited: a comparative analysis of interphase and mitotic human gammaTuRC redefines the set of core components and identifies the novel subunit GCP8. (2010 Nov 15) *Mol Biol Cell*
2. PMID 33754417: MZT2A promotes NSCLC viability and invasion by increasing Akt phosphorylation via the MOZART2 domain. (2021 Jun) *Cancer Sci*

## 5. AlphaFold / PAE / PDB / 结构域

pLDDT 数据可用 (UniProt: Q6P582)。PDB 模型: https://alphafold.ebi.ac.uk/files/AF-Q6P582-F1-model_v6.pdb

*InterPro: MOZART2*
*Pfam: MOZART2*

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络

### STRING (人类, top 10)

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|
| TUBG1 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP2 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP4 | 0.999 | 0.000 | 0.000 | 0.000 |
| MZT1 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP5 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP5 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP4 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP2 | 0.999 | 0.000 | 0.000 | 0.000 |
| TUBGCP5 | 0.999 | 0.000 | 0.000 | 0.000 |
| MZT1 | 0.999 | 0.000 | 0.000 | 0.000 |

*待 IntAct / BioGRID / humanPPI 补充。*

## 7. 中心体模块评分表

| 维度 | 评分 | 依据 |
|---|---:|---|
| 中心体证据 | 16/20 | HPA 标注 |
| PubMed/文献 | 8/20 | 14 篇文献 |
| PPI/互作网络 | 18/20 | STRING: 20p + 0 named |
| 结构/结构域 | 6/10 | AF 1 domains |
| 新颖性/特异性 | 8/10 | 低研究量 |

- **最终评分:** **68/100**

## 8. 最终结论

**CENTROSOME CANDIDATE**

⚠️ *此为自动生成初步评估。UniProt/GO-CC、PDB/结构域、IntAct/BioGRID、关键文献等维度需人工补充完善。*

### 深度机制分析

MZT2A（MOZART2蛋白）是微管组织中心相关蛋白，定位于中心体（HPA approved, Centrosome/Cytosol）。其结构域包含MOZART2保守结构域（InterPro、Pfam:MOZART2），属于γ-微管蛋白环复合物（γTuRC）的核心辅助亚基。γTuRC是微管成核的关键超分子组装体，包含γ-Tubulin、GCP2-6和MZT1/MZT2A等辅助蛋白，分子量超过2 MDa。MZT2A与TUBG1（STRING Combined Score=0.999）、TUBGCP2/4/5（0.999）、MZT1（0.999）形成高置信度互作网络，证实其作为γTuRC完整组分的保守身份（PMID:20861304）。

该蛋白在NSCLC中通过Akt磷酸化促进细胞活力和侵袭（PMID:33754417），其靶向Akt磷酸化的MOZART2结构域赋予其非微管依赖的促癌功能。MZT2A/mTOR/Akt信号轴提示中心体蛋白在细胞周期和生长信号整合中的非经典角色。

从TE调控角度，中心体蛋白与TE调控的关联属于非常间接的远端效应。中心体功能障碍导致染色体错误分离和非整倍体，非整倍体引发的基因组不稳定可导致异染色质去凝聚和重复序列（含TE）的转录去抑制。MZT2A作为γTuRC亚基，在维持有丝分裂纺锤体完整性和染色体正确分离中发挥基础性角色——其功能缺失可能通过基因组不稳定性间接影响全局TE表达水平。但该蛋白与染色质修饰酶、转录因子或TE沉默复合物无任何直接的PPI或定位重叠，其评分68/100属于中心体模块候选而非核蛋白TE调控靶标。

## 9. 人工复核备注

- HPA 来源: 中心体
- 抗体: HPA051758, HPA052623（IF 可靠性: Approved）
- 建议: 核实中心体 IF 文献定位
- 如 IF 图像质量不佳，检查 HPA 是否有替代抗体
