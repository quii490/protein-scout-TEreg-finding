---
type: protein-evaluation
gene: "FAM81A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM81A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM81A |
| 蛋白名称 | Protein FAM81A |
| 蛋白大小 | 368 aa / 42.4 kDa |
| UniProt ID | Q8TBF8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Postsynaptic density; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 368 aa / 42.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029619 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Postsynaptic density; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- glutamatergic synapse (GO:0098978)
- postsynaptic density (GO:0014069)
- postsynaptic density, intracellular component (GO:0099092)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Integrative network pharmacology, transcriptomics, and proteomics reveal the material basis and mechanism of the Shen Qing Weichang Formula against gastric cancer.. *Chinese medicine*. PMID: 40155922
2. FAM81A is a postsynaptic protein that regulates the condensation of postsynaptic proteins via liquid-liquid phase separation.. *PLoS biology*. PMID: 38452102
3. A susceptibility gene signature for ERBB2-driven mammary tumour development and metastasis in collaborative cross mice.. *EBioMedicine*. PMID: 39067134
4. Exploring the Genetic Association between Obesity and Serum Lipid Levels Using Bivariate Methods.. *Twin research and human genetics : the official journal of the International Society for Twin Studies*. PMID: 36606461
5. FAM81A identified as a stemness-related gene by screening DNA methylation sites based on machine learning-accessed stemness in pancreatic cancer.. *Epigenomics*. PMID: 35574683

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.4 |
| 高置信度残基 (pLDDT>90) 占比 | 53.8% |
| 置信残基 (pLDDT 70-90) 占比 | 23.1% |
| 中等置信 (pLDDT 50-70) 占比 | 13.6% |
| 低置信 (pLDDT<50) 占比 | 9.5% |
| 有序区域 (pLDDT>70) 占比 | 76.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.4，有序区 76.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029619 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OR5C1 | 0.596 | 0.596 | — |
| OR52B2 | 0.591 | 0.591 | — |
| PTPN20 | 0.530 | 0.000 | — |
| C9orf153 | 0.507 | 0.000 | — |
| LMBR1L | 0.502 | 0.000 | — |
| TMEM179 | 0.475 | 0.000 | — |
| CDRT1 | 0.471 | 0.000 | — |
| GPR171 | 0.463 | 0.000 | — |
| TOR2A | 0.462 | 0.000 | — |
| TMEM88B | 0.460 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| Syngap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| ZNF655 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| RCOR3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TXLNA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NAP1L2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| STX1B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PCM1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TFIP11 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| OR5C1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.4 + PDB: 无 | pLDDT=82.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Postsynaptic density; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. FAM81A — Protein FAM81A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小368 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TBF8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157470-FAM81A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM81A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TBF8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000157470-FAM81A/subcellular

![](https://images.proteinatlas.org/65797/1263_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/65797/1263_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/65797/1270_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/65797/1270_B4_4_red_green.jpg)
![](https://images.proteinatlas.org/65797/1718_B4_14_cr57f3f1c3802e6_red_green.jpg)
![](https://images.proteinatlas.org/65797/1718_B4_18_cr57f3f1cd3eb72_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TBF8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TBF8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029619; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000157470-FAM81A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NAP1L2 | Intact | false |
| STX1B | Intact | false |
| TFIP11 | Intact | false |
| TXLNA | Intact | false |
| ZNF655 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
