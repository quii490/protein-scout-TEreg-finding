---
type: protein-evaluation
gene: "NRDC"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NRDC 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NRDC |
| 蛋白名称 | Nardilysin |
| 蛋白大小 | 1151 aa / 131.7 kDa |
| UniProt ID | O43847 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 1151 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=29 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=82.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Metalloenz_LuxS/M16; Pept_M16_N; Pept_M16_Zn_BS |
| PPI | 5/10 | x3 | 15.0 | PPI degree=3 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=29 broad=137
- AF pLDDT=82.6 PDB=0
- InterPro: Metalloenz_LuxS/M16; Pept_M16_N; Pept_M16_Zn_BS
- Pfam: Peptidase_M16; Peptidase_M16_C; Peptidase_M16_M
- PPI degree=3 ChIP: None
35236897: Nardilysin in adipocytes regulates UCP1 expression and body temperature homeosta | 38096617: Nardilysin determines hematopoietic stem cell fitness by regulating protein synt | 41046976: Exercise training-induced extracellular miR-136-3p modulates glucose uptake and 

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Nardilysin

**功能**: Cleaves peptide substrates on the N-terminus of arginine residues in dibasic pairs. Is a critical activator of BACE1- and ADAM17-mediated pro-neuregulin ectodomain shedding, involved in the positive regulation of axonal maturation and myelination. Required for proper functioning of 2-oxoglutarate dehydrogenase (OGDH) (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011249 |
| InterPro | IPR011765 |
| InterPro | IPR001431 |
| InterPro | IPR050626 |
| InterPro | IPR007863 |
| InterPro | IPR032632 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

NRDC（Nardilysin）的深度机制围绕其M16金属蛋白酶的催化架构展开。该蛋白拥有1,151 aa的大分子量（131.7 kDa），整合了三个结构域模块：N端Peptidase_M16（Pfam PF00675）和C端Peptidase_M16_C（Pfam PF05193）共同构成催化核心，底部M16_M结构域（Pfam PF08367）提供底物识别和结构支撑。InterPro注释进一步将此架构细化为Metalloenz_LuxS/M16超家族（IPR011249）、Pept_M16_N（IPR011765）和Pept_M16_Zn_BS（IPR001431）。催化机制依赖两个Zn²⁺离子协同作用，在双碱性位点（dibasic pair）的Arg/Lys残基N端进行选择性水解。AlphaFold v6预测pLDDT=82.6显示出整体上较为可靠的折叠预测，但1,151个残基的长度意味着结构域间长程连接区段的柔性会导致局部区域置信度下降，需要PAE图进行区域级别的质量判断。0个PDB实验结构表明NRDC是纯预测模型，所有机制推断均需实验验证。

NRDC的PPI网络很小（degree=3），但伙伴的功能指向性极为明确。STRING中SETX（senataxin, score=956）是一个深度嵌入核内环境的RNA/DNA解旋酶——SETX定位于核质和核仁，参与转录终止、R-loop解旋和DNA损伤应答，其失活导致共济失调伴动眼神经失用症2型（AOA2）和肌萎缩侧索硬化症4型（ALS4）。NRDC与SETX的极高分STRING评分暗示两者不仅在物理上紧密结合，且在进化上共发生。SETX的R-loop功能提供了NRDC潜在TE调控的最直接桥梁——R-loop是转录过程中形成的RNA:DNA杂合链+置换单链DNA的三链结构，而TE序列富含的重复结构极易在转录时形成稳定的R-loop。若NRDC通过SETX参与R-loop的解旋或加工，它对TE位点的R-loop积累和基因组不稳定性就有间接调控作用。ADAP1（score=799）作为ArfGAP和锚蛋白重复蛋白，提供了膜信号与胞内运输的连接，与NRDC核定位的关联尚不明确。

NRDC的文献积累（PubMed strict=29, broad=137）覆盖了从能量代谢到干细胞生物学到运动生理学的广泛领域，但核内功能尤其是染色质/TE关联几乎为空白。PMID:35236897揭示NRDC在脂肪细胞中调控UCP1表达和体温稳态，UCP1是棕色脂肪组织的线粒体解偶联蛋白——这条信号轴的核内中间步骤（代谢信号→转录因子→UCP1启动子）完全未被解析，NRDC很可能在其中扮演上游信号传导者的角色。PMID:38096617的核心发现——NRDC通过调控蛋白质合成决定造血干细胞适应性——更为关键，因为它暗示NRDC的底物可能包括转录因子或翻译调控因子的蛋白水解激活（或失活），而不仅仅是传统认知的细胞外肽类激素的加工。

NRDC作为核质蛋白在TE调控中的理论角色定位为"蛋白水解信号中继站"。HPA标注Nucleoplasm（Approved，得分9/10）且PubMed新颖性极高（29篇，得分9/10），是该候选蛋白最大的结构优势。具体模型为：核质内NRDC→水解切割转录因子/共调控因子（可能的底物包括SETX相关的蛋白或R-loop结合蛋白）→释放活性片段→调控目标基因转录→间接影响TE沉默或去抑制。但此模型中存在严重的证据缺口：(1) NRDC在核内的直接底物尚未被鉴定（所有已知底物均为分泌型或膜蛋白）；(2) NRDC的水解活性是Zn²⁺依赖的，核内游离Zn²⁺浓度是否足以支持其活性需要验证；(3) 缺乏任何ChIP-seq/CUT&RUN或核内蛋白质组数据。NRDC的TE调控价值主要取决于未来是否能鉴定出其核内的直接底物，这需要N-terminomics（如TAILS或COFRADIC）等降解组学方法的介入。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SETX | STRING | 956 |
| ADAP1 | STRING | 799 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O43847-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000078618-NRDC

![](https://images.proteinatlas.org/53661/870_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/53661/870_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/53661/879_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/53661/879_G2_3_red_green.jpg)
![](https://images.proteinatlas.org/53661/872_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/53661/872_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/53661/905_G10_4_red_green.jpg)
![](https://images.proteinatlas.org/53661/905_G10_6_red_green.jpg)

### PubMed 文献

**PubMed count: 137**

| 42295608 | System-level evaluation of 5G standalone communication infrastructure for robotic telesurgery. | Int J Comput Assist Radiol Surg 2026 |
| 42287472 | Lactation Interrupted: PFAS Impact on Capacity to Breastfeed Ignored. | Curr Environ Health Rep 2026 |
| 42166398 | Elevated Serum Nardilysin Is Inversely Associated with Cardiovascular Disease in Kidney Transplant Recipients. | Kidney Blood Press Res 2026 |
### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NRDC

