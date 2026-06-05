---
type: protein-evaluation
gene: "CYP4F22"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CYP4F22 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYP4F22 |
| 蛋白名称 | Ultra-long-chain fatty acid omega-hydroxylase |
| 蛋白大小 | 531 aa / 62.0 kDa |
| UniProt ID | Q6NT55 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane; Microsome membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 531 aa / 62.0 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=93.5; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 22 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

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
1. Identification of Pathogenic Variants in CYP4F22, FLG, ALOX12B, and NIPAL4 in a Case Series of Inherited Ichthyosis.. *Int J Mol Sci*. PMID: 42196615
2. Comparison of cytochrome P450 activity and mRNA expression in canine vs. human hepatocytes after acetaminophen, diclofenac, or valproic acid exposure.. *J Vet Sci*. PMID: 41947679
3. The curious family of cytochrome P450 4F fatty acid ω-hydroxylases: recent developments in their function and relevance for human health.. *Open Biol*. PMID: 40858268
4. Exploration of functional cytochrome P450 4F enzymes in liver, intestine, and kidney from dogs, cats, pigs, and tree shrews and comparison of their metabolic capacities with human P450 4F2 and 4F12.. *Biochem Pharmacol*. PMID: 40154889
5. A case report and literature review of self-improving collodion baby in the newborn.. *Medicine (Baltimore)*. PMID: 40193669

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.5 |
| 高置信度残基 (pLDDT>90) 占比 | 78.3% |
| 置信残基 (pLDDT 70-90) 占比 | 20.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.5，有序区 99.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NIPAL4 | 0.000 | 0.000 | — |
| ABCA12 | 0.000 | 0.000 | — |
| TGM1 | 0.000 | 0.000 | — |
| PNPLA1 | 0.000 | 0.000 | — |
| LIPN | 0.000 | 0.000 | — |
| ALOXE3 | 0.000 | 0.000 | — |
| ALOX12B | 0.000 | 0.000 | — |
| CERS3 | 0.000 | 0.000 | — |
| SDR9C7 | 0.000 | 0.000 | — |
| SULT2B1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9BRK0 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96MV1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q6NT55 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q13520 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q15800 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 22
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 22 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.5 + PDB: 无 | pLDDT=93.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Microsome membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 22 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CYP4F22 -- Ultra-long-chain fatty acid omega-hydroxylase，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小531 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6NT55
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171954-CYP4F22/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYP4F22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6NT55
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6NT55-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
