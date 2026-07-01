---
type: protein-evaluation
gene: "Tada2b"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## Tada2b (Transcriptional adapter 2-beta) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | Tada2b |
| 蛋白全称 | Transcriptional adapter 2-beta |
| UniProt ID | Q86TJ2 |
| 蛋白大小 | 420 aa / 46.2 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 420 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR041983; InterPro:IPR016827; InterPro:IPR056267; InterPro:IPR009057; InterPro:IPR001005; InterPro:IPR017884 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Coactivates PAX5-dependent transcription together with either SMARCA4 or GCN5L2

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR041983 |
| InterPro | IPR016827 |
| InterPro | IPR056267 |
| InterPro | IPR009057 |
| InterPro | IPR001005 |
| InterPro | IPR017884 |
| InterPro | IPR055141 |
| InterPro | IPR036388 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TADA3 | STRING | 999 |
| SUPT3H | STRING | 999 |
| SGF29 | STRING | 999 |
| TAF9 | STRING | 999 |
| TRRAP | STRING | 998 |
| TAF12 | STRING | 997 |
| TAF10 | STRING | 997 |
| KAT2A | STRING | 996 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000173011-TADA2B

![](https://images.proteinatlas.org/35770/393_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/35770/393_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/35770/396_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/35770/396_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/35770/392_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/35770/392_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/35770/2266_E4_134_red_green.jpg)
![](https://images.proteinatlas.org/35770/2266_E4_160_red_green.jpg)

### PubMed 文献

**PubMed count: 12**

| 41577693 | In vivo CRISPR screening identifies SAGA complex members as key regulators of hematopoiesis. | Nat Commun 2026 |
| 41161382 | Mapping the intracellular HMGB1 interactome and alterations induced by Toll-like receptor 4 activation. | J Biol Chem 2025 |
| 40991071 | Selection of tumor invasion-related genes to build a prognostic model and predict immune response and potential drugs fo | Discov Oncol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/Tada2b

### 深度机制分析

**结构域架构**：TADA2B/ADA2B（UniProt Q86TJ2，420 aa，46.2 kDa）是SAGA（Spt-Ada-Gcn5 Acetyltransferase）组蛋白乙酰转移酶（HAT）复合体的核心亚基。其域架构经过高度优化以整合多个共激活功能：N端含SWIRM域（IPR017884 - SWIRM domain），该域采用螺旋-螺旋折叠（helix-turn-helix变体），与人TADA2A/ADA2A同源，参与核小体DNA的识别和结合（嗜碱性正电荷表面结合DNA磷酸骨架）；中央含锌指myb型域（IPR001005 - SANT/Myb domain；IPR009057 - Homeobox-like domain superfamily），为染色质结合结构模块；C端含TADA2亲和域（IPR041983 - Transcriptional adapter 2, conserved domain）和ADA2型ZnF（IPR056267及IPR055141），介导与GCN5 (KAT2A) HAT和SAGA核心模块的直接物理互作。IPR016827定义含ADA2型的SAGA亚基家族。

**PPI互作网络**：STRING分值为极高置信度的SAGA复合体核心网络：TADA3（评分999）和SUPT3H（评分999）为SAGA核心结构亚基，SGF29（评分999）为含Tudor域染色质阅读器，TAF9（评分999）、TAF12（评分997）和TAF10（评分997）为TBP关联因子/结构亚基。TRRAP（评分998）为巨型ATM/PI3K相关适配蛋白（约440 kDa），识别组蛋白乙酰转移酶至染色质。KAT2A（GCN5，评分996）为SAGA-HAT催化亚基，TADA2B直接与KAT2A的N端域结合，增强其HAT内在酶活性和底物乙酰化范围（从游离组蛋白到核小体组蛋白H3）。该PPI集群的评分接近理论极值（999），反映了SAGA在进化中高度保守的8亚基核心组装。

**结构-功能关系**：TADA2B通过SWIRM域和myb域将SAGA-GCN5定位至染色质的特定基因组位点，而通过C端TADA2保守域将GCN5/KAT2A的精确定向至核小体组蛋白H3 N端尾——此空间精准导向使H3K9、H3K14和H3K18等多乙酰化位点同步被催化。PAX5转录因子被TADA2B共激活——PAX5直接结合DNA并通过TADA2B-SAGA通路募集组蛋白乙酰化活性以打开B细胞谱系基因座（PMID:41577693 - 体内CRISPR筛选鉴定SAGA复合体成员为造血关键调控因子）。此外，TADA2B参与HMGB1互作网络（PMID:41161382 - HMGB1胞内互作组的TLR4激活改变），为高迁移率族蛋白的染色质重塑提供HAT活性。

**TE调控机制**：SAGA复合体是TE调控的已知核心参与者——GCN5/KAT2A催化H3K9ac和H3K14ac等活化修饰，而这一修饰模式与ERV-LTR启动子激活直接相关。TADA2B通过增强GCN5的核小体底物范围，可能将HAT活性导向特定的TE启动子亚群。SGF29-Tudor域识别H3K4me3标记——该标记在二价TE启动子上与H3K27me3共存时维持平衡/沉默（bivalency），而SAGA的募集可打破这一平衡，使TE启动子从二价状态转变为活化状态。PAX5→TADA2B→SAGA→TE启动子乙酰化代表了B细胞发育和淋巴瘤中TE去抑制的一条信号直接通路。TADA3（评分999）的SAGA核心结构功能是指向TE调控的重要共同因子——TADA3与p53直接互作且参与p53靶基因（含p53应答TE元件）的H3/H4乙酰化。

**前沿意义**：TADA2B位于染色质修饰SAGA复合体的核心，提供了组蛋白乙酰化→TE调控的最直接机械连接。SAGA-HAT模块的小分子抑制剂（如GCN5抑制剂丁内酯MB-3类似物）已可用，这使得靶向SAGA的TE调控具有药理学可行性。TADA2B-PAX5-GCN5的造血特异性功能（PMID:41577693）在TE去抑制驱动的白血病发生背景下尤其有意义——大多数急性白血病中ERV被广泛去抑制。12篇文献量凸显了TADA2B在SAGA亚基中的低代表性（TADA2A和TADA3文献量高10倍以上）。


