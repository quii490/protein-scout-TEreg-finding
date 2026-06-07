---
type: protein-evaluation
gene: "LAGE3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LAGE3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LAGE3 / DXS9879E, ESO3, ITBA2 |
| 蛋白名称 | EKC/KEOPS complex subunit LAGE3 |
| 蛋白大小 | 143 aa / 14.8 kDa |
| UniProt ID | Q14657 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 143 aa / 14.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=74.1; PDB: 6GWJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015419; Pfam: PF09341 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- EKC/KEOPS complex (GO:0000408)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DXS9879E, ESO3, ITBA2 |

**关键文献**:
1. Mutations in KEOPS-complex genes cause nephrotic syndrome with primary microcephaly.. *Nature genetics*. PMID: 28805828
2. Up-regulation of L Antigen Family Member 3 Associates With Aggressive Progression of Breast Cancer.. *Frontiers in oncology*. PMID: 33552947
3. Identification and validation of L Antigen Family Member 3 as an immune-related biomarker associated with the progression of papillary thyroid cancer.. *International immunopharmacology*. PMID: 33310661
4. Identification of host cellular proteins LAGE3 and IGFBP6 that interact with orf virus protein ORFV024.. *Gene*. PMID: 29605601
5. Correlation of LAGE3 with unfavorable prognosis and promoting tumor development in HCC via PI3K/AKT/mTOR and Ras/RAF/MAPK pathways.. *BMC cancer*. PMID: 35313850

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.1 |
| 高置信度残基 (pLDDT>90) 占比 | 40.6% |
| 置信残基 (pLDDT 70-90) 占比 | 13.3% |
| 中等置信 (pLDDT 50-70) 占比 | 32.2% |
| 低置信 (pLDDT<50) 占比 | 14.0% |
| 有序区域 (pLDDT>70) 占比 | 53.9% |
| 可用 PDB 条目 | 6GWJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=74.1，有序区 53.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015419; Pfam: PF09341 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OSGEP | 0.999 | 0.992 | — |
| TP53RK | 0.999 | 0.736 | — |
| GON7 | 0.999 | 0.981 | — |
| TPRKB | 0.999 | 0.655 | — |
| TMEM187 | 0.946 | 0.000 | — |
| OSGEPL1 | 0.902 | 0.347 | — |
| YRDC | 0.847 | 0.000 | — |
| NUP43 | 0.788 | 0.785 | — |
| L1CAM | 0.679 | 0.000 | — |
| HCFC1 | 0.675 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| OSGEP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SQSTM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| TP53RK | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-17703 |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| PNMA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GON7 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.1 + PDB: 6GWJ | pLDDT=74.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LAGE3 — EKC/KEOPS complex subunit LAGE3，非常新颖，仅有少数基础研究。
2. 蛋白大小143 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14657
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196976-LAGE3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LAGE3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14657
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000196976-LAGE3/subcellular

![](https://images.proteinatlas.org/36122/824_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/36122/824_H3_3_red_green.jpg)
![](https://images.proteinatlas.org/36122/884_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/36122/884_H3_3_red_green.jpg)
![](https://images.proteinatlas.org/36122/978_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/36122/978_H3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14657-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14657 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR015419; |
| Pfam | PF09341; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000196976-LAGE3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC28B | Intact, Biogrid | true |
| GON7 | Intact, Biogrid, Bioplex | true |
| OSGEP | Intact, Biogrid, Bioplex | true |
| POP7 | Intact, Biogrid, Bioplex | true |
| PRAME | Biogrid, Bioplex | true |
| TP53RK | Biogrid, Bioplex | true |
| TPRKB | Biogrid, Bioplex | true |
| AKAP8L | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
