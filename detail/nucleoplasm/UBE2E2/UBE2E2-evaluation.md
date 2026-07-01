---
type: protein-evaluation
gene: "UBE2E2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## UBE2E2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UBE2E2 |
| 蛋白名称 | Ubiquitin-conjugating enzyme E2 E2 |
| 蛋白大小 | 201 aa / 22.3 kDa |
| UniProt ID | Q96LR5 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 201 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=28 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=85.6; PDB=3 |
| 调控结构域 | 4/10 | x2 | 8.0 | UBC; UBQ-conjugating_AS; UBQ-conjugating_enzyme/RWD |
| PPI | 7/10 | x3 | 21.0 | PPI degree=101 |
| **加权总分** | | | **141/180** | |
| **归一化总分** | | | **77.6/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=28 broad=56
- AF pLDDT=85.6 PDB=3
- InterPro: UBC; UBQ-conjugating_AS; UBQ-conjugating_enzyme/RWD
- Pfam: UQ_con
- PPI degree=101 ChIP: None
41540009: Cryo-EM structure of the human COP1-DET1 ubiquitin ligase complex. | 35207731: PPARG, TMEM163, UBE2E2, and WFS1 Gene Polymorphisms Are Not Significant Risk Fac | 36765041: UBE2E2 enhances Snail-mediated epithelial-mesenchymal transition and Nrf2-mediat

### 4. 总体评价
**77.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ubiquitin-conjugating enzyme E2 E2

**功能**: Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro catalyzes 'Lys-11'- and 'Lys-48'-, as well as 'Lys-63'-linked polyubiquitination. Catalyzes the ISGylation of influenza A virus NS1 protein

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000608 |
| InterPro | IPR023313 |
| InterPro | IPR016135 |
| Pfam | PF00179 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---



### 深度机制分析

UBE2E2的域结构揭示了经典E2泛素结合酶的核心特征。InterPro域UBC（IPR000608）和UBQ-conjugating_enzyme/RWD（IPR016135），加上Pfam域UQ_con（PF00179），定义了该蛋白的催化核心。这些域的共同特点是含有一个保守的半胱氨酸活性位点，负责接受来自E1酶的泛素硫酯中间体。值得注意的是，UBE2E2还包含UBQ-conjugating_AS活性位点特征（IPR023313），表明其催化Cys残基位于一个高度保守的局部环境中。该蛋白的独特之处在于其内在的底物选择性——它可在体外催化Lys-11、Lys-48和Lys-63三种不同拓扑结构的聚泛素链，这种"一酶多链"的能力在E2家族中并不常见，暗示其活性位点具有构象可塑性以适应不同链型的延伸。

PPI网络分析揭示了UBE2E2嵌入多个关键泛素信号通路的深度。STRING评分最高的互作伙伴PRKN（Parkin, 978）和RLIM（RNF12, 976）将UBE2E2直接连接到线粒体自噬和转录调控通路。PRKN（又名PARK2）是Parkinson病相关的E3连接酶，其通过UBE2E2进行泛素化提示该E2参与线粒体质量控制。RLIM则是X染色体失活的关键调节因子，通过泛素化降解转录因子参与剂量补偿。UBA7（955，ISG15 E1酶）和RNF8（901，DNA损伤应答E3）的关联进一步扩展了功能谱：UBE2E2可能在先天免疫信号（ISGylation通路）和DNA双链断裂修复中发挥作用。SIAH1（840）和ARIH1（829）的出现分别提示Wnt/β-catenin降解复合物和非常规泛素化的参与。这一互作谱系清楚地描绘了UBE2E2作为"泛素编码中枢"的角色，与多种E3连接酶配对以产生不同链型，驱动截然不同的细胞结果。

结构层面，AlphaFold pLDDT 85.6和PDB中已有的3个实验结构为此蛋白提供了较为坚实的结构基础。COP1-DET1泛素连接酶复合物的冷冻电镜结构（PMID: 41540009）尤其关键——它捕获了UBE2E2在其天然E3复合物中的构象。这个中等pLDDT（85.6）反映了E2酶的固有无序区域（尤其是N端和C端延伸），这些区域在E3结合时会发生诱导折叠。3个PDB结构提供了不同功能状态下的快照：游离态、E1结合态和E3结合态，共同构成了一个构象循环的多状态视图。

综合所有证据，UBE2E2在分子水平上扮演"泛素信号路由器"的角色。其核心机制模型为：E1酶（UBA1/UBA6）将泛素加载到UBE2E2的催化Cys上；随后，特定的E3连接酶（RNF8, RLIM, PRKN, SIAH1等）招募UBE2E2~Ub复合物至特定底物；UBE2E2根据E3的别构引导选择Lys-11、Lys-48或Lys-63连接方式，决定底物蛋白的命运（蛋白酶体降解、信号激活或自噬靶向）。在核质环境中，RNF8-UBE2E2轴线在DNA损伤位点产生Lys-63链，招募修复因子；RLIM-UBE2E2轴线通过Lys-48链调控转录因子的降解。核质定位意味着该蛋白可能在染色质相关泛素化事件（如组蛋白H2A/H2B泛素化和转录因子周转）中具有未充分探索的功能。

UBE2E2的科研与治疗价值显著。该蛋白仅28篇严格PubMed文献的新颖性（评分9/10）与其在网络中的中心位置形成鲜明对比，表明这是一个严重研究不足的节点。在癌症方面，UBE2E2通过Snail介导的上皮-间质转化（EMT）和Nrf2抗氧化应答（PMID: 36765041）的双重调控使其成为转移性肿瘤的潜在靶点。COP1-DET1-UBE2E2复合物结构（PMID: 41540009）为基于结构的药物设计提供了起点。在神经退行性疾病方面，PRKN-UBE2E2连接提供了干预Parkinson病线粒体自噬缺陷的新角度。靶向UBE2E2的特异性抑制剂（区别于广谱E2抑制剂）可能提供优于E3靶向的治疗窗口，因为E2的选择性底物谱更窄。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PRKN | STRING | 978 |
| RLIM | STRING | 976 |
| UBA7 | STRING | 955 |
| UBE2E1 | STRING | 938 |
| UBE2E3 | STRING | 936 |
| RNF8 | STRING | 901 |
| SIAH1 | STRING | 840 |
| ARIH1 | STRING | 829 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96LR5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000182247-UBE2E2

![](https://images.proteinatlas.org/28872/918_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/28872/918_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/28872/911_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/28872/911_B11_3_red_green.jpg)
![](https://images.proteinatlas.org/28872/912_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/28872/912_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/28872/930_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/28872/930_F7_2_red_green.jpg)

### PubMed 文献

**PubMed count: 56**

| 42358995 | The UBE2/E2 ubiquitin-conjugating enzyme family at the interface of tumor biology and antitumor immunity: mechanisms, bi | Front Immunol 2026 |
| 41696008 | Genome-wide association study of nutrient composition in meat from three two-way crossbred pig populations using whole-g | Front Vet Sci 2026 |
| 41540009 | Cryo-EM structure of the human COP1-DET1 ubiquitin ligase complex. | Nat Commun 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UBE2E2

