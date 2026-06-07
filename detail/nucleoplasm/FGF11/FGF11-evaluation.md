---
type: protein-evaluation
gene: "FGF11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FGF11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FGF11 / FHF3 |
| 蛋白名称 | Fibroblast growth factor 11 |
| 蛋白大小 | 225 aa / 25.0 kDa |
| UniProt ID | Q92914 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Centrosome; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 225 aa / 25.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=59 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002209, IPR008996; Pfam: PF00167 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 59 |
| PubMed broad count | 94 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FHF3 |

**关键文献**:
1. Fibroblast Growth Factor (FGF) 13.. *Differentiation; research in biological diversity*. PMID: 39332965
2. Production and purification of recombinant long protein isoforms of FGF11 subfamily.. *Journal of biotechnology*. PMID: 40154621
3. Silencing of hypothalamic FGF11 prevents diet-induced obesity.. *Molecular brain*. PMID: 36064426
4. FGF12: biology and function.. *Differentiation; research in biological diversity*. PMID: 38042708
5. Fibroblast growth factor 11 inhibits foot-and-mouth disease virus gene expression and replication in vitro.. *The Journal of veterinary medical science*. PMID: 35387954

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.1 |
| 高置信度残基 (pLDDT>90) 占比 | 61.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.0% |
| 中等置信 (pLDDT 50-70) 占比 | 23.1% |
| 低置信 (pLDDT<50) 占比 | 11.1% |
| 有序区域 (pLDDT>70) 占比 | 65.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.1，有序区 65.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002209, IPR008996; Pfam: PF00167 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FGFR4 | 0.725 | 0.311 | — |
| FGFR1 | 0.722 | 0.311 | — |
| FGF17 | 0.702 | 0.000 | — |
| FGFR2 | 0.684 | 0.311 | — |
| FGFR3 | 0.678 | 0.311 | — |
| FGF23 | 0.620 | 0.000 | — |
| KL | 0.574 | 0.045 | — |
| APOD | 0.567 | 0.000 | — |
| FGFRL1 | 0.552 | 0.311 | — |
| RPL22 | 0.549 | 0.549 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HMBOX1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RPL22 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| STAC3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| THAP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NOS1AP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ANKRD17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MLYCD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MYC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRKAR1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MLLT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.1 + PDB: 无 | pLDDT=81.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FGF11 — Fibroblast growth factor 11，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小225 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 59 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92914
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161958-FGF11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FGF11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92914
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (approved)。来源: https://www.proteinatlas.org/ENSG00000161958-FGF11/subcellular

![](https://images.proteinatlas.org/66605/1244_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66605/1244_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/66605/1247_D11_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/66605/1247_D11_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/66605/1573_C7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66605/1573_C7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92914-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92914 |
| SMART | SM00442; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002209;IPR008996; |
| Pfam | PF00167; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000161958-FGF11/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AHCYL1 | Biogrid | false |
| HIF1A | Biogrid | false |
| HMBOX1 | Intact | false |
| MDM2 | Biogrid | false |
| RPL22 | Intact | false |
| SIRT1 | Biogrid | false |
| STAC3 | Intact | false |
| THAP1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
