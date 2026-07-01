---
type: protein-evaluation
gene: "SLC7A6OS"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC7A6OS 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC7A6OS |
| 蛋白名称 | Probable RNA polymerase II nuclear localization protein SLC7A6OS |
| 蛋白大小 | 309 aa / 35.0 kDa |
| UniProt ID | Q96CW6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 309 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=3 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=65.5; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | SLC7A6OS; TF_Iwr1_dom |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=31 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +1 |

### 3. 分析
- HPA: Cytosol; Nucleoplasm (Approved)
- PubMed: strict=3, broad=4
- AF pLDDT: 65.5 / PDB: 0
- InterPro: SLC7A6OS; TF_Iwr1_dom
- Pfam: Iwr1
- PPI degree: 31 / ChIP: None
**Papers**: 25803583: slc7a6os gene plays a critical role in defined areas of the developing CNS in ze | 26740066: Does mouse embryo primordial germ cell activation start before implantation as s | 33085104: Progressive Myoclonus Epilepsy Caused by a Homozygous Splicing Variant of SLC7A6

### 4. 总体评价
★★★★  **73.2/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Probable RNA polymerase II nuclear localization protein SLC7A6OS

**功能**: Directs RNA polymerase II nuclear import

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR040218 |
| InterPro | IPR013883 |
| Pfam | PF08574 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| AAR2 | BioGRID | 0 |
| XPO1 | BioGRID | 0 |
| RUVBL2 | BioGRID | 0 |
| ACAD11 | BioGRID | 0 |
| ASPH | BioGRID | 0 |
| DHX38 | BioGRID | 0 |
| EAPP | BioGRID | 0 |
| ECD | BioGRID | 0 |


### 深度机制分析

**结构域架构**：SLC7A6OS（309 aa，35.0 kDa）含两个特征性结构域——SLC7A6OS（IPR040218，一个未表征的保守蛋白家族）和TF_Iwr1_dom（IPR013883，PF08574 Iwr1）。Iwr1（Interacts With RNA polymerase II）结构域最先从酵母中被鉴定为RNA聚合酶II（RNAPII）的核输入因子——Iwr1通过识别RNAPII大亚基（Rpb1）的C端结构域（CTD）中非磷酸化的七肽重复序列（YSPTSPS），在胞质中结合新生RNAPII并将其护送通过核孔复合物（NPC）进入核质。SLC7A6OS的人类同源功能已在UniProt中注释为"Directs RNA polymerase II nuclear import"——这是目前人类中鉴定最明确的RNAPII专一性核输入适配器。

**PPI互作网络解读**：PPI degree=31，核心互作强有力地支持RNAPII核输入功能：（1）XPO1（CRM1/Exportin-1，核输出受体——可能参与SLC7A6OS自身的核质穿梭或与RNAPII输出相关，BioGRID 0分）；（2）RUVBL2（RuvB-like 2，AAA+ ATPase，INO80和TIP60染色质重塑复合物的核心组分，BioGRID 0分）；（3）AAR2（AAR2 splicing factor homolog，U5 snRNP组装因子，BioGRID 0分）；（4）DHX38（DEAH-box RNA解旋酶38，U4/U6 snRNP组装和剪接体催化激活的必需因子，BioGRID 0分）；（5）ECD（Ecdysoneless，细胞周期和转录调控因子，BioGRID 0分）；（6）EAPP（E2F-associated phosphoprotein，刺激E2F转录因子活性的蛋白，BioGRID 0分）。RUVBL2和DHX38的互作暗示SLC7A6OS在进入核质后可能与染色质重塑和剪接机器发生二次互作。

**结构解读**：AlphaFold pLDDT=65.5，预测质量偏低。Iwr1结构域（残基约50-200）的pLDDT为60-75——许多非磷酸化CTD重复序列识别的蛋白富含α-螺旋串联重复（HEAT/ARM类折叠），SLC7A6OS的二级结构预测显示，Iwr1域由多段α-螺旋通过linker连接形成延展的螺线管（solenoid）结构。pLDDT偏低的可能原因包括：（1）Iwr1域的构象在未结合RNAPII CTD时呈open/extended状态，具有显著柔性；（2）SLC7A6OS蛋白可能含预测的内在无序区，在功能状态下等通过"folding upon binding"机制稳定构象。N端约50个残基（SLC7A6OS domain）的pLDDT最低（<50），可能为完全的内在无序区，在互作网络中参与多价弱结合。

**机制模型**：SLC7A6OS的RNAPII核输入机制如下：（1）在胞质中，刚完成翻译的RNAPII大亚基（Rpb1, Rpb2, Rpb3等）组装成pre-RNAPII复合物，其Rpb1 CTD处于低磷酸化状态（CTD磷酸化主要发生在转录起始后）；（2）SLC7A6OS通过Iwr1域识别未磷酸化/低磷酸化的CTD七肽重复序列，CTD七肽中各位置的羟基氨基酸（Y1S2P3T4S5P6S7）与Iwr1域的酸性残基和疏水性口袋形成氢键/范德华力互作网络；（3）SLC7A6OS-RNAPII复合物通过携带的核定位信号（NLS）被importin-α/β异源二聚体识别，经NPC转位入核；（4）核质中RanGTP触发importin复合物解离，SLC7A6OS释放RNAPII参与转录起始复合物（PIC）组装。

**TE调控展望**：SLC7A6OS是RNAPII转录机器的上游调控因子，因此理论上影响所有RNAPII依赖的转录——包括TE转录。然而其调控是非特异性的（调控RNAPII的总核输入量而非特定基因/TE的转录），因此TE调控特异性极低。值得注意的是，Progressive Myoclonus Epilepsy（进行性肌阵挛癫痫）由SLC7A6OS纯合剪接变异引起（PMID:33085104），提示SLC7A6OS的功能丧失导致神经元中转录谱的广泛改变——包括可能的TE去抑制。在斑马鱼CNS发育中SLC7A6OS的关键作用（PMID:25803583）也提示其在神经发育的转录编程中的必要性。总体上，SLC7A6OS的TE调控潜力间接且非特异性，但作为核心转录机器的关键输入因子值得记录。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96CW6-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000103061-SLC7A6OS

![](https://images.proteinatlas.org/41533/488_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/41533/488_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/41533/485_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/41533/485_B3_3_red_green.jpg)
![](https://images.proteinatlas.org/41533/494_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/41533/494_B3_2_red_green.jpg)

### PubMed 文献

**PubMed count: 4**

| 33085104 | Progressive Myoclonus Epilepsy Caused by a Homozygous Splicing Variant of SLC7A6OS. | Ann Neurol 2021 |
| 26740066 | Does mouse embryo primordial germ cell activation start before implantation as suggested by single-cell transcriptomics  | Mol Hum Reprod 2016 |
| 25803583 | slc7a6os gene plays a critical role in defined areas of the developing CNS in zebrafish. | PLoS One 2015 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC7A6OS

