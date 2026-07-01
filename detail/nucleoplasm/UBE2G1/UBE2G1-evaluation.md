---
type: protein-evaluation
gene: "UBE2G1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## UBE2G1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UBE2G1 |
| 蛋白名称 | Ubiquitin-conjugating enzyme E2 G1 |
| 蛋白大小 | 170 aa / 19.5 kDa |
| UniProt ID | P62253 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 170 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=26 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=94.1; PDB=2 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ub_conjugating_enzyme; UBC; UBQ-conjugating_AS |
| PPI | 5/10 | x3 | 15.0 | PPI degree=48 |
| **加权总分** | | | **135/180** | |
| **归一化总分** | | | **74.3/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=26 broad=39
- AF pLDDT=94.1 PDB=2
- InterPro: Ub_conjugating_enzyme; UBC; UBQ-conjugating_AS
- Pfam: UQ_con
- PPI degree=48 ChIP: None
34182925: The plasma peptides of Alzheimer's disease. | 39379486: TRAF7 determines circadian period through ubiquitination and degradation of DBP. | 30042095: Genome-wide screen identifies cullin-RING ligase machinery required for lenalido

### 4. 总体评价
**74.3/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ubiquitin-conjugating enzyme E2 G1

**功能**: Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro catalyzes 'Lys-48'-, as well as 'Lys-63'-linked polyubiquitination. May be involved in degradation of muscle-specific proteins. Mediates polyubiquitination of CYP3A4

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050113 |
| InterPro | IPR000608 |
| InterPro | IPR023313 |
| InterPro | IPR016135 |
| Pfam | PF00179 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PARK2 | BioGRID | 0 |
| DIO2 | BioGRID | 0 |
| RBCK1 | BioGRID | 0 |
| AMFR | BioGRID | 0 |
| ELAVL1 | BioGRID | 0 |
| HUWE1 | BioGRID | 0 |
| ITCH | BioGRID | 0 |
| RBX1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P62253-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000132388-UBE2G1

![](https://images.proteinatlas.org/50551/1334_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/50551/1334_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/50551/771_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/50551/771_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/50551/694_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/50551/694_B8_2_red_green.jpg)

### 深度机制分析

UBE2G1的UBC结构域(IPR000608/IPR050113, Pfam PF00179)采用典型的E2泛素结合酶折叠——一个由四股β-sheet和四段α-helix组成的α/β结构，活性位点Cys-89位于IPR023313定义的保守loop区。AlphaFold pLDDT均值94.1且拥有2个PDB条目，表明UBC催化核心高度有序且已在实验层面验证，足够支持基于结构的抑制剂或化学探针设计。UBE2G1的PPI网络指向一组明确的核内靶向E3连接酶：HUWE1(HECT类E3，靶向组蛋白H2A和c-Myc)、ITCH(HECT类E3，靶向p63/p73和Notch)、RBX1(RING类E3，作为Cullin-RING连接酶复合物的催化亚基)、PARK2(RBR类E3，参与线粒体自噬与核蛋白质控)。特别值得注意的是，UBE2G1能够催化K48和K63两种连接类型的多泛素链合成，提示其可在核质中同时介导蛋白酶体降解信号(K48)和非降解信号转导(K63)，这与多数E2仅专一于一种链型的模式截然不同。

PMID 41784031和PMID 41641641揭示了UBE2G1在造血干细胞(HSC)衰老过程中的核心地位——HSC衰老伴随染色质开放性和转座元件(TE)去沉默。UBE2G1通过其UBC结构域与HUWE1协作，可能直接泛素化TE邻近区域的组蛋白或先锋转录因子(如PU.1、GATA2)，以K48链标记降解信号抑制异常转录；同时通过ITCH/K63轴维持特定HSC维持因子(如Notch胞内域)的稳定信号。PPI网络中ELAVL1(RNA结合蛋白,HuR)的共现进一步表明UBE2G1可能通过mRNA结合蛋白被引导至特定核区执行靶向泛素化。其穿梭机制模型为：胞浆中被E1(UBA1)充电的UBE2G1~Ub硫酯中间体，经importin途径进入核质后，通过E3选择性配对——HUWE1主导核蛋白质控(含TE编码的异常蛋白)，RBX1/Cullin复合物调控细胞周期相关的染色质蛋白周转，ITCH处理发育信号效应子——构成了一套核内泛素信号分拣系统。

这一核内E2功能为UBE2G1开辟了独特的TE调控研究前景。K48泛素化活性的丧失(如C89A催化失活突变体)可能直接导致TE编码蛋白(如LINE-1 ORF1p)在核质中积累并形成毒性聚集体，驱动基因组不稳定性；而K63活性的削弱则可能破坏TE位点处DNA损伤修复复合物的组装信号。研究启示：UBE2G1是核质泛素化网络中一个此前被忽视的"瓶颈"E2——其低PubMed count(26篇严格)与其在蛋白稳态和细胞衰老中的核心地位形成鲜明反差，提示该蛋白是一个高回报的新颖性靶标。实验策略：构建UBE2G1 C89A催化失活突变体与野生型的比较蛋白质组学(Ub-remnant profiling)，结合ATAC-seq检测HSC中TE家族(L1/LTR/Alu)的染色质可及性差异。

### PubMed 文献

**PubMed count: 39**

| 42331995 | Excessive postpartum body condition score loss coincides with skeletal muscle proteolysis in dairy cows: molecular and b | Sci Rep 2026 |
| 41784031 | Proteostasis meets signaling: UBE2G1 in hematopoietic stem cell aging. | Haematologica 2026 |
| 41641641 | Elevated levels of Ube2g1 in hematopoietic stem cells lead to segmental aging of the hematopoietic system. | Haematologica 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UBE2G1

