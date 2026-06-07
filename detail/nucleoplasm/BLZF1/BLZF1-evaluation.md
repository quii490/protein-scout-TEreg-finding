---
type: protein-evaluation
gene: "BLZF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BLZF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BLZF1 / JEM1 |
| 蛋白名称 | Golgin-45 |
| 蛋白大小 | 400 aa / 44.9 kDa |
| UniProt ID | Q9H2G9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Golgi apparatus membrane; Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 400 aa / 44.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027095, IPR013183; Pfam: PF08227 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Supported |
| UniProt | Golgi apparatus membrane; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cis-Golgi network (GO:0005801)
- cytoplasm (GO:0005737)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: JEM1 |

**关键文献**:
1. Mutation, methylation, and gene expression profiles in dup(1q)-positive pediatric B-cell precursor acute lymphoblastic leukemia.. *Leukemia*. PMID: 29626196
2. BLZF1 expression is of prognostic significance in hepatocellular carcinoma.. *Biochemical and biophysical research communications*. PMID: 26342799
3. Identification of key genes and pathways in castrate-resistant prostate cancer by integrated bioinformatics analysis.. *Pathology, research and practice*. PMID: 32853947
4. The role of BLZF1 in lung adenocarcinoma and its value as a diagnostic and prognostic biomarker.. *Scientific reports*. PMID: 41820452
5. Genomic organization of the JEM-1 (BLZF1) gene on human chromosome 1q24: molecular cloning and analysis of its promoter region.. *Genomics*. PMID: 11056056

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.4 |
| 高置信度残基 (pLDDT>90) 占比 | 40.0% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 22.0% |
| 低置信 (pLDDT<50) 占比 | 25.5% |
| 有序区域 (pLDDT>70) 占比 | 52.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.4，有序区 52.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027095, IPR013183; Pfam: PF08227 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GORASP2 | 0.999 | 0.855 | — |
| RAB2A | 0.993 | 0.360 | — |
| GORASP1 | 0.980 | 0.535 | — |
| ACBD3 | 0.898 | 0.436 | — |
| GOLGA2 | 0.789 | 0.000 | — |
| GOLGA5 | 0.731 | 0.000 | — |
| MBD4 | 0.720 | 0.000 | — |
| TNKS | 0.698 | 0.602 | — |
| TMED3 | 0.693 | 0.610 | — |
| RNF146 | 0.687 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RHEBL1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11703|pubmed:20368287 |
| RHEB | psi-mi:"MI:0018"(two hybrid) | imex:IM-11703|pubmed:20368287 |
| PB2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| GORASP2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| TMED3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CINP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| RAB2A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| LMO1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ZBTB24 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| OAZ3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.4 + PDB: 无 | pLDDT=71.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Nucleus; Cytoplasm / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. BLZF1 — Golgin-45，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小400 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H2G9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117475-BLZF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BLZF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H2G9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000117475-BLZF1/subcellular

![](https://images.proteinatlas.org/67113/2267_G8_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/67113/2267_G8_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/67113/1237_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/67113/1237_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/67113/1754_H5_13_cr57f3e9d007832_red_green.jpg)
![](https://images.proteinatlas.org/67113/1754_H5_18_cr57f3e9d94d62b_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H2G9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H2G9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027095;IPR013183; |
| Pfam | PF08227; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000117475-BLZF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GORASP2 | Intact, Biogrid, Opencell | true |
| PRKAB2 | Intact, Biogrid | true |
| TMED10 | Biogrid, Opencell, Bioplex | true |
| ZNF410 | Intact, Biogrid | true |
| AQP1 | Intact | false |
| ASXL1 | Biogrid | false |
| BAG3 | Intact | false |
| BAG4 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
