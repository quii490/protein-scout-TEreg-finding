---
type: protein-evaluation
gene: "CLOCK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLOCK — REJECTED (研究热度过高 (PubMed strict=14481，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLOCK / BHLHE8, KIAA0334 |
| 蛋白名称 | Circadian locomoter output cycles protein kaput |
| 蛋白大小 | 846 aa / 95.3 kDa |
| UniProt ID | O15516 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytosol |
| 蛋白大小 | 8/10 | ×1 | 8 | 846 aa / 95.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=14481 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.6; PDB: 4H10, 6QPJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR047230, IPR036638, IPR001067, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromatoid body (GO:0033391)
- chromosome (GO:0005694)
- CLOCK-BMAL transcription complex (GO:1990513)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14481 |
| PubMed broad count | 44694 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHE8, KIAA0334 |

**关键文献**:
1. Mitochondrial autophagy and cell survival is regulated by the circadian Clock gene in cardiac myocytes during ischemic stress.. *Autophagy*. PMID: 34085589
2. A CLOCK-targeting lncRNA induces trained immunity against tuberculosis.. *Cell host & microbe*. PMID: 41475336
3. A CLOCK-less clock.. *Trends in cell biology*. PMID: 16996737
4. Proteomics in Circadian Biology.. *Journal of molecular biology*. PMID: 31843517
5. The circadian protein BMAL1 supports endothelial cell cycle during angiogenesis.. *Cardiovascular research*. PMID: 37052172

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.6 |
| 高置信度残基 (pLDDT>90) 占比 | 31.7% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 53.1% |
| 有序区域 (pLDDT>70) 占比 | 42.2% |
| 可用 PDB 条目 | 4H10, 6QPJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.6），有序残基占 42.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR047230, IPR036638, IPR001067, IPR001610; Pfam: PF00010, PF00989, PF14598 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRY2 | 0.999 | 0.796 | — |
| CRY1 | 0.999 | 0.836 | — |
| ARNTL | 0.999 | 0.994 | — |
| ARNTL2 | 0.999 | 0.891 | — |
| SIRT1 | 0.999 | 0.335 | — |
| NPAS2 | 0.998 | 0.739 | — |
| CSNK1E | 0.994 | 0.558 | — |
| EP300 | 0.994 | 0.345 | — |
| PER2 | 0.991 | 0.742 | — |
| KDM5A | 0.983 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCA1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14978263|imex:IM-19458 |
| Per1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Per2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| PER3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TNFRSF14 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| yycF | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCKAP5 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| Sirt1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11902|pubmed:18662546 |
| Btrc | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11930|pubmed:17462724 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.6 + PDB: 4H10, 6QPJ | pLDDT=60.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytosol / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CLOCK — Circadian locomoter output cycles protein kaput，研究基础较多，新颖性有限。
2. 蛋白大小846 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 14481 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 14481 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15516
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134852-CLOCK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLOCK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15516
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000134852-CLOCK/subcellular

![](https://images.proteinatlas.org/1867/62_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/1867/62_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/1867/63_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/1867/63_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/1867/93_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/1867/93_G2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15516-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
