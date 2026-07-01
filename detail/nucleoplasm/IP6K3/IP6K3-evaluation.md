---
type: protein-evaluation
gene: "IP6K3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## IP6K3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | IP6K3 |
| 蛋白名称 | Inositol hexakisphosphate kinase 3 |
| 蛋白大小 | 410 aa / 46.4 kDa |
| UniProt ID | Q96PC2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 410 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=20 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=75.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | IPK; IPK_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=37 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=20 broad=30
- AF pLDDT=75.4 PDB=0
- InterPro: IPK; IPK_sf
- Pfam: IPK
- PPI degree=37 ChIP: None
33497757: IP6K3 and IPMK variations in LOAD and longevity: Evidence for a multifaceted sig | 38403246: Insights into the roles of inositol hexakisphosphate kinase 1 (IP6K1) in mammali | 41832493: Fibroblast-associated CTHRC1 as a key indicator of recurrence risk in prostate c

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Inositol hexakisphosphate kinase 3

**功能**: Kinase that converts inositol hexakisphosphate (InsP6) to diphosphoinositol pentakisphosphate (InsP7/PP-InsP5)(PubMed:11502751, PubMed:34381031). Regulates cellular phosphate export by binding to the SPX domain of the XPR1 phosphate transporter (PubMed:34381031)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR005522 |
| InterPro | IPR038286 |
| Pfam | PF03770 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IPPK | STRING | 960 |
| IP6K1 | STRING | 913 |
| IP6K2 | STRING | 913 |
| ITPKB | STRING | 761 |
| MAP3K3 | BioGRID | 1 |
| BAG6 | BioGRID | 1 |
| UBL4A | BioGRID | 1 |
| TARDBP | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96PC2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000161896-IP6K3

![](https://images.proteinatlas.org/53644/1536_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/53644/1536_H3_3_red_green.jpg)
![](https://images.proteinatlas.org/53644/1402_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/53644/1402_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/53644/1397_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/53644/1397_E1_3_red_green.jpg)

### PubMed 文献

**PubMed count: 30**

| 41832493 | Fibroblast-associated CTHRC1 as a key indicator of recurrence risk in prostate cancer. | World J Surg Oncol 2026 |
| 41683831 | Role of Inositol Hexakisphosphate Kinases in Vascular Smooth Muscle Cell Calcification. | Int J Mol Sci 2026 |
| 41387660 | MiR-127 and miR-375 regulate the proliferation and differentiation of yak intramuscular adipocyte precursors through the | Mamm Genome 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/IP6K3


### 深度机制分析

IP6K3（Inositol hexakisphosphate kinase 3）是肌醇焦磷酸合成途径的关键激酶，结构属于IPK（IP6K）激酶家族（InterPro:IPR005522, IPR038286/IPK_sf），Pfam注释为IPK（PF03770）。AlphaFold预测pLDDT=75.4，整体折叠质量中等偏好，其中IPK催化结构域（约300个残基的核心区域）可能以较高置信度折叠，而N端和C端延伸区段贡献了全局pLDDT的下降。PDB尚无实验结构（PDB=0），但家族成员IP6K1和IP6K2的晶体结构揭示了催化口袋的ATP结合位点和底物InsP6识别模式，可供同源建模。

IP6K3催化的核心生化反应是：InsP6（六磷酸肌醇）+ ATP → 5-PP-InsP5（二磷酸肌醇五磷酸, InsP7）+ ADP（PubMed:11502751）。InsP7（PP-InsP5）是细胞内一种含有高能焦磷酸键（diphospho）的"超磷酸化"肌醇分子，属于肌醇焦磷酸（inositol pyrophosphate）家族——其焦磷酸基团携带的磷酸酐键水解自由能接近ATP，因此被称为"代谢货币"（metabolic currency）。InsP7通过蛋白质焦磷酸化（protein pyrophosphorylation）——即InsP7将β-磷酸基团转移至靶蛋白的预先磷酸化的丝氨酸残基——执行信号转导。

PPI互作网络（degree=37）的核心显示了IP6K3在磷酸肌醇代谢中的家族内互作特征。STRING高分伙伴包括IPPK（score=960, 肌醇五磷酸2-激酶，IP6K3的上游酶——将InsP5转化为InsP6底物）、IP6K1（score=913）和IP6K2（score=913, 两个同工型，可能形成同源/异源二聚体）以及ITPKB（score=761, 肌醇三磷酸3-激酶）。BioGRID实验互作（score=1）包括MAP3K3（MAPK信号通路激酶）、BAG6（分子伴侣和蛋白质质量控制系统）、UBL4A（泛素样蛋白）和TARDBP（TDP-43, RNA结合蛋白）。TARDBP互作特别值得关注——TDP-43在细胞质中的聚集是ALS（肌萎缩侧索硬化症）和额颞叶痴呆的病理标志，IP6K3-TARDBP互作可能涉及肌醇焦磷酸信号对RNA代谢和蛋白聚集的调控。

IP6K3在HPA中显示Cytosol和Nucleoplasm（Approved），确认了该激酶的核-质双分布。核内InsP7的功能包括：调控组蛋白去乙酰化酶（HDAC）活性、参与染色质重塑复合体的组装、以及调控转录因子的DNA结合能力。IP6K3通过InsP7/PP-InsP5合成控制细胞磷酸盐外排——InsP7绑定XPR1磷酸转运体SPX结构域（PubMed:34381031），调控磷酸盐稳态。这建立了IP6K3→InsP7→磷酸盐代谢→核苷酸/核酸合成的间接转录调控链。综合来看，IP6K3的深度机制模型为：IPK催化折叠→InsP6→InsP7焦磷酸第二信使合成→蛋白焦磷酸化/XPR1磷酸盐转运→磷酸盐稳态+染色质调控+RNA代谢（TDP-43互作）。该蛋白通过InsP7介导的染色质调控和TDP-43互作间接参与核内RNA/DNA代谢，但作为TE直接调控因子的证据不足（TE调控评估：极低）。



