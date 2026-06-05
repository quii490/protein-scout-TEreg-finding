---
type: protein-evaluation
gene: "CRYBB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRYBB1 — REJECTED (核定位证据不足 (核定位得分 3/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRYBB1 |
| 蛋白名称 | Beta-crystallin B1 |
| 蛋白大小 | 252 aa / 28.0 kDa |
| UniProt ID | P53674 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | x4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 252 aa / 28.0 kDa |
| 研究新颖性 | 2/10 | x5 | 10 | PubMed strict=88 篇 (≤100→2) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.9; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 27 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.0/180** | |
| **归一化总分** | | | **41.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 88 |
| PubMed broad count | 110 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Evaluating gene-disease relationship strength in crystallin genes in association with pediatric cataracts.. *Ophthalmic Genet*. PMID: 42091610
2. The Genetic Landscape of Paediatric Cataract in Saudi Arabia: A Two-Decade Cohort with Novel Variants, Genotype-Phenotype Correlations, and Bioinformatic Analysis.. *J Clin Med*. PMID: 41899338
3. Identification and functional characterization of a novel CRYBB1 deletion mutation causing autosomal dominant congenital cataract in a Chinese family.. *BMC Ophthalmol*. PMID: 41559635
4. Next-Generation Sequencing in Congenital Eye Malformations: Identification of Genetic Causes and Comparison of Different Panel-Based Diagnostic Strategies.. *Int J Mol Sci*. PMID: 41155148
5. Biological sex, microglial signaling pathways, and radiation exposure shape cortical proteomic profiles and behavior in mice.. *Brain Behav Immun Health*. PMID: 39677060

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.9 |
| 高置信度残基 (pLDDT>90) 占比 | 66.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 24.6% |
| 有序区域 (pLDDT>70) 占比 | 69.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.9，有序区 69.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BFSP2 | 0.000 | 0.000 | — |
| GJA8 | 0.000 | 0.000 | — |
| GJA3 | 0.000 | 0.000 | — |
| CRYBA1 | 0.000 | 0.000 | — |
| CRYAA | 0.000 | 0.000 | — |
| BFSP1 | 0.000 | 0.000 | — |
| CRYAB | 0.000 | 0.000 | — |
| PITX3 | 0.000 | 0.000 | — |
| TMEM114 | 0.000 | 0.000 | — |
| LIM2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q10567-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P53674 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:P05813 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96D03 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:O00471 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:O95995 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 27
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 27 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.9 + PDB: 无 | pLDDT=79.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 27 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CRYBB1 -- Beta-crystallin B1，研究基础较多，新颖性有限。
2. 蛋白大小252 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 88 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P53674
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100122-CRYBB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRYBB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P53674
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P53674-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
