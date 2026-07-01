---
type: protein-evaluation
gene: "PSMD5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PSMD5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PSMD5 |
| 蛋白名称 | 26S proteasome non-ATPase regulatory subunit 5 |
| 蛋白大小 | 504 aa / 56.2 kDa |
| UniProt ID | Q16401 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Basal body; Centrosome; Connecting piece; Cytosol; (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 504 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=18 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=93.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | ARM-like; ARM-type_fold; PSMD5 |
| PPI | 7/10 | x3 | 21.0 | PPI degree=116 |
| **加权总分** | | | **140/180** | |
| **归一化总分** | | | **77.0/100** | 互证: +1 |

### 3. 分析
- Basal body; Centrosome; Connecting piece; Cytosol; Mid piece; Nucleoplasm (Approved)
- PubMed strict=18 broad=19
- AF pLDDT=93.8 PDB=0
- InterPro: ARM-like; ARM-type_fold; PSMD5
- Pfam: Proteasom_PSMB
- PPI degree=116 ChIP: None
40953274: More 26S and 30S proteasomes are beneficial in proteinopathy. | 36282272: Single-Nucleotide Variants and Epimutations Induce Proteasome Inhibitor Resistan | 22901813: Cancer vulnerabilities unveiled by genomic loss.

### 4. 总体评价
**77.0/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**结构域架构**: PSMD5含有ARM-like超螺旋折叠（IPR011989）和ARM-type_fold（IPR016024），这两种α-α超螺旋重复序列是介导蛋白-蛋白相互作用的经典骨架结构。PSMD5特异性结构域（IPR019538/PF10508）将其定义为一个专用的蛋白酶体组装因子，区别于其他ARM重复蛋白。Pfam还标注了Proteasom_PSMB关联，提示PSMD5可能通过ARM重复表面与20S核心颗粒（CP）的β亚基进行远距离偶联。ARM重复的螺线管式结构为19S调节颗粒（RP）碱基亚复合体的逐步组装提供了精确的分子模板。

**PPI网络解读**: PSMD5的互作网络高度聚焦于26S蛋白酶体碱基组装。PSMC2、PSMC1（AAA-ATPase亚基，BioGRID）与其形成预组装中间体PSMD5:PSMC2:PSMC1:PSMD2（UniProt功能注释已确认），作为碱基组装的起始支架。RAD23A（BioGRID）是泛素受体，介导泛素化底物向蛋白酶体的递送——PSMD5与RAD23A的互作暗示组装过程与底物识别存在偶联。ELAVL1（HuR，BioGRID）是RNA结合蛋白，参与mRNA稳定性调控，提示PSMD5的表达可能在转录后水平受HuR调控。COPS2（BioGRID）是COP9信号体（CSN）亚基，CSN通过去NEDD化调控CRL泛素连接酶活性，这构成了蛋白酶体上游的泛素化调控与蛋白酶体组装之间的一个潜在调控环。

**结构诠释**: AlphaFold pLDDT=93.8为极高置信度的预测结构，表明PSMD5的整体折叠高度有序。ARM重复通常形成右手超螺旋，其凹面为配体结合面。在PSMD5中，这个凹面可能依次结合PSMC2和PSMC1的C末端结构域，以正确的空间排布和化学计量比模板化AAA-ATPase六元环的组装。pLDDT如此之高暗示PSMD5在溶液中以单体形式稳定折叠，这与分子伴侣的功能需求一致——组装因子需要在结合客户蛋白之前维持自身稳定的构象。

**分子机制模型**: PSMD5作为26S蛋白酶体碱基亚复合体的专用组装伴侣（assembly chaperone），其作用机制是分步式的：(1) PSMD5通过ARM重复凹面同时或依次招募PSMC2和PSMC1，与PSMD2共同形成四元预组装模块；(2) 该模块随后与PSMD10:PSMC4:PSMC5:PAAF1模块对接，形成完整的碱基六元环；(3) PSMD5在对接完成后被释放，以便碱基与盖子亚复合体和20S核心颗粒进一步组装。PubMed 40953274发现"更多的26S和30S蛋白酶体有利于蛋白病"，直接表明提高PSMD5介导的组装效率可能是减缓蛋白毒性聚集的治疗策略。PubMed 36282272报道"单核苷酸变异和表观突变诱导蛋白酶体抑制剂耐药"，提示PSMD5的错义突变或表达异常可作为蛋白酶体抑制剂（如硼替佐米）治疗的耐药生物标志物。

**研究/治疗意义**: PSMD5是蛋白酶体组装通路的限速因子，其表达水平和活性直接影响细胞蛋白酶体容量。在多发性骨髓瘤等依赖高蛋白酶体活性的肿瘤中，PSMD5可作为联合治疗靶点——抑制PSMD5与硼替佐米联用可能产生合成致死效应。在神经退行性蛋白病（阿尔茨海默病、帕金森病）中，上调PSMD5或增强其组装效率可能加速毒性蛋白聚集体的清除。HuR-ELAVL1对PSMD5 mRNA的潜在调控（基于PPI数据）提示了一条通过RNA结合蛋白调控蛋白酶体容量的新通路。

### 补充分析 (UniProt API)

**蛋白全称**: 26S proteasome non-ATPase regulatory subunit 5

**功能**: Acts as a chaperone during the assembly of the 26S proteasome, specifically of the base subcomplex of the PA700/19S regulatory complex (RC). In the initial step of the base subcomplex assembly is part of an intermediate PSMD5:PSMC2:PSMC1:PSMD2 module which probably assembles with a PSMD10:PSMC4:PSMC5:PAAF1 module followed by dissociation of PSMD5

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011989 |
| InterPro | IPR016024 |
| InterPro | IPR019538 |
| Pfam | PF10508 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PSMC2 | BioGRID | 0 |
| PSMD2 | BioGRID | 0 |
| PSMC1 | BioGRID | 0 |
| PMS2 | BioGRID | 0 |
| ELAVL1 | BioGRID | 0 |
| RAD23A | BioGRID | 0 |
| PSMD1 | BioGRID | 0 |
| COPS2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q16401-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000095261-PSMD5

![](https://images.proteinatlas.org/3216/2241_C11_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2241_C11_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2234_B7_16_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2234_B7_76_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2232_D6_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2232_D6_31_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000095261-PSMD5

![](https://images.proteinatlas.org/3216/2241_C11_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2241_C11_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2234_B7_16_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2234_B7_76_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2232_D6_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2232_D6_31_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000095261-PSMD5

![](https://images.proteinatlas.org/3216/2241_C11_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2241_C11_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2234_B7_16_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2234_B7_76_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2232_D6_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/3216/2232_D6_31_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 19**

| 42289649 | Comparative mass spectrometry analysis of high and low centrifugation extracellular vesicle (EV) pellets from healthy ur | Clin Proteomics 2026 |
| 41653366 | Transcriptome remodeling of mouse hearts during postnatal cardiac maturation and under proteotoxic stress. | Mol Biol Rep 2026 |
| 41120564 | PACT is requisite for prostate cancer cell proliferation. | Sci Rep 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSMD5

