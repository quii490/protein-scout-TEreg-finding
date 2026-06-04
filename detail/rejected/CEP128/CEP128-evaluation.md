---
type: protein-evaluation
gene: "CEP128"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CEP128 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEP128 |
| 蛋白名称 | Centrosomal protein 128 |
| 蛋白大小 | 1094 aa / 128.0 kDa |
| UniProt ID | Q6ZU80 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CEP128/IF_images/BJ-Human-fibroblast_1.jpg|BJ Human fibroblast]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/CEP128/IF_images/Rh30_1.jpg|Rh30]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Centrosome; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1094 aa / 128.0 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.5; PDB: 无 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; C... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 22 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Integrative gene target mapping, RNA sequencing, in silico molecular docking, ADMET profiling and molecular dynamics simulation study of marine derived molecules for type 1 diabetes mellitus.. *Mol Divers*. PMID: 41533020
2. Runs of homozygosity reveal candidate genes for economic traits in Danish Large White pigs.. *Arch Anim Breed*. PMID: 42027904
3. Integrative Molecular and Functional Analysis of Human Sperm Subpopulations to Identify New Biomarkers of Fertilization Potential.. *Arch Med Res*. PMID: 40168948
4. RETRACTION: Circular RNA CEP128 Promotes Bladder Cancer Progression by Regulating Mir-145-5p/Myd88 via MAPK Signaling Pathway.. *Int J Cancer*. PMID: 40019841
5. Dual-color live imaging unveils stepwise organization of multiple basal body arrays by cytoskeletons.. *EMBO Rep*. PMID: 38316902

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.5 |
| 高置信度残基 (pLDDT>90) 占比 | 25.2% |
| 置信残基 (pLDDT 70-90) 占比 | 46.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 18.5% |
| 有序区域 (pLDDT>70) 占比 | 71.5% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CEP128/CEP128-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=74.5，有序区 71.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CEP170 | 0.000 | 0.000 | — |
| CCDC120 | 0.000 | 0.000 | — |
| CCDC68 | 0.000 | 0.000 | — |
| CNTRL | 0.000 | 0.000 | — |
| NIN | 0.000 | 0.000 | — |
| ODF2 | 0.000 | 0.000 | — |
| KIF2A | 0.000 | 0.000 | — |
| DCTN1 | 0.000 | 0.000 | — |
| CEP89 | 0.000 | 0.000 | — |
| CEP164 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P31491 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8CZZ7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q6ZU80-1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P08670 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q6ZU80 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:H0YJE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9Y2D8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q5TB80 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q66GS9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q2KHM9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.5 + PDB: 无 | pLDDT=74.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Centrosome | 一致 |
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
1. CEP128 — Centrosomal protein 128，非常新颖，仅有少数基础研究。
2. 蛋白大小1094 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZU80
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100629-CEP128/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEP128
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZU80
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CEP128/CEP128-PAE.png]]




