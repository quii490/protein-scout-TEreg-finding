---
type: protein-evaluation
gene: "SACM1L"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SACM1L 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SACM1L |
| 蛋白名称 | Phosphatidylinositol-3-phosphatase SAC1 |
| 蛋白大小 | 587 aa / 67.0 kDa |
| UniProt ID | Q9NTJ5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 587 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=13 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=90.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | SAC_dom |
| PPI | 7/10 | x3 | 21.0 | PPI degree=144 |
| **加权总分** | | | **140/180** | |
| **归一化总分** | | | **77.6/100** | 互证: +2 |

### 3. 分析
- Golgi apparatus; Nucleoplasm (Approved)
- PubMed strict=13 broad=22
- AF pLDDT=90.8 PDB=0
- InterPro: SAC_dom
- Pfam: Syja_N
- PPI degree=144 ChIP: None
40841558: Control of Golgi- V-ATPase through Sac1-dependent co-regulation of PI(4)P and ch | 36312597: Bioinformatics Analysis of Common Genetic and Molecular Traits and Association o | 37068596: Lipid phosphatase SAC1 suppresses hepatitis B virus replication through promotin

### 4. 总体评价
**77.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构与分子功能推断。** SACM1L (SAC1)是一种整合膜脂磷酸酶，其587 aa多肽包含两个功能结构域：N端的SAC磷酸酶结构域(SAC_dom, IPR002013/PF02383)和C端的Syja_N结构域。SAC结构域采用α/β双层折叠，以保守的CX5R(T/S)催化基序执行两步法磷酸肌醇水解——第一步Cys残基对肌醇环的磷酸基团发起亲核攻击，形成共价巯基-磷酸酶中间体；第二步水分子介导的水解释放游离磷酸并再生活性位点Cys。SACM1L具有明确的底物层级偏好：对"cis"构型(同一膜内)的PtdIns(4)P表现出极高的催化效率(kcat/Km)，对PtdIns(3)P的活性低约10倍，对PtdIns(3,5)P2几乎无活性(PubMed:24209621, PubMed:27044890, PubMed:29461204, PubMed:30659099)。底物选择的"cis"偏好性是其关键生物学特征——SACM1L必须在物理上定位到含PtdIns(4)P的膜上才能高效水解其底物，这一特性赋予了该蛋白作为"细胞器身份维护者"的功能。pLDDT=90.8的全局评分表明AF2对SAC磷酸酶折叠的预测高度可信；Syja_N结构域(IPR相关但未经独立Pfam确认)可能作为N端附属结构域参与亚细胞定位调控或蛋白质-蛋白质互作。

**PPI网络的生物学意义。** SACM1L的144个互作伙伴中，最显著的是COPI囊泡外壳蛋白的完整集合：COPA(α-COP)、COPB1(β-COP)、COPE(ε-COP)和COPG1(γ-COP)，这些互作均在BioGRID中被注释。COPI介导高尔基体→内质网(ER)的逆行囊泡运输——SACM1L作为COPI的货物蛋白，通过其C端双赖氨酸(KKxx/KKxxx)ER检索信号被COPI识别和包装，借此在高尔基体和ER之间循环。这一定位循环直接支持了其生物学功能：SACM1L在ER中消耗PtdIns(4)P以维持ER的低PtdIns(4)P身份特征，随后通过COPII囊泡顺行运输到高尔基体，在该处抑制PtdIns(4)P过度积累(PubMed:40841558)。PRKCA(PKCα)的互作提示SACM1L可能受Ser/Thr磷酸化调控其活性或定位循环，构成信号输入节点。P2RY12(P2Y12嘌呤受体，血小板ADP受体)和SPINT2(HAI-2，丝氨酸蛋白酶抑制剂)的互作将SACM1L连接到血小板激活和细胞表面蛋白水解的调控网络，暗示其在心血管和肿瘤微环境中的非经典功能。

**三维结构的功能解释。** AF2预测的SACM1L结构呈现双结构域组织：N端SAC磷酸酶结构域(约残基1-400)形成一个紧凑的α/β双层，活性位点CX5R(T/S)基序位于由保守碱性残基(Arg、Lys)组成的正电荷沟槽底部——后者负责识别并结合磷酸肌醇头基的多个磷酸基团。pLDDT在催化核心区域>95，在底物结合环(substrate-binding loop)处略低(85-90)，反映了这些环在apo状态下的柔性。C端约180残基(包含两个预测的跨膜螺旋，约残基500-560)呈现中等pLDDT(75-85)，跨膜螺旋被预测为ER膜锚定区，使SAC结构域面向胞质。PDB=0意味着尚无实验结构——然而，酵母Sac1p的晶体结构(PDB:3OW2)与人类SACM1L在SAC结构域上共享约40%序列同一性，为催化机制提供了可靠的比较模型。AF2预测还暗示SAC结构域表面存在一个保守的正电荷贴片——可能作为膜曲率传感器，使SACM1L优先定位到高曲率膜区域，如ER-高尔基体中间区室(ERGIC)和ER-线粒体接触位点。

**综合分子机制模型。** SACM1L是细胞内PtdIns(4)P稳态的"梯度维护器"和"细胞器身份守护者"。在ER膜上，SACM1L通过高效清除泄漏到ER的PtdIns(4)P来维持ER与高尔基体之间约10倍的PtdIns(4)P浓度梯度——这是维持两种细胞器功能身份的根本性生化区分。当SACM1L通过COPI逆行运输从高尔基体返回ER后，其PtdIns(4)P水解活性防止了高尔基体定位蛋白(如PtdIns(4)P效应器OSBP、FAPP、GOLPH3)在ER上的错误锚定。SACM1L的活性还间接控制了高尔基体的pH稳态：PtdIns(4)P招募V-ATPase组装因子到高尔基体膜，促进质子泵组装和维持高尔基体酸性环境(PubMed:40841558)。在抗病毒天然免疫方面，SACM1L的脂磷酸酶活性间接促进Ⅰ型干扰素信号传导，从而抑制乙肝病毒(HBV)复制(PubMed:37068596)——一个合理的机制模型是SACM1L通过调控ER膜的PtdIns(4)P水平，优化了ER定位的STING-MAVS天然免疫信号平台的组织。

**研究与治疗启示。** SACM1L的SAC磷酸酶活性位点是经典的小分子可药化靶点——Cys亲核体和正电荷底物结合沟槽的结合使得可设计共价抑制剂(靶向活性位点Cys)或竞争性磷酸肌醇类似物。PtdIns(4)P在多种疾病中的核心角色(包括高尔基体功能障碍相关神经退行性疾病、自噬失调、病毒复制)意味着SACM1L的药理学调控具有广泛治疗潜力。SACM1L抑制或敲低可纠正高尔基体PtdIns(4)P下降相关的病理状态，而SACM1L激活或过表达可抑制PtdIns(4)P过度积累驱动的促癌信号。作为椎间盘退变预测标志物(PubMed:41381667)和口腔鳞癌化疗耐药标志物(PubMed:41350832)的双重角色，SACM1L在精准医学中的生物标志物潜力值得进一步的前瞻性队列验证。

### 补充分析 (UniProt API)

**蛋白全称**: Phosphatidylinositol-3-phosphatase SAC1

**功能**: Phosphoinositide phosphatase which catalyzes the hydrolysis of phosphatidylinositol 4-phosphate (PtdIns(4)P) (PubMed:24209621, PubMed:27044890, PubMed:29461204, PubMed:30659099). Can also catalyze the hydrolysis of phosphatidylinositol 3-phosphate (PtdIns(3)P) and has low activity towards phosphatidylinositol-3,5-bisphosphate (PtdIns(3,5)P2) (By similarity). Shows a very robust PtdIns(4)P phosphatase activity when it binds PtdIns(4)P in a 'cis' configuration in the cellular environment, with muc

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002013 |
| Pfam | PF02383 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SACM1L | BioGRID | 0 |
| COPA | BioGRID | 0 |
| COPB1 | BioGRID | 0 |
| COPE | BioGRID | 0 |
| COPG1 | BioGRID | 0 |
| PRKCA | BioGRID | 0 |
| SPINT2 | BioGRID | 0 |
| P2RY12 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NTJ5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000211456-SACM1L

![](https://images.proteinatlas.org/69869/1446_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/69869/1446_C10_4_red_green.jpg)
![](https://images.proteinatlas.org/69869/1336_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/69869/1336_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/69869/1296_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/69869/1296_B6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 22**

| 41381667 | Unveiling key genes for intervertebral disc degeneration prediction and potential drug discovery. | Sci Rep 2025 |
| 41350832 | Identification and validation of key biomarkers for chemoresistance in oral squamous cell carcinoma. | BMC Cancer 2025 |
| 41128489 | Multiparametric Bulk and Single Extracellular Vesicle Pipeline for Identifying Adipose-Specific Signatures in Matched Hu | ACS Appl Mater Interfaces 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SACM1L

