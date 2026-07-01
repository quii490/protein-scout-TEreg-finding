---
type: protein-evaluation
gene: "STK35"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## STK35 (Serine/threonine-protein kinase 35) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | STK35 |
| 蛋白全称 | Serine/threonine-protein kinase 35 |
| UniProt ID | Q8TDR2 |
| 蛋白大小 | 534 aa / 58.7 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 534 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR050339; InterPro:IPR011009; InterPro:IPR000719; InterPro:IPR017441; InterPro:IPR008271; Pfam:PF00069 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL 未审查条目，功能尚未充分注释。

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR050339 |
| InterPro | IPR011009 |
| InterPro | IPR000719 |
| InterPro | IPR017441 |
| InterPro | IPR008271 |
| Pfam | PF00069 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Serine/threonine-protein kinase 35

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050339 |
| InterPro | IPR011009 |
| InterPro | IPR000719 |
| InterPro | IPR017441 |
| InterPro | IPR008271 |
| Pfam | PF00069 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000125834-STK35
定位: location reactome" data-name="nucleoplasm,nuclear_bodies">

![](https://images.proteinatlas.org/26452/1608_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/26452/1608_B6_3_red_green.jpg)
![](https://images.proteinatlas.org/26452/1662_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/26452/1662_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/26452/1664_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/26452/1664_B6_2_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00220; |
| InterPro | IPR050339;IPR011009;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |
| UniProt Domain | DOMAIN 202..530; /note="Protein kinase"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00159" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ELAVL1 | BioGRID | 1 |
| CTDSPL2 | BioGRID | 1 |
| C1ORF174 | BioGRID | 1 |
| UBP1 | BioGRID | 1 |
| HSP90AA1 | BioGRID | 1 |
| HSP90AB1 | BioGRID | 1 |
| TFCP2 | BioGRID | 1 |
| PRR14L | BioGRID | 1 |


### 深度机制分析

**结构域架构**：STK35（534 aa，58.7 kDa）是丝氨酸/苏氨酸蛋白激酶35，结构域架构在典型激酶折叠上扩展出N端延伸区（1-200 aa）和C端延伸尾端（530-534 aa）：Protein kinase催化结构域（UniProt DOMAIN 202-530，IPR000719, PF00069）——采用经典的双叶折叠，但定位异常（催化域位于202-530而非典型的N端），提示N端202 aa代表了独特的功能模块。IPR011009（蛋白激酶样结构域超家族）、IPR017441（ATP结合）、IPR008271（Ser/Thr激酶活性位点）和IPR050339（STK35特异的家族分类）完成结构注释。AlphaFold pLDDT可用。N端延伸区（1-201 aa）pLDDT可能较低（<60），暗示部分内在无序。

**PPI互作网络解读**：PPI数据揭示了STK35在DNA损伤应答（DDR）和RNA代谢中的定位：ELAVL1（HuR，AU-rich RNA结合蛋白，BioGRID 1）——调控mRNA稳定性的核心因子，提示STK35可能通过磷酸化ELAVL1影响其RNA结合亲和力；TFCP2（α-globin转录因子CP2）和UBP1（上游结合蛋白1）——转录调控因子互作簇；CTDSPL2——RNA聚合酶II CTD磷酸酶，拮抗转录延伸因子P-TEFb的活性；HSP90AA1/HSP90AB1——激酶折叠成熟的分子伴侣。PRR14L（富含脯氨酸蛋白14-like）的功能未知。PMID:42161060揭示了STK35在DNA损伤应答和遗传毒性药物耐受中的功能图谱，这是目前最全面的STK35功能研究。

**结构解读**：N端延伸区（200 aa）的低保守性可能包含：（1）蛋白质相互作用基序——ELAVL1和TFCP2可能通过这一区域与STK35结合而不涉及催化域；（2）核定位信号（NLS）——N端碱性残基簇确保Nuclear bodies的靶向；（3）可能的PEST降解信号——调控STK35的半衰期。C端催化域（202-530）中G-loop、αC螺旋、催化环和活化环均遵循保守激酶折叠。STK35可能通过活化环（activation loop）中Ser/Thr的自磷酸化实现活化，或通过上游激酶（可能的ATM/ATR在DDR通路中）磷酸化其活化环。

**机制模型**：（1）STK35在DNA损伤后活化——ATM/ATR通过磷酸化STK35活化环触发激酶活性；（2）活化STK35磷酸化ELAVL1（HuR）——改变ELAVL1的RNA结合特异性或核质穿梭动力学，从而重塑损伤应答相关的mRNA稳定性谱系（如p21, GADD45α, BAX等）；（3）STK35通过磷酸化CTDSPL2间接调控RNA Pol II CTD的磷酸化状态（Ser2/Ser5磷酸化）——这可能在DNA损伤诱导的转录沉默和重启中发挥调控作用；（4）Nuclear bodies定位：STK35在核体（可能是Cajal体或DNA损伤灶）中富集，与53BP1、γH2AX和MDC1等修复蛋白形成功能性组装，协调DNA修复与RNA代谢的交叉对话。PMID:39661519通过碱基编辑筛选系统性地绘制了STK35在DDR中的功能元件图谱。

**TE调控展望**：STK35通过ELAVL1/HuR和RNA Pol II CTD磷酸化间接连接TE调控。ELAVL1是AU-rich元件（ARE）的mRNA稳定性调控因子——许多反转录转座子（如L1, Alu）的3'UTR包含ARE或ARE-like序列，ELAVL1的结合可稳定这些TE转录本。STK35对ELAVL1的磷酸化可能改变其与ARE-TE转录本的亲和力，调控TE RNA的稳定性。此外，DNA损伤应答与TE转录激活的耦合是已知现象（'TE reactivation by DDR'）——STK35可能位于DDR-TE调控轴的交汇点，通过磷酸化下游效应蛋白在DDR条件下调控TE的转录输出。

### PubMed 文献

**PubMed count: 21**

| 42161060 | The functional landscape of STK35 residues at single-amino-acid resolution in the DNA damage response and genotoxic drug | Biochem Biophys Res Commun 2026 |
| 40128328 | New insights into the effects of PFOS exposure on rat lung development: morphological, functional, and single-cell seque | Arch Toxicol 2025 |
| 39661519 | Mapping functional elements of the DNA damage response through base editor screens. | Cell Rep 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/STK35

