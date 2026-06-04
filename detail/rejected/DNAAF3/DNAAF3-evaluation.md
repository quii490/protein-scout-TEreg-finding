---
type: protein-evaluation
gene: "DNAAF3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAAF3 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAAF3 |
| 蛋白名称 | Dynein axonemal assembly factor 3 |
| 蛋白大小 | 541 aa / 59.4 kDa |
| UniProt ID | Q8N9W5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; 额外: Vesicles; UniProt: Cytoplasm; Dynein axonemal particle |
| 蛋白大小 | 10/10 | x1 | 10 | 541 aa / 59.4 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=28 篇 (<=40->8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.6; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 8/10 | x3 | 24 | STRING 25 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Vesicles | Approved |
| UniProt | Cytoplasm; Dynein axonemal particle | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 33 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Prevalence and Nationality Distribution of Known and Novel Genetic Variants in Children With Primary Ciliary Dyskinesia in the State of Qatar.. *Clin Genet*. PMID: 41267578
2. Identification of a Novel DNAAF3 Variant in a 54-Year-Old Patient With Newly Diagnosed Primary Ciliary Dyskinesia (PCD).. *Case Rep Genet*. PMID: 41509703
3. Functional characterization of DNAAF3-AS1 in chromatin remodeling and H3K36me3 distribution.. *bioRxiv*. PMID: 41446072
4. Lentiviral Gene Delivery Rescues Ciliary Defects in Patient-Derived Airway Organoids from Primary Ciliary Dyskinesia.. *Hum Gene Ther*. PMID: 40947900
5. Clinical features and genetic spectrum of children with primary ciliary dyskinesia in central China: a referral center retrospective analysis.. *Front Pharmacol*. PMID: 40584616

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.6 |
| 高置信度残基 (pLDDT>90) 占比 | 65.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 20.7% |
| 有序区域 (pLDDT>70) 占比 | 75.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=79.6，有序区 75.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNAAF4 | 0.000 | 0.000 | — |
| DNAAF1 | 0.000 | 0.000 | — |
| DNAAF5 | 0.000 | 0.000 | — |
| ZMYND10 | 0.000 | 0.000 | — |
| LRRC6 | 0.000 | 0.000 | — |
| DNAI2 | 0.000 | 0.000 | — |
| PIH1D3 | 0.000 | 0.000 | — |
| CCDC103 | 0.000 | 0.000 | — |
| CCDC39 | 0.000 | 0.000 | — |
| CFAP298 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P49792 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q8N9W5-3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8N9W5 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 5
- 调控相关比例: 8 / 20 = 40%

**评价**: STRING 25 个预测互作，IntAct 5 个实验互作。调控相关配体占比 40%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.6 + PDB: 无 | pLDDT=79.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Dynein axonemal particle / Cytosol; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 25 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: *** (REJECTED)

**核心优势**:
1. DNAAF3 -- Dynein axonemal assembly factor 3，非常新颖，仅有少数基础研究。
2. 蛋白大小541 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N9W5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167646-DNAAF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAAF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N9W5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
