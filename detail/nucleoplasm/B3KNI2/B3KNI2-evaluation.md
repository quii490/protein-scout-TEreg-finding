---
type: protein-evaluation
gene: "B3KNI2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B3KNI2 (cDNA FLJ14650 fis, clone NT2RP2002185, highly similar to Ubiquilin-1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B3KNI2 |
| 蛋白全称 | cDNA FLJ14650 fis, clone NT2RP2002185, highly similar to Ubiquilin-1 |
| UniProt ID | B3KNI2 |
| 蛋白大小 | 589 aa / 64.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 589 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR006636; InterPro:IPR015940; InterPro:IPR009060; InterPro:IPR015496; InterPro:IPR000626; InterPro:IPR029071 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR006636 |
| InterPro | IPR015940 |
| InterPro | IPR009060 |
| InterPro | IPR015496 |
| InterPro | IPR000626 |
| InterPro | IPR029071 |
| Pfam | PF00627 |
| Pfam | PF00240 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B3KNI2编码Ubiquilin-1（UBQLN1）的同源蛋白，其结构域架构以泛素信号处理的多模块串联为特征：N端UBL（ubiquitin-like）结构域（IPR000626、Pfam PF00240）负责与蛋白酶体Shp亚基或泛素化底物对接；C端UBA（ubiquitin-associated）结构域（IPR015940、IPR009060、Pfam PF00627）识别Lys48或Lys63连接的泛素链；中央的STI1/热休克伴侣结合域（IPR006636）和多个泛素结合位点（IPR015496、IPR029071）赋予该蛋白在泛素-蛋白酶体系统（UPS）与自噬-溶酶体途径之间的货物分选功能。

589 aa（64.8 kDa）的分子量提供了多结构域串联的空间基础。AlphaFold pLDDT数据可用但无实验PDB验证。PPI数据极度有限（TrEMBL条目，PubMed=0），但基于Ubiquilin-1在蛋白质稳态和神经退行性疾病中已知的角色，其核心互作伙伴应包括PSEN1/2（早老素）、UBQLN2/4、HSP70/BAG6伴侣复合物，及多种泛素E3连接酶。Ubiquilin-1通过UBL-UBA串联识别错误折叠或聚集倾向的蛋白，将其分流至蛋白酶体或自噬体进行降解。

TE调控相关性的机制推论：Ubiquilin-1作为蛋白质量控制的关键节点，可能通过以下路径间接影响TE：首先，许多TE编码蛋白（如LINE-1 ORF1p/ORF2p）具有聚集倾向，Ubiquilin-1可能通过泛素化标签介导这些蛋白的降解，从而限制TE的逆转录转座活性；其次，Ubiquilin-1与自噬受体（p62/SQSTM1）的合作可能在选择性自噬过程中清除TE衍生的蛋白聚集体；最后，Ubiquilin-1通过调控组蛋白H2A泛素连接（与PRC1复合物交叉）可能间接影响染色质压缩状态。

但当前缺乏核定位GO-CC注释（核定位特异性仅4/10），且该TrEMBL变体无任何实验研究支撑。归一化总分67.8/100，TE调控潜力评分低。若获得核定位和TE编码蛋白的直接互作证据，Ubiquilin-1在TE蛋白质稳态控制中的角色可能成为新的调控维度，但目前仅作为低优先级候选。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B3KNI2

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B3KNI2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B3KNI2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B3KNI2
