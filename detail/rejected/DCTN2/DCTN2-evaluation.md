---
type: protein-evaluation
gene: "DCTN2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DCTN2 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCTN2 |
| 蛋白名称 | Dynactin subunit 2 |
| 蛋白大小 | 401 aa / 44.2 kDa |
| UniProt ID | Q13561 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Centrosome, Basal body; 额外: Cytosol, Connecting piece, Mid p; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | x1 | 10 | 401 aa / 44.2 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=40 篇 (<=40->8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=76.6; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Basal body; 额外: Cytosol, Connecting piece, Mid piece, Principal piece, End piece | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Membrane; Cytoplasm, cytoskeleto... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 112 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CCDC138 overexpression predicts poor prognosis and highlights ciliopathy-linked mechanisms in uterine corpus endometrial carcinoma.. *Front Mol Biosci*. PMID: 40861419
2. Machine learning-assisted multi-dimensional transcriptomic analysis of cytoskeleton-related molecules and their relationship with prognosis in hepatocellular carcinoma.. *Sci Rep*. PMID: 40610613
3. Transcriptional Landscape and Biomarker Discovery for Endoplasmic Reticulum Stress in Alzheimer's Disease: An Ex Vivo Study Using Patients-Derived Dermal Fibroblasts.. *Psychiatry Investig*. PMID: 40566894
4. Exploration of crucial stromal risk genes associated with prognostic significance and chemotherapeutic opportunities in invasive ductal breast carcinoma.. *J Genet Eng Biotechnol*. PMID: 40074422
5. Serum inflammation-related proteins in a acute compartment syndrome rat model.. *Sci Rep*. PMID: 39747444

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.6 |
| 高置信度残基 (pLDDT>90) 占比 | 25.7% |
| 置信残基 (pLDDT 70-90) 占比 | 41.9% |
| 中等置信 (pLDDT 50-70) 占比 | 26.9% |
| 低置信 (pLDDT<50) 占比 | 5.5% |
| 有序区域 (pLDDT>70) 占比 | 67.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.6，有序区 67.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCTN4 | 0.000 | 0.000 | — |
| DCTN3 | 0.000 | 0.000 | — |
| ACTR1A | 0.000 | 0.000 | — |
| DCTN1 | 0.000 | 0.000 | — |
| ACTR10 | 0.000 | 0.000 | — |
| DCTN5 | 0.000 | 0.000 | — |
| BICD2 | 0.000 | 0.000 | — |
| DCTN6 | 0.000 | 0.000 | — |
| ACTR1B | 0.000 | 0.000 | — |
| DYNC1I1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:A8K8J9 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q13561 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:P09471 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9NRI5-1 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9NRI5 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q99KJ8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P00533 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:- |
| uniprotkb:Q6AYH5 | psi-mi:"MI:0028"(cosedimentation in solution) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9PTG6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q99816 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.6 + PDB: 无 | pLDDT=76.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Centrosome, Basal body; 额外: Cytosol, Connecting pi | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

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
1. DCTN2 -- Dynactin subunit 2，非常新颖，仅有少数基础研究。
2. 蛋白大小401 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13561
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175203-DCTN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCTN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13561
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13561-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
