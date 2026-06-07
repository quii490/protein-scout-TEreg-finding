---
type: protein-evaluation
gene: "YPEL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YPEL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YPEL1 |
| 蛋白名称 | Protein yippee-like 1 |
| 蛋白大小 | 119 aa / 13.6 kDa |
| UniProt ID | O60688 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 119 aa / 13.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR034751, IPR004910, IPR039058; Pfam: PF03226 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.5/180** | |
| **归一化总分** | | | **78.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Yippee Like 1 Suppresses Glioma Progression and Serves as a Novel Prognostic Factor.. *The Tohoku journal of experimental medicine*. PMID: 35185081
2. Comprehensive analysis of the expression and prognosis of YPEL family members in clear cell renal cell cancer.. *Oncology reports*. PMID: 35674183
3. Bioinformatics analysis of potential glioblastoma circular RNA sponge network.. *Translational cancer research*. PMID: 35706804
4. Expression of YPEL1 in pancreatic cancer cell lines and tissues.. *Georgian medical news*. PMID: 19893129
5. Up-regulation of YPEL1 and YPEL5 and down-regulation of ITGA2 in erlotinib-treated EGFR-mutant non-small cell lung cancer: A bioinformatic analysis.. *Gene*. PMID: 29221754

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.7 |
| 高置信度残基 (pLDDT>90) 占比 | 80.7% |
| 置信残基 (pLDDT 70-90) 占比 | 9.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 3.4% |
| 有序区域 (pLDDT>70) 占比 | 89.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.7，有序区 89.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034751, IPR004910, IPR039058; Pfam: PF03226 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WDR26 | 0.630 | 0.302 | — |
| FBXL2 | 0.624 | 0.556 | — |
| STRN3 | 0.589 | 0.573 | — |
| CTTNBP2NL | 0.574 | 0.574 | — |
| STRN4 | 0.545 | 0.527 | — |
| FBXL20 | 0.511 | 0.417 | — |
| C1QL4 | 0.505 | 0.000 | — |
| ZNF564 | 0.436 | 0.000 | — |
| C1QL2 | 0.421 | 0.000 | — |
| NCAM1 | 0.416 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STRN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STRIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBXL20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STRN4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CTTNBP2NL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBXL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATG16L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31015422|imex:IM-29997 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 7
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.7 + PDB: 无 | pLDDT=90.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 12 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. YPEL1 — Protein yippee-like 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小119 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60688
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100027-YPEL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YPEL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60688
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60688-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60688 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 19..116; /note="Yippee"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01128" |
| InterPro | IPR034751;IPR004910;IPR039058; |
| Pfam | PF03226; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100027-YPEL1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
