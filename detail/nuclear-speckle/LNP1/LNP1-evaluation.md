---
type: protein-evaluation
gene: "LNP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LNP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LNP1 / NP3 |
| 蛋白名称 | Leukemia NUP98 fusion partner 1 |
| 蛋白大小 | 178 aa / 21.3 kDa |
| UniProt ID | A1A4G5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nuclear speckles, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 178 aa / 21.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029280; Pfam: PF15419 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nuclear speckles, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NP3 |

**关键文献**:
1. Lem2 and Lnp1 maintain the membrane boundary between the nuclear envelope and endoplasmic reticulum.. *Communications biology*. PMID: 32483293
2. ER-phagy requires Lnp1, a protein that stabilizes rearrangements of the ER network.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 29915089
3. Arabidopsis Lunapark proteins are involved in ER cisternae formation.. *The New phytologist*. PMID: 29797722
4. MSI-XGNN: an explainable GNN computational framework integrating transcription- and methylation-level biomarkers for microsatellite instability detection.. *Briefings in bioinformatics*. PMID: 37833839
5. Nuclear membrane protein Lem2 regulates nuclear size through membrane flow.. *Nature communications*. PMID: 31015410

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.9 |
| 高置信度残基 (pLDDT>90) 占比 | 3.9% |
| 置信残基 (pLDDT 70-90) 占比 | 23.6% |
| 中等置信 (pLDDT 50-70) 占比 | 60.1% |
| 低置信 (pLDDT<50) 占比 | 12.4% |
| 有序区域 (pLDDT>70) 占比 | 27.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.9），有序残基占 27.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029280; Pfam: PF15419 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRTN3 | 0.809 | 0.000 | — |
| MT-CO2 | 0.767 | 0.000 | — |
| MRGPRD | 0.575 | 0.054 | — |
| OS9 | 0.499 | 0.406 | — |
| ERLEC1 | 0.499 | 0.406 | — |
| URB1 | 0.488 | 0.000 | — |
| IL31RA | 0.464 | 0.059 | — |
| ANOS1 | 0.463 | 0.000 | — |
| MT-CO3 | 0.437 | 0.000 | — |
| NDUFB11 | 0.436 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GAPDH | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000373191.3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| GLUL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| YWHAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.9 + PDB: 无 | pLDDT=63.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Vesicles; 额外: Nuclear speckles, Cytosol | 待确认 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LNP1 — Leukemia NUP98 fusion partner 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小178 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A1A4G5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000206535-LNP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LNP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A1A4G5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A1A4G5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A1A4G5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029280; |
| Pfam | PF15419; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000206535-LNP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GAN | Bioplex | false |
| GLUL | Bioplex | false |
| LYN | Biogrid | false |
| YWHAE | Bioplex | false |
| YWHAG | Bioplex | false |
| YWHAH | Bioplex | false |
| YWHAQ | Bioplex | false |
| YWHAZ | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
