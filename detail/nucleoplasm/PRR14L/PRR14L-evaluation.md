---
type: protein-evaluation
gene: "PRR14L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRR14L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRR14L / C22orf30 |
| 蛋白名称 | Protein PRR14L |
| 蛋白大小 | 2151 aa / 237.3 kDa |
| UniProt ID | Q5THK1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 2/10 | ×1 | 2 | 2151 aa / 237.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=35.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026320, IPR028149; Pfam: PF15386 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C22orf30 |

**关键文献**:
1. Next-Generation Sequencing Analysis of 3 Uterine Adenosarcomas with Heterogeneously Differentiated Genomic Mutations.. *International journal of analytical chemistry*. PMID: 37810911
2. A seven-gene signature predicts overall survival of patients with colorectal cancer.. *Oncotarget*. PMID: 29221110
3. The scaffold protein PRR14L links the PP2A-TACC3 axis to mitotic fidelity and sensitivity to MPS1 inhibition.. *bioRxiv : the preprint server for biology*. PMID: 41279925
4. PRR14L mutations are associated with chromosome 22 acquired uniparental disomy, age-related clonal hematopoiesis and myeloid neoplasia.. *Leukemia*. PMID: 30573780
5. Glucose-Induced Changes in Gene Expression in Human Pancreatic Islets: Causes or Consequences of Chronic Hyperglycemia.. *Diabetes*. PMID: 28882899

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 35.5 |
| 高置信度残基 (pLDDT>90) 占比 | 0.7% |
| 置信残基 (pLDDT 70-90) 占比 | 1.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 91.3% |
| 有序区域 (pLDDT>70) 占比 | 2.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=35.5），有序残基占 2.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026320, IPR028149; Pfam: PF15386 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHD8 | 0.792 | 0.107 | — |
| PPP2R1A | 0.678 | 0.676 | — |
| NHLRC3 | 0.675 | 0.071 | — |
| PPP2CA | 0.666 | 0.657 | — |
| PPP2CB | 0.647 | 0.638 | — |
| PPIP5K2 | 0.551 | 0.045 | — |
| ZDHHC21 | 0.527 | 0.053 | — |
| DIDO1 | 0.485 | 0.113 | — |
| KYAT1 | 0.483 | 0.047 | — |
| CCDC87 | 0.480 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP2CA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| PPP2CB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| PPP2R1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| HSP90AA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19875381 |
| PB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| STK35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Bap1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CSNK2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=35.5 + PDB: 无 | pLDDT=35.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PRR14L — Protein PRR14L，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2151 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=35.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5THK1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183530-PRR14L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRR14L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5THK1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5THK1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000183530-PRR14L/subcellular

![](https://images.proteinatlas.org/62645/1106_F8_3_red_green.jpg)
![](https://images.proteinatlas.org/62645/1106_F8_4_red_green.jpg)
![](https://images.proteinatlas.org/62645/1148_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/62645/1148_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/62645/1169_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/62645/1169_F7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5THK1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026320;IPR028149; |
| Pfam | PF15386; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183530-PRR14L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PPP2CA | Biogrid | false |
| PPP2CB | Biogrid | false |
| PPP2R1A | Biogrid | false |
| PTGES3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
