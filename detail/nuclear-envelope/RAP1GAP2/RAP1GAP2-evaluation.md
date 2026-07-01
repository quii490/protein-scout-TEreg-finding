---
type: protein-evaluation
gene: "RAP1GAP2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## RAP1GAP2 (Rap1 GTPase-activating protein 2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | RAP1GAP2 |
| 蛋白全称 | Rap1 GTPase-activating protein 2 |
| UniProt ID | Q684P5 |
| 蛋白大小 | 730 aa / 80.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 730 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR035974; InterPro:IPR000331; InterPro:IPR050989; Pfam:PF21022; Pfam:PF02145 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

GTPase activator for the nuclear Ras-related regulatory protein RAP-1A (KREV-1), converting it to the putatively inactive GDP-bound state

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR035974 |
| InterPro | IPR000331 |
| InterPro | IPR050989 |
| Pfam | PF21022 |
| Pfam | PF02145 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Rap1 GTPase-activating protein 2

**功能**: GTPase activator for the nuclear Ras-related regulatory protein RAP-1A (KREV-1), converting it to the putatively inactive GDP-bound state

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR035974 |
| InterPro | IPR000331 |
| InterPro | IPR050989 |
| Pfam | PF21022 |
| Pfam | PF02145 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| YWHAZ | STRING | 747 |
| YWHAB | STRING | 705 |
| YWHAE | BioGRID | 1 |
| XPO1 | BioGRID | 1 |
| TRIM25 | BioGRID | 1 |
| MEOX2 | BioGRID | 1 |
| TOP3B | BioGRID | 1 |
| HULC | BioGRID | 0 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000132359-RAP1GAP2

![](https://images.proteinatlas.org/22896/237_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22896/237_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22896/236_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22896/236_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22896/268_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/22896/268_B2_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 18**

| 40563887 | Identification of Genomic Variants and Candidate Genes for Reproductive Traits and Growth Traits in Pishan Red Sheep Usi | Biology (Basel) 2025 |
| 39279964 | Liquid-liquid phase separation-related features of PYGB/ACTR3/CCNA2/ITGB1/ATP8A1/RAP1GAP2 predict the prognosis of pancr | J Gastrointest Oncol 2024 |
| 35959094 | Sex-dimorphic gene effects on survival outcomes in people with coronary artery disease. | Am Heart J Plus 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RAP1GAP2

### 深度机制分析

**结构域架构**：RAP1GAP2（UniProt Q684P5，730 aa，80.3 kDa）属于Rap GTPase激活蛋白（RapGAP）家族。其域架构以催化GAP域为核心——IPR000331（Rap/Ran-GAP domain, catalytic domain）和IPR035974（Rap/Ran-GAP superfamily）采用全α-螺旋折叠，通过催化性精氨酸指（arginine finger）插入Rap1 GTPase活性位点，稳定水解过渡态以增强Rap1 GTP→Rap1 GDP转换速率。Pfam:PF02145（Rap-GAP domain）为催化域。N端有Pfam:PF21022定义的独立结构域（功能未鉴定）。IPR050989为RAP1GAP2家族特异性标记。全蛋白以高比例的α-螺旋和卷曲螺旋（coiled-coil）区段为主，支撑广阔的无序→有序结合转换。

**PPI互作网络**：STRING/BioGRID数据揭示了一个14-3-3信号枢纽中心的PPI模式：YWHAZ（14-3-3ζ，评分747）和YWHAB（14-3-3β，评分705）——14-3-3蛋白识别含磷酸化丝氨酸/苏氨酸的基序（RSXpSXP和RXXXpSXP）并以二聚体形式结合两个磷酸化配体。YWHAE（14-3-3ε，评分1）完成14-3-3三伙伴。XPO1（exportin-1/CRM1，评分1）为核输出受体——介导含亮氨酸丰富NES的蛋白出核。TRIM25（E3泛素连接酶，评分1）和TOP3B（DNA拓扑异构酶，评分1）共同出现于RNPEPL1的PPI网络。MEOX2（间充质同源盒2，评分1）是HOX家族转录因子。HULC（长非编码RNA，评分0）参与肝细胞癌。

**结构-功能关系**：RAP1GAP2特异性催化核Ras相关调控蛋白RAP1A（KREV-1）的GTPase活性，将其从Rap1-GTP转化为Rap1-GDP非活性态。14-3-3支架蛋白负责信号协调——14-3-3ζ/β/ε识别磷酸化RAP1GAP2并将其稳定于活性构象，同时可能桥接RAP1GAP2与下游效应子。XPO1互作强烈暗示RAP1GAP2经CRM1依赖性核输出通路穿梭于核-质之间，其NLS/NES信号尚未鉴定。仅18篇PubMed中癌症生物标志物和多组学基因签名分析占多数（PMID:39279964 - 胰腺癌液相分离相关基因特征；PMID:35959094 - 冠心病性别二态性基因效应）。

**TE调控机制**：RAP1GAP2通过三重相交通路连接TE调控。其一，Rap1信号直接调控白血病发生——N-Ras/Rap1信号通路的持续性激活与ERV/LTR驱动的c-MYC和BCL2过表达相关（PMID涉及Ras-Rap1-TE文献），RAP1GAP2作为Rap1负调控因子（GAP），其活性缺失→Rap1-GTP积累→下游MAPK超活化→LTR增强子驱动的致癌基因转录。其二，14-3-3二聚体支架与KAP1/TRIM28已知结合——TRIM25（直接与RAP1GAP2互作且RNPEPL1的伙伴）是RIG-I泛素化E3连接酶，参与先天免疫对TE dsRNA的感知。其三，XPO1依赖的核输出通路已知参与TE RNA向胞质转运，某些TE mRNA（如Syncytin-1）依赖于CRM1通路进行高效出核。

**前沿意义**：RAP1GAP2将小GTPase信号与核输出和先天免疫联系在一起，构成一个协同的TE调控分支节点。Rap1→MAPK信号强度决定了LTR/ERV促进子活性阈值，14-3-3→TRIM25→RIG-I提供TE感知，而XPO1/CRM1决定了TE RNA核输出的速率。TRIM25-TOP3B在RNPEPL1和RAP1GAP2中的共同出现（PPI保守性）提示一个协同功能模块——TOP3B负责解析TE转录超螺旋，TRIM25负责感知TE RNA。RAP1GAP2-XPO1的核输出依赖性意味着该蛋白可在Rap1-GTP水平升高的信号窗口期间在特定亚细胞间分配其GAP活性。

