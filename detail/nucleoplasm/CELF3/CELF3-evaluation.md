---
type: protein-evaluation
gene: "CELF3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CELF3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CELF3 |
| 蛋白名称 | CUGBP Elav-like family member 3 |
| 蛋白大小 | 465 aa / 50.5 kDa |
| UniProt ID | Q5SZQ8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Nucleoplasm (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 465 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=10 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=70.1; PDB=1 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | CELF3/4/5/6_RRM1; Nucleotide-bd_a/b_plait_sf; RBD_domain_sf |
| 🔗 PPI | 4/10 | ×3 | 12.0 | PPI degree=15 |
| **加权总分** | | | **133/180** | |
| **归一化总分 (÷1.83)** | | | **73.8/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据
HPA: Nucleoplasm (Approved)
UniProt: SUBCELLULAR LOCATION: Nucleus {ECO:0000250}. Cytoplasm {ECO:0000250}.

**IF 图像**: [Protein Atlas](https://www.proteinatlas.org/)

#### 3.2 蛋白大小
465 aa / 50.5 kDa

#### 3.3 研究现状
PubMed strict=10, broad=33
- PMID 30132996: Integrative analysis of significant RNA-binding proteins in colorectal cancer metastasis. *Journal of cellular biochemistry*
- PMID 25145264: Formation of nuclear bodies by the lncRNA Gomafu-associating proteins Celf3 and SF1. *Genes to cells : devoted to molecular & cellular mechanisms*
- PMID 37537886: Members of the CUGBP Elav-like family of RNA-binding proteins are expressed in distinct populations of primary sensory n *The Journal of comparative neurology*

#### 3.4 三维结构
AF pLDDT=70.1, PDB=1

#### 3.5 结构域
InterPro: CELF3/4/5/6_RRM1; Nucleotide-bd_a/b_plait_sf; RBD_domain_sf
Pfam: RRM_1


#### 3.6 PPI 互作网络
Combined degree=15

#### 3.7 多库互证
basic cross-validation

### 4. 总体评价
⭐⭐⭐⭐
**73.8/100** | **nucleoplasm**


### 功能描述

RNA-binding protein involved in the regulation of pre-mRNA alternative splicing. Mediates exon inclusion and/or exclusion in pre-mRNA that are subject to tissue-specific and developmentally regulated alternative splicing. Specifically activates exon 5 inclusion of cardiac isoforms of TNNT2 during heart remodeling at the juvenile to adult transition. Activates the splicing of MAPT/Tau exon 10. Binds to muscle-specific splicing enhancer (MSE) intronic sites flanking the alternative exon 5 of TNNT2


### 深度机制分析

CELF3(CUGBP Elav-like family member 3)是CELF/BRUNOL RNA结合蛋白家族的重要核质成员，其结构域架构为经典的三联RNA识别基序(RRM)排列。CELF3/4/5/6_RRM1(IPR特定)位于N端，与串联RRM2和C端RRM3共同构成RBD_domain_sf(IPR)核苷酸结合折叠。每个RRM是由约90个氨基酸组成的βαββαβ折叠，其β-sheet表面的保守RNP1/RNP2基序通过氢键和疏水堆积力识别靶RNA中的UG/UGU重复序列。RRM1和RRM2串联排列形成高亲和力的RNA结合平台，RRM3则为辅助性RNA接触面。pLDDT=70.1，推测低置信度区域主要存在于连接RRM间和C端的内在无序区域(IDR)。

在核质中，CELF3的核心生物学功能是通过选择性地促进/抑制靶pre-mRNA的外显子"包含"(exon inclusion)或"跳跃"(exon skipping)来调控组织特异性可变剪接。其最佳鉴定的底物基因为MAPT(Tau蛋白)的外显子10和TNNT2(心肌肌钙蛋白T)的外显子5(UniProt功能注释)。结合机制为：CELF3识别内含子区域富含UG序列的MSE(肌肉特异性剪接增强子，Muscle-Specific Splicing Enhancer)，通过其N端结构域招募U2AF65剪接因子，促进上游外显子的剪接体组装。

CELF3的PPI网络显示其同时与RRM1/RRM2(核糖核苷酸还原酶大/小亚基，STRING=719/831)和CEBPD(CCAAT/增强子结合蛋白δ，STRING=900)互作——前者连接RNA代谢与dNTP前体合成，后者连接CELF3的剪接调控与转录因子的DNA结合。更为关键的是，CELF3与SF1(Splicing Factor 1)形成核质小体(PMID:25145264)，定位于长链非编码RNA Gomafu核内富集位点。这种lncRNA-蛋白质核内相分离体(Nuclear Body)是CELF3发挥其剪接调控活性的可能膜性无膜细胞器。

值得注意的是，CELF3在结肠癌转移中作为重要的可变剪接调控因子被报道(PMID:30132996)，其在初期感觉神经元中的特异性表达模式揭示了神经疾病的潜在关联(PMID:37537886)。CELF3为强核定位信号(Nucleoplasm Approved)，蛋白质体积适中(465 aa)，PubMed仅10篇——结构域注释清晰、靶RNA明确、无完善的人类结构数据，是理想的核蛋白功能性机制研究靶点。RNA-seq偶联CLIP-seq(CELF3 iCLIP)实验是最佳的功能验证路径。




### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000159409-CELF3

![](https://images.proteinatlas.org/6292/1253_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/6292/1253_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/6292/1219_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/6292/1219_H6_3_red_green.jpg)
![](https://images.proteinatlas.org/6292/1189_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/6292/1189_H6_2_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CEBPD | STRING | 900 |
| RRM2 | STRING | 831 |
| RRM1 | STRING | 719 |
| C14orf1 | physical | Stelzl U (2005) |
| SOBP | physical | Stelzl U (2005) |
| TLE1 | physical | Stelzl U (2005) |
| CDKN1A | physical | Vinayagam A (2011) |
| ANXA7 | physical | Vinayagam A (2011) |
| RBFOX1 | physical | Lim J (2006) |
| PCBP1 | physical | Lim J (2006) |
| CELF5 | physical | Huttlin EL (2017) |
| MKRN1 | physical | Huttlin EL (2017) |
| BRCA2 | physical | Malik S (2016) |


### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5SZQ8-F1-predicted_aligned_error_v6.png)

### PubMed

**Count: 33**

| PMID | Title |
|---|---|
| 42104406 | CELF family of RNA-binding proteins: roles in disease biology and potential for therapeutic intervention. |
| 38878991 | Early transcriptional similarities between two distinct neural lineages during ascidian embryogenesis. |
| 37537886 | Members of the CUGBP Elav-like family of RNA-binding proteins are expressed in distinct populations of primary sensory neurons. |
| 37186041 | Identifying potential targets for lung cancer intervention by analyzing the crosstalk of cancer-associated fibroblasts and immune and metabolism micro |
| 35784124 | MicroRNA-34a and microRNA-146a target CELF3 and suppress the osteogenic differentiation of periodontal ligament stem cells under cyclic mechanical str |


