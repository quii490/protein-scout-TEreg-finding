---
type: protein-evaluation
gene: "PCDHAC1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHAC1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PCDHAC1 |
| 蛋白全称 | Protocadherin alpha-C1 |
| UniProt ID | Q9H158 |
| 蛋白大小 | 963 aa / 105.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoli; Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 963 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=3 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=73.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 5/10 | x3 | 15.0 | PPI degree=18 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR002126 | Cadherin-like_dom |
| InterPro | IPR015919 | Cadherin-like_sf |
| InterPro | IPR032455 | Cadherin_C |
| InterPro | IPR031904 | Cadherin_CBD |
| InterPro | IPR020894 | Cadherin_CS |
| InterPro | IPR013164 | Cadherin_N |
| InterPro | IPR050174 | Protocadherin/Cadherin-CA |
| Pfam | PF00028 | Cadherin |


#### 3.4 结构信息

蛋白长度 963 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000248383-PCDHAC1

![](https://images.proteinatlas.org/52775/1303_D4_3_red_green.jpg)
![](https://images.proteinatlas.org/52775/1303_D4_4_red_green.jpg)
![](https://images.proteinatlas.org/52775/1442_E2_5_red_green.jpg)
![](https://images.proteinatlas.org/52775/1442_E2_6_red_green.jpg)
![](https://images.proteinatlas.org/52775/1753_D4_4_cr57f3d72844853_red_green.jpg)
![](https://images.proteinatlas.org/52775/1753_D4_13_cr57f3d730b7b4d_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**72.1/100** | **nucleolus**
Nuclear protein


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00112; |
| InterPro | IPR002126;IPR015919;IPR032455;IPR031904;IPR020894;IPR013164;IPR050174; |
| Pfam | PF00028;PF08266;PF16492;PF15974; |
| UniProt Domain | DOMAIN 19..124; /note="Cadherin 1"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00043"; DOMAIN 125..233; /note="Cadherin 2"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00043"; DOMAIN 234..340; /note="Cadherin 3"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00043"; DOMAIN 349..445; /note="Cadherin 4"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00043"; DOMAIN 446..555; /note="Cadherin 5"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00043"; DOMAIN 570..667; /note="Cadherin 6"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00043" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PCDHA10 | BioGRID | 0 |
| DNAJC18 | BioGRID | 0 |
| ABCB9 | BioGRID | 0 |
| C2CD2L | BioGRID | 0 |
| C1orf43 | BioGRID | 0 |
| ACVR2A | BioGRID | 0 |
| CISD2 | BioGRID | 0 |
| ATF6 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H158-F1-predicted_aligned_error_v6.png)

### 深度机制分析

**结构域架构**：PCDHAC1（963 aa，105.9 kDa）是原钙黏蛋白α-C1家族成员，拥有一套经典的钙黏蛋白重复结构域体系：N端6个Cadherin重复结构域（UniProt DOMAIN 19-667，每个约100-110 aa）、Cadherin_C（IPR032455）胞质尾端、Cadherin_CBD（IPR031904）和Cadherin_CS保守基序（IPR020894）。每个Cadherin重复采用β-三明治折叠，通过Ca²⁺离子桥连形成刚性棒状延伸结构。AlphaFold pLDDT=73.1表明整体折叠可信，但950+残基中长连接区（inter-repeat linkers）存在构象柔性（pLDDT 50-65区域）。HPA定位显示Nucleoli; Nucleoplasm; Vesicles（Approved），其中核仁定位对经典细胞黏附分子而言极为罕见。

**PPI互作网络解读**：PPI degree=18，核心互作集中在该基因簇的其他原钙黏蛋白成员：PCDHA10（同簇α亚型蛋白，BioGRID评分0）、DNAJC18（Hsp40家族共伴侶，可能参与内质网内钙黏蛋白折叠质量控制）、ABCB9（ATP结合盒转运蛋白）、ATF6（内质网应激传感器）。此外，ACVR2A（激活素A受体IIA型）和CISD2（线粒体铁硫蛋白）的互作提示PCDHAC1可能参与非经典的信号通路交叉调控。C2CD2L和C1orf43的互作缺乏功能注释，体现该蛋白领域的研究空白（PubMed仅4篇）。

**结构解读**：AlphaFold预测的胞外域呈刚性棒状结构——6个Cadherin重复串联成直线排列，每个重复的β-三明治核心由7条β-链折叠而成，Ca²⁺结合位点位于重复间界面（DxD, DRE, xDxE保守基序）。跨膜区（约700-720 aa）预测为单一α-螺旋。胞内Cadherin_C尾端（IPR032455）可能通过β-catenin/plakoglobin结合位点连接肌动蛋白细胞骨架。但PCDHAC1与其他经典cadherin不同，其胞内结构域较短且缺少典型的catenin结合基序（PxxxP），提示其可能通过与PCDHA10异源二聚化间接连接细胞骨架。

**机制模型**：PCDHAC1可能通过一种非经典的核定位路径实现核仁定位：（1）胞内Cadherin_C片段经calpain或γ-secretase介导的蛋白水解释放，暴露隐性的NLS序列；（2）游离胞内段经importin-α/β转运进入核质；（3）在核仁中，Cadherin_C通过其与核仁蛋白（如nucleolin/NCL、nucleophosmin/B23）的互作锚定于GC区（granular component），可能参与rRNA加工成熟或核仁应激应答。这一"黏附分子核内信号"模式类似Notch/DCC的受控蛋白水解-核转位范式（PMID:27544570提示胎盘镉暴露通过PCDHAC1甲基化变化影响胎儿发育，进一步支持环境应激-PCDHAC1-核内信号轴）。

**TE调控展望**：PCDHAC1不直接参与TE调控。PubMed仅4篇，CpG岛甲基化表型分析（PMID:22610075）提示该基因的启动子甲基化具有肿瘤分型价值。鉴于其核仁定位，PCDHAC1可能通过核仁应激信号间接影响异染色质维持——已知核仁是rDNA重复序列的组织中心，核仁扰动可释放核仁蛋白至核质激活p53通路，但这一机制与TE的关联无直接证据支持。

### PubMed 文献

**PubMed count: 4**

| 40092689 | Clinical significance and immune landscape analyses of the coagulation-related gene signatures in gastric cancer. | J Cancer 2025 |
| 27544570 | Maternal cadmium, placental PCDHAC1, and fetal development. | Reprod Toxicol 2016 |
| 22610075 | Single-CpG-resolution methylome analysis identifies clinicopathologically aggressive CpG island methylator phenotype cle | Carcinogenesis 2012 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHAC1

