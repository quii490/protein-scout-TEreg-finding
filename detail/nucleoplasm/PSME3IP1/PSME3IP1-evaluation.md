---
type: protein-evaluation
gene: "PSME3IP1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PSME3IP1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PSME3IP1 |
| 蛋白名称 | PSME3-interacting protein |
| 蛋白大小 | 254 aa / 28.9 kDa |
| UniProt ID | Q9GZU8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm; Vesicles (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 254 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=67.8; PDB=2 |
| 调控结构域 | 4/10 | ×2 | 8.0 | FAM192A; FAM192A/Fyv6_N |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=43 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | Nucleoplasm; Vesicles (Supported) |
| PubMed | strict=0, broad=1 |
| AF pLDDT | 67.8 |
| PDB | 2 |
| InterPro | FAM192A; FAM192A/Fyv6_N |
| Pfam | FAM192A_Fyv6_N |
| PPI degree | 43 |
| ChIP | None |

### 4. 总体评价
★★★★  **72.1/100**  |  **nucleoplasm**
Nuclear protein


### 深度机制分析

PSME3IP1（PSME3-interacting protein，亦称NIP30或FAM192A）是一个254 aa的核质蛋白（28.9 kDa），属于FAM192A/Fyv6_N结构域家族（Pfam PF10187, InterPro IPR019331）。该结构域在进化上从酵母到人类高度保守，但在高等真核生物中获得了核内特异性功能。AlphaFold2预测pLDDT=67.8（得分6/10），PDB数据库中有2个实验结构，提示至少部分结构域已获得结构验证。

PSME3IP1的PPI网络具有一个鲜明的特征：其最强互作伙伴几乎全部来自剪接体和mRNA加工机器。STRING网络中以极高评分（>800）连接的DHX8（DEAH-box解旋酶8）、SLU7（剪接因子）、XAB2（XPA结合蛋白2）、BCAS2（乳腺癌扩增序列2）、CDC5L（细胞分裂周期5样蛋白）、PPIE（肽基脯氨酰异构酶E）、CACTIN（剪接体相关蛋白）和PRPF8（pre-mRNA加工因子8，核心剪接体组分，STRING=988）构成了一个紧密的剪接体互作簇。RBM8A（RNA结合基序蛋白8A，外显子连接复合物核心，STRING=999）和PRKRIP1（PRKRA互作蛋白1，STRING=820）的极端高评分进一步巩固了这一观察。这些互作表明PSME3IP1深度嵌入核内mRNA加工机器。

PSME3IP1的核心功能机制涉及蛋白酶体系统与Cajal body（卡哈尔体）之间的调控回路。根据UniProt功能注释，PSME3IP1通过促进蛋白酶体激活因子PSME3（REGγ）与20S蛋白酶体的结合来调控蛋白酶体活性，并抑制PSME3介导的某些底物降解。同时，PSME3IP1抑制PSME3与COIL（coilin，Cajal body标志蛋白）的互作，抑制PSME3在Cajal body中的积累，从而正向调控Cajal body的数量。Cajal body是核内snRNP生物发生和剪接体组装的关键场所，PSME3IP1通过这一机制间接调控剪接体功能。

唯一一篇直接相关的文献（PMID:32764536）揭示了NIP30通过REGγ抑制增加p53缺陷肿瘤细胞对化疗的敏感性。这是PSME3IP1在癌症治疗中的转化应用前景的重要线索。尽管PubMed=0直接文献（得分10/10，极高新颖性），但STRING网络揭示的剪接体互作簇为PSME3IP1的核内功能提供了强有力的预测证据。PSME3IP1可能代表了一类新型的蛋白酶体-剪接体交叉调控节点，在RNA加工和蛋白降解这两个关键核内过程之间建立功能连接。

### 补充分析 (UniProt API)

**蛋白全称**: PSME3-interacting protein

**功能**: Promotes the association of the proteasome activator complex subunit PSME3 with the 20S proteasome and regulates its activity. Inhibits PSME3-mediated degradation of some proteasome substrates, probably by affecting their diffusion rate into the catalytic chamber of the proteasome. Also inhibits the interaction of PSME3 with COIL, inhibits accumulation of PSME3 in Cajal bodies and positively regulates the number of Cajal bodies in the nucleus

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR039845 |
| InterPro | IPR019331 |
| Pfam | PF10187 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9GZU8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000172775-PSME3IP1

![](https://images.proteinatlas.org/54382/885_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/54382/885_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/54382/869_C10_3_red_green.jpg)
![](https://images.proteinatlas.org/54382/869_C10_4_red_green.jpg)
![](https://images.proteinatlas.org/54382/849_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/54382/849_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/59652/1011_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/59652/1011_C12_4_red_green.jpg)

### PubMed 文献

**PubMed count: 1**

| 32764536 | The REGγ inhibitor NIP30 increases sensitivity to chemotherapy in p53-deficient tumor cells. | Nat Commun 2020 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSME3IP1

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GSC | STRING | 954 |
| DHX8 | STRING | 837 |
| FAM32A | STRING | 806 |
| PSME3 | STRING | 630 |
| SLU7 | STRING | 833 |
| PSME3IP1 | STRING | 807 |
| XAB2 | STRING | 814 |
| BCAS2 | STRING | 806 |
| CDC5L | STRING | 848 |
| PPIE | STRING | 800 |
| CACTIN | STRING | 802 |
| PRKRIP1 | STRING | 820 |
| PRPF8 | STRING | 988 |
| RBM8A | STRING | 999 |
