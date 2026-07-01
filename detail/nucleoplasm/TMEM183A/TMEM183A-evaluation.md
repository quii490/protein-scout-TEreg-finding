---
type: protein-evaluation
gene: "TMEM183A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM183A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM183A |
| 蛋白名称 | Transmembrane protein 183A |
| 蛋白大小 | 376 aa / 42.8 kDa |
| UniProt ID | Q8IXX5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cell Junctions; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 376 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=72.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | F-box-like_dom_sf; TMEM183 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=27 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +1 |

### 3. 分析
- Cell Junctions; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=5 broad=8
- AF pLDDT=72.6 PDB=0
- InterPro: F-box-like_dom_sf; TMEM183
- Pfam: TMEM183_C
- PPI degree=27 ChIP: None
35202345: Multiplexed Genome Editing for Efficient Phenotypic Screening in Zebrafish. | 41027479: Knockdown of tmem183a in Zebrafish Causes Thrombocytopenia and Reduces Coagulati | 39491753: Transcriptomic imputation identifies tissue-specific genes associated with cervi

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 183A

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036047 |
| InterPro | IPR026509 |
| Pfam | PF27923 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 0 |
| IFIT3 | BioGRID | 0 |
| SYP | BioGRID | 0 |
| ACTN3 | BioGRID | 0 |
| LRRC55 | BioGRID | 0 |
| PIPSL | BioGRID | 0 |
| KLRD1 | BioGRID | 0 |
| HCST | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8IXX5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000163444-TMEM183A

![](https://images.proteinatlas.org/72607/1412_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/72607/1412_E11_4_red_green.jpg)
![](https://images.proteinatlas.org/72607/1492_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/72607/1492_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/72607/1409_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/72607/1409_E11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 8**

| 41027479 | Knockdown of tmem183a in Zebrafish Causes Thrombocytopenia and Reduces Coagulation Factors, Disrupting Hemostasis. | Thromb Haemost 2025 |
| 39491753 | Transcriptomic imputation identifies tissue-specific genes associated with cervical myelopathy. | Spine J 2025 |
| 35202345 | Multiplexed Genome Editing for Efficient Phenotypic Screening in Zebrafish. | Vet Sci 2022 |

### 深度机制分析

TMEM183A的域架构将C端跨膜结构域与N端胞质区域结合在一起，后者折叠为F-box样结构域超家族（F-box-like_dom_sf, IPR036047）。F-box结构域是约40个残基的基序，首先在作为SCF（Skp1-Cullin1-F-box）E3泛素连接酶复合物底物受体亚基的蛋白质中发现。TMEM183家族标志（IPR026509）与F-box样折叠（Pfam PF27923, TMEM183_C）的配对暗示其具有模块化架构，将底物识别（F-box样）与膜定位（跨膜螺旋）结合起来。

结构信息中等（AlphaFold pLDDT=72.6），F-box样结构域的置信度较高，跨膜螺旋和连接区域的置信度较低。无任何实验结构。PPI网络（degree=27）包括APP（淀粉样蛋白前体蛋白）、IFIT3（干扰素诱导的TPR蛋白3，参与抗病毒天然免疫）、SYP（突触素）和ACTN3（α-辅肌动蛋白-3）。IFIT3的关联具有潜在重要性——IFIT家族蛋白严格依赖干扰素，直接结合病毒RNA和外源核酸以抑制翻译。TMEM183A与IFIT3的互作提示其可能在检测胞质核酸中发挥作用。

核质和细胞连接的定位，加之斑马鱼研究中消耗TMEM183A导致血小板减少症及凝血因子减少的发现（PMID 41027479），共同描绘出复杂的功能画面。血小板生成受巨核细胞成熟调控，其中许多步骤涉及核因子（如GATA1、NF-E2、RUNX1）。核质TMEM183A可能通过其F-box样结构域靶向细胞特定转录因子以进行泛素化及降解，从而对巨核细胞分化起到定时作用。

TE调控推测聚焦于IFIT3的连接。干扰素诱导的IFIT蛋白是限制非自我核酸（包括内源性逆转录病毒RNA）的关键屏障。若TMEM183A的F-box样结构域能通过泛素化调控IFIT3蛋白稳定性，则该蛋白可作为调节先天免疫系统内TE检测阈值的变阻器。斑马鱼血细胞减少症表型与TE激活诱导的造血干细胞耗竭在表型上存在一致性，为深入研究TE监控机制在血细胞系稳态中的作用打开了方向。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM183A

