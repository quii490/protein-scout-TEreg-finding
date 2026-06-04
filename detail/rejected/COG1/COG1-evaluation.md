---
type: protein-evaluation
gene: "COG1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COG1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COG1 |
| 蛋白名称 | Conserved oligomeric Golgi complex subunit 1 |
| 蛋白大小 | 980 aa / 109.0 kDa |
| UniProt ID | Q8WTW3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 8/10 | x1 | 8 | 980 aa / 109.0 kDa |
| 研究新颖性 | 2/10 | x5 | 10 | PubMed strict=82 篇 (≤100→2) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=77.3; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **69.0/180** | |
| **归一化总分** | | | **38.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 82 |
| PubMed broad count | 93 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The rewiring of a terminal selector regulatory cascade generates convergent neuronal laterality.. *PLoS Genet*. PMID: 41671266
2. Cold stress in rice (Oryza sativa L.): Molecular mechanisms of sensing, signaling, transcriptional regulation, membrane lipid remodeling, and hormonal modulation.. *Front Plant Sci*. PMID: 41560924
3. Rapid cognitive assessment: Accuracy and discriminant validity of Mini-Cog and process-based Clock Drawing Test.. *J Alzheimers Dis*. PMID: 39967041
4. The Mini-Cog: A Community Screening Tool for Dementia in Indonesia.. *Int J Geriatr Psychiatry*. PMID: 39681548
5. Author Correction: The COG1-OsSERL2 complex senses cold to trigger signaling network for chilling tolerance in japonica rice.. *Nat Commun*. PMID: 38671025

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.3 |
| 高置信度残基 (pLDDT>90) 占比 | 39.9% |
| 置信残基 (pLDDT 70-90) 占比 | 34.3% |
| 中等置信 (pLDDT 50-70) 占比 | 9.0% |
| 低置信 (pLDDT<50) 占比 | 16.8% |
| 有序区域 (pLDDT>70) 占比 | 74.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.3，有序区 74.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COG6 | 0.000 | 0.000 | — |
| COG5 | 0.000 | 0.000 | — |
| COG2 | 0.000 | 0.000 | — |
| COG4 | 0.000 | 0.000 | — |
| COG7 | 0.000 | 0.000 | — |
| COG8 | 0.000 | 0.000 | — |
| COG3 | 0.000 | 0.000 | — |
| GOSR2 | 0.000 | 0.000 | — |
| STX16 | 0.000 | 0.000 | — |
| STX5 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P53079 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9H9E3 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q9VGC3 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q04632 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P53271 | psi-mi:"MI:0363"(inferred by author) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P40094 | psi-mi:"MI:0363"(inferred by author) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q06096 | psi-mi:"MI:0363"(inferred by author) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P53951 | psi-mi:"MI:0363"(inferred by author) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P53959 | psi-mi:"MI:0363"(inferred by author) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P53195 | psi-mi:"MI:0363"(inferred by author) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.3 + PDB: 无 | pLDDT=77.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. COG1 -- Conserved oligomeric Golgi complex subunit 1，研究基础较多，新颖性有限。
2. 蛋白大小980 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 82 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WTW3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166685-COG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WTW3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
