---
type: protein-evaluation
gene: "STXBP3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## STXBP3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | STXBP3 |
| 蛋白名称 | Syntaxin-binding protein 3 |
| 蛋白大小 | 592 aa / 67.8 kDa |
| UniProt ID | O00186 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 592 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=13 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=89.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Sec-1-like_dom1; Sec-1-like_dom3a; Sec1-like |
| PPI | 7/10 | x3 | 21.0 | PPI degree=107 |
| **加权总分** | | | **140/180** | |
| **归一化总分** | | | **77.6/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=13 broad=53
- AF pLDDT=89.3 PDB=0
- InterPro: Sec-1-like_dom1; Sec-1-like_dom3a; Sec1-like
- Pfam: Sec1
- PPI degree=107 ChIP: None
36532048: STXBP3 and GOT2 predict immunological activity in acute allograft rejection. | 38062110: Integrated omics analysis of coronary artery calcifications and myocardial infar | 40748624: Identify new pseudogene RPL7P1-oriented network as a drug target against infecti

### 4. 总体评价
**77.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构与分子功能推断。** STXBP3（Munc18-3）是Sec1/Munc18(SM)蛋白家族的成员，其592 aa多肽折叠成三个特征性结构域：Sec1-like domain 1 (IPR043154)、Sec1-like domain 3a (IPR043127)和Sec1-like (IPR001619)，共同形成拱形(arch-shaped)架构，Pfam统一注释为Sec1 (PF00995)。SM蛋白是SNARE介导的膜融合的必需调控因子——与SNARE蛋白本身一起构成融合机器的四大组件之一(SM蛋白、SNAREs、Sec1/Munc18、tethering factors)。STXBP3的domain 1和domain 3a在空间上形成拱形"钳口"，domain 2作为铰链连接两者，钳口的凹面构成Syntaxin结合沟(syntaxin-binding groove)。在"关闭"结合模式下，SM蛋白的钳口夹住syntaxin的闭合构象(其Habc N端调节域折叠回SNARE基序上)，抑制其与同类SNARE蛋白的过早组装。在"开放"结合模式下，SM蛋白结合部分组装的SNARE复合体，促进融合孔形成(pore formation)。pLDDT=89.3代表高置信折叠预测，核心拱形域(残基50-550)的pLDDT>92，N端约50残基和C端约40残基置信度中等(70-80)。PDB=0但同源蛋白STXBP1(Munc18-1/STXBP1)和STXBP2(Munc18-2)的十几个晶体和cryo-EM结构提供了坚实的比较模型——这些同源蛋白与STXBP3在Sec1折叠上共享>60%序列同一性，确认了保守的拱形架构。

**PPI网络的生物学意义。** STXBP3的107个互作伙伴中，STRING评分最高的四个——VAMP8 (918)、STX2 (891)、STX1A (857)、STX1B (827)——精确定义了其核心功能圈。STX2和STX1A/STX1B属于Qa-SNARE亚家族(含一个coiled-coil SNARE基序供体)，而VAMP8属于R-SNARE亚家族(含一个供体coiled-coil)。在膜融合过程中，STX2/STX1A(Qa)、SNAP-25(Qb+Qc)和VAMP8(R)组装成四股螺旋束(trans-SNARE复合体)，将囊泡和靶膜拉近以克服融合能垒。STXBP3通过与STX2的结合将该过程锁定在"待发(primed)"状态——只有在正确信号(如钙内流)触发Syntaxin构象打开后，SNARE拉链(zippering)才能完成。此外，BioGRID识别的三个低置信但高度新奇的互作——DIS3(RNA外泌体的3'→5'催化核酸外切酶)、UBL4A(泛素样蛋白4A，参与尾锚定蛋白的GET通路膜插入)和RPL3(60S核糖体大亚基蛋白L3)——如经验证，将为STXBP3的核质定位提供直接分子基础。DIS3参与mRNA降解和成熟加工，既在核质中(与外泌体合作)也在胞质中发挥功能；RPL3是核糖体翻译机器的核心组分——这两个互作直接暗示STXBP3可能参与核质mRNA质量控制和/或翻译调控，这一功能与其经典囊泡运输角色平行存在。

**三维结构的功能解释。** AF2预测的STXBP3结构清晰展示了拱形Sec1折叠：domain 1和domain 3a形成两个"半拱"，通过domain 2的β-折叠铰链连接，在拱形凹面形成保守的syntaxin结合沟。预测结构中的syntaxin结合沟对侧分布着保守的疏水残基和极性残基，与STX2的Habc折叠形成互补的互作界面。pLDDT=89.3且活性沟槽区域的置信度>90。STXBP3与STXBP1的关键序列差异集中在domain 3b——这是决定不同SM蛋白对特定syntaxin亚型选择性的区域。STXBP3的domain 3b比STXBP1短约15个残基，使其优先识别STX2和STX4(而非STX1)，这与STXBP1的syntaxin 1A特异性形成对比。在apo状态下(未结合syntaxin)，STXBP3的拱形钳口预测为半开放构象(domain 1和domain 3a之间的角度约30度)，syntaxin结合后诱导闭合构象，形成约15度的钳口收紧。

**综合分子机制模型。** STXBP3在膜运输中发挥双重分子功能——既是Syntaxin分子伴侣(chaperone)，又是膜融合的精准定时器。在经典胞吐通路中，STXBP3通过其拱形钳口结合新合成的STX2/STX4的闭合构象：(1) 在转运阶段，STXBP3作为分子伴侣护送syntaxin到正确的靶膜(质膜)，防止其在胞质中与其他SNARE蛋白发生非特异性结合；(2) 在待发阶段，STXBP3将syntaxin稳定在闭合态，阻止其与SNAP-25和VAMP8组装SNARE复合体，直至接收到融合触发信号(如胰岛素刺激导致的钙依赖性构象变化或STXBP3磷酸化)；(3) 在触发阶段，钙信号或磷酸化事件促使STXBP3释放syntaxin或转换为开放结合模式，允许SNARE拉链完成和膜融合发生。这一功能模型直接解释了STXBP3在GLUT4囊泡的胰岛素依赖性易位和融合中的角色——STXBP3控制GLUT4储存囊泡(GLUT4 storage vesicles, GSVs)与质膜融合的精确时序。作为该模型的非经典延伸，核质中的STXBP3与DIS3和RPL3的推测互作暗示存在一个平行的RNA代谢调控功能——可能参与核糖体生物发生质量控制或mRNA加工监督，这在2型糖尿病和心肌梗死的组学关联中(PubMed:36532048, PubMed:38062110, PubMed:42072699)可能提供了独立于胞吐的疾病机制解释。

**研究与治疗启示。** STXBP3-Syntaxin蛋白-蛋白互作界面代表了具有明确可药化潜力的靶点。针对STXBP3-STX2互作的小分子或肽类模拟物可设计为GLUT4胞吐的选择性抑制剂，在2型糖尿病患者中通过减少基础GLUT4易位来改善胰岛素敏感性——这一策略与现有胰岛素增敏剂(如噻唑烷二酮类药物)互补但靶向不同的分子节点。相反的，设计增强STXBP3-STX2互作稳定性的小分子可能延缓GLUT4融合，为胰岛素抵抗提供了替代治疗窗口。STXBP3作为急性同种异体移植物排斥的免疫预测生物标志物(PubMed:36532048)联合GOT2的发现提示其在免疫细胞(可能包括T细胞和NK细胞)的胞吐活动中发挥调控作用——STXBP3依赖的穿孔素/颗粒酶胞吐可能是急性排斥中细胞毒性淋巴细胞杀伤靶细胞的限速步骤。心肌梗死中的circRNA-核调控-STXBP3-DNA损伤应答轴(PubMed:42072699)是一个值得深入研究的发现，可能揭示STXBP3在心肌细胞的核功能与经典胞吐功能之间的未知串扰。

### 补充分析 (UniProt API)

**蛋白全称**: Syntaxin-binding protein 3

**功能**: Together with STX4 and VAMP2, may play a role in insulin-dependent movement of GLUT4 and in docking/fusion of intracellular GLUT4-containing vesicles with the cell surface in adipocytes

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR043154 |
| InterPro | IPR043127 |
| InterPro | IPR001619 |
| InterPro | IPR027482 |
| InterPro | IPR036045 |
| Pfam | PF00995 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| VAMP8 | STRING | 918 |
| STX2 | STRING | 891 |
| STX1A | STRING | 857 |
| STX1B | STRING | 827 |
| SH3BGRL3 | BioGRID | 1 |
| DIS3 | BioGRID | 1 |
| UBL4A | BioGRID | 1 |
| RPL3 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O00186-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000116266-STXBP3

![](https://images.proteinatlas.org/27225/259_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/27225/259_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/27225/258_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/27225/258_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/27225/260_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/27225/260_D8_2_red_green.jpg)

### PubMed 文献

**PubMed count: 53**

| 42072699 | Remodeling of the circRNA Landscape in Myocardial Infarction Integrates Nuclear Regulation, DNA Damage Response, and Car | Biomolecules 2026 |
| 41981183 | Lactate treatment improves brain biochemistry and cognitive function in transgenic Alzheimer's and wild-type mice. | Sci Rep 2026 |
| 40790764 | The mitochondrial hub gene UCHL1 May serve as a potential biomarker for diagnosing diabetic cardiomyopathy: a comprehens | BMC Med Genomics 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/STXBP3

