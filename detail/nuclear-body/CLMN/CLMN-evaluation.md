---
type: protein-evaluation
gene: "CLMN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CLMN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLMN / KIAA1188 |
| 蛋白名称 | Calmin |
| 蛋白大小 | 1002 aa / 111.7 kDa |
| UniProt ID | Q96JQ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nuclear bodies; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 8/10 | x1 | 8 | 1002 aa / 111.7 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=52.2; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR001589, IPR001715, IPR036872, IPR047827, IPR047 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- meiotic nuclear membrane microtubule tethering complex (GO:0034993)
- nuclear outer membrane (GO:0005640)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 50 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1188 |

**关键文献**:
1. Diagnostic Yield and Novel Candidate Genes by Exome Sequencing in 152 Consanguineous Families With Neurodevelopmental Disorders.. *JAMA psychiatry*. PMID: 28097321
2. Exploration of the active components and pharmacological mechanism of Compound Longmaining for the treatment of myocardial infarction.. *Frontiers in bioscience (Landmark edition)*. PMID: 34719208
3. Spatial proteomics of ER tubules reveals CLMN, an ER-actin tether at focal adhesions that promotes cell migration.. *Cell reports*. PMID: 40184252
4. Potential Significance and Clinical Value Explorations of Calmin (CLMN) in Breast Invasive Carcinoma.. *International journal of general medicine*. PMID: 34531680
5. The all-trans retinoic acid (atRA)-regulated gene Calmin (Clmn) regulates cell cycle exit and neurite outgrowth in murine neuroblastoma (Neuro2a) cells.. *Experimental cell research*. PMID: 22001116

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.2 |
| 高置信度残基 (pLDDT>90) 占比 | 17.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.8% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 67.3% |
| 有序区域 (pLDDT>70) 占比 | 26.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.2），有序残基占 26.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001589, IPR001715, IPR036872, IPR047827, IPR047826; Pfam: PF00307 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYNE2 | 0.674 | 0.000 | — |
| SYNE1 | 0.664 | 0.000 | — |
| SYNE3 | 0.628 | 0.101 | — |
| SUN2 | 0.619 | 0.091 | — |
| SUN1 | 0.615 | 0.091 | — |
| SUN5 | 0.593 | 0.091 | — |
| SUN3 | 0.593 | 0.091 | — |
| SPAG4 | 0.593 | 0.091 | — |
| CCDC155 | 0.551 | 0.063 | — |
| EMD | 0.466 | 0.112 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.2 + PDB: 无 | pLDDT=52.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nuclear bodies; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CLMN -- Calmin，非常新颖，仅有少数基础研究。
2. 蛋白大小1002 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=52.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96JQ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165959-CLMN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLMN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96JQ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96JQ2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
