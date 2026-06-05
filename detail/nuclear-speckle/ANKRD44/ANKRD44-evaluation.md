---
type: protein-evaluation
gene: "ANKRD44"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKRD44 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKRD44 |
| 蛋白名称 | Serine/threonine-protein phosphatase 6 regulatory ankyrin repeat subunit B |
| 蛋白大小 | 993 aa / 107.6 kDa |
| UniProt ID | Q8N8A2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nuclear speckles; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 993 aa / 107.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002110, IPR036770; Pfam: PF00023, PF12796, PF13 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nuclear speckles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. ANKRD44 Gene Silencing: A Putative Role in Trastuzumab Resistance in Her2-Like Breast Cancer.. *Frontiers in oncology*. PMID: 31297336
2. Protein phosphatase 6 promotes stemness of colorectal cancer cells.. *Cancer science*. PMID: 39014521
3. Identification of novel pleiotropic gene for bone mineral density and lean mass using the cFDR method.. *Annals of human genetics*. PMID: 34115876
4. Integrating transcriptome-wide association study and mRNA expression profile identified candidate genes related to hand osteoarthritis.. *Arthritis research & therapy*. PMID: 33691763
5. Study on the expression changes of lncRNA in patients with systemic lupus erythematosus and its correlation with Treg cells.. *Clinical rheumatology*. PMID: 38253780

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.6 |
| 高置信度残基 (pLDDT>90) 占比 | 79.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 3.3% |
| 有序区域 (pLDDT>70) 占比 | 92.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.6，有序区 92.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770; Pfam: PF00023, PF12796, PF13637 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP6R1 | 0.964 | 0.844 | — |
| PPP6C | 0.951 | 0.848 | — |
| PPP6R2 | 0.914 | 0.712 | — |
| PPP6R3 | 0.903 | 0.690 | — |
| ANKRD28 | 0.893 | 0.835 | — |
| USP10 | 0.801 | 0.785 | — |
| TRMT2A | 0.565 | 0.534 | — |
| PLK2 | 0.529 | 0.472 | — |
| ZNRF2 | 0.505 | 0.366 | — |
| NOTCH1 | 0.482 | 0.455 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| USP6 | psi-mi:"MI:0018"(two hybrid) | pubmed:16555005 |
| Pag1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:26512138|imex:IM-25616 |
| WWP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PPP6C | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| ANKRD28 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP6R2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDKN2C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NOTCH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NOTCH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.6 + PDB: 无 | pLDDT=90.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Mitochondria; 额外: Nuclear speckles | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ANKRD44 — Serine/threonine-protein phosphatase 6 regulatory ankyrin repeat subunit B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小993 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N8A2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000065413-ANKRD44/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANKRD44
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N8A2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000065413-ANKRD44/subcellular

![](https://images.proteinatlas.org/56549/1050_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/56549/1050_C8_5_red_green.jpg)
![](https://images.proteinatlas.org/56549/911_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/56549/911_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/56549/912_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/56549/912_B8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N8A2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
