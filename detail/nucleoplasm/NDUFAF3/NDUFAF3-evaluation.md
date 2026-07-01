---
type: protein-evaluation
gene: "NDUFAF3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NDUFAF3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NDUFAF3 |
| 蛋白名称 | NADH dehydrogenase [ubiquinone] 1 alpha subcomplex assembly factor 3 |
| 蛋白大小 | 127 aa / 13.8 kDa |
| UniProt ID | A4FU71 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 📏 蛋白大小 | 6/10 | ×1 | 6.0 | 127 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=9 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=89.7; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | MTH938-like_sf; NDUF3; NDUFAF3/AAMDC |
| 🔗 PPI | 7/10 | ×3 | 21.0 | PPI degree=161 |
| **加权总分** | | | **126/180** | |
| **归一化总分 (÷1.83)** | | | **69.4/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据
HPA: nan (nan)
UniProt: SUBCELLULAR LOCATION: Mitochondrion inner membrane {ECO:0000256|ARBA:ARBA00004273}. Nucleus {ECO:0000256|ARBA:ARBA00004123}.;SUBCELLULAR LOCATION: Nucleus {ECO:0000250}. Mitochondrion inner membrane {

IF 图像: [Protein Atlas](https://www.proteinatlas.org/)

#### 3.2 蛋白大小
127 aa / 13.8 kDa

#### 3.3 研究现状
PubMed strict=9, broad=28
- PMID 34386730: Dissecting the concordant and disparate roles of NDUFAF3 and NDUFAF4 in mitochondrial complex I biogenesis. *iScience*
- PMID 19463981: Mutations in NDUFAF3 (C3ORF60), encoding an NDUFAF4 (C6ORF66)-interacting complex I assembly protein, cause fatal neonat *American journal of human genetics*
- PMID 28857403: In vivo chlorophyll fluorescence screening allows the isolation of a Chlamydomonas mutant defective for NDUFAF3, an asse *The Plant journal : for cell and molecular biology*

#### 3.4 三维结构
AF pLDDT=89.7, PDB=0

#### 3.5 结构域
InterPro: MTH938-like_sf; NDUF3; NDUFAF3/AAMDC
Pfam: DUF498
Standard nuclear protein domains

#### 3.6 PPI 互作网络
Combined degree=161

### 4. 总体评价
⭐⭐⭐⭐
**69.4/100** | **nucleoplasm**
Nuclear protein with standard evaluation


### 功能描述

Essential factor for the assembly of mitochondrial NADH:ubiquinone oxidoreductase complex (complex I)


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ICT1 | BioGRID | 0 |
| GEM | BioGRID | 0 |
| ABCC1 | BioGRID | 0 |
| SURF1 | BioGRID | 0 |
| NDUFS8 | BioGRID | 0 |
| CYC1 | BioGRID | 0 |
| NDUFB11 | BioGRID | 0 |
| NDUFS4 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：NDUFAF3（127 aa / 13.8 kDa, UniProt A4FU71）是线粒体呼吸链复合物I（CI）装配因子，具有紧凑的单结构域架构（InterPro: MTH938-like_sf, NDUF3, NDUFAF3/AAMDC; Pfam: DUF498）。仅127 aa使其成为评价集中最小蛋白之一。AlphaFold v6预测高置信度（pLDDT=89.7），尽管体积小但仍呈现明确的折叠。MTH938-like超家族折叠通常为混合α/β三明治结构，NDUFAF3可能采用此拓扑作为独立结构模块。无PDB实验结构（PDB=0）意味着AlphaFold提供唯一结构信息，但pLDDT=89.7使预测结果足够可靠，可用于机制建模。DUF498/NDUFAF3结构域作为蛋白-蛋白互作支架的作用在进化上高度保守，从衣藻到人均有对应同源蛋白。

**PPI网络分析**：PPI网络广泛（combined degree=161），反映NDUFAF3在线粒体CI装配中作为中枢节点的角色。BioGRID互作包括典型CI亚基（NDUFS8、NDUFS4、NDUFS8、NDUFB11）和装配因子（SURF1、CYC1、ICT1），确认NDUFAF3在CI装配通路中的位置。NDUFAF3与NDUFAF4协同装配CI的Q-模块（PMID:34386730, PMID:19463981）。关键文献（PMID:19463981）证实NDUFAF3突变导致致命新生儿乳酸性酸中毒，凸显此装配因子不可或缺。UniProt双定位注释（线粒体内膜+细胞核）值得关注：线粒体定位有功能和疾病遗传学支撑，但细胞核注释（ECO:0000256, ARBA自动注释）缺乏实验验证，可能源自与其他核蛋白的序列相似性，也可能代表真正的非经典核功能。

**结构解读与机制模型**：NDUFAF3的主要机制模型为线粒体呼吸链装配。其MTH938-like结构域作为蛋白-蛋白互作支架，促进45亚基呼吸链复合物I的分步装配。NDUFAF3专门参与Q-模块（泛醌结合模块，包含亚基NDUFS2、NDUFS3、NDUFS7、NDUFS8）的装配，这是CI生物合成中关键的后期步骤。DUF498结构域介导NDUFAF3与NDUFAF4的异源二聚化，二者协同作用方可完成Q-模块整合。NDUFAF3突变破坏此装配过程（PMID:19463981），导致CI缺陷相关的致命线粒体病。核质注释是否代表NDUFAF3的反向信号功能（将CI装配状态传递至核转录程序）或仅是免疫交叉反应/背景信号，仍需进一步验证。

**TE调控意义与实验建议**：NDUFAF3与TE生物学的关系最多为间接关联。其线粒体呼吸功能与转座元件生物学无直接联系。其在核质筛选列表中的存在可能源自ARBA核注释，需要谨慎对待。然而，线粒体-核交互在TE生物学中日益受到重视：（1）线粒体逆行信号可激活应激响应TE；（2）代谢状态（NAD+/NADH比值）直接调控sirtuin HDAC——控制TE染色质的关键酶；（3）线粒体功能障碍降低ATP水平，影响TE位点染色质重塑所需的能量供应。NDUFAF3可能通过这些代谢效应间接影响TE沉默。但鉴于核定位证据薄弱（无HPA数据，仅ARBA注释）和极小蛋白体积（127 aa），NDUFAF3是直接TE调控研究中优先级较低的候选。若推进，优先验证核定位（核质分级+western blot）。

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

![PAE](https://alphafold.ebi.ac.uk/files/AF-A4FU71-F1-predicted_aligned_error_v6.png)

### PubMed

**Count: 28**

| PMID | Title |
|---|---|
| 41815173 | Exploring the lactate-metabolism related characteristics during the development of medulloblastoma through single-cell and bulk RNA-seq. |
| 41498029 | Immunomodulatory Mechanisms of Rehmanniae Radix Praeparata-Achyranthes Root-Chinese Angelica Root Combination in Nontraumatic Osteonecrosis of the Fem |
| 41399979 | Metabolic Osteoimmune Biodegradable Zn-Mn Alloys: High Strength-Ductility and In Situ Vascular-Osteogenic Coupling. |
| 41234160 | Recessive variants in mitochondrial Complex I nuclear subunits are an underrated cause of optic atrophy. |
| 40650522 | NDUFAF3 is Involved in the Assembly of the Q/P Modules of Respiratory Complex I in the Green Microalga Chlamydomonas reinhardtii. |


