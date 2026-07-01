---
type: protein-evaluation
gene: "B3KMC9"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B3KMC9 (5'-3' exoribonuclease) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B3KMC9 |
| 蛋白全称 | 5'-3' exoribonuclease |
| UniProt ID | B3KMC9 |
| 蛋白大小 | 950 aa / 104.5 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 950 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR027073; InterPro:IPR041412; InterPro:IPR004859; InterPro:IPR017151; Pfam:PF17846; Pfam:PF03159 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **122/180** | |
| **归一化总分 (/1.83)** | | | **66.7/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Possesses 5'->3' exoribonuclease activity. May promote termination of transcription by RNA polymerase II

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR027073 |
| InterPro | IPR041412 |
| InterPro | IPR004859 |
| InterPro | IPR017151 |
| Pfam | PF17846 |
| Pfam | PF03159 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B3KMC9编码5'-3'外切核糖核酸酶（XRN2/Rat1同源蛋白）的TrEMBL变体，其结构域架构以两个保守功能模块串联：N端XRN2特异的激活域（IPR041412、Pfam PF17846）负责与Rai1/DXO等辅因子互作进行底物选择性的调控；C端XRN家族催化域（IPR027073、IPR004859、IPR017151、Pfam PF03159）采用经典的折纸状折叠，含两个保守的Mg²⁺-配位酸性残基进行两步金属离子催化的5'→3'磷酸二酯键水解，释放单个NMP产物。

950 aa（104.5 kDa）的超大分子量（在75个蛋白中排名前列）和Pfam分域极好的保守性赋予该蛋白容纳底物识别区及辅因子互作面的充足空间。AlphaFold预测结构可用，催化核心区域pLDDT较高但loop区域和N端激活区可能存在柔性。

功能注释揭示其核内主要角色为RNA聚合酶II转录终止的关键执行者——XRN2识别Pol II 3'端加工信号后切割并降解预先Cleavage的多余3'延伸RNA，同时通过"鱼雷模型"（torpedo model）追赶并促进Pol II在PolyA位点下游的构象变化和转录终止。这一过程中XRN2（1）直接接触Pol II CTD的磷酸化状态（尤其Ser2P）；（2）与CPSF/CstF等3'加工因子竞争RNA 3'末端；（3）通过持续的5'→3'消化活性生成短I RNA产物。

TE调控相关性机制推论极为多元和直接——XRN2在转录终止层面的功能决定了Pol II通读TE元件后的转录命运。TE调控的三个关键方面与XRN2相关：（1）**转录通读限制**：多数TE（如LINE-1、Alu）在基因组中嵌入为内含子或基因间多聚A簇，其中Alu元件常含PolyT和RNA Pol III终止信号。当Pol II通读TE嵌入位点后，XRN2的追赶速率决定了TE衍生RNA的清除效率和TE可能产生的异常激活程度。（2）**TE来源的内源性双链RNA（dsRNA）处理**：XRN2的核内5'→3'消化能力可快速降解TE来源的异常RNA（尤其反义转录本），防止其与同源DNA模板配对形成dsRNA中间体，从而降低RNase L和PKR激活触发先天免疫应答的风险。（3）**Pol II pausing调控**：XRN2与Pol II的CTD Ser2P互作影响转录暂停-终止决策，可能在TE启动子近端调控Pol II释放和通读效率。

但缺少GO-CC核定位注释（核定位特异性4/10）是主要短板——尽管XRN2主要定位于细胞核，但该TrEMBL变体缺少正式注释。PubMed=0，新颖性10/10。归一化总分66.7/100。实际上XRN2在转录终止中的核心地位使其TE调控潜力远高于分值所反映，建议在获得核定位确认后优先进行其TE衍生RNA的CLIP-seq或RNA降解动力学实验。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B3KMC9

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B3KMC9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B3KMC9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B3KMC9
