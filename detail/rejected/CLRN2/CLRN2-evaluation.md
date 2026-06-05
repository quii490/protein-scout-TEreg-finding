---
type: protein-evaluation
gene: "CLRN2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLRN2 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLRN2 |
| 蛋白名称 | Clarin-2 |
| 蛋白大小 | 232 aa / 25.4 kDa |
| UniProt ID | A0PK11 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell projection, stereocilium membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 232 aa / 25.4 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=91.3; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 16 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cell projection, stereocilium membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 8 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Compensatory Interplay Between Clarin-1 and Clarin-2 Deafness-Associated Proteins Governs Phenotypic Variability in Hearing.. *Adv Sci (Weinh)*. PMID: 41572507
2. A significant genomic region underlying growth traits in adult Beijing You chicken identified by genome-wide association analysis.. *Poult Sci*. PMID: 40561828
3. A novel CLRN2 variant: expanding the mutation spectrum and its critical role in isolated hearing impairment.. *Genes Genomics*. PMID: 39446282
4. Clarin-2 gene supplementation durably preserves hearing in a model of progressive hearing loss.. *Mol Ther*. PMID: 38243601
5. A biallelic variant in CLRN2 causes non-syndromic hearing loss in humans.. *Hum Genet*. PMID: 33496845

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.3 |
| 高置信度残基 (pLDDT>90) 占比 | 80.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 91.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.3，有序区 91.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CACNG2 | 0.000 | 0.000 | — |
| GRXCR2 | 0.000 | 0.000 | — |
| USH1C | 0.000 | 0.000 | — |
| STRC | 0.000 | 0.000 | — |
| CEP295NL | 0.000 | 0.000 | — |
| TMC1 | 0.000 | 0.000 | — |
| PPP1R17 | 0.000 | 0.000 | — |
| KLHDC7B | 0.000 | 0.000 | — |
| CHRNA10 | 0.000 | 0.000 | — |
| CHRNA9 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8N386 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q9UHP7-3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9Y3P8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9H7M9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q8N6S5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:O00501 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q8WWF3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:P26715 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:P27105 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8TBE3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 16，IntAct interactions: 30
- 调控相关比例: 2 / 16 = 12%

**评价**: STRING 16 个预测互作，IntAct 30 个实验互作。调控相关配体占比 12%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.3 + PDB: 无 | pLDDT=91.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, stereocilium membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 16 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLRN2 -- Clarin-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小232 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0PK11
- Protein Atlas: https://www.proteinatlas.org/ENSG00000249581-CLRN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLRN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0PK11
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A0PK11-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
