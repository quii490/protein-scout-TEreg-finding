---
type: protein-evaluation
gene: "SUPT4H1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUPT4H1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUPT4H1 / SPT4H, SUPT4H |
| 蛋白名称 | Transcription elongation factor SPT4 |
| 蛋白大小 | 117 aa / 13.2 kDa |
| UniProt ID | P63272 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 117 aa / 13.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.5; PDB: 3H7H, 5OIK, 6GMH, 6GML, 6TED, 7OKY, 7UND |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029040, IPR009287, IPR022800, IPR038510; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **152.0/180** | |
| **归一化总分** | | | **84.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- DSIF complex (GO:0032044)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPT4H, SUPT4H |

**关键文献**:
1. Revealing the effects of lactate on bovine SCNT embryo development through transcriptome sequencing analyses.. *Theriogenology*. PMID: 39951848
2. A fly model of SCA36 reveals combinatorial neurotoxicity of hexanucleotide and dipeptide repeats.. *PLoS genetics*. PMID: 41337098
3. Biallelic SUPT4H1 variants cause a multisystem neurodevelopmental disorder associated with disrupted transcription.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 41842694
4. A Transcriptome-Wide Association Study Identifies Novel Candidate Susceptibility Genes for Pancreatic Cancer.. *Journal of the National Cancer Institute*. PMID: 31917448
5. Transcriptome-Wide Association Study Identified Novel Blood Tissue Gene Biomarkers for Prostate Cancer Risk.. *The Prostate*. PMID: 39878408

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.5 |
| 高置信度残基 (pLDDT>90) 占比 | 94.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 3H7H, 5OIK, 6GMH, 6GML, 6TED, 7OKY, 7UND, 7YCX, 8A3Y, 8P4C |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3H7H, 5OIK, 6GMH, 6GML, 6TED, 7OKY, 7UND, 7YCX, 8A3Y, 8P4C）+ AlphaFold极高置信度预测（pLDDT=96.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029040, IPR009287, IPR022800, IPR038510; Pfam: PF06093 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUPT6H | 0.999 | 0.978 | — |
| POLR2B | 0.999 | 0.990 | — |
| POLR2D | 0.999 | 0.988 | — |
| SUPT5H | 0.999 | 0.998 | — |
| POLR2A | 0.999 | 0.992 | — |
| POLR2C | 0.998 | 0.989 | — |
| RTF1 | 0.998 | 0.948 | — |
| POLR2G | 0.998 | 0.989 | — |
| POLR2I | 0.998 | 0.987 | — |
| POLR2E | 0.997 | 0.988 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ANXA5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| SUPT5H | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:10075709|imex:IM-19325 |
| MFHAS1 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| PAK5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMA16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DOK4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FGF9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Rprd1b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| LRRK2 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.5 + PDB: 3H7H, 5OIK, 6GMH, 6GML, 6TED,  | pLDDT=96.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. SUPT4H1 — Transcription elongation factor SPT4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小117 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P63272
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213246-SUPT4H1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUPT4H1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P63272
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000213246-SUPT4H1/subcellular

![](https://images.proteinatlas.org/59748/1017_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/59748/1017_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/59748/1043_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/59748/1043_A8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P63272-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P63272 |
| SMART | SM01389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029040;IPR009287;IPR022800;IPR038510; |
| Pfam | PF06093; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000213246-SUPT4H1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SUPT5H | Intact, Biogrid, Opencell | true |
| POLR2K | Opencell | false |
| RNGTT | Biogrid | false |
| SEM1 | Opencell | false |
| SNRPA | Opencell | false |
| SNRPC | Opencell | false |
| SNRPF | Opencell | false |
| SOCS2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
