---
type: protein-evaluation
gene: "CRY2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRY2 — REJECTED (研究热度过高 (PubMed strict=1014，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRY2 / KIAA0658 |
| 蛋白名称 | Cryptochrome-2 |
| 蛋白大小 | 593 aa / 66.9 kDa |
| UniProt ID | Q49AN0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 593 aa / 66.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1014 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036134, IPR036155, IPR005101, IPR002081, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **85.5/180** | |
| **归一化总分** | | | **47.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cry-Per complex (GO:1990512)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- mitochondrion (GO:0005739)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1014 |
| PubMed broad count | 1554 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0658 |

**关键文献**:
1. Light-induced LLPS of the CRY2/SPA1/FIO1 complex regulating mRNA methylation and chlorophyll homeostasis in Arabidopsis.. *Nature plants*. PMID: 38066290
2. Light-dependent modulation of protein localization and function in living bacteria cells.. *Nature communications*. PMID: 39737933
3. Clinical applicability of optogenetic gene regulation.. *Biotechnology and bioengineering*. PMID: 34287844
4. The dual-action mechanism of Arabidopsis cryptochromes.. *Journal of integrative plant biology*. PMID: 37902426
5. UVA1 exposures change gene expression and circadian time-related protein CRY2 in human skin.. *Journal of photochemistry and photobiology. B, Biology*. PMID: 41690255

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.2 |
| 高置信度残基 (pLDDT>90) 占比 | 72.0% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 16.7% |
| 有序区域 (pLDDT>70) 占比 | 80.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.2，有序区 80.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036134, IPR036155, IPR005101, IPR002081, IPR006050; Pfam: PF00875, PF03441 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARNTL | 0.999 | 0.973 | — |
| CRY1 | 0.999 | 0.986 | — |
| CLOCK | 0.999 | 0.796 | — |
| PER3 | 0.999 | 0.958 | — |
| PER2 | 0.999 | 0.991 | — |
| FBXL3 | 0.999 | 0.967 | — |
| NPAS2 | 0.998 | 0.676 | — |
| PER1 | 0.998 | 0.978 | — |
| CSNK1E | 0.997 | 0.757 | — |
| TIMELESS | 0.996 | 0.579 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q8VZY9 | psi-mi:"MI:0018"(two hybrid) | pubmed:15805487|imex:IM-19425 |
| PHYB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:11089975 |
| BZZ1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BRX1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BUD14 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SRB6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PIN4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RTS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| BFR2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| APM2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.2 + PDB: 无 | pLDDT=84.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear speckles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CRY2 — Cryptochrome-2，研究基础较多，新颖性有限。
2. 蛋白大小593 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1014 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1014 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q49AN0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121671-CRY2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRY2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q49AN0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000121671-CRY2/subcellular

![](https://images.proteinatlas.org/37577/517_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/37577/517_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/37577/520_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/37577/520_F4_3_red_green.jpg)
![](https://images.proteinatlas.org/37577/523_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/37577/523_F4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q49AN0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q49AN0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 22..151; /note="Photolyase/cryptochrome alpha/beta" |
| InterPro | IPR036134;IPR036155;IPR005101;IPR002081;IPR006050;IPR014729; |
| Pfam | PF00875;PF03441; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000121671-CRY2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PPP5C | Intact, Biogrid | true |
| XRN2 | Intact, Biogrid | true |
| BMAL1 | Biogrid | false |
| CLOCK | Biogrid | false |
| CRY1 | Biogrid | false |
| CSNK1D | Biogrid | false |
| CSNK1E | Biogrid | false |
| CSNK2B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
