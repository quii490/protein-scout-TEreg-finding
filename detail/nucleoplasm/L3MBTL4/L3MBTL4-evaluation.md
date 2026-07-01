---
type: protein-evaluation
gene: "L3MBTL4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted TE_REG_CANDIDATE]
status: shortlisted
---

## L3MBTL4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | L3MBTL4 |
| 蛋白名称 | Lethal(3)malignant brain tumor-like protein 4 |
| 蛋白大小 | 623 aa / 71.1 kDa |
| UniProt ID | Q8NA19 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 623 aa |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=16 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=74.8; PDB=0 |
| 🧬 调控结构域 | 6/10 | ×2 | 12.0 | Mbt; PcG_chromatin_remod_factors; SAM |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=22 |
| **加权总分** | | | **132/180** | |
| **归一化总分 (÷1.83)** | | | **72.7/100** | 互证: +1 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | Nucleoplasm; Vesicles (Approved) |
| PubMed | strict=16, broad=19 |
| AlphaFold | pLDDT=74.8 |
| PDB | 0 entries |
| InterPro | Mbt; PcG_chromatin_remod_factors; SAM |
| Pfam | MBT; SAM_1; zf-C2HC |
| PPI | combined degree=22 |
| ChIP | None |

### 4. 总体评价
⭐⭐⭐⭐
**72.7/100** | **nucleoplasm**
TE regulatory candidate — Mbt; PcG_chromatin_remod_factors; SAM


### 补充分析 (UniProt API)

**蛋白全称**: Lethal(3)malignant brain tumor-like protein 4

**功能**: Putative Polycomb group (PcG) protein. PcG proteins maintain the transcriptionally repressive state of genes, probably via a modification of chromatin, rendering it heritably changed in its expressibility (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004092 |
| InterPro | IPR050548 |
| InterPro | IPR001660 |
| InterPro | IPR013761 |
| InterPro | IPR002515 |
| Pfam | PF02820 |

### 深度机制分析

L3MBTL4（lethal(3)malignant brain tumor-like protein 4，UniProt: Q8NA19）是Polycomb group（PcG）蛋白家族的推定成员。其结构域架构高度特征化：N端含有MBT（malignant brain tumor）重复域（PF02820），每个MBT重复呈β折叠桶结构，可识别单甲基化和二甲基化赖氨酸残基；中部为C2HC型锌指（zf-C2HC），具有潜在的核酸或蛋白结合能力；C端为SAM（sterile alpha motif）结构域（IPR013761），已知介导同源/异源寡聚化形成蛋白聚合物支架。这种"阅读器（MBT）-效应器（C2HC）-组装模块（SAM）"的线性排列是典型的染色质调控蛋白架构。

PcG蛋白功能的核心在于维持基因转录抑制状态，通过修饰染色质使其呈现可遗传的表达性改变。L3MBTL4的MBT结构域与L3MBTL1-3高度保守，它们均通过MBT重复识别H3K20me1/2和H4K20me1/2，在DNA损伤应答和复制叉稳定性维持中发挥功能。SAM结构域可产生螺旋状聚合物，类似于Drosophila Polyhomeotic（Ph）蛋白的SAM聚合机制，将PcG蛋白组织成染色质上的高密度抑制性复合体。

然而，AlphaFold v6预测的pLDDT仅为74.8，有序区域比例不高，无明显PDB条目覆盖——这可能反映了SAM结构域在未聚合状态下存在构象柔性和IDR区域。HPA定位为nucleoplasm与vesicles双重定位（Approved级），这与经典PcG蛋白的核内染色质定位不完全一致，extra-nucleoplasmic的囊泡信号可能代表胞质转运中间体或分泌途径定位的次要组分。

PPI网络显示L3MBTL4与L3MBTL3互作（BioGRID），后者是同家族中研究最深入的MBT染色质阅读器，提示可能通过MBT-SAM串联组装形成异源聚合物。与KPNA3（importin alpha 3，核输入受体）的互作暗示其入核运输依赖于经典的importin α/β通路。与HSF2BP（热休克因子结合蛋白，减数分裂重组调控因子）的互作则指向潜在的减数分裂/DNA修复相关功能的交叉。值得注意的是，PubMed文献中L3MBTL4表观遗传沉默与食管癌DNA-PKcs抑制剂敏感性相关（PMID: 41876459），DNA-PKcs是非同源末端连接（NHEJ）修复的核心激酶——结合MBT结构域对H4K20me（53BP1招募信号）的识别能力，L3MBTL4可能在DNA双链断裂修复途径选择（HR vs NHEJ）中扮演染色质阅读器-信号整合器的角色。TE调控方面，作为PcG蛋白，L3MBTL4可能通过维持逆转录转座子及其他重复元件的H3K27me3/H2AK119ub抑制性标记，但直接的ChIP或靶向实验数据仍然缺乏。

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 1 |
| L3MBTL3 | BioGRID | 1 |
| PSMB5 | BioGRID | 1 |
| PSMD14 | BioGRID | 1 |
| KPNA3 | BioGRID | 1 |
| HSF2BP | BioGRID | 1 |
| PMM2 | BioGRID | 1 |
| GAPDHS | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NA19-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000154655-L3MBTL4

![](https://images.proteinatlas.org/69042/1581_C9_4_red_green.jpg)
![](https://images.proteinatlas.org/69042/1581_C9_7_red_green.jpg)
![](https://images.proteinatlas.org/69042/1374_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/69042/1374_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/69042/1376_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/69042/1376_F3_3_red_green.jpg)

### PubMed 文献

**PubMed count: 19**

| 41876459 | Epigenetic silencing L3MBTL4 sensitizes esophageal cancer to DNA-PKcs inhibitor. | Cancer Biol Ther 2026 |
| 41694402 | Mendelian randomization and transcriptome analysis reveal depression-driven regulatory patterns of the immune microenvir | Front Immunol 2026 |
| 40595878 | LncRNAs regulates cell death in osteosarcoma. | Sci Rep 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/L3MBTL4

