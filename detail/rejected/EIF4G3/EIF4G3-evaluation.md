---
type: protein-evaluation
gene: "EIF4G3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF4G3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF4G3 |
| 蛋白名称 | Eukaryotic translation initiation factor 4 gamma 3 |
| 蛋白大小 | 1585 aa / 176.7 kDa |
| UniProt ID | O43432 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1585 aa / 176.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.3; PDB: 1HU3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR003891, IPR003890, IPR003307; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **85.5/180** | |
| **归一化总分** | | | **47.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- eukaryotic translation initiation factor 4F complex (GO:0016281)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. De novo and biallelic DEAF1 variants cause a phenotypic spectrum.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 30923367
2. m(6)A Reader hnRNPA2B1 Modulates Late Pachytene Progression in Male Meiosis Through Post-Transcriptional Control.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40720760
3. Two related trypanosomatid eIF4G homologues have functional differences compatible with distinct roles during translation initiation.. *RNA biology*. PMID: 25826663
4. Chidamide and Radiotherapy Synergistically Induce Cell Apoptosis and Suppress Tumor Growth and Cancer Stemness by Regulating the MiR-375-EIF4G3 Axis in Lung Squamous Cell Carcinomas.. *Journal of oncology*. PMID: 34194495
5. Mapping the intracellular HMGB1 interactome and alterations induced by Toll-like receptor 4 activation.. *The Journal of biological chemistry*. PMID: 41161382

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.3 |
| 高置信度残基 (pLDDT>90) 占比 | 10.0% |
| 置信残基 (pLDDT 70-90) 占比 | 28.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 55.5% |
| 有序区域 (pLDDT>70) 占比 | 38.1% |
| 可用 PDB 条目 | 1HU3 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.3），有序残基占 38.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR003891, IPR003890, IPR003307; Pfam: PF02847, PF02854, PF02020 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF4A2 | 0.999 | 0.875 | — |
| EIF4E | 0.999 | 0.923 | — |
| EIF4A1 | 0.999 | 0.895 | — |
| PABPC1 | 0.996 | 0.757 | — |
| EIF4E2 | 0.995 | 0.091 | — |
| EIF4G1 | 0.972 | 0.705 | — |
| EIF4G2 | 0.968 | 0.595 | — |
| EIF4E1B | 0.960 | 0.515 | — |
| EIF4E3 | 0.945 | 0.478 | — |
| EIF4B | 0.887 | 0.119 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NCBP1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:15361857 |
| EIF4A1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF4A2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19805454|imex:IM-19495 |
| A0A0J1HXZ1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A1T3V3K0 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ORF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16317|pubmed:22522808 |
| USP10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| EIF3H | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| VAV2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 4 / 15 = 27%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 27%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.3 + PDB: 1HU3 | pLDDT=55.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF4G3 — Eukaryotic translation initiation factor 4 gamma 3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1585 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=55.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43432
- Protein Atlas: https://www.proteinatlas.org/ENSG00000075151-EIF4G3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF4G3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43432
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43432-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
