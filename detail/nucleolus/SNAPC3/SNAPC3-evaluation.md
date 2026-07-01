---
type: protein-evaluation
gene: "SNAPC3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SNAPC3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SNAPC3 |
| 蛋白全称 | snRNA-activating protein complex subunit 3 |
| UniProt ID | B4DDR9 |
| 蛋白大小 | 218 aa / 24.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 218 aa|
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=8 |
| 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=63.2; PDB=0 |
| 🧬 调控结构域 | 5/10 | ×2 | 10.0 | IPR022042|
| PPI | 5/10 | ×3 | 15.0 | PPI degree=36 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 2: Evidence at transcript level |

#### 3.2 功能描述

Part of the SNAPc complex required for the transcription of both RNA polymerase II and III small-nuclear RNA genes. Binds to the proximal sequence element (PSE), a non-TATA-box basal promoter element common to these 2 types of genes. Recruits TBP and BRF2 to the U6 snRNA TATA box

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR022042 | snRNA-activating_su3 |


#### 3.4 结构信息

蛋白长度 218 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164975-SNAPC3

![](https://images.proteinatlas.org/53145/876_B5_4_red_green.jpg)
![](https://images.proteinatlas.org/53145/876_B5_6_red_green.jpg)
![](https://images.proteinatlas.org/53145/882_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/53145/882_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/53145/831_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/53145/831_B2_3_red_green.jpg)
![](https://images.proteinatlas.org/66031/1277_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/66031/1277_C7_2_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。

### 深度机制分析

**结构域架构**：SNAPC3（snRNA-activating protein complex subunit 3, 218 aa, 24.0 kDa, B4DDR9）是SNAPc（snRNA activating protein complex, 又称PTF）转录因子复合物的三个核心亚单位之一。结构域含snRNA-activating_su3（IPR022042）——这是SNAPC3特异性的保守区域，无已知结构折叠信息。AlphaFold pLDDT=63.2（较低），ESMFold pLDDT=0.55（极低）——暗示SNAPC3为单体IDP——在SNAPc复合物中通过"coupled folding-and-binding"获得稳定构象。PPI（degree=36）以SNAPc组分和RB1为核心：SNAPC1（BioGRID）和SNAPC2（BioGRID）为SNAPc其余两个亚单位——SNAPC1是最大亚基（~43 kDa, Myb domain），直接识别PSE DNA序列；SNAPC2（~38 kDa）含锌指。RB1（retinoblastoma protein, BioGRID）是核心肿瘤抑制因子——RB1-E2F complex抑制S期基因转录——SNAPC3-RB1互作暗示RB1可能将SNAPc从Pol II/III snRNA转录激活转变为抑制模式。XPO1/CRM1（exportin-1, BioGRID）为NES识别核export受体——暗示SNAPC3可能在核质-胞质间穿梭。

**TE调控展望**：SNAPc复合物负责Pol II和Pol III依赖的snRNA基因转录——而LINE-1 5'UTR含sense promoter驱动L1 mRNA（Pol II products）和antisense promoter（ASP）——ASP可驱动邻近基因的Pol II转录。SNAPC3参与的snRNA transcription machinery可能与TE来源的promoter竞争Pol II转录起始因子（如TBP, TFIIB）。UBE3A（BioGRID, HECT E3 ligase, Angelman syndrome基因）的互作暗示泛素化参与SNAPC3的转换——E3 ubiquitin ligase activity可直接影响SNAPC3的TE-proximal promoter occupancy。SUMO化（PMID 40956881, PNAS 2025）揭示SUMO conjugation to PSE-associated proteins影响snRNA转录——SUMO pathway也调控LINE-1和ERV转录——SNAPC3可能是SUMO-mediated TE transcription repression的一个辅因子。PSME3（Proteasome activator subunit 3/REGγ, BioGRID）的互作提示proteasome-dependent degradation of TE-derived peptides可能是SNAPC3的一个附加功能。

### 4. 总体评价
★★★★  **68.3/100**  **nucleolus**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: snRNA-activating protein complex subunit 3

**功能**: Part of the SNAPc complex required for the transcription of both RNA polymerase II and III small-nuclear RNA genes. Binds to the proximal sequence element (PSE), a non-TATA-box basal promoter element common to these 2 types of genes. Recruits TBP and BRF2 to the U6 snRNA TATA box

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR022042 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RB1 | BioGRID | 0 |
| SNAPC1 | BioGRID | 0 |
| SNAPC2 | BioGRID | 0 |
| HSD17B14 | BioGRID | 0 |
| CEP57L1 | BioGRID | 0 |
| PSME3 | BioGRID | 0 |
| XPO1 | BioGRID | 0 |
| UBE3A | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-B4DDR9-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 16**

| 41006818 | Integrating genetic and transcriptomic data to identify genes underlying obesity risk loci. | Int J Obes (Lond) 2025 |
| 40956881 | SUMO conjugation to promoter-proximal sequence elements-associated proteins impacts on snRNA transcription. | Proc Natl Acad Sci U S A 2025 |
| 40706988 | A Systematic, Evidence-Based Workflow for Classifying KMT2A Fusions in Acute Myeloid Leukemia. | J Mol Diagn 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SNAPC3

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/SNAPC3_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.55 |
| pLDDT > 0.9 | 0.0% |
| pLDDT < 0.5 | 29.8% |
| 残基数 | 218 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

