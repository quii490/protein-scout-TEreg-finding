---
type: protein-evaluation
gene: "LGALS14"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LGALS14 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LGALS14 / PPL13 |
| 蛋白名称 | Placental protein 13-like |
| 蛋白大小 | 139 aa / 16.1 kDa |
| UniProt ID | Q8TCE9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 139 aa / 16.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=97.2; PDB: 6K2Y, 6K2Z |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **148.0/180** | |
| **归一化总分** | | | **82.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PPL13 |

**关键文献**:
1. Bioinformatics Analysis Identifies Potential Related Genes in the Pathogenesis of Intrauterine Fetal Growth Retardation.. *Evolutionary bioinformatics online*. PMID: 35923419
2. Using RNA sequencing for identifying gene imprinting and random monoallelic expression in human placenta.. *Epigenetics*. PMID: 25437054
3. Altered Biomarkers in Trophoblast Cells Obtained Noninvasively Prior to Clinical Manifestation of Perinatal Disease.. *Scientific reports*. PMID: 27660926
4. Examining Sex Differences in the Human Placental Transcriptome During the First Fetal Androgen Peak.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 33150487
5. Evolutionary origins of the placental expression of chromosome 19 cluster galectins and their complex dysregulation in preeclampsia.. *Placenta*. PMID: 25266889

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.2 |
| 高置信度残基 (pLDDT>90) 占比 | 97.8% |
| 置信残基 (pLDDT 70-90) 占比 | 1.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 6K2Y, 6K2Z |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6K2Y, 6K2Z）+ AlphaFold高质量预测（pLDDT=97.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LGALS1 | 0.564 | 0.000 | — |
| LGALS2 | 0.507 | 0.000 | — |
| ITLN2 | 0.495 | 0.064 | — |
| FLNA | 0.463 | 0.463 | — |
| APOL4 | 0.457 | 0.000 | — |
| CGB3 | 0.432 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IKZF3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| REL | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| GFAP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TCF4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| MID2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| FCHO1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| AJUBA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PICK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| POF1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SPAG5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 15
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.2 + PDB: 6K2Y, 6K2Z | pLDDT=97.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 6 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LGALS14 — Placental protein 13-like，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小139 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TCE9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000006659-LGALS14/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LGALS14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TCE9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000006659-LGALS14/subcellular

![](https://images.proteinatlas.org/65180/1830_F2_63_red_green.jpg)
![](https://images.proteinatlas.org/65180/1830_F2_64_red_green.jpg)
![](https://images.proteinatlas.org/65180/1901_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/65180/1901_E6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TCE9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TCE9 |
| SMART | SM00908;SM00276; |
| UniProt Domain [FT] | DOMAIN 6..138; /note="Galectin"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00639" |
| InterPro | IPR013320;IPR044156;IPR001079; |
| Pfam | PF00337; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000006659-LGALS14/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGR2 | Intact | false |
| AJUBA | Intact | false |
| BANP | Intact | false |
| BLZF1 | Intact | false |
| C1QTNF2 | Intact | false |
| COG6 | Intact | false |
| CRLF3 | Intact | false |
| DDIT4L | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
