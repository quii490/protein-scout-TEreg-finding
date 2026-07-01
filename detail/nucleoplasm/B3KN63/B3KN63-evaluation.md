---
type: protein-evaluation
gene: "B3KN63"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B3KN63 ((human) hypothetical protein) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B3KN63 |
| 蛋白全称 | (human) hypothetical protein |
| UniProt ID | B3KN63 |
| 蛋白大小 | 1127 aa / 124.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 1127 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR050520; InterPro:IPR027417; InterPro:IPR038718; InterPro:IPR000330; Pfam:PF00176 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **122/180** | |
| **归一化总分 (/1.83)** | | | **66.7/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR050520 |
| InterPro | IPR027417 |
| InterPro | IPR038718 |
| InterPro | IPR000330 |
| Pfam | PF00176 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

B3KN63（hypothetical protein，UniProt: B3KN63，1127 aa / 124.0 kDa）的结构域架构显示其含有InterPro: IPR050520（SNF2/RAD5-like ATPase）、IPR027417（P-loop containing nucleoside triphosphate hydrolase）、IPR038718（SNF2-like domain superfamily）、IPR000330（SNF2 N-terminal）；Pfam注释为PF00176（SNF2 family N-terminal domain）。SNF2家族蛋白是ATP-dependent chromatin remodeling enzyme的核心催化亚基，其典型功能是使用ATP水解能量改变nucleosome positioning、促进transcription factor access或介导histone octamer sliding。

蛋白质互作网络目前数据有限。然而SNF2家族蛋白通常与chromatin remodeling复合体（SWI/SNF、ISWI、CHD、INO80四大类）中的其他亚基形成稳定复合物。B3KN63的SNF2 domain architecture暗示其可能具有helicase-like活性，能够通过ATP水解驱动的translocation改变DNA-histone接触。该蛋白1127 aa的大尺寸与SNF2 family成员的典型长度一致，可能包含auto-inhibitory domain和regulatory insertion。

从结构-功能机制角度分析，B3KN63属于TrEMBL未审查条目，尚缺乏实验性结构数据。AlphaFold预测pLDDT无具体数值，但SNF2-type ATPase domain通常折叠为bilobed architecture（RecA-like lobe 1 + RecA-like lobe 2），ATP在lobe interface处结合和水解。评估综合得分66.7/100，推荐等级2/5。

对于TE调控机制的意义而言，B3KN63的SNF2-like domain暗示其可能直接参与chromatin结构调控。SNF2 family成员在TE silencing中具有重要功能：ATRX/DAXX通过沉积H3.3 at pericentromeric repeat；SMARCAD1在LINE-1 silencing中起作用；MORC family在transposon repression中发挥功能。B3KN63可能以类似的ATP-dependent mechanism调控特定TE loci的chromatin accessibility。PubMed=0（TrEMBL条目），该蛋白高度新颖，学术探索空间极大。

综上所述，B3KN63作为一个1127 aa的SNF2 family protein，其chromatin remodeling潜力使其成为TE调控研究的高度候选靶标。建议首先通过nuclear localization validation（IF+subcellular fractionation）确认其在核内的分布，再设计ChIP-seq和ATPase activity assay验证其在chromatin上的结合位点和remodeling活性。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B3KN63

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B3KN63
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B3KN63
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B3KN63
