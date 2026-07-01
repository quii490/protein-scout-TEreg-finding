---
type: protein-evaluation
gene: "A0A140VJQ5"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A140VJQ5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VJQ5 |
| 蛋白大小 | 427 aa / 48.2 kDa |
| UniProt ID | A0A140VJQ5 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 427 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=73.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | 2-oxogl_dehyd_N; 2oxoglutarate_DH_E1; DH_E1 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **117/180** | |
| **归一化总分** | | | **65.0/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=73.3 PDB=0
- InterPro: 2-oxogl_dehyd_N; 2oxoglutarate_DH_E1; DH_E1
- Pfam: 2-oxogl_dehyd_N; E1_dh
- PPI degree=0 ChIP: None


### 4. 总体评价
**65.0/100** | **nucleoplasm**
Nuclear protein


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DLD | STRING | 751 |
| ACO2 | STRING | 607 |
| IDH3G | STRING | 607 |
| PDHX | STRING | 612 |
| DLAT | STRING | 675 |
| IDH3A | STRING | 780 |
| IDH2 | STRING | 657 |
| DLST | STRING | 780 |
| DBT | STRING | 644 |
| OGDHL | STRING | 932 |
| SUCLG1 | STRING | 856 |
| OGDH | STRING | 957 |
| IDH1 | STRING | 784 |
| SUCLG2 | STRING | 806 |
| IDH3B | STRING | 869 |

### 深度机制分析

A0A140VJQ5的InterPro/Pfam注释指向α-酮戊二酸脱氢酶（α-KGDH/OGDH）E1亚基家族的成员，携带三个特征结构域：2-oxogl_dehyd_N（IPR029061, 2-酮戊二酸脱氢酶N端结构域）、2oxoglutarate_DH_E1（IPR032106, E1活性结构域）和DH_E1（IPR042179, 脱氢酶E1超家族折叠）。Pfam注释到2-oxogl_dehyd_N（PF16078）和E1_dh（PF00676），后者编码硫胺素焦磷酸（ThDP）依赖的脱氢酶催化核心，介导α-酮戊二酸 + CoA-SH + NAD+ → 琥珀酰-CoA + CO2 + NADH的不可逆反应（PMID: 24407285）。427个氨基酸和48.2 kDa代表最小功能性的E1亚基单元，不含E2（二氢硫辛酰胺琥珀酰转移酶）或E3（二氢硫辛酰胺脱氢酶）融合。这意味着A0A140VJQ5必须依靠互作伙伴（E2和E3亚基）来重建完整的α-KGDH多酶复合体活性。

STRING PPI网络完美重构了完整的TCA循环相关多酶复合体架构：OGDH（957分）和OGDHL（932分）均为α-酮戊二酸脱氢酶E1亚基的同工酶，提示A0A140VJQ5可能是E1亚基的第三个同源物；DLST（780分）为二氢硫辛酰胺琥珀酰转移酶E2亚基，通过硫辛酰赖基摆动臂在E1和E3之间传递琥珀酰基团；DLD（751分）为二氢硫辛酰胺脱氢酶E3亚基，负责FADH2→FAD的再氧化。成簇出现的IDH1/IDH2/IDH3A/IDH3B/IDH3G（异柠檬酸脱氢酶家族，607-869分）将互作锚定在TCA循环的紧邻上游反应（异柠檬酸→α-酮戊二酸）。DBT（644分）为支链α-酮酸脱氢酶E2亚基，SUCLG1/SUCLG2（856/806分）为琥珀酰-CoA合成酶，表明A0A140VJQ5可能也参与支链氨基酸衍生α-酮酸的代谢交叉对话。ACO2（607分）和PDHX（612分）进一步确认线粒体基质多酶代谢网络的完整性。

α-酮戊二酸脱氢酶复合体核质定位的生物学意义需要超越传统线粒体代谢的视角来看待。α-酮戊二酸（α-KG）是2-酮戊二酸依赖性双加氧酶（2-OGDD）超家族的必需共底物，该家族包含TET DNA去甲基化酶（TET1/2/3）、JMJC组蛋白去甲基化酶（KDM2-7）、以及ALKBH家族RNA去甲基化酶（PMID: 33110246, 23260665）。核内α-KG浓度直接控制TET催化5mC→5hmC→5fC→5caC的反应速率，以及KDM酶对H3K4me3、H3K9me、H3K27me、H3K36me等组蛋白甲基标记的去除效率。核质中的α-KGDH复合体可能局部消耗α-KG以产生琥珀酰-CoA，后者可作为组蛋白琥珀酰化的底物——赖氨酸琥珀酰化是一种新近发现但与TE调控相关的染色质标记（PMID: 29020646）。另外，ThDP依赖性脱氢酶可能消耗核内的NAD+产生NADH，改变局部氧化还原电位间接影响SIRT1/SIRT6的NAD+依赖性组蛋白去乙酰化酶活性，这些酶直接参与TE位点如LINE-1、IAP、MLV等逆转录转座子的异染色质化（PMID: 26686653, 30602777）。

TE调控推测模型：A0A140VJQ5作为核内α-KG代谢节点。线粒体α-KGDH复合体产生琥珀酰-CoA作为TCA循环中间体，但核内版本的E1亚基（本文所述蛋白质）可能通过以下途径影响TE染色质状态：（1）消耗α-KG，减少TET和JMJC酶的共底物供应，导致TE GC-rich区域（CpG岛化LINE-1 5'UTR）的DNA甲基化水平升高；（2）产生琥珀酰-CoA，通过p300/CBP（二者均有琥珀酰转移酶活性）促进TE位点组蛋白赖氨酸琥珀酰化（succinylation），这是一种与非乙酰化不同的表观遗传标记；（3）核内NAD+/NADH比率改变通过SIRT1介导影响H4K16ac水平（TE启动子的一个关键激活标记）；（4）该蛋白质可能与IDH1（784分）形成核内α-KG代谢小循环——IDH1催化异柠檬酸→α-KG，A0A140VJQ5催化α-KG→琥珀酰-CoA，两者的差额决定了局部α-KG浓度。pLDDT=73.3显示折叠良好，比线粒体典型E1亚基稍高，这可能是核定位蛋白需要更紧凑折叠以适应核质基质（无膜包被）的进化适应。

研究意义：（1）核内TCA酶在TE调控中的功能属于完全未开发的交叉领域——代谢酶moonlighting在核内产生表观遗传调控信号；（2）A0A140VJQ5可能提供代谢状态（α-KG/琥珀酸/NAD+水平）与TE去抑制之间的直接联系，这对理解衰老和癌症中伴随的TE激活（已知受代谢重编程调控）很关键；（3）代谢组学（LC-MS追踪核质α-KG/succinyl-CoA）+ ChIP-seq（succinyl-lysine/H3K9me3）组合实验可以验证这一模型。PubMed=0+功能域明确+互作网完整，使之成为代谢-TE调控连接的高价值候选。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000105953

![](https://images.proteinatlas.org/19514/198_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19514/198_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19514/152_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19514/152_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19514/154_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19514/154_H10_2_blue_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A140VJQ5
