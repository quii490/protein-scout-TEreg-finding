---
type: protein-evaluation
gene: "PTPDC1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PTPDC1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PTPDC1 |
| 蛋白名称 | Protein tyrosine phosphatase domain-containing protein 1 |
| 蛋白大小 | 754 aa / 84.5 kDa |
| UniProt ID | A2A3K4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 754 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=4 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=70.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Dual-sp_phosphatase_cat-dom; Prot-tyrosine_phosphatase-like; PTP |
| PPI | 6/10 | x3 | 18.0 | PPI degree=69 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=4 broad=5
- AF pLDDT=70.0 PDB=0
- InterPro: Dual-sp_phosphatase_cat-dom; Prot-tyrosine_phosphatase-like; PTP
- Pfam: DSPc
- PPI degree=69 ChIP: None
31889940: The plasma peptides of breast versus ovarian cancer. | 26227905: A Pooling Genome-Wide Association Study Combining a Pathway Analysis for Typical | 37229194: Whole-exome identifies germline variants in families with obstructive sleep apne

### 4. 总体评价
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein tyrosine phosphatase domain-containing protein 1

**功能**: May play roles in cilia formation and/or maintenance

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000340 |
| InterPro | IPR029021 |
| InterPro | IPR050561 |
| InterPro | IPR049573 |
| InterPro | IPR016130 |
| InterPro | IPR003595 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

PTPDC1（Protein tyrosine phosphatase domain-containing protein 1）是本批次中结构域信息最具酶学深度的候选蛋白之一，尽管其生物学功能研究极度匮乏。结构域架构包括：Dual-sp_phosphatase_cat-dom（IPR000340）——双特异性磷酸酶催化域、Prot-tyrosine_phosphatase-like（IPR029021）、PTP（IPR050561/IPR049573）以及蛋白酪氨酸磷酸酶折叠（IPR016130）和酪氨酸蛋白磷酸酶活性位点（IPR003595）。Pfam注释为DSPc（PF00782），确认了其双特异性磷酸酶（DSP）的身份。754个氨基酸（84.5 kDa）的大分子量表明PTPDC1除了PTP催化域外还含有大量的辅助结构域或调控区域。然而，pLDDT仅为70.0，提示存在大量无序区域，这些区域可能用于支架蛋白功能或翻译后修饰调控。

双特异性磷酸酶（DSPs）是蛋白磷酸酶的重要亚家族，能够同时去磷酸化磷酸酪氨酸和磷酸丝氨酸/磷酸苏氨酸残基，在细胞信号转导中作为关键的负调控因子。在核内，DSPs主要参与MAPK信号通路的去磷酸化失活——包括ERK1/2、JNK和p38，从而直接调控转录因子的活性。PTPDC1的cytosol/nucleoplasm双重定位与其作为信号调控磷酸酶的预期亚细胞分布一致。值得注意的是，UniProt注释提示PTPDC1"可能在纤毛形成和/或维护中发挥作用"——纤毛作为细胞信号中枢，其形成和功能依赖MAPK通路的精密调控。

PPI网络提供了关键的机制线索。STRING数据显示PPP2R2A（784分，蛋白磷酸酶2A的调控亚基B55α）和BioGRID数据中的MAPK1（ERK2）、MAPK3（ERK1）、PPP2CA（PP2A催化亚基）和PPP2R1A（PP2A支架亚基Aα）揭示PTPDC1与丝/苏氨酸磷酸酶PP2A复合体之间存在密切关联。XPO1（Exportin-1/CRM1）的互作提示核输出信号（NES）介导的核质穿梭调控。USP9X的互作涉及去泛素化修饰调控。FBXO3（F-box蛋白3）作为SCF泛素连接酶的底物识别亚基，暗示PTPDC1可能受到泛素-蛋白酶体系统的降解调控。

从TE调控角度，PTPDC1的潜在影响力通过MAPK信号通路实现。MAPK通路（ERK、JNK、p38）是TE元件转录激活的主要驱动力之一——环境应激（热激、氧化应激、DNA损伤）激活的MAPK信号可直接磷酸化转录因子（如HSF1、AP-1、ATF2），进而结合TE元件的启动子区域驱动其转录。PTPDC1作为MAPK信号的负调控磷酸酶，可能通过维持MAPK通路的基础抑制状态来限制TE的异常转录。此外，PP2A是异染色质稳定性的关键调控因子——PP2A通过去磷酸化HP1α调控其与H3K9me3的结合，直接影响异染色质区域的完整性。PTPDC1-PP2A的互作可能通过这一轴间接调控转座子元件的表观遗传沉默。PubMed strict=4篇的极端新颖性和PTP催化域的深度酶学潜力使PTPDC1成为值得优先进行功能验证的候选蛋白。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PPP2R2A | STRING | 784 |
| XPO1 | BioGRID | 1 |
| FBXO3 | BioGRID | 1 |
| MAPK1 | BioGRID | 1 |
| MAPK3 | BioGRID | 1 |
| PPP2CA | BioGRID | 1 |
| PPP2R1A | BioGRID | 1 |
| USP9X | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-A2A3K4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000158079-PTPDC1

![](https://images.proteinatlas.org/16747/956_H10_3_red_green.jpg)
![](https://images.proteinatlas.org/16747/956_H10_4_red_green.jpg)
![](https://images.proteinatlas.org/16747/1061_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/16747/1061_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/16747/954_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/16747/954_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/26832/231_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/26832/231_D2_2_red_green.jpg)

### PubMed 文献

**PubMed count: 5**

| 37229194 | Whole-exome identifies germline variants in families with obstructive sleep apnea syndrome. | Front Genet 2023 |
| 34803498 | Circ-PTPDC1 promotes the Progression of Gastric Cancer through Sponging Mir-139-3p by Regulating ELK1 and Functions as a | Int J Biol Sci 2021 |
| 31889940 | The plasma peptides of breast versus ovarian cancer. | Clin Proteomics 2019 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PTPDC1

