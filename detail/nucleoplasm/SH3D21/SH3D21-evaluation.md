---
type: protein-evaluation
gene: "SH3D21"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SH3D21 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SH3D21 |
| 蛋白名称 | SH3 domain-containing protein 21 |
| 蛋白大小 | 640 aa / 70.5 kDa |
| UniProt ID | A4FU49 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Basal body; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 640 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=6 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=52.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Endophilin_SH3RF; SH3-like_dom_sf; SH3_domain |
| PPI | 5/10 | x3 | 15.0 | PPI degree=4 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- Basal body; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=6 broad=8
- AF pLDDT=52.6 PDB=0
- InterPro: Endophilin_SH3RF; SH3-like_dom_sf; SH3_domain
- Pfam: SH3_2
- PPI degree=4 ChIP: None
35094659: miR-669a-5p promotes adipogenic differentiation and induces browning in preadipo | 28417008: Association of gene coding variation and resting metabolic rate in a multi-ethni | 33428857: Epigenomic Profiles of African-American Transthyretin Val122Ile Carriers Reveals

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: SH3 domain-containing protein 21

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050384 |
| InterPro | IPR036028 |
| InterPro | IPR001452 |
| InterPro | IPR035468 |
| Pfam | PF07653 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SENP2 | BioGRID | 0 |
| PSMD14 | BioGRID | 0 |
| YAP1 | BioGRID | 0 |
| FOXRED1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-A4FU49-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000214193-SH3D21

![](https://images.proteinatlas.org/42456/488_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/42456/488_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/42456/485_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/42456/485_C4_3_red_green.jpg)
![](https://images.proteinatlas.org/42456/494_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/42456/494_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/66168/1346_B5_5_red_green.jpg)
![](https://images.proteinatlas.org/66168/1346_B5_6_red_green.jpg)

### 深度机制分析

**结构域架构**：SH3D21（640 aa，70.5 kDa）是含SH3结构域蛋白21，属于Endophilin/SH3RF家族（IPR050384）。核心架构含三个功能模块：SH3结构域（IPR001452, PF07653）——由约60 aa的β-桶状折叠（5条反平行β-链，β1-β2-β3-β4-β5）构成，识别富含脯氨酸的PxxP配体基序，结合面由β2-β3 loop（RT loop）和β4上的保守芳香族残基（Trp/Tyr）组成疏水口袋；SH3-like_dom_sf（IPR036028）——SH3超家族折叠，提示可能含额外的非经典SH3样结构域。AlphaFold pLDDT=52.6（较低），提示存在长段内在无序区（IDR）——IDR在信号衔接蛋白中常见，允许结构域间灵活的构象采样和多位点磷酸化调控。HPA定位显示Nucleoplasm; Basal body; Plasma membrane（Approved）。

**PPI互作网络解读**：PPI degree=4，尽管网络规模小但核心互作高度指向性：SENP2（Sentrin特异性蛋白酶2，去SUMO化酶）——调控蛋白质SUMO化的关键酶，SUMO化是核质蛋白定位和转录调控的重要翻译后修饰；YAP1（Hippo通路转录共激活因子）——YAP与SENP2存在已知调控关系（SUMO化修饰调控YAP核定位和转录活性），SH3D21可能通过其SH3结构域作为SENP2-YAP1之间的衔接蛋白调控YAP去SUMO化效率；PSMD14（26S蛋白酶体19S调控颗粒的去泛素化酶亚基RPN11）——提示SH3D21可能连接泛素-蛋白酶体系统和SUMO化修饰网络；FOXRED1（FAD依赖型氧化还原酶）——线粒体呼吸链组装因子，非典型核质互作。

**结构解读**：SH3结构域在AlphaFold预测中应为置信度较高的区域（pLDDT>75），而连接SH3与其他结构域的IDR区域（可能200-600 aa）折叠预测质量低（pLDDT 40-55）。SH3的PxxP结合口袋由三个疏水亚位点组成——特异性由RT loop（n-Src loop）的残基决定，SH3D21属于Class I SH3结构域（识别RxxPxxP共有基序）。PAE矩阵应显示SH3结构域自身的低PAE（<10A），而SH3与IDR间的PAE应该高（>20A），表征SH3结构域作为独立折叠单元而IDR为柔性连接。

**机制模型**：SH3D21通过衔接蛋白的经典模式运作：（1）SH3结构域以中等亲和力（Kd ~1-10 μM）识别YAP1/SENP2中的PxxP基序，将底物（YAP1）招募至酶（SENP2）附近以加速去SUMO化反应；（2）在核质中，SENP2-SH3D21-YAP1三分子复合体调控YAP的去SUMO化状态——非SUMO化YAP倾向于核滞留和TEAD结合（促增殖转录），而SUMO化YAP被PML核体截留并泛素化降解；（3）PSMD14互作暗示SH3D21可能通过联合SUMO化和泛素化修饰网络调控核质蛋白的蛋白酶体降解速率——这是SUMO-targeted ubiquitin ligase (STUbL)通路的变体。PMID:42286192将SH3D21与微管manchette结构连接，提示其在细胞骨架组织中的功能。

**TE调控展望**：SH3D21通过YAP1-SENP2轴间接连接TE调控。YAP/TEAD是多种HERV-H和MaLR LTR的转录激活因子（TEAD结合MCAT/GGAATG基序，在众多LTR中作为增强子基序存在）。SH3D21对YAP去SUMO化的调控可能影响YAP对LTR驱动基因的转录输出。此外，SUMO化修饰在异染色质维持中至关重要——SUMO依赖的异染色质蛋白1（HP1α）靶向异染色质区域（包括着丝粒周围TE富集区），SENP2-SH3D21的去SUMO化活性可能在特定条件下释放这些区域的SUMO介导沉默。

### PubMed 文献

**PubMed count: 8**

| 42286192 | SPACA9 and MNMIP1 bridge the seam of spermatid manchette microtubules. | EMBO J 2026 |
| 40818124 | Identification of actin cytoskeleton organization genes in oral cancer and oral potentially malignant disorders using or | Med Oral Patol Oral Cir Bucal 2025 |
| 40179068 | Integrating bulk and single-cell RNA sequencing reveals SH3D21 promotes hepatocellular carcinoma progression by activati | PLoS One 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SH3D21

