---
type: protein-evaluation
gene: "CLDN15"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLDN15 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLDN15 |
| 蛋白名称 | Claudin-15 |
| 蛋白大小 | 228 aa / 24.4 kDa |
| UniProt ID | P56746 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell junction, tight junction; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 228 aa / 24.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006187, IPR008094, IPR017974, IPR004031; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell junction, tight junction; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- bicellular tight junction (GO:0005923)
- lateral plasma membrane (GO:0016328)
- plasma membrane (GO:0005886)
- tight junction (GO:0070160)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 55 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Megaintestine in claudin-15-deficient mice.. *Gastroenterology*. PMID: 18242218
2. Ion and water permeation through claudin-10b and claudin-15 paracellular channels.. *Computational and structural biotechnology journal*. PMID: 39640531
3. Gene Expression Analysis for Uterine Cervix and Corpus Cancer Characterization.. *Genes*. PMID: 38540371
4. Multiscale modelling of claudin-based assemblies: A magnifying glass for novel structures of biological interfaces.. *Computational and structural biotechnology journal*. PMID: 36382184
5. Intestinal Epithelial Digestive, Transport, and Barrier Protein Expression Is Increased in Environmental Enteric Dysfunction.. *Laboratory investigation; a journal of technical methods and pathology*. PMID: 36870290

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 55.7% |
| 置信残基 (pLDDT 70-90) 占比 | 18.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.6% |
| 低置信 (pLDDT<50) 占比 | 12.7% |
| 有序区域 (pLDDT>70) 占比 | 73.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.8，有序区 73.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006187, IPR008094, IPR017974, IPR004031; Pfam: PF00822 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OCLN | 0.925 | 0.075 | — |
| CLDN12 | 0.862 | 0.000 | — |
| TJP1 | 0.855 | 0.051 | — |
| CLDN34 | 0.824 | 0.000 | — |
| CLDN18 | 0.822 | 0.072 | — |
| TJP3 | 0.802 | 0.051 | — |
| CLDN16 | 0.747 | 0.000 | — |
| CLDN23 | 0.735 | 0.000 | — |
| ESAM | 0.726 | 0.000 | — |
| CLDN8 | 0.714 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GEM | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SLC35B2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PLPP6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 无 | pLDDT=81.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell junction, tight junction; Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLDN15 — Claudin-15，非常新颖，仅有少数基础研究。
2. 蛋白大小228 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P56746
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106404-CLDN15/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLDN15
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P56746
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P56746-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
