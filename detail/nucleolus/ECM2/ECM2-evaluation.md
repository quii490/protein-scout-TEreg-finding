---
type: protein-evaluation
gene: "ECM2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ECM2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ECM2 |
| 蛋白名称 | Extracellular matrix protein 2 |
| 蛋白大小 | 699 aa / 79.8 kDa |
| UniProt ID | O94769 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Endoplasmic reticulum; UniProt: Secreted, extracellular space, extracellular matrix |
| 蛋白大小 | 10/10 | ×1 | 10 | 699 aa / 79.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.3; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Endoplasmic reticulum | Approved |
| UniProt | Secreted, extracellular space, extracellular matrix | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 68 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Alpha-Ketoglutarate Drives an Osteogenic and Extracellular Matrix Gene Program in Periodontal Ligament Fibroblasts via Selective Reduction of H3K27me3.. *Biology (Basel)*. PMID: 41823800
2. Proteomic and histopathologic profiling reveal molecular features and clinical biomarkers of coronary atherosclerosis.. *Biomark Res*. PMID: 41126379
3. A Patient-Derived Scaffold-Based 3D Culture Platform for Head and Neck Cancer: Preserving Tumor Heterogeneity for Personalized Drug Testing.. *Cells*. PMID: 41090771
4. Co-delivery of ripasudil and dexamethasone in trabecular meshwork cells for potential prevention of GC-induced ocular hypertension.. *Exp Cell Res*. PMID: 40972884
5. ECM-based molecular subtypes define prognostic, EMT status, and therapeutic diversity in IDH-mutant gliomas.. *NPJ Precis Oncol*. PMID: 40866630

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.3 |
| 高置信度残基 (pLDDT>90) 占比 | 45.5% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 35.6% |
| 有序区域 (pLDDT>70) 占比 | 62.8% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=71.3，有序区 62.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SNW1 | 0.000 | 0.000 | — |
| BUD31 | 0.000 | 0.000 | — |
| RBM22 | 0.000 | 0.000 | — |
| CWC15 | 0.000 | 0.000 | — |
| CDC5L | 0.000 | 0.000 | — |
| PLRG1 | 0.000 | 0.000 | — |
| OMD | 0.000 | 0.000 | — |
| OGN | 0.000 | 0.000 | — |
| DCN | 0.000 | 0.000 | — |
| ASPN | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P38241 | psi-mi:"MI:0363"(inferred by author) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P32639 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q12309 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P32523 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q12417 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P10592 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P33334 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O59800 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P39964 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P70663 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.3 + PDB: 无 | pLDDT=71.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted, extracellular space, extracellular matri / Nucleoli fibrillar center, Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. ECM2 — Extracellular matrix protein 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小699 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94769
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106823-ECM2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ECM2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94769
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
