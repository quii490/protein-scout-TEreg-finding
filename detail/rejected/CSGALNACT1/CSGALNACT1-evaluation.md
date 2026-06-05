---
type: protein-evaluation
gene: "CSGALNACT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CSGALNACT1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSGALNACT1 |
| 蛋白名称 | Chondroitin sulfate N-acetylgalactosaminyltransferase 1 |
| 蛋白大小 | 532 aa / 61.3 kDa |
| UniProt ID | Q8TDX6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; 额外: Golgi apparatus; UniProt: Golgi apparatus, Golgi stack membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 532 aa / 61.3 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=59 篇 (≤60→6) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=87.2; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.5/180** | |
| **归一化总分** | | | **52.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Golgi apparatus | Approved |
| UniProt | Golgi apparatus, Golgi stack membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 59 |
| PubMed broad count | 59 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Impact of CSGALNACT1-mediated structural changes in chondroitin sulfate on tau seed uptake and pathological progression.. *Biochim Biophys Acta Gen Subj*. PMID: 41996943
2. Alterations in gene expression and protein levels of extracellular matrix-related molecules in major depressive disorder: Insights from analyses in the hippocampus and prefrontal cortex.. *Neurobiol Dis*. PMID: 42229016
3. Genetic impacts on within-pair DNA methylation variance in monozygotic twins capture gene-environment interactions and cell-type effects.. *Genome Biol*. PMID: 41654882
4. Unveiling the toxicological impact of cigarette smoke exposure on chronic obstructive pulmonary disease: integrated insights from network toxicology and multi-omics.. *Naunyn Schmiedebergs Arch Pharmacol*. PMID: 41217457
5. Comprehensive analysis of the papillary thyroid carcinoma identifies CSGALNACT1 as a proliferation driver and prognostic biomarker.. *Front Cell Dev Biol*. PMID: 40950406

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 63.7% |
| 置信残基 (pLDDT 70-90) 占比 | 24.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 5.1% |
| 有序区域 (pLDDT>70) 占比 | 88.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.2，有序区 88.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHPF | 0.000 | 0.000 | — |
| B3GAT3 | 0.000 | 0.000 | — |
| CSGALNACT2 | 0.000 | 0.000 | — |
| CHPF2 | 0.000 | 0.000 | — |
| CHSY1 | 0.000 | 0.000 | — |
| CHSY3 | 0.000 | 0.000 | — |
| B4GALT7 | 0.000 | 0.000 | — |
| CHST7 | 0.000 | 0.000 | — |
| CHST12 | 0.000 | 0.000 | — |
| CHST11 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q16720-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6NUQ4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8N6G5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9H1E5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NZH0 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9UNS1-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9Y6D5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9Y6D6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9Y6M5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8TDX6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 无 | pLDDT=87.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, Golgi stack membrane / Cytosol; 额外: Golgi apparatus | 一致 |
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
1. CSGALNACT1 -- Chondroitin sulfate N-acetylgalactosaminyltransferase 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小532 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 59 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TDX6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147408-CSGALNACT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSGALNACT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TDX6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TDX6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
