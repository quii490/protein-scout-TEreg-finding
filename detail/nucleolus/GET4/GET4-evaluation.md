---
type: protein-evaluation
gene: "GET4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GET4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GET4 / C7orf20, CEE, TRC35 |
| 蛋白名称 | Golgi to ER traffic protein 4 homolog |
| 蛋白大小 | 327 aa / 36.5 kDa |
| UniProt ID | Q7L5D6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Cytosol; 额外: Nucleoplasm, Mitotic chromosome; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 327 aa / 36.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.6; PDB: 6AU8, 7RU9, 7RUA, 7RUC |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007317, IPR011990; Pfam: PF04190 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol; 额外: Nucleoplasm, Mitotic chromosome | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- BAT3 complex (GO:0071818)
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 55 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C7orf20, CEE, TRC35 |

**关键文献**:
1. Genome-wide CRISPR/Cas9 screen shows that loss of GET4 increases mitochondria-endoplasmic reticulum contact sites and is neuroprotective.. *Cell death & disease*. PMID: 38467609
2. Structures of Get3, Get4, and Get5 provide new models for TA membrane protein targeting.. *Structure (London, England : 1993)*. PMID: 20696390
3. Crystal structure of Get4-Get5 complex and its interactions with Sgt2, Get3, and Ydj1.. *The Journal of biological chemistry*. PMID: 20106980
4. Structural insights into metazoan pretargeting GET complexes.. *Nature structural & molecular biology*. PMID: 34887561
5. Deciphering the molecular organization of GET pathway chaperones through native mass spectrometry.. *Biophysical journal*. PMID: 35189106

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.6 |
| 高置信度残基 (pLDDT>90) 占比 | 76.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 8.9% |
| 有序区域 (pLDDT>70) 占比 | 82.3% |
| 可用 PDB 条目 | 6AU8, 7RU9, 7RUA, 7RUC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6AU8, 7RU9, 7RUA, 7RUC）+ AlphaFold高质量预测（pLDDT=87.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007317, IPR011990; Pfam: PF04190 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BAG6 | 0.999 | 0.991 | — |
| SGTA | 0.999 | 0.850 | — |
| UBL4A | 0.999 | 0.901 | — |
| GET3 | 0.999 | 0.991 | — |
| GET1 | 0.958 | 0.124 | — |
| RNF126 | 0.956 | 0.847 | — |
| SGTB | 0.899 | 0.542 | — |
| CAMLG | 0.888 | 0.000 | — |
| AMFR | 0.796 | 0.514 | — |
| SEC61B | 0.795 | 0.314 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EMI2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| LYS9 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| VMA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SGT2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| EEF1G | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CEP126 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| KAT5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CAPNS1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PLK1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.6 + PDB: 6AU8, 7RU9, 7RUA, 7RUC | pLDDT=87.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nucleoli, Cytosol; 额外: Nucleoplasm, Mitotic chromo | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GET4 — Golgi to ER traffic protein 4 homolog，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小327 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L5D6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000239857-GET4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GET4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L5D6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L5D6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7L5D6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007317;IPR011990; |
| Pfam | PF04190; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000239857-GET4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BAG6 | Biogrid, Opencell | true |
| GET3 | Intact, Biogrid, Bioplex | true |
| PRKAB2 | Intact, Biogrid | true |
| RNF126 | Biogrid, Opencell | true |
| SHARPIN | Biogrid, Bioplex | true |
| UBL4A | Biogrid, Opencell, Bioplex | true |
| AMFR | Biogrid | false |
| C1orf109 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
