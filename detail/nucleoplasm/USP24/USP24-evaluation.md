---
type: protein-evaluation
gene: "USP24"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## USP24 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | USP24 |
| 蛋白名称 | Ubiquitin carboxyl-terminal hydrolase 24 |
| 蛋白大小 | 2620 aa / 294.4 kDa |
| UniProt ID | Q9UPU5 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm (Supported) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 2620 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=44 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=75.1; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | ARM-type_fold; ARM_UBP34_24_USP9X_Y; Papain-like_cys_pep_sf |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=111 |
| **加权总分** | | | **125/180** | |
| **归一化总分** | | | **69.4/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Supported)
- PubMed strict=44 broad=67
- AF pLDDT=75.1 PDB=0
- InterPro: ARM-type_fold; ARM_UBP34_24_USP9X_Y; Papain-like_cys_pep_sf
- Pfam: ARM_UBP24_USP9X-Y; UCH; UCH_UBL1
- PPI degree=111 ChIP: None
40238877: Deubiquitinase USP24 activated by IL-6/STAT3 enhances PD-1 protein stability and | 30957634: The PARK10 gene USP24 is a negative regulator of autophagy and ULK1 protein stab | 40448065: USP24 upregulation stabilizes PKA-Cα to promote lipogenesis, inflammation, and f

### 4. 总体评价
**69.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ubiquitin carboxyl-terminal hydrolase 24

**功能**: Ubiquitin-specific protease that regulates cell survival in various contexts through modulating the protein stability of some of its substrates including DDB2, MCL1 or TP53. Plays a positive role on ferritinophagy where ferritin is degraded in lysosomes and releases free iron

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR016024 |
| InterPro | IPR056850 |
| InterPro | IPR038765 |
| InterPro | IPR050164 |
| InterPro | IPR001394 |
| InterPro | IPR015940 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

USP24（Ubiquitin carboxyl-terminal hydrolase 24，UniProt: Q9UPU5，2620 aa / 294.4 kDa）的结构域架构分析显示：InterPro结构域包括IPR001394, IPR015940, IPR016024, IPR038765, IPR050164, IPR056850。 AlphaFold预测的pLDDT均值为75.1，整体结构置信度中等，部分区域可能为内在无序区，需要注意其构象柔性对功能的影响。

蛋白质互作网络分析揭示USP24与以下关键因子存在相互作用：DDB2、HIVEP3、KBP-1、ELAVL4、TP53（PPI度为111）。 功能注释显示Ubiquitin-specific protease that regulates cell survival in various contexts through modulating the protein stability of some of its substrates including DDB2, MCL1 or TP53. Plays a positive role on f。 这些互作伙伴暗示该蛋白可能通过多蛋白复合物参与细胞过程调控，其互作网络的拓扑位置值得进一步实验验证。

从结构-功能机制角度分析，USP24的亚细胞定位为，具有明确的核/核周定位特征，提示其可能直接参与染色质水平或核内体的调控过程。 评估综合得分69.4/100，属于中等兴趣候选，在明确核定位后其TE调控潜力可能显著提升。

对于TE调控机制的意义而言，USP24的结构域组成不直接指向经典染色质调控因子，但其在核内的存在（若经实验确认）可能暗示非经典TE调控途径。 研究新颖性方面，PubMed检索获得44篇文献，有一定研究基础但远未饱和，可从TE调控新角度切入。 代表性文献包括PMID:42321163, 42233473, 42218160等。

综上所述，USP24作为一个2620 aa / 294.4 kDa的定位蛋白，具有一定的TE调控研究价值，建议首先通过亚细胞分级和免疫荧光明确其在核内的分布模式，再设计针对性的功能实验。 AlphaFold pLDDT=75.1的结构预测可作为设计突变体和结构-功能关系研究的起点。


---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DDB2 | STRING | 986 |
| HIVEP3 | STRING | 800 |
| KBP-1 | STRING | 800 |
| ELAVL4 | STRING | 790 |
| TP53 | STRING | 709 |
| ARRB1 | BioGRID | 1 |
| SIRT7 | BioGRID | 1 |
| CSNK2A1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UPU5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162402-USP24

![](https://images.proteinatlas.org/26723/259_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/26723/259_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/26723/258_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/26723/258_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/26723/260_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/26723/260_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/28428/511_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/28428/511_B9_2_red_green.jpg)

### PubMed 文献

**PubMed count: 67**

| 42321163 | USP24 is a cross-reactive DUB targeting MOV10 to regulate IFN-I production. | Nat Commun 2026 |
| 42233473 | Sevoflurane pre-treatment attenuates myocardial cell ferroptosis caused by hypoxia and reoxygenation via regulating lncR | Toxicol Mech Methods 2026 |
| 42218160 | USP24-dependent STAT2 stabilization mediates physiologic and pathologic bone formation. | Cell Death Dis 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/USP24

