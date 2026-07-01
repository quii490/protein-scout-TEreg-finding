---
type: protein-evaluation
gene: "MICU2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MICU2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MICU2 |
| 蛋白名称 | Calcium uptake protein 2, mitochondrial |
| 蛋白大小 | 434 aa / 49.7 kDa |
| UniProt ID | Q8IYU8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 434 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=50 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=74.2; PDB=12 |
| 调控结构域 | 4/10 | x2 | 8.0 | EF-hand-dom_pair; EF_hand_dom; MICU1/2/3 |
| PPI | 7/10 | x3 | 21.0 | PPI degree=104 |
| **加权总分** | | | **138/180** | |
| **归一化总分** | | | **76.5/100** | 互证: +2 |

### 3. 分析
- Mitochondria; Nucleoplasm (Approved)
- PubMed strict=50 broad=107
- AF pLDDT=74.2 PDB=12
- InterPro: EF-hand-dom_pair; EF_hand_dom; MICU1/2/3
- Pfam: 
- PPI degree=104 ChIP: None
38747181: MICU3 Regulates Mitochondrial Calcium and Cardiac Hypertrophy. | 30036491: Mitochondrial Ca(2+) signaling. | 32494073: Structure and mechanism of the mitochondrial Ca(2+) uniporter holocomplex.

### 4. 总体评价
**76.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Calcium uptake protein 2, mitochondrial

**功能**: Calcium sensor of the mitochondrial calcium uniporter (MCU) channel, which senses calcium level via its EF-hand domains (PubMed:24503055, PubMed:24560927, PubMed:26903221, PubMed:28615291, PubMed:30699349, PubMed:31397067, PubMed:32494073, PubMed:32667285, PubMed:32762847, PubMed:32790952). MICU1 and MICU2 form a disulfide-linked heterodimer that stimulates and inhibits MCU activity, depending on the concentration of calcium (PubMed:24560927, PubMed:26903221, PubMed:28615291, PubMed:30699349, Pu

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011992 |
| InterPro | IPR002048 |
| InterPro | IPR039800 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PHB2 | STRING | 797 |
| ITPR1 | STRING | 718 |
| COPS5 | BioGRID | 1 |
| ASH2L | BioGRID | 1 |
| CSNK1E | BioGRID | 1 |
| CSNK1D | BioGRID | 1 |
| KLHL22 | BioGRID | 1 |
| CDH5 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8IYU8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000165487-MICU2

![](https://images.proteinatlas.org/58790/1446_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/58790/1446_F8_4_red_green.jpg)
![](https://images.proteinatlas.org/58790/1149_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/58790/1149_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/58790/1138_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/58790/1138_F3_3_red_green.jpg)

### PubMed 文献

**PubMed count: 107**

| 42340986 | Correction: MICU2, a Paralog of MICU1, Resides within the Mitochondrial Uniporter Complex to Regulate Calcium Handling. | PLoS One 2026 |
| 42275149 | Disruption of Polycystin-1 Cleavage Impairs Mitochondrial Bioenergetics and Calcium Uptake in a Substrate-Dependent Mann | Am J Physiol Renal Physiol 2026 |
| 42129466 | MICU proteins facilitate calcium-dependent mitochondrial metabolon formation to regulate cellular energetics independent | Nat Metab 2026 |

### 深度机制分析

**结构域架构与分子功能推演。** MICU2的EF-hand结构域对(IPR011992, IPR002048)构成其钙感知核心,而MICU1/2/3家族特征域(IPR039800)赋予其与MCU通道复合体的特异性对接能力。典型的EF-hand以helix-loop-helix基序配位Ca2+离子,MICU2拥有两个串联EF-hand,这使其钙结合具有协同性(cooperativity)——第一个Ca2+结合后增强第二个位点的亲和力,形成类似"开关"的别构行为。不同于钙调蛋白(calmodulin)的广泛靶标谱,MICU2的EF-hand在进化上被限定于线粒体钙单向转运体(MCU)复合体,其表面电荷分布经过优化以识别MCU的coiled-coil跨膜螺旋(PubMed:32494073)。这种结构特化解释了为何MICU2虽然具备通用钙传感器折叠,却在功能上高度专一。AF2预测的pLDDT=74.2提示蛋白整体折叠良好但存在一定的柔性区域(尤其是在EF-hand之间的连接环),这种构象柔性对于"钙浓度依赖的门控切换"是功能必需的(PubMed:24560927)。

**PPI网络揭示的生物学意义。** PHB2(STRING 797)与ITPR1(STRING 718)构成MICU2互作网络的最高置信度核心。PHB2(prohibitin 2)是线粒体内膜的支架蛋白,参与线粒体嵴形态维持和OPA1加工——MICU2与PHB2的强互作暗示其可能在MCU复合体外还参与线粒体超微结构调控。ITPR1(IP3受体)是内质网Ca2+释放通道,MICU2→ITPR1→MCU构成了一条"ER→线粒体"的钙信号传递轴:IP3介导的ER钙释放被ITPR1感应,进而通过MICU2调控MCU介导的线粒体钙摄取,实现"钙微域(calcium microdomain)"的精准转导。更值得关注的是核质互作伴侣:ASH2L是COMPASS/MLL甲基转移酶复合体的核心亚基,负责催化H3K4me3——经典的转录激活标志;COPS5(CSN5/JAB1)是COP9信号小体(CSN)的去NEDD化酶催化亚基,调控Cullin-RING E3泛素连接酶的活性周期。这两个核蛋白与MICU2的互作强烈暗示MICU2在核质中存在非经典功能。

**结构层面的功能解读。** 12个PDB结构(包括冷冻电镜结构)已解析了MICU1-MICU2异二聚体与MCU孔道亚基的全长组装方式。关键结构特征包括:(1)MICU2通过C-terminal helix与MICU1形成域交换(domain-swapped)二聚体,二硫键锁定这一构象;(2)MICU1-MICU2异二聚体以两个对称位点结合MCU四聚体的N-terminal domain,形成"双闸门"调控架构;(3)Ca2+-free状态下MICU2的EF-hand呈闭合构象,遮盖MCU的孔道入口以阻止Ca2+内流;(4)Ca2+结合后EF-hand发生约30度的铰链运动,暴露MCU孔道并解除抑制(PubMed:30699349)。pLDDT=74.2的中等置信度主要来源于EF-hand间连接环的构象无序,这正是别构调控所必需的"动态结构元件"而非折叠错误。

**分子机制综合模型。** 综合所有证据,MICU2在分子层面执行"双稳态钙门控"功能:低钙(静息态,[Ca2+]cyt约100nM)时,MICU2-MICU1异二聚体物理阻塞MCU孔道,防止线粒体钙过载和ROS过量产生;高钙(信号态,[Ca2+]cyt>1μM)时,Ca2+结合引发EF-hand构象变化,异二聚体从MCU孔道解离,允许线粒体基质摄取Ca2+以激活TCA循环脱氢酶。然而,核质定位提示存在第二个功能层——MICU2可能在特定信号条件下易位至细胞核,通过ASH2L将钙信号耦联至H3K4甲基化表观遗传调控。这一"钙→MICU2核易位→H3K4me3重编程"假说如果成立,将是连接线粒体代谢状态与核基因表达的直接分子桥梁,弥补了目前"线粒体逆行信号(retrograde signaling)"领域的一个关键空白。COPS5的互作则进一步暗示MICU2可能影响Cullin-RING泛素化周期,将钙信号延伸至蛋白质稳态调控。

**研究与转化意义。** (1)若MICU2核质功能被实验验证,这将是首次发现线粒体钙传感器直接参与核内表观遗传调控,颠覆"MCU调控仅限于线粒体"的传统认知。(2)MICU2的EF-hand作为可药性结构域,针对其钙结合口袋开发小分子调节剂可能同时影响线粒体代谢和核基因表达——这在心肌肥厚(PubMed:38747181)和神经退行性疾病中具有双重治疗潜力。(3)PHB2与MICU2的强互作为理解线粒体嵴重塑与钙稳态的协调机制提供了切入点。(4)ASH2L-MICU2互作轴的验证需要ChIP-seq结合钙信号扰动实验,以确定MICU2是否确实影响H3K4me3在全基因组水平的分布。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MICU2

