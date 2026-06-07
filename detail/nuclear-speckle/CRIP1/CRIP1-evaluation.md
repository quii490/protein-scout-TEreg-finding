---
type: protein-evaluation
gene: "CRIP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRIP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRIP1 / CRIP, CRP1 |
| 蛋白名称 | Cysteine-rich protein 1 |
| 蛋白大小 | 77 aa / 8.5 kDa |
| UniProt ID | P50238 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear speckles, Cytosol; 额外: Plasma membrane, Centrosome; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 77 aa / 8.5 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=93 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001781; Pfam: PF00412 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Cytosol; 额外: Plasma membrane, Centrosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 93 |
| PubMed broad count | 150 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CRIP, CRP1 |

**关键文献**:
1. CRIP1 fosters MDSC trafficking and resets tumour microenvironment via facilitating NF-κB/p65 nuclear translocation in pancreatic ductal adenocarcinoma.. *Gut*. PMID: 37541772
2. CRIP1 Reshapes the Gastric Cancer Microenvironment to Facilitate Development of Lymphatic Metastasis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37409440
3. CRIP1 suppresses BBOX1-mediated carnitine metabolism to promote stemness in hepatocellular carcinoma.. *The EMBO journal*. PMID: 35775648
4. CRIP1 regulates osteogenic differentiation of bone marrow stromal cells and pre-osteoblasts via the Wnt signaling pathway.. *Biochemical and biophysical research communications*. PMID: 38936225
5. CRIP1 involves the pathogenesis of multiple myeloma via dual-regulation of proteasome and autophagy.. *EBioMedicine*. PMID: 38199044

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 23.4% |
| 置信残基 (pLDDT 70-90) 占比 | 58.4% |
| 中等置信 (pLDDT 50-70) 占比 | 16.9% |
| 低置信 (pLDDT<50) 占比 | 1.3% |
| 有序区域 (pLDDT>70) 占比 | 81.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.8，有序区 81.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001781; Pfam: PF00412 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LMO1 | 0.774 | 0.000 | — |
| LMO2 | 0.617 | 0.000 | — |
| SPARC | 0.603 | 0.000 | — |
| CAPG | 0.598 | 0.469 | — |
| S100A6 | 0.527 | 0.046 | — |
| FGD2 | 0.482 | 0.054 | — |
| S100A10 | 0.476 | 0.000 | — |
| MTA1 | 0.472 | 0.000 | — |
| AGO2 | 0.472 | 0.000 | — |
| ASB9 | 0.461 | 0.051 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VOPP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SH3GL3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SH2D3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| PRKD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| TK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP2R5E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35063084|imex:IM-29773 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 无 | pLDDT=81.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles, Cytosol; 额外: Plasma membrane, Ce | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. CRIP1 — Cysteine-rich protein 1，研究基础较多，新颖性有限。
2. 蛋白大小77 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 93 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50238
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213145-CRIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50238
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000213145-CRIP1/subcellular

![](https://images.proteinatlas.org/42462/1126_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/42462/1126_D1_4_red_green.jpg)
![](https://images.proteinatlas.org/42462/1573_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/42462/1573_A1_3_red_green.jpg)
![](https://images.proteinatlas.org/42462/480_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/42462/480_F5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P50238-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P50238 |
| SMART | SM00132; |
| UniProt Domain [FT] | DOMAIN 2..63; /note="LIM zinc-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125" |
| InterPro | IPR001781; |
| Pfam | PF00412; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000213145-CRIP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| STUB1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
