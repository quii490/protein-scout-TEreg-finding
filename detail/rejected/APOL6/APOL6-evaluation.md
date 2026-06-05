---
type: protein-evaluation
gene: "APOL6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## APOL6 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | APOL6 |
| 蛋白名称 | Apolipoprotein L6 |
| 蛋白大小 | 343 aa / 38.1 kDa |
| UniProt ID | Q9BWW8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 343 aa / 38.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008405; Pfam: PF05461 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular region (GO:0005576)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. ApoL6 associates with lipid droplets and disrupts Perilipin1-HSL interaction to inhibit lipolysis.. *Nature communications*. PMID: 38167864
2. Research on radiotherapy related genes and prognostic target identification of rectal cancer based on multi-omics.. *Journal of translational medicine*. PMID: 38012642
3. Goat miR-92a-3p Targets APOL6 Gene to Regulate the Differentiation of Intramuscular Precursor Adipocytes.. *Genes*. PMID: 38254947
4. APOL6 predicts immunotherapy efficacy of bladder cancer by ferroptosis.. *BMC cancer*. PMID: 39187773
5. Role of necroptosis-related genes in immune activity and prognosis of colorectal cancer.. *Frontiers in immunology*. PMID: 40959081

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.8 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 23.3% |
| 中等置信 (pLDDT 50-70) 占比 | 31.8% |
| 低置信 (pLDDT<50) 占比 | 44.9% |
| 有序区域 (pLDDT>70) 占比 | 23.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.8），有序残基占 23.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008405; Pfam: PF05461 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COMT | 0.767 | 0.000 | — |
| PARP9 | 0.642 | 0.000 | — |
| GBP5 | 0.640 | 0.000 | — |
| APOL1 | 0.591 | 0.000 | — |
| GBP1 | 0.559 | 0.000 | — |
| GBP4 | 0.551 | 0.000 | — |
| PLAAT4 | 0.541 | 0.000 | — |
| IFI44 | 0.533 | 0.000 | — |
| OAS2 | 0.523 | 0.000 | — |
| STAT1 | 0.517 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KRTAP10-8 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| ADAMTSL4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| FLJ13057 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| KPNA3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| IGF2R | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TEPSIN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RGS13 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GMCL1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FNTB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LAMTOR3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.8 + PDB: 无 | pLDDT=53.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. APOL6 — Apolipoprotein L6，非常新颖，仅有少数基础研究。
2. 蛋白大小343 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=53.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BWW8
- Protein Atlas: https://www.proteinatlas.org/search/APOL6
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=APOL6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BWW8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000221963-APOL6/subcellular

![](https://images.proteinatlas.org/29165/270_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/29165/270_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/29165/271_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/29165/271_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/29165/272_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/29165/272_E8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BWW8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
