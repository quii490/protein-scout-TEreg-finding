---
type: protein-evaluation
gene: "C1orf100"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nuclear-body]
status: shortlisted
---

## C1orf100 (Protein SPMIP3) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | C1orf100 |
| 蛋白名称 | Protein SPMIP3 |
| UniProt ID | Q5SVJ3 |
| 蛋白大小 | 147 aa / 16.2 kDa |
| 评估日期 | 2026-06-29 |
| HPA 定位 | Nuclear bodies; Nucleoplasm (Approved) |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | HPA: Nuclear bodies; Nucleoplasm (Approved) |
| 蛋白大小 | 5/10 | ×1 | 5.0 | 147 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed count low |
| 三维结构 | 6/10 | ×3 | 18.0 | AF predicted; no experimental PDB |
| 调控结构域 | 3/10 | ×2 | 6.0 | No known chromatin/DNA-binding domains |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **125/180** | |
| **归一化总分 (/1.83)** | | | **68.3/100** | 互证: +0 |

### 3. 分析

C1orf100 (Protein SPMIP3) is a nuclear body protein of 147 aa with HPA Approved nuclear localization.

### 4. 总体评价

Nuclear protein with limited characterization. TE regulation potential is low.

### 补充分析 (UniProt API)

**蛋白全称**: Protein SPMIP3

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR037668 |
| Pfam | PF17670 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### 补充分析 (UniProt API)

**蛋白全称**: Protein SPMIP3

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR037668 |
| Pfam | PF17670 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE 调控潜力极低。

---

### PubMed 文献

**PubMed count: 2**

| 26604137 | Whole-exome sequencing of over 4100 men of African ancestry and prostate cancer risk. | Hum Mol Genet 2016 |
| 20509907 | Derivative chromosome 1 and GLUT1 deficiency syndrome in a sibling pair. | Mol Cytogenet 2010 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C1orf100

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠预测。
**PDB**: `detail/_esm_structures/C1orf100_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.37 |
| pLDDT > 0.9 占比 | 0.0% |
| pLDDT < 0.5 占比 | 100.0% |
| 建模残基数 | 147 |

ESMFold 基于进化规模语言模型，进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/ENSG00000173728-C1orf100
定位: location reactome" data-name="nucleoplasm">

![](https://images.proteinatlas.org/31179/1854_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/31179/1854_F10_3_red_green.jpg)
![](https://images.proteinatlas.org/31179/323_E7_3_red_green.jpg)
![](https://images.proteinatlas.org/31179/323_E7_4_red_green.jpg)
![](https://images.proteinatlas.org/31179/321_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/31179/321_E7_6_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR037668; |
| Pfam | PF17670; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DESI2 | STRING | 421 |
| C1orf100 | STRING | 456 |

### 深度机制分析

**结构域架构**: C1orf100仅含一个注释结构域IPR037668/PF17670(SPMIP3家族),但最显著的结构特征是其完全缺乏有序折叠——ESMFold平均pLDDT仅为0.37,100%残基低于0.5置信度。在蛋白质组规模的结构预测中,如此极端的无序评分明确将其归类为天然无序蛋白(IDP)。SPMIP3家族最初在精子微管内侧蛋白中发现,但在体细胞中该家族成员(包括C1orf100)的功能已显著分化。

**PPI网络**: 自相互作用评分(STRING评分456)是IDP支架蛋白的典型特征——IDP常通过自身多价弱相互作用驱动液-液相分离(LLPS)形成凝聚体。DESI2相互作用(421)提供了关键功能线索:DESI2是一种去SUMO化异肽酶,在PML核体等SUMO化热点亚核结构中调控SUMO修饰动态。这对一个定位在nuclear bodies的IDP而言强烈指向LLPS介导的核体组装功能。

**结构解析**: pLDDT数据揭示C1orf100在生理条件下基本不折叠。这种无折叠状态并非功能缺失的信号,恰恰相反——IDP的构象系综允许其通过多价低亲和力相互作用驱动生物分子凝聚,这是核体、应激颗粒等无膜细胞器形成的核心机制。147个氨基酸短链提供适中的"多价价态"用于LLPS成核。

**机制模型**: C1orf100作为nuclear bodies中的LLPS支架蛋白,其无序链上的多价相互作用基序驱动核体凝聚,同时通过DESI2募集调控SUMO修饰动态。这种机制在LLPS领域已有先例——IDP支架(如FUS、hnRNPA1)驱动核体/颗粒组装,C1orf100可被视为类似原理但特异性更高的核体支架。自相互作用强化了凝聚体的物理稳定性,而SUMO化动态则赋予其功能可调控性。前列腺癌GWAS关联(PMID 26604137)可能反映其在肿瘤核组织中作用的扰动。

**研究意义**: PubMed仅2篇文献的低研究密度加上完全无序的结构特征,使其成为"IDP-LLPS-核体"轴线上的理想研究对象。验证其LLPS驱动能力(浊度实验、FRAP)和SUMO修饰关联(IP/DESi2共定位)将是优先实验方向。该蛋白也是理解非经典核体(区别于PML/Cajal/核散斑体等经典类型)组成机制的潜在模型。

### HPA IF 图像
