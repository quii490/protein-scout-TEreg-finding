---
type: protein-evaluation
gene: "GNLY"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNLY — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=146，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNLY / LAG2, NKG5, TLA519 |
| 蛋白名称 | Granulysin |
| 蛋白大小 | 145 aa / 16.4 kDa |
| UniProt ID | P22749 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted |
| 蛋白大小 | 8/10 | ×1 | 8 | 145 aa / 16.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=146 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=78.1; PDB: 1L9L |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038847, IPR008138, IPR011001, IPR008139; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65.0/180** | |
| **归一化总分** | | | **36.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Secreted | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)
- phagocytic vesicle lumen (GO:0097013)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 146 |
| PubMed broad count | 519 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LAG2, NKG5, TLA519 |

**关键文献**:
1. Integrating single-cell RNA and T cell/B cell receptor sequencing with mass cytometry reveals dynamic trajectories of human peripheral immune cells from birth to old age.. *Nature immunology*. PMID: 39881000
2. Single-cell transcriptomic analyses reveal distinct immune cell contributions to epithelial barrier dysfunction in checkpoint inhibitor colitis.. *Nature medicine*. PMID: 38724705
3. Combining single-cell RNA sequencing and network pharmacology to explore the target of cangfu daotan decoction in the treatment of obese polycystic ovary syndrome from an immune perspective.. *Frontiers in pharmacology*. PMID: 39539629
4. Single-cell transcriptome analysis and protein profiling reveal broad immune system activation in IgG4-related disease.. *JCI insight*. PMID: 37561593
5. Single-cell RNA and T-cell receptor sequencing unveil mycosis fungoides heterogeneity and a possible gene signature.. *Frontiers in oncology*. PMID: 39169943

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.1 |
| 高置信度残基 (pLDDT>90) 占比 | 49.0% |
| 置信残基 (pLDDT 70-90) 占比 | 15.9% |
| 中等置信 (pLDDT 50-70) 占比 | 18.6% |
| 低置信 (pLDDT<50) 占比 | 16.6% |
| 有序区域 (pLDDT>70) 占比 | 64.9% |
| 可用 PDB 条目 | 1L9L |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=78.1，有序区 64.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038847, IPR008138, IPR011001, IPR008139; Pfam: PF03489 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRF1 | 0.999 | 0.000 | — |
| GZMB | 0.995 | 0.000 | — |
| GZMA | 0.976 | 0.000 | — |
| SRRT | 0.969 | 0.000 | — |
| RBPJ | 0.965 | 0.000 | — |
| GZMH | 0.958 | 0.000 | — |
| NKG7 | 0.951 | 0.000 | — |
| FASLG | 0.921 | 0.000 | — |
| KLRD1 | 0.904 | 0.000 | — |
| CD8A | 0.890 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DERL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BCL2L1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PRKCI | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RPL37 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| C1QBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LBR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZNF638 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RANBP10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAEA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RBM23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.1 + PDB: 1L9L | pLDDT=78.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Secreted / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GNLY — Granulysin，研究基础较多，新颖性有限。
2. 蛋白大小145 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 146 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P22749
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115523-GNLY/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNLY
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P22749
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P22749-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
