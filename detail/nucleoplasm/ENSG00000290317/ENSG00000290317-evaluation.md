---
type: protein-evaluation
gene: "ENSG00000290317"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## ENSG00000290317 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ENSG00000290317 |
| 蛋白名称 | KRAB domain-containing protein 1 |
| 蛋白大小 | 128 aa / 14.9 kDa |
| UniProt ID | C9JBD0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 128 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=66.9; PDB=0 |
| 调控结构域 | 6/10 | x2 | 12.0 | KRAB; KRAB_dom_sf; Krueppel_C2H2_ZnF |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
- Golgi apparatus; Nucleoplasm (Approved)
- PubMed strict=0 broad=0
- AF pLDDT=66.9 PDB=0
- InterPro: KRAB; KRAB_dom_sf; Krueppel_C2H2_ZnF
- Pfam: KRAB
- PPI degree=0 ChIP: None


### 4. 总体评价
**73.8/100** | **nucleoplasm**
TE candidate: KRAB; KRAB_dom_sf; Krueppel_C2H2_ZnF


### 补充分析 (UniProt API)

**蛋白全称**: KRAB domain-containing protein 1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001909 |
| InterPro | IPR036051 |
| InterPro | IPR050169 |
| Pfam | PF01352 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: KRAB domain-containing protein 1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001909 |
| InterPro | IPR036051 |
| InterPro | IPR050169 |
| Pfam | PF01352 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

ENSG00000290317编码KRAB domain-containing protein 1，是KRAB锌指蛋白(KZFP)家族中的新预测成员。该蛋白兼具KRAB结构域(IPR001909/PF01352，位于N端)和Krueppel_C2H2_ZnF结构域(IPR050169，位于C端)。KRAB结构域是转录抑制的核心模块，通过招募KAP1/TRIM28辅抑制因子和组蛋白甲基转移酶SETDB1建立局部异染色质环境。C2H2锌指阵列赋予序列特异性DNA结合能力，将KRAB介导的抑制效应锚定至特定基因组位点。

该蛋白仅有128 aa(14.9 kDa)，是这批核蛋白中最小者。AlphaFold预测pLDDT仅66.9，C端锌指域的折叠置信度较低，可能反映了部分残基固有(IDR)的无序倾向。这种"低结构复杂度+强功能模块"的构型是许多转录因子的典型特征——高度有序的α-螺旋KRAB和二硫键稳定的锌指结构之间由柔性连接区域分隔，允许DNA扫描时的构象适应。

ENSG00000290317在HPA中被注释为Golgi apparatus和Nucleoplasm(Approved)。双定位特征提示其可能经历一种非经典的转运机制：新合成的KZFP在细胞质中被KAP1保护性结合，穿过核孔复合体后释放KAP1，在核质中结合靶DNA。高尔基体的附带定位可能是过表达或应激条件下的异常滞留。

该蛋白的PPI度degree=0，PubMed计数为0，是可获得的最新高新颖性蛋白。这同时意味着几乎所有的分析依赖于结构域推断和家族保守性建模。基于已知KRAB-ZNF蛋白的功能逻辑，ENSG00000290317很可能作为内源性逆转录病毒(ERV)和长末端重复序列(LTR)转座元件的转录抑制因子发挥作用。在胚胎早期发育过程中，KZFP特异性地沉默LTR启动子驱动的转座子转录，防止逆转录转座导致的基因组不稳定。该蛋白已被本评估系统标记为TE(yourself)候选因子(TE_REG_CANDIDATE)，是进一步的CRISPR激活/敲除功能验证实验的最高优先级候选对象。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-C9JBD0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 亚细胞定位: https://www.proteinatlas.org/ENSG00000290317-ENSG00000290317/subcellular


### HPA IF 图像

![](https://images.proteinatlas.org/46901/1331_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46901/1331_B2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/46901/1830_F1_61_blue_red_green.jpg)
![](https://images.proteinatlas.org/46901/1830_F1_63_blue_red_green.jpg)

