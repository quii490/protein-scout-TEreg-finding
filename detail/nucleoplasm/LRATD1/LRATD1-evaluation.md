---
type: protein-evaluation
gene: "LRATD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRATD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRATD1 / FAM84A, NSE1 |
| 蛋白名称 | Protein LRATD1 |
| 蛋白大小 | 292 aa / 32.5 kDa |
| UniProt ID | Q96KN4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 292 aa / 32.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007053, IPR043299; Pfam: PF04970 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM84A, NSE1 |

**关键文献**:
1. Binding Affinity Determines Substrate Specificity and Enables Discovery of Substrates for N-Myristoyltransferases.. *ACS catalysis*. PMID: 34956690

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.5 |
| 高置信度残基 (pLDDT>90) 占比 | 42.8% |
| 置信残基 (pLDDT 70-90) 占比 | 20.5% |
| 中等置信 (pLDDT 50-70) 占比 | 24.3% |
| 低置信 (pLDDT<50) 占比 | 12.3% |
| 有序区域 (pLDDT>70) 占比 | 63.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.5，有序区 63.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007053, IPR043299; Pfam: PF04970 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DACT2 | 0.605 | 0.000 | — |
| FAM49A | 0.559 | 0.000 | — |
| PPP1R1A | 0.467 | 0.000 | — |
| NT5DC2 | 0.461 | 0.000 | — |
| ANKRD55 | 0.454 | 0.000 | — |
| PLAAT1 | 0.454 | 0.000 | — |
| SF3B3 | 0.453 | 0.000 | — |
| CZIB | 0.425 | 0.000 | — |
| KIAA0355 | 0.424 | 0.000 | — |
| RSAD1 | 0.406 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CYGB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARHGEF5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NMT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NMT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FIGNL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATXN10 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 6
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.5 + PDB: 无 | pLDDT=76.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 13 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRATD1 — Protein LRATD1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小292 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96KN4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162981-LRATD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRATD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96KN4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000162981-LRATD1/subcellular

![](https://images.proteinatlas.org/47703/1421_B10_5_red_green.jpg)
![](https://images.proteinatlas.org/47703/1421_B10_6_red_green.jpg)
![](https://images.proteinatlas.org/47703/697_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/47703/697_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/47703/735_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/47703/735_A2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96KN4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96KN4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 133..228; /note="LRAT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01283" |
| InterPro | IPR007053;IPR043299; |
| Pfam | PF04970; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162981-LRATD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARHGEF5 | Intact | false |
| ATXN10 | Intact | false |
| CYGB | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
