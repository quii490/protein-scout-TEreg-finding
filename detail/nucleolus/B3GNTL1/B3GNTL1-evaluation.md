---
type: protein-evaluation
gene: "B3GNTL1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B3GNTL1 (Queuosine-tRNA galactosyltransferase) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B3GNTL1 |
| 蛋白全称 | Queuosine-tRNA galactosyltransferase |
| UniProt ID | Q67FW5 |
| 蛋白大小 | 346 aa / 38.1 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 346 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 6/10 | x2 | 12.0 | InterPro:IPR001173; InterPro:IPR029044; Pfam:PF00535 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **120/180** | |
| **归一化总分 (/1.83)** | | | **65.6/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Glycosyltransferase that specifically catalyzes galactosylation of cytoplasmic tRNA(Tyr) modified with queuosine at position 34 (queuosine(34)) (PubMed:37992713). Galactosylates the cyclopentene hydroxyl group of queuosine(34) in tRNA(Tyr) to form galactosyl-queuosine(34) (PubMed:37992713). Mannosylation of queuosine(34) in tRNA(Tyr) is required to slow-down elongation at cognate codons UAC and su

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR001173 |
| InterPro | IPR029044 |
| Pfam | PF00535 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000175711-B3GNTL1

![](https://images.proteinatlas.org/24547/548_C9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/24547/548_C9_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/24547/508_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24547/508_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24547/505_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24547/505_C9_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR001173;IPR029044; |
| Pfam | PF00535; |
| UniProt Domain | 未检出 |


### 深度机制分析

**结构域架构**：B3GNTL1（Q67FW5, Queuosine-tRNA galactosyltransferase, 346 aa / 38.1 kDa）的主要结构域注释为IPR001173, IPR029044。Pfam数据库进一步识别到PF00535等保守域。AlphaFold pLDDT=0.82（中低置信度）——结构预测显示较大无序区域，可能含IDR或需要结合伴侣才能有序折叠。该蛋白暂无实验PDB结构（PDB=0），当前结构信息依赖AlphaFold预测。PubMed=0，TrEMBL未审查条目，机制解析尚未起步。

**PPI互作网络解读**：PPI network（degree=N/A）——BioGRID数据库记录的关键互作伙伴包括IMPDH1、HNRNPL、FTL。其中HNRNPL等具有染色质调控或转录相关功能——提示B3GNTL1可能通过PPI平台间接参与核内转录调控网络。

**结构解读**：InterPro注释到2个保守结构域：IPR001173、IPR029044——这些domain signature暗示了该蛋白的功能类别。Pfam域PF00535的保守性进一步验证了该蛋白特定的进化约束。结构预测置信度有限，需实验结构解析确证。

**机制模型**：B3GNTL1为queuosine-tRNA galactosyltransferase——GT-B fold glycosyltransferase，使用UDP-galactose作为donor substrate。tRNA modification（Q34 galactosylation）影响translation speed——在nucleoplasm中tRNA modification enzyme可能具有non-canonical nuclear function。

**TE调控展望**：B3GNTL1的TE regulation潜力目前缺乏直接的实验证据。TE调控关联性取决于：（1）B3GNTL1与chromatin remodeling complex（SWI/SNF, NuRD, PRC1/2）的physical association；（2）B3GNTL1能否通过其结构域识别TE-derived element；（3）B3GNTL1的depletion是否改变LINE-1或ERV family的expression level。建议affinity purification-MS鉴定B3GNTL1在核内的完整interactome。Combined with RNA-seq upon knockdown/overexpression——可在transcriptome level评估其对TE subfamily expression的潜在影响。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IMPDH1 | BioGRID | 0 |
| HNRNPL | BioGRID | 0 |
| FTL | BioGRID | 0 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B3GNTL1

### PubMed

**Count: 8**

| PMID | Title |
|---|---|
| 40020829 | Whole-exome sequencing identifies EP300 variants associated with visceral leishmaniasis relapse. |
| 38255262 | Shared Genetics between Age at Menarche and Type 2 Diabetes Mellitus: Genome-Wide Genetic Correlation Study. |
| 37372436 | Genomic Landscape of Copy Number Variations and Their Associations with Climatic Variables in the World's Sheep. |
| 37101220 | Accurate detection of early-stage lung cancer using a panel of circulating cell-free DNA methylation biomarkers. |
| 36323795 | Discovering a trans-omics biomarker signature that predisposes high risk diabetic patients to diabetic kidney disease. |

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/B3GNTL1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.82 |
| pLDDT > 0.9 | 35.0% |
| pLDDT < 0.5 | 2.3% |
| 残基数 | 346 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

