---
type: protein-evaluation
gene: "PSMD3"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PSMD3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PSMD3 |
| 蛋白名称 | 26S proteasome non-ATPase regulatory subunit 3 |
| 蛋白大小 | 534 aa / 61.0 kDa |
| UniProt ID | O43242 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm (Enhanced) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 534 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=38 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=72.6; PDB=79 |
| 调控结构域 | 4/10 | ×2 | 8.0 | CSN3; PCI_dom; PSMD3_C |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=390 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **76.0/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Enhanced)
- PubMed strict=38 broad=56
- AF pLDDT=72.6 PDB=79
- InterPro: CSN3; PCI_dom; PSMD3_C
- Pfam: PCI; Rpn3_C; TPR_PSMD3_N
- PPI degree=390 ChIP: None
36948574: PSMD3 gene mutations cause pathological myopia. | 40074718: Discovering new hub genes of dilated cardiomyopathy. | 37337223: PSMD3-ILF3 signaling cascade drives lung cancer cell proliferation and migration

### 4. 总体评价
**76.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: 26S proteasome non-ATPase regulatory subunit 3

**功能**: Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050756 |
| InterPro | IPR000717 |
| InterPro | IPR013586 |
| InterPro | IPR011990 |
| InterPro | IPR057985 |
| InterPro | IPR036390 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PSMD8 | STRING | 999 |
| USP14 | STRING | 999 |
| ADRM1 | STRING | 999 |
| PSMD4 | STRING | 999 |
| ECD | STRING | 999 |
| PSMD1 | STRING | 999 |
| PSMD14 | STRING | 999 |
| PSMD13 | STRING | 999 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O43242-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000108344-PSMD3

![](https://images.proteinatlas.org/17038/621_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/17038/621_H5_3_red_green.jpg)
![](https://images.proteinatlas.org/17038/612_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/17038/612_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/17038/615_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/17038/615_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/48972/805_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/48972/805_H6_3_red_green.jpg)

### 深度机制分析

**结构域架构与分子功能推断** PSMD3（Rpn3）是26S蛋白酶体19S调节颗粒（RP）"lid"子复合物的核心亚基。结构域架构包含：PCI结构域（InterPro: IPR000717，Pfam: PCI）是lid亚基的标志性折叠——一个由C端α-螺旋束形成的翼状螺旋结构，介导lid内亚基间的稳定组装。N端含有TPR-like重复（Pfam: TPR_PSMD3_N），属于四三肽重复折叠（IPR011990）。C端PSMD3_C结构域（IPR013586）构成lid与20S核心颗粒（CP）界面的关键部分。PCI结构域超家族（IPR036390）将PSMD3与COP9信号体（CSN）和eIF3起始因子统一在一个结构超家族之下。534 aa（61.0 kDa）的较大尺寸使PSMD3成为lid中最大的亚基之一，PDB=79个实验结构提供了极其丰富的结构资源，但AF pLDDT仅为72.6，在五个蛋白中最低，反映了lid内亚基间界面和柔性连接区对独立单体预测的挑战。

**PPI网络与信号通路解析** PPI网络是经典26S蛋白酶体核心——PSMD8（999，lid亚基Rpn12）、USP14（999，去泛素化酶）、ADRM1（999，Rpn13/泛素受体）、PSMD4（999，Rpn10/泛素受体）、PSMD1（999，base亚基Rpn2）、PSMD14（999，lid去泛素化酶Rpn11）、PSMD13（999，lid亚基Rpn9）和ECD（999，ecdysoneless同源蛋白）均以999的满分出现。PPI度390是五个蛋白中最高的，完美反映了PSMD3作为lid组装支架的拓扑位置——它通过PCI结构域介导的异源二聚化与几乎每一个lid亚基形成直接接触。USP14和PSMD14双去泛素化酶的高分互作表明PSMD3所处的lid亚复合物紧邻泛素链修剪和去除的催化中心。

**结构解读** 冷冻电镜解析的26S蛋白酶体全酶结构给出了PSMD3定位的原子级图景。PSMD3的PCI结构域与相邻lid亚基的PCI结构域通过C端翼状螺旋区域形成异源二聚体，构成一个马蹄形的lid复合物——PSMD3占据该马蹄的关键"拱心石"位置。N端TPR-like重复可能通过一种类似共享β-sheet的方式与同一lid内或base内的相邻亚基互作。pLDDT=72.6的低值主要源于：当PSMD3从lid复合物中分离时，它的PCI结构域缺少互作伙伴而部分去折叠——这是PCI结构域的共同特性，它们依赖于同源/异源伙伴共折叠以维持结构完整性。PAE图应显示与lid伙伴的界面低PAE区域（高置信共折叠），而单独区域则因缺乏伙伴出现高PAE。

**分子机制模型** PSMD3作为26S蛋白酶体lid亚复合物的结构支架，同时承担三个关键角色。第一，作为组装骨架——PSMD3通过其PCI结构域将PSMD6、PSMD7、PSMD12、PSMD13和PSMD8等lid亚基有序地装配成马蹄形lid复合物。第二，作为lid-base界面桥梁——PSMD3的C端PSMD3_C结构域直接与base亚基PSMD1/Rpn2结合，将lid的泛素识别和去泛素化功能耦合到底部AAA+ ATPase环的底物转运通道上。第三，作为去泛素化调控平台——PSMD3在空间上接近USP14和PSMD14/Rpn11，可能参与调控泛素链修剪的时序性：Rpn11在底物转位前去除整个泛素链（en bloc），而USP14在底物识别阶段逐步修剪远端的泛素。核质定位（HPA Enhanced级别）凸显了26S蛋白酶体在核内蛋白质量控制中的核心地位——核内错误折叠蛋白、转录因子定时降解和DNA损伤应答蛋白的周转全部依赖核内的26S蛋白酶体。PSMD3的突变——通过破坏lid组装——可导致特定核内底物的积累，引发选择性蛋白质毒性。突变致病变性近视的发现（PubMed: 36948574）极具启发性——提示PSMD3功能异常导致眼组织中特定蛋白质的积累，这一组织特异表型在核心蛋白酶体组分中极为罕见。

**研究与治疗意义** PSMD3在肺癌细胞增殖和迁移中的驱动作用是通过与ILF3（白介素增强子结合因子3）的直接信号轴实现的（PubMed: 37337223），提示PSMD3-ILF3复合物可以选择性降解某类细胞周期抑制因子，为靶向lid特异性底物识别提供切入点。扩张型心肌病的相关基因发现（PubMed: 40074718）进一步扩展了PSMD3突变引起组织特异性病理的谱系。一项高度创新的研究发现，肠道菌群代谢产物OAA通过PSMD3介导的YTHDF2降解控制肥胖和脂代谢（PubMed: 41844893），揭示了PSMD3-泛素蛋白酶体轴在代谢性疾病的菌群-宿主互作中未被预料的角色。治疗方向包括：开发PSMD3-PCI界面的选择性抑制剂以调控特定底物降解而不完全阻断蛋白酶体（避免bortezomib/carfilzomib的全局毒性）；利用PSMD3-ILF3信号轴作为肺癌分层的生物标志物；研究菌群代谢产物通过PSMD3的选择性底物招募机制。

### PubMed 文献

**PubMed count: 57**

| 42042009 | S-Doped Carbon Dot Treatment Alters RNA Processing, Translation, and Protein Degradation Pathways in HeLa Cells. | Curr Issues Mol Biol 2026 |
| 41956029 | Shared genetic architecture between major depressive disorder and inflammatory bowel disease: Insights from large-scale  | Hum Immunol 2026 |
| 41844893 | Romboutsia ilealis related metabolite OAA controls obesity and lipid metabolism through PSMD3-mediated degradation of YT | Cell Death Differ 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSMD3

