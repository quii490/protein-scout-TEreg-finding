---
type: protein-evaluation
gene: "RLIM"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RLIM 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RLIM / RNF12 |
| 蛋白名称 | E3 ubiquitin-protein ligase RLIM |
| 蛋白大小 | 624 aa / 68.5 kDa |
| UniProt ID | Q9NVW2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 624 aa / 68.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=66 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.7; PDB: 6W7Z, 6W9A, 6W9D |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051834, IPR058896, IPR001841, IPR013083; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 66 |
| PubMed broad count | 133 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF12 |

**关键文献**:
1. X-exome sequencing of 405 unresolved families identifies seven novel intellectual disability genes.. *Molecular psychiatry*. PMID: 25644381
2. RLIM-specific activity reporters define variant pathogenicity in Tonne-Kalscheuer syndrome.. *HGG advances*. PMID: 39482882
3. Deficient spermiogenesis in mice lacking Rlim.. *eLife*. PMID: 33620316
4. Sequential stabilization of RNF220 by RLIM and ZC4H2 during cerebellum development and Shh-group medulloblastoma progression.. *Journal of molecular cell biology*. PMID: 35040952
5. Rlim/Rnf12, Rex1, and X Chromosome Inactivation.. *Frontiers in cell and developmental biology*. PMID: 31737626

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.7 |
| 高置信度残基 (pLDDT>90) 占比 | 7.4% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 17.0% |
| 低置信 (pLDDT<50) 占比 | 62.0% |
| 有序区域 (pLDDT>70) 占比 | 21.0% |
| 可用 PDB 条目 | 6W7Z, 6W9A, 6W9D |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=49.7），有序残基占 21.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051834, IPR058896, IPR001841, IPR013083; Pfam: PF25914, PF13639 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBE2E2 | 0.976 | 0.967 | — |
| UBE2D2 | 0.970 | 0.965 | — |
| UBC | 0.937 | 0.934 | — |
| AXIN2 | 0.935 | 0.292 | — |
| UBA52 | 0.932 | 0.926 | — |
| LDB1 | 0.917 | 0.628 | — |
| UBE2D1 | 0.916 | 0.815 | — |
| RPS27A | 0.910 | 0.909 | — |
| UBB | 0.910 | 0.909 | — |
| UBXN1 | 0.785 | 0.591 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RPS14 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SNX17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| UBXN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UBE2D4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2E1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2E2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| LNX2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.7 + PDB: 6W7Z, 6W9A, 6W9D | pLDDT=49.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. RLIM — E3 ubiquitin-protein ligase RLIM，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小624 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 66 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=49.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVW2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131263-RLIM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RLIM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVW2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RLIM/IF_images/RLIM_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000131263-RLIM/subcellular

![](https://images.proteinatlas.org/18895/149_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/18895/149_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/18895/150_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/18895/150_G12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVW2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NVW2 |
| SMART | SM00184; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR051834;IPR058896;IPR001841;IPR013083; |
| Pfam | PF25914;PF13639; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000131263-RLIM/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LDB2 | Intact, Biogrid | true |
| TUBB | Biogrid, Bioplex | true |
| ANTXR1 | Bioplex | false |
| ASXL1 | Biogrid | false |
| BRF1 | Biogrid | false |
| CFLAR | Biogrid | false |
| CIB2 | Bioplex | false |
| CIB3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
