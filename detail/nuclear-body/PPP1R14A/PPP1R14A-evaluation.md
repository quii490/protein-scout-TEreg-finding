---
type: protein-evaluation
gene: "PPP1R14A"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## PPP1R14A (Protein phosphatase 1 regulatory subunit 14A) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PPP1R14A |
| 蛋白全称 | Protein phosphatase 1 regulatory subunit 14A |
| UniProt ID | Q96A00 |
| 蛋白大小 | 147 aa / 16.2 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 5/10 | x1 | 5.0 | 147 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 6/10 | x2 | 12.0 | InterPro:IPR008025; InterPro:IPR036658; Pfam:PF05361 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **116/180** | |
| **归一化总分 (/1.83)** | | | **63.4/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Inhibitor of PPP1CA. Has over 1000-fold higher inhibitory activity when phosphorylated, creating a molecular switch for regulating the phosphorylation status of PPP1CA substrates and smooth muscle contraction

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR008025 |
| InterPro | IPR036658 |
| Pfam | PF05361 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000167641-PPP1R14A
定位: location reactome" data-name="nucleoplasm">

![](https://images.proteinatlas.org/5044/624_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/5044/624_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/5044/630_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/5044/630_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/54534/984_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/54534/984_A1_2_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR008025;IPR036658; |
| Pfam | PF05361; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HEL-S-80P | STRING | 986 |
| PPP1CB | STRING | 986 |
| PPP1CC | STRING | 972 |
| PPP1CA | STRING | 949 |
| RHOA | STRING | 807 |
| PAK1 | STRING | 797 |
| IMUP | STRING | 780 |
| PPP1R12B | STRING | 713 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PPP1R14A

### PubMed

**Count: 186**

| PMID | Title |
|---|---|
| 42045466 | Identification of novel protein markers and therapeutic targets for common urological cancers by integrating large-scale human plasma proteome with th |
| 42022378 | PPP1R14A in male erectile dysfunction: key role in smooth muscle cells. |
| 41863461 | Apigenin is a Potential Drug for Treating Ischemic Stroke. Association between Plasma Protein Genes and Ischemic Stroke: A Proteome-wide Mendelian Ran |
| 40619010 | TRPV4 maintains the contractile phenotype of VSMCs by regulating CPI-17. |
| 40593373 | Integrated eQTL-pQTL Mendelian randomization and single-cell sequencing reveal therapeutic targets in ovarian clear cell cancer. |


### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/PPP1R14A_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.63 |
| pLDDT > 0.9 占比 | 0.0% |
| pLDDT < 0.5 占比 | 42.9% |
| 建模残基数 | 147 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。


### 深度机制分析

PPP1R14A（亦称CPI-17）是一个经典的蛋白磷酸酶1（PP1）抑制蛋白，其深度机制分析揭示了一个精致的磷酸化驱动分子开关模型。该蛋白仅147个氨基酸（16.2 kDa），属于PP1抑制蛋白家族，含有一个PP1 inhibitory domain（InterPro:IPR008025, Pfam:PF05361），且属于Thioredoxin-like superfamily（IPR036658）的结构折叠。ESMFold预测显示了较差的结构置信度——全局pLDDT仅0.63，0%残基pLDDT>0.9，而42.9%残基pLDDT<0.5，表明其天然状态可能以固有无序蛋白（IDP）形式存在，仅在结合PP1催化亚基后才发生折叠耦合。这种"无序-有序"转变（disorder-to-order transition）是许多调控性抑制蛋白的共同特征——无序状态允许快速降解，而结合状态则形成稳定的抑制性构象。

该蛋白的核心功能机制是磷酸化驱动的分子开关。UniProt注释明确记载："Has over 1000-fold higher inhibitory activity when phosphorylated, creating a molecular switch for regulating the phosphorylation status of PPP1CA substrates and smooth muscle contraction"。这一机制的关键在于PPP1R14A的Thr38位点——未磷酸化状态下，其对PP1催化亚基的抑制活性极弱（Ki在微摩尔范围）；磷酸化Thr38后，其Ki提升超过1000倍（降至纳摩尔范围），成为PP1的高效抑制剂。磷酸化主要由PKC（蛋白激酶C）和ROCK（Rho-associated kinase）催化，将胞外信号（G蛋白偶联受体→RhoA→ROCK）转化为PP1抑制信号，从而实现平滑肌收缩的钙增敏调节。

PPI互作网络完美支撑了这一模型。STRING数据显示PPP1R14A与PP1催化亚基三个同工型之间存在最高置信度互作：PPP1CB（score=986）、PPP1CC（score=972）和PPP1CA（score=949），这与UniProt功能注释"inhibitor of PPP1CA"直接吻合。此外，RHOA（score=807）和PAK1（score=797）的互作提示了上游调控信号——RhoA通过ROCK→PPP1R14A磷酸化→PP1抑制→MLC磷酸化维持→平滑肌收缩。IMUP（score=780）的互作值得特别注意——IMUP（Immortalization-upregulated protein）同样是本评估项目中的一个核蛋白候选（nucleoplasm），两者间可能的功能耦合值得后续验证。PPP1R12B（score=713）是另一个PP1调控亚基（MYPT2），提示存在PP1调控网络内的交叉调控。

PubMed文献分析显示PPP1R14A在泌尿系统肿瘤和血管平滑肌调控中的重要性。PMID 42022378发现PPP1R14A在男性勃起功能障碍中通过平滑肌细胞调控发挥关键作用——这直接契合其平滑肌收缩调控的核心功能。PMID 40619010证实TRPV4通过维持CPI-17（PPP1R14A）维持血管平滑肌细胞收缩表型。PMID 42045466和40593373分别在泌尿系统肿瘤和卵巢癌中鉴定了PPP1R14A作为蛋白标志物和治疗靶标的潜力。这些研究共同指向PPP1R14A的胞质/平滑肌功能定位。

然而，PPP1R14A作为胞质PP1调控蛋白的角色与核内TE调控存在根本性功能断层。该蛋白缺乏任何核定位信号、DNA结合结构域或染色质相关功能注释，且GO-CC中无核定位证据。其42.9%的低置信结构占比进一步不利于基于结构的功能改造。推荐等级2/5（63.4/100）反映了新颖性（10/10）与上述劣势的平衡。综合深度机制模型为：PKC/ROCK→PPP1R14A Thr38磷酸化（~1000倍亲和力增益）→PP1催化亚基抑制→MLC磷酸化维持→平滑肌收缩/血管张力调控。这一模型与TE调控无关，但PPP1R14A作为平滑肌功能和血管疾病的潜在靶标具有独立的转化医学价值。



- UniProt: https://www.uniprot.org/uniprotkb/Q96A00
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96A00
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PPP1R14A
