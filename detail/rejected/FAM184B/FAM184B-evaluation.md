---
type: protein-evaluation
gene: "FAM184B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM184B — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM184B / KIAA1276 |
| 蛋白名称 | Protein FAM184B |
| 蛋白大小 | 1060 aa / 121.0 kDa |
| UniProt ID | Q9ULE4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 1060 aa / 121.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039478; Pfam: PF15665 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1276 |

**关键文献**:
1. Genome-Wide Association Study to Identify QTL for Carcass Traits in Korean Hanwoo Cattle.. *Animals : an open access journal from MDPI*. PMID: 37685003
2. Association Analyses between Single Nucleotide Polymorphisms in ZFAT, FBN1, FAM184B Genes and Litter Size of Xinggao Mutton Sheep.. *Animals : an open access journal from MDPI*. PMID: 38066991
3. Aberrant AHRR, ADAMTS2 and FAM184 DNA Methylation: Candidate Biomarkers in the Oral Rinse of Heavy Smokers.. *Biomedicines*. PMID: 37509437
4. Genetic architectures and selection signatures of body height in Chinese indigenous donkeys revealed by next-generation sequencing.. *Animal genetics*. PMID: 35535569
5. Global gene expression changes in the prefrontal cortex of rabbits with hypercholesterolemia and/or hypertension.. *Neurochemistry international*. PMID: 27890723

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 49.7% |
| 置信残基 (pLDDT 70-90) 占比 | 14.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 28.7% |
| 有序区域 (pLDDT>70) 占比 | 64.5% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.8，有序区 64.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039478; Pfam: PF15665 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LCORL | 0.777 | 0.000 | — |
| DCAF16 | 0.759 | 0.000 | — |
| NCAPG | 0.747 | 0.045 | — |
| MED28 | 0.594 | 0.000 | — |
| PACRGL | 0.588 | 0.157 | — |
| SPTY2D1 | 0.461 | 0.099 | — |
| MEPE | 0.457 | 0.000 | — |
| CCDC87 | 0.451 | 0.000 | — |
| IBSP | 0.450 | 0.122 | — |
| FAM13A | 0.444 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| Rab8b | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26885862|imex:IM-24977 |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35063084|imex:IM-29773 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 无 | pLDDT=73.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FAM184B — Protein FAM184B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1060 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULE4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000047662-FAM184B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM184B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULE4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9ULE4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
