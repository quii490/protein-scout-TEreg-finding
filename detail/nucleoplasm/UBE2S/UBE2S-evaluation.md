---
type: protein-evaluation
gene: "UBE2S"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## UBE2S 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UBE2S |
| 蛋白名称 | Ubiquitin-conjugating enzyme E2 S |
| 蛋白大小 | 222 aa / 23.8 kDa |
| UniProt ID | Q16763 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 222 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=93 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=80.7; PDB=9 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ub_conjugating_enzyme; UBC; UBQ-conjugating_AS |
| PPI | 7/10 | x3 | 21.0 | PPI degree=198 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **74.3/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=93 broad=157
- AF pLDDT=80.7 PDB=9
- InterPro: Ub_conjugating_enzyme; UBC; UBQ-conjugating_AS
- Pfam: UQ_con
- PPI degree=198 ChIP: None
38915206: UBE2S promotes glycolysis in hepatocellular carcinoma by enhancing E3 enzyme-ind | 33589597: UBE2S interacting with TRIM28 in the nucleus accelerates cell cycle by ubiquitin | 41083491: UBE2S inhibits colorectal cancer proliferation by regulating the PI3K/AKT and MA

### 4. 总体评价
**74.3/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ubiquitin-conjugating enzyme E2 S

**功能**: Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins (PubMed:19820702, PubMed:19822757, PubMed:22496338, PubMed:27259151). Catalyzes 'Lys-11'-linked polyubiquitination. Acts as an essential factor of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated ubiquitin ligase that controls progression through mitosis (PubMed:19820702, PubMed:19822757, PubMed:27259151, PubMed:27910872). Acts by specifically elongating 'Lys-11'-linked polyubiqu

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050113 |
| InterPro | IPR000608 |
| InterPro | IPR023313 |
| InterPro | IPR016135 |
| Pfam | PF00179 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

UBE2S（Ubiquitin-conjugating enzyme E2 S）是本批次中最后一个但功能最明确的候选蛋白之一。它是泛素结合酶E2家族的成员，结构域架构为典型的E2折叠：Ub_conjugating_enzyme（IPR050113/IPR000608）、UBC（IPR023313）和UBQ-conjugating_AS（IPR016135）。222个氨基酸（23.8 kDa）、pLDDT=80.7和9个PDB结构条目指示一个紧凑的α/β蛋白，其核心为约150个氨基酸的保守UBC域，包含催化活性所必须的活性位点半胱氨酸（C95或等同残基），该位点接受来自E1酶的泛素，并通过硫酯键将泛素传递给E3连接酶或直接转移到底物蛋白上。

UBE2S的一个高度特异性的生化特征是它专门催化Lys-11连接的多聚泛素链延伸。与常规的Lys-48（蛋白酶体靶向）和Lys-63（信号转导）连接不同，Lys-11连接的多聚泛素链在细胞周期调控中发挥独特作用。UBE2S作为后期促进复合体/环化体（APC/C）的专性伙伴，在APC/C上被首先通过Lys-48链标记的底物上延伸Lys-11链，产生"分支/混合链"泛素拓扑，强化有丝分裂调控蛋白的蛋白酶体降解信号——这是确保有丝分裂适时退出的关键质量控制步骤。

PPI网络极其精确地反映了UBE2S在APC/C复合体中的核心E2身份。STRING数据库中最高置信度的互作全部为APC/C的核心亚基：CDC20（999分，APC/C的辅激活因子）、ANAPC11（999分，APC/C环指亚基，含RING域）、CDC27（999分，APC/C TPR亚基3）、ANAPC2（996分，APC/C Cullin亚基）、ANAPC10（996分，APC/C DOC域亚基）、CDC23（995分）、ANAPC4（992分）和ANAPC5（991分）。这些极端高置信度（990+）的STRING评分在评估队列中独一无二，反映了UBE2S作为APC/C-E2模块的核心定位已被高度实验验证。PPI degree=198的高结合度进一步体现了APC/C复合体作为最大的E3泛素连接酶之一（约1.5 MDa，含14个亚基）的复杂性。

从TE调控角度，UBE2S-APC/C轴的潜在影响力通过细胞周期与表观遗传组维护的交叉点实现。APC/C调控的底物包括Aurora A/B激酶、Cyclin B、securin和多种有丝分裂调控因子——这些蛋白的适时有丝分裂降解是确保染色体正确分离和核结构重建的基础。有丝分裂过程中的错误（如染色体错配、染色体凝聚缺陷）可导致微核化（micronucleation）——游离于主核外的微核中染色质经历广泛的DNA损伤和表观遗传重塑，导致TE元件（特别是LINE-1）的选择性激活。因此，UBE2S通过确保有丝分裂保真度可能间接维护TE的表观遗传沉默。

更直接地，PMID 33589597（2021）报道了UBE2S在核内与TRIM28（KAP1）互作，通过泛素化促进细胞周期加速。TRIM28是TE元件的核心表观遗传沉默因子——通过招募SETDB1（H3K9me3甲基转移酶）、HP1和NuRD复合体来建立和维持异染色质状态。UBE2S对TRIM28的泛素化（可能通过Lys-11连接链）可能调控TRIM28的稳定性、活性或染色质结合动力学，从而间接影响TE元件的转录状态。这一TE调控的候选机制具有高度的实验可验证性：（1）Co-IP验证UBE2S-TRIM28的内源互作；（2）分析UBE2S敲除/过表达下的全局TE转录组变化；（3）利用TUBEs（串联泛素结合实体）分析UBE2S依赖的TRIM28泛素链拓扑。鉴于其明确的生化功能、精确的PPI网络和与TRIM28的已验证互作，UBE2S是评估队列中TE调控机制最值得优先验证的候选蛋白之一。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CDC20 | STRING | 999 |
| ANAPC11 | STRING | 999 |
| CDC27 | STRING | 999 |
| ANAPC2 | STRING | 996 |
| ANAPC10 | STRING | 996 |
| CDC23 | STRING | 995 |
| ANAPC4 | STRING | 992 |
| ANAPC5 | STRING | 991 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q16763-F1-predicted_aligned_error_v6.png)


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000108106-UBE2S

![](https://images.proteinatlas.org/57150/972_F12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57150/972_F12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/57150/942_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57150/942_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57150/955_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57150/955_F12_4_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 157**

| 42133651 | UBE2S emerges as a key driver in an NK cell-based prognostic model for clear cell renal cell carcinoma. | PLoS One 2026 |
| 42032653 | UBE2S promotes small cell lung cancer transformation and progression via monitoring metabolic remodeling and cell cycle. | J Transl Med 2026 |
| 41985273 | A palmitoylation-related prognostic risk scoring model and tumor microenvironment characterization in lung adenocarcinom | Comput Biol Chem 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UBE2S

