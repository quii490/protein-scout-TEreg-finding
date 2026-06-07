---
type: protein-evaluation
gene: "FLI1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FLI1 — REJECTED (研究热度过高 (PubMed strict=1500，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FLI1 |
| 蛋白名称 | Friend leukemia integration 1 transcription factor |
| 蛋白大小 | 452 aa / 51.0 kDa |
| UniProt ID | Q01543 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 452 aa / 51.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1500 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.4; PDB: 1FLI, 1X66, 2YTU, 5E8G, 5E8I, 5JVT, 6VG2 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR003118, IPR013761, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1500 |
| PubMed broad count | 2440 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Ewing sarcoma.. *Nature reviews. Disease primers*. PMID: 29977059
2. EWS-FLI1 utilizes divergent chromatin remodeling mechanisms to directly activate or repress enhancer elements in Ewing sarcoma.. *Cancer cell*. PMID: 25453903
3. The O-glycosyltransferase C1GALT1 promotes EWSR1::FLI1 expression and is a therapeutic target for Ewing sarcoma.. *Nature communications*. PMID: 39894896
4. Ceramide-induced cleavage of GPR64 intracellular domain drives Ewing sarcoma.. *Cell reports*. PMID: 39024100
5. Disruption of Microhomology-mediated End-joining in Ewing Sarcoma.. *bioRxiv : the preprint server for biology*. PMID: 40568108

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.4 |
| 高置信度残基 (pLDDT>90) 占比 | 29.6% |
| 置信残基 (pLDDT 70-90) 占比 | 10.2% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 48.5% |
| 有序区域 (pLDDT>70) 占比 | 39.8% |
| 可用 PDB 条目 | 1FLI, 1X66, 2YTU, 5E8G, 5E8I, 5JVT, 6VG2, 6VG8, 6VGD, 9CP6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.4），有序残基占 39.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR003118, IPR013761, IPR035573; Pfam: PF00178, PF02198 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FBXW7 | 0.995 | 0.051 | — |
| TPP1 | 0.940 | 0.045 | — |
| GATA2 | 0.928 | 0.000 | — |
| RUNX1 | 0.921 | 0.236 | — |
| EWSR1 | 0.912 | 0.292 | — |
| TAL1 | 0.911 | 0.045 | — |
| RUNX2 | 0.849 | 0.840 | — |
| SPI1 | 0.848 | 0.000 | — |
| MYB | 0.844 | 0.000 | — |
| PPT1 | 0.841 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Grip1 | psi-mi:"MI:0096"(pull down) | pubmed:16990252 |
| ilvD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Fmr1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| SIAH1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| CTBP2 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| SOX30 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| Herc2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| SMAD3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| IRF8 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35140242|imex:IM-28767 |
| ERG | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35140242|imex:IM-28767 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.4 + PDB: 1FLI, 1X66, 2YTU, 5E8G, 5E8I,  | pLDDT=63.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nuclear bodies; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FLI1 — Friend leukemia integration 1 transcription factor，研究基础较多，新颖性有限。
2. 蛋白大小452 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1500 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1500 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01543
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151702-FLI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FLI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01543
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000151702-FLI1/subcellular

![](https://images.proteinatlas.org/73099/2178_H9_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/73099/2178_H9_44_blue_red_green.jpg)
![](https://images.proteinatlas.org/73099/1400_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/73099/1400_G6_4_red_green.jpg)
![](https://images.proteinatlas.org/73099/1406_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/73099/1406_G6_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q01543-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q01543 |
| SMART | SM00413;SM00251; |
| UniProt Domain [FT] | DOMAIN 112..198; /note="PNT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00762" |
| InterPro | IPR000418;IPR046328;IPR003118;IPR013761;IPR035573;IPR036388;IPR036390; |
| Pfam | PF00178;PF02198; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000151702-FLI1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ETV6 | Biogrid | false |
| GATA1 | Biogrid | false |
| KAT2B | Biogrid | false |
| KLF1 | Biogrid | false |
| PIAS2 | Biogrid | false |
| PRKCD | Biogrid | false |
| SIAH1 | Intact | false |
| SMAD3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
