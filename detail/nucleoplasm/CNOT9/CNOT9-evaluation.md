---
type: protein-evaluation
gene: "CNOT9"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CNOT9 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CNOT9 |
| 蛋白名称 | CCR4-NOT transcription complex subunit 9 |
| 蛋白大小 | 299 aa / 33.6 kDa |
| UniProt ID | B2RE59 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | nan (Approved) |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 299 aa |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=13 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=92.2; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | ARM-like; ARM-type_fold; CNOT9 |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=33 |
| **加权总分** | | | **132/180** | |
| **归一化总分 (÷1.83)** | | | **72.7/100** | 互证: +1 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | nan (Approved) |
| PubMed | strict=13, broad=23 |
| AlphaFold | pLDDT=92.2 |
| PDB | 0 entries |
| InterPro | ARM-like; ARM-type_fold; CNOT9 |
| Pfam | Rcd1 |
| PPI | combined degree=33 |
| ChIP | None |

### 4. 总体评价
⭐⭐⭐⭐
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: CCR4-NOT transcription complex subunit 9

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011989 |
| InterPro | IPR016024 |
| InterPro | IPR007216 |
| Pfam | PF04078 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: CCR4-NOT transcription complex subunit 9

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011989 |
| InterPro | IPR016024 |
| InterPro | IPR007216 |
| Pfam | PF04078 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

**结构域架构**：CNOT9（299 aa，33.6 kDa）是CCR4-NOT转录复合物的第九亚基，含ARM-like（IPR011989）和ARM-type_fold（IPR016024）结构域，形成典型的ARM（Armadillo）/HEAT重复螺旋束折叠。CNOT9特异性结构域（IPR007216，PF04078 Rcd1）标识其在CCR4-NOT复合物中作为适配器亚基的独特角色。ARM重复折叠形成超螺旋管状结构（弧形表面），其凸面用于蛋白质-蛋白质互作（结合CNOT1支架亚基），凹面可能参与RNA结合或与mRNA降解/翻译相关的其他因子互作。

**PPI互作网络解读**：PPI degree=33（BioGRID），但STRING共表达网络极其丰富：CNOT1（984分，CCR4-NOT核心支架）、CNOT10（980分）、CNOT6（999分，去腺苷酸酶催化亚基）、CNOT6L（974分）、CNOT4（973分，E3泛素连接酶）、CNOT8（941分）、CNOT7（846分），完整涵盖了CCR4-NOT复合物的所有主要亚基。此外MTREX（Mtr4，RNA解旋酶，核外泌体靶向复合物NEXT组分，440分）、TOB1（抗增殖蛋白，611分）、TNKS1BP1（端锚聚合酶结合蛋白，916分）的STRING连接提示CNOT9参与RNA代谢和质量控制的多个层面。

**结构解读**：AlphaFold pLDDT=92.2（本批次中最高之一），预测结构质量极佳。ARM重复折叠由串联的ARM重复单元（每个约40个残基，形成2个α-螺旋）堆叠构成右手超螺旋。高pLDDT反映该折叠在无配体状态下也非常稳定——ARM重复蛋白倾向于形成刚性骨架，互作界面通常位于超螺旋的凹面或端部。CNOT9的Rcd1结构域表面富含保守的疏水性残基和芳香族残基，提示其互作界面涉及蛋白-蛋白而非蛋白-核酸接触。

**机制模型**：CNOT9在CCR4-NOT复合物中充当模块化适配器（modular adaptor），连接CNOT1支架与下游效应蛋白：（1）通过ARM重复结构域与CNOT1的MIF4G结构域结合，锚定于复合物中央平台；（2）可能通过与TOB1等BTG/TOB家族抗增殖蛋白的互作，招募CCR4-NOT至特定mRNA群体（如含ARE元件的mRNA）实现靶向mRNA降解；（3）CCR4-NOT复合物在核质中的功能涉及转录延伸/终止调控和核RNA质量控制——CNOT9可能在核内作为mRNA输出前的监测因子，通过CNOT6/CNOT6L的去腺苷酸酶活性标记异常转录本进行核内降解。

**TE调控展望**：CCR4-NOT复合物已被报道参与LINE-1和ERV等TE转录本的降解（核RNA质量控制机制去除异常/高拷贝TE RNA），CNOT9作为复合物的结构性亚基间接参与这一过程。其在核质中的定位（Approved）与CCR4-NOT核内亚复合物的功能一致。虽然CNOT9不具有序列特异性RNA结合能力（适配器而非识别亚基），但CCR4-NOT复合物整体的TE RNA降解功能对维持基因组稳定性和防止TE异常表达至关重要。在此过程中，CNOT9的作用是为去腺苷酸酶（CNOT6/CNOT6L）提供正确的亚细胞定位和底物呈递平台。


![PAE](https://alphafold.ebi.ac.uk/files/AF-B2RE59-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000144580-CNOT9

![](https://images.proteinatlas.org/46622/622_G6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/46622/622_G6_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/46622/619_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46622/619_G6_4_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000144580-CNOT9

![](https://images.proteinatlas.org/46622/622_G6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/46622/622_G6_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/46622/619_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46622/619_G6_4_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000144580-CNOT9

![](https://images.proteinatlas.org/46622/622_G6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/46622/622_G6_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/46622/619_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46622/619_G6_4_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 23**

| 42239063 | A BRRF1-CCR4-NOT axis underlies conserved transcriptome-wide loss of splicing fidelity during gammaherpesvirus reactivat | bioRxiv 2026 |
| 39856550 | Whole-genome resequencing landscape of adaptive evolution in Relict gull (Larus relictus). | BMC Genomics 2025 |
| 39131325 | The Unkempt RNA binding protein reveals a local translation program in centriole overduplication. | bioRxiv 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CNOT9

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CNOT2 | STRING | 671 |
| MTREX | STRING | 440 |
| CPEB3 | STRING | 620 |
| CNOT11 | STRING | 635 |
| CNOT1 | STRING | 984 |
| CNOT3 | STRING | 875 |
| CNOT7 | STRING | 846 |
| TNRC6A | STRING | 503 |
| CNOT10 | STRING | 980 |
| CNOT6L | STRING | 974 |
| TOB1 | STRING | 611 |
| CNOT8 | STRING | 941 |
| TNKS1BP1 | STRING | 916 |
| CNOT4 | STRING | 973 |
| CNOT6 | STRING | 999 |
