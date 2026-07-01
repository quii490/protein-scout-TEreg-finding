---
type: protein-evaluation
gene: "RANGRF"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## RANGRF 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RANGRF |
| 蛋白名称 | Ran guanine nucleotide release factor |
| 蛋白大小 | 186 aa / 20.4 kDa |
| UniProt ID | Q9HD47 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32.0 | Cytosol; Nucleoplasm (Supported) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 186 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=7 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=78.0; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Mog1; Mog1/PsbP_a/b/a-sand |
| PPI | 5/10 | x3 | 15.0 | PPI degree=41 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +2 |

### 3. 分析
HPA: Cytosol; Nucleoplasm (Supported)
PubMed: strict=7, broad=10
AF pLDDT: 78.0  PDB: 1
InterPro: Mog1; Mog1/PsbP_a/b/a-sand
Pfam: Mog1
PPI degree: 41  ChIP: None
**Papers**: 20301690: Brugada Syndrome. | 24142675: Brugada syndrome and p.E61X_RANGRF. | 28796037: Functional prediction of miR-3144-5p in human cardiac myocytes based on transcri

### 4. 总体评价
★★★★  **73.8/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ran guanine nucleotide release factor

**功能**: May regulate the intracellular trafficking of RAN (PubMed:11290418). Promotes guanine nucleotide release from RAN and inhibits binding of new GTP by preventing the binding of the RAN guanine nucleotide exchange factor RCC1 (PubMed:29040603). Regulates the levels of GTP-bound RAN in the nucleus, and thereby plays a role in the regulation of RAN-dependent mitotic spindle dynamics (PubMed:29040603). Enhances the expression of SCN5A at the cell membrane in cardiomyocytes (PubMed:18184654, PubMed:216

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR007681 |
| InterPro | IPR016123 |
| Pfam | PF04603 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RAN | BioGRID | 0 |
| THUMPD1 | BioGRID | 0 |
| HGS | BioGRID | 0 |
| ZDHHC17 | BioGRID | 0 |
| PHF19 | BioGRID | 0 |
| RAB3A | BioGRID | 0 |
| SGCZ | BioGRID | 0 |
| AGO3 | BioGRID | 0 |


### 深度机制分析

RANGRF（也称为MOG1）编码Ran鸟嘌呤核苷酸释放因子，其结构域架构由Mog1结构域（InterPro: IPR007681; Pfam: PF04603）和Mog1/PsbP α/β/α-三明治折叠（IPR016123）组成。该蛋白通过独特的"双重调控"模式控制核内Ran-GTP水平：一方面促进Ran释放结合的GDP/GTP，另一方面阻止RanGEF（RCC1）催化新GTP的结合（PMID:29040603）。HPA定位为Cytosol/Nucleoplasm（Supported, 核定位特异性8/10），与其功能——调节Ran依赖的有丝分裂纺锤体动力学——高度一致。蛋白较小（186 aa / 20.4 kDa），但AlphaFold pLDDT=78.0且具有一个实验性PDB条目，表明其折叠状态明确。

RanGTPase系统是真核细胞核质转运和有丝分裂纺锤体组装的核心分子开关。RANGRF作为Ran的"双向刹车"——同时切割核苷酸释放并阻断RCC1的再装载——其在核质中的定位使其能通过微调局部Ran-GTP梯度来影响核孔复合物（NPC）处的转运受体（importin/exportin）与货物蛋白的解离/结合动力学。此外，RANGRF在心肌细胞中增强SCN5A（NaV1.5钠通道）膜表达的能力（PMID:18184654）暗示其功能不仅限于Ran调控，可能通过未知机制将核质信号与离子通道运输偶联。

PPI网络核心互作对象为RAN（BioGRID评分0，但功能意义最高）及多个具有核功能的蛋白（PHF19是PRC2多梳抑制复合物的辅助因子，AGO3参与核内小RNA介导的基因沉默）。THUMPD1的互作暗示tRNA/RNA修饰相关功能的潜在交叉。与Brugada综合征的临床关联（PMID:24142675, RANGRF p.E61X无义突变）为理解核质Ran信号与心脏电生理之间的致病机制提供了独特的切入点。7篇PubMed使其成为高度新颖靶标，其作为Ran系统"非经典调节器"的精细分子机制（特别是阻止RCC1结合的结构基础）仍是开放问题。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9HD47-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000108961-RANGRF

![](https://images.proteinatlas.org/57280/972_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/57280/972_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/57280/942_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/57280/942_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/57280/955_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/57280/955_A10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 10**

| 37796154 | From Death to Life/Back to the Future: Detailed Premorbid Clinical and Family History Can Save Lives and Address the Fin | Appl Immunohistochem Mol Morphol 2023 |
| 37327621 | Generation of a homozygous RANGRF knockout hiPSC line by CRISPR/Cas9 system. | Stem Cell Res 2023 |
| 20301690 | Brugada Syndrome. |  1993 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RANGRF

