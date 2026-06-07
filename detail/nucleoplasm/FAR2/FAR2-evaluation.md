---
type: protein-evaluation
gene: "FAR2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAR2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAR2 / MLSTD1 |
| 蛋白名称 | Fatty acyl-CoA reductase 2 |
| 蛋白大小 | 515 aa / 59.4 kDa |
| UniProt ID | Q96K12 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoli; UniProt: Peroxisome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 515 aa / 59.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026055, IPR033640, IPR013120, IPR036291; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoli | Approved |
| UniProt | Peroxisome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- peroxisomal membrane (GO:0005778)
- peroxisome (GO:0005777)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MLSTD1 |

**关键文献**:
1. Dose-dependent transcriptional effects of lithium and adverse effect burden in a psychiatric cohort.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 34320404
2. FAR2 is associated with kidney disease in mice and humans.. *Physiological genomics*. PMID: 29652635
3. Meta-analysis of gene expression data in adipose tissue reveals new obesity associated genes.. *Gene*. PMID: 35063573
4. Gene-specific DNA methylation may mediate atypical antipsychotic-induced insulin resistance.. *Bipolar disorders*. PMID: 27542345
5. Fatty acyl-CoA reductase FAR1 is essential for the testicular seminolipid synthesis required for spermatogenesis and male fertility.. *The Journal of biological chemistry*. PMID: 40288649

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.1 |
| 高置信度残基 (pLDDT>90) 占比 | 86.6% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 0.4% |
| 有序区域 (pLDDT>70) 占比 | 98.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.1，有序区 98.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026055, IPR033640, IPR013120, IPR036291; Pfam: PF07993, PF03015 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAR1 | 0.906 | 0.000 | — |
| GNPAT | 0.870 | 0.000 | — |
| AGPS | 0.728 | 0.000 | — |
| FASN | 0.710 | 0.000 | — |
| IQCF1 | 0.601 | 0.601 | — |
| ECI2 | 0.515 | 0.000 | — |
| HACL1 | 0.486 | 0.000 | — |
| SOAT1 | 0.481 | 0.000 | — |
| PEX7 | 0.479 | 0.000 | — |
| AASDH | 0.479 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| GRPR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHRNA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC39A4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC39A12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCDHGB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PEX19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATP2B2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SCN3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.1 + PDB: 无 | pLDDT=94.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Peroxisome membrane / Golgi apparatus; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAR2 — Fatty acyl-CoA reductase 2，非常新颖，仅有少数基础研究。
2. 蛋白大小515 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96K12
- Protein Atlas: https://www.proteinatlas.org/ENSG00000064763-FAR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96K12
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000064763-FAR2/subcellular

![](https://images.proteinatlas.org/15884/127_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15884/127_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/15884/128_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15884/128_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/15884/129_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15884/129_G7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96K12-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96K12 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026055;IPR033640;IPR013120;IPR036291; |
| Pfam | PF07993;PF03015; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000064763-FAR2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PEX19 | Bioplex | false |
| SLC31A1 | Biogrid | false |
| SLC39A12 | Biogrid | false |
| SLC39A4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
