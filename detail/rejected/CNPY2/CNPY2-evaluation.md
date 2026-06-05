---
type: protein-evaluation
gene: "CNPY2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CNPY2 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNPY2 |
| 蛋白名称 | Protein canopy homolog 2 |
| 蛋白大小 | 182 aa / 20.7 kDa |
| UniProt ID | Q9Y2B0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; UniProt: Endoplasmic reticulum |
| 蛋白大小 | 8/10 | x1 | 8 | 182 aa / 20.7 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=63 篇 (≤80→4) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=84.9; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Endoplasmic reticulum | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 63 |
| PubMed broad count | 65 |
| 别名(未计入scoring) |  |

**关键文献**:
1. TRIM26-Mediated CBX6 Ubiquitination Triggers NETosis to Drive Bladder Cancer Tumor Growth via the CNPY2/NF-κB Signaling Pathway.. *Drug Dev Res*. PMID: 42163428
2. miR-144 targets in myocardial hypertrophy and coronary microvascular dysfunction in hypertrophic cardiomyopathy: molecular research meets imaging.. *Basic Res Cardiol*. PMID: 41557158
3. Multifaceted role of CNPY2 beyond ER stress: Disease implications and therapeutic potential.. *Cell Stress*. PMID: 42016348
4. Integrating environmental factors and genetic variants in machine learning to assess occupational noise impact on health.. *Ecotoxicol Environ Saf*. PMID: 41671953
5. Bioinformatics-based screening and validation of ferroptosis-related genes in sepsis and type 2 diabetes mellitus.. *Exp Biol Med (Maywood)*. PMID: 41194984

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.9 |
| 高置信度残基 (pLDDT>90) 占比 | 56.0% |
| 置信残基 (pLDDT 70-90) 占比 | 28.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.4% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 84.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.9，有序区 84.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYLIP | 0.000 | 0.000 | — |
| MYLPF | 0.000 | 0.000 | — |
| PSAPL1 | 0.000 | 0.000 | — |
| LRRTM4 | 0.000 | 0.000 | — |
| MYL12B | 0.000 | 0.000 | — |
| PSAP | 0.000 | 0.000 | — |
| CNPY4 | 0.000 | 0.000 | — |
| HSPA5 | 0.000 | 0.000 | — |
| CNPY3 | 0.000 | 0.000 | — |
| PTPRS | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9Y2B0 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:A0A6L8PZ36 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q13263 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:P14625 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:P02458-1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q14554 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q14807 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q2NKJ3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q5MNZ6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6PCB0 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.9 + PDB: 无 | pLDDT=84.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CNPY2 -- Protein canopy homolog 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小182 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 63 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2B0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000257727-CNPY2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNPY2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2B0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2B0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
