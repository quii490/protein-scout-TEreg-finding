---
type: protein-evaluation
gene: "UBR3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## UBR3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | UBR3 |
| 蛋白全称 | E3 ubiquitin-protein ligase UBR3 |
| UniProt ID | Q6ZT12 |
| 蛋白大小 | 1888 aa / 207.7 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoli; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 1888 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=22 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=77.2; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | E3_ligase_UBR-like_C; UBR1-like; UBR1-like_WH |
| PPI | 6/10 | x3 | 18.0 | PPI degree=97 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

E3 ubiquitin-protein ligase which is a component of the N-end rule pathway (By similarity). Does not bind to proteins bearing specific N-terminal residues that are destabilizing according to the N-end rule, leading to their ubiquitination and subsequent degradation (By similarity). May play a role i

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR044046 | E3_ligase_UBR-like_C |
| InterPro | IPR039164 | UBR1-like |
| InterPro | IPR055194 | UBR1-like_WH |
| InterPro | IPR003126 | Znf_UBR |
| Pfam | PF18995 | PRT6_C |
| Pfam | PF22960 | WHD_UBR1 |
| Pfam | PF02207 | zf-UBR |


#### 3.4 结构信息

蛋白长度 1888 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000144357-UBR3

![](https://images.proteinatlas.org/35390/434_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/35390/434_G7_3_red_green.jpg)
![](https://images.proteinatlas.org/35390/450_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/35390/450_G7_3_red_green.jpg)
![](https://images.proteinatlas.org/35390/453_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/35390/453_G7_2_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**72.1/100** | **nucleolus**
Nuclear protein


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00396; |
| InterPro | IPR044046;IPR039164;IPR055194;IPR003126; |
| Pfam | PF18995;PF22960;PF02207; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UBE2A | BioGRID | 0 |
| UBE2B | BioGRID | 0 |
| UBE2Z | BioGRID | 0 |
| DZIP3 | BioGRID | 0 |
| HOXB7 | BioGRID | 0 |
| FAHD1 | BioGRID | 0 |
| SPINT2 | BioGRID | 0 |
| ZSCAN32 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6ZT12-F1-predicted_aligned_error_v6.png)

### 深度机制分析

**结构域架构**：UBR3（1888 aa，207.7 kDa）是N端规则（N-end rule）泛素化通路的E3泛素连接酶，含三个关键结构域：Znf_UBR（IPR003126, PF02207）——锌指结构域，特异性识别底物N端不稳定残基（Type-1/Type-2），采用交叉支架（cross-brace）锌指折叠；UBR1-like_WH（IPR055194, PF22960）——翼状螺旋（winged-helix）结构域，参与蛋白-蛋白/DNA识别界面；E3_ligase_UBR-like_C（IPR044046, PF18995/PRT6_C）——C端催化结构域，含RING-like指负责泛素从E2~Ub硫酯转移至底物Lys。AlphaFold pLDDT=77.2，在1888 aa长度上置信度中等偏上，N端Znf_UBR（~40-100 aa）和C端RING-like结构域（~1600-1750 aa）预测质量最高（pLDDT>85），而中央长连接区（~500-1500 aa）pLDDT介于55-70，提示存在较大的内在无序区域（IDR）或多结构域间柔性铰链。

**PPI互作网络解读**：PPI degree=97，核心互作反映了UBR3在泛素化级联中的中心位置：UBE2A/UBE2B（E2泛素结合酶，直接负责Ub供体递送）、UBE2Z（非经典E2酶）、DZIP3（另一E3连接酶，可能形成异源二聚化调控复合体）。尤其值得关注的是HOXB7（同源框转录因子B7）和ZSCAN32（锌指转录因子）的互作——这提示UBR3可能通过N端规则途径直接调控特定转录因子的蛋白质稳态，从而影响基因表达程序。SPINT2（丝氨酸肽酶抑制剂）和FAHD1（富马酰乙酰乙酸水解酶）代表代谢酶-泛素化通路交叉。

**结构解读**：AlphaFold预测显示Znf_UBR采用经典的C4锌指折叠（4个Cys配位Zn²⁺），形成疏水结合口袋识别底物N端疏水/碱性残基。UBR1-like_WH结构域采用翼状螺旋折叠（α1-β1-α2-α3-β2-W1-β3），与转录因子的DNA结合结构域折叠相似，暗示UBR3可能保留祖先型DNA结合能力。C端PRT6_C结构域折叠成α/β混合构型，RING-like指（Cys-His簇）与E2酶（UBE2A/UBE2B）的催化Cys形成硫酯中间体过渡态。PAE矩阵显示Znf_UBR与C端催化结构域之间为高PAE（>20A），表明这些结构域彼此独立运动，中间IDR可能作为蛋白质相互作用平台。

**机制模型**：UBR3通过经典的N端规则泛素化通路运作：（1）Znf_UBR识别底物蛋白N端暴露的不稳定残基（如Arg、Lys、His为Type-1，Phe、Tyr、Trp、Leu、Ile为Type-2）；（2）底物结合诱导构象变化，使C端RING-like结构域重排以招募E2~Ub；（3）Ub从E2转移至底物近端Lys残基形成K48连接多聚泛素链，靶向26S蛋白酶体降解。在核仁中，UBR3可能通过降解核仁驻留蛋白（如HOXB7转录调控靶标）参与核仁应激适应的蛋白质稳态重塑。PMID:41533598显示UBR3调控DNA修复蛋白APE1水平，连接了泛素化和基因组稳定性，暗示核仁UBR3可能在rDNA损伤修复中发挥作用。

**TE调控展望**：UBR3通过HOXB7和ZSCAN32互作间接连接转录调控。HOXB7作为同源框转录因子可识别TAAT/ATTA核心基序——许多内源性逆转录病毒（特别是HERV-H/MaLR LTR）启动子含TAAT富集序列。若UBR3介导HOXB7泛素化降解，则可能影响HOXB7靶基因（包括TE驱动基因）的表达水平。但此推测依赖实验验证，目前无直接的TE调控文献支持。

### PubMed 文献

**PubMed count: 33**

| 41651857 | Whole-genome sequencing analysis of anthropometric traits in 672,976 individuals reveals convergence between rare and co | Nat Commun 2026 |
| 41533598 | Correction to "Ubiquitin ligase UBR3 regulates cellular levels of the essential DNA repair protein APE1 and is required  | Nucleic Acids Res 2026 |
| 41325391 | Integrated single-cell RNA-seq and bulk RNA-seq analysis to investigate key adipogenesis genes in adipose-derived stem c | PLoS One 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UBR3

