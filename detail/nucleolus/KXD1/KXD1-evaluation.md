---
type: protein-evaluation
gene: "KXD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KXD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KXD1 / C19orf50 |
| 蛋白名称 | KxDL motif-containing protein 1 |
| 蛋白大小 | 176 aa / 19.7 kDa |
| UniProt ID | Q9BQD3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Centrosome, Cytosol; UniProt: Lysosome membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 176 aa / 19.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039843, IPR019371; Pfam: PF10241 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Centrosome, Cytosol | Approved |
| UniProt | Lysosome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- BORC complex (GO:0099078)
- cytoplasmic side of lysosomal membrane (GO:0098574)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C19orf50 |

**关键文献**:
1. Integrated analysis of single-cell and bulk RNA sequencing data reveals a pan-cancer stemness signature predicting immunotherapy response.. *Genome medicine*. PMID: 35488273
2. Transcriptomics and the mechanisms of antidepressant efficacy.. *European neuropsychopharmacology : the journal of the European College of Neuropsychopharmacology*. PMID: 26621261
3. Alternatively Expressed Transcripts Analysis of Non-Small Cell Lung Cancer Cells under Different Hypoxic Microenvironment.. *Journal of oncology*. PMID: 33936200
4. The BLOS1-interacting protein KXD1 is involved in the biogenesis of lysosome-related organelles.. *Traffic (Copenhagen, Denmark)*. PMID: 22554196

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.7 |
| 高置信度残基 (pLDDT>90) 占比 | 48.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 22.2% |
| 低置信 (pLDDT<50) 占比 | 21.6% |
| 有序区域 (pLDDT>70) 占比 | 56.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.7，有序区 56.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039843, IPR019371; Pfam: PF10241 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BORCS6 | 0.999 | 0.666 | — |
| BORCS5 | 0.999 | 0.241 | — |
| BLOC1S2 | 0.999 | 0.226 | — |
| BLOC1S1 | 0.999 | 0.288 | — |
| BORCS8 | 0.998 | 0.165 | — |
| BORCS7 | 0.998 | 0.240 | — |
| SNAPIN | 0.998 | 0.201 | — |
| RPS27A | 0.956 | 0.797 | — |
| UBA52 | 0.902 | 0.000 | — |
| TPM1 | 0.871 | 0.869 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KRT81 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| RABGEF1 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| LNX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CEP170P1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NIF3L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TPM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| IFT20 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TPM3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZC4H2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MOB1A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.7 + PDB: 无 | pLDDT=75.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Lysosome membrane / Nucleoli fibrillar center, Centrosome, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KXD1 — KxDL motif-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小176 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQD3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105700-KXD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KXD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQD3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000105700-KXD1/subcellular

![](https://images.proteinatlas.org/41507/486_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41507/486_H5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41507/490_H5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41507/490_H5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/41507/509_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41507/509_H5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BQD3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BQD3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039843;IPR019371; |
| Pfam | PF10241; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000105700-KXD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BORCS6 | Intact, Biogrid, Bioplex | true |
| CEP63 | Intact, Biogrid | true |
| EXOC5 | Intact, Biogrid | true |
| EXOC7 | Intact, Biogrid | true |
| IFT20 | Intact, Biogrid | true |
| KRT81 | Intact, Biogrid | true |
| MAP1LC3B | Intact, Biogrid | true |
| RABGEF1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
