---
type: protein-evaluation
gene: "MAX"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MAX — REJECTED (研究热度过高 (PubMed strict=17778，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAX / BHLHD4 |
| 蛋白名称 | Protein max |
| 蛋白大小 | 160 aa / 18.3 kDa |
| UniProt ID | P61244 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus; UniProt: Nucleus; Cell projection, dendrite |
| 蛋白大小 | 8/10 | ×1 | 8 | 160 aa / 18.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=17778 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=81.3; PDB: 1AN2, 1HLO, 1NKP, 1NLW, 1R05, 5EYO, 6G6J |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011598, IPR036638; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus | Supported |
| UniProt | Nucleus; Cell projection, dendrite | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- dendrite (GO:0030425)
- Mad-Max complex (GO:0070443)
- MLL1 complex (GO:0071339)
- Myc-Max complex (GO:0071943)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-DNA complex (GO:0032993)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17778 |
| PubMed broad count | 278971 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHD4 |

**关键文献**:
1. CRISPR/Cas9-based editing of NF-YC4 promoters yields high-protein rice and soybean.. *The New phytologist*. PMID: 39307530
2. A Phytophthora sojae Glycoside Hydrolase 12 Protein Is a Major Virulence Factor during Soybean Infection and Is Recognized as a PAMP.. *The Plant cell*. PMID: 26163574
3. Nilotinib: Disrupting the MYC-MAX Heterocomplex.. *Bioinformatics and biology insights*. PMID: 39081669
4. The MAX-interacting transcription factor network.. *Seminars in cancer biology*. PMID: 16908182
5. Genome-wide identification and expression analysis of metal tolerance protein (MTP) gene family in soybean (Glycine max) under heavy metal stress.. *Molecular biology reports*. PMID: 36653731

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.3 |
| 高置信度残基 (pLDDT>90) 占比 | 52.5% |
| 置信残基 (pLDDT 70-90) 占比 | 9.4% |
| 中等置信 (pLDDT 50-70) 占比 | 35.6% |
| 低置信 (pLDDT<50) 占比 | 2.5% |
| 有序区域 (pLDDT>70) 占比 | 61.9% |
| 可用 PDB 条目 | 1AN2, 1HLO, 1NKP, 1NLW, 1R05, 5EYO, 6G6J, 6G6K, 6G6L, 7RCU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1AN2, 1HLO, 1NKP, 1NLW, 1R05, 5EYO, 6G6J, 6G6K, 6G6L, 7RCU）+ AlphaFold极高置信度预测（pLDDT=81.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638; Pfam: PF00010 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYC | 0.999 | 0.999 | — |
| MXD1 | 0.999 | 0.991 | — |
| MXI1 | 0.998 | 0.934 | — |
| MYCN | 0.996 | 0.894 | — |
| MGA | 0.995 | 0.782 | — |
| E2F6 | 0.984 | 0.623 | — |
| MAPK14 | 0.976 | 0.409 | — |
| RNF2 | 0.965 | 0.607 | — |
| MYCL | 0.962 | 0.761 | — |
| RUVBL2 | 0.950 | 0.456 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MTX1 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:17981999|imex:IM-19447 |
| AOX1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17981999|imex:IM-19447 |
| OM64 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17981999|imex:IM-19447 |
| TOM20-4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17981999|imex:IM-19447 |
| TOM20-2 | psi-mi:"MI:0018"(two hybrid) | pubmed:17981999|imex:IM-19447 |
| TOM20-3 | psi-mi:"MI:0018"(two hybrid) | pubmed:17981999|imex:IM-19447 |
| UGT75B1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11283335 |
| CALS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11283334|imex:IM-19525 |
| LE1 | psi-mi:"MI:0892"(solid phase assay) | pubmed:25205096|imex:IM-26195 |
| MGA | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.3 + PDB: 1AN2, 1HLO, 1NKP, 1NLW, 1R05,  | pLDDT=81.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cell projection, dendrite / Nucleoplasm; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. MAX — Protein max，研究基础较多，新颖性有限。
2. 蛋白大小160 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 17778 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 17778 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P61244
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125952-MAX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P61244
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000125952-MAX/subcellular

![](https://images.proteinatlas.org/328/924_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/328/924_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/328/932_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/328/932_B8_3_red_green.jpg)
![](https://images.proteinatlas.org/328/971_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/328/971_B8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P61244-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P61244 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 23..74; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR036638; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000125952-MAX/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK2A1 | Biogrid, Opencell | true |
| E2F6 | Intact, Biogrid | true |
| L3MBTL2 | Intact, Biogrid | true |
| MGA | Intact, Biogrid | true |
| MNT | Intact, Biogrid | true |
| MXD1 | Intact, Biogrid | true |
| MXI1 | Intact, Biogrid | true |
| MYC | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
