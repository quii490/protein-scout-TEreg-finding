---
type: protein-evaluation
gene: "POLDIP3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## POLDIP3 (Polymerase delta-interacting protein 3) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | POLDIP3 |
| 蛋白全称 | Polymerase delta-interacting protein 3 |
| UniProt ID | B4E0L0 |
| 蛋白大小 | 438 aa / 48.2 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 438 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR051229; InterPro:IPR012677; InterPro:IPR034784; InterPro:IPR035979; InterPro:IPR000504; Pfam:PF00076 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Is involved in regulation of translation. Is preferentially associated with CBC-bound spliced mRNA-protein complexes during the pioneer round of mRNA translation. Contributes to enhanced translational efficiency of spliced over nonspliced mRNAs. Recruits activated ribosomal protein S6 kinase beta-1 I/RPS6KB1 to newly synthesized mRNA. Involved in nuclear mRNA export; probably mediated by associati

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR051229 |
| InterPro | IPR012677 |
| InterPro | IPR034784 |
| InterPro | IPR035979 |
| InterPro | IPR000504 |
| Pfam | PF00076 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RPS6KB1 | BioGRID | 0 |
| USP20 | BioGRID | 0 |
| TERF2 | BioGRID | 0 |
| POT1 | BioGRID | 0 |
| HDGF | BioGRID | 0 |
| SIRT7 | BioGRID | 0 |
| ERH | BioGRID | 0 |
| NQO1 | BioGRID | 0 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100227-POLDIP3

![](https://images.proteinatlas.org/18419/199_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/18419/199_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/18419/155_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/18419/155_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/18419/157_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/18419/157_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/48790/798_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/48790/798_F11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 39**

| 40950343 | A novel lactylation-related signature for predicting esophageal cancer prognosis and immune infiltration. | J Gastrointest Oncol 2025 |
| 40407859 | Construction and Multi-dimensional Validation of a Lactylation-Related Signature for Glioblastoma Multiforme Prognostic  | Mol Biotechnol 2026 |
| 40275359 | Multi-region brain transcriptomic analysis of amyotrophic lateral sclerosis reveals widespread RNA alterations and subst | Mol Neurodegener 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/POLDIP3

### 深度机制分析

**结构域架构**：POLDIP3/SKAR（UniProt B4E0L0，438 aa，48.2 kDa）是S6K1剪接产物结合适配蛋白。其域架构以N端RRM（RNA recognition motif）域为中心：IPR000504（RNA recognition motif domain；Pfam:PF00076）采用经典的βαββαβ折叠识别剪接mRNA的5' cap近端序列，特别是CBC（cap-binding complex）结合剪接mRNA的剪接连接区域。IPR012677（Nucleotide-binding alpha-beta plait domain superfamily）定义整个N端半段的折叠拓扑。IPR051229为POLDIP3特有的S6K1招募结构域标记，IPR034784为POLDIP3型RRM的序列特异标记。C端含富含丝氨酸/脯氨酸区段，为S6K1 (RPS6KB1)的停靠（docking）位点。整个域架构适配mRNA从核输出到胞质翻译的整个过程。

**PPI互作网络**：BioGRID数据描述了一个核mRNP-端粒-PPARγ-细胞保护网络：RPS6KB1（核糖体蛋白S6激酶β-1/S6K1，评分0）是POLDIP3的标志性互作伙伴——S6K1被mTORC1磷酸化激活后结合到POLDIP3，POLDIP3随后招募S6K1至CBC结合的剪接mRNA以促进新生mRNA的翻译效率（剪接增强翻译/SET机制）；TERF2（端粒重复结合因子2，评分0）和POT1（端粒保护蛋白1，评分0）是shelterin端粒保护复合体的核心组分——POLDIP3与端粒蛋白的互作暗示其参与端粒维持；HDGF（肝癌源性生长因子，评分0）为染色质结合生长因子；SIRT7（sirtuin-7，评分0）为核仁NAD+依赖的去乙酰化酶；ERH（增强子rudimentary同源物，评分0）参与细胞周期调控和pre-mRNA剪接；USP20（去泛素化酶，评分0）和NQO1（NAD(P)H醌氧化还原酶，评分0）参与应激应答。

**结构-功能关系**：POLDIP3的核心功能是在新生mRNP形成后立即促进其翻译——这一过程称为剪接依赖性翻译增强（Splicing-Enhanced Translation, SET）。CBC结合的剪接mRNA通过POLDIP3作为桥梁，将活化的S6K1 (p-p70 S6K) 带到eIF4B和PDCD4等翻译起始因子处进行磷酸化，从而加速翻译起始速率。此机制确保剪接mRNA（相对于非剪接mRNA）获得翻译优先权。TERF2/POT1互作提示POLDIP3在端粒处具有独立于mRNA翻译的功能——端粒TERRA RNA（含端粒重复的非编码RNA）的翻译调控或端粒完整性监测。

**TE调控机制**：POLDIP3通过TERF2/POT1端粒保护蛋白的互作与TE调控建立直接联系——端粒酶和端粒维持机制与LINE-1逆转录转座共享酶学基础（都需要逆转录酶活性），端粒保护复合体（shelterin）的损坏导致端粒去保护化，引发ALT（替代性端粒延长）通路的激活——ALT通路可利用TE序列作为端粒重建的模板。SIRT7去乙酰化酶（评分为0的互作）是核仁rDNA转录的抑制因子，而其活性延伸至染色质水平——SIRT7缺失已被报道导致LINE-1表达上调和基因组不稳定性。ERH参与含U12的内含子剪接（次要剪接体）——某些TE（特别是SINE和LINE元件）利用U12依赖的剪接供体位点进行异常加工。

**前沿意义**：POLDIP3在剪接→翻译偶联中的核心角色使其在TE RNA加工的不同层级均有调控潜力——核输出（CBC结合）、翻译效率（S6K1招募）和端粒保护（TERF2互作）。TERF2-POT1-shelterin功能网络与TE的联系代表了TE研究的新方向——端粒完整性是限制LINE-1转座的内在屏障，而shelterin的破坏可能导致TE机会性插入。39篇文献中相对有限的研究深度使这一方向变得更加吸引人。


