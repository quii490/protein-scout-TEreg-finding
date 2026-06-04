---
type: protein-evaluation
gene: "CYP2S1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CYP2S1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYP2S1 |
| 蛋白名称 | Cytochrome P450 2S1 |
| 蛋白大小 | 504 aa / 55.8 kDa |
| UniProt ID | Q96SQ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Endoplasmic reticulum; UniProt: Endoplasmic reticulum membrane; Microsome membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 504 aa / 55.8 kDa |
| 研究新颖性 | 2/10 | x5 | 10 | PubMed strict=96 篇 (≤100→2) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=92.6; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **74.5/180** | |
| **归一化总分** | | | **41.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Supported |
| UniProt | Endoplasmic reticulum membrane; Microsome membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 96 |
| PubMed broad count | 104 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Multi-Omics Profiling of oxylipins and gene expression in pediatric sarcomas identifies metastatic signatures and prognostic models.. *Free Radic Biol Med*. PMID: 42177999
2. Cytochrome P450 Cyp2s1 regulation of the intestinal metabolome and microbiome.. *Mucosal Immunol*. PMID: 41120053
3. Proteomic Characterization Reveals CYP2S1 as a Mediator of Drug Resistance in PDAC.. *Pancreas*. PMID: 41001906
4. Serine Glycine Restriction Aggravates Hepatic Ischemia-reperfusion Injury.. *Transplantation*. PMID: 40842043
5. Upregulation of PLAU in granulosa cells disrupts steroid hormone synthesis and promotes apoptosis by activating NF-κB signaling pathway in PCOS.. *J Ovarian Res*. PMID: 41462288

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.6 |
| 高置信度残基 (pLDDT>90) 占比 | 85.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 1.8% |
| 有序区域 (pLDDT>70) 占比 | 95.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.6，有序区 95.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYP3A4 | 0.000 | 0.000 | — |
| CYP26A1 | 0.000 | 0.000 | — |
| CYP3A5 | 0.000 | 0.000 | — |
| CYP4A22 | 0.000 | 0.000 | — |
| CYP4A11 | 0.000 | 0.000 | — |
| CYP3A7 | 0.000 | 0.000 | — |
| CYP26B1 | 0.000 | 0.000 | — |
| CYP1A1 | 0.000 | 0.000 | — |
| CYP1A2 | 0.000 | 0.000 | — |
| CYP26C1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q96SQ9-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6UY14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96SQ9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:E5RI47 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O00192-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O43491 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O95297-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P01112 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P07947 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P10114 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.6 + PDB: 无 | pLDDT=92.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Microsome membrane / Endoplasmic reticulum | 一致 |
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
1. CYP2S1 -- Cytochrome P450 2S1，研究基础较多，新颖性有限。
2. 蛋白大小504 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 96 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96SQ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167600-CYP2S1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYP2S1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96SQ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
