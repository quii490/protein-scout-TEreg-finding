---
type: protein-evaluation
gene: "DNAJB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJB1 — REJECTED (研究热度过高 (PubMed strict=308，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJB1 |
| 蛋白名称 | DnaJ homolog subfamily B member 1 |
| 蛋白大小 | 340 aa / 38.0 kDa |
| UniProt ID | P25685 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | x1 | 10 | 340 aa / 38.0 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=308 篇 (>100->REJECTED) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=82.6; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Nucleus, nucleolus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 308 |
| PubMed broad count | 461 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Dysregulation of mRNAs and hub genes in Parkinson's disease within post mortem substantia Nigra: using three methods differential expression genes analysis.. *Neurosci Lett*. PMID: 41980674
2. Carney complex with PRKAR1A variant and breast/fibrolamellar carcinomas.. *Hum Genome Var*. PMID: 42209451
3. Amide Hydrogen-Deuterium Exchange in Isotopically Mixed Water.. *ACS Phys Chem Au*. PMID: 42221934
4. Metastatic Fibrolamellar Hepatocellular Carcinoma in a Young Adult: A Case Report and Narrative Review.. *J Hepatocell Carcinoma*. PMID: 42117090
5. Identification of integrated stress response-related prognostic genes in high-grade serous ovarian cancer using Mendelian randomization, single-cell RNA sequencing, and bulk RNA sequencing.. *Front Oncol*. PMID: 42164124

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.6 |
| 高置信度残基 (pLDDT>90) 占比 | 58.5% |
| 置信残基 (pLDDT 70-90) 占比 | 19.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 14.7% |
| 有序区域 (pLDDT>70) 占比 | 78.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.6，有序区 78.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.000 | 0.000 | — |
| HSP90AA1 | 0.000 | 0.000 | — |
| HSP90AB1 | 0.000 | 0.000 | — |
| HSPA4 | 0.000 | 0.000 | — |
| HSPA1B | 0.000 | 0.000 | — |
| STIP1 | 0.000 | 0.000 | — |
| BAG1 | 0.000 | 0.000 | — |
| HSPH1 | 0.000 | 0.000 | — |
| HSPA1A | 0.000 | 0.000 | — |
| HSPA6 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 25，IntAct interactions: 0
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 0 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.6 + PDB: 无 | pLDDT=82.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus, nucleolus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ** (REJECTED)

**核心优势**:
1. DNAJB1 -- DnaJ homolog subfamily B member 1，研究基础较多，新颖性有限。
2. 蛋白大小340 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 308 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 308 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P25685
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132002-DNAJB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P25685
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P25685-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P25685 |
| SMART | SM00271; |
| UniProt Domain [FT] | DOMAIN 2..70; /note="J"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00286" |
| InterPro | IPR002939;IPR001623;IPR018253;IPR051339;IPR008971;IPR036869; |
| Pfam | PF00226;PF01556; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132002-DNAJB1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BAG2 | Biogrid, Opencell | true |
| BAG5 | Biogrid, Opencell | true |
| BCKDK | Biogrid, Bioplex | true |
| CDC37 | Intact, Biogrid, Opencell | true |
| DNAJB4 | Biogrid, Opencell, Bioplex | true |
| DNAJB5 | Biogrid, Opencell | true |
| HSPA1L | Biogrid, Opencell | true |
| HSPA2 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
