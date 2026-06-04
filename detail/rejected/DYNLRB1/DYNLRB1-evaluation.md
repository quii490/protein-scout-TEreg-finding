---
type: protein-evaluation
gene: "DYNLRB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DYNLRB1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYNLRB1 |
| 蛋白名称 | Dynein light chain roadblock-type 1 |
| 蛋白大小 | 148 aa / 16.3 kDa |
| UniProt ID | B1AKR6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 8/10 | ×1 | 8 | 148 aa / 16.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.3; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 41 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Inhibition of TGF-beta signaling protects from alpha-synuclein induced toxicity.. *Cell Death Discov*. PMID: 41387695
2. Integrative machine learning approach for forecasting lung cancer chemosensitivity: From algorithm to cell line validation.. *Comput Struct Biotechnol J*. PMID: 40778317
3. Selection Signatures in Italian Goat Populations Sharing the "facciuto" Phenotype.. *Genes (Basel)*. PMID: 40282350
4. Multi-omic characteristics of longitudinal immune profiling after breakthrough infections caused by Omicron BA.5 sublineages.. *EBioMedicine*. PMID: 39536392
5. Compartmentalization proteomics revealed endolysosomal protein network changes in a goat model of atrial fibrillation.. *iScience*. PMID: 38827406

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.7% |
| 置信残基 (pLDDT 70-90) 占比 | 60.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 33.8% |
| 有序区域 (pLDDT>70) 占比 | 61.5% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 预测质量有限（pLDDT=68.3），有序残基占 61.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DYNC1I2 | 0.000 | 0.000 | — |
| DYNC1H1 | 0.000 | 0.000 | — |
| DYNLL1 | 0.000 | 0.000 | — |
| WDR60 | 0.000 | 0.000 | — |
| WDR34 | 0.000 | 0.000 | — |
| DYNC1LI2 | 0.000 | 0.000 | — |
| DYNC2LI1 | 0.000 | 0.000 | — |
| DYNC1I1 | 0.000 | 0.000 | — |
| DYNLT1 | 0.000 | 0.000 | — |
| DYNC1LI1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9NP97 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q5NIP8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P62628 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:A0A5P8YCS1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P43356 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q8WW35 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.3 + PDB: 无 | pLDDT=68.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DYNLRB1 — Dynein light chain roadblock-type 1，非常新颖，仅有少数基础研究。
2. 蛋白大小148 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/B1AKR6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125971-DYNLRB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYNLRB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B1AKR6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
