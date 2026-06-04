---
type: protein-evaluation
gene: "DENND11"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DENND11 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DENND11 |
| 蛋白名称 | DENN domain-containing protein 11 |
| 蛋白大小 | 455 aa / 51.4 kDa |
| UniProt ID | A4D1U4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 455 aa / 51.4 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=1 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=77.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 19 partners; IntAct 22 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 2 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Impact of life adversity and gene expression on psychiatric symptoms in children and adolescents: findings from the Brazilian high risk cohort study.. *Front Psychiatry*. PMID: 40018685

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.8 |
| 高置信度残基 (pLDDT>90) 占比 | 60.4% |
| 置信残基 (pLDDT 70-90) 占比 | 12.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 21.8% |
| 有序区域 (pLDDT>70) 占比 | 72.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.8，有序区 72.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AVL9 | 0.000 | 0.000 | — |
| DENND10 | 0.000 | 0.000 | — |
| DENND6A | 0.000 | 0.000 | — |
| VAMP1 | 0.000 | 0.000 | — |
| RIC1 | 0.000 | 0.000 | — |
| SCAND1 | 0.000 | 0.000 | — |
| YKT6 | 0.000 | 0.000 | — |
| RAB33B | 0.000 | 0.000 | — |
| VAMP4 | 0.000 | 0.000 | — |
| RAB30 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:A4D1U4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:C9J7X6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 19，IntAct interactions: 22
- 调控相关比例: 0 / 19 = 0%

**评价**: STRING 19 个预测互作，IntAct 22 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.8 + PDB: 无 | pLDDT=77.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus | 待确认 |
| PPI | STRING + IntAct | 19 + 22 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: *** (REJECTED)

**核心优势**:
1. DENND11 -- DENN domain-containing protein 11，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小455 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A4D1U4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000257093-DENND11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DENND11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A4D1U4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
