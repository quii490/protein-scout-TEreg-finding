---
type: protein-evaluation
gene: "PUDP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PUDP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PUDP / DXF68S1E, FAM16AX, GS1, HDHD1, HDHD1A |
| 蛋白名称 | Pseudouridine-5'-phosphatase |
| 蛋白大小 | 228 aa / 25.2 kDa |
| UniProt ID | Q08623 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 228 aa / 25.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=97.4; PDB: 3L5K, 9M7L, 9M7M |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045228, IPR036412, IPR006439, IPR041492, IPR023 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DXF68S1E, FAM16AX, GS1, HDHD1, HDHD1A |

**关键文献**:
1. STS and PUDP Deletion Identified by Targeted Panel Sequencing with CNV Analysis in X-Linked Ichthyosis: A Case Report and Literature Review.. *Genes*. PMID: 37895274
2. X chromosome dosage and the genetic impact across human tissues.. *Genome medicine*. PMID: 36978128
3. DNA polymorphisms predict time to progression from uncomplicated to complicated Crohn's disease.. *European journal of gastroenterology & hepatology*. PMID: 29293112
4. Novel Microdeletion in the X Chromosome Leads to Kallmann Syndrome, Ichthyosis, Obesity, and Strabismus.. *Frontiers in genetics*. PMID: 32670353
5. Identification of Gender-Specific Molecular Differences in Glioblastoma (GBM) and Low-Grade Glioma (LGG) by the Analysis of Large Transcriptomic and Epigenomic Datasets.. *Frontiers in oncology*. PMID: 34621669

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.4 |
| 高置信度残基 (pLDDT>90) 占比 | 96.9% |
| 置信残基 (pLDDT 70-90) 占比 | 2.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.4% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.5% |
| 可用 PDB 条目 | 3L5K, 9M7L, 9M7M |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3L5K, 9M7L, 9M7M）+ AlphaFold高质量预测（pLDDT=97.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045228, IPR036412, IPR006439, IPR041492, IPR023214; Pfam: PF13419 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PGGHG | 0.914 | 0.000 | — |
| GPI | 0.897 | 0.000 | — |
| AGXT | 0.896 | 0.000 | — |
| YIPF6 | 0.888 | 0.000 | — |
| PNPLA4 | 0.872 | 0.000 | — |
| STS | 0.872 | 0.000 | — |
| MPI | 0.858 | 0.065 | — |
| YRDC | 0.845 | 0.000 | — |
| PGM3 | 0.823 | 0.455 | — |
| ADHFE1 | 0.810 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAGEA4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GLYCTK | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AIRIM | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TXNRD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ARHGAP32 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HDAC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AP1G2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HAUS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SBF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCZ1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.4 + PDB: 3L5K, 9M7L, 9M7M | pLDDT=97.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PUDP — Pseudouridine-5'-phosphatase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小228 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q08623
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130021-PUDP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PUDP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q08623
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000130021-PUDP/subcellular

![](https://images.proteinatlas.org/292/1910_C2_5_red_green.jpg)
![](https://images.proteinatlas.org/292/1910_C2_6_red_green.jpg)
![](https://images.proteinatlas.org/292/1972_H6_31_red_green.jpg)
![](https://images.proteinatlas.org/292/1972_H6_33_red_green.jpg)
![](https://images.proteinatlas.org/292/2032_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/292/2032_F2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q08623-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q08623 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR045228;IPR036412;IPR006439;IPR041492;IPR023214;IPR023198; |
| Pfam | PF13419; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000130021-PUDP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AP1G2 | Bioplex | false |
| ARAP3 | Bioplex | false |
| ASCC3 | Bioplex | false |
| BBS2 | Bioplex | false |
| C1orf109 | Intact | false |
| CCZ1B | Bioplex | false |
| EIF2A | Bioplex | false |
| FAM91A1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
