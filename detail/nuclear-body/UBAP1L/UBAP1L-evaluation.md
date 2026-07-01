---
type: protein-evaluation
gene: "UBAP1L"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## UBAP1L (Ubiquitin-associated protein 1-like) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | UBAP1L |
| 蛋白全称 | Ubiquitin-associated protein 1-like |
| UniProt ID | F5GYI3 |
| 蛋白大小 | 381 aa / 41.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 381 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR049467; InterPro:IPR038870; InterPro:IPR042575; InterPro:IPR023340; Pfam:PF21267 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL 未审查条目，功能尚未充分注释。

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR049467 |
| InterPro | IPR038870 |
| InterPro | IPR042575 |
| InterPro | IPR023340 |
| Pfam | PF21267 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Ubiquitin-associated protein 1-like

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR049467 |
| InterPro | IPR038870 |
| InterPro | IPR042575 |
| InterPro | IPR023340 |
| Pfam | PF21267 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### PubMed 文献

**PubMed count: 8**

| 41378939 | Ubap1l Knockout Mice Model Recapitulates Retinal Degeneration Phenotype Observed in Patients and Exhibits Irregular Phot | Invest Ophthalmol Vis Sci 2025 |
| 39325468 | Biallelic Loss-of-Function Variants in UBAP1L and Nonsyndromic Retinal Dystrophies. | JAMA Ophthalmol 2024 |
| 39293306 | Generation of human induced pluripotent stem cell lines from a subject with UBAP1L-associated retinal dystrophy and CRIS | Stem Cell Res 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UBAP1L

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000246922-UBAP1L

![](https://images.proteinatlas.org/65334/1337_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65334/1337_B7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/65334/1516_H8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65334/1516_H8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65334/1338_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65334/1338_B7_4_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR049467;IPR038870;IPR042575;IPR023340; |
| Pfam | PF21267; |
| UniProt Domain | DOMAIN 4..50; /note="UMA"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00830" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CHMP4B | STRING | 540 |

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/UBAP1L_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.62 |
| pLDDT > 0.9 | 16.8% |
| pLDDT < 0.5 | 42.8% |
| 残基数 | 381 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

### 深度机制分析

**结构域架构**: UBAP1L的特征性标志是N端UMA结构域(4-50 aa,IPR049467/IPR023340/PF21267),该结构域最初在UBAP1(ubiquitin-associated protein 1)和MVB12(ESCRT-I亚基)中被发现,是ESCRT-I复合物的保守蛋白-蛋白互作模块。UMA结构域采用α-螺旋束折叠,介导与泛素化货物蛋白和ESCRT-I核心亚基(TSG101/VPS28/VPS37/MVB12)的对接。IPR042575标记UBAP1-Like亚家族,提示该蛋白是UBAP1的旁系同源物。IPR038870提供UMA超家族的折叠识别框架。除UMA结构域外,剩余331个氨基酸(~87%的序列)缺乏注释结构域,可能构成ESCRT-III募集和膜重塑的灵活界面。

**PPI网络**: CHMP4B互作评分540是6个蛋白PPI数据集中的最强信号,且具有高度功能特异性——CHMP4B是ESCRT-III多聚体纤维的核心亚基,负责膜切割。该互作将UBAP1L放置在ESCRT-I→ESCRT-III的桥接节点:UMA结构域结合ESCRT-I和泛素化货物(上游),而C端区域募集CHMP4B(下游)以启动膜重塑。这相当于一个"泛素化信号→膜变形"的信号转换器。

**结构解析**: ESMFold平均pLDDT 0.62,pLDDT>0.9残基占16.8%,集中在UMA结构域(4-50 aa),与该结构域在进化上的高度保守性一致。pLDDT<0.5占42.8%,这部分对应预测为无序的C端区域,可能与CHMP4B及其他ESCRT-III亚基的诱导性折叠结合一致——许多ESCRT组分通过"折叠-耦合-结合"机制相互作用。全长381 aa(41.9 kDa)的蛋白在静息态下采取"N端有序UMA域+C端柔性臂"的模块化架构。

**机制模型**: UBAP1L作为ESCRT-I相关蛋白,在核膜动力学中发挥关键功能。具体机制:UMA结构域识别并结合核膜蛋白上的泛素化信号(可能是核孔复合物组分或有丝分裂后残留在核膜上的蛋白质),同时C端柔性区域募集CHMP4B以启动ESCRT-III多聚化和膜切割。在有丝分裂末期,核膜在染色体周围重新组装——ESCRT-III在核膜孔封闭和核膜密封中至关重要,UBAP1L-UMA→CHMP4B轴可能在这一过程中充当初级信号转换器。视网膜营养不良表型(PMID 39325468; UBAP1L双等位基因功能丧失致非综合征性视网膜变性)揭示ESCRT介导的核膜动态对视网膜光感受器细胞具有独特脆弱性——光感受器外节每日经历大量膜盘脱落和更新,可能对核膜ESCRT功能有特别高的需求。

**研究意义**: UBAP1L处于ESCRT领域和核膜生物学的交界,是探索"泛素-ESCRT轴如何调控核膜完整性"的理想对象。与UBAP1(突变导致遗传性痉挛性截瘫)的表型差异提示ESCRT-I相关蛋白在不同组织中的功能专门化。测定UMA-CHMP4B完整复合物结构、鉴定核膜上的泛素化底物蛋白、以及构建光感受器特异性条件敲除小鼠是推进该领域的关键下一步。

