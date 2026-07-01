---
type: protein-evaluation
gene: "PCDHGC5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGC5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGC5 |
| 蛋白名称 | Protocadherin gamma-C5 |
| 蛋白大小 | 944 aa / 101.9 kDa |
| UniProt ID | Q9Y5F6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 944 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=6 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=74.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 5/10 | x3 | 15.0 | PPI degree=22 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=6 broad=8
- AF pLDDT=74.4 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_C
- Pfam: Cadherin; Cadherin_2; Cadherin_C_2
- PPI degree=22 ChIP: None
32049967: Selection in Australian Thoroughbred horses acts on a locus associated with earl | 34367733: Autoantibody profiling of alveolar rhabdomyosarcoma patients unveils tumor-assoc | 38308496: Synaptic adhesion molecule protocadherin-γC5 mediates β-amyloid-induced neuronal

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

PCDHGC5（Protocadherin gamma-C5）是原钙粘蛋白γ簇的一员，拥有944 aa的大分子量和经典的钙粘蛋白结构域架构：N端胞外区含有6个钙粘蛋白重复结构域（InterPro IPR002126, IPR015919），负责Ca²⁺依赖的同嗜性细胞黏附，C端含有一个保守的钙粘蛋白胞内结构域（Pfam Cadherin_C_2, InterPro IPR032455）。AlphaFold2预测pLDDT=74.4，无独立PDB结构，但钙粘蛋白折叠已有大量同源模板支持，结构预测相对可靠。

PCDHGC5的PPI网络度为22，关键互作伙伴揭示了其在神经生物学中的核心角色。与APP（淀粉样前体蛋白）的BioGRID互作在神经退行性疾病背景下尤为重要——APP的胞内结构域（AICD）是核内转录调控因子，PCDHGC5可能通过调控APP的加工或转运影响AICD的核内信号输出。与NEK4（NIMA相关激酶4）的互作提示PCDHGC5可能参与细胞周期或纤毛相关信号通路，这与原钙粘蛋白γ簇在神经元特异性连接建立和维持中的功能一致。

最新研究（PMID:38308496）揭示了PCDHGC5在阿尔茨海默病中的直接病理作用：突触黏附分子PCDHGC5介导β-淀粉样蛋白诱导的神经元过度兴奋和认知缺陷。这一发现颠覆了传统认知——原钙粘蛋白不仅是被动的结构黏附分子，更是主动的信号传导者，能够将胞外Aβ信号转导为胞内毒性应答。在核质环境中，PCDHGC5的胞内结构域可能被γ-分泌酶或类似蛋白酶剪切后入核，参与基因表达调控，这一机制已在γ-原钙粘蛋白家族的恒定区中被证实。

PCDHGC5属于核质蛋白中最具研究新颖性的类型（PubMed=6，得分10/10），且HPA定位明确（Nucleoplasm Approved，得分9/10）。其最大特色在于"膜蛋白核定位"的非经典分布模式——从一个经典的细胞黏附分子转变为核内功能执行者，这种双重身份在肿瘤发生和神经退行性疾病中可能具有关键的病理意义。PMID:41818197的最新研究建立了Pcdhgc5突变小鼠模型，证实γC5亚型并非发育必需，但其在应激和病理条件下的功能仍有待深入探索。

### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin gamma-C5

**功能**: Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR032455 |
| InterPro | IPR031904 |
| InterPro | IPR020894 |
| InterPro | IPR013164 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 0 |
| NEK4 | BioGRID | 0 |
| PNPLA6 | BioGRID | 0 |
| ITPRIP | BioGRID | 0 |
| FAM189B | BioGRID | 0 |
| PTPRU | BioGRID | 0 |
| MLYCD | BioGRID | 0 |
| NXPE3 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5F6-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000240764-PCDHGC5

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 8**

| 41818197 | A new mouse mutant with a discrete mutation in Pcdhgc5 reveals that the Protocadherin γC5 isoform is not essential for d | PLoS One 2026 |
| 40740562 | Identification of Prognostic and Diagnostic Biomarkers for Glioma Utilizing Immune System Gene Profiling. | Med J Islam Repub Iran 2025 |
| 38308496 | Synaptic adhesion molecule protocadherin-γC5 mediates β-amyloid-induced neuronal hyperactivity and cognitive deficits in | J Neurochem 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGC5

