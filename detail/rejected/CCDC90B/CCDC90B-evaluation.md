---
type: protein-evaluation
gene: "CCDC90B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CCDC90B — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC90B |
| 蛋白名称 | Coiled-coil domain-containing protein 90B, mitochondrial |
| 蛋白大小 | 254 aa / 29.5 kDa |
| UniProt ID | Q9GZT6 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CCDC90B/IF_images/A-431_1.jpg|A 431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/CCDC90B/IF_images/U-251MG_1.jpg|U 251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 254 aa / 29.5 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.9; PDB: 无 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 19 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Enhanced |
| UniProt | Mitochondrion membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Causal relationship between mitochondrial-associated proteins and cerebral aneurysms: a Mendelian randomization study.. *Front Neurol*. PMID: 39087007
2. A Comparative Cross-Platform Analysis to Identify Potential Biomarker Genes for Evaluation of Teratozoospermia and Azoospermia.. *Genes (Basel)*. PMID: 36292606
3. Identification of an Immune Classification and Prognostic Genes for Lung Adenocarcinoma Based on Immune Cell Signatures.. *Front Med (Lausanne)*. PMID: 35433762
4. Bioinformatic Prediction of Gene Ontology Terms of Uncharacterized Proteins from Chromosome 11.. *J Proteome Res*. PMID: 33089979
5. Characterization of MCU-Binding Proteins MCUR1 and CCDC90B - Representatives of a Protein Family Conserved in Prokaryotes and Eukaryotic Organelles.. *Structure*. PMID: 30612859

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.9 |
| 高置信度残基 (pLDDT>90) 占比 | 63.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 18.5% |
| 有序区域 (pLDDT>70) 占比 | 76.8% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CCDC90B/CCDC90B-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=81.9，有序区 76.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCUR1 | 0.000 | 0.000 | — |
| FAM32A | 0.000 | 0.000 | — |
| TRMT1L | 0.000 | 0.000 | — |
| NIPAL2 | 0.000 | 0.000 | — |
| MRPL53 | 0.000 | 0.000 | — |
| ANKRD42 | 0.000 | 0.000 | — |
| WDR74 | 0.000 | 0.000 | — |
| IGSF22 | 0.000 | 0.000 | — |
| RAB30 | 0.000 | 0.000 | — |
| MICU1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9GZT6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:A0A6L7H0E1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:A0A380PDY1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q562R1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q96AQ8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 19，IntAct interactions: 30
- 调控相关比例: 1 / 19 = 5%

**评价**: STRING 19 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.9 + PDB: 无 | pLDDT=81.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion membrane / Mitochondria | 一致 |
| PPI | STRING + IntAct | 19 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CCDC90B — Coiled-coil domain-containing protein 90B, mitochondrial，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小254 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9GZT6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137500-CCDC90B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC90B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9GZT6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CCDC90B/CCDC90B-PAE.png]]




