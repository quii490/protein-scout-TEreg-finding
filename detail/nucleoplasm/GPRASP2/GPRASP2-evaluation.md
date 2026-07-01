---
type: protein-evaluation
gene: "GPRASP2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GPRASP2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GPRASP2 |
| 蛋白名称 | G protein-coupled receptor-associated sorting protein 2 |
| 蛋白大小 | 838 aa / 93.8 kDa |
| UniProt ID | Q96D09 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 838 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=20 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=49.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | ARM-like; ARM-rpt_dom; ARM-type_fold |
| PPI | 7/10 | x3 | 21.0 | PPI degree=123 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=20 broad=31
- AF pLDDT=49.9 PDB=0
- InterPro: ARM-like; ARM-rpt_dom; ARM-type_fold
- Pfam: Arm_2
- PPI degree=123 ChIP: None
39706197: Chromosome X-wide common variant association study in autism spectrum disorder. | 39479518: GPRASP protein deficiency triggers lymphoproliferative disease by affecting B-ce | 32027737: GPRASP proteins are critical negative regulators of hematopoietic stem cell tran

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

GPRASP2（G蛋白偶联受体相关分选蛋白2）是838个氨基酸的大分子支架蛋白，其结构特征为ARM-like（IPR011989）串联重复折叠和ARM-type fold（IPR016024）的三维架构。ARM重复作为经典的蛋白-蛋白互作模块，赋予GPRASP2高度的构象可塑性——能够同时与多个伙伴蛋白形成动态的相互作用界面。然而，AlphaFold预测的pLDDT仅为49.9，提示蛋白含有大量内在无序区（IDR），这些柔性区域可能充当分子海绵，通过液-液相分离（LLPS）机制富集GPCR分选相关因子。

PPI网络分析（degree=123）揭示了GPRASP2作为E3泛素连接酶底物适配器的核心功能：与BTRC（β-TrCP）、CUL3的互作（BioGRID评分=1）指示其参与基于Cullin-RING E3连接酶（CRL）的泛素化途径。GPRASP2通过识别特定GPCR的胞内尾部序列，将其招募至BTRC/CUL3复合体进行泛素化标记，从而介导受体的溶酶体分选与降解。与BARD1的互作进一步将GPRASP2连接至DNA损伤修复与中心体功能，而与HTT（亨廷顿蛋白）的互作则暗示可能的神经退行性疾病关联。

HPA Approved的核质定位（Nucleoplasm）与经典胞质功能（endocytic trafficking）的共存是该蛋白最引人注目的特征。GPRASP2缺乏经典核定位信号，其入核可能通过ARM重复结构域介导的"piggyback"机制——即通过与携带NLS的核蛋白（如TCF25、LRIF1）结合而被动转运。最新研究显示GPRASP2维持造血干细胞（HSC）的静息态需要其内吞体分选功能（PMID:41726907），而GPRASP2缺陷导致淋巴增殖性疾病（PMID:39479518），这强烈提示该蛋白在核质中可能直接调控干性相关转录程序。

从TE调控研究角度来看，GPRASP2作为核质定位的GPCR调控支架蛋白，其新颖性（PubMed=20，得分9/10）极高。GPRASP蛋白是HSC移植的关键负调控因子（PMID:32027737），敲除后可增强HSC的植入效率——这一表型可能部分通过其核内功能实现。鉴于ARM重复蛋白在TE调控网络中的潜在角色，GPRASP2值得作为优先候选进行功能获得/缺失的TE活性报告基因筛选。

**蛋白全称**: G protein-coupled receptor-associated sorting protein 2

**功能**: May play a role in regulation of a variety of G protein coupled receptors

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011989 |
| InterPro | IPR006911 |
| InterPro | IPR016024 |
| InterPro | IPR043374 |
| Pfam | PF04826 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TCF25 | STRING | 994 |
| PIFO | STRING | 805 |
| BTRC | BioGRID | 1 |
| CUL3 | BioGRID | 1 |
| LRIF1 | BioGRID | 1 |
| BARD1 | BioGRID | 1 |
| HTT | BioGRID | 1 |
| TXN2 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96D09-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000158301-GPRASP2

![](https://images.proteinatlas.org/17438/173_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/173_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/140_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/140_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/168_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/168_D1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000158301-GPRASP2

![](https://images.proteinatlas.org/17438/173_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/173_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/140_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/140_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/168_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/168_D1_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000158301-GPRASP2

![](https://images.proteinatlas.org/17438/173_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/173_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/140_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/140_D1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/168_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17438/168_D1_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 31**

| 41726907 | Elevated endocytic trafficking mediated by GPRASP2 maintains HSC fidelity. | bioRxiv 2026 |
| 41688572 | Abnormal iron homeostasis mediates cochlear hair cell impairment and hearing loss in Gprasp2-deficient mice. | Commun Biol 2026 |
| 39706197 | Chromosome X-wide common variant association study in autism spectrum disorder. | Am J Hum Genet 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GPRASP2

