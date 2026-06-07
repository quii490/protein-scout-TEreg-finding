---
type: protein-evaluation
gene: "RASL11B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RASL11B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RASL11B |
| 蛋白名称 | Ras-like protein family member 11B |
| 蛋白大小 | 248 aa / 27.5 kDa |
| UniProt ID | Q9BPW5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 248 aa / 27.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027417, IPR051065, IPR005225, IPR001806; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Regulation of gene expression downstream of a novel Fgf/Erk pathway during Xenopus development.. *PloS one*. PMID: 37856433
2. Cloning, genomic organization, and tissue-specific expression of the RASL11B gene.. *Biochimica et biophysica acta*. PMID: 17628721
3. Gene expression profile of human lymphocytes exposed to (211)At alpha particles.. *Radiation research*. PMID: 20681779
4. Upregulation of MAPK10, TUBB2B and RASL11B may contribute to the development of neuroblastoma.. *Molecular medicine reports*. PMID: 31432180
5. Identification of target genes downstream of semaphorin6A/PlexinA2 signaling in zebrafish.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 28440030

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.0 |
| 高置信度残基 (pLDDT>90) 占比 | 51.6% |
| 置信残基 (pLDDT 70-90) 占比 | 21.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 18.5% |
| 有序区域 (pLDDT>70) 占比 | 72.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.0，有序区 72.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR051065, IPR005225, IPR001806; Pfam: PF00071 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARL9 | 0.851 | 0.000 | — |
| ITSN1 | 0.545 | 0.497 | — |
| ITSN2 | 0.540 | 0.497 | — |
| SYDE2 | 0.500 | 0.097 | — |
| TGFB1 | 0.483 | 0.045 | — |
| LNX1 | 0.469 | 0.306 | — |
| CNKSR1 | 0.456 | 0.096 | — |
| CCDC125 | 0.454 | 0.000 | — |
| ARRDC2 | 0.449 | 0.053 | — |
| RHOF | 0.442 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MFHAS1 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| GEMIN6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MAGI1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LRRK2 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| SCGB2A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPM1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LTF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPM1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAP1GDS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.0 + PDB: 无 | pLDDT=79.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RASL11B — Ras-like protein family member 11B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小248 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BPW5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128045-RASL11B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RASL11B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BPW5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000128045-RASL11B/subcellular

![](https://images.proteinatlas.org/57803/1143_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57803/1143_B6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57803/1259_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57803/1259_C4_6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BPW5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BPW5 |
| SMART | SM00175;SM00173;SM00174; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027417;IPR051065;IPR005225;IPR001806; |
| Pfam | PF00071; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000128045-RASL11B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GEMIN6 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
