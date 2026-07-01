---
type: protein-evaluation
gene: "A0A140VJI9"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A140VJI9 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VJI9 |
| 蛋白大小 | 333 aa / 38.2 kDa |
| UniProt ID | A0A140VJI9 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 333 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=70.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Nse4/EID; Nse4_C; Nse4_Nse3-bd |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **117/180** | |
| **归一化总分** | | | **65.0/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=70.9 PDB=0
- InterPro: Nse4/EID; Nse4_C; Nse4_Nse3-bd
- Pfam: Nse4-Nse3_bdg; Nse4_C
- PPI degree=0 ChIP: None


### 4. 总体评价
**65.0/100** | **nucleoplasm**
Nuclear protein


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CREBBP | STRING | 532 |
| NSMCE2 | STRING | 779 |
| RAD21 | STRING | 600 |
| EID2B | STRING | 401 |
| SUMO4 | STRING | 914 |
| SMC1A | STRING | 535 |
| NSMCE3 | STRING | 424 |
| SMC3 | STRING | 737 |
| SMC5 | STRING | 444 |
| NSMCE1 | STRING | 998 |
| NSMCE4A | STRING | 439 |
| EID2 | STRING | 437 |
| SMC6 | STRING | 999 |
| EID1 | STRING | 855 |
| TXNRD1 | STRING | 689 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000255150

![](https://images.proteinatlas.org/59367/1112_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/59367/1112_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/59367/1527_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/59367/1527_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/59367/1116_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/59367/1116_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/59367/2268_G4_14_red_green.jpg)
![](https://images.proteinatlas.org/59367/2268_G4_111_red_green.jpg)

### 深度机制分析

A0A140VJI9的InterPro/Pfam注释揭示其属于Nse4/EID家族（IPR029403），携带两个特征结构域：Nse4-Nse3结合域（Nse4-Nse3_bdg, PF12409）和Nse4_C（Nse4 C-terminal domain, PF15125）。Nse4是从酵母到人类保守的SMC5/6复合体的核心非SMC亚基，被称为NSMCE4A（Non-SMC Element 4 Homolog A）或EID3（EP300-Interacting Inhibitor of Differentiation 3）。Nse4-Nse3_bdg通过α-螺旋-α-螺旋构象介导与Nse3（NSMCE3）亚基的高亲和力异二聚化（Kd ~ 2-10 nM in yeast, PMID: 19683513）。Nse4_C延伸形成臂状结构，通过其酸性C末端尾与SMC5的铰链域相互作用，作为SMC5/6异二聚体的ATP酶激活器。333个氨基酸（38.2 kDa）是Nse4/EID家族中紧凑但完整的成员，不含有明显的大型插入序列。

STRING PPI网络清晰地重构了完整的SMC5/6复合体：SMC5（444分）和SMC6（999分）为ATP驱动的ring-shaped骨架亚基；NSMCE1（998分）和NSMCE2/Mms21（779分）为kleisin和SUMO连接酶亚基；NSMCE3（424分）和NSMCE4A（439分）为桥接亚基。SMC5/6复合体已知的生化功能是DNA损伤修复中的姐妹染色单体间同源重组和复制叉保护（PMID: 18851830）。值得注意的是SUMO4（914分）和SMC1A（535分）也出现在网络中——SUMO4暗示SMC5/6复合体的SUMO化调控（NSMCE2作为E3 SUMO连接酶），而SMC1A可能指示SMC5/6与cohesin（SMC1/SMC3）之间的交叉对话。

CREBBP/CBP（532分）和EID家族成员（EID1 855分、EID2 437分、EID2B 401分）的存在拓宽了A0A140VJI9的功能视野。EID1最初被鉴定为CBP/p300组蛋白乙酰转移酶的抑制因子，通过阻断CBP与核受体的结合来抑制配体依赖性转录激活（PMID: 10675336, 11073989）。CBP/p300是多种TE转录共激活因子（如NF-κB、AP-1、STATs）必需的通用转录共激活因子，而EID家族的抑制剂活性意味着A0A140VJI9在特定条件下可能抑制TE的来源转录。

SMC5/6复合体与转座子抑制的关联在2019-2022年间得到突破性建立。SMC5/6被证明是乙肝病毒（HBV）cccDNA转录的宿主限制因子，通过与HBV cccDNA的微小染色体结合来抑制其转录（PMID: 27723722, 32084395）。进一步研究表明SMC5/6也可限制外源性转座子（如sleeping beauty、piggyBac）和内源性逆转录元件（PMID: 34352020）。机制上，SMC5/6通过其环状结构"包裹"外源DNA，并利用NSMCE2的SUMO连接酶活性使染色质蛋白SUMO化，从而建立沉默染色质状态。同时，SMC5/6也参与PML核体（SUMO化修饰的组分）的形成。

A0A140VJI9的特异性TE调控模型：该蛋白质作为NSMCE4A类的Nse4/EID因子，通过EID抑制活性将SMC5/6复合体的TE DNA识别功能与CBP/p300依赖的TE转录调控耦合。具体步骤见下（推测）：（1）SMC6/SMC5环识别并topologically包裹TE来源的超螺旋DNA或R-loop结构（尤其是LTR区域）；（2）NSMCE2的SUMO E3连接酶活性将SMC5/6在TE处的DNA结合蛋白SUMO化，招募PML核体组分；（3）A0A140VJI9通过其Nse4-CREBBP互作，竞争性抑制CBP/p300在TE位点的HAT（组蛋白乙酰转移酶）活性，降低H3K27ac，从而阻碍TE的启动子活性；（4）EID1/EID2同源物可能作为交换因子或稳定因子调节这一抑制过程的持续性。pLDDT=70.9意味着大部分核心结构折叠良好，这与Nse4-Nse3复合体已知的高亲和力折叠一致。PDB=0仍反映该特定人类同源物的新颖性。

优先实验验证：（1）在A0A140VJI9 KD细胞中进行ATAC-seq+H3K27ac ChIP-seq确认TE染色质状态变化；（2）在TE报告基因系（如L1-EGFP或IAP-luciferase）中过表达A0A140VJI9进行功能gain-of-function验证；（3）Co-IP检测A0A140VJI9-CREBBP和A0A140VJI9-SMC5互作。PubMed=0+生物学功能路径清晰+功能域明确，使A0A140VJI9成为探索SMC5/6-TE调控轴的高优先级候选蛋白。

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A140VJI9
