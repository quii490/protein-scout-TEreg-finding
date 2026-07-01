---
type: protein-evaluation
gene: "B3KQB8"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B3KQB8 (cDNA FLJ90160 fis, clone HEMBB1002661, highly similar to Hairy/enhancer-of-split related with YRPW motif 1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B3KQB8 |
| 蛋白全称 | cDNA FLJ90160 fis, clone HEMBB1002661, highly similar to Hairy/enhancer-of-split related with YRPW motif 1 |
| UniProt ID | B3KQB8 |
| 蛋白大小 | 304 aa / 33.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 304 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR011598; InterPro:IPR050370; InterPro:IPR036638; InterPro:IPR003650; Pfam:PF07527; Pfam:PF00010 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR011598 |
| InterPro | IPR050370 |
| InterPro | IPR036638 |
| InterPro | IPR003650 |
| Pfam | PF07527 |
| Pfam | PF00010 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B3KQB8编码HEY1（Hairy/Enhancer-of-split Related with YRPW motif 1）的同源蛋白，其结构域架构以bHLH-Orange转录抑制因子家族典型特征为核心：N端碱性螺旋-环-螺旋（bHLH）DNA结合域（IPR011598、Pfam PF00010）负责识别E-box（CANNTG）或N-box（CACNAG）基序；Orange结构域（IPR003650）形成额外的二聚化界面并参与共抑制因子选择。IPR036638（Orange超家族折叠）和IPR050370（HEY家族特征）进一步确认其分类归属。

304 aa（33.4 kDa）的紧凑分子量在该家族中较为典型。AlphaFold pLDDT数据可用但pLDDT值未进一步提供，整体结构域折叠预测可信度中等。作为TrEMBL未审阅条目（PubMed=0），PPI数据极度有限，但基于HEY1已知生物学，其核心互作伙伴应包括：NOTCH胞内域（NICD）/RBPJ复合物、TLE/Groucho共抑制因子、HDAC/Sin3辅抑制物，以及SIRT1去乙酰化酶。

TE调控相关性从机制推论来看具有一定潜力：HEY1作为Notch信号下游效应分子，当被NICD招募至RBPJ结合位点时，可同时作为转录激活或抑制因子，取决于Orange结构域选择的共抑制伙伴。若TCF/LEF或RBPJ结合位点富集于特定TE家族（如HERV-K或SVA元件的LTR区域），HEY1可能在Notch信号激活时介导这些TE的阶段性转录调控。此外，bHLH结构域的二聚化选择性（与E蛋白如E2A形成异源二聚体而非同源二聚体）为TE调控提供了额外的层次化特异性。

然而，该蛋白目前缺少核定位GO-CC注释（核定位特异性仅4/10），且作为TrEMBL变体缺乏实验验证，TE调控潜力评分为低（归一化67.8/100）。若未来获得核定位确认和bHLH结构域的E-box结合能力直接证据，HEY1/Notch/TE调控轴的假说将值得进一步追踪，尤其关注其在发育过程中LINE-1或HERV激活时序中的角色。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B3KQB8

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B3KQB8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B3KQB8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B3KQB8
