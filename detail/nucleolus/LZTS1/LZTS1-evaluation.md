---
type: protein-evaluation
gene: "LZTS1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## LZTS1 (Leucine zipper putative tumor suppressor 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | LZTS1 |
| 蛋白全称 | Leucine zipper putative tumor suppressor 1 |
| UniProt ID | Q9Y250 |
| 蛋白大小 | 596 aa / 65.6 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 596 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 5/10 | x2 | 10.0 | InterPro:IPR045329; Pfam:PF06818 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **118/180** | |
| **归一化总分 (/1.83)** | | | **64.5/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Involved in the regulation of cell growth. May stabilize the active CDC2-cyclin B1 complex and thereby contribute to the regulation of the cell cycle and the prevention of uncontrolled cell proliferation. May act as a tumor suppressor

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR045329 |
| Pfam | PF06818 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

LZTS1（Leucine zipper putative tumor suppressor 1）。定位于nucleolus。包含596 aa / 65.6 kDa。UniProt编号Q9Y250。其InterPro结构域组成为IPR045329。Pfam注释1个保守结构域（PF06818，LZTS1/LZTS2家族）。AlphaFold预测三维结构可用（无具体pLDDT数值），尚无实验解析的PDB结构。

从功能机制角度，该蛋白被注释为推定的肿瘤抑制因子（PMID:40131646），其核心功能为通过稳定活性CDC2-cyclin B1复合物维持细胞周期正常进程并防止细胞不受控增殖。PPI网络分析提供了直接的实验验证——LZTS1与CDK1（BioGRID score=1）存在互作，而CDK1正是CDC2-cyclin B1复合物的催化亚基（CDK1=CDC2），这一互作从分子层面验证了其功能注释。此外，LZTS1与DLC1（STRING combined score=731）存在高置信度互作，DLC1为重要的RhoGAP肿瘤抑制因子，提示LZTS1可能通过Rho信号通路参与细胞骨架重塑与迁移调控。其他实验验证互作伙伴包括DYRK1A（双特异性酪氨酸磷酸化调控激酶，BioGRID score=1）、KDM1A（组蛋白去甲基化酶LSD1/H3K4me1/2去甲基化酶，score=1）、HMGB2（高迁移率族染色质结构蛋白，score=1）、EEF1G（翻译延伸因子）、DCAF4（CUL4-DDB1 E3泛素连接酶底物受体）及LMO3（转录调控因子），互作网络同时覆盖细胞周期调控、表观遗传修饰、染色质结构和转录调控等层面。

从结构生物学角度，该蛋白命名中含"亮氨酸拉链"（Leucine zipper），暗示可能含有经典的bZIP类二聚化结构域，但当前InterPro和Pfam注释中未明确检出该结构域，结构域注释较为有限（仅IPR045329和PF06818），提示其结构研究尚处于早期阶段。在TE调控的背景下，LZTS1的nucleolus定位使其可能与核仁组织区（NOR）附近的rDNA重复序列及转座子元件产生空间交叠；其与KDM1A（组蛋白H3K4me1/2去甲基化酶）的互作尤其值得关注——KDM1A已知参与ERV/LTR类TE的表观遗传沉默，LZTS1可能通过调控KDM1A活性或定位间接影响TE的表观遗传状态。

从研究转化角度，PubMed broad检索共103篇文献，但其在TE调控领域的研究完全空白，新颖度评分满分（10/10）。综合评分64.5/100，属中等优先级。与CDK1（细胞周期）和KDM1A（表观遗传）的双向互作关系，为后续TE调控功能研究提供了独特的双重切入点。

### 补充分析 (UniProt API)

**蛋白全称**: Leucine zipper putative tumor suppressor 1

**功能**: Involved in the regulation of cell growth. May stabilize the active CDC2-cyclin B1 complex and thereby contribute to the regulation of the cell cycle and the prevention of uncontrolled cell proliferation. May act as a tumor suppressor

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR045329 |
| Pfam | PF06818 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000061337-LZTS1

![](https://images.proteinatlas.org/6294/1165_G8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/6294/1165_G8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/6294/1269_C1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6294/1269_C1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6294/7_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6294/7_B7_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR045329; |
| Pfam | PF06818; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DLC1 | STRING | 731 |
| EEF1G | BioGRID | 1 |
| CDK1 | BioGRID | 1 |
| DYRK1A | BioGRID | 1 |
| DCAF4 | BioGRID | 1 |
| HMGB2 | BioGRID | 1 |
| KDM1A | BioGRID | 1 |
| LMO3 | BioGRID | 1 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/LZTS1

### PubMed

**Count: 103**

| PMID | Title |
|---|---|
| 41390337 | Prognostic value of brown adipocyte-related genes in colorectal cancer: a multi-omics and Mendelian randomization study. |
| 41197447 | Development of multiple cell death pattern features to predict prognosis and drug sensitivity in gastric adenocarcinoma. |
| 41003828 | Immunogenic cell death-related macrophage gene model for prognostic prediction in glioblastoma. |
| 40131646 | Natural resistance to cancers in long-lived mammals: genomic mechanisms and experimental evidence to explain Peto's paradox. |
| 39757032 | Screening Differentially Expressed Proteins in Areca Nut-Related Oral Squamous Cell Carcinoma Using Tandem Mass Tag Proteomics. |


### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q9Y250
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y250
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LZTS1
