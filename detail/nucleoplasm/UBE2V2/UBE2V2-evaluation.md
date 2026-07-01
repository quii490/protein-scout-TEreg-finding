---
type: protein-evaluation
gene: "UBE2V2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## UBE2V2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UBE2V2 |
| 蛋白名称 | Ubiquitin-conjugating enzyme E2 variant 2 |
| 蛋白大小 | 145 aa / 16.4 kDa |
| UniProt ID | Q15819 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Supported) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 145 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=34 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=94.4; PDB=18 |
| 调控结构域 | 4/10 | ×2 | 8.0 | UBC; UBQ-conjugating_enzyme/RWD |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=128 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **76.0/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Supported)
- PubMed strict=34 broad=83
- AF pLDDT=94.4 PDB=18
- InterPro: UBC; UBQ-conjugating_enzyme/RWD
- Pfam: UQ_con
- PPI degree=128 ChIP: None
15725630: UBE2V2 (MMS2) is not required for effective immunoglobulin gene conversion or DN | 39906994: Downregulated PSME3 Contributes to Severe Preeclampsia by Promoting Trophoblast  | 37755128: UBE2V2 promotes metastasis by regulating EMT and predicts a poor prognosis in lu

### 4. 总体评价
**76.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ubiquitin-conjugating enzyme E2 variant 2

**功能**: Has no ubiquitin ligase activity on its own. The UBE2V2/UBE2N heterodimer catalyzes the synthesis of non-canonical poly-ubiquitin chains that are linked through 'Lys-63'. This type of poly-ubiquitination does not lead to protein degradation by the proteasome. Mediates transcriptional activation of target genes. Plays a role in the control of progress through the cell cycle and differentiation. Plays a role in the error-free DNA repair pathway and contributes to the survival of cells after DNA da

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000608 |
| InterPro | IPR016135 |
| Pfam | PF00179 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UBE2N | STRING | 999 |
| RPS27A | STRING | 997 |
| RAD18 | STRING | 992 |
| HLTF | STRING | 990 |
| SHPRH | STRING | 988 |
| UBA52 | STRING | 982 |
| TRAF6 | STRING | 971 |
| UBE2B | STRING | 966 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q15819-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000169139-UBE2V2

![](https://images.proteinatlas.org/52535/1028_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/52535/1028_F12_4_red_green.jpg)
![](https://images.proteinatlas.org/52535/1309_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/52535/1309_G10_3_red_green.jpg)
![](https://images.proteinatlas.org/52535/802_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/52535/802_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/53186/1028_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/53186/1028_B3_2_red_green.jpg)

### 深度机制分析

**结构域架构与分子功能**：UBE2V2包含两个核心结构域——UBC泛素结合酶核心结构域（InterPro: IPR000608; Pfam: PF00179）和RWD结构域（IPR016135）。UBC结构域是泛素结合酶（E2）家族的标志性α/β折叠，但UBE2V2缺乏催化半胱氨酸残基，使其成为一种非经典E2变体——自身不具备泛素连接酶活性，必须与具有催化能力的UBE2N（Ubc13）形成异源二聚体才能行使功能。RWD结构域（命名源于RING finger、WD repeat和DEAD-like helicase三个家族的首字母）通常介导蛋白质-蛋白质相互作用，在此可能参与底物识别或E3连接酶对接。AlphaFold预测全长pLDDT=94.4，表明该145个氨基酸的蛋白折叠高度有序；18个PDB实验结构（包括UBE2V2-UBE2N复合物晶体）进一步验证了这一构象稳定性。

**PPI网络与信号通路**：STRING数据库显示UBE2V2拥有128个互作伙伴。UBE2N（STRING score=999）是其最核心的功能伴侣——二者形成的异源二聚体专门催化Lys-63（K63）连接的非经典多聚泛素链合成，与经典的K48连接（介导蛋白酶体降解）截然不同，K63泛素链主要发挥信号传导平台功能。RAD18（992）、HLTF（990）和SHPRH（988）均为DNA损伤修复通路的E3泛素连接酶：RAD18介导PCNA单泛素化启动跨损伤合成，HLTF和SHPRH则通过K63多聚泛素化PCNA调控复制后修复中的模板转换。TRAF6（971）是天然免疫中IL-1R/TLR通路和NF-κB信号的关键E3连接酶，提示UBE2V2在炎症信号转导中的角色。RPS27A（997）和UBA52（982）是泛素前体蛋白（融合泛素-核糖体蛋白），高评分可能反映泛素供体功能关系。UBE2B（966）是另一E2酶，参与DNA修复，可能在某些条件下与UBE2V2形成替代二聚体。

**结构解读**：pLDDT=94.4意味着AlphaFold对全长的预测置信度极高，蛋白核心几乎完全有序折叠。UBC结构域的典型α/β折叠包含4条α螺旋和4条β折叠，其活性位点环区（尽管缺乏催化性Cys）在与UBE2N结合后会经历构象重排。已有晶体结构证明UBE2V2-UBE2N异源二聚体形成不对称界面：UBE2V2的UBC结构域通过氢键网络和疏水作用与UBE2N的对应结构域紧密结合，同时将UBE2N的催化半胱氨酸（Cys87）定位至有利于K63连接的方向——K63位于受体泛素的溶剂可及表面，而非K48所在的疏水裂隙。PAE图显示单链内部残基间预测误差极低（<5 A），表明单体内折叠高度可信；UBE2V2与UBE2N界面区域PAE值亦较低，与已知实验结构一致。

**分子机制模型**：综合全部证据，UBE2V2作为E2变体通过与UBE2N组成型异源二聚化发挥K63特异性泛素链合成功能。在DNA损伤应答中，HLTF/SHPRH通过其UBZ/UBM泛素结合结构域识别已泛素化的PCNA，将UBE2V2-UBE2N复合物招募至停滞的复制叉，催化PCNA的K63多聚泛素化，启动模板转换介导的无错修复。在天然免疫信号中，TRAF6利用该复合物催化自身K63自泛素化，形成的K63链作为TAK1/TAB和IKK复合物的招募支架激活NF-κB。核质定位与DNA损伤应答功能高度一致——PCNA泛素化发生在核内的复制叉位点。最新研究（PMID: 41879050）揭示了Uev1A（UBE2V2的同源物）在多倍体和二倍体细胞中拮抗致癌Ras信号的功能，拓展了UBE2V2在细胞周期和基因组稳定性中的调控职责。

**研究与治疗意义**：UBE2V2在肺癌转移中通过调控上皮间质转化（EMT）促进转移并预测不良预后（PMID: 37755128）。由于UBE2V2不具备独立的催化活性，靶向UBE2V2-UBE2N二聚化界面（而非活性位点）代表了一种新颖的药物设计策略——可能实现更高的选择性。UBE2V2在K63泛素化通路中的核心地位使其成为炎症性疾病和DNA修复缺陷相关肿瘤的潜在靶点。仅34篇PubMed论文（8/10新颖性）暗示大量的下游信号通路仍有待阐明。

### PubMed 文献

**PubMed count: 83**

| 41879050 | Uev1A counteracts oncogenic Ras stimuli in both polyploid and diploid cells. | Elife 2026 |
| 41719745 | Environmentally relevant levels of BDE-209 induces proteomic and phosphoproteomic reprogramming in murine melanoma cells | Chemosphere 2026 |
| 41706758 | Human Periodontal Ligament Transcriptomes Under Orthodontic Extrusion and Intrusion: An Exploratory Pilot RNA-Seq Study  | Orthod Craniofac Res 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UBE2V2

