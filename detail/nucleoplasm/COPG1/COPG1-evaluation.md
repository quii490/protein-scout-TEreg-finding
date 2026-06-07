---
type: protein-evaluation
gene: "COPG1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COPG1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COPG1 / COPG |
| 蛋白名称 | Coatomer subunit gamma-1 |
| 蛋白大小 | 874 aa / 97.7 kDa |
| UniProt ID | Q9Y678 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Golgi apparatus membrane; Cytoplasmic vesicle, CO |
| 蛋白大小 | 8/10 | x1 | 8 | 874 aa / 97.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=15 篇 (<=20->10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=87.9; PDB: 1R4X |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR011989, IPR016024, IPR002553, IPR013041, IPR009 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Golgi apparatus membrane; Cytoplasmic vesicle, COPI-coated vesicle membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- COPI vesicle coat (GO:0030126)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- endoplasmic reticulum-Golgi intermediate compartment (GO:0005793)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- transport vesicle (GO:0030133)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COPG |

**关键文献**:
1. A new severe congenital neutropenia syndrome associated with autosomal recessive COPZ1 mutations.. *Blood*. PMID: 39642330
2. A proteome-wide association study identifies putative causal proteins for breast cancer risk.. *British journal of cancer*. PMID: 39468330
3. Coatomer protein complex I is required for efficient secretion of dengue virus non-structural protein 1.. *Journal of virology*. PMID: 40838750
4. COPG1 Is a Selectively Essential Regulator of Cancer Progression and Chemoresistance via Redox Modulation and AKT Signaling.. *International journal of molecular sciences*. PMID: 41751842
5. [Malignant solitary fibrous tumors: a clinicopathological and molecular genetic analysis].. *Zhonghua bing li xue za zhi = Chinese journal of pathology*. PMID: 35673723

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.9 |
| 高置信度残基 (pLDDT>90) 占比 | 59.6% |
| 置信残基 (pLDDT 70-90) 占比 | 34.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 4.3% |
| 有序区域 (pLDDT>70) 占比 | 94.3% |
| 可用 PDB 条目 | 1R4X |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.9，有序区 94.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR002553, IPR013041, IPR009028; Pfam: PF01602, PF16381, PF08752 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARCN1 | 0.999 | 0.942 | — |
| COPB1 | 0.999 | 0.960 | — |
| COPB2 | 0.999 | 0.954 | — |
| COPA | 0.998 | 0.950 | — |
| COPZ1 | 0.998 | 0.953 | — |
| COPE | 0.996 | 0.935 | — |
| COPZ2 | 0.991 | 0.885 | — |
| COPG2 | 0.977 | 0.843 | — |
| TMED10 | 0.914 | 0.638 | — |
| GBF1 | 0.897 | 0.611 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BRF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ILK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PHB2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MAGED1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSTK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.9 + PDB: 1R4X | pLDDT=87.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Golgi apparatus membrane; Cytoplasmic v / Golgi apparatus; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. COPG1 -- Coatomer subunit gamma-1，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小874 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y678
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181789-COPG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COPG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y678
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y678-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y678 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011989;IPR016024;IPR002553;IPR013041;IPR009028;IPR032154;IPR017106;IPR013040;IPR037067;IPR012295; |
| Pfam | PF01602;PF16381;PF08752; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000181789-COPG1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARCN1 | Biogrid, Opencell, Bioplex | true |
| ATL2 | Biogrid, Opencell | true |
| CFTR | Intact, Biogrid | true |
| COPA | Biogrid, Opencell | true |
| COPB1 | Biogrid, Opencell, Bioplex | true |
| COPB2 | Biogrid, Opencell, Bioplex | true |
| COPE | Biogrid, Opencell, Bioplex | true |
| COPG2 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
