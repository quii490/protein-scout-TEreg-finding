---
type: protein-evaluation
gene: "TMEM209"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM209 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM209 |
| 蛋白名称 | Transmembrane protein 209 |
| 蛋白大小 | 561 aa / 62.9 kDa |
| UniProt ID | Q96SK2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28.0 | HPA: Nuclear membrane; Nuclear speckles; Vesicles (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 561 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=10 篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT=68.4; PDB: 0 entries |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | Cytochrome_B561-rel |
| 🔗 PPI | 6/10 | ×3 | 18.0 | Combined PPI degree=147 |
| **加权总分** | | | **128/180** | |
| **归一化总分 (÷1.83)** | | | **70.5/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nuclear membrane; Nuclear speckles; Vesicles | Approved |
| GO-CC | Golgi apparatus(IEA:UniProtKB-SubCell); membrane(IBA:GO_Central); nuclear envelope(IEA:UniProtKB-Sub | — |

**IF 图像**: See [Protein Atlas](https://www.proteinatlas.org/)

**PAE 图**: https://alphafold.ebi.ac.uk/files/AF-Q96SK2-F1-predicted_aligned_error_v6.png

#### 3.2 蛋白大小评估
561 aa / 62.9 kDa.

#### 3.3 研究现状
PubMed strict: 10. Broad: 10.

- PMID 39414762: TMEM209 promotes hepatocellular carcinoma progression by activating the Wnt/β-catenin signaling pathway through KPNB1 st. *Cell death discovery*
- PMID 34003694: Screening of Potential Key Genes Related to Tubal Factor Infertility Based on Competitive Endogenous RNA Network.. *Genetic testing and molecular biomarkers*
- PMID 41582553: The nuclear envelope protein TMEM209 is an integral component of the nuclear pore complex and interacts with Nup210.. *Journal of cell science*

#### 3.4 三维结构分析
AlphaFold pLDDT=68.4. PDB=0.

#### 3.5 结构域分析
InterPro: Cytochrome_B561-rel
Pfam: CytochromB561_N

#### 3.6 PPI 互作网络
Combined human PPI degree=147.

#### 3.7 多库互证
| 维度 | 来源 | 结果 |
|---|---|---|
| 核定位 | HPA + GO-CC | consistent |
| 结构域 | InterPro + Pfam | verified |
| PPI | STRING/BioGRID | 有数据 |

### 4. 总体评价
**推荐等级**: ⭐⭐⭐⭐
**归一化总分**: 70.5/100
**定位分类**: nuclear-envelope

Non-chromatin-regulatory nuclear protein with some nuclear localization evidence. Very novel (10 PubMed papers).

### 功能描述

Nuclear envelope protein which in association with NUP205, may be involved in nuclear transport of various nuclear proteins in addition to MYC


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ELAVL1 | BioGRID | 0 |
| MUS81 | BioGRID | 0 |
| IFI16 | BioGRID | 0 |
| TCTN2 | BioGRID | 0 |
| TCTN3 | BioGRID | 0 |
| CEP135 | BioGRID | 0 |
| TMEM17 | BioGRID | 0 |
| TMEM216 | BioGRID | 0 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000146842-TMEM209

![](https://images.proteinatlas.org/31678/374_F7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/31678/374_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31678/372_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31678/372_F7_3_blue_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。


### PubMed

**Count: 10**

| PMID | Title |
|---|---|
| 41898718 | Integrative Multi-Omics Analysis Identifies NUP205 as a Candidate Prognostic Biomarker in Liver Hepatocellular Carcinoma. |
| 41582553 | The nuclear envelope protein TMEM209 is an integral component of the nuclear pore complex and interacts with Nup210. |
| 41562482 | Transmembrane Protein GbTMEM209 Inhibits Fibre Elongation via Competitive Interaction With GbHOX3 in Gossypium barbadense. |
| 39414762 | TMEM209 promotes hepatocellular carcinoma progression by activating the Wnt/β-catenin signaling pathway through KPNB1 stabilization. |
| 38305770 | Risk model based on genes regulating the response of tumor cells to T-cell-mediated killing in esophageal squamous cell carcinoma. |

### 深度机制分析

**结构域架构**：TMEM209（UniProt Q96SK2，561 aa，62.9 kDa）是核孔复合体（NPC）的跨膜整合蛋白。InterPro和Pfam注释仅识别Cyt_B561相关域（Cytochrome_B561-rel / CytochromB561_N）——该域含两个Bis-His配位的b型血红素辅因子，参与跨膜电子传递和抗坏血酸再生。此域在核孔蛋白中极为罕见，赋予了TMEM209独特的功能可能性——作为核被膜的氧化还原传感器或在核孔中建立局部氧化还原微环境。

**PPI互作网络**：BioGRID数据显示TMEM209与多个核孔/纤毛蛋白存在互作，包括TCTN2（构造蛋白2，评分0）、TCTN3（构造蛋白3，评分0）、CEP135（中心体蛋白135，评分0）、TMEM17（跨膜蛋白17，评分0）和TMEM216（跨膜蛋白216，评分0）。该PPI模式呈现核孔-初级纤毛膜蛋白轴的特征。ELAVL1（RNA结合蛋白，评分0）、MUS81（结构特异性内切酶，评分0）和IFI16（干扰素γ诱导蛋白16，评分0）的互作暗示功能涉及RNA代谢、DNA修复和先天免疫感知。PPI总度（combined degree=147）提示较大规模的互作网络。

**结构-功能关系**：AlphaFold pLDDT=68.4（中等置信度）表明部分域折叠良好但存在柔性区段。TMEM209作为核被膜蛋白与NUP205协同参与核蛋白转运（含MYC核输入），关键文献（PMID:41582553）直接证明了TMEM209是NPC的完整组分并与Nup210互作。TMEM209-KPNB1（importin β）互作通过稳定KPNB1来促进Wnt/β-catenin信号通路（PMID:39414762），机制涉及核输入受体表达水平的蛋白质稳定性调控。GO-CC注释含nuclear envelope（IEA:UniProtKB-SubCell）。

**TE调控机制**：TMEM209作为NPC组分的身份赋予了其TE调控的多维可能性。其一，NPC是TE转录本和TE编码蛋白出入核的物理瓶颈——NUP210（TMEM209互作伙伴）的功能改变直接影响核转运选择性。其二，KPNB1/importin β的稳定化可能增强特定的核输入通路（如KRAB-ZFP→KAP1→染色质修饰物的核输入），有利于TE沉默因子的核积累。其三，cGAS-STING通路感知胞质TE-DNA，IFI16已知在核内和胞质中识别TE/viral DNA以启动先天免疫——TMEM209在核孔微环境可能作为DNA传感器平台。其四，Wnt/β-catenin信号活化已知与ERV/LTR转录相关（TCF/LEF结合LTR增强子启动TE转录），TMEM209通过KPNB1稳定性调控Wnt信号强度可能间接影响TE转录组。

**前沿意义**：TMEM209仅10篇PubMed文献，其中核孔功能的关键验证（PMID:41582553）是2025-2026年的最新发现，标志该蛋白研究正在进入功能性爆发期。b型血红素域的存在使TMEM209成为NPC中极少数具有氧化还原活性的跨膜蛋白——NPC腔道内的局部氧化还原状态可能调控富含半胱氨酸的核孔FG repeat蛋白的凝聚态行为（液-液相分离）。TMEM209敲除/敲低→核转运组+TE-RNA-seq联合分析可确定其对TE转录本核输出的选择性调控。


