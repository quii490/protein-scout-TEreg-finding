---
type: protein-evaluation
gene: "ERP27"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERP27 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERP27 / C12orf46 |
| 蛋白名称 | Endoplasmic reticulum resident protein 27 |
| 蛋白大小 | 273 aa / 30.5 kDa |
| UniProt ID | Q96DN0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum lumen |
| 蛋白大小 | 10/10 | ×1 | 10 | 273 aa / 30.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.2; PDB: 2L4C, 4F9Z |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036249; Pfam: PF13848 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum lumen | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum lumen (GO:0005788)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C12orf46 |

**关键文献**:
1. A novel role for protein disulfide isomerase ERp18 in venous thrombosis.. *Thrombosis journal*. PMID: 39696500
2. ERp27, a new non-catalytic endoplasmic reticulum-located human protein disulfide isomerase family member, interacts with ERp57.. *The Journal of biological chemistry*. PMID: 16940051
3. Bioinformatic Analysis Suggests That Three Hub Genes May Be a Vital Prognostic Biomarker in Pancreatic Ductal Adenocarcinoma.. *Journal of computational biology : a journal of computational molecular cell biology*. PMID: 32216644
4. Gene Expression Trajectories from Normal Nonsmokers to COPD Smokers and Disease Progression Discriminant Modeling in Response to Cigarette Smoking.. *Disease markers*. PMID: 36157207
5. Development and validation of an endoplasmic reticulum stress-related molecular prognostic model for breast cancer.. *Frontiers in oncology*. PMID: 37313465

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.2 |
| 高置信度残基 (pLDDT>90) 占比 | 78.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 12.8% |
| 有序区域 (pLDDT>70) 占比 | 80.9% |
| 可用 PDB 条目 | 2L4C, 4F9Z |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2L4C, 4F9Z）+ AlphaFold高质量预测（pLDDT=86.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036249; Pfam: PF13848 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDIA3 | 0.950 | 0.121 | — |
| CALR | 0.745 | 0.087 | — |
| EEF1G | 0.713 | 0.628 | — |
| EEF1D | 0.705 | 0.681 | — |
| TXN | 0.695 | 0.000 | — |
| EEF1B2 | 0.640 | 0.610 | — |
| CARS1 | 0.622 | 0.610 | — |
| PDIA5 | 0.614 | 0.163 | — |
| ERP29 | 0.605 | 0.000 | — |
| VARS1 | 0.604 | 0.565 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBQLN4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| EEF1D | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| SGTA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| UBQLN1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| BLOC1S2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBQLN2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBL4A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| C12orf60 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MED20 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLGA8F | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.2 + PDB: 2L4C, 4F9Z | pLDDT=86.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum lumen / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ERP27 — Endoplasmic reticulum resident protein 27，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小273 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96DN0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139055-ERP27/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERP27
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DN0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96DN0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
