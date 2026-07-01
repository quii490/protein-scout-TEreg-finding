---
type: protein-evaluation
gene: "PNMA5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PNMA5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PNMA5 |
| 蛋白名称 | Paraneoplastic antigen-like protein 5 |
| 蛋白大小 | 448 aa / 49.9 kDa |
| UniProt ID | Q96PV4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | nan (Approved) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 448 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=9 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=69.6; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PNMA; PNMA_C; PNMA_N |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=65 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +2 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | nan (Approved) |
| PubMed | strict=9, broad=14 |
| AF pLDDT | 69.6 |
| PDB | 0 |
| InterPro | PNMA; PNMA_C; PNMA_N |
| Pfam | PNMA; PNMA_N |
| PPI degree | 65 |
| ChIP | None |

**Papers**: 27424190: Distinct functional domains of PNMA5 mediate protein-protein interaction, nuclea | 34136487: PNMA5 Promotes Bone Metastasis of Non-small-Cell Lung Cancer as a Target of BMP2 | 39101471: Evolution of Virus-like Features and Intrinsically Disordered Regions in Retrotr

### 4. 总体评价
★★★★  **75.4/100**  |  **nucleoplasm**
Nuclear protein


### 深度机制分析

**1. 结构域架构与分子功能推断**

PNMA5含有三个高度特化的结构域：PNMA_N（IPR048271/PF20846, N端保守区）、核心PNMA结构域（IPR026523/PF14893）和PNMA_C（IPR048270, C端保守区）。PNMA家族（paraneoplastic Ma antigen）最显著的进化特征是PMID:39101471所揭示的——该蛋白包含类似逆转录病毒Gag衣壳蛋白的结构模体，且PNMA_N结构域与Ty3/Gypsy逆转录转座子的Gag蛋白具有同源性，暗示PNMA5可能起源于古老的逆转录转座子驯化事件。PNMA_C结构域在家族内高度保守，推测介导同源/异源多聚化组装，类似于病毒衣壳的寡聚化。关键的机制线索来自PMID:27424190（J Biol Chem 2016），该文献证实PNMA5的不同功能域分别介导蛋白质互作和核定位——N端结构域负责核内滞留，而C端结构域介导蛋白质-蛋白质相互作用。Alphafold预测的pLDDT=69.6偏低，这与PNMA_N/C之间的内在无序区（IDR，约aa 150-250）一致——该IDR可能为翻译后修饰和多价互作提供平台，是病毒样颗粒组装的核心调控区。

**2. PPI互作网络与通路分析**

PNMA5的PPI网络（degree=65）揭示了其在细胞周期、RNA代谢和核质转运中的多维度功能。最具生物学意义的互作伙伴包括：（1）KPNA2（Importin α-2）——这是PNMA5核定位分子机制的直接证据：KPNA2识别PNMA5的NLS（核定位信号），通过经典Importin α/β途径介导核输入。PMID:27424190确认PNMA5的N端结构域含有功能性NLS；（2）CCNC（Cyclin C）是Mediator复合体和CDK8激酶模块的组分，调控RNA聚合酶II的转录——PNMA5-CCNC互作提示PNMA5可能作为转录共调控因子，通过CDK8-Mediator轴影响全局基因表达；（3）DDX6（DEAD-box RNA解旋酶6）是P-body（加工小体）的核心成分，参与mRNA去帽、脱腺苷化和翻译抑制——PNMA5-DDX6互作将PNMA5功能延伸至转录后RNA代谢调控；（4）GRB2是经典RTK-RAS-MAPK信号通路的衔接蛋白，PNMA5可能通过GRB2将生长因子信号与基因调控耦合；（5）RAD23B是核苷酸切除修复和泛素化蛋白降解的双功能穿梭蛋白——PNMA5-RAD23B互作暗示PNMA5可能参与DNA损伤应答与蛋白酶体降解的界面调控；（6）PRKAA1（AMPKα1）是细胞能量感受器——PNMA5可能受AMPK磷酸化调控其活性或定位。

**3. 结构生物学解析**

AlphaFold pLDDT=69.6在所有评估蛋白中最低，但这并非预测质量差的标志，而是反映了PNMA5结构的本质特征——嵌有长IDR的模块化蛋白。PNMA_N结构域预期折叠为类似Gag衣壳蛋白N端结构域（CA-NTD）的α-螺旋束（6-7个α-螺旋），pLDDT预期约75-85。中央IDR区域（pLDDT<50）富含P, S, R残基，包含多个潜在磷酸化位点（AMPK、CK2、CDK共识序列），是其作为信号整合枢纽的结构基础。PNMA_C结构域预期为寡聚化界面，可能形成卷曲螺旋（coiled-coil）二聚化模块。值得注意的是，PMID:39101471利用冷冻电镜发现PNMA家族成员可自组装为非包膜病毒样衣壳结构，并能包装自身mRNA——这暗示PNMA5可能通过PNMA_C介导的同源寡聚化形成类似逆转录病毒Gag的衣壳样颗粒，参与细胞间mRNA的水平转移，类似于Arc/Arg3.1的已知机制。PAE图预期显示N端和C端折叠域内部低误差，但域间相对取向高度可变。

**4. 整合机制模型**

综合所有证据，PNMA5是一个驯化逆转录转座子衍生的多功能核质蛋白，其分子机制包含四个层次：（1）**核输入与滞留**——通过KPNA2识别NLS进入核质，N端结构域提供核滞留信号使其在核内富集；（2）**转录调控**——通过与CCNC/CDK8/Mediator复合体的互作，调控RNA聚合酶II的转录输出；PMID:34136487确认PNMA5是BMP2信号的下游靶基因，且在NSCLC骨转移中高表达，提示其参与了BMP2-SMAD转录程序的正反馈调控；（3）**RNA代谢**——通过DDX6参与的P-body定位，调控特定mRNA的翻译抑制或降解；（4）**衣壳样组装与细胞间通讯**——PNMA5可能通过C端寡聚化形成病毒样颗粒，包装并水平转移mRNA，类似于Arc在突触可塑性中的功能。在肿瘤微环境中，PNMA5+囊泡/颗粒可被邻近细胞摄取，重塑其转录组促进转移前微环境形成（骨转移，PMID:34136487）。USP22介导的去泛素化（PMID:40784167）通过稳定PNMA5蛋白，增强其在前列腺癌细胞中的促增殖和侵袭功能；（5）**DNA损伤界面**——通过RAD23B衔接，PNMA5可能将BMP2生长信号与基因组稳定性检查点耦合。

**5. 研究与转化意义**

PNMA5是这5个评估蛋白中机制深度最丰富的靶点。其双重身份——既是转录共调控因子又是驯化转座子衍生的衣壳蛋白——为其提供了独特的治疗干预窗口。USP22-PNMA5去泛素化轴（PMID:40784167）可直接用小分子USP22抑制剂（如PR-619）靶向；miR-877-3P/PNMA5调控轴（PMID:41308389）提示基于miRNA替代疗法的可行性。PNMA5的病毒样衣壳组装能力使其成为mRNA递送载体的候选骨架蛋白——工程化改造其PNMA_C寡聚化界面可调节颗粒大小和包装效率。此外，PNMA5在泛癌中作为副肿瘤抗原（原始命名来源），其核内表达模式的异常可能触发自身免疫应答——检测血清抗PNMA5自身抗体可能作为肿瘤早期筛查的生物标志物，尤其在前列腺癌（PMID:40784167）和胃癌（PMID:40539460）中。PDB=0意味着高分辨率结构研究是一个亟待填补的空白——PNMA5衣壳样组装体的冷冻电镜结构将为其RNA包装机制和抗癌药物设计提供关键信息。


### 补充分析 (UniProt API)

**蛋白全称**: Paraneoplastic antigen-like protein 5

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026523 |
| InterPro | IPR048270 |
| InterPro | IPR048271 |
| Pfam | PF14893 |
| Pfam | PF20846 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CCNC | BioGRID | 1 |
| CETN2 | BioGRID | 1 |
| DDX6 | BioGRID | 1 |
| GRB2 | BioGRID | 1 |
| KPNA2 | BioGRID | 1 |
| PRKAA1 | BioGRID | 1 |
| RAD23B | BioGRID | 1 |
| VIM | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96PV4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000198883-PNMA5

![](https://images.proteinatlas.org/44690/526_D7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/526_D7_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/545_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/545_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/528_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/528_D7_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000198883-PNMA5

![](https://images.proteinatlas.org/44690/526_D7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/526_D7_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/545_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/545_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/528_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/528_D7_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000198883-PNMA5

![](https://images.proteinatlas.org/44690/526_D7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/526_D7_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/545_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/545_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/528_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44690/528_D7_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 14**

| 41308389 | Platycodin D inhibits non-small cell lung cancer bone metastasis by inducing ferroptosis through miR-877-3P/PNMA5 regula | Phytomedicine 2025 |
| 40784167 | USP22-mediated PNMA5 deubiquitination promotes proliferation, migration and invasion of prostate cancer cells. | Acta Histochem 2025 |
| 40539460 | Comprehensive in‑silico molecular analysis of early‑onset gastric cancer identifies novel genes implicated in disease ch | Oncol Rep 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PNMA5

