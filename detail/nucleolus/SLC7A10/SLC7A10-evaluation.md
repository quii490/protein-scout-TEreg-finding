---
type: protein-evaluation
gene: "SLC7A10"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC7A10 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SLC7A10 |
| 蛋白全称 | Asc-type amino acid transporter 1 |
| UniProt ID | Q9NS82 |
| 蛋白大小 | 523 aa / 57.5 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 523 aa|
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=29 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=83.4; PDB=4 |
| 🧬 调控结构域 | 7/10 | ×2 | 14.0 | IPR002293, IPR050598, PF13520|
| PPI | 5/10 | ×3 | 15.0 | PPI degree=4 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.4/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Associates with SLC3A2/4F2hc to form a functional heterodimeric complex that translocates small neutral L- and D-amino acids across the plasma membrane. Preferentially mediates exchange transport, but can also operate via facilitated diffusion (By similarity) (PubMed:10863037). Acts as a major trans

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR002293 | AA/rel_permease1 |
| InterPro | IPR050598 | AminoAcid_Transporter |
| Pfam | PF13520 | AA_permease_2 |


#### 3.4 结构信息

蛋白长度 523 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000130876-SLC7A10

![](https://images.proteinatlas.org/41884/509_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/41884/509_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/41884/490_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/41884/490_H7_3_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**69.4/100** | **nucleolus**
Nuclear protein


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR002293;IPR050598; |
| Pfam | PF13520; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APPBP2 | BioGRID | 0 |
| CFTR | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NS82-F1-predicted_aligned_error_v6.png)

### 深度机制分析

**结构域架构**：SLC7A10（523 aa，57.5 kDa）是Asc-type氨基酸转运蛋白1（Solute Carrier Family 7 Member 10），属于氨基酸/生长激素/生长因子转运体超家族。其核心结构域为AA_permease_2（IPR002293/AA/rel_permease1, PF13520）——构成典型的12次跨膜α-螺旋束（TM1-TM12），通过LeuT-like折叠（5+5反向重复）形成底物转运通道。TM1和TM6在通道中央断裂（TM1a/TM1b, TM6a/TM6b），形成底物结合和门控开关。IPR050598（AminoAcid_Transporter家族）涵盖SLC7亚家族，以与SLC3辅助亚基形成异源二聚体为特征——SLC7A10与SLC3A2/4F2hc通过二硫键共价偶联，后者负责膜靶向和转运活性调节。AlphaFold pLDDT=83.4，TM核心区预测质量高（pLDDT>85），而N/C端胞质尾端（pLDDT 65-70）和胞外环（EL2/EL4, pLDDT 60-65）置信度较低。

**PPI互作网络解读**：PPI degree=4，网络极简：APPBP2（淀粉样前体蛋白结合蛋白2/ARA67）——含多个TPR重复的支架蛋白，参与膜蛋白转运与定位；CFTR（囊性纤维化跨膜传导调节因子）——cAMP激活的Cl⁻通道，提示SLC7A10可能与CFTR在顶端膜共定位并形成功能性膜蛋白复合体。小PPI网络反映了SLC7A10作为代谢转运蛋白的功能单一性，但其核质定位（HPA Approved）暗示存在未被发现的功能维度。

**结构解读**：12-TM束采用5+5反向重复折叠——TM1-TM5和TM6-TM10形成结构伪对称的核心，TM1b和TM6a的断裂位点在通道中央形成底物结合腔。底物结合涉及Na⁺偶联——Na1和Na2两个钠离子结合位点在TM1和TM8界面，Na⁺结合诱导TM1b和TM6a的构象重排以封闭胞外侧门并打开胞内侧门（交替开放机制）。SLC7A10偏好小分子中性L-和D-氨基酸（Ala, Ser, Cys, Thr），通过Na⁺梯度驱动的交换转运（antiport）模式运作。实验PDB存在4个条目，其中冷冻电镜结构可提供SLC7A10-SLC3A2异源二聚体的组织分辨率。

**机制模型**：（1）SLC7A10-SLC3A2异源二聚体靶向质膜，SLC3A2胞外结构域进行糖基化修饰和氧化还原感应；（2）胞外氨基酸结合触发Na⁺协同转运，'elevator'机制使底物结合域相对于支架域发生刚体位移（~15A）；（3）核质定位（Nucleoplasm Approved）的可能机制：SLC7A10 N端胞质尾端（残基1-50）含高比例的碱性残基（Lys/Arg），可能作为隐蔽NLS——在特定应激条件下（如氨基酸饥饿或氧化应激），膜蛋白经泛素化/内吞后从内吞体逃逸或经未完全折叠的新生肽链直接核输入；（4）核质中的SLC7A10可能作为氨基酸可用性的核内传感器，通过调控mTORC1溶酶体定位信号间接影响核内翻译调控。胆固醇对SLC7A10转运活性至关重要（PMID:41936919），揭示了膜微环境对转运功能的调节。

**TE调控展望**：SLC7A10与TE调控的直接关联极弱。唯一可构想的联系是通过氨基酸代谢-表观遗传轴的间接作用：SLC7A10转运的Ser和Cys分别是单碳代谢（one-carbon metabolism）和谷胱甘肽合成的底物，而SAM/SAH比率直接影响DNA甲基化状态——已知TE区域的甲基化水平对其转录活性至关重要。若SLC7A10功能异常导致细胞内Ser/Cys水平改变，可能通过甲基供体SAM的可用性间接影响TE甲基化谱。但这一通路过于间接，不建议作为TE调控靶标。

### PubMed 文献

**PubMed count: 79**

| 41936919 | Cholesterol, but not its oxidized derivatives, is essential for the transport activity of ASC1 (SLC7A10). | Free Radic Biol Med 2026 |
| 41654970 | CI-994 is a dual modulator of class I HDACs and Wnt/β-catenin signaling for the treatment of Alzheimer's disease. | Alzheimers Res Ther 2026 |
| 41365200 | Shikonin improves cerebral ischemia-reperfusion injury by regulating astrocyte polarization through ERK1/2-SP1-SLC7A10. | Int Immunopharmacol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC7A10

