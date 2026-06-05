---
type: protein-evaluation
gene: "CUX2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CUX2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CUX2 / CUTL2, KIAA0293 |
| 蛋白名称 | Homeobox protein cut-like 2 |
| 蛋白大小 | 1486 aa / 161.7 kDa |
| UniProt ID | O14529 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1486 aa / 161.7 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=91 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.5; PDB: 1WH6, 1WH8, 1X2L |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003350, IPR057476, IPR001356, IPR017970, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.5/180** | |
| **归一化总分** | | | **48.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 91 |
| PubMed broad count | 243 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CUTL2, KIAA0293 |

**关键文献**:
1. Identification of epilepsy-associated neuronal subtypes and gene expression underlying epileptogenesis.. *Nature communications*. PMID: 33028830
2. Gene regulatory landscape of cerebral cortex folding.. *Science advances*. PMID: 38838158
3. CUX2/KDM5B/SOX17 Axis Affects the Occurrence and Development of Breast Cancer.. *Endocrinology*. PMID: 35881915
4. Molecular Signatures of Resilience to Alzheimer's Disease in Neocortical Layer 4 Neurons.. *bioRxiv : the preprint server for biology*. PMID: 39574639
5. Molecular signatures of resilience to Alzheimer's disease in neocortical layer 4 neurons.. *Nature communications*. PMID: 41620473

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.5 |
| 高置信度残基 (pLDDT>90) 占比 | 23.4% |
| 置信残基 (pLDDT 70-90) 占比 | 20.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 51.0% |
| 有序区域 (pLDDT>70) 占比 | 43.7% |
| 可用 PDB 条目 | 1WH6, 1WH8, 1X2L |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.5），有序残基占 43.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003350, IPR057476, IPR001356, IPR017970, IPR009057; Pfam: PF02376, PF25398, PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PHETA1 | 0.833 | 0.000 | — |
| FEZF2 | 0.701 | 0.098 | — |
| SATB2 | 0.697 | 0.052 | — |
| RORB | 0.676 | 0.000 | — |
| TSPEAR | 0.650 | 0.046 | — |
| TBR1 | 0.639 | 0.070 | — |
| BCL11B | 0.616 | 0.098 | — |
| EMX1 | 0.586 | 0.000 | — |
| PAX6 | 0.583 | 0.084 | — |
| ACAD10 | 0.582 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dlg4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:19022416|imex:IM-16994 |
| HNRNPC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| KPNA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KPNA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SNX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CUX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| WDR45B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SNX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NAV3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.5 + PDB: 1WH6, 1WH8, 1X2L | pLDDT=59.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. CUX2 — Homeobox protein cut-like 2，研究基础较多，新颖性有限。
2. 蛋白大小1486 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 91 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=59.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14529
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111249-CUX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CUX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14529
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14529-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
