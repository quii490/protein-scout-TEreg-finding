---
type: protein-evaluation
gene: "LGALSL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LGALSL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LGALSL / GRP |
| 蛋白名称 | Galectin-related protein |
| 蛋白大小 | 172 aa / 19.0 kDa |
| UniProt ID | Q3ZCW2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 172 aa / 19.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.7; PDB: 2JJ6, 3B9C |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.5/180** | |
| **归一化总分** | | | **77.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GRP |

**关键文献**:
1. Genetic susceptibility and validation of angiographic patterns in Takayasu arteritis.. *Journal of autoimmunity*. PMID: 41207179
2. An Investigative Study of LGALSL and HLA-DRB1 as Prognostic Biomarkers and Therapeutic Targets in Chronic Hepatitis B Patients With Persistent HBV DNA Viremia Under Entecavir Treatment.. *Journal of medical virology*. PMID: 40167905
3. Analysis of chicken LGALSL (galectin-related protein) gene's proximal promoter and its control by Krüppel-like factors 3 and 7.. *Gene*. PMID: 39343186
4. Quantitative serum proteomic analysis for biomarker discovery in post-COVID-19 postural orthostatic tachycardia syndrome (PC-POTS) patients.. *Autonomic neuroscience : basic & clinical*. PMID: 40022872
5. Role of fatty acid metabolism-related genes in periodontitis based on machine learning and bioinformatics analysis.. *Hua xi kou qiang yi xue za zhi = Huaxi kouqiang yixue zazhi = West China journal of stomatology*. PMID: 39610070

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.7 |
| 高置信度残基 (pLDDT>90) 占比 | 79.1% |
| 置信残基 (pLDDT 70-90) 占比 | 1.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 16.9% |
| 有序区域 (pLDDT>70) 占比 | 80.3% |
| 可用 PDB 条目 | 2JJ6, 3B9C |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2JJ6, 3B9C）+ AlphaFold高质量预测（pLDDT=86.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C1orf198 | 0.604 | 0.000 | — |
| CDH24 | 0.461 | 0.000 | — |
| FAM13C | 0.447 | 0.000 | — |
| IGSF1 | 0.440 | 0.000 | — |
| ITGB1BP1 | 0.423 | 0.000 | — |
| CEP68 | 0.418 | 0.000 | — |
| CST2 | 0.408 | 0.045 | — |
| ST3GAL6 | 0.406 | 0.000 | — |
| FOXS1 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DDIT4L | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| LHX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FCF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAD1L1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CCR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SSUH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SCAF11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| STX17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ADI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZC3HC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 12
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.7 + PDB: 2JJ6, 3B9C | pLDDT=86.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 9 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LGALSL — Galectin-related protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小172 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3ZCW2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119862-LGALSL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LGALSL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3ZCW2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000119862-LGALSL/subcellular

![](https://images.proteinatlas.org/46079/616_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/46079/616_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/46079/619_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/46079/619_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/46079/622_E1_3_red_green.jpg)
![](https://images.proteinatlas.org/46079/622_E1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3ZCW2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
