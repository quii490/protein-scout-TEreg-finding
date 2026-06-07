---
type: protein-evaluation
gene: "FERD3L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FERD3L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FERD3L / BHLHA31, NATO3, NTWIST |
| 蛋白名称 | Fer3-like protein |
| 蛋白大小 | 166 aa / 19.0 kDa |
| UniProt ID | Q96RJ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 166 aa / 19.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHA31, NATO3, NTWIST |

**关键文献**:
1. HDAC9, TWIST1 and FERD3L gene expression in asymptomatic stable and unstable carotid plaques.. *Inflammation research : official journal of the European Histamine Research Society ... [et al.]*. PMID: 26621503
2. SLC17A3 rs9379800 and Ischemic Stroke Susceptibility at the Northern Region of Malaysia.. *Journal of stroke and cerebrovascular diseases : the official journal of National Stroke Association*. PMID: 34384670
3. A two-gene epigenetic signature for the prediction of response to neoadjuvant chemotherapy in triple-negative breast cancer patients.. *Clinical epigenetics*. PMID: 30786922
4. Mapping transcription factor functions in astrocytes using in vivo gain-of-function Perturb-seq.. *Science (New York, N.Y.)*. PMID: 42024736
5. Rs10230207 genotype confers changes in HDAC9 and TWIST1, but not FERD3L in lymphoblasts from patients with intracranial aneurysm.. *Neurogenetics*. PMID: 30919159

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.0 |
| 高置信度残基 (pLDDT>90) 占比 | 35.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.8% |
| 中等置信 (pLDDT 50-70) 占比 | 25.3% |
| 低置信 (pLDDT<50) 占比 | 28.3% |
| 有序区域 (pLDDT>70) 占比 | 46.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.0，有序区 46.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050283, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FAM9B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| USP19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NES | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DMWD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CORO2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HEXIM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCF12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGEB4 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 11
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.0 + PDB: 无 | pLDDT=70.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 11 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FERD3L — Fer3-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小166 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96RJ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146618-FERD3L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FERD3L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96RJ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96RJ6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96RJ6 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 101..153; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR050283;IPR036638; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000146618-FERD3L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TCF4 | Intact, Biogrid | true |
| FAM9B | Intact | false |
| MAGEB4 | Intact | false |
| SGTA | Intact | false |
| TCF12 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
