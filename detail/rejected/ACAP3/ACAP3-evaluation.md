---
type: protein-evaluation
gene: "ACAP3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ACAP3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ACAP3 / CENTB5, KIAA1716 |
| 蛋白名称 | Arf-GAP with coiled-coil, ANK repeat and PH domain-containing protein 3 |
| 蛋白大小 | 834 aa / 92.5 kDa |
| UniProt ID | Q96P50 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 834 aa / 92.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045258, IPR042695, IPR027267, IPR002110, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- growth cone (GO:0030426)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CENTB5, KIAA1716 |

**关键文献**:
1. Aging Differentially Affects Axonal Autophagosome Formation and Maturation.. *Autophagy*. PMID: 37464898
2. ACAP3 negatively regulated by HDAC2 inhibits the malignant development of papillary thyroid carcinoma cells.. *The international journal of biochemistry & cell biology*. PMID: 39098591
3. Myc-mediated epigenetic silencing of ACAP3 promotes lung adenocarcinoma proliferation via regulating EGFR dynamics.. *British journal of cancer*. PMID: 41520057
4. Length Polymorphism and Methylation Status of UPS29 Minisatellite of the ACAP3 Gene as Molecular Biomarker of Epilepsy. Sex Differences in Seizure Types and Symptoms.. *International journal of molecular sciences*. PMID: 33276684
5. Integrative functional analysis of super enhancer SNPs for coronary artery disease.. *Journal of human genetics*. PMID: 29491472

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.5 |
| 高置信度残基 (pLDDT>90) 占比 | 50.6% |
| 置信残基 (pLDDT 70-90) 占比 | 20.3% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 25.1% |
| 有序区域 (pLDDT>70) 占比 | 70.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.5，有序区 70.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045258, IPR042695, IPR027267, IPR002110, IPR036770; Pfam: PF12796, PF01412, PF16746 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SEPTIN5 | 0.690 | 0.610 | — |
| RAB35 | 0.669 | 0.619 | — |
| SCNN1D | 0.645 | 0.000 | — |
| SEPTIN9 | 0.645 | 0.610 | — |
| UBE2J2 | 0.634 | 0.000 | — |
| SEPTIN8 | 0.627 | 0.610 | — |
| ACAP2 | 0.615 | 0.601 | — |
| SEPTIN6 | 0.612 | 0.610 | — |
| SEPTIN3 | 0.612 | 0.610 | — |
| SEPTIN11 | 0.611 | 0.610 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ITGB3BP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SLC35G2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| SEPTIN6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SEPTIN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACAP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SEPTIN7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SEPTIN8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SEPTIN5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SEPTIN11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.5 + PDB: 无 | pLDDT=75.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ACAP3 — Arf-GAP with coiled-coil, ANK repeat and PH domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小834 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96P50
- Protein Atlas: https://www.proteinatlas.org/search/ACAP3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ACAP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96P50
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ACAP3/IF_images/ACAP3_IF_if_selected_60x60.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000131584-ACAP3/subcellular

![](https://images.proteinatlas.org/58381/1061_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/58381/1061_H8_3_red_green.jpg)
![](https://images.proteinatlas.org/58381/983_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/58381/983_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/58381/991_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/58381/991_F11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96P50-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
