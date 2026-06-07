---
type: protein-evaluation
gene: "HEMGN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HEMGN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HEMGN / EDAG, NDR |
| 蛋白名称 | Hemogen |
| 蛋白大小 | 484 aa / 55.3 kDa |
| UniProt ID | Q9BXL5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 484 aa / 55.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033272 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EDAG, NDR |

**关键文献**:
1. Hemgn Protects Hematopoietic Stem and Progenitor Cells Against Transplantation Stress Through Negatively Regulating IFN-γ Signaling.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 34923767
2. HEMGN and SLC2A1 might be potential diagnostic biomarkers of steroid-induced osteonecrosis of femoral head: study based on WGCNA and DEGs screening.. *BMC musculoskeletal disorders*. PMID: 33451334
3. Upregulation of nuclear protein Hemgn by transcriptional repressor Gfi1 through repressing PU.1 contributes to the anti-apoptotic activity of Gfi1.. *The Journal of biological chemistry*. PMID: 39374784
4. Genetic Regulation of Avian Testis Development.. *Genes*. PMID: 34573441
5. Cancer/testis antigen HEMGN correlated with immune infiltration serves as a prognostic biomarker in lung adenocarcinoma.. *Molecular immunology*. PMID: 36563642

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.0 |
| 高置信度残基 (pLDDT>90) 占比 | 3.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.5% |
| 中等置信 (pLDDT 50-70) 占比 | 50.4% |
| 低置信 (pLDDT<50) 占比 | 42.8% |
| 有序区域 (pLDDT>70) 占比 | 6.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.0），有序残基占 6.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033272 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GYPA | 0.834 | 0.000 | — |
| TRMO | 0.821 | 0.000 | — |
| EPB42 | 0.804 | 0.000 | — |
| AHSP | 0.748 | 0.000 | — |
| GYPB | 0.747 | 0.000 | — |
| KLF1 | 0.699 | 0.000 | — |
| GATA1 | 0.692 | 0.292 | — |
| SLC4A1 | 0.676 | 0.000 | — |
| SPTA1 | 0.667 | 0.000 | — |
| SP100 | 0.666 | 0.474 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CTBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| Insr | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:30300385|imex:IM-26942| |
| QKI | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |
| HNRNPC | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.0 + PDB: 无 | pLDDT=54.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HEMGN — Hemogen，非常新颖，仅有少数基础研究。
2. 蛋白大小484 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXL5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136929-HEMGN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HEMGN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXL5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HEMGN/IF_images/K-562_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HEMGN/IF_images/HEL_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000136929-HEMGN/subcellular

![](https://images.proteinatlas.org/19572/1848_F9_31_red_green.jpg)
![](https://images.proteinatlas.org/19572/1848_F9_34_red_green.jpg)
![](https://images.proteinatlas.org/19572/1892_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/19572/1892_G5_4_red_green.jpg)
![](https://images.proteinatlas.org/19604/1848_C9_31_red_green.jpg)
![](https://images.proteinatlas.org/19604/1848_C9_32_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BXL5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BXL5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR033272; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000136929-HEMGN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CTBP1 | Intact, Biogrid | true |
| NPM1 | Intact, Biogrid | true |
| COPS4 | Biogrid | false |
| EP300 | Biogrid | false |
| FBL | Biogrid | false |
| GATA1 | Biogrid | false |
| HMG20A | Biogrid | false |
| HSPA8 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
