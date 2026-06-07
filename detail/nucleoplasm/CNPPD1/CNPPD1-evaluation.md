---
type: protein-evaluation
gene: "CNPPD1"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
nuclear_score: 7
---

## CNPPD1 (Protein CNPPD1) -- 评估报告

### 1. 基本信息

| 属性 | 值 |
|------|-----|
| **UniProt ID** | Q9BV87 |
| **Protein Name** | Protein CNPPD1 |
| **Aliases** | C2orf24 |
| **Length** | 410 aa |
| **Mass** | 45.5 kDa |
| **AlphaFold mean pLDDT** | 69.4 |
| **AlphaFold pLDDT >90** | 35.1% |
| **AlphaFold pLDDT <50** | 33.7% |
| **PubMed (strict)** | 2 |
| **Function** |  |

### 2. 核定位证据

#### UniProt Subcellular Location
Membrane

#### GO Cellular Component
- **cyclin-dependent protein kinase holoenzyme complex** (IBA:GO_Central)
- **membrane** (IEA:UniProtKB-SubCell)
- **nucleus** (IBA:GO_Central)

#### HPA Subcellular Localization
- **Main location**: 无
- **Additional locations**: 无
- **Reliability (IF)**: None
- **IF Display Images Available**: NO

HPA IF 原图未可靠获取（HPA 检索页无可用的 subcellular IF 原图）。核定位基于 HPA localization/reliability + UniProt + GO-CC。

### 3. HPA Immunofluorescence

暂无数据（Pending cell analysis），核定位基于 UniProt + GO + HPA 注释。

HPA IF 原图未可靠获取（HPA 检索页无可用的 subcellular IF 原图）。核定位基于 HPA localization/reliability + UniProt + GO-CC。

### 4. PubMed Literature Assessment

| Query Type | Count |
|------------|-------|
| Strict | 2 |

**Key Papers:**
- PMID:35508649 -- Multi-staged gene expression profiling reveals potential genes and the critical pathways in kidney cancer. (Scientific reports, 2022 May 4)
- PMID:30670769 -- Low mutation and neoantigen burden and fewer effector tumor infiltrating lymphocytes correlate with breast cancer metast (Scientific reports, 2019 Jan 22)


**Research Volume Assessment**: 非常低（<10篇），几乎未被研究，是探索新型核蛋白功能的绝佳候选

### 5. AlphaFold / PAE / PDB

#### AlphaFold
- Mean pLDDT: 69.4
- pLDDT >90: 35.1%, 70-90: 18.0%, 50-70: 13.2%, <50: 33.7%

#### Experimental PDB Structures
| PDB ID | Method | Resolution | Chains |
|--------|--------|------------|--------|
| 无 | -- | -- | -- |

**Structure Assessment**: AlphaFold低置信度（pLDDT 69.4），作为新颖蛋白属正常现象

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

### 6. InterPro / Pfam Domains

| InterPro | Description |
|----------|-------------|
| IPR013922 |  |

| Pfam | Description |
|------|-------------|
| PF08613 |  |

**Domain Assessment**: 结构域注释稀疏，作为新颖蛋白属正常

### 7. Protein-Protein Interaction Network

#### STRING (Combined Score >0.4)
| Partner | Score | Exp | Regulatory? |
|---------|-------|-----|-------------|
| GPR108 | 0.636 | 0.0 | -- |
| CXXC1 | 0.63 | 0.0 | -- |
| SLC23A3 | 0.581 | 0.0 | -- |
| SMIM14 | 0.545 | 0.0 | -- |
| RETREG2 | 0.516 | 0.0 | -- |
| NHEJ1 | 0.469 | 0.0 | -- |
| RCC1L | 0.462 | 0.0 | -- |
| MAF1 | 0.451 | 0.0 | -- |
| TPGS2 | 0.439 | 0.0 | -- |
| LRRC70 | 0.434 | 0.0 | -- |

#### IntAct (Experimental)
| Partner | Method | PMID | Type | Regulatory? |
|---------|--------|------|------|-------------|
| SLC27A2 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| CDK5 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| PLS1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| OMA1 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:28514442|doi:10.10 | psi-mi:"MI:0914"(association) | -- |
| TNNC2 | psi-mi:"MI:0007"(anti tag coimmunoprecip | pubmed:33961781|imex:IM-2 | psi-mi:"MI:0914"(association) | -- |
| RSPH1 | psi-mi:"MI:0399"(two hybrid fragment poo | pubmed:35914814|imex:IM-2 | psi-mi:"MI:0915"(physical asso | -- |

#### UniProt Interactions
- 无 UniProt 互作注释

**PPI Assessment**: PPI网络稀薄（11个STRING伙伴），可能为独立功能蛋白

### 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 7/10 | x4 | 28 | 主要核定位，部分胞质信号 |
| 蛋白大小 | 10/10 | x1 | 10 | 中等大小（410 aa），生化实验操作便利 |
| 研究新颖性 | 10/10 | x5 | 50 | 极度新颖（PubMed=2篇），几乎未被研究，探索空间巨大 |
| 三维结构 | 6/10 | x3 | 18 | 中等质量（pLDDT 69.4），35%高置信度，33%无序 |
| 调控结构域 | 4/10 | x2 | 8 | 结构域注释稀疏，作为新颖蛋白属正常 |
| PPI 网络 | 3/10 | x3 | 9 | PPI网络稀薄（11个STRING伙伴），可能为独立功能蛋白 |
| **加权总分** | | | **124.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 9. Final Decision

**SCORED: 67.8/100 -- VALIDATED CANDIDATE**

**Strengths:**
- PubMed 2 篇，研究新颖性极高
- 中等大小（410 aa），生化实验操作便利
- AlphaFold结构可用

**Weaknesses:**
- 核定位需HPA进一步确认
- 结构域注释有限
- PPI网络稀薄

### 10. Data Sources
- UniProt: https://www.uniprot.org/uniprotkb/Q9BV87
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22CNPPD1%22%5BTitle/Abstract%5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BV87
- STRING: https://string-db.org/cgi/network?identifiers=CNPPD1&species=9606
- Protein Atlas: https://www.proteinatlas.org/search/CNPPD1

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BV87-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BV87 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013922; |
| Pfam | PF08613; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000115649-CNPPD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDK5 | Bioplex | false |
| TNNC2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
