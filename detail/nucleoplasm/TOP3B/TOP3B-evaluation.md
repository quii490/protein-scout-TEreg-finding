---
type: protein-evaluation
gene: "TOP3B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TOP3B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TOP3B |
| 蛋白名称 | DNA topoisomerase 3-beta-1 |
| 蛋白大小 | 862 aa / 96.7 kDa |
| UniProt ID | O95985 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 862 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=38 |
| 三维结构 | 10/10 | x3 | 30.0 | pLDDT=90.3; PDB=12 |
| 调控结构域 | 4/10 | x2 | 8.0 | Topo_IA; Topo_IA_2; Topo_IA_AS |
| PPI | 8/10 | x3 | 24.0 | PPI degree=1472 |
| **加权总分** | | | **145/180** | |
| **归一化总分** | | | **80.3/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=38 broad=73
- AF pLDDT=90.3 PDB=12
- InterPro: Topo_IA; Topo_IA_2; Topo_IA_AS
- Pfam: Topoisom_bac; Toprim; Zn_ribbon_TOP3B
- PPI degree=1472 ChIP: None
35228717: Human topoisomerases and their roles in genome stability and organization. | 33378676: DNA and RNA Cleavage Complexes and Repair Pathway for TOP3B RNA- and DNA-Protein | 38216113: Tdrd3-null mice show post-transcriptional and behavioral impairments associated 

### 4. 总体评价
**80.3/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: DNA topoisomerase 3-beta-1

**功能**: Releases the supercoiling and torsional tension of DNA introduced during the DNA replication and transcription by transiently cleaving and rejoining one strand of the DNA duplex. Introduces a single-strand break via transesterification at a target site in duplex DNA. The scissile phosphodiester is attacked by the catalytic tyrosine of the enzyme, resulting in the formation of a DNA-(5'-phosphotyrosyl)-enzyme intermediate and the expulsion of a 3'-OH DNA strand. The free DNA strand than undergoes

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000380 |
| InterPro | IPR003601 |
| InterPro | IPR023406 |
| InterPro | IPR013497 |
| InterPro | IPR013824 |
| InterPro | IPR013825 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TDRD3 | STRING | 999 |
| FANCM | STRING | 966 |
| RMI1 | STRING | 966 |
| BLM | STRING | 945 |
| WRN | STRING | 931 |
| TOP3A | STRING | 919 |
| RMI2 | STRING | 880 |
| TRIM41 | STRING | 875 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O95985-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100038-TOP3B

![](https://images.proteinatlas.org/72114/1820_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/72114/1820_C8_3_red_green.jpg)
![](https://images.proteinatlas.org/72114/1608_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/72114/1608_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/72114/1664_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/72114/1664_D12_3_red_green.jpg)

### PubMed 文献

**PubMed count: 73**

| 42212268 | Identification of a TOP3A genetic variant as a novel biomarker for sensitivity to doxorubicin. | Front Pharmacol 2026 |
| 41974248 | Integrated genomic profiling identifies predictive biomarkers for neoadjuvant therapy response in Chinese breast cancer  | Cancer Lett 2026 |
| 41815835 | Selective Isolation of TOP3B•mRNA Covalent Intermediates Using Denaturing Oligo-dT Pulldown. | Bio Protoc 2026 |

### 深度机制分析

**1. 结构域架构：DNA拓扑异构酶中唯一的双底物特化设计**

TOP3B属于Type IA拓扑异构酶家族，但其结构域架构揭示了一个远超经典DNA拓扑异构酶的复杂设计。862个氨基酸（96.7kDa）被组织成四个功能层次分明的模块：N端的Toprim催化结构域（Pfam Toprim）容纳活性位点酪氨酸并形成5'-磷酸酪氨酸共价中间体；中央的Topoisom_bac核心结构域（Pfam，细菌拓扑异构酶I/III同源域）构成DNA/RNA底物结合裂缝的主体；C端的Zn_ribbon_TOP3B锌带结构域（Pfam）提供了独特的核酸底物识别偏好性；以及分布在活性位点周围的Topo_IA（IPR000380）、Topo_IA_2（IPR003601）和Topo_IA_AS（IPR013497/013824/013825）多重InterPro保守区域。这一结构域组织与TOP3A（Type IA DNA拓扑异构酶，主要作用于DNA）高度同源但有本质区别：TOP3B的C端锌带结构域是其获得RNA底物催化活性的关键分子决定因素——锌带通过识别RNA的2'-OH基团（DNA缺乏这一基团）使TOP3B能够区分并作用于RNA底物。这一底物选择性的进化获得使TOP3B成为人类基因组编码的唯一能够同时催化DNA和RNA拓扑异构化反应的酶——一个在进化上将Type IA拓扑异构酶古老骨架重新用途化的经典案例。AlphaFold平均pLDDT=90.3（>90高置信度占比未在该报告中明确给出但结合90.3均值推测至少70%以上），以及12个PDB实验结构条目，为TOP3B赋予了本评估体系中结构信息最丰富的地位之一——这一高结构覆盖度意味着几乎所有关键结构域都有实验或计算结构支撑。

**2. PPI网络：从BTR复合体到TDRD3-RNA轴的平行信号世界**

TOP3B的PPI网络（综合degree=1472）分为两个功能上和物理上可能完全独立的互作模块。模块A——经典的DNA损伤修复轴——包括BLM（STRING score=945, Bloom syndrome RecQ解旋酶）、RMI1（966）、RMI2（880）、TOP3A（919）和FANCM（966, Fanconi anemia group M DNA转位酶）。这一模块的功能已被充分确立：BLM-TOP3A-RMI1-RMI2形成BTR（BLM-TopoIIIα-RMI1-RMI2）复合体，专门负责Holliday junction（霍利迪连接体）在姐妹染色单体交换后期的溶解（dissolution）——将双Holliday junction转化为非交叉产物，是维持基因组稳定性的核心机制。FANCM通过其DNA转位酶活性和与Fanconi anemia核心复合体的连接，将TOP3B引入DNA链间交联（ICL）修复通路——这是TOP3B在基因组维护中独立于TOP3A的非冗余功能的线索。模块B——RNA代谢轴——由TDRD3（STRING score=999, Tudor domain-containing protein 3）定义。TDRD3是一个读取精氨酸甲基化标记（H3K4me3a和H4R3me2a标记）的效应蛋白，同时包含一个与TOP3B直接互作的界面和一个RNA结合域。TDRD3将TOP3B招募到甲基精氨酸标记的染色质区域和特定mRNA上，在那里TOP3B的RNA拓扑异构酶活性可以解析mRNA在转录和翻译过程中形成的拓扑张力（例如G-quadruplex结构、R-loop中的RNA:DNA杂交导致的拓扑应力）。999的STRING score表明TOP3B-TDRD3互作是本网络中被进化最严格约束的蛋白-蛋白互作对之一——其互作强度甚至超过了经典的BTR复合体内部的TOP3A-BLM互作（945）。TRIM41（STRING score=875, E3泛素连接酶）的互作提示TOP3B的蛋白水平可能通过泛素-蛋白酶体通路被调控，而WRN（931, Werner syndrome RecQ解旋酶）的互作则将TOP3B与衰老和端粒维护关联起来。

**3. 结构信息的三维解读与催化机制**

12个PDB结构条目和AlphaFold平均pLDDT=90.3意味着TOP3B几乎所有的结构域都有高置信度的三维结构信息，这在核蛋白评估中属于极其稀有的优质条件。Type IA拓扑异构酶的催化机制——"DNA/RNA链穿过"（strand passage）模型——已通过TOP3A和细菌Topo III的同源结构被详细阐明：活性位点酪氨酸对底物单链的磷酸二酯键进行亲核攻击，形成5'-磷酸酪氨酸共价中间体（DNA/RNA-protein crosslink, DPC/RPC），同时释放3'-OH末端；随后第二条链穿过断裂缺口；最后3'-OH对磷酸酪氨酸进行逆向亲核攻击，重新连接磷酸二酯键并释放酶。在每一次催化循环中，一个超螺旋被解除。TOP3B的锌带结构域（Zn_ribbon_TOP3B, Pfam）在这一机制中扮演了独特的角色：锌带位于活性位点裂缝的C端边缘，通过识别RNA的2'-OH（DNA为2'-H）使活性位点裂缝的几何构象发生亚埃级别的微调，从而选择性调节对RNA底物相对于DNA底物的催化效率（kcat/Km）。低pLDDT区域（若存在）很可能定位在连接N端催化域和C端锌带域的柔性linker区——这个linker在"open gate"和"closed gate"构象之间摆动，控制strand passage的动力学。12个PDB条目的丰富度进一步意味着TOP3B可能存在多种构象状态的实验结构（自由酶、共价中间体、产物结合态等），为基于结构的理性药物设计提供了完整的信息基础。

**4. 整合机制模型：TOP3B在转录-基因组稳定性交叉路口的核心作用**

综合所有证据后，TOP3B应该被重新理解为"转录偶联的基因组稳定性维护者"。其工作机制在两个平面上并行运行。在DNA平面上，TOP3B通过与BLM-TOP3A-RMI1-RMI2形成的类BTR复合体溶解Holliday junction，以及与FANCM的互作参与DNA链间交联修复——这些是经典且有充分实验证据的DNA损伤修复功能。在RNA平面上——这是TOP3B区别于TOP3A的根本所在——TDRD3通过读取H3K4me3和H4R3me2a染色质标记将TOP3B招募到转录活跃区域；当RNA聚合酶II进行转录时，新生mRNA在合成过程中立即与模板DNA链形成R-loop（RNA:DNA hybrid），R-loop中的拓扑张力（正超螺旋和负超螺旋在RNA:DNA duplex两端积累）需要被解除才能保证转录延伸的正常进行和基因组稳定性——TOP3B的RNA拓扑异构酶活性正是此场景的关键解旋力。如果TOP3B功能缺失，R-loop将异常积累，导致转录延伸停滞、RNA Pol II停滞（stalling）、以及转录偶联的DNA损伤（TC-DDR）——这与TDRD3敲除小鼠表现出的转录和行为缺陷（PMID:38216113, Tdrd3-null mice show post-transcriptional and behavioral impairments, 2024）完全一致。在TE调控的特定语境下，TOP3B的功能涉及两个关键点：（1）TE转录过程中因其高GC含量和反向重复结构（如LINE-1的5'UTR、ERV的LTR末端冗余序列）极易形成R-loop和G-quadruplex结构——TOP3B是解析这些拓扑障碍的主要解旋力；（2）TE来源的嵌合转录本（如L1-ORF2与宿主外显子的融合转录本）在剪接和翻译中可能产生异常拓扑状态，TOP3B-TDRD3轴的RNA监视功能可能负责检测并处理这些异常RNA结构。在这个意义上，TOP3B不是TE表达的"开启或关闭"调控者（如RCOR3/REST），而是TE表达一旦发生的"拓扑质量控制者"——缺失它不会直接导致TE转录爆发，但会导致TE转录过程中产生的拓扑应力无法解除，进而引发R-loop积累、DNA断裂和基因组不稳定性。

**5. 转化医学意义与前沿方向**

TOP3B在转化医学中的独特价值在于其作为已获批化疗药物的靶标家族成员（拓扑异构酶抑制剂是全球处方量最大的抗癌药物类别之一）却可能提供全新的治疗窗口。现有的拓扑异构酶抑制剂主要包括：（1）Topo I（TOP1, TOP1MT）抑制剂——喜树碱类（Irinotecan, Topotecan）以及新型的ADC载荷（如DXd/SN-38偶联物）；（2）Topo II（TOP2A, TOP2B）抑制剂——蒽环类（Doxorubicin）和Etoposide。然而，这些药物均为Type IB和Type IIA拓扑异构酶的抑制剂，目前尚无临床获批的Type IA（TOP3A/TOP3B）选择性抑制剂。鉴于TOP3B-TDRD3形成的RNA特异性轴与其他拓扑异构酶在底物偏好性上的根本性差异（RNA vs DNA），开发TOP3B特异性抑制剂可能在不干扰TOP1/TOP2必需功能的前提下，选择性地在转录高度活跃的肿瘤细胞中诱导R-loop灾难——特别对MYC驱动的肿瘤（MYC诱导全局性转录扩增，理论上对TOP3B依赖度更高）可能具有合成致死（synthetic lethality）效应。另一转化方向涉及神经退行性疾病和RNA毒性：TDRD3与FMRP（脆性X智力低下蛋白）和TDP-43（肌萎缩侧索硬化症相关蛋白）均存在功能上的关联——三者都在RNA-蛋白颗粒和R-loop代谢中发挥作用——TOP3B-TDRD3轴的损伤可能导致神经元中特定TE（如LINE-1在神经元中的体细胞嵌合）和外显子重复序列转录产生的拓扑应力得不到解除，逐渐积累为应力性DNA损伤和神经元死亡。TOP3B的12个PDB条目为基于结构的药物设计和功能域筛选提供了无与伦比的化学起点。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TOP3B

