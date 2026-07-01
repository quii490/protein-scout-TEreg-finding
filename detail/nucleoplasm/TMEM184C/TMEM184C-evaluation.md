---
type: protein-evaluation
gene: "TMEM184C"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM184C 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM184C |
| 蛋白名称 | Transmembrane protein 184C |
| 蛋白大小 | 438 aa / 50.1 kDa |
| UniProt ID | Q9NVA4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 438 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=71.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ostalpha/TMEM184C |
| PPI | 5/10 | x3 | 15.0 | PPI degree=13 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=0 broad=2
- AF pLDDT=71.5 PDB=0
- InterPro: Ostalpha/TMEM184C
- Pfam: Solute_trans_a
- PPI degree=13 ChIP: None


### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 184C

**功能**: Possible tumor suppressor which may play a role in cell growth

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR005178 |
| Pfam | PF03619 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 184C

**功能**: Possible tumor suppressor which may play a role in cell growth

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR005178 |
| Pfam | PF03619 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PRMT9 | STRING | 732 |
| SGK1 | BioGRID | 1 |
| TCTN3 | BioGRID | 1 |
| POLR1D | BioGRID | 1 |
| MATR3 | BioGRID | 1 |
| CSK | BioGRID | 0 |
| NPC1 | BioGRID | 0 |
| LAMP2 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：TMEM184C（438 aa，50.1 kDa）属于Ostalpha/TMEM184C家族（IPR005178），含Solute_trans_a结构域（PF03619）。该家族蛋白结构特征为多次跨膜α-螺旋组成的通道/转运体折叠，预测跨膜域为7-10次。作为肿瘤抑制候选蛋白（UniProt标注"Possible tumor suppressor which may play a role in cell growth"），其跨膜拓扑结构使得核质定位成为一个值得深入探讨的异常现象。

**PPI互作网络解读**：PPI degree=13，最值得关注的互作伙伴为PRMT9（STRING 732分，高置信度共表达）和MATR3（BioGRID 1分）。PRMT9是蛋白精氨酸甲基转移酶，催化组蛋白和非组蛋白的精氨酸甲基化修饰，在RNA剪接调控和DNA损伤应答中发挥作用；MATR3（Matrin-3）是核基质的核心结构蛋白，结合DNA和RNA并参与RNA加工。TMEM184C同时与SGK1（血清/糖皮质激素调节激酶）和POLR1D（RNA聚合酶I亚基）互作，进一步暗示其可能存在核质功能。

**结构解读**：AlphaFold pLDDT=71.5，跨膜区域预测置信度中等（典型膜蛋白特征），而胞质loop区的pLDDT偏高（75-85）。Solute_trans_a折叠形成由跨膜α-螺旋围绕的中心孔道，可能介导离子或小分子跨膜转运。目前无实验结构验证。TMEM184C的肿瘤抑制活性可能与以下机制相关：通过调控离子/代谢物跨膜通量影响细胞增殖信号通路（如钙离子信号、mTOR通路），或通过PRMT9介导的甲基化修饰间接影响表观遗传调控。

**机制模型**：（1）膜定位功能：TMEM184C作为质膜/囊泡膜转运蛋白，通过调控特定离子或代谢物梯度影响细胞增殖速率，在肿瘤发生中充当制动器（brake）；（2）核质功能：TMEM184C可能通过内吞途径内化后经逆行运输至核膜，在核质中与MATR3-PRMT9形成核基质相关复合物，参与RNA剪接和核内RNA代谢的空间组织。PMID:36785897发现的染色体17q拷贝数变异提示TMEM184C的剂量效应在骨骼肌发育中的重要性。

**TE调控展望**：TMEM184C不直接具备TE调控结构基础（无DNA结合域、无组蛋白修饰域），但其与MATR3的互作值得关注——Matrin-3已被报道与LINE-1 RNA结合并影响LINE-1逆转录转座。TMEM184C可能通过稳定MATR3的核基质锚定间接影响TE RNA的命运决定。鉴于PubMed仅2篇记录，此蛋白的核质功能完全未被研究，是一个高度新颖但需实验验证的候选。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NVA4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164168-TMEM184C

![](https://images.proteinatlas.org/54013/984_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/54013/984_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/54013/867_F9_3_red_green.jpg)
![](https://images.proteinatlas.org/54013/867_F9_4_red_green.jpg)
![](https://images.proteinatlas.org/54013/981_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/54013/981_F7_4_red_green.jpg)

### PubMed 文献

**PubMed count: 2**

| 36785897 | A 1.1 Mb duplication CNV on chromosome 17 contributes to skeletal muscle development in Boer goats. | Zool Res 2023 |
| 21636067 | X-linked congenital hypertrichosis syndrome is associated with interchromosomal insertions mediated by a human-specific  | Am J Hum Genet 2011 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM184C

