---
type: protein-evaluation
gene: "CAPNS2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CAPNS2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAPNS2 |
| 蛋白名称 | Calpain small subunit 2 |
| 蛋白大小 | 248 aa / 27.7 kDa |
| UniProt ID | Q96L46 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CAPNS2/IF_images/HaCaT_1.jpg|HaCaT]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/CAPNS2/IF_images/hTCEpi_1.jpg|hTCEpi]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm; Cell membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 248 aa / 27.7 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.4; PDB: 无 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 10 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Exploring shared molecular pathways and gene signatures in type 2 diabetes mellitus and Alzheimer's disease in a Pakistani cohort.. *J Alzheimers Dis Rep*. PMID: 41929972
2. Large-scale exome sequencing identified 18 novel genes for neuroticism in 394,005 UK-based individuals.. *Nat Hum Behav*. PMID: 39511343
3. lncRNA CDKN2B-AS1 regulates collagen expression.. *Hum Genet*. PMID: 38833008
4. Transcriptomic Analysis of Alzheimer's Disease Pathways in a Pakistani Population.. *J Alzheimers Dis Rep*. PMID: 38549628
5. RNA-seq analysis revealed genes associated with neuropathic pain induced by chronic compressive injury in interferon regulatory factors 4 knockout mice.. *Hum Exp Toxicol*. PMID: 38073479

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.4 |
| 高置信度残基 (pLDDT>90) 占比 | 43.5% |
| 置信残基 (pLDDT 70-90) 占比 | 25.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 21.8% |
| 有序区域 (pLDDT>70) 占比 | 69.3% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CAPNS2/CAPNS2-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=75.4，有序区 69.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAST | 0.000 | 0.000 | — |
| CAPN1 | 0.000 | 0.000 | — |
| CAPNS1 | 0.000 | 0.000 | — |
| CAPN6 | 0.000 | 0.000 | — |
| CAPN5 | 0.000 | 0.000 | — |
| CAPN7 | 0.000 | 0.000 | — |
| CAPN2 | 0.000 | 0.000 | — |
| CAPN14 | 0.000 | 0.000 | — |
| CAPN13 | 0.000 | 0.000 | — |
| CAPN15 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q96L46 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:P04632 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P20810-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P62736 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q562R1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8IVB5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q96KR7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96DZ9-2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.4 + PDB: 无 | pLDDT=75.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cell membrane / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CAPNS2 — Calpain small subunit 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小248 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96L46
- Protein Atlas: https://www.proteinatlas.org/ENSG00000256812-CAPNS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CAPNS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96L46
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CAPNS2/CAPNS2-PAE.png]]




