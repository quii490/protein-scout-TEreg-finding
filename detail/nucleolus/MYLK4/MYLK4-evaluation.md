---
type: protein-evaluation
gene: "MYLK4"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## MYLK4 (Myosin light chain kinase family member 4) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | MYLK4 |
| 蛋白全称 | Myosin light chain kinase family member 4 |
| UniProt ID | Q86YV6 |
| 蛋白大小 | 388 aa / 42.7 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 388 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR011009; InterPro:IPR000719; InterPro:IPR017441; InterPro:IPR008271; Pfam:PF00069 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL 未审查条目，功能尚未充分注释。

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR011009 |
| InterPro | IPR000719 |
| InterPro | IPR017441 |
| InterPro | IPR008271 |
| Pfam | PF00069 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Myosin light chain kinase family member 4

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011009 |
| InterPro | IPR000719 |
| InterPro | IPR017441 |
| InterPro | IPR008271 |
| Pfam | PF00069 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---


### 深度机制分析

**结构域架构**：MYLK4（388 aa, 42.7 kDa, Q86YV6, Myosin light chain kinase family member 4）属于蛋白激酶超家族（IPR011009, Protein kinase-like domain superfamily），含经典eukaryotic protein kinase catalytic domain（IPR000719, Pfam PF00069, residues 106-361）。该kinase domain采用典型bilobal kinase fold——N-lobe（~residues 106-200）由5-stranded anti-parallel beta-sheet和conserved alpha-C helix组成，C-lobe（~residues 201-361）主要为alpha-helical——ATP binding cleft位于N/C-lobe之间的deep cleft——catalytic loop（HRD motif）和activation loop（DFG to APE motif）位于C-lobe。MYLK4属于myosin light chain kinase（MLCK）家族但不同于经典MLCK（MYLK/MYLK2/MYLK3）——缺乏IQ motif/motor domain——可能为非典型MLCK或pseudokinase。ESMFold pLDDT=0.83（51.0% pLDDT>0.9）——kinase domain折叠良好，N端和C端无序tail区域pLDDT较低。TrEMBL未审查条目，PubMed strict=0——功能注释完全缺失。

**PPI互作网络解读**：PPI degree限于BioGRID互作数据。HSP90AA1/HSP90AB1及其pseudogenes（HSP90AB4P/AB3P/AA5P, BioGRID）构成HSP90分子伴侣系统——HSP90以ATP依赖方式稳定和折叠~400个client proteins——包括多种kinases（如AKT, CDK4, RAF, SRC）——MYLK4与HSP90的互作表明它可能为HSP90的kinase client——经CDC37-HSP90 cochaperone pathway进行折叠和成熟。CDC37（BioGRID）是HSP90的kinase-specific cochaperone——CDC37直接识别kinase domain的N-lobe→将kinase递给HSP90进行ATP-dependent folding——MYLK4-HSP90-CDC37三元件高度提示MYLK4为bona fide protein kinase。COPS5（COP9 signalosome subunit 5, BioGRID）是deneddylase——催化cullin-RING E3 ligase（CRL）的去泛素化（移除NEDD8）——调控CRL活性。SUPT20H（BioGRID）是SAGA/STAGA histone acetyltransferase complex的组分——参与transcription initiation。

**结构解读**：ESMFold pLDDT=0.83（51% >0.9置信度）。Kinase domain的conserved催化元件包括：（1）Gly-rich loop（GxGxxG motif, N-lobe）——形似lid覆盖ATP phosphate；（2）Lys-Glu salt bridge（catalytic Lys in beta-3, Glu in alpha-C helix）——定位ATP alpha/beta-phosphate；（3）HRD motif（catalytic loop, His-Arg-Asp）——Asp作为catalytic base；（4）DFG motif（activation loop N-terminus）——DFG-in（active）vs DFG-out（inactive）构象转换调控kinase activity；（5）APE motif（activation loop C-terminus）——锚定C-lobe。MYLK4的activation loop phosphorylation位点（保守Thr/Ser/Tyr残基）的功能尚不明——可能通过auto-phosphorylation或upstream kinase（如CaMKK, PKA?）激活。UniProt Domain注释（ECO:0000255 PROSITE-ProRule）基于序列profile而非实验验证。

**机制模型**：（1）HSP90-CDC37 chaperone cycle——新合成MYLK4经HSP70/HSP40 pre-folding complex→递交给CDC37→CDC37识别kinase N-lobe→HSP90 dimer形成闭合构象→ATP hydrolysis驱动kinase folding成熟→mature MYLK4 release。（2）Myosin light chain phosphorylation——经典MLCK（MYLK/MYLK2）以Ca2+/CaM依赖方式磷酸化myosin regulatory light chain（RLC/MYL9 Ser19 and Thr18）——促进myosin II motor activity和actomyosin contraction——MYLK4可能具有类似的底物特异性但以Ca2+-independent或不同cofactor依赖方式工作。（3）MYLK家族在非肌肉细胞中的非经典功能——non-muscle myosin II在核内参与transcription, chromatin remodeling和DNA repair——MYLK4的nucleoplasm/nucleolus定位提示其可能在核内磷酸化nuclear myosin II或nuclear myosin light chain→调控nuclear actin-myosin dynamics。

**TE调控展望**：MYLK4的TE调控关联为推测性。Nuclear actin-myosin II在TE silencing中潜在角色：（1）Nuclear myosin II产生mechanochemical force参与chromatin loop extrusion和TAD formation中的cohesin processivity——影响TE插入位点的染色质拓扑和enhancer activity。（2）HSP90-CDC37 chaperone pathway调控多种transcription factor stability（如GR, AR, p53, HSF1）——MYLK4作为HSP90 client可能间接依赖HSP90功能影响TE transcription。（3）COPS5-SUPT20H的SAGA HAT和CRL deneddylation活性直接影响chromatin acetylation和泛素化——在TE座位的histone H3/H4 acetylation和H2A ubiquitination调控TE transcription——MYLK4-COPS5/SUPT20H互作可能作为这两个chromatin modifier的regulatory input。但鉴于MYLK4完全缺乏实验表征（TrEMBL, PubMed=0），任何TE调控推测都需要kinase assay和knock-out实验的基础验证。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000145949-MYLK4

![](https://images.proteinatlas.org/15860/128_G10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15860/128_G10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/15860/1848_C2_15_cr5abb827639837_blue_red_green.jpg)
![](https://images.proteinatlas.org/15860/1848_C2_21_cr5abb82763a162_blue_red_green.jpg)
![](https://images.proteinatlas.org/15860/129_G10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/15860/129_G10_2_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00220; |
| InterPro | IPR011009;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |
| UniProt Domain | DOMAIN 106..361; /note="Protein kinase"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00159" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| COPS5 | BioGRID | 0 |
| HSP90AA1 | BioGRID | 0 |
| HSP90AB1 | BioGRID | 0 |
| HSP90AB4P | BioGRID | 0 |
| HSP90AB3P | BioGRID | 0 |
| HSP90AA5P | BioGRID | 0 |
| CDC37 | BioGRID | 0 |
| SUPT20H | BioGRID | 0 |


### PubMed 文献

**PubMed count: 35**


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MYLK4

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/MYLK4_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.83 |
| pLDDT > 0.9 | 51.0% |
| pLDDT < 0.5 | 4.1% |
| 残基数 | 388 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

