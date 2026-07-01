---
type: protein-evaluation
gene: "PCDHGB3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGB3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGB3 |
| 蛋白名称 | Protocadherin gamma-B3 |
| 蛋白大小 | 929 aa / 101.2 kDa |
| UniProt ID | Q9Y5G1 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 929 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=1 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=75.4; PDB=3 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 5/10 | x3 | 15.0 | PPI degree=8 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=1 broad=2
- AF pLDDT=75.4 PDB=3
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_C
- Pfam: Cadherin; Cadherin_2; Cadherin_C_2
- PPI degree=8 ChIP: None
39380273: Identification of an immune cell infiltration-related gene signature for prognos

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**1. 结构域架构与分子功能推断**

PCDHGB3含有6个钙黏蛋白重复结构域（IPR002126 Cadherin-like_dom, IPR020894 Cadherin-like），以及C端胞质结构域（IPR032455 Cadherin_C）。钙黏蛋白超家族（IPR015919 Cadherin-like_sf）的典型功能是钙依赖性同嗜性细胞黏附，其胞外区通过反式二聚化介导细胞间连接。929 aa的大分子量（101.2 kDa）表明其胞外区由多个钙黏蛋白重复单元串联排列，形成延伸的刚性杆状结构。值得注意的是，Pfam还注释到Cadherin_2（非典型钙黏蛋白重复）和Cadherin_C_2（非典型胞质尾），这暗示PCDHGB3可能不是经典I型钙黏蛋白，而属于其特有的非典型信号传导亚类。IPR031904（Protocadherin胞质域）的存在进一步确认其属于原钙黏蛋白γ簇——该簇蛋白的胞质尾与经典钙黏蛋白不同，不具备β-catenin结合基序，提示其具有独特的胞内信号通路而非经典黏附连接功能。

**2. PPI互作网络与通路分析**

PPI网络（degree=8）的核心特征是同簇内广泛互作：PCDHGB3与PCDHGC3、PCDHGB1、PCDHGB4、PCDHGB2、PCDHGB5均存在BioGRID报道的互作，这与原钙黏蛋白γ簇的顺式四聚化组装模型一致——同簇异构体在顺式膜平面内形成多聚体复合物，从而扩大细胞表面黏附编码的多样性。最具机制价值的是RNF123（E3泛素连接酶）和HIST1H2BD（组蛋白H2B）两个互作伙伴。RNF123（KPC1）是Kip1泛素化促进复合体的催化亚基，介导p27^Kip1的泛素化降解，参与细胞周期G1/S转换调控；PCDHGB3与RNF123的互作提示原钙黏蛋白可能通过E3连接酶衔接调控细胞周期。HIST1H2BD的互作则强烈暗示PCDHGB3可能在核质中与染色质发生直接或间接接触——考虑到原钙黏蛋白γ簇的胞质尾含有一个保守的PXXP基序可结合含SH3结构域的核质穿梭蛋白，这一核内功能假说值得深入验证。

**3. 结构生物学解析**

AlphaFold预测的pLDDT值为75.4，属于中高置信度。钙黏蛋白重复结构域通常折叠良好（pLDDT>80），但胞质尾区域（最后约100 aa）和重复单元之间的连接环可能是低置信度区（pLDDT<70），拉低了整体平均值。PDB数据库中有3个相关结构条目，参考同簇蛋白PCDHγB4的晶体结构（Elife 2016, PMID:27472898），胞外钙黏蛋白重复1-4形成反式平行的同源二聚体界面，其中重复1-2负责亲和力，重复3-4负责特异性编码。这种"亲和力-特异性"双模块机制使得PCDHGB3能以有限的基因数量产生指数级的细胞表面身份编码——这是神经元自我回避（self-avoidance）和突触特异性建立的分子基础。PAE图预期显示胞外区内部残基间的对齐误差较低（<5Å），而胞质尾与胞外区之间的相对取向则可能高度可变，这与该蛋白作为膜锚定受体的构象灵活性需求一致。

**4. 整合机制模型**

综合所有证据，PCDHGB3在分子水平上是一个双功能蛋白：（1）在质膜上，作为原钙黏蛋白γ-B3亚型，通过胞外钙黏蛋白重复的反式二聚化，与同簇其他异构体（PCDHGB1-5）形成顺式多聚体，参与神经元表面身份编码和突触特异性识别；（2）在核质中，其胞质尾可能通过RNF123介导的泛素化信号或HIST1H2BD相关的染色质锚定，发挥非经典的核内信号传导功能。核定位与该蛋白在HPA中"Vesicles"的定位注释共同提示，PCDHGB3可能经历受调控的膜内蛋白水解（RIP），其胞内域被剪切后通过囊泡运输进入核质。这一模型将细胞黏附与转录调控偶联，类似于Notch和CADH1/E-cadherin的已知机制。

**5. 研究与转化意义**

PCDHGB3的PubMed文献仅2篇（strict count），研究与新颖性得分10/10，是极佳的探索靶点。PMID:39380273在TNBC中鉴定的免疫浸润基因标签包含PCDHGB3，提示其在肿瘤微环境中的潜在角色。鉴于RNF123-p27轴在细胞周期调控中的核心地位，PCDHGB3-RNF123互作可能为三阴性乳腺癌的CDK4/6抑制剂耐药提供了新的机制解释。此外，原钙黏蛋白γ簇的神经元特异性表达模式使其成为神经发育疾病（如自闭症谱系障碍和Rett综合征）中突触连接异常的功能候选基因。建议优先验证PCDHGB3的核内切割产物是否存在，以及该切割是否受钙离子浓度或Wnt信号调控。


### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin gamma-B3

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
| PCDHGC3 | BioGRID | 0 |
| PCDHGB1 | BioGRID | 0 |
| PCDHGB4 | BioGRID | 0 |
| RNF123 | BioGRID | 0 |
| PCDHGB2 | BioGRID | 0 |
| PCDHGB5 | BioGRID | 0 |
| HIST1H2BD | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5G1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000262209-PCDHGB3

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/35822/1331_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/35822/1331_B4_7_red_green.jpg)

### PubMed 文献

**PubMed count: 2**

| 39380273 | Identification of an immune cell infiltration-related gene signature for prognosis prediction in triple-negative breast  | Cell Mol Biol (Noisy-le-grand) 2024 |
| 27472898 | Antiparallel protocadherin homodimers use distinct affinity- and specificity-mediating regions in cadherin repeats 1-4. | Elife 2016 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGB3

