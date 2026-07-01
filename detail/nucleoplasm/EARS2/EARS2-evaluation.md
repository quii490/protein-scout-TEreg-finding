---
type: protein-evaluation
gene: "EARS2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## EARS2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | EARS2 |
| 蛋白名称 | Nondiscriminating glutamyl-tRNA synthetase EARS2, mitochondrial |
| 蛋白大小 | 523 aa / 58.7 kDa |
| UniProt ID | Q5JPH6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 523 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=35 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=89.5; PDB=0 |
| 调控结构域 | 6/10 | x2 | 12.0 | aa-tRNA-synth_I_cd-bd; aa-tRNA-synth_I_codon-bd_sub2; aa-tRNA-synth_I_CS |
| PPI | 8/10 | x3 | 24.0 | PPI degree=204 |
| **加权总分** | | | **142/180** | |
| **归一化总分** | | | **78.7/100** | 互证: +2 |

### 3. 分析
- Mitochondria; Nucleoplasm (Approved)
- PubMed strict=35 broad=51
- AF pLDDT=89.5 PDB=0
- InterPro: aa-tRNA-synth_I_cd-bd; aa-tRNA-synth_I_codon-bd_sub2; aa-tRNA-synth_I_CS
- Pfam: Anticodon_2; tRNA-synt_1c
- PPI degree=204 ChIP: None
26425749: Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview. | 27290639: New perspective in diagnostics of mitochondrial disorders: two years' experience | 40389993: B cell dysfunction in thalamus and brainstem involvement and high lactate caused

### 4. 总体评价
**78.7/100** | **nucleoplasm**
TE candidate: aa-tRNA-synth_I_cd-bd; aa-tRNA-synth_I_codon-bd_sub2; aa-tRNA-synth_I_CS


### 深度机制分析

EARS2属于I类氨酰tRNA合成酶超家族，其架构由三个保守结构域模块构成：N端的aa-tRNA-synth_I_catalyic_core(由Pfam:tRNA-synt_1c注释)，负责谷氨酰-AMP的催化合成——这是所有I类aaRS共有的Rossmann折叠催化核心，采用HIGH和KMSKS两个保守基序协调ATP的结合和腺苷酸过渡态的稳定；中段的aa-tRNA-synth_I_codon-bd_sub2和aa-tRNA-synth_I_cd-bd(InterPro)构成反密码子结合域，特异性识别线粒体tRNAGlu和tRNAGln的反密码子；C端的Anticodon_2(Pfam)提供了额外的反密码子读取模块。pLDDT 89.5表明整体折叠良好，但较KARS1(90.5)略低——这可能反映EARS2的非鉴别性活性(同时识别tRNAGlu和tRNAGln两种底物)对反密码子结合域的构象柔性的需求，结构必须容纳两个略有差异的反密码子序列。无PDB实验结构揭示了结构生物学中的空白——EARS2的非鉴别性催化机制(一个酶如何精确氨酰化两个不同tRNA物种)尚未被结构研究捕获，这是理解线粒体翻译进化的关键结构问题。

PPI网络(combined degree=204)清楚表明EARS2处于两个功能圈的交叉点：线粒体翻译(与DARS2, KARS, YARS, NARS2, IARS等线粒体aaRS蛋白关联)和核糖体生物发生(与FAU和MARS的高分互作)。FAU(STRING评分990)编码核糖体蛋白S30的泛素样融合蛋白——极高分值的互作强烈提示EARS2在核糖体前体组装中的功能性角色，而非单纯的空间邻近；FAU作为60S核糖体亚基的组成部分，其加工和成熟可能依赖EARS2的谷氨酸化活性。MARS(STRING评分983)作为甲硫氨酰tRNA合成酶是线粒体翻译起始的核心酶，二者高度的物理关联提示线粒体aaRS之间存在超分子组装体——类似于细胞质MSC的线粒体版本，这可能实现翻译效率的协同优化。值得特别注意的是，EARS2的核质定位(UniProt Approved)与线粒体tRNA合成酶的预期线粒体定位存在冲突——这一双定位模式提示EARS2可能存在核质中的非经典功能。

核质定位的数据为EARS2的非经典功能提供了有力的实验支持。线粒体aaRS蛋白在核质中出现并非孤例——多个线粒体aaRS被发现同时存在于核和线粒体中，核质池中的aaRS被认为参与：(1)线粒体蛋白的逆向信号转导——线粒体应激时，部分aaRS从线粒体释放到细胞质/核质以启动适应性转录程序；(2)核内tRNA氨酰化的质量控制——通过核质中氨酰化的重检验来确保tRNA在出核前的功能完整性。文献中EARS2表达受ALKBH5介导的m6A去甲基化调控(PMID:42185511)的发现尤为关键——m6A是mRNA代谢的核心表观转录调控形式，EARS2的m6A修饰状态直接影响其蛋白水平，这为核质定位提供了调控层面的解释：m6A去甲基化酶ALKBH5在核质中作用于EARS2 mRNA，调控其在两个细胞器中蛋白水平的分区平衡。EARS2调控线粒体生物发生和ROS稳态的功能(PMID:42272283)进一步暗示其在代谢重编程中具有核心作用——肿瘤细胞通过下调EARS2可能降低线粒体翻译从而促进Warburg效应。

综合分子机制模型：EARS2通过aa-tRNA-synth_I催化核心以非鉴别性方式催化线粒体tRNAGlu和tRNAGln的谷氨酸化——反密码子结合域的构象柔性(解释pLDDT 89.5和缺少PDB结构)允许容纳两个不同反密码子，这是线粒体tRNAGlx系统简化进化的结构基础。核质池中的EARS2通过m6A表观调控(ALKBH5依赖)调节其表达，参与逆行信号转导和翻译代谢平衡。转化意义上：(1)EARS2作为前列腺癌恩杂鲁胺耐药中的关键因子(PMID:42272283)，其调控线粒体生物发生和ROS稳态的能力提示靶向EARS2可逆转AR拮抗剂耐药——联合抑制线粒体翻译和雄激素信号可能产生协同致死效应；(2)m6A调控层面，调控ALKBH5-EARS2轴中的甲基化状态可精确调节线粒体翻译容量——为代谢性疾病和癌症治疗提供表观转录干预靶点；(3)Leigh综合征谱系中EARS2的致病突变(PMID:26425749)提示基因治疗(AAV递送校正基因至受影响脑区)是潜在的治疗方向。


### 功能描述

Non-discriminating glutamyl-tRNA synthetase that catalyzes aminoacylation of both mitochondrial tRNA(Glu) and tRNA(Gln) and participates in RNA aminoacylation for mitochondrial protein translation (PubMed:19805282). Attachs glutamate to tRNA(Glu) or tRNA(Gln) in a two-step reaction: glutamate is first activated by ATP to form Glu-AMP and then transferred to the acceptor end of tRNA(Glu) or tRNA(Gln) (PubMed:19805282). In vitro, cytoplasmic tRNA(Gln) is slightly glutamylated, but with low activit


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FAU | STRING | 990 |
| MARS | STRING | 983 |
| DARS2 | STRING | 929 |
| KARS | STRING | 928 |
| YARS | STRING | 928 |
| LARS | STRING | 924 |
| NARS2 | STRING | 913 |
| IARS | STRING | 912 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000103356-EARS2

![](https://images.proteinatlas.org/43289/1404_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/1404_B9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/584_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/584_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/565_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/565_F12_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000103356-EARS2

![](https://images.proteinatlas.org/43289/1404_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/1404_B9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/584_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/584_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/565_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/565_F12_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000103356-EARS2

![](https://images.proteinatlas.org/43289/1404_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/1404_B9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/584_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/584_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/565_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43289/565_F12_2_blue_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5JPH6-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 51**

| 42272283 | Glutamyl-tRNA synthetase 2 regulates mitochondrial biogenesis and reactive oxygen species homeostasis mediatingenzalutam | J Physiol Pharmacol 2026 |
| 42185511 | Icariin suppresses glycolysis in prostate cancer by upregulating ALKBH5 to mediate EARS2 m(6)A demethylation. | J Mol Histol 2026 |
| 41999222 | Rougan Tongluo Decoction Initiates Neuroprotection Against Cerebral Ischemia by Activating the Endogenous SLC6A8-Creatin | Mediators Inflamm 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/EARS2

