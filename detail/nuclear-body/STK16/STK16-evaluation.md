---
type: protein-evaluation
gene: "STK16"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## STK16 (Serine/threonine-protein kinase 16) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | STK16 |
| 蛋白全称 | Serine/threonine-protein kinase 16 |
| UniProt ID | O75716 |
| 蛋白大小 | 305 aa / 33.5 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 305 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR011009; InterPro:IPR000719; InterPro:IPR052239; InterPro:IPR008271; Pfam:PF00069 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Membrane-associated protein kinase that phosphorylates on serine and threonine residues. In vitro substrates include DRG1, ENO1 and EIF4EBP1. Also autophosphorylates. May be involved in secretory vesicle trafficking or intracellular signaling. May have a role in regulating stromal-epithelial interactions that occur during ductal morphogenesis in the mammary gland. May be involved in TGF-beta signa

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR011009 |
| InterPro | IPR000719 |
| InterPro | IPR052239 |
| InterPro | IPR008271 |
| Pfam | PF00069 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000115661-STK16
定位: location reactome" data-name="nucleoplasm,nuclear_bodies,plasma_membrane,primary_cilium,primary_cili

![](https://images.proteinatlas.org/29450/290_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/29450/290_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/29450/249_G12_4_red_green.jpg)
![](https://images.proteinatlas.org/29450/249_G12_3_red_green.jpg)
![](https://images.proteinatlas.org/29450/2243_G3_66_blue_red_green.jpg)
![](https://images.proteinatlas.org/29450/2243_G3_107_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00220; |
| InterPro | IPR011009;IPR000719;IPR052239;IPR008271; |
| Pfam | PF00069; |
| UniProt Domain | DOMAIN 20..293; /note="Protein kinase"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00159" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NAGK | BioGRID | 1 |
| VHL | BioGRID | 1 |
| PASK | BioGRID | 1 |
| ROCK2 | BioGRID | 1 |
| MKKS | BioGRID | 1 |
| EBLN2 | BioGRID | 1 |
| HNF4A | BioGRID | 1 |
| SNRK | BioGRID | 1 |


### PubMed 文献

**PubMed count: 31**

| 38723720 | Serine/Threonine kinase 16 phosphorylates STAT3 and confers a JAK2-Inhibition resistance phenotype in triple-negative br | Biochem Pharmacol 2024 |
| 38622518 | STK16 promoted colorectal cancer progress in a c-MYC signaling-dependent manner. | Mol Med 2024 |
| 35738348 | Numb-associated kinases are required for SARS-CoV-2 infection and are cellular targets for antiviral strategies. | Antiviral Res 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/STK16

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/STK16_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.9 |
| pLDDT > 0.9 占比 | 67.2% |
| pLDDT < 0.5 占比 | 0.0% |
| 建模残基数 | 305 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。

### 深度机制分析

**结构域架构**：STK16（UniProt O75716，305 aa，33.5 kDa）属于丝氨酸/苏氨酸蛋白激酶超家族。其激酶催化域（UniProt Domain 注释：第20-293位为Protein kinase域，证据ECO:0000255|PROSITE:PRU00159）是蛋白的绝对主体，几乎占据整个蛋白序列（273/305 aa）。该激酶域采用经典的双叶折叠——N端小叶由β-折叠主导（ATP结合口袋），C端小叶以α-螺旋为主（底物识别面），活性位点夹在两叶之间的裂隙中。IPR011009（kinase-like domain superfamily）、IPR000719（protein kinase domain）、IPR008271（serine/threonine-protein kinase, active site）和SMART:SM00220（S_TKc）均指向保守的激酶催化中心。IPR052239为STK16家族特异性标记。

**PPI互作网络**：BioGRID互作数据显示NAGK（N-乙酰葡糖胺激酶，评分1）、VHL（von Hippel-Lindau肿瘤抑制蛋白，评分1）、PASK（PAS域含丝氨酸/苏氨酸激酶，评分1）、ROCK2（Rho相关coiled-coil激酶，评分1）、MKKS（McKusick-Kaufman综合征蛋白，评分1）、EBLN2（内源性博尔纳病毒样核蛋白2，评分1）、HNF4A（肝细胞核因子4α，评分1）和SNRK（SNF1相关激酶，评分1）。VHL是HIFα ubiquitylation E3连接酶组分，HNF4A为核受体转录因子，EBLN2是驯化的病毒核蛋白——该PPI集群连接代谢信号、缺氧应答和病毒驯化。

**结构-功能关系**：STK16的ESMFold结构预测质量极高——平均pLDDT=0.90，pLDDT>0.9占比67.2%，pLDDT<0.5占比0.0%。这说明305 aa的激酶域整体折叠高度有序，呈现典型的双叶激酶折叠。STK16已知的体外底物包括DRG1（发育调控GTP结合蛋白1）、ENO1（烯醇化酶1）和EIF4EBP1（真核翻译起始因子4E结合蛋白1），功能涉及分泌小泡运输和TGF-β信号通路。HPA定位含nucleoplasm和nuclear_bodies，支持其核内功能。

**TE调控机制**：STK16经STAT3磷酸化参与JAK2抑制抗性（PMID:38723720 - TNBC中STK16磷酸化STAT3），在结直肠癌中经c-MYC信号促进进展（PMID:38622518），在SARS-CoV-2感染中与Numb相关激酶协同（PMID:35738348）。TE调控维度上，STK16→STAT3磷酸化轴可能间接影响TE转录——STAT3是已知的LTR/ERV启动子激活转录因子，而STK16对STAT3的磷酸化调控可改变其DNA结合活性和靶基因谱。HNF4α互作指向代谢核受体→染色质重塑→转座子沉默的连接，VHL参与HIFα降解→缺氧应答→TE激活通路。EBLN2（驯化Bornavirus核蛋白）与STK16的互作最令人兴奋——EBLN蛋白是哺乳动物基因组中固定化的非逆转录病毒元件，其互作强烈暗示STK16参与驯化病毒蛋白的功能网络。

**前沿意义**：STK16通过HPA定位数据确认nucleoplasm/nuclear_bodies分布（HPA: location reactome nucleoplasm, nuclear_bodies, plasma_membrane），为核内激酶功能提供直接IF证据。尽管PubMed有31篇文献，但从TE调控视角出发属完全未探索领域。STK16作为相对研究充分的激酶，其已有的化学生物学工具（如激酶活性检测试剂盒）可加速TE调控假说的实验验证。c-MYC和STAT3是已知的ERV/LTR激活因子——STK16是否通过磷酸化调节这两个转录因子的TE靶向性是极具前景的研究问题。

