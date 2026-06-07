---
type: protein-evaluation
gene: "TACSTD2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TACSTD2 — REJECTED (研究热度过高 (PubMed strict=133，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TACSTD2 / GA733-1, M1S1, TROP2 |
| 蛋白名称 | Tumor-associated calcium signal transducer 2 |
| 蛋白大小 | 323 aa / 35.7 kDa |
| UniProt ID | P09758 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoli, Vesicles; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 323 aa / 35.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=133 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.7; PDB: 2MAE, 2MVK, 2MVL, 7E5M, 7E5N, 7PEE |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR049420, IPR043406, IPR041630, IPR000716, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoli, Vesicles | Supported |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- basal plasma membrane (GO:0009925)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular space (GO:0005615)
- lateral plasma membrane (GO:0016328)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 133 |
| PubMed broad count | 526 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GA733-1, M1S1, TROP2 |

**关键文献**:
1. Trop2 and its overexpression in cancers: regulation and clinical/therapeutic implications.. *Genes & cancer*. PMID: 26000093
2. Genomic, immunologic, and prognostic associations of TROP2 (TACSTD2) expression in solid tumors.. *The oncologist*. PMID: 38986529
3. Single-cell transcriptomics reveal metastatic CLDN4+ cancer cells underlying the recurrence of malignant pleural effusion in patients with advanced non-small-cell lung cancer.. *Clinical and translational medicine*. PMID: 38629624
4. Assessment of TROP2, CEACAM5 and DLL3 in metastatic prostate cancer: Expression landscape and molecular correlates.. *NPJ precision oncology*. PMID: 38760413
5. Associations of TACSTD2/TROP2 and NECTIN-4/NECTIN-4 with molecular subtypes, PD-L1 expression, and FGFR3 mutational status in two advanced urothelial bladder cancer cohorts.. *Histopathology*. PMID: 38196202

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.7 |
| 高置信度残基 (pLDDT>90) 占比 | 59.1% |
| 置信残基 (pLDDT 70-90) 占比 | 15.8% |
| 中等置信 (pLDDT 50-70) 占比 | 16.4% |
| 低置信 (pLDDT<50) 占比 | 8.7% |
| 有序区域 (pLDDT>70) 占比 | 74.9% |
| 可用 PDB 条目 | 2MAE, 2MVK, 2MVL, 7E5M, 7E5N, 7PEE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2MAE, 2MVK, 2MVL, 7E5M, 7E5N, 7PEE）+ AlphaFold极高置信度预测（pLDDT=82.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR049420, IPR043406, IPR041630, IPR000716, IPR036857; Pfam: PF21283, PF18635, PF00086 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLDN7 | 0.966 | 0.411 | — |
| CLDN1 | 0.899 | 0.292 | — |
| IGF1 | 0.815 | 0.000 | — |
| ERBB2 | 0.732 | 0.000 | — |
| ZNF92 | 0.725 | 0.000 | — |
| TG | 0.722 | 0.000 | — |
| MDK | 0.681 | 0.000 | — |
| EGFR | 0.644 | 0.000 | — |
| CCND1 | 0.628 | 0.000 | — |
| KRT7 | 0.608 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATP6V1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21674799|imex:IM-16565 |
| ATF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22304920|imex:IM-17307 |
| HNRNPAB | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| KRTAP1-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP10-8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP5-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LCE2C | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CYP8B1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLDN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:20651236|imex:IM-22294 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.7 + PDB: 2MAE, 2MVK, 2MVL, 7E5M, 7E5N,  | pLDDT=82.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane; 额外: Nucleoli, Vesicles | 一致 |
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
1. TACSTD2 — Tumor-associated calcium signal transducer 2，研究基础较多，新颖性有限。
2. 蛋白大小323 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 133 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 133 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P09758
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184292-TACSTD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TACSTD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P09758
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000184292-TACSTD2/subcellular

![](https://images.proteinatlas.org/55067/893_A3_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/55067/893_A3_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/55067/895_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55067/895_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55067/958_A12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55067/958_A12_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P09758-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P09758 |
| SMART | SM00211; |
| UniProt Domain [FT] | DOMAIN 70..145; /note="Thyroglobulin type-1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00500" |
| InterPro | IPR049420;IPR043406;IPR041630;IPR000716;IPR036857; |
| Pfam | PF21283;PF18635;PF00086; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000184292-TACSTD2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KRTAP1-3 | Intact | false |
| KRTAP10-8 | Intact | false |
| KRTAP5-2 | Intact | false |
| LCE2C | Intact | false |
| MBNL1 | Bioplex | false |
| SFTPC | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
