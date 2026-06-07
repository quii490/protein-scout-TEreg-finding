---
type: protein-evaluation
gene: "FBXO46"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO46 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO46 / FBX46, FBXO34L |
| 蛋白名称 | F-box only protein 46 |
| 蛋白大小 | 603 aa / 64.6 kDa |
| UniProt ID | Q6PJ61 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 603 aa / 64.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=44.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR039594; Pfam: PF12937 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX46, FBXO34L |

**关键文献**:
1. FBXO46 negatively regulates p53 activity by stabilizing Mdm2.. *FEBS letters*. PMID: 39548735
2. PPA1, TRIM68 and FBXO46: Potential Therapeutic Targets for Triple Negative Breast Cancer.. *Current protein & peptide science*. PMID: 39754775
3. Coordination of Single-cell and Bulk RNA Sequencing to Construct a Cuproptosis-related Gene Prognostic Index for Endometrial Cancer Prognosis, Immune Microenvironment Infiltration, and Immunotherapy Treatment Options.. *Journal of Cancer*. PMID: 37859813
4. The SCF(FBXO46) ubiquitin ligase complex mediates degradation of the tumor suppressor FBXO31 and thereby prevents premature cellular senescence.. *The Journal of biological chemistry*. PMID: 30171069
5. Identification and Clinical Validation of a Novel 4 Gene-Signature with Prognostic Utility in Colorectal Cancer.. *International journal of molecular sciences*. PMID: 31387239

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 44.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.8% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 77.3% |
| 有序区域 (pLDDT>70) 占比 | 12.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=44.9），有序残基占 12.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR039594; Pfam: PF12937 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.910 | 0.794 | — |
| CUL1 | 0.881 | 0.705 | — |
| ASB6 | 0.494 | 0.000 | — |
| KLHL29 | 0.483 | 0.000 | — |
| C11orf1 | 0.445 | 0.000 | — |
| TWISTNB | 0.437 | 0.000 | — |
| FBXO42 | 0.422 | 0.000 | — |
| THOC7 | 0.422 | 0.000 | — |
| KIAA1257 | 0.418 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18850735|imex:IM-20477 |
| SKP1 | psi-mi:"MI:0231"(mammalian protein protein interac | pubmed:19159283|imex:IM-20301 |
| CAPZA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| FSD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EMILIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NEXN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SDC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Myh9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Myo1c | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Arrb2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 15
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=44.9 + PDB: 无 | pLDDT=44.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Vesicles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 9 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBXO46 — F-box only protein 46，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小603 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=44.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PJ61
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177051-FBXO46/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO46
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PJ61
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000177051-FBXO46/subcellular

![](https://images.proteinatlas.org/49390/1047_H6_3_red_green.jpg)
![](https://images.proteinatlas.org/49390/1047_H6_4_red_green.jpg)
![](https://images.proteinatlas.org/49390/1048_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/49390/1048_H6_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6PJ61-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PJ61 |
| SMART | SM00256; |
| UniProt Domain [FT] | DOMAIN 470..522; /note="F-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00080" |
| InterPro | IPR036047;IPR001810;IPR039594; |
| Pfam | PF12937; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177051-FBXO46/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SKP1 | Intact, Biogrid, Bioplex | true |
| CUL1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
