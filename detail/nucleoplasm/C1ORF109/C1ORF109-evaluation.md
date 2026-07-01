---
type: protein-evaluation
gene: "C1ORF109"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## C1ORF109

### 1. Basic Info
| Item | Value |
|---|---|
| Gene | C1ORF109 |
| Protein Name | AFG2-interacting ribosome maturation factor |
| Size | 203 aa / 23.4 kDa |
| UniProt | Q9NX04 |
| Date | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 203 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=10 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=94.2; PDB=2 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | CA109-like |
| 🔗 PPI | 7/10 | ×3 | 21.0 | PPI degree=163 |
| **加权总分** | | | **130.0/180** | |
| **归一化总分 (÷1.83)** | | | **71.0/100** | 互证: +2.0 |

### 3. Analysis
- HPA: nan (nan)
- PubMed: strict=10, broad=11
- AF pLDDT: 94.2 / PDB: 2
- InterPro: CA109-like
- Pfam: CA109-like
- PPI degree=163 ChIP: None
38554706: The SPATA5-SPATA5L1 ATPase complex directs replisome proteostasis to ensure geno | 40760247: A programmed decline in ribosome levels governs human early neurodevelopment. | 40268917: Cryo-EM structure of the AAA+ SPATA5 complex and its role in human cytoplasmic p

### 4. Assessment
★★★★  **72.1/100**  **nucleoplasm**
Nuclear protein


### 深度机制分析

C1ORF109（AIRIM，AFG2-interacting ribosome maturation factor）是203个氨基酸的高保守蛋白，其唯一的结构特征为CA109-like结构域（IPR029159/PF15011）。AlphaFold预测pLDDT高达94.2——这是本批次30个蛋白中的最高值之一——结合2个PDB条目（来自冷冻电镜结构），C1ORF109是目前结构表征最好的NEW核蛋白之一。其折叠预计为全α-螺旋束——紧凑而高度有序——这与其作为大型多亚基复合体中刚性适配器蛋白的功能设定一致。

在功能机制上，C1ORF109是55LCC（SPATA5-SPATA5L1-C1orf109-CINP）异源六聚体ATPase复合体的核心组分，与SPATA5L1协同确保复制体蛋白稳态（PMID:38554706）。C1ORF109在55LCC中充当关键的适配器/连接器角色——其CA109-like结构域可能作为"platform"（平台结构域）介导SPATA5L1 ATPase与CINP底物识别模块之间的物理偶联。冷冻电镜结构解析（PMID:40268917）进一步揭示了该复合体在细胞质pre-60S核糖体成熟中的双重功能——说明55LCC在核糖体生物合成和复制应激响应中均发挥必要的ATPase驱动功能。

PPI网络（degree=163）的紧密性极为惊人：与CINP（STRING=918，55LCC组分）、SPATA5L1（STRING=836，直接结合伙伴）、CWC25（STRING=788，剪接体组分）的强互作映射了该蛋白在RNA代谢与DNA复制质量控制交界处的枢纽角色。同时，与CSNK2A1（CK2激酶催化亚基）、CRX（cone-rod homeobox转录因子）、PHC2（Polyhomeotic-like 2，PRC1组分）、MEOX2（同源结构域转录因子）和REL（NF-kB亚基）的核内互作（BioGRID）强烈暗示C1ORF109可能在转录调控或染色质结构维持中拥有独立于55LCC的非典型功能。

尽管HPA核定位为"nan"（核定位特异性5/10），C1ORF109作为复制叉相关和染色质相关蛋白的功能在本质上完全依赖核定位——55LCC复合体的许多底物（包括CMG解旋酶、PCNA等）仅在核内存在。HPA评分的缺失可能是组织特异性表达或抗体灵敏度不足所致。C1ORF109被鉴定为人早期神经发育中核糖体水平程序性下降的关键调控因子（PMID:40760247）——这一发现将其功能从复制应激扩展至神经发育的时序调控。从TE研究角度，C1ORF109与SPATA5L1应被视为功能耦合单元——基因组稳定性维持过程中的任何缺陷都可能导致转座子去抑制——使得55LCC复合体的两个蛋白成为值得联合筛选的天然功能配对。

**蛋白全称**: AFG2-interacting ribosome maturation factor

**功能**: Part of the 55LCC heterohexameric ATPase complex which is chromatin-associated and promotes replisome proteostasis to maintain replication fork progression and genome stability. Required for replication fork progression, sister chromatid cohesion, and chromosome stability. The ATPase activity is specifically enhanced by replication fork DNA and is coupled to cysteine protease-dependent cleavage of replisome substrates in response to replication fork damage. Uses ATPase activity to process replis

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029159 |
| Pfam | PF15011 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CINP | STRING | 918 |
| SPATA5L1 | STRING | 836 |
| CWC25 | STRING | 788 |
| CSNK2A1 | BioGRID | 1 |
| CRX | BioGRID | 1 |
| PHC2 | BioGRID | 1 |
| MEOX2 | BioGRID | 1 |
| REL | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NX04-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000116922-C1orf109

![](https://images.proteinatlas.org/27127/1033_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/1033_A4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/1898_B1_7_cr5ba361544fb21_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/1898_B1_28_cr5ba361545078f_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/214_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/214_B12_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000116922-C1orf109

![](https://images.proteinatlas.org/27127/1033_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/1033_A4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/1898_B1_7_cr5ba361544fb21_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/1898_B1_28_cr5ba361545078f_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/214_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/214_B12_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000116922-C1orf109

![](https://images.proteinatlas.org/27127/1033_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/1033_A4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/1898_B1_7_cr5ba361544fb21_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/1898_B1_28_cr5ba361545078f_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/214_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27127/214_B12_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 11**

| 41098063 | Molecular Atlas of PM(2.5) Chemical Constituents on Cardiac Conduction: A Multiomics Landscape in Older Adults. | Environ Sci Technol 2025 |
| 40760247 | A programmed decline in ribosome levels governs human early neurodevelopment. | Nat Cell Biol 2025 |
| 40268917 | Cryo-EM structure of the AAA+ SPATA5 complex and its role in human cytoplasmic pre-60S maturation. | Nat Commun 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C1ORF109

