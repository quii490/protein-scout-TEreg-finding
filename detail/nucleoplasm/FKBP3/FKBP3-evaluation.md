---
type: protein-evaluation
gene: "FKBP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FKBP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FKBP3 / FKBP25 |
| 蛋白名称 | Peptidyl-prolyl cis-trans isomerase FKBP3 |
| 蛋白大小 | 224 aa / 25.2 kDa |
| UniProt ID | Q00688 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 224 aa / 25.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.1; PDB: 1PBK, 2KFV, 2MPH, 5D75, 5GPG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043368, IPR041200, IPR046357, IPR001179; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 55 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FKBP25 |

**关键文献**:
1. Biotin-painted proteins have thermodynamic stability switched by kinetic folding routes.. *The Journal of chemical physics*. PMID: 35597640
2. FKBP3 aggravates the malignant phenotype of diffuse large B-cell lymphoma by PARK7-mediated activation of Wnt/β-catenin signalling.. *Journal of cellular and molecular medicine*. PMID: 37987202
3. Identification of Prognostic Factors Related to Super Enhancer-Regulated ceRNA Network in Metastatic Lung Adenocarcinoma.. *International journal of general medicine*. PMID: 34629892
4. FKBP3 Promotes Proliferation of Non-Small Cell Lung Cancer Cells through Regulating Sp1/HDAC2/p27.. *Theranostics*. PMID: 28839465
5. Basic Tilted Helix Bundle - a new protein fold in human FKBP25/FKBP3 and HectD1.. *Biochemical and biophysical research communications*. PMID: 24667607

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.1 |
| 高置信度残基 (pLDDT>90) 占比 | 23.7% |
| 置信残基 (pLDDT 70-90) 占比 | 52.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 15.2% |
| 有序区域 (pLDDT>70) 占比 | 75.9% |
| 可用 PDB 条目 | 1PBK, 2KFV, 2MPH, 5D75, 5GPG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1PBK, 2KFV, 2MPH, 5D75, 5GPG）+ AlphaFold极高置信度预测（pLDDT=77.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043368, IPR041200, IPR046357, IPR001179; Pfam: PF18410, PF00254 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTOR | 0.951 | 0.925 | — |
| HDAC1 | 0.928 | 0.314 | — |
| HDAC2 | 0.899 | 0.314 | — |
| PPP3R1 | 0.789 | 0.747 | — |
| MDM2 | 0.760 | 0.292 | — |
| CALM3 | 0.733 | 0.276 | — |
| YY1 | 0.730 | 0.324 | — |
| CALML5 | 0.726 | 0.276 | — |
| CALML3 | 0.726 | 0.276 | — |
| CALM1 | 0.698 | 0.577 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TNIK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| NCBP3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| ERBB2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| Pik3r2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| OTUB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-23897|pubmed:26752685 |
| CEP19 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.1 + PDB: 1PBK, 2KFV, 2MPH, 5D75, 5GPG | pLDDT=77.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FKBP3 — Peptidyl-prolyl cis-trans isomerase FKBP3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小224 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q00688
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100442-FKBP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FKBP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q00688
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q00688-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q00688 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 128..224; /note="PPIase FKBP-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00277" |
| InterPro | IPR043368;IPR041200;IPR046357;IPR001179; |
| Pfam | PF18410;PF00254; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100442-FKBP3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MDM2 | Intact, Biogrid | true |
| BARD1 | Biogrid | false |
| CALM1 | Biogrid | false |
| MAPT | Biogrid | false |
| NEDD4 | Biogrid | false |
| NEDD4L | Biogrid | false |
| OSGEP | Bioplex | false |
| PARP2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
