---
type: protein-evaluation
gene: "HEBP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HEBP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HEBP1 / HBP |
| 蛋白名称 | Heme-binding protein 1 |
| 蛋白大小 | 189 aa / 21.1 kDa |
| UniProt ID | Q9NRV9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 189 aa / 21.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011256, IPR006917; Pfam: PF04832 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HBP |

**关键文献**:
1. Heme-binding protein 1 delivered via pericyte-derived extracellular vesicles improves neurovascular regeneration in a mouse model of cavernous nerve injury.. *International journal of biological sciences*. PMID: 37324943
2. HEBP1 - An early trigger for neuronal cell death and circuit dysfunction in Alzheimer's disease.. *Seminars in cell & developmental biology*. PMID: 35842370
3. Identification of macrophage-associated diagnostic biomarkers and molecular subtypes in gestational diabetes mellitus based on machine learning.. *Artificial cells, nanomedicine, and biotechnology*. PMID: 40476676
4. Identification of Potential Biomarkers and Therapeutic Targets for Periodontitis.. *International dental journal*. PMID: 39532570
5. Association between genetically plasma proteins and osteonecrosis: a proteome-wide Mendelian randomization analysis.. *Frontiers in genetics*. PMID: 39119575

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.7 |
| 高置信度残基 (pLDDT>90) 占比 | 50.8% |
| 置信残基 (pLDDT 70-90) 占比 | 37.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 6.9% |
| 有序区域 (pLDDT>70) 占比 | 88.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.7，有序区 88.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011256, IPR006917; Pfam: PF04832 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FPR3 | 0.983 | 0.000 | — |
| FPR2 | 0.705 | 0.000 | — |
| FPR1 | 0.519 | 0.000 | — |
| APP | 0.512 | 0.000 | — |
| SRC | 0.505 | 0.000 | — |
| SAA1 | 0.501 | 0.000 | — |
| CCL23 | 0.499 | 0.000 | — |
| AGTR2 | 0.499 | 0.000 | — |
| AGT | 0.499 | 0.000 | — |
| FECH | 0.483 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KCNMA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-15154|pubmed:22174833 |
| metE | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Got1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:15627969|imex:IM-16651 |
| COQ8A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| NMES1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| COQ9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| NDUFS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| LARP1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| - | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| KSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.7 + PDB: 无 | pLDDT=84.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HEBP1 — Heme-binding protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小189 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRV9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000013583-HEBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HEBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRV9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000013583-HEBP1/subcellular

![](https://images.proteinatlas.org/56417/913_D3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/56417/913_D3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/56417/914_D3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/56417/914_D3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/56417/919_D3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/56417/919_D3_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRV9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NRV9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011256;IPR006917; |
| Pfam | PF04832; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000013583-HEBP1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
