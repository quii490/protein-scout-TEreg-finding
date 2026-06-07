---
type: protein-evaluation
gene: "HDHD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HDHD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HDHD3 / C9orf158 |
| 蛋白名称 | Haloacid dehalogenase-like hydrolase domain-containing protein 3 |
| 蛋白大小 | 251 aa / 28.0 kDa |
| UniProt ID | Q9BSH5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Vesicles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 251 aa / 28.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.7; PDB: 3K1Z |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051828, IPR036412, IPR006439, IPR011949, IPR044 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Vesicles | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf158 |

**关键文献**:
1. The first study on the effect of crocodile oil from Crocodylus siamensis on hepatic mitochondrial function for energy homeostasis in rats.. *Veterinary world*. PMID: 35698522
2. Machine learning deciphers the significance of mitochondrial regulators on the diagnosis and subtype classification in non-alcoholic fatty liver disease.. *Heliyon*. PMID: 38707433
3. Effects of Three-Month Administration of High-Saturated Fat Diet and High-Polyunsaturated Fat Diets with Different Linoleic Acid (LA, C18:2n-6) to α-Linolenic Acid (ALA, C18:3n-3) Ratio on the Mouse Liver Proteome.. *Nutrients*. PMID: 34063343
4. Mulberry-Derived 1-Deoxynojirimycin Prevents Type 2 Diabetes Mellitus Progression via Modulation of Retinol-Binding Protein 4 and Haptoglobin.. *Nutrients*. PMID: 36364802
5. Proteomic landscape of colorectal cancer liver metastasis: molecular signatures and novel therapeutic targets.. *PeerJ*. PMID: 41769411

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.7 |
| 高置信度残基 (pLDDT>90) 占比 | 95.2% |
| 置信残基 (pLDDT 70-90) 占比 | 2.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 1.6% |
| 有序区域 (pLDDT>70) 占比 | 97.2% |
| 可用 PDB 条目 | 3K1Z |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.7，有序区 97.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051828, IPR036412, IPR006439, IPR011949, IPR044924; Pfam: PF00702 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PSAT1 | 0.757 | 0.000 | — |
| NT5E | 0.742 | 0.000 | — |
| PNP | 0.588 | 0.000 | — |
| MTAP | 0.579 | 0.000 | — |
| SHMT1 | 0.523 | 0.000 | — |
| GNE | 0.515 | 0.000 | — |
| TSPEAR | 0.513 | 0.000 | — |
| SHMT2 | 0.511 | 0.000 | — |
| NUDT12 | 0.505 | 0.000 | — |
| C10orf120 | 0.505 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIP13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MTHFD2L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FANCL | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PLSCR4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TLE5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FOXH1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CSTF2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| CYSRT1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SMYD1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.7 + PDB: 3K1Z | pLDDT=95.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HDHD3 — Haloacid dehalogenase-like hydrolase domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小251 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BSH5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119431-HDHD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HDHD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BSH5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000119431-HDHD3/subcellular

![](https://images.proteinatlas.org/20427/1030_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20427/1030_H4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/20427/1207_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20427/1207_E9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/20427/191_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20427/191_G11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BSH5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BSH5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR051828;IPR036412;IPR006439;IPR011949;IPR044924;IPR023214; |
| Pfam | PF00702; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119431-HDHD3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSTF2 | Intact | false |
| CYP24A1 | Bioplex | false |
| CYSRT1 | Intact | false |
| FANCL | Intact | false |
| FOXH1 | Intact | false |
| KLHL38 | Intact | false |
| LONP1 | Bioplex | false |
| MCCC1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
