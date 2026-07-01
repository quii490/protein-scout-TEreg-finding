---
type: protein-evaluation
gene: "MPIG6B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MPIG6B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MPIG6B |
| 蛋白名称 | Megakaryocyte and platelet inhibitory receptor G6b |
| 蛋白大小 | 241 aa / 26.2 kDa |
| UniProt ID | O95866 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Endoplasmic reticulum; Golgi apparatus; N (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 241 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=15 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=73.2; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | G6B; G6B_V-set |
| PPI | 5/10 | x3 | 15.0 | PPI degree=4 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- Cytosol; Endoplasmic reticulum; Golgi apparatus; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=15 broad=35
- AF pLDDT=73.2 PDB=1
- InterPro: G6B; G6B_V-set
- Pfam: G6B
- PPI degree=4 ChIP: None
35134123: G6b-B regulates an essential step in megakaryocyte maturation. | 40643151: Thrombocytopenia in myelofibrosis is characterized by inflammatory megakaryocyte | 35940081: A novel MPIG6B gene mutation in an adolescent girl with congenital thrombocytope

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

MPIG6B（G6b/G6b-B）是一个241个氨基酸的I型跨膜抑制性免疫受体，属于免疫球蛋白超家族（IgSF）的血小板特异性亚群。其胞外区含有单个G6B_V-set Ig-like结构域（IPR048308），这是一类截短的V-set结构域——仅含部分β-三明治折叠，通过非经典二硫键稳定。胞内区含两个串联的免疫受体酪氨酸抑制基序（ITIM），这是抑制性免疫受体的标志性信号单元。AlphaFold预测pLDDT为73.2，结合1个PDB条目（胞外V-set结构域），结构表征较为完整。

经典的ITIM信号机制为：受体被配体交联/聚集后，Src家族激酶磷酸化ITIM内的关键酪氨酸残基，磷酸化的ITIM招募含SH2结构域的蛋白酪氨酸磷酸酶（SHP-1/PTPN6和SHP-2/PTPN11，STRING评分=982/807），磷酸酶随后去磷酸化下游激活信号分子（如CLEC1B和GP6/FcRγ复合体的ITAM基序），从而抑制血小板聚集和激活。这种"ITIM-ITAM拮抗"机制是免疫平衡维持的核心策略。

HPA Approved的多重定位（Cytosol; Endoplasmic reticulum; Golgi apparatus; Nucleoplasm; Plasma membrane）揭示了一个引人入胜的非经典运输/信号传导路径。MPIG6B可能在内质网中合成和折叠，经高尔基体成熟后运输至血小板质膜。核质定位则可能是：（1）内质网-核膜连续性导致的核膜被动定位；（2）ITIM基序被磷酸化后触发的内吞-内体逃逸-核转位信号级联——类似于EGFR或IFNAR的核转位机制。

MPIG6B在血小板生成（thrombopoiesis）中的关键角色通过人类遗传学研究得到有力支持：MPIG6B基因突变导致先天性血小板减少伴骨髓纤维化（PMID:35940081、PMID:41838173）。G6b-B调控巨核细胞成熟的一个必需步骤（PMID:35134123），其缺失导致巨核细胞分泌促纤维化因子增多，引发骨髓微环境纤维化重塑。特别值得注意的是，MPIG6B缺陷巨核细胞呈现炎性特征（PMID:40643151），提示该受体在抑制固有免疫信号中具有扩展功能——可能通过阻断TLR或炎症小体信号的异常激活。从TE调控角度，免疫受体在核质中的定位极其罕见，MPIG6B可能代表了"非经典核ITIM信号"的新类别——值得通过磷酸化蛋白质组学解析核内ITIM信号网络。

**蛋白全称**: Megakaryocyte and platelet inhibitory receptor G6b

**功能**: Inhibitory receptor that acts as a critical regulator of hematopoietic lineage differentiation, megakaryocyte function and platelet production (PubMed:12665801, PubMed:17311996, PubMed:27743390). Inhibits platelet aggregation and activation by agonists such as ADP and collagen-related peptide (PubMed:12665801). This regulation of megakaryocate function as well as platelet production ann activation is done through the inhibition (via the 2 ITIM motifs) of the receptors CLEC1B and GP6:FcRgamma sig

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR028070 |
| InterPro | IPR048308 |
| Pfam | PF15096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PTPN11 | STRING | 982 |
| PTPN6 | STRING | 807 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O95866-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000204420-MPIG6B

![](https://images.proteinatlas.org/54404/1877_D8_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1877_D8_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1707_D2_8_cr57ea950249c33_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1707_D2_28_cr57ea950a35917_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1737_E3_7_cr58063fd449d7f_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1737_E3_23_cr58063fdd8f3ee_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000204420-MPIG6B

![](https://images.proteinatlas.org/54404/1877_D8_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1877_D8_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1707_D2_8_cr57ea950249c33_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1707_D2_28_cr57ea950a35917_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1737_E3_7_cr58063fd449d7f_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1737_E3_23_cr58063fdd8f3ee_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000204420-MPIG6B

![](https://images.proteinatlas.org/54404/1877_D8_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1877_D8_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1707_D2_8_cr57ea950249c33_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1707_D2_28_cr57ea950a35917_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1737_E3_7_cr58063fd449d7f_blue_red_green.jpg)
![](https://images.proteinatlas.org/54404/1737_E3_23_cr58063fdd8f3ee_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 35**

| 41838173 | MPIG6B-related thrombocytopenia and myelofibrosis: A case report. | Ann Hematol 2026 |
| 40643151 | Thrombocytopenia in myelofibrosis is characterized by inflammatory megakaryocytes with reduced G6B expression. | Blood 2025 |
| 39979109 | [MPIG6B gene variation causing thrombocytopenia with myelofibrosis in a child]. | Zhonghua Er Ke Za Zhi 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MPIG6B

