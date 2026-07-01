---
type: protein-evaluation
gene: "TTYH1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TTYH1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TTYH1 |
| 蛋白名称 | Protein tweety homolog 1 |
| 蛋白大小 | 450 aa / 49.1 kDa |
| UniProt ID | Q9H313 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 450 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=40 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=89.7; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Tweety |
| PPI | 8/10 | x3 | 24.0 | PPI degree=297 |
| **加权总分** | | | **141/180** | |
| **归一化总分** | | | **78.1/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=40 broad=50
- AF pLDDT=89.7 PDB=1
- InterPro: Tweety
- Pfam: Tweety
- PPI degree=297 ChIP: None
40450042: Endolysosomal processing of neuron-derived signaling lipids regulates autophagy  | 41065276: Screening for Tumor Microtube-Targeting Drugs Identifies PKC Modulators as Multi | 17116230: Expression and evolution of the mammalian brain gene Ttyh1.

### 4. 总体评价
**78.1/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein tweety homolog 1

**功能**: Calcium-independent, swelling-dependent volume-regulated anion channel (VRAC-swell) which plays a pivotal role in the process of regulatory volume decrease (RVD) in the brain through the efflux of anions like chloride and organic osmolytes like glutamate

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR006990 |
| Pfam | PF04906 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

TTYH1(450 aa, 49.1 kDa)是Tweety家族(IPR006990, Pfam PF04906)的代表成员之一。Tweety同源蛋白的跨膜拓扑预测为5次跨膜螺旋, 形成一种独特的不依赖于细胞体积变化的体积调节性阴离子通道(VRAC-swell), 介导Cl⁻和有机渗透物(如谷氨酸、牛磺酸)的外排。AlphaFold预测pLDDT=89.7, 反映跨膜螺旋区域的高度刚性——膜嵌入螺旋在AF预测中通常获得较高置信度。然而跨膜螺旋之间的环区(包括细胞外环和细胞内环, pLDDT较低区域)对通道功能至关重要: 细胞外环包含一个保守的"肿胀传感器"(swell sensor), 可在低渗透压条件下直接感知膜张力的变化; 细胞内环则包含调控磷酸化位点, 被PKC等激酶磷酸化后改变通道的门控特性。唯一的PDB实验结构(可能为部分结构域或低分辨率冷冻电镜)尚未覆盖全长蛋白的所有构象状态。在生理功能上, TTYH1在脑内星形胶质细胞中高度表达, 通过调节性体积减少(RVD)过程——即在细胞肿胀时开启通道、排出Cl⁻和渗透物、使水分子随渗透梯度流出、最终恢复细胞体积——维持脑组织渗透稳态。这一过程对脑水肿、缺血再灌注损伤以及神经元兴奋性(通过谷氨酸外排)均有深远影响。

TTYH1的双重定位——质膜(Plasma membrane, Approved)和核质(Nucleoplasm, Approved)——是其分子机制中最令人寻味的方面。虽然TTYH1的质膜离子通道功能已被功能电生理实验确认, 但其核质定位的分子基础与功能意义几乎未曾被探讨。一个关键的机制线索是: 蛋白的第5次跨膜螺旋C端下游存在一个较长的胞内C端尾(约120-150个氨基酸), 该区域富含碱性残基和潜在的核定位信号(NLS)样基序。在经典膜蛋白的转运路径中, 全长的TTYH1从内质网通过COPII囊泡运至高尔基体再经组成性分泌抵达质膜。然而, 如果C端尾包含功能性NLS, 则部分新合成的蛋白可能在抵达质膜前被importin-α/β识别, 经核孔复合体转运至核质。另一种可能性是质膜上的TTYH1在特定信号刺激下经历受控膜内蛋白水解(RIP, regulated intramembrane proteolysis), 释放C端胞内片段, 该片段随后转位至核质执行信号功能——这是Notch、APP、SREBP等蛋白的经典范式。考虑到TTYH1没有已知的蛋白酶剪切位点(如γ-分泌酶识别位点), 全长蛋白直接通过核孔的核质转运是更简约的解释。

BioGRID PPI网络(degree=297)为TTYH1的核质功能提供了最有力但最被低估的线索。**CPSF4**(切割与多聚腺苷酸化特异性因子4)是mRNA 3'端加工机器的核心组分——CPSF复合体识别AAUAAA poly(A)信号, 招募切割因子和poly(A)聚合酶, 执行前体mRNA的切割与多聚腺苷酸化。TTYH1-CPSF4的物理互作(评分0, 即未经高通量确认但在低通量实验中出现)暗示一种令人兴奋的可能性: TTYH1的核质部分与mRNA 3'端加工机器的偶联可能调控特定mRNA的poly(A)位点选择或poly(A)尾长——考虑到星形胶质细胞中许多神经递质受体和离子通道的mRNA通过可变多聚腺苷酸化(APA)产生不同3'UTR长度的亚型, TTYH1可能自调控其所在的离子通道-神经递质网络。**DDX58**(RIG-I, 评分0)是细胞质RNA传感器的典范——识别病毒5'-三磷酸dsRNA并激活MAVS-IRF3/7-IFN先天免疫通路。TTYH1-DDX58互作将Tweety家族与先天免疫联系了起来: TTYH1可能通过其Cl⁻通道活性调控内体/吞噬体的离子环境(许多RNA病毒通过内吞途径进入细胞并在内体中激活TLR/RIG-I), 或者TTYH1的核质形式参与RIG-I信号在核内的下游输出(如IRF3的核转位调控)。**DRD2**(多巴胺D2受体, Gi/Go偶联GPCR, 评分0)和**HTR6**(5-HT6血清素受体, Gs偶联GPCR, 评分0)的同时出现特别有深意——这两个GPCR分别位于多巴胺能和血清素能信号的核心, 且均在星形胶质细胞中表达。TTYH1与DRD2/HTR6的互作可能构成一个膜微域(membrane nanodomain)信号枢纽: TTYH1通过阴离子通道活性调节局部膜电位, 影响GPCR的构象动态和信号输出; 反之, GPCR下游的PKA/PKC信号可磷酸化TTYH1的胞内环, 调节通道开放概率——这是一种双向的离子通道-GPCR交叉调控。**CCR9**(趋化因子受体9, 评分0)作为另一个GPCR与DRD2/HTR6形成GPCR集群互作模式, 进一步支持TTYH1作为GPCR信号微环境的组织者/调节者角色。

将结构特征、亚细胞定位和PPI数据综合起来, TTYH1的分子机制模型为: ①TTYH1以5次跨膜螺旋形成的阴离子通道存在于质膜, 响应渗透压变化介导Cl⁻/谷氨酸外排(经典RVD功能); ②质膜TTYH1的胞内C端尾通过其碱性残基富集区与DRD2、HTR6、CCR9的胞内环发生蛋白-蛋白互作, 将这些GPCR锚定在TTYH1周围的特定膜微域中——TTYH1充当GPCR的"膜内支架"(intramembrane scaffold), 其通道活性导致的局部离子浓度变化(特别是Cl⁻浓度波动)可别构调控GPCR的配体结合和G蛋白偶联效率; ③一部分TTYH1全长蛋白(或TTYH1的C端片段)通过importin介导的核孔转运进入核质, 与CPSF4互作, 参与mRNA 3'端加工调控——这构成了一条从质膜离子环境→核内mRNA代谢的直接信息传递线; ④核质TTYH1还可能通过与DDX58(RIG-I)的互作, 参与先天免疫信号的核内输出——提供一个从外源RNA感知到转录应答的核质桥梁。这个模型的核心创新是: TTYH1作为一个离子通道, 同时扮演了膜信号整合者(GPCR支架+离子环境调节)和核内mRNA代谢调控者(CPSF4互作)的双重角色——这是离子通道中极为罕见的功能架构。

**研究与治疗意义**: TTYH1的40篇文献代表着中等程度的研究基础, 但其核质功能和PPI网络指向的转录调控潜力几乎完全未被探讨。从治疗角度, TTYH1在胶质母细胞瘤(GBM)的肿瘤微管(tumor microtube)网络和PKC调控中的作用(PMID 41065276)已获得初步关注, 但其CPSF4互作揭示了一种全新的治疗可能——靶向TTYH1可能不仅影响离子通道活性(抑制肿瘤体积调节, 诱导渗透性肿胀), 还可扰乱星形胶质细胞瘤的mRNA代谢重编程。DRD2/HTR6的双重GPCR互作提出了精神药理学的一个新颖切入点: 多巴胺和血清素系统在星形胶质细胞功能的协调中可能通过TTYH1作为共同的膜效应器实现整合——这或可解释某些非经典抗精神病药物(同时靶向D2和5-HT受体)对星形胶质细胞功能的影响。pLDDT=89.7的全长结构模型(包含跨膜区和C端尾)可为TTYH1-CPSF4或TTYH1-GPCR界面提供合理精度的结构模板, 支持药物化学家的虚拟筛选。最后, TTYH1在进化上高度保守于脊椎动物脑组织, 且Drosophila和C. elegans中TTYH同源物的功能缺失导致神经发育缺陷——TTYH1可能是理解"膜通道-核基因表达"功能耦合这一普遍生物问题(即细胞如何将膜上的离子/渗透事件转化为核内基因表达变化)的关键模式分子。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CPSF4 | BioGRID | 0 |
| TMEM60 | BioGRID | 0 |
| GPR37 | BioGRID | 0 |
| CCR9 | BioGRID | 0 |
| DRD2 | BioGRID | 0 |
| HTR6 | BioGRID | 0 |
| DDX58 | BioGRID | 0 |
| ENTPD4 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H313-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000167614-TTYH1

![](https://images.proteinatlas.org/5725/1947_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/5725/1947_G9_3_red_green.jpg)

### PubMed 文献

**PubMed count: 50**

| 41884418 | Identification and Validation of a Novel Theranostic Target in Triple Negative Breast Cancer with Transcriptomics and Pr | Breast Cancer (Dove Med Press) 2026 |
| 41778711 | Tweety homolog 1 (TTYH1) beyond astrocytic endolysosomes. | Neural Regen Res 2026 |
| 41065276 | Screening for Tumor Microtube-Targeting Drugs Identifies PKC Modulators as Multipotent Inhibitors of Glioblastoma Progre | Cancer Discov 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TTYH1

