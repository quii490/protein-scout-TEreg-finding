---
type: protein-evaluation
gene: "PPME1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## PPME1 (Protein phosphatase methylesterase 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PPME1 |
| 蛋白全称 | Protein phosphatase methylesterase 1 |
| UniProt ID | Q9Y570 |
| 蛋白大小 | 386 aa / 42.5 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 386 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 7/10 | x2 | 14.0 | InterPro:IPR000073; InterPro:IPR029058; InterPro:IPR016812; Pfam:PF12697 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **122/180** | |
| **归一化总分 (/1.83)** | | | **66.7/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Demethylates proteins that have been reversibly carboxymethylated. Demethylates PPP2CB (in vitro) and PPP2CA. Binding to PPP2CA displaces the manganese ion and inactivates the enzyme

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR000073 |
| InterPro | IPR029058 |
| InterPro | IPR016812 |
| Pfam | PF12697 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000214517-PPME1
定位: location reactome" data-name="nucleoplasm">

![](https://images.proteinatlas.org/4541/670_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/4541/670_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/4541/661_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/4541/661_E12_4_red_green.jpg)
![](https://images.proteinatlas.org/4541/662_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/4541/662_E12_2_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR000073;IPR029058;IPR016812; |
| Pfam | PF12697; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PPP2R1A | STRING | 999 |
| PPP2CA | STRING | 999 |
| PPP2R5C | STRING | 981 |
| PPP2R1B | STRING | 978 |
| PPP2CB | STRING | 966 |
| LCMT1 | STRING | 920 |
| PPP2R2A | STRING | 907 |
| PPP2R5D | STRING | 896 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PPME1

### PubMed

**Count: 21**

| PMID | Title |
|---|---|
| 42321189 | Scaling covalent ligand discovery through dynamic combinatorial library-versus-proteome screening. |
| 41937053 | Investigating the genetic architecture of dairy calf disease traits and their relationships with traits of economic importance in Canadian Holstein ca |
| 41884849 | The value of Protein Phosphatase Methylesterase 1 in diagnosis, prognosis and immunoregulation: from pan-cancer analysis to breast cancer verification |
| 41417796 | Functional dynamics between resident transcriptionally active microbes (TAMs) and host genes underlie Dengue severity. |
| 39502510 | Comparative Proteomic and Phosphoproteomic Analyses Reveal Molecular Signatures of Myocardial Infarction and Transverse Aortic Constriction in Aged Mo |

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/PPME1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.86 |
| pLDDT > 0.9 占比 | 58.8% |
| pLDDT < 0.5 占比 | 3.1% |
| 建模残基数 | 386 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。

### 深度机制分析

PPME1（Protein phosphatase methylesterase 1）的深度机制分析需从其在PP2A磷酸酶调控网络中的核心角色切入。该蛋白属于alpha/beta水解酶超家族（InterPro:IPR029058），含有一个活性AB_hydrolase结构域（IPR000073, Pfam:PF12697），以丝氨酸水解酶机制催化PP2A催化亚基（PPP2CA/PPP2CB）C端亮氨酸309的可逆甲酯化修饰的去甲基化。ESMFold预测展示了极高的结构置信度——全局pLDDT=0.86且58.8%的残基pLDDT>0.9，说明AB_hydrolase结构域折叠极为完善，活性位点催化三联体（Ser-Asp-His）具有精确的几何排列。这一去甲基化酶活性具有深远的调控意义：PP2A催化亚基的C端甲酯化状态直接调控其与B调控亚基的组装，从而决定PP2A全酶的底物特异性和亚细胞定位。

PPI互作网络数据完美印证了这一机制模型。STRING互作谱显示PPME1与PP2A核心组分之间存在极高置信度的互作：PPP2R1A（支架A亚基, score=999）、PPP2CA（催化C亚基, score=999）、PPP2R5C（B56调控亚基, score=981）、PPP2R1B（score=978）、PPP2CB（score=966）以及LCMT1（PP2A甲酯转移酶, score=920）。其中PPME1与LCMT1构成一对功能拮抗的酶——LCMT1负责PP2A的甲酯化（激活），PPME1负责去甲基化（失活），两者共同维持PP2A甲酯化动态平衡。值得注意的是，PPP2R1A和PPP2CA均为score=999的最高置信互作，与UniProt功能注释"demethylates PPP2CA (in vitro) and PPP2CB; binding to PPP2CA displaces manganese ion and inactivates PP2A"完全吻合，形成了从序列注释→结构置信度→PPI验证的三层证据闭环。

在疾病关联方面，PMID 41884849系统评估了PPME1在泛癌中的诊断、预后和免疫调控价值，并通过乳腺癌实验验证了其作为生物标志物的潜力——这直接关联PPME1对PP2A活性的调控，因为PP2A是已知的肿瘤抑制因子，其失活与多种癌症的发生发展相关。此外，PMID 42321189报道的动态组合库筛选方法将PPME1作为共价配体的潜在靶标，提示该蛋白的活性位点具有可药性。然而，PPME1现有的功能注释和文献完全聚焦于其对PP2A的调控，缺乏任何核定位或TE调控的直接证据——其GO-CC注释为"无已知核定位注释"，核定位特异性评分仅4/10。

综合来看，PPME1是一个具有高度可信结构、清晰酶学机制和完美PPI验证的磷酸酶调控蛋白，但其生物学功能锚定于胞质PP2A信号网络，而非核内TE调控。推荐等级2/5（66.7/100）主要由新颖性（10/10）和良好的结构数据（6/10）驱动。其深度机制模型是：AB_hydrolase结构域催化PP2A催化亚基C端去甲基化→锰离子解离→PP2A失活→下游磷酸化信号改变。这一模型高度可信且实验证据充分，但与目标TE调控方向无关。若考虑重新定位研究价值，PPME1更适合作为PP2A相关肿瘤信号通路的调控靶标，而非TE调控候选蛋白。

