---
type: protein-evaluation
gene: "ESM1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ESM1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=196，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ESM1 |
| 蛋白名称 | Endothelial cell-specific molecule 1 |
| 蛋白大小 | 184 aa / 20.1 kDa |
| UniProt ID | Q9NQ30 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; UniProt: Secreted |
| 蛋白大小 | 8/10 | ×1 | 8 | 184 aa / 20.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=196 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038850, IPR009030, IPR000867; Pfam: PF00219 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.5/180** | |
| **归一化总分** | | | **34.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Secreted | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- extracellular matrix (GO:0031012)
- extracellular region (GO:0005576)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 196 |
| PubMed broad count | 719 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. ESM1 enhances fatty acid synthesis and vascular mimicry in ovarian cancer by utilizing the PKM2-dependent warburg effect within the hypoxic tumor microenvironment.. *Molecular cancer*. PMID: 38720298
2. Validation of ESM1 Related to Ovarian Cancer and the Biological Function and Prognostic Significance.. *International journal of biological sciences*. PMID: 36594088
3. Identification of hub genes involved in the pathogenesis of diabetic nephropathy: A multi-omics study integrating machine learning, mendelian randomization and mediation analysis.. *Diabetes, obesity & metabolism*. PMID: 40555691
4. Intramyocardial Sprouting Tip Cells Specify Coronary Arterialization.. *Circulation research*. PMID: 39092506
5. Artery formation in the intestinal wall and mesentery by intestine-derived Esm1+ endothelial cells.. *Nature communications*. PMID: 40998858

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.7 |
| 高置信度残基 (pLDDT>90) 占比 | 28.8% |
| 置信残基 (pLDDT 70-90) 占比 | 26.1% |
| 中等置信 (pLDDT 50-70) 占比 | 25.5% |
| 低置信 (pLDDT<50) 占比 | 19.6% |
| 有序区域 (pLDDT>70) 占比 | 54.9% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.7，有序区 54.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038850, IPR009030, IPR000867; Pfam: PF00219 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ITGAL | 0.849 | 0.292 | — |
| ITGB2 | 0.749 | 0.048 | — |
| ANGPT2 | 0.649 | 0.000 | — |
| HGF | 0.588 | 0.000 | — |
| SDC1 | 0.587 | 0.000 | — |
| CDH5 | 0.582 | 0.000 | — |
| DLL4 | 0.559 | 0.045 | — |
| ICAM2 | 0.543 | 0.000 | — |
| PDGFB | 0.539 | 0.000 | — |
| APLN | 0.530 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RPS2 | psi-mi:"MI:0096"(pull down) | pubmed:19000159|imex:IM-20263 |
| TGA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:38884001|imex:IM-30532 |
| PRKAB2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| YY1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NUFIP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ANKS1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HDAC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BANP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HOXA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NRF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.7 + PDB: 无 | pLDDT=72.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted / Vesicles | 一致 |
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
1. ESM1 — Endothelial cell-specific molecule 1，研究基础较多，新颖性有限。
2. 蛋白大小184 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 196 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQ30
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164283-ESM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ESM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQ30
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQ30-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
