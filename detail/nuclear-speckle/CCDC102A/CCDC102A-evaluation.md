---
type: protein-evaluation
gene: "CCDC102A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC102A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC102A |
| 蛋白名称 | Coiled-coil domain-containing protein 102A |
| 蛋白大小 | 550 aa / 62.6 kDa |
| UniProt ID | Q96A19 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 550 aa / 62.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002928; Pfam: PF01576 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- myosin complex (GO:0016459)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. MYO5B and the Polygenic Landscape of Very Early-Onset Inflammatory Bowel Disease in an Ethnically Diverse Population.. *Inflammatory bowel diseases*. PMID: 39096520
2. Prediction significance of autophagy-related genes in survival probability and drug resistance in diffuse large B-cell lymphoma.. *Aging*. PMID: 38240686
3. Identification and validation of a prognostic risk-scoring model for AML based on m(7)G-associated gene clustering.. *Frontiers in oncology*. PMID: 38273850
4. Comprehensive Analysis of Crucial m(6)A-Related Differentially Expressed Genes in Psoriasis.. *Frontiers in bioscience (Landmark edition)*. PMID: 39344312
5. Dual roles of CCDC102A in governing centrosome duplication and cohesion.. *Cell reports*. PMID: 38280197

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.2 |
| 高置信度残基 (pLDDT>90) 占比 | 56.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 27.3% |
| 有序区域 (pLDDT>70) 占比 | 64.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.2，有序区 64.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002928; Pfam: PF01576 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KIAA1671 | 0.534 | 0.000 | — |
| CCDC102B | 0.518 | 0.450 | — |
| DOK4 | 0.502 | 0.000 | — |
| CDC42EP4 | 0.498 | 0.000 | — |
| GALNT16 | 0.492 | 0.000 | — |
| HEG1 | 0.470 | 0.000 | — |
| SUGCT | 0.461 | 0.000 | — |
| FAM207A | 0.460 | 0.000 | — |
| KTN1 | 0.460 | 0.000 | — |
| ERLEC1 | 0.458 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.2 + PDB: 无 | pLDDT=76.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CCDC102A — Coiled-coil domain-containing protein 102A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小550 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96A19
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135736-CCDC102A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC102A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96A19
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000135736-CCDC102A/subcellular

![](https://images.proteinatlas.org/40598/460_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/40598/460_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/40598/465_D1_3_red_green.jpg)
![](https://images.proteinatlas.org/40598/465_D1_4_red_green.jpg)
![](https://images.proteinatlas.org/40598/467_D1_3_red_green.jpg)
![](https://images.proteinatlas.org/40598/467_D1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96A19-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96A19 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002928; |
| Pfam | PF01576; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135736-CCDC102A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LACTB | Intact | false |
| RAB3IL1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
