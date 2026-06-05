---
type: protein-evaluation
gene: "SP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SP2 — REJECTED (研究热度过高 (PubMed strict=1070，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SP2 / KIAA0048 |
| 蛋白名称 | Transcription factor Sp2 |
| 蛋白大小 | 613 aa / 64.9 kDa |
| UniProt ID | Q02086 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 613 aa / 64.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1070 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=44.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036236, IPR013087; Pfam: PF00096 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1070 |
| PubMed broad count | 6607 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0048 |

**关键文献**:
1. A Dual Role of Mesenchymal Stem Cell Derived Small Extracellular Vesicles on TRPC6 Protein and Mitochondria to Promote Diabetic Wound Healing.. *ACS nano*. PMID: 38290527
2. The conserved HIV-1 spacer peptide 2 triggers matrix lattice maturation.. *Nature*. PMID: 40011770
3. Urinary proteomics identifies distinct immunological profiles of sepsis associated AKI sub-phenotypes.. *Critical care (London, England)*. PMID: 39695715
4. Viable mutations of mouse midnolin suppress B cell malignancies.. *The Journal of experimental medicine*. PMID: 38625151
5. Role of Sp1 in atherosclerosis.. *Molecular biology reports*. PMID: 35715606

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 44.5 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 14.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 78.3% |
| 有序区域 (pLDDT>70) 占比 | 14.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=44.5），有序残基占 14.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036236, IPR013087; Pfam: PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POLRMT | 0.701 | 0.046 | — |
| TFB2M | 0.686 | 0.070 | — |
| MTERF1 | 0.657 | 0.042 | — |
| TFAM | 0.602 | 0.091 | — |
| E2F1 | 0.598 | 0.300 | — |
| TFB1M | 0.594 | 0.070 | — |
| TEFM | 0.583 | 0.000 | — |
| MT-ND6 | 0.542 | 0.000 | — |
| FHL2 | 0.439 | 0.433 | — |
| MTERF3 | 0.432 | 0.042 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q6A0E1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Neto | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Hinfp | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ar6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PITPNC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NFYC | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| QRICH1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FHL2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TNFRSF10D | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ANKS6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 15
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=44.5 + PDB: 无 | pLDDT=44.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 12 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SP2 — Transcription factor Sp2，研究基础较多，新颖性有限。
2. 蛋白大小613 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1070 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=44.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1070 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q02086
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167182-SP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q02086
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000167182-SP2/subcellular

![](https://images.proteinatlas.org/10245/921_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/10245/921_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/10245/923_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/10245/923_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/10245/931_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/10245/931_D10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q02086-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
