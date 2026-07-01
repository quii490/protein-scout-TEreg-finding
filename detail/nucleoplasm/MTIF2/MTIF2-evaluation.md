---
type: protein-evaluation
gene: "MTIF2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MTIF2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MTIF2 |
| 蛋白名称 | Translation initiation factor IF-2, mitochondrial |
| 蛋白大小 | 727 aa / 81.3 kDa |
| UniProt ID | P46199 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 727 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=26 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=84.2; PDB=9 |
| 调控结构域 | 4/10 | x2 | 8.0 | EF-G-like_DII; IF2_II; P-loop_NTPase |
| PPI | 8/10 | x3 | 24.0 | PPI degree=456 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=26 broad=33
- AF pLDDT=84.2 PDB=9
- InterPro: EF-G-like_DII; IF2_II; P-loop_NTPase
- Pfam: EF-G_D2; GTP_EFTU; IF-2
- PPI degree=456 ChIP: None
31350787: Schizosaccharomyces pombe Mti2 and Mti3 act in conjunction during mitochondrial  | 32522994: Distinct pre-initiation steps in human mitochondrial translation. | 12932832: The human mitochondrial translation initiation factor 2 gene (MTIF2): transcript

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Translation initiation factor IF-2, mitochondrial

**功能**: Mitochondrial translation initiation factor that promotes binding of formylmethionyl-tRNA to the 30S ribosomal subunits (By similarity). Also involved in the hydrolysis of GTP during the formation of the 70S ribosomal complex (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR053905 |
| InterPro | IPR044145 |
| InterPro | IPR027417 |
| InterPro | IPR005225 |
| InterPro | IPR000795 |
| InterPro | IPR000178 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

MTIF2是线粒体翻译起始因子2的核编码蛋白，在胞质合成后定位于线粒体基质，负责线粒体内70S核糖体翻译起始。其结构域架构包含三个功能模块：P-loop_NTPase结构域(IPR027417，GTP结合/水解)、EF-G-like Domain II(IPR044145，核糖体转位酶同源域)和IF2_II(IPR053905，起始tRNA结合域)，整体pLDDT=84.2揭示其结构具有良好的折叠完整性与刚性。PDB数据库中的9个结构条目主要来源于冷冻电镜解析的线粒体翻译起始复合体。

线粒体翻译机制研究表明，MTIF2的主要功能是将甲酰甲硫氨酰-tRNA(fMet-tRNA)递送至线粒体28S小亚基，并催化GTP水解驱动30S起始复合物向70S延伸复合物的转变(PMID:32522994)。然而，HPA记录中其亚细胞定位信息缺失(nan)，这与线粒体蛋白在HPA数据库中常被低估的系统性偏差一致。

PPI网络以极高置信度揭示了MTIF2与线粒体核糖体小亚基蛋白(MRPS9、MRPS5，STRING score>990)和线粒体翻译起始因子3(MTIF3，STRING=987)的物理互作。该网络结构清晰表明MTIF2嵌入于线粒体翻译起始复合体的核心模块，与MRPL2/19等大亚基组分协同完成70S组装。值得注意的是，其互作伙伴DAP3(线粒体核糖体凋亡蛋白)同时参与翻译起始与凋亡信号转导调控。

基于现有证据，MTIF2的核质定位信号并不充分——其主要功能场所在线粒体而非核质。HPA定位缺失(nan)为后续验证留下了不确定性。然而，其高PPI连接度(degree=456)和低PubMed文献数(26篇)表明该蛋白在其功能领域仍存在大量未知的调控机制，尤其在核编码线粒体蛋白如何反馈调控核基因组表达这一交叉机制上，是值得深入探索的方向。




![PAE](https://alphafold.ebi.ac.uk/files/AF-P46199-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000085760-MTIF2

![](https://images.proteinatlas.org/6021/80_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/80_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/79_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/79_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/81_E6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/61422/1135_D7_1_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000085760-MTIF2

![](https://images.proteinatlas.org/6021/80_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/80_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/79_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/79_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/81_E6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/61422/1135_D7_1_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000085760-MTIF2

![](https://images.proteinatlas.org/6021/80_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/80_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/79_E6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/79_E6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6021/81_E6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/61422/1135_D7_1_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 33**

| 42342677 | Pseudouridine synthase PUS1 and initiation factor mtIF2 are human mitoribosomal small subunit assembly factors. | Nat Commun 2026 |
| 41935065 | Mechanisms of human mitochondrial leaderless mRNA translation initiation. | Nat Commun 2026 |
| 41894431 | Transplantation of Saccharomyces cerevisiae Rmd9p peptide into mammalian mitochondrial IF2 substitutes for the IF1 funct | Microbiology (Reading) 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MTIF2

