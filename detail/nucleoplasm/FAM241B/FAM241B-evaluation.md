---
type: protein-evaluation
gene: "FAM241B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM241B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM241B / C10orf35 |
| 蛋白名称 | Protein FAM241B |
| 蛋白大小 | 121 aa / 13.2 kDa |
| UniProt ID | Q96D05 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Centrosome; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 121 aa / 13.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027953, IPR052502; Pfam: PF15378 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome; 额外: Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf35 |

**关键文献**:
1. Protein family FAM241 in human and mouse.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 39715844
2. Glioblastoma Prognosis and Therapeutic Response Predicted by a Cancer-Associated Fibroblasts Risk Score.. *Mediators of inflammation*. PMID: 41498024
3. Screening the hub genes and analyzing the mechanisms in discharged COVID-19 patients retesting positive through bioinformatics analysis.. *Journal of clinical laboratory analysis*. PMID: 35657140
4. Single-cell analysis of gene expression in the substantia nigra pars compacta of a pesticide-induced mouse model of Parkinson's disease.. *Translational neuroscience*. PMID: 36117858
5. Genome-wide association study of blood lipids in Indians confirms universality of established variants.. *Journal of human genetics*. PMID: 30911093

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.5 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 51.2% |
| 中等置信 (pLDDT 50-70) 占比 | 20.7% |
| 低置信 (pLDDT<50) 占比 | 28.1% |
| 有序区域 (pLDDT>70) 占比 | 51.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.5），有序残基占 51.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027953, IPR052502; Pfam: PF15378 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LRRC69 | 0.527 | 0.000 | — |
| PRRT1 | 0.518 | 0.518 | — |
| TEX26 | 0.506 | 0.000 | — |
| PLSCR5 | 0.476 | 0.000 | — |
| WLS | 0.474 | 0.474 | — |
| FAM149B1 | 0.448 | 0.000 | — |
| FAM160A2 | 0.446 | 0.000 | — |
| ARL6IP5 | 0.435 | 0.435 | — |
| TMEM170A | 0.429 | 0.422 | — |
| TMEM208 | 0.423 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PA | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| IFITM3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| ERBB2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| ERBB3 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| ERBB4 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| HTR3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LPAR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNF5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SCN3B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM234 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.5 + PDB: 无 | pLDDT=65.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Centrosome; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM241B — Protein FAM241B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小121 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96D05
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171224-FAM241B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM241B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96D05
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000171224-FAM241B/subcellular

![](https://images.proteinatlas.org/34591/428_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/34591/428_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/34591/433_C5_3_red_green.jpg)
![](https://images.proteinatlas.org/34591/433_C5_4_red_green.jpg)
![](https://images.proteinatlas.org/34591/440_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/34591/440_C5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96D05-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96D05 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027953;IPR052502; |
| Pfam | PF15378; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171224-FAM241B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACKR2 | Bioplex | false |
| ADORA2B | Bioplex | false |
| APLNR | Bioplex | false |
| ARL6IP5 | Bioplex | false |
| ATP5PB | Bioplex | false |
| ATP6V0C | Bioplex | false |
| C5AR1 | Bioplex | false |
| CCR3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
