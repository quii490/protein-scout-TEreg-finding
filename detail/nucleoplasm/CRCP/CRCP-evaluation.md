---
type: protein-evaluation
gene: "CRCP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRCP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRCP |
| 蛋白名称 | DNA-directed RNA polymerase III subunit RPC9 |
| 蛋白大小 | 148 aa / 16.9 kDa |
| UniProt ID | O75575 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Nucleus; Cell membrane |
| 蛋白大小 | 8/10 | x1 | 8 | 148 aa / 16.9 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=35 篇 (<=40->8) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=82.9; PDB: 7A6H, 7AE1, 7AE3, 7AEA, 7AST, 7D58, 7D59 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR010997, IPR006590, IPR005574, IPR038324, IPR038 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Approved |
| UniProt | Nucleus; Cell membrane | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- cytosol (GO:0005829)
- DNA polymerase III complex (GO:0009360)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- RNA polymerase III complex (GO:0005666)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 331 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Studies on the delineation of the antigenic determinants of chicken riboflavin carrier protein (cRCP). Identification of a determinant in the region 10-24 of the protein.. *International journal of peptide and protein research*. PMID: 7679667
2. Genome-scale CRISPR/Cas9 screening reveals the role of PSMD4 in colibactin-mediated cell cycle arrest.. *mSphere*. PMID: 39918307
3. Identification of an LPS-Induced Chemo-Attractive Peptide from Ciona robusta.. *Marine drugs*. PMID: 32290587
4. Comparison of antibodies raised against the peptide 10-24 of chicken riboflavin carrier protein (cRCP) by classical and multiple antigen peptide (MAP) approaches.. *Journal of immunological methods*. PMID: 8621956
5. Differential Metabolic and Transcriptional Responses of PBMCs to Blastocystis sp. Subtypes in Chemotherapy-Treated Colorectal Cancer Patients.. *Acta parasitologica*. PMID: 42154421

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.9 |
| 高置信度残基 (pLDDT>90) 占比 | 58.8% |
| 置信残基 (pLDDT 70-90) 占比 | 20.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.8% |
| 低置信 (pLDDT<50) 占比 | 9.5% |
| 有序区域 (pLDDT>70) 占比 | 79.7% |
| 可用 PDB 条目 | 7A6H, 7AE1, 7AE3, 7AEA, 7AST, 7D58, 7D59, 7DN3, 7DU2, 7FJI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7A6H, 7AE1, 7AE3, 7AEA, 7AST, 7D58, 7D59, 7DN3, 7DU2, 7FJI）+ AlphaFold极高置信度预测（pLDDT=82.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010997, IPR006590, IPR005574, IPR038324, IPR038846; Pfam: PF03874 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POLR3B | 0.999 | 0.997 | — |
| POLR3F | 0.999 | 0.997 | — |
| POLR3C | 0.999 | 0.996 | — |
| POLR1D | 0.999 | 0.993 | — |
| POLR3A | 0.999 | 0.997 | — |
| POLR1C | 0.999 | 0.999 | — |
| POLR3H | 0.999 | 0.997 | — |
| POLR2E | 0.999 | 0.998 | — |
| POLR3E | 0.999 | 0.997 | — |
| POLR2H | 0.999 | 0.996 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| VAV2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| terA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| LRIF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GSC2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DYNLRB1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AGR2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| POLR3GL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POLR3D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POLR1C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.9 + PDB: 7A6H, 7AE1, 7AE3, 7AEA, 7AST,  | pLDDT=82.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cell membrane / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. CRCP -- DNA-directed RNA polymerase III subunit RPC9，非常新颖，仅有少数基础研究。
2. 蛋白大小148 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75575
- Protein Atlas: https://www.proteinatlas.org/ENSG00000241258-CRCP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRCP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75575
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000241258-CRCP/subcellular

![](https://images.proteinatlas.org/6883/1836_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/6883/1836_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/6883/1901_N9_2_red_green.jpg)
![](https://images.proteinatlas.org/6883/1901_N9_5_red_green.jpg)
![](https://images.proteinatlas.org/6883/2063_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/6883/2063_H8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75575-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
