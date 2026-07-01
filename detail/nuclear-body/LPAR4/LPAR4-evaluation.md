---
type: protein-evaluation
gene: "LPAR4"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## LPAR4 (Lysophosphatidic acid receptor 4) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | LPAR4 |
| 蛋白全称 | Lysophosphatidic acid receptor 4 |
| UniProt ID | Q99677 |
| 蛋白大小 | 370 aa / 40.7 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 370 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 6/10 | x2 | 12.0 | InterPro:IPR000276; InterPro:IPR017452; Pfam:PF00001 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **120/180** | |
| **归一化总分 (/1.83)** | | | **65.6/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Receptor for lysophosphatidic acid (LPA), a mediator of diverse cellular activities. Transduces a signal by increasing the intracellular calcium ions and by stimulating adenylyl cyclase activity. The rank order of potency for agonists of this receptor is 1-oleoyl- > 1-stearoyl- > 1-palmitoyl- > 1-myristoyl- > 1-alkyl- > 1-alkenyl-LPA

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR000276 |
| InterPro | IPR017452 |
| Pfam | PF00001 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000147145-LPAR4

![](https://images.proteinatlas.org/46563/1595_C10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46563/1595_C10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/46563/1500_A12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/46563/1500_A12_5_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM01381; |
| InterPro | IPR000276;IPR017452; |
| Pfam | PF00001; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GNAS | STRING | 924 |
| BCL6 | BioGRID | 1 |
| BAG3 | BioGRID | 1 |
| ATM | BioGRID | 1 |
| RTCA | BioGRID | 1 |
| PPP2R5E | BioGRID | 1 |
| BTAF1 | BioGRID | 1 |
| PRKDC | BioGRID | 1 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/LPAR4

### PubMed

**Count: 97**

| PMID | Title |
|---|---|
| 42284392 | LPAR4 mediates resistance to interferon-induced stress in soft tissue sarcoma. |
| 42228231 | Lysophosphatidic Acid Reduces Ischemic Brain Injury by Attenuating Vascular Permeability Through LPA4 Receptor Signaling. |
| 42034529 | Lysophosphatidic acid mitigates vascular permeability and allergic rhinitis in mice. |
| 41871909 | mRNA 3' UTRs direct microRNA degradation to participate in imprinted gene networks and regulate growth. |
| 41528806 | Lysophosphatidic acid-mediated NF-κB activation promotes FOXC2 expression essential for lymphatic valve development. |

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/LPAR4_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.85 |
| pLDDT > 0.9 占比 | 33.2% |
| pLDDT < 0.5 占比 | 0.0% |
| 建模残基数 | 370 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。

### 深度机制分析

LPAR4是一个典型的七次跨膜G蛋白偶联受体（GPCR），其结构域架构由IPR000276/IPR017452（GPCR家族）和Pfam:PF00001（7TM受体）定义，SMART注释为SM01381。ESMFold预测的全局pLDDT=0.85（33.2%残基pLDDT>0.9），提示跨膜螺旋区域折叠良好，但胞内环区和C端尾部可能具有较大的构象柔性——这是GPCR家族的共性特征。作为溶血磷脂酸（LPA）受体，LPAR4以1-oleoyl-LPA>1-stearoyl-LPA>1-palmitoyl-LPA的效能顺序结合配体，激活后通过G蛋白偶联信号增加胞内钙离子浓度并刺激腺苷酸环化酶活性。其7TM结构域直接决定了配体识别和信号转导的分子机制，但与核定位或DNA结合功能完全无关。

PPI互作网络中最显著的发现是LPAR4与GNAS的STRING互作（combined score=924），后者编码刺激性G蛋白α亚基（Gsα），是GPCR信号转导的核心下游效应器。这一高置信度互作与LPAR4的GPCR功能注释高度一致——LPA结合后通过Gsα激活腺苷酸环化酶-cAMP通路。其他BioGRID互作（评分均为1）包括BCL6（转录抑制因子）、BAG3（共分子伴侣）、ATM（DNA损伤激酶）、RTCA（RNA末端磷酸环化酶）、PPP2R5E（PP2A调控亚基）、BTAF1（TBP相关因子）和PRKDC（DNA-PK催化亚基），功能分散且缺乏与GPCR信号通路的逻辑一致性，提示这些可能为非特异性高通量互作。

Pubmed文献分析揭示了LPAR4在疾病中的重要功能。PMID 42284392报道LPAR4介导软组织肉瘤对干扰素诱导应激的抵抗，PMID 42228231发现LPA通过LPA4受体信号减轻缺血性脑损伤中的血管通透性，PMID 41528806证实LPA介导的NF-κB激活通过LPAR4促进FOXC2表达以支持淋巴管瓣膜发育。这些研究共同描绘了LPAR4在血管生物学、炎症和肿瘤微环境中的核心角色，但其作用位点均为质膜——作为跨膜受体接收胞外LPA信号并启动胞内信号级联。

从亚细胞定位角度审视，LPAR4是经典的质膜整合膜蛋白，其七次跨膜拓扑结构决定了其无法以可溶形式进入细胞核。该蛋白缺乏任何核定位信号序列或DNA结合结构域，在GO-CC中亦无核定位注释。核定位特异性评分4/10仅为基线值。综合来看，LPAR4的深度机制模型是一个质膜LPA受体，通过Gsα-cAMP和Gq-Ca2+通路调控下游生物学过程，与核内TE调控无任何结构或功能关联。推荐等级2/5（65.6/100），不建议作为TE调控靶标。

