---
type: protein-evaluation
gene: "TRIR"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRIR 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIR / C19orf43 |
| 蛋白名称 | Telomerase RNA component interacting RNase |
| 蛋白大小 | 176 aa / 18.4 kDa |
| UniProt ID | Q9BQ61 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 176 aa / 18.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038838 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

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

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 246 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C19orf43 |

**关键文献**:
1. Characterisation of the triclosan efflux pump TriABC and its regulator TriR in Agrobacterium tumefaciens C58.. *Microbiological research*. PMID: 35810656
2. A novel disulfidptosis-related mRNA signature predicts prognosis and therapeutic response in lung squamous cell carcinoma.. *BMC pulmonary medicine*. PMID: 41063164
3. Unraveling the Photoactivation Mechanism of a Light-Activated Adenylyl Cyclase Using Ultrafast Spectroscopy Coupled with Unnatural Amino Acid Mutagenesis.. *ACS chemical biology*. PMID: 36038143
4. Electron-transfer acceleration investigated by time resolved infrared spectroscopy.. *Accounts of chemical research*. PMID: 25699661
5. N-acyl-homoserine lactone inhibition of rhizobial growth is mediated by two quorum-sensing genes that regulate plasmid transfer.. *Journal of bacteriology*. PMID: 12142421

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.0 |
| 高置信度残基 (pLDDT>90) 占比 | 5.1% |
| 置信残基 (pLDDT 70-90) 占比 | 22.2% |
| 中等置信 (pLDDT 50-70) 占比 | 48.9% |
| 低置信 (pLDDT<50) 占比 | 23.9% |
| 有序区域 (pLDDT>70) 占比 | 27.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.0），有序残基占 27.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038838 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COX5A | 0.976 | 0.784 | — |
| COX7C | 0.973 | 0.784 | — |
| UQCRB | 0.970 | 0.783 | — |
| COX5B | 0.968 | 0.784 | — |
| UQCR10 | 0.955 | 0.785 | — |
| UQCRQ | 0.935 | 0.744 | — |
| UQCRFS1 | 0.924 | 0.784 | — |
| UQCRC2 | 0.923 | 0.784 | — |
| CYC1 | 0.918 | 0.786 | — |
| MT-CO3 | 0.900 | 0.783 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SNRPA | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| glpA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000242784.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ERBB3 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| PRKD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| OTUB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-23897|pubmed:26752685 |
| MYO1C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| EMC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MMGT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SLC33A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.0 + PDB: 无 | pLDDT=62.0, v6 | 仅预测 |
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
1. TRIR — Telomerase RNA component interacting RNase，非常新颖，仅有少数基础研究。
2. 蛋白大小176 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQ61
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123144-TRIR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQ61
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000123144-TRIR/subcellular

![](https://images.proteinatlas.org/59965/1018_D8_4_red_green.jpg)
![](https://images.proteinatlas.org/59965/1018_D8_5_red_green.jpg)
![](https://images.proteinatlas.org/59965/1043_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/59965/1043_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/59965/1218_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/59965/1218_D8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BQ61-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BQ61 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR038838; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000123144-TRIR/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SNRPA | Intact, Biogrid | true |
| CEBPA | Biogrid | false |
| RBM17 | Opencell | false |
| SF3B1 | Opencell | false |
| U2SURP | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
