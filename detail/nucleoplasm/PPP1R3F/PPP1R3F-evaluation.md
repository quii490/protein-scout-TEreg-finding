---
type: protein-evaluation
gene: "PPP1R3F"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PPP1R3F 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PPP1R3F |
| 蛋白名称 | Protein phosphatase 1 regulatory subunit 3F |
| 蛋白大小 | 799 aa / 82.8 kDa |
| UniProt ID | Q6ZSY5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 799 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=48.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | CBM21_dom; CBM21_dom_sf; PP1_regulatory_subunit_3 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=21 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=5 broad=6
- AF pLDDT=48.8 PDB=0
- InterPro: CBM21_dom; CBM21_dom_sf; PP1_regulatory_subunit_3
- Pfam: CBM_21
- PPI degree=21 ChIP: None
37531237: Hemizygous variants in protein phosphatase 1 regulatory subunit 3F (PPP1R3F) are | 39000267: Genetic and Epigenetic Association of FOXP3 with Papillary Thyroid Cancer Predis | 20479760: Systematic resequencing of X-chromosome synaptic genes in autism spectrum disord

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

PPP1R3F（Protein Phosphatase 1 Regulatory Subunit 3F）是一个799 aa的大分子PP1靶向亚基，其结构域架构包含两个关键功能模块：N端CBM21碳水化合物结合模块（Pfam CBM_21, InterPro IPR005036），负责将PP1催化亚基靶向糖原颗粒；C端PP1调控亚基3家族保守区（InterPro IPR050782）。AlphaFold2预测pLDDT仅为48.8（得分4/10），且无PDB实验结构，提示该蛋白含有大量内在无序区域（IDR），可能通过液-液相分离（LLPS）在核质中形成功能性凝聚体。

PPP1R3F的PPI网络度为21，其互作伙伴揭示了一个与激酶-磷酸酶平衡相关的信号网络。与DYRK1A和DYRK1B（双特异性酪氨酸磷酸化调控激酶）的BioGRID互作尤为关键——DYRK1A是核内关键的磷酸化调控因子，参与转录延伸、pre-mRNA剪接和染色质重塑。PPP1R3F与DYRK1A的协同调控可能在核质中形成磷酸化-去磷酸化开关，控制底物蛋白的活性状态。与WDR5（MLL/COMPASS组蛋白甲基转移酶复合物核心亚基）的互作则直接连接PPP1R3F与组蛋白修饰和表观遗传调控。

PPP1R3F的功能研究几乎为空白（PubMed=5，得分10/10），但临床遗传学已提供重要线索。PMID:37531237报道PPP1R3F半合子变异与神经发育障碍相关，提示该蛋白在脑发育中不可或缺。PPP1R3F定位在X染色体上，PMID:39000267发现FOXP3与甲状腺乳头状癌的遗传和表观遗传关联涉及PPP1R3F所在区域。这些发现与PPP1R3F在核质（Approved级别）和囊泡中的定位高度一致——PP1靶向亚基在核内通过去磷酸化组蛋白H3、RNA聚合酶II CTD或剪接因子调控基因表达的多个层面。

PPP1R3F是典型的"高潜力、低认知"候选核蛋白。其高无序性（pLDDT=48.8）在核质蛋白中并不罕见——许多转录因子和染色质调控因子富含IDR以支持多价弱互作和相分离。CBM21结构域在核质中的功能意义是一个开放问题，可能涉及核内糖原代谢或O-GlcNAc修饰的糖信号感知。该蛋白的核定位特异性得分9/10和781 aa的较大分子量使其成为深入机制研究的理想靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Protein phosphatase 1 regulatory subunit 3F

**功能**: Glycogen-targeting subunit for protein phosphatase 1 (PP1)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR005036 |
| InterPro | IPR038175 |
| InterPro | IPR050782 |
| Pfam | PF03370 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DYRK1A | BioGRID | 0 |
| DYRK1B | BioGRID | 0 |
| PPP1CC | BioGRID | 0 |
| WDR5 | BioGRID | 0 |
| AGTR1 | BioGRID | 0 |
| GPR35 | BioGRID | 0 |
| HTR2B | BioGRID | 0 |
| PTGER4 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6ZSY5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000049769-PPP1R3F

![](https://images.proteinatlas.org/244/1207_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/244/1207_H9_4_red_green.jpg)
![](https://images.proteinatlas.org/244/169_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/244/169_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/244/171_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/244/171_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/75936/2163_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/75936/2163_G5_3_red_green.jpg)

### PubMed 文献

**PubMed count: 6**

| 39000267 | Genetic and Epigenetic Association of FOXP3 with Papillary Thyroid Cancer Predisposition. | Int J Mol Sci 2024 |
| 37531237 | Hemizygous variants in protein phosphatase 1 regulatory subunit 3F (PPP1R3F) are associated with a neurodevelopmental di | Hum Mol Genet 2023 |
| 34145793 | Methylation of three genes encoded by X chromosome in blood leukocytes and colorectal cancer risk. | Cancer Med 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PPP1R3F

