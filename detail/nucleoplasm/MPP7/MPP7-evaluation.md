---
type: protein-evaluation
gene: "MPP7"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MPP7 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MPP7 |
| 蛋白名称 | MAGUK p55 subfamily member 7 |
| 蛋白大小 | 576 aa / 65.5 kDa |
| UniProt ID | Q5T2T1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cell Junctions; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 576 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=45 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=80.2; PDB=2 |
| 调控结构域 | 4/10 | ×2 | 8.0 | GK/Ca_channel_bsu; Guanylate_kin-like_dom; Guanylate_kinase_CS |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=98 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +2 |

### 3. 分析
- Cell Junctions; Nucleoplasm (Supported)
- PubMed strict=45 broad=59
- AF pLDDT=80.2 PDB=2
- InterPro: GK/Ca_channel_bsu; Guanylate_kin-like_dom; Guanylate_kinase_CS
- Pfam: Guanylate_kin; L27; PDZ
- PPI degree=98 ChIP: None
38016970: Proteomic characterization of epithelial ovarian cancer delineates molecular sig | 41484943: MPP7 inhibits tumor metastasis through promoting snail degradation in clear cell | 14719143: Identification and characterization of human MPP7 gene and mouse Mpp7 gene in si

### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

MPP7（MAGUK p55 subfamily member 7）是576个氨基酸的膜相关鸟苷酸激酶（MAGUK）家族成员，其多结构域模块化架构是MAGUK蛋白的经典范式。从N端到C端依次为：L27结构域（IPR004172，介导与DLG1的异源二聚化）、PDZ结构域（IPR041489，约90个氨基酸的紧凑球状折叠，识别靶蛋白C端的T/S-X-V/I-COOH基序）、SH3结构域和Guanylate_kinase（GK）结构域（IPR008144/Guanylate_kin-like_dom）。GK结构域尽管与真正的GMP激酶序列同源，但催化活性已丧失——它已进化成专司蛋白-蛋白互作的磷酸化肽结合模块。AlphaFold预测pLDDT高达80.2，配合2个PDB条目，MPP7是本批次中多结构域分析最为可靠的蛋白之一。

MPP7的核心细胞功能为上皮细胞极性和紧密连接（tight junction）组装的关键适配蛋白。通过与DLG1直接结合（L27-L27异源二聚化），MPP7被招募至新生细胞-细胞接触位点，其PDZ和GK结构域进一步招募和组装紧密连接特异性蛋白（如claudins、occludin）及细胞骨架连接因子。这一分步组装过程确保了上皮屏障的形成和极性轴的正确建立。HPA Supported的Cell Junctions定位完全印证了这一经典功能，但同时获得的Nucleoplasm评分暗示其可能具有非连接功能。

PPI网络（degree=98）揭示了惊人的"双面人生"模式：STRINg高分互作——CHAF1A（染色质组装因子1A，STRING=999）、RBBP4（Rb结合蛋白4/p48，STRING=999）、ASF1B/ASF1A（组蛋白伴侣，STRING=993/988）、PCNA（STRING=933）、HIST1H4H（组蛋白H4，STRING=929）——全部是核内染色质/组蛋白相关蛋白，而非细胞连接组分。这种"互作组重定向"强烈暗示MPP7的核内池参与了染色质组装和组蛋白转运——一个与细胞连接功能完全不同的功能域。

MPP7的最关键发现为：其通过促进Snail降解来抑制肿瘤转移——尤其在透明细胞肾癌中（PMID:41484943）。这一机制建立了一条直接的"核连接蛋白→转录因子降解"信号轴——MPP7可能通过招募E3泛素连接酶（类似于DLG1通过Scribble复合体招募APC/C）促进Snail的泛素化-蛋白酶体降解，从而拮抗EMT。这一发现完美解释了MPP7在上皮极性（EMT逆转->MET）和核内染色质/转录（组蛋白调控和Snail转录抑制功能）中的双重角色。从TE调控角度，MAGUK蛋白的TE调控角色几乎未被探索——MPP7通过控制Snail稳定性间接调控EMT过程中转座子活性是一个令人兴奋的研究假说。

**蛋白全称**: MAGUK p55 subfamily member 7

**功能**: Acts as an important adapter that promotes epithelial cell polarity and tight junction formation via its interaction with DLG1. Involved in the assembly of protein complexes at sites of cell-cell contact

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR008145 |
| InterPro | IPR008144 |
| InterPro | IPR020590 |
| InterPro | IPR014775 |
| InterPro | IPR004172 |
| InterPro | IPR036892 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CHAF1A | STRING | 999 |
| RBBP4 | STRING | 999 |
| ASF1B | STRING | 993 |
| ASF1A | STRING | 988 |
| PCNA | STRING | 933 |
| HIST1H4H | STRING | 929 |
| HEL25 | STRING | 911 |
| CBX5 | STRING | 911 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5T2T1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000150054-MPP7

![](https://images.proteinatlas.org/37597/1549_H6_3_red_green.jpg)
![](https://images.proteinatlas.org/37597/1549_H6_4_red_green.jpg)
![](https://images.proteinatlas.org/37597/1529_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/37597/1529_G4_3_red_green.jpg)
![](https://images.proteinatlas.org/37597/1515_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/37597/1515_H6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 59**

| 42250062 | Identification and external validation of a prognostic signature based on bone morphogenetic protein-related mRNAs for k | Discov Oncol 2026 |
| 41979832 | Machine Learning-Based Identification of Molecular Signatures in PTOA Cell Subtypes via Single-Cell Transcriptomics in a | Stem Cell Rev Rep 2026 |
| 41764223 | MAGUK p55 subfamily member 7 attenuates allergic airway inflammation by modulating lung dendritic cells functions. | Sci Rep 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MPP7

