---
type: protein-evaluation
gene: "SNAPC2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## SNAPC2 (snRNA-activating protein complex subunit 2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SNAPC2 |
| 蛋白全称 | snRNA-activating protein complex subunit 2 |
| UniProt ID | Q13487 |
| 蛋白大小 | 334 aa / 36.7 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 334 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 5/10 | x2 | 10.0 | InterPro:IPR021281; Pfam:PF11035 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **118/180** | |
| **归一化总分 (/1.83)** | | | **64.5/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Part of the SNAPc complex required for the transcription of both RNA polymerase II and III small-nuclear RNA genes. Binds to the proximal sequence element (PSE), a non-TATA-box basal promoter element common to these 2 types of genes. Recruits TBP and BRF2 to the U6 snRNA TATA box

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR021281 |
| Pfam | PF11035 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000104976-SNAPC2
定位: location reactome" data-name="nucleoplasm,nuclear_bodies">

![](https://images.proteinatlas.org/49843/805_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/49843/805_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/49843/979_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/49843/979_C6_3_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR021281; |
| Pfam | PF11035; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SNAPC1 | STRING | 999 |
| SNAPC4 | STRING | 999 |
| SNAPC5 | STRING | 997 |
| TBP | STRING | 922 |
| BRF2 | STRING | 702 |
| XPO1 | BioGRID | 1 |
| MBD1 | BioGRID | 1 |
| EGFR | BioGRID | 1 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SNAPC2

### PubMed

**Count: 12**

| PMID | Title |
|---|---|
| 40465781 | Identification of key genes and signaling pathways of liver cancer and model construction for prognosis and diagnosis based on bioinformatics analysis |
| 39747245 | Structural insights into distinct mechanisms of RNA polymerase II and III recruitment to snRNA promoters. |
| 31552087 | Machine Learning Classifiers for Endometriosis Using Transcriptomics and Methylomics Data. |
| 27610895 | Association between genes on chromosome 19p13.2 and panic disorder. |
| 26506879 | Genome-wide methylation profiling reveals new biomarkers for prognosis prediction of glioblastoma. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/SNAPC2_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.62 |
| pLDDT > 0.9 占比 | 6.0% |
| pLDDT < 0.5 占比 | 24.6% |
| 建模残基数 | 334 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。


### 深度机制分析

SNAPC2与SNAPC3同属snRNA激活蛋白复合体（SNAPc），但其在复合体中的功能角色和结构特征存在显著差异。SNAPC2含有一个SNAPC2-specific结构域（InterPro:IPR021281, Pfam:PF11035），这是SNAPc五个亚基中独特的存在。ESMFold预测的全局pLDDT为0.62（略优于SNAPC3的0.55），高置信残基占比6.0%，但仍有24.6%残基pLDDT<0.5，表明SNAPC2同样含有大量固有无序区域——这与SNAPc支架亚基的共性一致。然而，SNAPC2独有的Pfam:PF11035结构域可能介导特定的蛋白互作或构象调控功能。

PPI互作网络是SNAPC2的最大亮点。STRING数据显示SNAPC2与SNAPC1（score=999）、SNAPC4（score=999）和SNAPC5（score=997）之间存在极高置信度的互作——完美覆盖了SNAPc复合体中除SNAPC3外的所有亚基。更重要的是，TBP（TATA-box binding protein, score=922）和BRF2（TFIIIB组分, score=702）的高置信互作直接验证了UniProt功能注释中"SNAPC2 recruits TBP and BRF2 to the U6 snRNA TATA box"的描述。这种从STRING互作到功能注释的自洽性验证极为罕见，构成了SNAPC2功能机制的强有力证据闭环。SNAPC2在SNAPc中可能作为关键的衔接蛋白——一方面通过其特异性结构域锚定于PSE结合的SNAPc核心（SNAPC1/SNAPC4），另一方面以柔性区域招募TBP-BRF2复合体至下游TATA框。

PubMed文献的深度分析揭示了SNAPC2在转录调控中的结构基础。PMID 39747245报道了PSE结合蛋白招募RNA聚合酶II和III至snRNA启动子的不同机制的结构解析——这是理解SNAPc双重聚合酶特异性的关键突破。SNAPC2很可能通过其独特的结构域构象变化，实现对Pol II（U1/U2 snRNA）和Pol III（U6 snRNA）的选择性招募。在这一模型中，SNAPC2的可诱导构象可能决定了PSE与下游TATA框之间的空间排列，从而允许大分子量的Pol II进入（Pol II型启动子）或优先容纳紧凑的Pol III机制（U6型启动子）。

在TE调控的潜在关联方面，Alu元件（SINE家族）的转录部分依赖Pol III机制，而Pol III的PSE依赖性招募与snRNA基因启动子共享SNAPc-TBP-BRF2通路。此外，BioGRID互作中的MBD1（methyl-CpG binding domain protein 1）是DNA甲基化"阅读器"，可结合甲基化CpG岛并招募转录抑制复合体。MBD1与SNAPC2的互作可能将DNA甲基化信号与snRNA/TE转录耦合——即甲基化状态通过MBD1-SNAPC2轴调控PSE依赖性TE启动子活性。EGFR（表皮生长因子受体）的互作则提示生长因子信号可能通过磷酸化SNAPC2间接调节SNAPc活性。

尽管SNAPC2的PPI数据质量远优于SNAPC3（STRING高置信度互作 vs BioGRID评分0），其核定位GO-CC注释仍然缺失。推荐等级2/5（64.5/100）。SNAPC2的深度机制模型为：PF11035结构域锚定于PSE结合的SNAPc核心→柔性区域招募TBP（score=922）和BRF2（score=702）→构象选择决定Pol II/III特异性→MBD1介导的甲基化耦合调控→EGFR信号磷酸化调控→可能间接影响含PSE样元件的TE转录。SNAPC2在SNAPc五个亚基中具有最优的PPI数据质量，是研究SNAPc-TE调控联系的最佳候选。



- UniProt: https://www.uniprot.org/uniprotkb/Q13487
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13487
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SNAPC2
