---
type: protein-evaluation
gene: "EML5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EML5 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EML5 |
| 蛋白名称 | Echinoderm microtubule-associated protein-like 5 |
| 蛋白大小 | 1969 aa / 219.4 kDa |
| UniProt ID | Q05BV3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 5/10 | ×1 | 5 | 1969 aa / 219.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR055442, IPR055439, IPR005108, IPR011041, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cilium (GO:0005929)
- extracellular exosome (GO:0070062)
- microtubule (GO:0005874)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Eml5, a novel WD40 domain protein expressed in rat brain.. *Gene*. PMID: 15225882
2. Echinoderm microtubule-associated protein -like protein 5 in anterior temporal neocortex of patients with intractable epilepsy.. *Iranian journal of basic medical sciences*. PMID: 26730336
3. Inferring circadian gene regulatory relationships from gene expression data with a hybrid framework.. *BMC bioinformatics*. PMID: 37752445
4. Expression levels of NPPB, ITGB6, CPNE4, EML5, and ITSN1 in fresh exudates swabbed from critically colonised and infected full-thickness wounds in rats.. *International wound journal*. PMID: 36307995
5. A Non-Synonymous Point Mutation in a WD-40 Domain Repeat of EML5 Leads to Decreased Bovine Sperm Quality and Fertility.. *Frontiers in cell and developmental biology*. PMID: 35478957

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.0 |
| 高置信度残基 (pLDDT>90) 占比 | 59.8% |
| 置信残基 (pLDDT 70-90) 占比 | 31.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 4.2% |
| 有序区域 (pLDDT>70) 占比 | 90.9% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.0，有序区 90.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055442, IPR055439, IPR005108, IPR011041, IPR011047; Pfam: PF23409, PF23414, PF03451 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF500 | 0.550 | 0.091 | — |
| PTPN21 | 0.547 | 0.000 | — |
| TTC8 | 0.520 | 0.129 | — |
| ZC3H14 | 0.482 | 0.071 | — |
| SPATA7 | 0.453 | 0.000 | — |
| TOP3B | 0.447 | 0.000 | — |
| CRTC3 | 0.438 | 0.000 | — |
| IFT140 | 0.425 | 0.312 | — |
| CRYBA4 | 0.420 | 0.420 | — |
| MAD2L1 | 0.415 | 0.310 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H3-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| STT3B | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RPL27A | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPD | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CFAP161 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CRYBA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAJC7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BTRC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAJA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPP4R1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 14
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.0 + PDB: 无 | pLDDT=87.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 14 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EML5 — Echinoderm microtubule-associated protein-like 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1969 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q05BV3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165521-EML5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EML5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q05BV3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q05BV3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
