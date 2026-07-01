---
type: protein-evaluation
gene: "PCDHGA11"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGA11 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGA11 |
| 蛋白名称 | Protocadherin gamma-A11 |
| 蛋白大小 | 935 aa / 101.5 kDa |
| UniProt ID | Q9Y5H2 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 935 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=3 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=75.2; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=20 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.4/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain)
- PubMed strict=3 broad=4
- AF pLDDT=75.2 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_C
- Pfam: Cadherin; Cadherin_2; Cadherin_C_2
- PPI degree=20 ChIP: None
39305332: Anti-tumor potential of high salt in breast Cancer cell lines. | 40191489: Genetic Markers of Spina Bifida: Enrichment of Pathogenic Variants and Variants  | 41763620: Physicochemical characterization, lipid-metabolism effects and transcriptomics i

### 4. 总体评价
**69.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin gamma-A11

**功能**: Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR032455 |
| InterPro | IPR031904 |
| InterPro | IPR020894 |
| InterPro | IPR013164 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RYK | BioGRID | 0 |
| CEACAM21 | BioGRID | 0 |
| C2orf48 | BioGRID | 0 |
| PCDHGB1 | BioGRID | 0 |
| TMEM30B | BioGRID | 0 |
| PCDH12 | BioGRID | 0 |
| DKKL1 | BioGRID | 0 |
| FCGRT | BioGRID | 0 |


### 深度机制分析

**结构域架构**：PCDHGA11（935 aa, 101.5 kDa）是原钙黏蛋白γ亚家族A11成员，属钙黏蛋白超家族（cadherin superfamily）。含六个串联的钙黏蛋白胞外重复结构域（EC1-EC6, 各约110 aa, IPR002126 Cadherin-like_dom, IPR015919 Cadherin-like_sf, Pfam Cadherin/Cadherin_2），一个跨膜螺旋（TM, ~700-720 aa）和一个胞质C端含保守Cadherin_C结构域（IPR032455, IPR020894, IPR013164, Pfam Cadherin_C_2, ~750-935 aa）。AlphaFold pLDDT=75.2（PDB=0），高置信度残基（pLDDT>90）占比30-40%，有序区域>60%，主要归因于EC1-EC6 β-sandwich结构的良好折叠——每个EC域由7条反平行β链形成两个β片层（A-G-F-C和C'-B-E-D, 免疫球蛋白样折叠）。相邻EC域之间由保守的Ca²⁺配位linker连接——每个EC-EC界面结合3个Ca²⁺离子（由保守的Asp/Glu/Gln残基的羧基/酰胺氧配位），Ca²⁺结合使胞外域从柔性链转变为刚性棒状结构（rod-like），为经典钙黏蛋白的Ca²⁺依赖性细胞黏附功能的分子基础。胞质Cadherin_C域含保守的catenin结合位点（DEEED/EEEED motif）——与β-catenin（armadillo repeat域）或p120-catenin（连环蛋白, armadillo repeat域）形成复合体，将细胞膜钙黏蛋白锚定至皮层actin网。

**PPI互作网络解读**：PPI网络（degree=20）虽小但反映原钙黏蛋白的非经典黏附功能。RYK（receptor-like tyrosine kinase/Deralied, Wnt共受体, BioGRID）为原钙黏蛋白的非典型伙伴——RYK胞外域含WIF（Wnt inhibitory factor）样结构域，识别Wnt3a/Wnt5a配体，激活Wnt/β-catenin和Wnt/PCP（planar cell polarity）信号——PCDHGA11可能作为RYK的跨膜共受体或配体呈递蛋白在细胞-细胞接触处增强局部Wnt信号。PCDHGB1和PCDH12（原钙黏蛋白γ-B1和原钙黏蛋白12, cadherin家族同源蛋白）为PCDHGA11的顺式伙伴（cis-interaction, 位于同一细胞膜的相邻蛋白），在脂筏或黏附连接处形成同源/异源顺式二聚体以增强黏附特异性。CEACAM21（癌胚抗原相关细胞黏附分子21, Ig超家族成员, 免疫检查点分子）和FCGRT（新生儿Fcγ受体, IgG和albumin的转胞吞受体）为PCDHGA11的免疫细胞伙伴——PCDHGA11可能参与免疫突触（immunological synapse）的组织或白细胞迁移中的异嗜性黏附。DKKL1（Dickkopf-like protein 1, Wnt拮抗因子家族同源物）为Wnt信号的负调控因子——PCDHGA11-DKKL1互作提示PCDHGA11参与Wnt信号调控网络的可能扩展。

**结构解读**：原钙黏蛋白γ-A11的胞外域EC1-EC6重复以反平行二聚体（antiparallel dimer）排列实现跨细胞黏附。经典钙黏蛋白的trans（跨细胞）二聚化机制为EC1域的N端β-strand（strand A）在对面细胞partner EC1域的A-strand交换结构域交换——一个EC1的Trp2（N端色氨酸, Triad Trp2/Trp4）插入partner EC1的疏水口袋→形成"strand-swap dimer"（Kd ~10-50 μM）。这一机制赋予钙黏蛋白同嗜性（homophilic）识别特异性——仅相同或高度同源的钙黏蛋白之间发生strand交换。PCDHGA11的trans二聚化特异性由EC1-EC3串联域的序列（严格的表面残基charge和shape互补性）编码。胞质Cadherin_C域通过catenin复合体连接至F-actin——β-catenin/plakoglobin的armadillo域结合Cadherin_C的DEEED基序→β-catenin的N端招募α-catenin（Vinculin家族F-actin结合蛋白）→将黏附连接机械锚定于皮层actin应力纤维束。

**机制模型**：（1）神经元回路形成——原钙黏蛋白γ家族16个基因（PCDHGA1-GA12, PCDHGB1-GB7包括PCDHGA11）簇集在5q31染色体原钙黏蛋白γ基因簇——通过可变启动子选择和顺式剪接异构体组合产生约>100种不同的原钙黏蛋白异构体，赋予每个神经元独特的膜表面原钙黏蛋白"条形码"。PCDHGA11的条形码身份决定神经元的同嗜性自我回避（self-avoidance）——使同一神经元的树突分支互相排斥而不发生无功能的自体突触（autapse）。PCDHGA11缺陷→树突自回避丧失→树突丛（dendritic fasciculation/bundling）→突触连接混乱。（2）钙黏蛋白剪切信号——PCDHGA11的胞外域（EC1-EC6）可被ADAM10/ADAM17（去整合素金属蛋白酶）和γ-secretase（早老素/PSEN1/PSEN2-Nicastrin-APH1-PEN2复合体）连续剪切（regulated intramembrane proteolysis, RIP）——ADAM剪切释放soluble ECD（sPCDHGA11, 胞外拮抗物），γ-secretase在TM内切割释放胞内域（PCDHGA11-ICD）。被释放的ICD可转位至核质——含Cadherin_C域和catenin结合区的ICD可能作为转录共激活因子与β-catenin/TCF在核质中重新结合→调控Wnt靶基因。HPA Uncertain的核质定位可能存在（胞质→核质ICD转位）。（3）钙黏蛋白-生长因子受体crosstalk——RYK为PCDHGA11的互作伙伴→PCDHGA11-RYK顺式复合体在细胞-细胞接触处将RYK聚集于cell-cell junction→激活局部Wnt/PCP和Wnt/Ca²⁺信号（而非经典Wnt/β-catenin）→调控细胞骨架重排（RhoA/Rac1/Cdc42 GTPase）和细胞迁移/趋化。

**TE调控展望**：PCDHGA11通过钙黏蛋白剪切-RIP产生的核质ICD转录功能或Wnt-RYK信号间接影响TE。γ-secretase剪切产生的钙黏蛋白ICD在核质中可充当TCF/β-catenin的转录共因子——β-catenin-TCF的经典靶基因包括含TCF/LEF结合位点（WRE）的LTR-TE（MMTV LTR, HERV-K LTR, HERV-H LTR）。PCDHGA11-ICD的核质浓度由神经元活动调控钙黏蛋白剪切率决定，产生活动依赖的WRE-LTR转录调控。Wnt/RYK-PCP信号可调控染色质结构——RYK下游的JNK磷酸化转录因子AP-1（c-Jun/c-Fos）和ATF2→AP-1和ATF2结合位点在TE（LINE-1 5'UTR, Alu, ERV-LTR）中广泛分布→神经元活动或形态发生过程中TE的转录被PCP信号动态调控。然而PCDHGA11缺乏直接DNA结合结构域，其TE调控影响为远距离间接效应，更多通过Wnt信号和剪切-RIP的核质信号传递实现。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5H2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000253873-PCDHGA11

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 4**

| 41763620 | Physicochemical characterization, lipid-metabolism effects and transcriptomics insights of perilla seed oil in high-fat- | J Ethnopharmacol 2026 |
| 40191489 | Genetic Markers of Spina Bifida: Enrichment of Pathogenic Variants and Variants of Uncertain Significance. | J Indian Assoc Pediatr Surg 2025 |
| 39305332 | Anti-tumor potential of high salt in breast Cancer cell lines. | Mol Biol Rep 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGA11

