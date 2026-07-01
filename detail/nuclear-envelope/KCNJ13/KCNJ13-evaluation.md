---
type: protein-evaluation
gene: "KCNJ13"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## KCNJ13 (Inward rectifier potassium channel 13) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | KCNJ13 |
| 蛋白全称 | Inward rectifier potassium channel 13 |
| UniProt ID | O60928 |
| 蛋白大小 | 360 aa / 39.6 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 360 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR014756; InterPro:IPR041647; InterPro:IPR016449; InterPro:IPR013518; InterPro:IPR008062; InterPro:IPR040445 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Inward rectifier potassium channels are characterized by a greater tendency to allow potassium to flow into the cell rather than out of it. Their voltage dependence is regulated by the concentration of extracellular potassium; as external potassium is raised, the voltage range of the channel opening shifts to more positive voltages. The inward rectification is mainly due to the blockage of outward

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR014756 |
| InterPro | IPR041647 |
| InterPro | IPR016449 |
| InterPro | IPR013518 |
| InterPro | IPR008062 |
| InterPro | IPR040445 |
| Pfam | PF01007 |
| Pfam | PF17655 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IK | STRING | 932 |
| KCNK5 | STRING | 929 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000115474-KCNJ13

![](https://images.proteinatlas.org/51609/2186_G3_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/51609/2186_G3_53_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 79**

| 42265079 | Engineered tRNA reduces vision loss in a mouse model of Leber congenital amaurosis. | Signal Transduct Target Ther 2026 |
| 42262737 | Ion Channels as Gatekeepers of Fertility: From Uterine Kir7.1 to Sperm CatSper. | Physiology (Bethesda) 2026 |
| 42199967 | Association of Autosomal Dominant Snowflake Vitreoretinal Degeneration with Retinoschisis. | Ophthalmol Sci 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KCNJ13

### 深度机制分析

**结构域架构**：KCNJ13/Kir7.1（UniProt O60928，360 aa，39.6 kDa）是内向整流钾通道（Kir）家族的成员。与Kv通道不同，Kir通道仅含2次跨膜螺旋（M1和M2）加一个pore loop（P-loop），不含S1-S4电压感受域。非电压依赖的门控是通过对K⁺离子浓度和膜磷脂（特别是PIP₂）的响应实现——内源性多胺（精胺/亚精胺）和Mg²⁺在去极化时从胞质侧阻断孔道，产生内向整流的电生理特征（IPR016449 - Potassium channel, inwardly rectifying, Kir）。IPR013518（Potassium channel, inwardly rectifying, Kir, cytoplasmic）为C端胞质域，形成延长的α-螺旋和β-折叠延伸结构，其中对PIP₂和G蛋白βγ亚基的结合位点控制通道开闭。Pfam:PF01007（IRK）为孔道域，PF17655（IRK_C）为C端调控域。

**PPI互作网络**：STRING数据显示KCNJ13与IK（IER3IP1 - 即早应答蛋白3互作蛋白1，评分932）和KCNK5（双孔钾通道TASK-2，评分929）存在高置信互作。IK（基因名IER3IP1）编码内质网定位蛋白，参与内质网应激和分泌蛋白运输——其与KCNJ13的互作提示Kir7.1可能经IK介导的膜运输通路运往质膜。仅有79篇PubMed文献，主导研究集中在遗传性视网膜疾病（Leber先天性黑矇——PMID:42265079，tRNA基因治疗减轻小鼠LCA模型视力丧失）和通道病（PMID:42262737综述离子通道在生育力中的作用）。

**结构-功能关系**：Kir7.1的导电性极低（仅在皮西门子范围内），因而作为精细的钾电导调控者而非大电流发生器。PIP₂依赖性门控——内源性PIP₂缺失可导致通道关闭——使其活性与磷脂酶C（PLC）信号耦合。多胺/Mg²⁺阻断的正向电压依赖性产生标志性的内向整流I-V曲线。在视网膜色素上皮（RPE）细胞的基底侧质膜中维持K⁺稳态（PMID:42265079）。

**TE调控机制**：KCNJ13的TE调控连接主要围绕即时早期基因IER3IP1/IK（PPI评分932）。IER3IP1/IK在细胞应激（缺氧、氧化应激、DNA损伤）后被迅速诱导，参与内质网应激介导的未折叠蛋白反应（UPR）——UPR已知可通过ATF6/XBP1通路激活ERV/LTR转录。Kir7.1通过PIP₂敏感性感知磷脂代谢信号，而TE去抑制常伴随核被膜和ER膜脂质组成的变化（如神经酰胺积累）。IK的分泌蛋白运输功能可能调控TE编码的膜蛋白（如Syncytin融合蛋白）的胞内运输。鉴于Kir7.1对K⁺的微弱导电性，其生理功能可能更偏向非导电性信号支架角色而非典型的离子通道。

**前沿意义**：KCNJ13的高置信度IER3IP1互作（评分932）是连接离子通道与内质网应激/TE调控的极重要线索。仅79篇文献几乎全部聚焦于视网膜疾病，但IK（3p21.3染色体位点在多种癌症中表达异常）—KCNJ13功能轴在应激条件下可能调控ER→核信号传递——此方向在TE调控中完全未探索。KCNJ13的低导电性特征支持其"兼职"信号支架功能的假说，可通过KCNJ13敲除后ER-UPR-TE报告系统进行验证。

