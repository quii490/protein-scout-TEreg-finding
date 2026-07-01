---
type: protein-evaluation
gene: "EXOSC6"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## EXOSC6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | EXOSC6 |
| 蛋白名称 | Exosome complex component MTR3 |
| 蛋白大小 | 272 aa / 28.2 kDa |
| UniProt ID | Q5RKV6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 272 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=7 |
| 🏗️ 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=80.4; PDB=8 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | ExoRNase_PH_dom1; ExoRNase_PH_dom2_sf; PNPase/RNase_PH_dom_sf |
| 🔗 PPI | 7/10 | ×3 | 21.0 | PPI degree=136 |
| **加权总分** | | | **133/180** | |
| **归一化总分 (÷1.83)** | | | **73.8/100** | 互证: +2 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | nan (nan) |
| PubMed | strict=7, broad=9 |
| AlphaFold | pLDDT=80.4 |
| PDB | 8 entries |
| InterPro | ExoRNase_PH_dom1; ExoRNase_PH_dom2_sf; PNPase/RNase_PH_dom_sf |
| Pfam | RNase_PH |
| PPI | combined degree=136 |
| ChIP | None |

### 4. 总体评价
⭐⭐⭐⭐
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Exosome complex component MTR3

**功能**: Non-catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with processing defe

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001247 |
| InterPro | IPR036345 |
| InterPro | IPR027408 |
| InterPro | IPR020568 |
| InterPro | IPR050080 |
| Pfam | PF01138 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

EXOSC6(MTR3)是RNA外切体(Exosome)复合体的非催化核心亚基。RNA外切体是细胞RNA代谢的中心机器，具有3'→5'外切核酸酶活性。EXOSC6本身无催化活性，但其ExoRNase_PH_dom1(IPR001247)和ExoRNase_PH_dom2_sf(IPR036345)结构域构成RNase PH-like环状骨架，与EXOSC4/5/7等其他PH-like亚基共同形成六元环结构，为全酶的组装提供结构基座。pLDDT=80.4且PDB有8个结构条目(多数为冷冻电镜结构)，反映了该复合体在结构生物学中的成熟研究状态。

核质定位的RNA外切体通过EXOSC10(RRP6)亚基锚定于核膜内侧和核仁。EXOSC6所在的PH-ring将底物RNA通道化递送至催化亚基EXOSC10和DIS3的活性位点。在核质中，RNA外切体的底物谱极其广泛：核糖体RNA前体(pre-rRNA)的3'修剪、snRNA和snoRNA的成熟加工、PROMT(启动子上游转录本)和抗义RNA的监看降解、以及加工缺陷mRNA的质控清除。EXOSC6的PPI网络以STRING score=999的高置信度呈现完整的9亚基外切体互作组(EXOSC1-5/7/10加上MPHOSPH6辅因子)，这种全通路覆盖的PPI模式是结构稳定的多亚基复合体的典型特征。

该蛋白的功能逻辑可从核酸外切酶缺陷导致的人类疾病中洞察。RNA外切体亚基突变可引起RNA加工障碍——从Pontocerebellar Hypoplasia(EXOSC3突变)到Trichohepatoenteric Syndrome(SKI2/SKI3突变)。EXOSC6在肺癌中已有表达异常的报道(PMID:42171853)，提示其在肿瘤转录组重编程中的潜在角色。

EXOSC6的一个关键机制问题是：非催化亚基是否具有独立的结构域调控功能？其ExoRNase_PH_dom2_sf虽然缺乏催化残基，但可能通过变构方式调控催化亚基(EXOSC10/DIS3)的活性，或作为特定RNA底物的适配器(Adaptor)影响底物偏好的选择。然而，HPA的核定位数据为nan(缺失)，这需要通过免疫荧光进一步确认。PubMed仅7篇，研究新颖性极高，结构信息丰富(PDB=8)，二者结合使EXOSC6成为结构导向的药物设计靶点。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5RKV6-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 9**

| 42171853 | Comprehensive bioinformatics analysis of EXOSC family genes in lung adenocarcinoma. | Discov Oncol 2026 |
| 40588408 | [Multi-omics Mendelian randomization study on the causality between non-ionizing radiation and facial aging]. | Zhonghua Shao Shang Yu Chuang Mian Xiu Fu Za Zhi 2025 |
| 37315317 | Alterations in the expression pattern of RBC membrane associated proteins (RMAPs) in whole body γ-irradiated Sprague Daw | Int J Radiat Biol 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/EXOSC6

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| EXOSC5 | STRING | 999 |
| MPHOSPH6 | STRING | 999 |
| EXOSC7 | STRING | 999 |
| EXOSC4 | STRING | 999 |
| EXOSC3 | STRING | 999 |
| EXOSC1 | STRING | 999 |
| EXOSC2 | STRING | 999 |
| EXOSC10 | STRING | 999 |
| DIS3 | STRING | 999 |
| EXOSC9 | STRING | 999 |
| EXOSC8 | STRING | 999 |
| C1D | STRING | 997 |
| LRP1 | STRING | 997 |
| MTREX | STRING | 995 |
| ZFC3H1 | STRING | 948 |
| PSMB1 | physical | Lehner B (2004) |
| LSM1 | physical | Lehner B (2004) |
| LSM7 | physical | Lehner B (2004) |
| LSM8 | physical | Lehner B (2004) |
| DNAJC30 | physical | Lehner B (2004) |

