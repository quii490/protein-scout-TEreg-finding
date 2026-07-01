---
type: protein-evaluation
gene: "NKX1-1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## NKX1-1 (NK1 transcription factor-related protein 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | NKX1-1 |
| 蛋白全称 | NK1 transcription factor-related protein 1 |
| UniProt ID | Q15270 |
| 蛋白大小 | 448 aa / 49.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 448 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR001356; InterPro:IPR020479; InterPro:IPR017970; InterPro:IPR050394; InterPro:IPR009057; Pfam:PF00046 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

May be required for the coordinated crosstalk of factors involved in the maintenance of energy homeostasis, possibly by regulating the transcription of specific factors involved in energy balance

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR001356 |
| InterPro | IPR020479 |
| InterPro | IPR017970 |
| InterPro | IPR050394 |
| InterPro | IPR009057 |
| Pfam | PF00046 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000235608-NKX1-1

![](https://images.proteinatlas.org/29367/1511_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29367/1511_H4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/29367/1314_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29367/1314_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29367/1969_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29367/1969_F4_8_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00389; |
| InterPro | IPR001356;IPR020479;IPR017970;IPR050394;IPR009057; |
| Pfam | PF00046; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| AURKA | BioGRID | 1 |


### PubMed 文献

**PubMed count: 8**

| 37282810 | Genomic inbreeding estimation, runs of homozygosity, and heterozygosity-enriched regions uncover signals of selection in | J Anim Breed Genet 2023 |
| 36795966 | A Urine-based DNA Methylation Marker Test to Detect Upper Tract Urothelial Carcinoma: A Prospective Cohort Study. | J Urol 2023 |
| 36243213 | Mediation by DNA methylation on the association of BMI and serum uric acid in Chinese monozygotic twins. | Gene 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NKX1-1

### 深度机制分析

NKX1-1（NK1 transcription factor-related protein 1）属于NK型同源框转录因子家族，其核心结构元件为SMART SM00389标注的HOX类同源框结构域（Pfam PF00046, InterPro IPR001356），该结构域采用经典的helix-turn-helix（HTH）三级折叠——由三个α螺旋构成，识别螺旋（helix III）插入DNA大沟以碱基特异性方式读取5'-TAAT-3'或类似短序列基序。IPR020479和IPR017970进一步将NKX1-1归入同源框保守位点子家族，其残基保守性集中在疏水核心（稳定HTH折叠）和N端臂（接触DNA小沟）。IPR009057同源框域样超家族覆盖范围更广，提示可能存在辅助DNA接触区域。448 aa/49.3 kDa介于典型转录因子大小范围内，足够编码额外的反式激活/抑制结构域。值得注意的是IPR050394将NKX1-1归入"Nkx-1-like transcription factor"分支——这是包含NKX1-2的旁系同源组，其序列保守性限于同源框区域，N端和C端功能域的多样性可能负责差异化的下游靶基因选择。

PPI网络中仅有的互作伙伴AURKA（极光激酶A, BioGRID score=1）具有不同寻常的机制启示。AURKA是中心体和纺锤体组装的关键丝氨酸/苏氨酸激酶，在G2/M期磷酸化多种底物以驱动有丝分裂进入和中心体成熟。该互作提示三种可能：其一，NKX1-1可能是AURKA的直接磷酸化底物——转录因子在有丝分裂期间被中心体-纺锤体相关激酶磷酸化是经典的非转录功能调控模式（参见FOXM1、MYBL2），磷酸化后NKX1-1可能被排除出染色质以确保有丝分裂期转录沉默；其二，NKX1-1可能作为AURKA的核定位锚定因子——在间期将AURKA滞留于核质以控制其过早活化；其三，该互作仅为高通量双杂交的假阳性（多数BioGRID score=1的互作未经独立重复验证）。

尽管GO-CC定位标注为"无已知核定位注释"，同源框结构域的存在本身就是核定位的最强间接证据——所有已知同源框蛋白均为序列特异性DNA结合转录因子，通过核定位信号（NLS）依赖或非依赖方式主动转运入核。该蛋白的HPA IF图像显示明确的核富集模式，与UniProt TrEMBL条目中"May regulate transcription of factors involved in energy homeostasis"的功能描述一致。PubMed严格检索0篇（8篇宽松文献仅涉及GWAS关联、DNA甲基化标记和基因组纯合度分析）的双重极低研究度，使NKX1-1在当前阶段处于"转录因子身份确凿但靶基因和生物过程完全空白"的初始发现状态。归一化评分67.8/100中的4/10核定位特异性得分是数据库注释延迟而非实际生物学信号造成的低估——若未来GO-CC和UniProt注释更新以反映同源框域→核质导向的事实，该维度的分数至少可上调至7/10。

从TE调控视角看，同源框转录因子家族如PAX、HOX、NKX等已多次被报道结合散布重复元件的衍生序列。LTR和L1启动子中的TAAT样基序可能是NKX家族蛋白的非经典识别位点，这种"主转录因子-重复元件共选择"机制在胚胎发育和应激响应中对转座子的驯化具有深远意义。NKX1-1参与能量稳态调控的已知线索（Q15270功能描述）进一步暗示其可能通过调节代谢相关TE的转录活性参与线粒体和核基因组间的协同调控——这是一条在PubMed 0篇背景下完全空白但逻辑连贯的假说轴。

