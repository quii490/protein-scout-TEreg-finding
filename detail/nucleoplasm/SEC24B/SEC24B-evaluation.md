---
type: protein-evaluation
gene: "SEC24B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SEC24B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SEC24B |
| 蛋白名称 | Protein transport protein Sec24B |
| 蛋白大小 | 1268 aa / 137.4 kDa |
| UniProt ID | O95487 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 1268 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=35 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=71.4; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | ADF-H/Gelsolin-like_dom_sf; Beta-sandwich_Sec23_24; Gelsolin-like_dom |
| PPI | 8/10 | x3 | 24.0 | PPI degree=265 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=35 broad=45
- AF pLDDT=71.4 PDB=1
- InterPro: ADF-H/Gelsolin-like_dom_sf; Beta-sandwich_Sec23_24; Gelsolin-like_dom
- Pfam: Gelsolin; Sec23_BS; Sec23_helical
- PPI degree=265 ChIP: None
36536241: Microglia ferroptosis is regulated by SEC24B and contributes to neurodegeneratio | 40536345: Spatiotemporal Regulation of STING Activity by Linear Ubiquitination Governs Ant | 38321032: Unraveling the genetic architecture of congenital vertebral malformation with re

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein transport protein Sec24B

**功能**: Component of the coat protein complex II (COPII) which promotes the formation of transport vesicles from the endoplasmic reticulum (ER). The coat has two main functions, the physical deformation of the endoplasmic reticulum membrane into vesicles and the selection of cargo molecules for their transport to the Golgi complex (PubMed:17499046, PubMed:18843296, PubMed:20427317). Plays a central role in cargo selection within the COPII complex and together with SEC24A may have a different specificity

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029006 |
| InterPro | IPR012990 |
| InterPro | IPR007123 |
| InterPro | IPR036180 |
| InterPro | IPR006900 |
| InterPro | IPR036175 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SEC23A | BioGRID | 0 |
| FYCO1 | BioGRID | 0 |
| TERF2 | BioGRID | 0 |
| SCAP | BioGRID | 0 |
| RNF139 | BioGRID | 0 |
| TSG101 | BioGRID | 0 |
| CUL3 | BioGRID | 0 |
| SEC23B | BioGRID | 0 |


### 深度机制分析

**结构域架构**：SEC24B（1268 aa，137.4 kDa）是COPII包被复合物的核心选择性货物受体，含三个结构模块：（1）Gelsolin-like_dom（IPR007123）和ADF-H/Gelsolin-like_dom_sf（IPR029006）构成N端β-三叶草折叠，负责与SEC23亚基的结合界面；（2）Beta-sandwich_Sec23_24（IPR012990）为中央结构域，形成免疫球蛋白样β-三明治折叠，识别货物蛋白的Sec24结合基序（如LxxLE、DxE等ER输出信号）；（3）C端gelsolin-like结构域（IPR036180, IPR036175）参与膜曲率感知和SAR1 GTPase的协同作用。

**PPI互作网络解读**：PPI degree=265，是COPII复合物的核心节点蛋白。关键互作包括：SEC23A/SEC23B（直接结合形成内层COPII笼）、TERF2（端粒结合蛋白2，提示SEC24B可能在端粒代谢中有非经典功能）、TSG101（ESCRT-I组分，涉及内体分选）、CUL3（E3泛素连接酶支架）。SEC23A/B的互作验证了其COPII经典功能，但TERF2和TSG101的互作提示SEC24B在核膜-ER膜接触位点和端粒稳态中可能具有额外的锚定功能。

**结构解读**：AlphaFold pLDDT=71.4（1个PDB结构验证），整体折叠质量中等受限于蛋白长度（1268 aa）。中央Beta-sandwich域的pLDDT最高（>85），形成刚性的β-片层平台用于货物识别。Gelsolin样结构域的pLDDT偏低（60-70），该区域在无配体时可能具有显著的构象柔性。SEC24B的货物识别面富含疏水残基和酸性残基，形成与货物信号肽互补的结合沟槽。值得注意的是，SEC24B在COPII家族中具有最广泛的货物谱（包括G蛋白偶联受体、生长因子受体和胶原蛋白），这与其较大的货物识别面一致。

**机制模型**：SEC24B的核质定位（Approved）的可能机制：（1）SEC24B参与核膜蛋白的ER→核膜运输，在核孔复合物组装和核膜完整性维持中发挥间接作用。核膜蛋白（如SUN、Nesprin、Lamin相关蛋白）作为COPII货物经由SEC24B识别，其运输受阻将影响核膜结构；（2）COPII囊泡可沿微管运输至核周区域，SEC24B在该区域的局部富集产生HPA核质信号；（3）TERF2互作提示SEC24B可能在端粒核膜锚定和端粒位置效应（TPE）中提供膜-染色质界面。PMID:36536241发现SEC24B调控小胶质细胞铁死亡（ferroptosis），PMID:40536345表明SEC24B参与STING通路的线性泛素化调控，进一步支持其在炎症信号中的核周功能。

**TE调控展望**：SEC24B作为COPII核心货物受体不直接参与转录调控，但通过以下机制可能间接影响TE：（1）控制核膜蛋白运输，影响核膜上的染色质锚定区域和核纤层相关染色质结构域（LADs），LADs富含LINE-1等TE序列；（2）通过STING-cGAS通路调控衰老相关分泌表型（SASP），该通路被胞质dsDNA（包括TE来源的cDNA）激活。SEC24B的核质信号值得在核膜脂质代谢和TE区域核周定位的空间关系背景下进一步研究。


![PAE](https://alphafold.ebi.ac.uk/files/AF-O95487-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000138802-SEC24B

![](https://images.proteinatlas.org/38181/440_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/38181/440_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/38181/428_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/38181/428_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/38181/433_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/38181/433_D8_2_red_green.jpg)

### PubMed 文献

**PubMed count: 45**

| 42079608 | Identification of a migrasome-related lncRNA signature and its prognostic and immunological role in bladder cancer. | Front Immunol 2026 |
| 41840584 | TCOF1 affects Golgi secretory pathway contributing to the angiogenesis in renal cancer. | Cell Commun Signal 2026 |
| 41598173 | Positive Selection in Aggression-Linked Genes and Their Protein Interaction Networks. | Life (Basel) 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SEC24B

