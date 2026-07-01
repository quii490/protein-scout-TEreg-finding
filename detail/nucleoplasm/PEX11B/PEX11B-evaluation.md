---
type: protein-evaluation
gene: "PEX11B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PEX11B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PEX11B |
| 蛋白名称 | Peroxisomal membrane protein 11B |
| 蛋白大小 | 259 aa / 28.4 kDa |
| UniProt ID | O96011 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 259 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=29 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=88.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | PEX11 |
| PPI | 6/10 | x3 | 18.0 | PPI degree=52 |
| **加权总分** | | | **135/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=29 broad=67
- AF pLDDT=88.8 PDB=0
- InterPro: PEX11
- Pfam: PEX11
- PPI degree=52 ChIP: None
20301621: Zellweger Spectrum Disorder. | 23821150: Peroxisomes and photomorphogenesis. | 40689797: Protein Kinase C promotes peroxisome biogenesis and peroxisome-endoplasmic retic

### 4. 总体评价
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Peroxisomal membrane protein 11B

**功能**: Involved in peroxisomal proliferation (PubMed:9792670). May regulate peroxisome division by recruiting the dynamin-related GTPase DNM1L to the peroxisomal membrane (PubMed:12618434). Promotes membrane protrusion and elongation on the peroxisomal surface (PubMed:20826455)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR008733 |
| Pfam | PF05648 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

PEX11B（Peroxisomal membrane protein 11B）是过氧化物酶体增殖的关键调控因子，其InterPro结构域PEX11（IPR008733）和Pfam结构域PEX11（PF05648）定义了该蛋白的核心功能区域。259个氨基酸（28.4 kDa）的相对较小分子量使其成为PEX11家族中最紧凑的成员之一。AlphaFold预测的pLDDT高达88.8，表明该蛋白具有高度有序的三维折叠，这是功能蛋白的有利特征。然而，HPA免疫荧光定位显示Nucleoplasm; Vesicles (Approved)——核质的定位结果与该蛋白经典的过氧化物酶体膜定位存在显著偏差，这一"错位"可能揭示其尚未被认识的非经典功能。

PPI互作网络分析揭示了PEX11B在过氧化物酶体生物发生中的核心地位。STRING数据库显示PEX2（967）和PEX14（921）是最高置信度的互作伙伴，两者均为过氧化物酶体基质蛋白导入系统的关键组分。ACBD5（802）的互作则连接了过氧化物酶体与内质网（ER）的膜接触位点。BioGRID数据补充了HTT（亨廷顿蛋白）、RNF4（SUMO E3泛素连接酶）和CRELD1等额外互作因子。这一互作模式与PEX11B的功能注释高度一致：通过招募dynamin相关GTPase DNM1L到过氧化物酶体膜上促进过氧化物酶体分裂（PMID 12618434），并通过促进膜突起和延伸来调控过氧化物酶体增殖（PMID 20826455）。

从结构-功能关系角度，PEX11B的核质定位可能与过氧化物酶体-细胞核信号通讯有关。过氧化物酶体是脂质代谢和活性氧（ROS）稳态的关键细胞器，其功能状态需要反馈至细胞核以调控相关基因表达。PPARα是过氧化物酶体增殖物激活受体，在核内调控脂质代谢基因——PEX11B的核质定位可能参与这一反馈回路。此外，近期的研究揭示了PEX11B棕榈酰化修饰在糖尿病神经病变中的作用（PMID 39934809, J Biomed Sci, 2025），以及蛋白激酶C促进过氧化物酶体-ER相互作用的机制（PMID 40689797, J Cell Biol, 2025），提示翻译后修饰可能动态调控PEX11B的亚细胞定位。

PEX11B的PubMed strict=29篇文献表明研究覆盖度适中，但缺乏结构生物学数据（PDB=0）。未来研究应聚焦于：（1）利用冷冻电镜或X射线晶体学解析PEX11B的完整三维结构；（2）通过活细胞成像验证PEX11B的核质穿梭动力学；（3）鉴定介导其核定位的分子决定因素；（4）探索PEX11B在核内是否参与过氧化物酶体功能相关基因的转录调控。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PEX2 | STRING | 967 |
| PEX14 | STRING | 921 |
| ACBD5 | STRING | 802 |
| PEX11B | BioGRID | 1 |
| HTT | BioGRID | 1 |
| RNF4 | BioGRID | 1 |
| CRELD1 | BioGRID | 1 |
| SAAL1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O96011-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000131779-PEX11B

![](https://images.proteinatlas.org/17150/1871_G11_20_cr5b717efb73676_blue_red_green.jpg)
![](https://images.proteinatlas.org/17150/1871_G11_21_cr5b4882c63994d_blue_red_green.jpg)
![](https://images.proteinatlas.org/17150/1913_I13_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17150/1913_I13_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000131779-PEX11B

![](https://images.proteinatlas.org/17150/1871_G11_20_cr5b717efb73676_blue_red_green.jpg)
![](https://images.proteinatlas.org/17150/1871_G11_21_cr5b4882c63994d_blue_red_green.jpg)
![](https://images.proteinatlas.org/17150/1913_I13_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17150/1913_I13_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000131779-PEX11B

![](https://images.proteinatlas.org/17150/1871_G11_20_cr5b717efb73676_blue_red_green.jpg)
![](https://images.proteinatlas.org/17150/1871_G11_21_cr5b4882c63994d_blue_red_green.jpg)
![](https://images.proteinatlas.org/17150/1913_I13_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17150/1913_I13_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 67**

| 42118293 | Peroxisome calcium uptake is dependent on ER-peroxisome membrane contact. | Cell Mol Life Sci 2026 |
| 40689797 | Protein Kinase C promotes peroxisome biogenesis and peroxisome-endoplasmic reticulum interaction. | J Cell Biol 2025 |
| 39934809 | PEX11B palmitoylation couples peroxisomal dysfunction with Schwann cells fail in diabetic neuropathy. | J Biomed Sci 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PEX11B

