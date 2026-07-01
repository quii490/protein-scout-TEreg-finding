---
type: protein-evaluation
gene: "C17ORF49"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## C17ORF49

### 1. Basic Info
| Item | Value |
|---|---|
| Gene | C17ORF49 |
| Protein Name | BPTF-associated chromatin complex component 1 |
| Size | 172 aa / 17.9 kDa |
| UniProt | Q8IXM2 |
| Date | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) + ChIP |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 172 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=2 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=69.6; PDB=0 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | Homeodomain-like_sf; SANT/Myb |
| 🔗 PPI | 7/10 | ×3 | 21.0 | PPI degree=129 |
| **加权总分** | | | **129.0/180** | |
| **归一化总分 (÷1.83)** | | | **70.5/100** | 互证: +3.0 |

### 3. Analysis
- HPA: nan (nan)
- PubMed: strict=2, broad=11
- AF pLDDT: 69.6 / PDB: 0
- InterPro: Homeodomain-like_sf; SANT/Myb
- Pfam: BACC1_N
- PPI degree=129 ChIP: Yes
35672711: Synergistic anti-proliferative activity of JQ1 and GSK2801 in triple-negative br | 37108449: HMGXB4 Targets Sleeping Beauty Transposition to Germinal Stem Cells.

### 4. Assessment
★★★★  **72.1/100**  **nucleoplasm**
TE candidate: Homeodomain-like_sf; SANT/Myb


### 补充分析 (UniProt API)

**蛋白全称**: BPTF-associated chromatin complex component 1

**功能**: Component of chromatin complexes such as the MLL1/MLL and NURF complexes

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009057 |
| InterPro | IPR001005 |
| Pfam | PF27797 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| BPTF | STRING | 990 |
| HMGXB4 | STRING | 983 |
| SMARCA5 | STRING | 974 |
| SMARCA1 | STRING | 974 |
| RBBP4 | STRING | 964 |
| DPY30 | STRING | 943 |
| WDR5 | STRING | 935 |
| BAZ1A | STRING | 921 |



### 深度机制分析

C17ORF49（BPTF-associated chromatin complex component 1/BAP18，172 aa）是最具TE调控潜力的候选者之一。结构域包含Homeodomain-like超家族（IPR009057）和SANT/Myb结构域（IPR001005, PF27797），两者均为经典的染色质/DNA结合模块。SANT结构域是组蛋白尾部识别和染色质重塑复合物招募的核心结构。PPI网络（degree=129）高度富集染色质调控因子：BPTF（990，NURF复合物的最大亚基）、HMGXB4（983，转座子靶向因子）、SMARCA5/SNF2H（974，ISWI家族ATP酶）、RBBP4（964，组蛋白伴侣）、WDR5（935，MLL复合物核心组分）、DPY30（943）和BAZ1A（921）。关键文献36828916揭示BAP18促进CTCF介导的染色质可及性以调控乳腺癌增强子活性（Cell Death Differ 2023），38042310发现BAP18作为PPARalpha新共调控因子促进肝癌发生。该蛋白作为MLL1/MLL和NURF染色质重塑复合物的组分，通过SANT结构域识别组蛋白尾部，直接参与建立和维持开放染色质状态。其与CTCF的功能关联尤其重要——CTCF是绝缘子和染色质环锚定蛋白，在TE区域广泛分布。C17ORF49可能通过稳定CTCF占据或增强NURF在TE增强子处的活性调控TE驱动的基因表达，是TE调控的高优先级机制候选者。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8IXM2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000258315-C17orf49

![](https://images.proteinatlas.org/22961/193_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/22961/193_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/22961/192_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/22961/192_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/22961/194_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/22961/194_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/24457/196_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/24457/196_E7_1_red_green.jpg)

### PubMed 文献

**PubMed count: 11**

| 38042310 | BAP18 acting as a novel peroxisome proliferator-activated receptor α co-regulator contributes to hepatocellular carcinom | Biochim Biophys Acta Mol Basis Dis 2024 |
| 37108449 | HMGXB4 Targets Sleeping Beauty Transposition to Germinal Stem Cells. | Int J Mol Sci 2023 |
| 36828916 | BAP18 facilitates CTCF-mediated chromatin accessible to regulate enhancer activity in breast cancer. | Cell Death Differ 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C17ORF49

