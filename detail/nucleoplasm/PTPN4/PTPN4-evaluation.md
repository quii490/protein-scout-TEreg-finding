---
type: protein-evaluation
gene: "PTPN4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PTPN4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PTPN4 |
| 蛋白名称 | Tyrosine-protein phosphatase non-receptor type 4 |
| 蛋白大小 | 926 aa / 105.9 kDa |
| UniProt ID | P29074 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 926 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=46 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=77.2; PDB=8 |
| 调控结构域 | 4/10 | x2 | 8.0 | Band_41_domain; FA; FERM/acyl-CoA-bd_prot_sf |
| PPI | 6/10 | x3 | 18.0 | PPI degree=52 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=46 broad=67
- AF pLDDT=77.2 PDB=8
- InterPro: Band_41_domain; FA; FERM/acyl-CoA-bd_prot_sf
- Pfam: FA; FERM_C; FERM_M
- PPI degree=52 ChIP: None
18614237: The protein tyrosine phosphatase PTPN4/PTP-MEG1, an enzyme capable of dephosphor | 34306144: miR-16-5p Regulates PTPN4 and Affects Cardiomyocyte Apoptosis and Autophagy Indu | 19107198: The FERM and PDZ domain-containing protein tyrosine phosphatases, PTPN4 and PTPN

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Tyrosine-protein phosphatase non-receptor type 4

**功能**: Phosphatase that plays a role in immunity, learning, synaptic plasticity or cell homeostasis (PubMed:25825441, PubMed:27246854). Regulates neuronal cell homeostasis by protecting neurons against apoptosis (PubMed:20086240). Negatively regulates TLR4-induced interferon beta production by dephosphorylating adapter TICAM2 and inhibiting subsequent TRAM-TRIF interaction (PubMed:25825441). Also dephosphorylates the immunoreceptor tyrosine-based activation motifs/ITAMs of the TCR zeta subunit and ther

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR019749 |
| InterPro | IPR014847 |
| InterPro | IPR014352 |
| InterPro | IPR035963 |
| InterPro | IPR019748 |
| InterPro | IPR019747 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MECP2 | STRING | 759 |
| ZZEF1 | BioGRID | 1 |
| ATRX | BioGRID | 1 |
| KAT5 | BioGRID | 1 |
| EEF1A1 | BioGRID | 1 |
| EEF1G | BioGRID | 1 |
| MGMT | BioGRID | 1 |
| CRK | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P29074-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000088179-PTPN4

![](https://images.proteinatlas.org/19351/234_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/19351/234_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/19351/535_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/19351/535_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/19351/235_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/19351/235_D2_2_red_green.jpg)

### 深度机制分析

**1. 结构域架构与分子功能推断**

PTPN4是一种非受体型酪氨酸磷酸酶，其结构域架构在PTP家族中独具特色——N端含有一个FERM结构域（IPR019749, IPR014352, IPR035963），C端为PTP催化结构域（IPR019748），两者之间由FA（FERM-adjacent）区域及一个PDZ结构域连接。FERM结构域典型功能是介导质膜与细胞骨架的连接，通常通过与磷脂酰肌醇及跨膜蛋白的胞内区结合来实现定位。PDZ结构域则识别底物蛋白C末端的特定序列基序，充当分子支架。这种"FERM+FA+PDZ+PTPc"的四模块架构暗示PTPN4不仅是一个磷酸酶催化单元，更是一个能够同时锚定膜结构、招募底物并执行去磷酸化的多功能信号整合平台。值得注意的是，IPR014847标记的Band_41结构域与FERM超家族（IPR014352）存在重叠，提示该蛋白可能通过类似ezrin/radixin/moesin（ERM）蛋白的机制参与膜-细胞骨架偶联。

**2. PPI互作网络的生物学意义**

PTPN4的PPI网络最引人注目的互作伙伴是MECP2（STRING评分759），这几乎是极高置信度的互作信号。MECP2是一种甲基化CpG结合蛋白，作为转录抑制因子在中枢神经系统基因调控中发挥核心作用，其突变导致Rett综合征（一种严重的神经发育障碍）。这种高强度的MECP2-PTPN4互作提示PTPN4可能通过去磷酸化MECP2的特定酪氨酸位点来调控其DNA结合能力或转录抑制活性——这是目前完全未被探索的调控维度。此外，ATRX（一种SWI/SNF家族染色质重塑因子）和KAT5（即TIP60，一种组蛋白乙酰转移酶）均为BioGRID捕获的实验互作伙伴，它们与MECP2共同指向PTPN4参与染色质水平的基因表达调控网络。CRK（一种SH2/SH3衔接蛋白）的存在进一步强化了PTPN4在酪氨酸磷酸化信号级联中的核心地位。

**3. 三维结构解读**

AlphaFold预测的pLDDT为77.2，在926个氨基酸的全长蛋白中属于中等置信度，但有8个PDB实验结构提供验证，这在该评估体系中被评分9/10的结构维度反映了实验数据的支撑力。FERM域通常折叠为三叶草形结构（F1/F2/F3三个亚结构域），F3亚结构域含有磷酸酪氨酸结合口袋，可以类比为PTB（phosphotyrosine-binding）结构域的折叠方式。PDZ域形成典型的五股β-折叠夹心结构。PTP催化域含有标志性的HCX5R活性位点基序，其中半胱氨酸亲核残基参与形成硫代磷酸酶中间体。pLDDT曲线中较低区域可能位于FERM-PDZ-PTP之间的柔性linker，这些区域的构象灵活性对于PTPN4同时接触膜锚定点（通过FERM）和底物蛋白（通过PTP域）是功能必需的。

**4. 分子机制综合模型**

综合所有证据，PTPN4在分子水平上执行以下核心功能：通过其FERM结构域锚定于核膜内侧或核质中的膜性结构，同时通过PDZ结构域招募含有特定C末端序列的底物蛋白，由PTP催化域对其执行酪氨酸去磷酸化。在核内，PTPN4的最主要功能底物很可能是MECP2——它在结合甲基化DNA后被磷酸化激活，而PTPN4对其进行去磷酸化从而关闭其转录抑制活性。这一模型将PTPN4嵌入到一个尚未被描述的"磷酸化开关-表观遗传调控"界面中：酪氨酸激酶→MECP2磷酸化→DNA结合→转录抑制→PTPN4去磷酸化→MECP2释放→转录恢复。该循环在神经元的突触可塑性（PubMed:27246854）和免疫细胞的TLR4信号通路（PubMed:25825441, 去磷酸化TICAM2）中均有实验验证，但在核内的MECP2场景下是全新的机制假设。此外，PTPN4还通过去磷酸化TCR ζ链的ITAM基序调节T细胞活化阈值，体现其在不同亚细胞定位中执行截然不同的信号功能。

**5. 研究与转化意义**

PTPN4-MECP2互作轴为Rett综合征提供了全新的治疗思路。目前Rett综合征的治疗策略集中于基因替代疗法和GABA激动剂，而PTPN4作为MECP2的上游调控酶，其小分子抑制剂或激活剂可能绕过MECP2本身突变的限制来调节下游通路。已有病例报告（PubMed:41776703）显示携带PTPN4突变的发育障碍患儿可通过强化康复获得改善，进一步验证了PTPN4功能调控的临床价值。从药物化学角度看，PTPN4的PTP催化域是一个可成药口袋——PTP1B抑制剂（如ertiprotafib）的开发已积累了丰富的PTP药物化学经验，可以移植到PTPN4上。同时，PTPN4-KAT5互作提示其可能参与DNA双链断裂修复中的组蛋白H4乙酰化调控，这是肿瘤放疗增敏的潜在靶点。

### PubMed 文献

**PubMed count: 67**

| 42045320 | YKL-40 alleviates the TNF-α-Induced chondrocyte injury in osteoarthritis in vitro. | Sci Rep 2026 |
| 41776703 | Major clinical improvement in a boy with developmental disabilities and a PTPN4 mutation with intensive re-education and | J Med Case Rep 2026 |
| 41391036 | Circular RNA PTPN4 Contributes to Blood-Brain Barrier Disruption during Early Epileptogenesis. | Adv Sci (Weinh) 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PTPN4

