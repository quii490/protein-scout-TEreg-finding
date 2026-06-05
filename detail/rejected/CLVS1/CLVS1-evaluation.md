---
type: protein-evaluation
gene: "CLVS1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLVS1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLVS1 |
| 蛋白名称 | Clavesin-1 |
| 蛋白大小 | 354 aa / 40.8 kDa |
| UniProt ID | Q8IUQ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Golgi apparatus, trans-Golgi network membrane; Cytoplasmic v |
| 蛋白大小 | 10/10 | x1 | 10 | 354 aa / 40.8 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=81.5; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Golgi apparatus, trans-Golgi network membrane; Cytoplasmic vesicle, clathrin-coated vesicle; Early e... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 7 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Genome-Wide Search for Associations with Meat Production Parameters in Karachaevsky Sheep Breed Using the Illumina BeadChip 600 K.. *Genes (Basel)*. PMID: 37372468
2. A New Prognostic Risk Score: Based on the Analysis of Autophagy-Related Genes and Renal Cell Carcinoma.. *Front Genet*. PMID: 35237298
3. Steroid-sensitive nephrotic syndrome candidate gene CLVS1 regulates podocyte oxidative stress and endocytosis.. *JCI Insight*. PMID: 34874915
4. Genetic basis of psychopathological dimensions shared between schizophrenia and bipolar disorder.. *Prog Neuropsychopharmacol Biol Psychiatry*. PMID: 30149091
5. 8q12 microduplication including CHD7: clinical report on a new patient with Duane retraction syndrome type 3.. *Mol Cytogenet*. PMID: 24206642

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.5 |
| 高置信度残基 (pLDDT>90) 占比 | 72.6% |
| 置信残基 (pLDDT 70-90) 占比 | 2.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 22.3% |
| 有序区域 (pLDDT>70) 占比 | 75.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.5，有序区 75.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLTC | 0.000 | 0.000 | — |
| N4BP2L1 | 0.000 | 0.000 | — |
| AP1G1 | 0.000 | 0.000 | — |
| IGSF21 | 0.000 | 0.000 | — |
| TMEM92 | 0.000 | 0.000 | — |
| AP1S2 | 0.000 | 0.000 | — |
| AP1S3 | 0.000 | 0.000 | — |
| AP1S1 | 0.000 | 0.000 | — |
| ZNF618 | 0.000 | 0.000 | — |
| AP1M1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9NZD4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8IUQ0 | psi-mi:"MI:0089"(protein array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 4
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.5 + PDB: 无 | pLDDT=81.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, trans-Golgi network membrane; Cyt / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 4 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLVS1 -- Clavesin-1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小354 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IUQ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177182-CLVS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLVS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IUQ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IUQ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
