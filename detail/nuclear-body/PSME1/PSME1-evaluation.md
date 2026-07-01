---
type: protein-evaluation
gene: "PSME1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## PSME1 (Proteasome activator complex subunit 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PSME1 |
| 蛋白全称 | Proteasome activator complex subunit 1 |
| UniProt ID | Q06323 |
| 蛋白大小 | 249 aa / 27.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 249 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR003186; InterPro:IPR036997; InterPro:IPR036996; InterPro:IPR009077; InterPro:IPR003185; InterPro:IPR036252 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Implicated in immunoproteasome assembly and required for efficient antigen processing. The PA28 activator complex enhances the generation of class I binding peptides by altering the cleavage pattern of the proteasome

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR003186 |
| InterPro | IPR036997 |
| InterPro | IPR036996 |
| InterPro | IPR009077 |
| InterPro | IPR003185 |
| InterPro | IPR036252 |
| Pfam | PF02252 |
| Pfam | PF02251 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000092010-PSME1

![](https://images.proteinatlas.org/6632/8_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6632/8_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6632/9_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6632/9_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6632/7_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6632/7_C2_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR003186;IPR036997;IPR036996;IPR009077;IPR003185;IPR036252; |
| Pfam | PF02252;PF02251; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PSME2 | STRING | 999 |
| PSMB5 | STRING | 988 |
| PSMD14 | STRING | 940 |
| PSMD1 | STRING | 863 |
| PSMD4 | STRING | 830 |
| ADRM1 | STRING | 814 |
| USP14 | STRING | 795 |
| UCHL5 | STRING | 765 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSME1

### PubMed

**Count: 243**

| PMID | Title |
|---|---|
| 42364494 | Pan-cancer analysis identifies immunoproteasome as the predominant survival-associated component of antigen processing machinery. |
| 42289649 | Comparative mass spectrometry analysis of high and low centrifugation extracellular vesicle (EV) pellets from healthy urine following Tamm-Horsfall pr |
| 42094829 | Cell type-specific alterations in fatty acid metabolism in neuronal subpopulations of schizophrenia and construction of a diagnostic model. |
| 42052091 | Altered expression of ADAR1, N4BP1, and PSME1 in PBMCs correlated with therapeutic outcomes in HBeAg-negative chronic hepatitis B patients treated wit |
| 42036226 | [Interferon-α induces disulfidptosis occurrence in human liver cancer cells]. |

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/PSME1_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.88 |
| pLDDT > 0.9 占比 | 57.0% |
| pLDDT < 0.5 占比 | 0.0% |
| 建模残基数 | 249 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。

### 深度机制分析

**结构域架构**：PSME1/PA28α（UniProt Q06323，249 aa，27.4 kDa）是免疫蛋白酶体激活因子PA28（11S调节粒子）的α亚基。其域架构以两段串联PA28/REG型激活因子域为核心：N端激活域（IPR003186 - PA28/REG alpha/beta subunit, Pfam:PF02252）和C端激活域（IPR003185 - PA28/REG gamma subunit, Pfam:PF02251），两域均采用α-螺旋四螺旋束拓扑（IPR036252 - four-helix bundle）。IPR036997和IPR036996分别为α/β亚基和γ亚基的超家族标记。IPR009077（PA28 C-terminal domain）形成与20S核心蛋白酶体α环对接的C端尾结构。

**PPI互作网络**：STRING数据显示PSME1的PPI网络完全集中于蛋白酶体系统。PSME2（PA28β，评分999）形成α₃β₄异七聚体PA28环。PSMB5（20S核心β5亚基，评分988）为糜蛋白酶样催化位点。PSMD14（Rpn11去泛素化酶，评分940）、PSMD1（19S调节粒子支架，评分863）、PSMD4（泛素受体，评分830）均为26S蛋白酶体19S调控粒子组分。ADRM1（26S蛋白酶体泛素受体，评分814）、USP14（去泛素化酶，评分795）和UCHL5（泛素C端水解酶，评分765）构成去泛素化酶调控网络。

**结构-功能关系**：PSME1的ESMFold平均pLDDT=0.88（pLDDT>0.9占57.0%），反映了高度结构化的四螺旋束域。PA28α₃β₄异七聚体通过与20S核心蛋白酶体α环C端的活化环对接，使其轴向通道打开，从而促进未折叠多肽底物的入口。PA28的突出特点是改变蛋白酶体裂解偏好——增强对碱性、疏水性残基的裂解活性，产生更适合MHC I类结合的8-10 aa肽段，优化抗原呈递效率。

**TE调控机制**：免疫蛋白酶体与TE调控的连接是抗原加工和先天免疫的核心交叉。内源性逆转录病毒（ERV）和LINE-1的ORF编码蛋白若被表达，需要通过MHC I类途径呈递以激活CTL介导的清除——PSME1通过增强蛋白酶体生成免疫原性肽段在此通路中发挥关键作用（PMID:42364494 - 免疫蛋白酶体为抗原加工机器的主要存活相关组分）。cGAS-STING感知TE来源的胞质DNA后，IFN-I信号上调PSME1表达（PSME1启动子含ISRE元件），形成炎症→免疫蛋白酶体活化→TE肽呈递的正反馈环路。同时，泛素化异常蛋白的积累（如TE编码的错误折叠蛋白）需PA28增强的蛋白酶体降解以维持蛋白稳态。

**前沿意义**：PSME1以243篇PubMed文献量成为研究最充分的蛋白之一，但现有文献几乎全部聚焦于免疫蛋白酶体在抗原呈递中的功能（含干扰素诱导和免疫调控），TE调控视角尚未被明确探索。PSME1的IFN-I诱导性和TE肽加工功能使其成为先天免疫感知与TE沉默之间的连接枢纽蛋白。PSME1/2敲除小鼠已有，结合TE-RNA-seq和MHC I-IP/MS鉴定TE来源肽组将能够直接验证PSME1→免疫蛋白酶体→TE抗原呈递轴的生理相关性。

