---
type: protein-evaluation
gene: "B2R9U5"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B2R9U5 (cDNA, FLJ94560, highly similar to Homo sapiens homeo box A11 (HOXA11), mRNA) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B2R9U5 |
| 蛋白全称 | cDNA, FLJ94560, highly similar to Homo sapiens homeo box A11 (HOXA11), mRNA |
| UniProt ID | B2R9U5 |
| 蛋白大小 | 313 aa / 34.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 313 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR021918; InterPro:IPR001356; InterPro:IPR020479; InterPro:IPR017970; InterPro:IPR009057; Pfam:PF12045 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR021918 |
| InterPro | IPR001356 |
| InterPro | IPR020479 |
| InterPro | IPR017970 |
| InterPro | IPR009057 |
| Pfam | PF12045 |
| Pfam | PF00046 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B2R9U5编码HOXA11（Homeobox A11）同源蛋白的TrEMBL变体，其结构域架构以经典同源异型转录因子模块为特征：homeodomain DNA结合域（IPR001356、IPR009057）采用螺旋-转角-螺旋（HTH）折叠，识别基因组中的TAAT/ATTA核心基序，Pfam PF00046（Homeodomain）覆盖该区域。N端的HOXA11特异性结构域（IPR021918、Pfam PF12045）可能与共因子选择（如PBX、MEIS）和转录调控活性切换相关。IPR020479和IPR017970进一步确认其归属为同源异型Antennapedia类转录因子。

313 aa（34.4 kDa）的紧凑分子量在同源异型转录因子中较为典型——homeodomain本身仅约60 aa，其余序列负责蛋白-蛋白互作和转录调控域的承载。AlphaFold预测结构可用，homeodomain三螺旋结构的pLDDT通常较高，但N端和linker区域可能呈现柔性。作为TrEMBL未审阅条目（PubMed=0），PPI数据有限，但HOXA11的已知生物学角色暗示其核心互作伙伴包括PBX1-4（PBC家族）、MEIS1-3、FOXO1及组蛋白修饰酶复合物。

TE调控相关性从机制推论来看，HOXA11作为序列特异性转录因子具有直接调控的潜力——若其homeodomain识别的TAAT基序富集于特定TE家族（如MaLR/LTR逆转座子或MER元素）的调控区域，HOXA11可能直接结合并激活或抑制这些TE的转录。此外，HOX蛋白通常与Trithorax（MLL）或Polycomb（PRC）染色质修饰复合物合作，这意味着HOXA11在TE区域的结合可能导致组蛋白H3K4me3（激活）或H3K27me3（抑制）的沉积，从而改变TE的染色质状态。

然而，该变体缺少核定位GO-CC注释（核定位特异性仅4/10），无直接的TE结合数据。归一化总分67.8/100，TE调控潜力评分低。若未来通过ChIP-seq实验获得HOXA11在基因组TE区域的结合谱，其对特定家族（如HERV或L1）的直接调控机制将成为值得探索的方向。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B2R9U5

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B2R9U5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B2R9U5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B2R9U5
