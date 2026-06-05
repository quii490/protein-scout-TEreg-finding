---
type: protein-evaluation
gene: "COG2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COG2 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COG2 |
| 蛋白名称 | Conserved oligomeric Golgi complex subunit 2 |
| 蛋白大小 | 738 aa / 83.2 kDa |
| UniProt ID | Q14746 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Golgi apparatus; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 738 aa / 83.2 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=80.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 65 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Rapid cognitive assessment: Accuracy and discriminant validity of Mini-Cog and process-based Clock Drawing Test.. *J Alzheimers Dis*. PMID: 39967041
2. Double-alternating injectable multifunctional hydrogel based on chitosan for skin wound repair.. *Int J Biol Macromol*. PMID: 39645136
3. The Mini-Cog: A Community Screening Tool for Dementia in Indonesia.. *Int J Geriatr Psychiatry*. PMID: 39681548
4. Validation of Candidate Host Cell Entry Factors for Bovine Herpes Virus Type-1 Based on a Genome-Wide CRISPR Knockout Screen.. *Viruses*. PMID: 38400072
5. Sociodemographic Determinants in Cervical Cancer Screening Among the Underserved West Texas Women.. *Womens Health Rep (New Rochelle)*. PMID: 37096123

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.8 |
| 高置信度残基 (pLDDT>90) 占比 | 35.5% |
| 置信残基 (pLDDT 70-90) 占比 | 49.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 9.2% |
| 有序区域 (pLDDT>70) 占比 | 85.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.8，有序区 85.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COG5 | 0.000 | 0.000 | — |
| COG6 | 0.000 | 0.000 | — |
| COG4 | 0.000 | 0.000 | — |
| COG7 | 0.000 | 0.000 | — |
| COG8 | 0.000 | 0.000 | — |
| COG1 | 0.000 | 0.000 | — |
| COG3 | 0.000 | 0.000 | — |
| STX5 | 0.000 | 0.000 | — |
| GOSR2 | 0.000 | 0.000 | — |
| COPB1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:F4JRR1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P53271 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q921L5 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9H9E3 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q14746 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q9VF78 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q21444 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8II59 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| intact:EBI-824705 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8II29 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.8 + PDB: 无 | pLDDT=80.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Golgi apparatus | 一致 |
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
1. COG2 -- Conserved oligomeric Golgi complex subunit 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小738 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14746
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135775-COG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14746
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14746-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
