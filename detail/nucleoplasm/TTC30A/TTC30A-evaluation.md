---
type: protein-evaluation
gene: "TTC30A"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TTC30A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TTC30A |
| 蛋白名称 | Intraflagellar transport protein 70A |
| 蛋白大小 | 665 aa / 76.1 kDa |
| UniProt ID | Q86WT1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Basal body; Centrosome; Nucleoplasm; Primary ciliu (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 665 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=2 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=92.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TPR-like_helical_dom_sf; TPR_rpt; TT30 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=38 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **76.5/100** | 互证: +1 |

### 3. 分析
- Basal body; Centrosome; Nucleoplasm; Primary cilium; Primary cilium tip (Approved)
- PubMed strict=2 broad=4
- AF pLDDT=92.8 PDB=0
- InterPro: TPR-like_helical_dom_sf; TPR_rpt; TT30
- Pfam: TPR_16
- PPI degree=38 ChIP: None
38074101: Paralog-specific TTC30 regulation of Sonic hedgehog signaling. | 31735294: Bi-allelic Mutations in TTC29 Cause Male Subfertility with Asthenoteratospermia 

### 4. 总体评价
**76.5/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构**：TTC30A（IFT70A）的核心结构特征是由多个三十四肽重复序列（TPR，Tetratricopeptide Repeat）单元组成的螺旋螺线管支架。InterPro注释包含IPR011990（TPR样螺旋结构域超家族）、IPR019734（TPR重复序列）和IPR039941（TT30家族，IFT70特异性），Pfam注释为PF13432（TPR_16）。单个TPR基序由34个氨基酸组成，形成一对反平行的α-螺旋；串联TPR单元折叠成右手超螺旋螺线管，产生一个凹面配体结合槽。TTC30A的665个氨基酸中包含多个TPR串联重复序列，构建了一个延伸型蛋白质-蛋白质相互作用平台。不同TPR的螺距和槽的几何形状决定了其结合配偶体的特异性——这是一种模块化的识别架构，允许IFT70通过沿其螺线管长度的不同TPR位点同时与多个IFT-B亚基结合。TTC30A的C端TT30保守区域（IPR039941）预计形成疏水核心，负责IFT-B复合物中的定向锚定。

**PPI网络与纤毛内转运**：TTC30A的PPI网络（degree=38）精确映射到IFT-B复合物的核心组成。IFT57和IFT81是IFT-B复合物中负责与IFT-A互作的桥梁亚基，决定了IFT颗粒的组装完整性。TRAF3IP1（IFT54）是IFT-B的另一个亚基，CLUAP1（IFT38的同源物）介导IFT-B与驱动蛋白-II马达的连接。IFT81和IFT74共同形成IFT-B的管蛋白结合模块——IFT81的N端结构域直接结合管蛋白α/β异源二聚体，而TTC30A通过TPR介导的支架作用稳定IFT81的构象。这一网络的结构意义在于：TTC30A不直接结合管蛋白，而是通过维持IFT81/IFT74的正确空间排布来确保管蛋白前体高效装载到IFT列车上。ARL13B（小GTP酶，Joubert综合征致病基因）和LCA5（Leber先天性黑蒙蛋白）的互作提示TTC30A额外承担纤毛膜蛋白的运输或信号分子的顺行转运功能。关键文献揭示了TTC30A/TTC30B的功能冗余（PubMed 35885974）：双敲除导致IFT-B完整性丧失和纤毛发生完全阻断，而单敲除表型轻微——这一"后备机制"解释了为什么TTC30A在基因组层面看起来非必需（PubMed=2），但在进化中却被高度保守。

**结构生物学解读**：pLDDT=92.8是这5个评估蛋白中的最高值，也是所有核蛋白评估中的顶级置信度之一。这一极高的pLDDT反映了TPR螺线管折叠的自稳定特性——连续TPR单元之间的密集疏水堆积产生高度有序且刚性的超螺旋，几乎没有柔性环或无序区域。665个氨基酸产生约76.1 kDa的分子量，生成的TPR螺线管长度估计约为120-140Å。无实验PDB结构（PDB=0），这使得TTC30A成为冷冻电镜（cryo-EM）结构解析的极佳候选——IFT-B全复合物（>1 MDa）在体外可重组组装，TTC30A的刚性和高pLDDT有利于颗粒取向的准确分配和3D重建的最高分辨率区域。

**分子机制模型**：TTC30A在纤毛内顺行转运（IFT）中的功能可分解为三个层次：(1) **基体装载**——在纤毛基底部的基体/中心粒（HPA Approved定位），TTC30A利用其TPR螺线管支架将IFT57、IFT81、TRAF3IP1/IFT54组装成一个功能性IFT-B亚复合物。这个"预组装模块"随后与IFT-A复合物和驱动蛋白-II马达对接，形成完整的IFT列车。(2) **顺行转运与货物递送**——驱动蛋白-II推动IFT列车沿轴丝微管（从基体到纤毛顶端）移动。在转运过程中，TTC30A通过稳定的IFT-B支架确保管蛋白（被IFT81/IFT74结合）和其他货物（SHH信号分子、纤毛膜蛋白）不会中途脱落。到达纤毛顶端后，IFT列车解体并释放货物。(3) **非纤毛核质功能**——HPA Approved核质定位不被经典IFT文献所预测，但表明TTC30A可能在纤毛发生信号与核基因表达重编程之间行使非经典功能。已知SHH信号通路中，纤毛是Gli转录因子的加工场所（Gli-FL→Gli-R转换），TTC30A通过调控SHH信号（PubMed 38074101，旁系同源特异性）可能参与Gli加工因子的纤毛-核穿梭。此外，TTC30A的管蛋白多聚谷氨酸化功能（UniProt）涉及轴丝管蛋白的翻译后修饰，这种修饰模式可能通过影响微管的信号传导属性间接影响YAP/TAZ等机械转导路径。

**研究与转化医学意义**：TTC30A的转化价值集中在纤毛病（ciliopathies）和SHH相关肿瘤：(1) 多囊肾病模型（PubMed 34548398）中TTC30A影响管蛋白修饰，提示TTC30A是纤毛软骨发育不良伴多囊肾的潜在修饰因子；(2) SHH信号在基底细胞癌和髓母细胞瘤中过度激活，TTC30A作为SHH信号调节因子的独立角色（区别于IFT转运功能）可能被药物靶向；(3) TTC30A/TTC30B冗余性揭示了一个合成致死机会——在TTC30B高表达的肿瘤中，选择性靶向TTC30A可能破坏IFT而不影响正常组织。在基础研究层面，TTC30A的极高pLDDT（92.8）和无实验结构（PDB=0）的组合是冷冻电镜社区寻找高价值靶标的理想特征：有保证的折叠质量降低了构象异质性对颗粒分类的干扰。核质定位的分子功能（Approved级，非不确定）需要用细胞周期同步化实验和核质分离蛋白组学进行验证——这可能开启IFT蛋白直接参与基因调控的全新研究领域。


### 补充分析 (UniProt API)

**蛋白全称**: Intraflagellar transport protein 70A

**功能**: Required for polyglutamylation of axonemal tubulin. Plays a role in anterograde intraflagellar transport (IFT), the process by which cilia precursors are transported from the base of the cilium to the site of their incorporation at the tip

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011990 |
| InterPro | IPR019734 |
| InterPro | IPR039941 |
| Pfam | PF13432 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ANKRD55 | BioGRID | 0 |
| IFT57 | BioGRID | 0 |
| ARL13B | BioGRID | 0 |
| LCA5 | BioGRID | 0 |
| UBXN10 | BioGRID | 0 |
| CLUAP1 | BioGRID | 0 |
| IFT81 | BioGRID | 0 |
| TRAF3IP1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q86WT1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000197557-TTC30A

![](https://images.proteinatlas.org/51714/2177_H10_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2177_H10_51_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2147_E7_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2147_E7_57_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2161_C12_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2161_C12_33_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000197557-TTC30A

![](https://images.proteinatlas.org/51714/2177_H10_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2177_H10_51_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2147_E7_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2147_E7_57_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2161_C12_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2161_C12_33_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000197557-TTC30A

![](https://images.proteinatlas.org/51714/2177_H10_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2177_H10_51_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2147_E7_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2147_E7_57_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2161_C12_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/51714/2161_C12_33_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 4**

| 38074101 | Paralog-specific TTC30 regulation of Sonic hedgehog signaling. | Front Mol Biosci 2023 |
| 35885974 | TTC30A and TTC30B Redundancy Protects IFT Complex B Integrity and Its Pivotal Role in Ciliogenesis. | Genes (Basel) 2022 |
| 34548398 | Ttc30a affects tubulin modifications in a model for ciliary chondrodysplasia with polycystic kidney disease. | Proc Natl Acad Sci U S A 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TTC30A

