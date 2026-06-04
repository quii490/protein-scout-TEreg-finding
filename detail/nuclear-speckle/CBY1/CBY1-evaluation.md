---
type: protein-evaluation
gene: "CBY1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CBY1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CBY1 / ARB1, C22orf2, CBY, PGEA1 |
| 蛋白名称 | Protein chibby homolog 1 |
| 蛋白大小 | 126 aa / 14.5 kDa |
| UniProt ID | Q9Y3M2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus speckle; Cytoplasm, cytoskeleton, cilium basal body; |
| 蛋白大小 | 8/10 | ×1 | 8 | 126 aa / 14.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.7; PDB: 4WRQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR028118; Pfam: PF14645 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Nucleus speckle; Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cytoskeleton, microtubule or... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARB1, C22orf2, CBY, PGEA1 |

**关键文献**:
1. Chibby1 knockdown promotes mesenchymal-to-epithelial transition-like changes.. *Cell cycle (Georgetown, Tex.)*. PMID: 28107095
2. Dimerization of the BAR domain-containing protein FAM92A modulates lipid binding and interaction with CBY1.. *The Journal of biological chemistry*. PMID: 40484380
3. Chibby 1: a new component of β-catenin-signaling in chronic myeloid leukemia.. *Oncotarget*. PMID: 29152155
4. BAR Domain-Containing FAM92 Proteins Interact with Chibby1 To Facilitate Ciliogenesis.. *Molecular and cellular biology*. PMID: 27528616
5. Loss of the ciliary protein Chibby1 in mice leads to exocrine pancreatic degeneration and pancreatitis.. *Scientific reports*. PMID: 34446743

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.7 |
| 高置信度残基 (pLDDT>90) 占比 | 41.3% |
| 置信残基 (pLDDT 70-90) 占比 | 46.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 1.6% |
| 有序区域 (pLDDT>70) 占比 | 88.1% |
| 可用 PDB 条目 | 4WRQ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.7，有序区 88.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028118; Pfam: PF14645 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YWHAZ | 0.992 | 0.958 | — |
| CTNNB1 | 0.992 | 0.649 | — |
| FAM92A | 0.949 | 0.787 | — |
| XPO1 | 0.842 | 0.000 | — |
| LEF1 | 0.773 | 0.000 | — |
| DZIP1L | 0.770 | 0.645 | — |
| PKD2 | 0.761 | 0.000 | — |
| DZIP1 | 0.752 | 0.630 | — |
| ODF2 | 0.678 | 0.000 | — |
| TCIM | 0.669 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AGTPBP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| sbcC3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000413934.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TNFAIP8L3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.7 + PDB: 4WRQ | pLDDT=85.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus speckle; Cytoplasm, cytoskeleton, cilium b / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CBY1 — Protein chibby homolog 1，非常新颖，仅有少数基础研究。
2. 蛋白大小126 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3M2
- Protein Atlas: https://www.proteinatlas.org/search/CBY1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CBY1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3M2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/CBY1/IF_images/CBY1_IF_34760.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/CBY1/IF_images/CBY1_IF_thumb_if_selected_60x60.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/CBY1/CBY1-PAE.png]]
