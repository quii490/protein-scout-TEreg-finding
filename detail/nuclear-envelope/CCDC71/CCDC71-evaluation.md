---
type: protein-evaluation
gene: "CCDC71"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC71 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC71 |
| 蛋白名称 | Coiled-coil domain-containing protein 71 |
| 蛋白大小 | 467 aa / 49.6 kDa |
| UniProt ID | Q8IV32 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 467 aa / 49.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026695; Pfam: PF15374 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. ATRX proximal protein associations boast roles beyond histone deposition.. *PLoS genetics*. PMID: 34780483
2. Identification of novel integration sites for bovine leukemia virus proviral DNA in cancer driver genes in cattle with persistent lymphocytosis.. *Virus research*. PMID: 35584733
3. Identification of MARK2, CCDC71, GATA2, and KLRC3 as candidate diagnostic genes and potential therapeutic targets for repeated implantation failure with antiphospholipid syndrome by integrated bioinformatics analysis and machine learning.. *Frontiers in immunology*. PMID: 37901230

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.5 |
| 高置信度残基 (pLDDT>90) 占比 | 11.1% |
| 置信残基 (pLDDT 70-90) 占比 | 6.4% |
| 中等置信 (pLDDT 50-70) 占比 | 18.2% |
| 低置信 (pLDDT<50) 占比 | 64.2% |
| 有序区域 (pLDDT>70) 占比 | 17.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.5），有序残基占 17.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026695; Pfam: PF15374 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DYRK2 | 0.599 | 0.000 | — |
| ANTXR2 | 0.592 | 0.000 | — |
| UNC119B | 0.580 | 0.000 | — |
| RBBP7 | 0.567 | 0.511 | — |
| FAM207A | 0.554 | 0.000 | — |
| ZNF282 | 0.543 | 0.000 | — |
| SH3BP5L | 0.524 | 0.000 | — |
| HDAC1 | 0.514 | 0.484 | — |
| DLK1 | 0.490 | 0.000 | — |
| ZNF19 | 0.490 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KRT8 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TCP1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SSB | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HDAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RBBP7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SUPT5H | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| UNC13B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| WDHD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FRYL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.5 + PDB: 无 | pLDDT=52.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear membrane | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CCDC71 — Coiled-coil domain-containing protein 71，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小467 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=52.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IV32
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177352-CCDC71/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC71
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IV32
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000177352-CCDC71/subcellular

![](https://images.proteinatlas.org/47547/697_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/47547/697_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/47547/735_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/47547/735_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/47547/749_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/47547/749_E8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IV32-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
