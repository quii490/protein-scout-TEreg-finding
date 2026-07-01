---
type: protein-evaluation
gene: "TTC30B"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TTC30B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TTC30B |
| 蛋白名称 | Intraflagellar transport protein 70B |
| 蛋白大小 | 665 aa / 76.1 kDa |
| UniProt ID | Q8N4P2 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Basal body; Centrosome; Nucleoplasm; Primary ciliu (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 665 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=92.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TPR-like_helical_dom_sf; TPR_rpt; TT30 |
| PPI | 6/10 | x3 | 18.0 | PPI degree=62 |
| **加权总分** | | | **142/180** | |
| **归一化总分** | | | **78.7/100** | 互证: +2 |

### 3. 分析
- Basal body; Centrosome; Nucleoplasm; Primary cilium; Primary cilium tip (Approved)
- PubMed strict=5 broad=6
- AF pLDDT=92.8 PDB=0
- InterPro: TPR-like_helical_dom_sf; TPR_rpt; TT30
- Pfam: 
- PPI degree=62 ChIP: None
38074101: Paralog-specific TTC30 regulation of Sonic hedgehog signaling. | 31306809: A rare TTC30B variant is identified as a candidate for synpolydactyly in a Chine | 41786235: HOXD12 a candidate gene for a novel form of synpolydactyly.

### 4. 总体评价
**78.7/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

TTC30B的域架构以TPR(tetratricopeptide repeat)重复序列(IPR019734)和TPR超家族折叠(IPR011990)为核心，这是蛋白-蛋白相互作用中典型的多价支架基序。每个TPR基序由34个氨基酸形成一对反平行α螺旋，串联排列构成螺旋-转角-螺旋折叠的超螺旋结构，为IFT复合体B的组装提供了延伸的结合界面。TT30家族结构域(IPR039941)是其纤毛特异性功能标志。AlphaFold pLDDT高达92.8表明该蛋白整体折叠良好，TPR超螺旋呈现高度刚性的棒状构型，这正是IFT颗粒作为分子列车沿着轴丝微管双向运输的结构基础。缺乏PDB实验结构进一步说明TTC30B在IFT复合体B中的构象尚未被捕获——可能因为它需要结合到IFT-B1亚复合体后才呈现稳定构象，单独的TTC30B处于动态的无序到有序转变边界。

PPI网络清晰地定位了TTC30B在IFT-B复合体中的拓扑位置。IFT88(BioGRID)是IFT-B1亚复合体的核心组分，IFT81(BioGRID)、IFT52(BioGRID)、IFT46(BioGRID)和IFT57(BioGRID)均为IFT-B的规则亚基——TTC30B与所有这些组分的直接互作表明它紧密嵌入IFT-B核心架构，而非外围调控因子。CLUAP1/IFT38(BioGRID)作为IFT-B和IFT-A之间的连接器出现在网络中，进一步将TTC30B锚定在IFT颗粒的完整组装体中。UBXN10(BioGRID)含UBX结构域，通过识别p97/VCP AAA ATP酶参与泛素化蛋白的逆向转运，其与TTC30B的互作提示纤毛蛋白质量控制中可能存在IFT依赖的逆向分选机制。值得一提的是，ANKRD55(BioGRID)是锚蛋白重复蛋白，与神经发育障碍和脱髓鞘疾病相关，TTC30B-ANKRD55的物理连接暗示IFT可能在神经系统发育中选择性运输特定信号分子。

功能冗余性与亚功能化是TTC30B机制理解的关键维度。文献明确表明TTC30A和TTC30B在IFT复合体B的完整性维护中存在功能冗余(PMID:35885974)，这一遗传冗余解释了为何个体旁系同源物在纤毛组装中可互相代偿。然而，旁系同源物特异性的Sonic hedgehog信号调控(PMID:38074101)揭示了TTC30B的独特非冗余功能——SHH信号转导依赖于初级纤毛(SHH受体Patched和效应器Smo在刺激下的纤毛定位变化)，TTC30B可能通过调控IFT-B对SHH信号组分的纤毛内运输或出口而选择性激活该通路。TTC30B罕见错义变体被鉴定为并指(趾)多指症候选基因(PMID:31306809)以及HOXD12被验证为新型并指候选基因(PMID:41786235)的发现高度一致——SHH信号梯度在肢芽中控制指/趾数目，而TTC30B纤毛中的IFT功能精确调控SHH信号强度。

综合分子机制模型：TTC30B通过TPR超螺旋结构域在IFT-B1亚复合体中充当分子支架——多个TPR重复串联排列，以螺旋-螺旋相互作用精确嵌入IFT88/IFT81/IFT52等核心亚基的组装界面，pLDDT 92.8的高置信折叠确保了IFT颗粒在轴丝微管上以微米级距离往返运输时的机械稳定性。其与TTC30A的冗余性保障了IFT-B的基本组装完整性，而旁系同源物特异性功能(尤其是SHH信号调控)可能源于不同货物适配器蛋白对TTC30A/B的选择性识别或二者在纤毛基部和纤毛尖端的差异性定位。转化意义上，靶向TTC30B-IFT界面的小分子可选择性调控SHH信号强度，为SHH驱动的肿瘤(如基底细胞癌、髓母细胞瘤)和SHH缺陷性疾病(如并指、前脑全裂)提供精确干预策略——在不完全破坏纤毛结构下实现信号通路的分级调控。


### 补充分析 (UniProt API)

**蛋白全称**: Intraflagellar transport protein 70B

**功能**: Required for polyglutamylation of axonemal tubulin. Plays a role in anterograde intraflagellar transport (IFT), the process by which cilia precursors are transported from the base of the cilium to the site of their incorporation at the tip

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011990 |
| InterPro | IPR019734 |
| InterPro | IPR039941 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ANKRD55 | BioGRID | 0 |
| IFT57 | BioGRID | 0 |
| UBXN10 | BioGRID | 0 |
| IFT52 | BioGRID | 0 |
| CLUAP1 | BioGRID | 0 |
| IFT46 | BioGRID | 0 |
| IFT81 | BioGRID | 0 |
| IFT88 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N4P2-F1-predicted_aligned_error_v6.png)


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000196659-TTC30B

![](https://images.proteinatlas.org/51714/2177_H10_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2177_H10_51_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2147_E7_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2147_E7_57_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2161_C12_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2161_C12_33_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 6**

| 41786235 | HOXD12 a candidate gene for a novel form of synpolydactyly. | Bone 2026 |
| 38074101 | Paralog-specific TTC30 regulation of Sonic hedgehog signaling. | Front Mol Biosci 2023 |
| 35885974 | TTC30A and TTC30B Redundancy Protects IFT Complex B Integrity and Its Pivotal Role in Ciliogenesis. | Genes (Basel) 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TTC30B

