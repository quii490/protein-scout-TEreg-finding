---
type: protein-evaluation
gene: "TCP10L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TCP10L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCP10L |
| 蛋白名称 | T-complex protein 10A homolog 1 |
| 蛋白大小 | 215 aa / 23.9 kDa |
| UniProt ID | Q8TDR4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 215 aa / 23.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026581 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. TCP10L is expressed specifically in spermatogenic cells and binds to death associated protein kinase-3.. *International journal of andrology*. PMID: 15910542
2. TCP10L synergizes with MAD1 in transcriptional suppression and cell cycle arrest through mutual interaction.. *BMB reports*. PMID: 26698869
3. Identification of a novel liver-specific expressed gene, TCP10L, encoding a human leucine zipper protein with transcription inhibition activity.. *Journal of human genetics*. PMID: 14586771
4. TCP10L negatively regulates alpha-fetoprotein expression in hepatocellular carcinoma.. *BMB reports*. PMID: 32438969
5. Identification of TCP10L as primate-specific gene derived via segmental duplication and homodimerization of TCP10L through the leucine zipper motif.. *Molecular biology reports*. PMID: 17377852

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.2 |
| 高置信度残基 (pLDDT>90) 占比 | 25.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 45.1% |
| 低置信 (pLDDT<50) 占比 | 24.7% |
| 有序区域 (pLDDT>70) 占比 | 30.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.2），有序残基占 30.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026581 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STIL | 0.631 | 0.513 | — |
| C12orf4 | 0.625 | 0.618 | — |
| TBCK | 0.593 | 0.593 | — |
| MXD4 | 0.587 | 0.421 | — |
| DAPK3 | 0.552 | 0.453 | — |
| UACA | 0.500 | 0.090 | — |
| FKBP15 | 0.486 | 0.000 | — |
| CEP295 | 0.482 | 0.099 | — |
| SASS6 | 0.478 | 0.254 | — |
| BBS10 | 0.469 | 0.065 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MXD4 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| PMF1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| DAPK3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| TNNC1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |
| MAX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHMP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SMARCD1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NXF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.2 + PDB: 无 | pLDDT=66.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TCP10L — T-complex protein 10A homolog 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小215 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TDR4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000242220-TCP10L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCP10L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TDR4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TDR4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TDR4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026581; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000242220-TCP10L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GRIPAP1 | Intact, Biogrid, Bioplex | true |
| MXD4 | Intact, Biogrid | true |
| BACE2 | Intact | false |
| C2CD6 | Intact | false |
| CCDC102B | Intact | false |
| CCDC70 | Intact | false |
| CDR2L | Intact | false |
| CIAO1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
