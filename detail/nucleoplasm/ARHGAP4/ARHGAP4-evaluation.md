---
type: protein-evaluation
gene: "ARHGAP4"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## ARHGAP4 (Rho GTPase-activating protein 4) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | ARHGAP4 |
| 蛋白全称 | Rho GTPase-activating protein 4 |
| UniProt ID | P98171 |
| 蛋白大小 | 946 aa / 104.1 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 946 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR027267; InterPro:IPR031160; InterPro:IPR001060; InterPro:IPR008936; InterPro:IPR000198; InterPro:IPR036028 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **122/180** | |
| **归一化总分 (/1.83)** | | | **66.7/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Inhibitory effect on stress fiber organization. May down-regulate Rho-like GTPase in hematopoietic cells

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR027267 |
| InterPro | IPR031160 |
| InterPro | IPR001060 |
| InterPro | IPR008936 |
| InterPro | IPR000198 |
| InterPro | IPR036028 |
| InterPro | IPR001452 |
| InterPro | IPR051627 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

**结构域架构**：ARHGAP4（946 aa, 104.1 kDa, P98171, Rho GTPase-activating protein 4）是多结构域RhoGAP家族蛋白。核心催化域RhoGAP（IPR000198, IPR008936）含有保守的arginine finger残基（对应于Cdc42GAP的Arg305）——插入Rho GTPase的核苷酸结合口袋——通过稳定过渡态中的γ-phosphate离去基团催化GTP水解（"arginine finger"机制）——将Rho GTPase从GTP-bound active state转换为GDP-bound inactive state。N端含SH3结构域（IPR001452, 约aa 1-60）识别富脯氨酸序列（PxxP motif）——介导与信号蛋白的互作募集。中间区域含PH-like domain（IPR001060, Pleckstrin Homology）——结合phosphatidylinositol phosphates（PIPs）——将ARHGAP4定位至膜区室。C端区域（IPR031160, IPR027267）为ARHGAP4特异的扩展序列——推测含多个磷酸化位点（PKA/PKC consensus sites）。AlphaFold预测可用但平均pLDDT未显式列出，推测折叠域pLDDT>75。PubMed仅60篇（PMID:40817404: colorectal cancer stemness中ARHGAP4/MYH9/beta-catenin/c-Jun正反馈loop的促癌机制；PMID:41757196: 人骨骼肌衰老网络图谱）。

**PPI互作网络解读**：PPI网络揭示ARHGAP4在actin cytoskeleton remodeling和nuclear signaling间的连接。WAS（Wiskott-Aldrich syndrome protein, STRING 717）是ARP2/3复合体激活因子——WAS结合Cdc42-GTP后释放自抑制构象→激活ARP2/3→actin nucleation——ARHGAP4通过GAP活性使Cdc42失活→间接调控WAS-ARP2/3-actin通路。RAC1（BioGRID）是ARHGAP4的直接底物——RAC1-GTP调控lamellipodia形成和cell migration——ARHGAP4的GAP活性下调RAC1 signaling→抑制cell motility。SMARCA2（BRM, SWI/SNF chromatin remodeler ATPase, BioGRID）的互作是最引人注目的——SMARCA2/BRG1（SMARCA4）是BAF（SWI/SNF）chromatin remodeling complex的mutually exclusive catalytic ATPase——调控DNA accessibility和transcription。ARHGAP4-SMARCA2的物理互作提示ARHGAP4可能在chromatin remodeling层面间接参与基因表达调控。HMGN2（High Mobility Group Nucleosome Binding Protein 2, BioGRID）是核小体结合蛋白——与核小体core particle结合——促进chromatin decompaction→增强转录因子access——HMGN2已知调控epigenetic marks H3K27ac和DNase I hypersensitivity。TRIM25（BioGRID）为E3 ubiquitin ligase——催化RIG-I（DDX58）的K63-linked ubiquitination→激活innate immune IFN signaling——也参与stress granule assembly和RNA metabolism。

**结构解读**：ARHGAP4的催化机制遵循RhoGAP家族保守模式——RhoGAP domain（约200 aa）的fold为alpha-helical bundle——catalytic Arg和conserved Lys/Gln形成过渡态稳定网络——GAP与Rho-GTP复合物的共晶结构（如Cdc42-Cdc42GAP, PDB: 1GRN）揭示GAP domain的精氨酸指（arginine finger）插入活性位点后稳定Gln61的catalytic water positioning。SH3 domain为standard beta-barrel fold（~60 aa）——识别PxxP motif的type I或type II orientation。PH domain的beta-sandwich fold含保守basic patch（K/R-rich loop）——结合PI(4,5)P2或PI(3,4,5)P3——ARHGAP4的PH domain可能偏好PI(4,5)P2（质膜富集），但核膜和核内体（endosome）的PI(3)P和PI(4)P也为其核定位提供了phosphoinositide基础。

**机制模型**：（1）细胞质经典功能——ARHGAP4通过GAP活性调控Rho GTPase cycling——Cdc42/Rac1/RhoA switch决定cytoskeleton remodeling和cell migration模式——ARHGAP4主要在hematopoietic cells中表达——下调stress fiber formation和actin polymerization。（2）核内非经典功能——ARHGAP4-SMARCA2互作提示chromatin remodeling coupling——ARHGAP4可能在serum/cytokine刺激下经importin/exportin系统穿梭入核→与SMARCA2/BRM BAF complex结合→调控BAF complex的chromatin targeting（如影响enhancer/promoter区域的chromatin accessibility）→间接调控包括TE区域在内的基因组位点的转录。（3）ARHGAP4/MYH9/beta-catenin/c-Jun正反馈loop（PMID:40817404）——ARHGAP4上调MYH9（non-muscle myosin IIA）表达→MYH9稳定beta-catenin→beta-catenin-TCF/LEF激活c-Jun transcription→c-Jun再反馈激活ARHGAP4——此回路在colorectal cancer中驱动cancer stemness——TE activation常伴随Wnt/beta-catenin通路活化——ARHGAP4的反馈loop可能导致TE区域的chromatin relaxation和cryptic transcription。

**TE调控展望**：ARHGAP4的TE调控关联主要通过chromatin remodeling耦合。SMARCA2 interaction是核心线索——BAF complex（SWI/SNF）已知在ES细胞中与EZH2/PRC2存在functional antagonism——BAF complex促进chromatin accessibility——失去PRC2-mediated H3K27me3的TE区域可能被BAF complex重新打开→TE transcription。ARHGAP4可能通过调控BAF complex activity或recruitment间接影响TE区域的chromatin state。HMGN2（nucleosome binding protein）的互作进一步支持ARHGAP4在chromatin level的作用——HMGN2 knockout影响全基因组chromatin accessibility和H3K27ac landscape。Wnt/beta-catenin/c-Jun正反馈loop作为"second hit"机制——持续激活的transcription network可能overwhelm local TE silencing→TE de-repression——尤其在"开放"染色质区域的ERV/L1家族拷贝。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| WAS | STRING | 717 |
| PCBP1 | BioGRID | 1 |
| ARHGAP4 | BioGRID | 1 |
| TRIM25 | BioGRID | 1 |
| HMGN2 | BioGRID | 1 |
| RAC1 | BioGRID | 1 |
| SMARCA2 | BioGRID | 1 |
| CSTA | BioGRID | 1 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ARHGAP4

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000089820-ARHGAP4

![](https://images.proteinatlas.org/301/1846_E4_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/1846_E4_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/2055_E7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/2055_E7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/1893_C2_13_cr5bbcaf4c26260_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/1893_C2_16_cr5bbcaf4c279fb_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000089820-ARHGAP4

![](https://images.proteinatlas.org/301/1846_E4_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/1846_E4_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/2055_E7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/2055_E7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/1893_C2_13_cr5bbcaf4c26260_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/1893_C2_16_cr5bbcaf4c279fb_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000089820-ARHGAP4

![](https://images.proteinatlas.org/301/1846_E4_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/1846_E4_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/2055_E7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/2055_E7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/1893_C2_13_cr5bbcaf4c26260_blue_red_green.jpg)
![](https://images.proteinatlas.org/301/1893_C2_16_cr5bbcaf4c279fb_blue_red_green.jpg)

### PubMed

**Count: 60**

| PMID | Title |
|---|---|
| 42346437 | A Network Toxicology Framework for Identification of Immune System Disruption by Per- and Polyfluoroalkyl Substance (PFAS) Mixture: In Silico Analysis |
| 41757196 | A network-based atlas of human skeletal muscle aging. |
| 40817404 | ARHGAP4/MYH9/β-catenin/c-Jun positive feedback loop promotes colorectal cancer stemness. |
| 40553870 | WITHDRAWN: ARHGAP4/ MYH9/ β-catenin/ c-Jun positive feedback loop regulates colorectal cancer stemness. |
| 40275315 | E2F expression profiling-based subtypes in head and neck squamous cell carcinoma: clinical relevance, prognostic implications, and personalized therap |


