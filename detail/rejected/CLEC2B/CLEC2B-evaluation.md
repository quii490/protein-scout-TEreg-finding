---
type: protein-evaluation
gene: "CLEC2B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLEC2B — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLEC2B |
| 蛋白名称 | C-type lectin domain family 2 member B |
| 蛋白大小 | 149 aa / 17.3 kDa |
| UniProt ID | Q92478 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Golgi apparatus membrane |
| 蛋白大小 | 8/10 | x1 | 8 | 149 aa / 17.3 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=92.2; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cell membrane; Golgi apparatus membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 147 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CLEC2B-KLRB1 axis acts as an immune checkpoint, governing the exhaustion of CD8(+) T cells and their resistance to immune checkpoint blockade.. *J Immunother Cancer*. PMID: 42208981
2. Single-cell transcriptomic analysis reveals distinct cancer-associated fibroblast signatures in treatment-refractory esophageal squamous cell carcinoma.. *Sci Rep*. PMID: 41345494
3. Immune dysregulation in preeclampsia: integrative analysis of peripheral transcriptomes and placental single-cell land-scapes.. *Front Immunol*. PMID: 41403942
4. Single-cell transcriptomics reveals pathogen interactions and T cell reprogramming in HIV and Mycobacterium tuberculosis co-infection.. *Front Immunol*. PMID: 41394852
5. Meta_B cells: a computationally identified candidate immunosuppressive driver of gastric cancer metastasis revealed by single-cell analysis and machine learning.. *Discov Oncol*. PMID: 40770460

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.2 |
| 高置信度残基 (pLDDT>90) 占比 | 79.9% |
| 置信残基 (pLDDT 70-90) 占比 | 14.8% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 94.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.2，有序区 94.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KLRF1 | 0.000 | 0.000 | — |
| SLAMF6 | 0.000 | 0.000 | — |
| KLRC4 | 0.000 | 0.000 | — |
| KLRF2 | 0.000 | 0.000 | — |
| HLA-E | 0.000 | 0.000 | — |
| NCR1 | 0.000 | 0.000 | — |
| NCR2 | 0.000 | 0.000 | — |
| NCR3 | 0.000 | 0.000 | — |
| MICB | 0.000 | 0.000 | — |
| KLRK1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q92478 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P01023 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:O14656-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P50570-2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O15121 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O43306 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O60637 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75063 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75907 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O94901 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.2 + PDB: 无 | pLDDT=92.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Golgi apparatus membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLEC2B -- C-type lectin domain family 2 member B，非常新颖，仅有少数基础研究。
2. 蛋白大小149 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92478
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110852-CLEC2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLEC2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92478
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92478-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
