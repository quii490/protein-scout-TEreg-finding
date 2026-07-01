---
type: protein-evaluation
gene: "GXYLT2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GXYLT2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GXYLT2 |
| 蛋白名称 | Glucoside xylosyltransferase 2 |
| 蛋白大小 | 443 aa / 51.1 kDa |
| UniProt ID | A0PJZ3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytokinetic bridge; Midbody ring; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 443 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=13 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=83.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Glyco_trans_8; Glycosyltransferase_8; Nucleotide-diphossugar_trans |
| PPI | 5/10 | x3 | 15.0 | PPI degree=27 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Cytokinetic bridge; Midbody ring; Nucleoplasm (Approved)
- PubMed strict=13 broad=24
- AF pLDDT=83.1 PDB=0
- InterPro: Glyco_trans_8; Glycosyltransferase_8; Nucleotide-diphossugar_trans
- Pfam: Glyco_transf_8
- PPI degree=27 ChIP: None
34506251: Glucoside xylosyltransferase 2 as a diagnostic and prognostic marker in gastric  | 40903443: Pathogenic glycosyltransferase genes and potential therapeutic drugs in pressure | 36263004: Prognostic Signature GXYLT2 Is Correlated with Immune Infiltration in Bladder Ca

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Glucoside xylosyltransferase 2

**功能**: Glycosyltransferase which elongates the O-linked glucose attached to EGF-like repeats in the extracellular domain of Notch proteins by catalyzing the addition of xylose

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002495 |
| InterPro | IPR051993 |
| InterPro | IPR029044 |
| Pfam | PF01501 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FBL | BioGRID | 1 |
| SRPK2 | BioGRID | 1 |
| CD70 | BioGRID | 1 |
| NEUROG3 | BioGRID | 1 |
| KLRG2 | BioGRID | 1 |
| TRIM25 | BioGRID | 1 |
| PPCS | BioGRID | 1 |
| HSPA8 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-A0PJZ3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000172986-GXYLT2

![](https://images.proteinatlas.org/68429/1414_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/68429/1414_H6_3_red_green.jpg)
![](https://images.proteinatlas.org/68429/1335_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/68429/1335_C10_4_red_green.jpg)
![](https://images.proteinatlas.org/68429/1352_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/68429/1352_C10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 24**

| 41492474 | GXYLT2 serves as a prognostic biomarker and is associated with β-catenin activation and gastric cancer aggressiveness. | Genes Dis 2026 |
| 41140820 | XXYLT1 inhibits NOTCH1 activation in Jurkat cells while promoting cell proliferation. | Nagoya J Med Sci 2025 |
| 40903443 | Pathogenic glycosyltransferase genes and potential therapeutic drugs in pressure overload-induced heart failure. | ESC Heart Fail 2025 |

### 深度机制分析

GXYLT2（443 aa, 51.1 kDa）属于糖基转移酶8家族（GT8, Glyco_transf_8, IPR002495），其结构域架构以GT8催化结构域为核心，并具有核苷酸-二磷酸糖结合折叠（Nucleotide-diphossugar_trans, IPR029044）。GT8家族酶催化糖基从核苷酸-糖供体转移至受体底物的α-连接反应，GXYLT2的特异性底物为Notch蛋白胞外域EGF样重复序列上的O-连接葡萄糖，负责在葡萄糖残基上添加木糖以延伸糖链。AlphaFold预测pLDDT=83.1，GT8折叠预测质量较高，但活性位点环区的精确构象需要实验结构验证。

GXYLT2的生化意义在于其对Notch信号通路的直接调控。Notch受体在细胞表面被配体激活后经历蛋白酶解，释放Notch胞内域（NICD）转位至核内激活转录。EGF重复序列的O-糖基化（包括葡萄糖和木糖延伸）精细调控Notch-配体互作的亲和力和Notch激活阈值。因此GXYLT2通过控制Notch蛋白的糖基化修饰间接调控NICD的核转位和随后的转录激活，包括可能激活TE来源的增强子或启动子。

HPA定位为Cytokinetic bridge; Midbody ring; Nucleoplasm（Approved级别），其中Nucleoplasm定位使GXYLT2直接进入TE调控的视野。胞质分裂桥和中间体的定位与其糖基转移酶活性在执行有丝分裂最后阶段的潜在功能一致——可能参与中间体脱落时所需膜糖蛋白的修饰。PPI网络（BioGRID degree=27）中，与FBL（纤维蛋白，核仁rRNA甲基转移酶）、SRPK2（SR剪接因子激酶）、TRIM25和HSPA8（分子伴侣）的互作提示GXYLT2在核质/核仁中可能通过与剪接因子和伴侣蛋白协作来影响RNA加工。

文献证据强烈指向GXYLT2作为肿瘤诊断和预后标志物：在胃癌（PMID:34506251；PMID:41492474）和膀胱癌（PMID:36263004）中高表达，且与β-catenin激活（胃癌侵袭性）关联。压力超负荷心衰中GXYLT2表达受致病性糖基转移酶网络调控（PMID:40903443）。在TE调控层面，GXYLT2可能通过两种机制参与：其一，通过Notch-NICD通路间接调控TE位点——NICD/RBPJ复合物可能结合TE来源的增强子；其二，GXYLT2在核质中的存在可能允许其糖基化核质蛋白（包括转录因子或组蛋白），从而影响染色质结构和TE转录。但需特别注意GXYLT2是高尔基体/ER定位的糖基转移酶，核定位可能代表新合成蛋白的短暂ER-核膜关联，而非功能性核定位。

