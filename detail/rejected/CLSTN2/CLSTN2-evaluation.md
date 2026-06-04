---
type: protein-evaluation
gene: "CLSTN2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLSTN2 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLSTN2 |
| 蛋白名称 | Calsyntenin-2 |
| 蛋白大小 | 955 aa / 107.0 kDa |
| UniProt ID | Q9H4D0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Vesicles; 额外: Cytokinetic bridge; UniProt: Postsynaptic cell membrane; Endoplasmic reticulum membrane;  |
| 蛋白大小 | 8/10 | x1 | 8 | 955 aa / 107.0 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=61 篇 (≤80→4) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=78.9; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 22 partners; IntAct 19 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Cytokinetic bridge | Uncertain |
| UniProt | Postsynaptic cell membrane; Endoplasmic reticulum membrane; Golgi apparatus membrane; Cell projectio... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 61 |
| PubMed broad count | 65 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Integrated New Approach Methodologies Reveal the Potential Role of 2,7-Dibromocarbazole in Parkinson's Disease via Monoamine Oxidase B Inhibition and Dopaminergic Dysfunction.. *Environ Sci Technol*. PMID: 41725537
2. Genomic insights on the Parma and Piacenza Italian native turkey breed for conservation and traceability.. *Poult Sci*. PMID: 41518904
3. Plasma IGFBP7 improves risk reclassification for liver-related outcomes: Insights from proteo-transcriptomic profiling.. *JHEP Rep*. PMID: 41631129
4. Mining of candidate genes related to prolificacy in Jining grey goats using transcriptomics.. *BMC Genomics*. PMID: 41398643
5. Investigating the prognostic potential of PTPN11 gene in papillary thyroid carcinoma: A comprehensive study of bulk and single cell transcriptome.. *Medicine (Baltimore)*. PMID: 41367010

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.9 |
| 高置信度残基 (pLDDT>90) 占比 | 49.7% |
| 置信残基 (pLDDT 70-90) 占比 | 27.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 17.9% |
| 有序区域 (pLDDT>70) 占比 | 77.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=78.9，有序区 77.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NMNAT3 | 0.000 | 0.000 | — |
| KLC2 | 0.000 | 0.000 | — |
| KLC4 | 0.000 | 0.000 | — |
| KLC1 | 0.000 | 0.000 | — |
| GRIP1 | 0.000 | 0.000 | — |
| CDH17 | 0.000 | 0.000 | — |
| KLC3 | 0.000 | 0.000 | — |
| NRXN2 | 0.000 | 0.000 | — |
| SLC12A9 | 0.000 | 0.000 | — |
| NUP37 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O60645 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75592 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75691 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O94985 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O95470 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O96018 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P11277 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P29597 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P39880 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P49257 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 22，IntAct interactions: 19
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 22 个预测互作，IntAct 19 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.9 + PDB: 无 | pLDDT=78.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Postsynaptic cell membrane; Endoplasmic reticulum  / Vesicles; 额外: Cytokinetic bridge | 一致 |
| PPI | STRING + IntAct | 22 + 19 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CLSTN2 -- Calsyntenin-2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小955 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 61 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H4D0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158258-CLSTN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLSTN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H4D0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
