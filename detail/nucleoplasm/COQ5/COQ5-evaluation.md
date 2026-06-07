---
type: protein-evaluation
gene: "COQ5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COQ5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COQ5 |
| 蛋白名称 | 2-methoxy-6-polyprenyl-1,4-benzoquinol methylase, mitochondrial |
| 蛋白大小 | 327 aa / 37.1 kDa |
| UniProt ID | Q5HYK3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoli, Mitochondria; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 327 aa / 37.1 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=50 篇 (≤60→6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=82.6; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Mitochondria | Approved |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 50 |
| PubMed broad count | 55 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Ubiquinone-based gene mutation and protein compactness of CoQ5 may contribute to a novel caspofungin resistance mode in Aspergillus flavus from pulmonary aspergillosis.. *Diagn Microbiol Infect Dis*. PMID: 41690241
2. Integrating Multi-Omics Data to Uncover Causal Links Between Mitochondria-Related Genes and Chronic Obstructive Pulmonary Disease: A Mendelian Randomization Study.. *Int J Chron Obstruct Pulmon Dis*. PMID: 41868721
3. Severe Neurological Presentation in Siblings With COQ5-Related Primary Coenzyme Q10 Deficiency: Expanding Clinical and Molecular Spectrum.. *JIMD Rep*. PMID: 41199775
4. Genomic insights into chlorine resistance of a Mycobacterium sp. strain isolated from treated wastewater effluent.. *Water Res*. PMID: 40381280
5. Prenatal cannabis exposure is associated with alterations in offspring DNA methylation at genes involved in neurodevelopment, across the life course.. *Mol Psychiatry*. PMID: 39277688

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.6 |
| 高置信度残基 (pLDDT>90) 占比 | 49.5% |
| 置信残基 (pLDDT 70-90) 占比 | 31.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 14.4% |
| 有序区域 (pLDDT>70) 占比 | 80.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.6，有序区 80.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COQ7 | 0.000 | 0.000 | — |
| COQ6 | 0.000 | 0.000 | — |
| COQ3 | 0.000 | 0.000 | — |
| COQ9 | 0.000 | 0.000 | — |
| COQ4 | 0.000 | 0.000 | — |
| COQ8A | 0.000 | 0.000 | — |
| COQ8B | 0.000 | 0.000 | — |
| PDSS1 | 0.000 | 0.000 | — |
| COQ2 | 0.000 | 0.000 | — |
| PDSS2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9VYF8 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P49017 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P38820 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q949S4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9SZZ4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q04767 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P53845 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P40150 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:Q5HYK3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NZJ6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.6 + PDB: 无 | pLDDT=82.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / Nucleoli, Mitochondria | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. COQ5 -- 2-methoxy-6-polyprenyl-1,4-benzoquinol methylase, mitochondrial，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小327 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 50 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5HYK3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110871-COQ5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COQ5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5HYK3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5HYK3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5HYK3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029063;IPR004033;IPR023576; |
| Pfam | PF01209; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000110871-COQ5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| COQ4 | Intact, Biogrid | true |
| COQ6 | Intact, Biogrid | true |
| COQ9 | Intact, Biogrid | true |
| ALOX12B | Bioplex | false |
| APLNR | Bioplex | false |
| CD70 | Bioplex | false |
| COQ3 | Intact | false |
| COQ7 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
