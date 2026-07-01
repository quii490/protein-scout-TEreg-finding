---
type: protein-evaluation
gene: "GADD45GIP1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GADD45GIP1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GADD45GIP1 |
| 蛋白名称 | Large ribosomal subunit protein mL64 |
| 蛋白大小 | 124 aa / 14.5 kDa |
| UniProt ID | Q7LAX7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | 32.0 | nan (Supported) |
| 📏 蛋白大小 | 6/10 | ×1 | 6.0 | 124 aa |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=12 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=86.5; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | Ribosomal_mL64; Ribosomal_mL64_sf |
| 🔗 PPI | 8/10 | ×3 | 24.0 | PPI degree=317 |
| **加权总分** | | | **136/180** | |
| **归一化总分 (÷1.83)** | | | **74.9/100** | 互证: +1 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | nan (Supported) |
| PubMed | strict=12, broad=41 |
| AlphaFold | pLDDT=86.5 |
| PDB | 0 entries |
| InterPro | Ribosomal_mL64; Ribosomal_mL64_sf |
| Pfam | CR6_interact |
| PPI | combined degree=317 |
| ChIP | None |

### 4. 总体评价
⭐⭐⭐⭐
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Large ribosomal subunit protein mL64

**功能**: Acts as a negative regulator of G1 to S cell cycle phase progression by inhibiting cyclin-dependent kinases. Inhibitory effects are additive with GADD45 proteins but also occur in the absence of GADD45 proteins. Acts as a repressor of the orphan nuclear receptor NR4A1 by inhibiting AB domain-mediated transcriptional activity. May be involved in the hormone-mediated regulation of NR4A1 transcriptional activity. May play a role in mitochondrial protein synthesis

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR018472 |
| InterPro | IPR043035 |
| Pfam | PF10147 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

GADD45GIP1（Growth arrest and DNA damage-inducible 45 gamma-interacting protein 1），又名CRIF1或mL64，是一个具有双重身份的多功能蛋白。其InterPro结构域包括Ribosomal_mL64（IPR018472）和Ribosomal_mL64_sf（IPR043035），Pfam注释为CR6_interact（PF10147），反映了其核糖体蛋白（线粒体核糖体大亚基mL64）和核调控蛋白的双重特性。124个氨基酸（14.5 kDa）的小分子量表明这是一个紧凑的单结构域蛋白，AlphaFold预测的pLDDT=86.5确认了其折叠的可信度。

GADD45GIP1的功能表现为细胞核和线粒体中的双重定位与双重角色。在核内，它是G1/S细胞周期检查点的负调控因子——通过与GADD45蛋白协同作用（或独立于GADD45）抑制细胞周期蛋白依赖性激酶的活性，阻止细胞周期进程。它还作为孤儿核受体NR4A1（Nur77）的转录抑制因子，通过抑制NR4A1的AB域介导的转录活性来调控基因表达。在线粒体中，GADD45GIP1作为线粒体核糖体大亚基蛋白mL64参与线粒体蛋白合成。这种核-线粒体双重定位在评估队列中独一无二，提示该蛋白可能作为协调核基因表达和线粒体功能的信号整合器。

PPI互作网络高度支持其核糖体和GADD45相关的功能。STRING数据库揭示了与线粒体核糖体亚基的极端高置信度互作：MRPL58（994）、MRPL40（986）、MRPL51（984）、MRPL15（984）、MRPL52（981）和MRPL10（973），确认了其核糖体身份。同时，与GADD45A（985）和GADD45G（971）的极端高置信度互作验证了其GADD45结合功能。PPI degree=317的高结合度反映了该蛋白在多个功能模块中的核心位置——核糖体模块、细胞周期调控模块和核受体调控模块的交汇点。

从TE调控角度，GADD45GIP1的研究前景值得关注。GADD45家族蛋白是已知的表观遗传调控因子——GADD45A可促进DNA去甲基化、参与活性DNA去甲基化途径（通过碱基切除修复），并调控特定基因组位点的表观遗传状态。GADD45GIP1作为GADD45的互作伙伴，可能参与GADD45介导的DNA去甲基化过程。考虑到TE元件的沉默高度依赖DNA甲基化（尤其是逆转座子元件的5mC修饰），GADD45GIP1-GADD45A复合体可能通过局部DNA去甲基化来激活或抑制特定TE元件。此外，GADD45GIP1与NR4A1的互作将雄激素受体信号通路与TE调控联系起来——NR4A1在激素响应基因调控中发挥重要作用，许多TE元件含有激素响应元件。PMID 42116756（Ann Med, 2026）关于CRIF1在乳腺癌预后和免疫浸润中作用的综合分析进一步支持了其作为潜在治疗靶标的价值。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MRPL58 | STRING | 994 |
| MRPL40 | STRING | 986 |
| GADD45A | STRING | 985 |
| MRPL51 | STRING | 984 |
| MRPL15 | STRING | 984 |
| MRPL52 | STRING | 981 |
| MRPL10 | STRING | 973 |
| GADD45G | STRING | 971 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q7LAX7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000179271-GADD45GIP1

![](https://images.proteinatlas.org/55205/878_F6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/878_F6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/1905_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/1905_F4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/873_F6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/873_F6_6_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000179271-GADD45GIP1

![](https://images.proteinatlas.org/55205/878_F6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/878_F6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/1905_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/1905_F4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/873_F6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/873_F6_6_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000179271-GADD45GIP1

![](https://images.proteinatlas.org/55205/878_F6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/878_F6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/1905_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/1905_F4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/873_F6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/55205/873_F6_6_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 41**

| 42116756 | Comprehensive analysis suggests CRIF1 is a potential target in breast cancer associated with prognosis and immune infilt | Ann Med 2026 |
| 41606585 | Unresolved questions on the GADD45GIP1-RPL35 axis in osteosarcoma: mechanistic links to ER stress and therapeutic target | Cancer Cell Int 2026 |
| 40905463 | Identification of EMT-related subtype and a 9 genes signature predicts the prognosis in osteosarcoma. | Connect Tissue Res 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GADD45GIP1

