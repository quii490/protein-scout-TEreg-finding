---
type: protein-evaluation
gene: "PPP1R32"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PPP1R32 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PPP1R32 |
| 蛋白名称 | Stabilizer of axonemal microtubules 4 |
| 蛋白大小 | 425 aa / 47.3 kDa |
| UniProt ID | Q7Z5V6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; End piece; Mid piece; Nucleoplasm; Plasma (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 425 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=3 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=55.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | SAXO4 |
| PPI | 6/10 | x3 | 18.0 | PPI degree=79 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +2 |

### 3. 分析
- Cytosol; End piece; Mid piece; Nucleoplasm; Plasma membrane; Principal piece (Approved)
- PubMed strict=3 broad=5
- AF pLDDT=55.8 PDB=0
- InterPro: SAXO4
- Pfam: PPP1R32
- PPI degree=79 ChIP: None
28194645: Expression of a Novel Ciliary Protein, IIIG9, During the Differentiation and Mat | 34535732: IIIG9 inhibition in adult ependymal cells changes adherens junctions structure a | 41566508: IIIG9 and PP1α form a protein complex in the adherens junctions of polarized epe

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Stabilizer of axonemal microtubules 4

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR031410 |
| Pfam | PF15691 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 0 |
| PPP1CC | BioGRID | 0 |
| PPP1CA | BioGRID | 0 |
| UBR1 | BioGRID | 0 |
| IDE | BioGRID | 0 |
| RNF123 | BioGRID | 0 |
| LASP1 | BioGRID | 0 |
| AKAP8L | BioGRID | 0 |


### 深度机制分析

PPP1R32编码SAXO4（Stabilizer of Axonemal Microtubules 4），属于蛋白磷酸酶1（PP1）调节亚基家族（Pfam: PPP1R32; InterPro: IPR031410）。HPA显示其具有多重定位（Cytosol、End piece、Mid piece、Nucleoplasm、Plasma membrane、Principal piece，均为Approved），其中核质定位暗示其在纤毛/鞭毛结构功能之外的核内角色。蛋白大小425 aa / 47.3 kDa，但AlphaFold pLDDT仅55.8（PDB=0）表明该蛋白可能含有大量固有无序区域（IDRs），这是许多PP1调节亚基和中心体/纤毛蛋白的共同特征——IDRs通过液-液相分离（LLPS）形成生物分子凝聚体。

PPI网络的核心发现是与PPP1CA和PPP1CC（PP1催化亚基α和γ异构体）的互作，确立了其作为PP1全酶的靶向亚基的角色。PP1是丝氨酸/苏氨酸磷酸酶超家族的核心成员，在核内参与有丝分裂退出、转录调控、RNA加工和DNA损伤应答等多个关键过程。PPP1R32可能通过将PP1催化活性靶向至特定核内底物（如剪接因子、转录因子或染色质修饰酶）来调控磷酸化信号。最近发表的文献证实PPP1R32/IIIG9与PP1α在极化室管膜细胞的黏附连接处形成蛋白复合物（PMID:41566508），其核质定位可能参与调控细胞连接相关基因的转录程序。

从结构域角度看，PPP1R32缺乏除自身家系（IPR031410）之外的任何功能注释结构域，与其可能的IDR特性一致。AKAP8L的互作（BioGRID）增强了其核功能假说——AKAP8L是核基质相关的PKA锚定蛋白，参与核内A-kinase信号微域的组织。若PPP1R32同时锚定PP1和AKAP8L，可能构建磷酸酶-激酶信号对，在核内特定亚区室中精细调控底物磷酸化。PubMed仅3篇使其成为极度新颖靶标，其作为PP1全酶组分在哺乳动物纤毛和核质之间的双重功能切换机制代表了结构生物学和信号转导交汇处的重要发现机会。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q7Z5V6-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162148-PPP1R32

![](https://images.proteinatlas.org/39068/1471_F11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/1471_F11_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/1784_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/1784_C2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/442_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/442_E8_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162148-PPP1R32

![](https://images.proteinatlas.org/39068/1471_F11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/1471_F11_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/1784_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/1784_C2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/442_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/442_E8_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162148-PPP1R32

![](https://images.proteinatlas.org/39068/1471_F11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/1471_F11_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/1784_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/1784_C2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/442_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39068/442_E8_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 5**

| 41566508 | IIIG9 and PP1α form a protein complex in the adherens junctions of polarized ependymal and MDCK cells. | Fluids Barriers CNS 2026 |
| 36544342 | The First Case Report of JAK2-BCR-PPP1R32 Fusion Genes Because of a Translocation (9;22;11)(p24;q11.2;q13) in a Patient  | Ann Lab Med 2023 |
| 34535732 | IIIG9 inhibition in adult ependymal cells changes adherens junctions structure and induces cellular detachment. | Sci Rep 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PPP1R32

