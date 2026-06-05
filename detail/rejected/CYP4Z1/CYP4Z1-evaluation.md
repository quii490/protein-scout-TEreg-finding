---
type: protein-evaluation
gene: "CYP4Z1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CYP4Z1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYP4Z1 |
| 蛋白名称 | Cytochrome P450 4Z1 |
| 蛋白大小 | 505 aa / 59.1 kDa |
| UniProt ID | Q86W10 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane; Microsome membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 505 aa / 59.1 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=92.1; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Endoplasmic reticulum membrane; Microsome membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 63 |
| 别名(未计入scoring) |  |

**关键文献**:
1. In silico studies, synthesis, and biological evaluation of novel imidazopyridine-based CYP4Z1 inhibitors targeting breast cancer stem cells.. *Eur J Med Chem*. PMID: 42097058
2. The utility of genomics and functional imaging to predict sunitinib pharmacokinetics and pharmacodynamics: The predict SU study.. *Br J Clin Pharmacol*. PMID: 41485482
3. Spotting a unicorn: spatial transcriptome analysis of the eyelid reveals gene regulatory networks enriched in Moll glands.. *Brief Bioinform*. PMID: 41903186
4. Fluvastatin suppresses breast cancer initiation and progression via targeting CYP4Z1.. *Commun Biol*. PMID: 41526697
5. Elucidate biomarkers and the molecular pathways associated with genetic variants that contribute to the etiology of Parkinson's disease.. *Acta Neurol Belg*. PMID: 41026459

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.1 |
| 高置信度残基 (pLDDT>90) 占比 | 82.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.3% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 95.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.1，有序区 95.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYP4X1 | 0.000 | 0.000 | — |
| POR | 0.000 | 0.000 | — |
| AASDH | 0.000 | 0.000 | — |
| SQLE | 0.000 | 0.000 | — |
| LSS | 0.000 | 0.000 | — |
| CYP2U1 | 0.000 | 0.000 | — |
| CYP2W1 | 0.000 | 0.000 | — |
| CYP2S1 | 0.000 | 0.000 | — |
| CYP1B1 | 0.000 | 0.000 | — |
| CYP20A1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 25，IntAct interactions: 0
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.1 + PDB: 无 | pLDDT=92.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Microsome membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CYP4Z1 -- Cytochrome P450 4Z1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小505 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86W10
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186160-CYP4Z1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYP4Z1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86W10
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86W10-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
