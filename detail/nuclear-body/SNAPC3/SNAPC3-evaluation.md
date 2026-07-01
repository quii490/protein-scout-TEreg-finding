---
type: protein-evaluation
gene: "SNAPC3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## SNAPC3 (snRNA-activating protein complex subunit 3) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SNAPC3 |
| 蛋白全称 | snRNA-activating protein complex subunit 3 |
| UniProt ID | B4DDR9 |
| 蛋白大小 | 218 aa / 24.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 218 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 4/10 | x2 | 8.0 | InterPro:IPR022042 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **116/180** | |
| **归一化总分 (/1.83)** | | | **63.4/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Part of the SNAPc complex required for the transcription of both RNA polymerase II and III small-nuclear RNA genes. Binds to the proximal sequence element (PSE), a non-TATA-box basal promoter element common to these 2 types of genes. Recruits TBP and BRF2 to the U6 snRNA TATA box

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR022042 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: snRNA-activating protein complex subunit 3

**功能**: Part of the SNAPc complex required for the transcription of both RNA polymerase II and III small-nuclear RNA genes. Binds to the proximal sequence element (PSE), a non-TATA-box basal promoter element common to these 2 types of genes. Recruits TBP and BRF2 to the U6 snRNA TATA box

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR022042 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000164975-SNAPC3
定位: location reactome" data-name="nucleoplasm,nuclear_bodies">

![](https://images.proteinatlas.org/53145/876_B5_4_red_green.jpg)
![](https://images.proteinatlas.org/53145/876_B5_6_red_green.jpg)
![](https://images.proteinatlas.org/53145/882_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/53145/882_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/53145/831_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/53145/831_B2_3_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR022042; |
| Pfam | PF12251; |
| UniProt Domain [FT] | 未检出 |


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


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SNAPC3

### PubMed

**Count: 16**

| PMID | Title |
|---|---|
| 41006818 | Integrating genetic and transcriptomic data to identify genes underlying obesity risk loci. |
| 40956881 | SUMO conjugation to promoter-proximal sequence elements-associated proteins impacts on snRNA transcription. |
| 40706988 | A Systematic, Evidence-Based Workflow for Classifying KMT2A Fusions in Acute Myeloid Leukemia. |
| 38903089 | Integrating Genetic and Transcriptomic Data to Identify Genes Underlying Obesity Risk Loci. |
| 34937578 | DNA methylation mediates the association between breastfeeding and early-life growth trajectories. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/SNAPC3_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.55 |
| pLDDT > 0.9 占比 | 0.0% |
| pLDDT < 0.5 占比 | 29.8% |
| 建模残基数 | 218 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。


### 深度机制分析

SNAPC3是snRNA激活蛋白复合体（SNAPc）的核心亚基之一，其深度机制分析必须置于SNAPc全酶的组装和功能框架中。SNAPc由五个亚基组成（SNAPC1至SNAPC5），负责同时激活RNA聚合酶II和III转录的snRNA基因——这在真核转录机制中是罕见的双聚合酶特异性。SNAPC3的UniProt功能注释明确指出其参与SNAPc复合体的形成，结合snRNA基因启动子中的近端序列元件（PSE, proximal sequence element），并招募TBP和BRF2至U6 snRNA的TATA框。然而，SNAPC3本身仅含有一个注释结构域InterPro:IPR022042（Pfam:PF12251），意味着其可能在SNAPc中作为结构支架亚基，而DNA结合活性主要由其他亚基（如SNAPC1/SNAPC4）提供。

ESMFold结构预测揭示了SNAPC3的一个重要弱点：全局pLDDT仅0.55，高置信残基（pLDDT>0.9）占比0%，近30%残基pLDDT<0.5。这种广泛的结构无序性并非偶然——在转录调控复合体中，支架亚基常以固有无序区域（IDRs）介导多价蛋白-蛋白互作，通过"模糊复合体"（fuzzy complex）机制维持复合体组装灵活性。SNAPC3的低结构有序度恰与其支架角色一致，但也意味着基于结构的药物设计面临困难。

PPI互作网络BioGRID数据（所有评分均为0）显示SNAPC3与SNAPC1和SNAPC2存在直接互作——这完全符合SNAPc复合体的已知组成。此外，RB1（视网膜母细胞瘤蛋白）、XPO1（核输出受体CRM1）和PSME3（PA28γ蛋白酶体激活因子）的出现值得关注。RB1是一个经典的转录共抑制因子，能够通过与SNAPc的互作抑制RNA Pol III转录，将细胞周期调控与snRNA合成耦联。XPO1/CRM1可能参与了SNAPc亚基的核质穿梭调控。PSME3/PA28γ作为一种核内蛋白酶体激活因子，参与非泛素依赖的蛋白降解，其与SNAPC3的互作可能调控SNAPc亚基的稳定性。

PubMed文献中，PMID 40956881报道了关键发现：SUMO化修饰（SUMO conjugation）作用于PSE相关蛋白并影响snRNA转录。SUMO化是核内蛋白的重要翻译后修饰，调控蛋白定位、活性和复合体组装。SNAPc组分（包括SNAPC3）的SUMO化可能精细调控snRNA基因的转录活性，进而间接影响含有PSE样元件的TE启动子活性——部分TE家族（如Alu元件）的Pol III依赖性转录依赖于PSE样启动子结构。这一机制为SNAPC3在TE调控中的潜在角色提供了初步的理论基础。

尽管如此，多项因素限制了SNAPC3作为TE调控靶标的开发价值：极低的结构有序度（pLDDT=0.55）、仅有BioGRID评分0的低置信PPI数据、缺乏直接TE调控文献、以及GO-CC中无核定位注释（虽然其snRNA转录功能必然发生于核内）。推荐等级2/5（63.4/100）反映了新颖性（10/10）与上述劣势之间的平衡。深度机制模型为：SNAPC3作为SNAPc支架亚基，通过IDRs介导复合体组装→SNAPc结合PSE→招募Pol II/III机制→转录snRNA基因→可能的SUMO化调控→间接影响含PSE样元件的TE转录。



- UniProt: https://www.uniprot.org/uniprotkb/B4DDR9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B4DDR9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SNAPC3
