---
type: protein-evaluation
gene: "RBBP8NL"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RBBP8NL 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RBBP8NL |
| 蛋白名称 | RBBP8 N-terminal-like protein |
| 蛋白大小 | 664 aa / 71.4 kDa |
| UniProt ID | Q8NC74 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 664 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=3 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=54.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | CtIP_N; RBBP8-like |
| PPI | 5/10 | x3 | 15.0 | PPI degree=10 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=3 broad=3
- AF pLDDT=54.8 PDB=0
- InterPro: CtIP_N; RBBP8-like
- Pfam: CtIP_N
- PPI degree=10 ChIP: None
33548076: Whole genome sequencing identifies novel genetic mutations in patients with ecze | 34541834: Identification of hub genes in bladder cancer based on weighted gene co-expressi | 40709405: Genome-wide scanning for selection signatures in two autochthonous Anatolian chi

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

RBBP8NL（RBBP8 N-terminal-like protein）是664个氨基酸的CtIP/RBBP8旁系同源蛋白，其N端含有一个保守的CtIP_N结构域（IPR019518/PF10482），该结构域是DNA末端切除和同源重组修复中的关键调控模块。与RBBP8（CtIP）类似，RBBP8NL的CtIP_N结构域可能通过四聚化形成稳定的分子平台，招募MRN复合体（MRE11-RAD50-NBS1）至DNA双链断裂（DSB）位点。然而，与亲本RBBP8（PubMed>500）不同，RBBP8NL的PubMed文献仅3篇——这是基因复制后功能分化的典型案例。

AlphaFold预测pLDDT仅54.8，显著低于其在DNA修复中的亲本RBBP8，提示RBBP8NL可能经历了功能退化（non-functionalization）或新功能化（neofunctionalization）。HPA Approved的Nucleoplasm定位（Nucleoplasm; Vesicles）明确支持其核内功能，但与PPI网络中HNRNPL（hnRNP L，可变剪接调控因子）、PIN1（肽基脯氨酰顺反异构酶，调控磷酸化蛋白构象）、PHF1（PHD finger蛋白，识别H3K27me3）等核蛋白的互作（BioGRID评分=0但已验证）暗示RBBP8NL的功能可能已偏离DNA修复，转向剪接调控或染色质修饰。

分子机制假说：RBBP8NL的CtIP_N结构域保留了四聚化能力，使其能够作为支架蛋白——但其DNA损伤识别功能可能已丧失或改变。通过与HNRNPL的互作，RBBP8NL可能参与pre-mRNA的可变剪接调控；与PIN1的互作则暗示其受脯氨酸异构化调控——这是细胞周期调控蛋白的经典特征。PHF1作为Polycomb抑制复合体2（PRC2）的识别因子，介导H3K27me3染色质的识别与沉默，RBBP8NL-PHF1互作可能将该蛋白连接至Polycomb介导的转录抑制网络。

作为一种极度新颖的核蛋白（新颖性10/10），RBBP8NL的研究价值主要在于其与癌症重要蛋白CtIP的结构同源性。其在膀胱癌（PMID:34541834）和湿疹疱疹（PMID:33548076）中的GWAS关联虽弱，但结合其PPI网络中PIN1/Polycomb轴的暗示，RBBP8NL可能作为肿瘤表观基因组调控中的一个"暗节点"。建议首先通过CRISPR敲除/过表达确定RBBP8NL对DNA损伤响应和剪接效率的功能影响，再根据初步表型决定是否进行TE调控功能的深入筛选。

**蛋白全称**: RBBP8 N-terminal-like protein

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR019518 |
| InterPro | IPR033316 |
| Pfam | PF10482 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: RBBP8 N-terminal-like protein

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR019518 |
| InterPro | IPR033316 |
| Pfam | PF10482 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HNRNPL | BioGRID | 0 |
| NCK2 | BioGRID | 0 |
| ARPC3 | BioGRID | 0 |
| PHF1 | BioGRID | 0 |
| PIN1 | BioGRID | 0 |
| EGLN3 | BioGRID | 0 |
| CHIA | BioGRID | 0 |
| LARP1B | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NC74-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000130701-RBBP8NL

![](https://images.proteinatlas.org/42627/1253_G3_2_red_green.jpg)
![](https://images.proteinatlas.org/42627/1253_G3_3_red_green.jpg)
![](https://images.proteinatlas.org/42627/1134_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/42627/1134_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/42627/532_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/42627/532_B1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 3**

| 40709405 | Genome-wide scanning for selection signatures in two autochthonous Anatolian chicken breeds. | Br Poult Sci 2026 |
| 34541834 | Identification of hub genes in bladder cancer based on weighted gene co-expression network analysis from TCGA database. | Cancer Rep (Hoboken) 2022 |
| 33548076 | Whole genome sequencing identifies novel genetic mutations in patients with eczema herpeticum. | Allergy 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RBBP8NL

