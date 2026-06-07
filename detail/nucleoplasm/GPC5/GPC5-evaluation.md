---
type: protein-evaluation
gene: "GPC5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPC5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPC5 |
| 蛋白名称 | Glypican-5 |
| 蛋白大小 | 572 aa / 63.7 kDa |
| UniProt ID | P78333 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cell membrane; Secreted, extracellular space |
| 蛋白大小 | 10/10 | ×1 | 10 | 572 aa / 63.7 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=87 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001863, IPR019803; Pfam: PF01153 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cell membrane; Secreted, extracellular space | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- extracellular region (GO:0005576)
- Golgi lumen (GO:0005796)
- lysosomal lumen (GO:0043202)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)
- side of membrane (GO:0098552)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 87 |
| PubMed broad count | 142 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Cell-type brain-region specific changes in prefrontal cortex of a mouse model of alcohol dependence.. *Neurobiology of disease*. PMID: 37992784
2. Intracellular accumulation of amyloid-ß is a marker of selective neuronal vulnerability in Alzheimer's disease.. *Nature communications*. PMID: 40467545
3. GPC5 suppresses lung cancer progression and metastasis via intracellular CTDSP1/AhR/ARNT signaling axis and extracellular exosome secretion.. *Oncogene*. PMID: 34079082
4. Glypican-1, -3, -5 (GPC1, GPC3, GPC5) and Hedgehog Pathway Expression in Oral Squamous Cell Carcinoma.. *Applied immunohistochemistry & molecular morphology : AIMM*. PMID: 33512817
5. The novel lncRNA GPC5-AS1 stabilizes GPC5 mRNA by competitively binding with miR-93/106a to suppress gastric cancer cell proliferation.. *Aging*. PMID: 35183057

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.9 |
| 高置信度残基 (pLDDT>90) 占比 | 59.6% |
| 置信残基 (pLDDT 70-90) 占比 | 10.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 25.0% |
| 有序区域 (pLDDT>70) 占比 | 70.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.9，有序区 70.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001863, IPR019803; Pfam: PF01153 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UNC5D | 0.783 | 0.754 | — |
| SHH | 0.783 | 0.114 | — |
| GPC6 | 0.747 | 0.103 | — |
| WNT3A | 0.691 | 0.143 | — |
| SDC3 | 0.691 | 0.000 | — |
| SDC2 | 0.687 | 0.127 | — |
| HSPG2 | 0.683 | 0.174 | — |
| SDC1 | 0.677 | 0.127 | — |
| APOE | 0.676 | 0.000 | — |
| SLC10A1 | 0.669 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DCPS | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Shcbp1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HSPA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPP2R2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FXYD6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FAM117B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| MAGEC3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| BOD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| RYBP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.9 + PDB: 无 | pLDDT=77.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Secreted, extracellular space / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. GPC5 — Glypican-5，研究基础较多，新颖性有限。
2. 蛋白大小572 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 87 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78333
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179399-GPC5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPC5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78333
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000179399-GPC5/subcellular

![](https://images.proteinatlas.org/44081/1027_F8_8_red_green.jpg)
![](https://images.proteinatlas.org/44081/1027_F8_9_red_green.jpg)
![](https://images.proteinatlas.org/44081/687_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/44081/687_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/44081/783_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/44081/783_E11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P78333-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P78333 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001863;IPR019803; |
| Pfam | PF01153; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000179399-GPC5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BRAF | Intact | false |
| FAM117B | Intact | false |
| HSPG2 | Bioplex | false |
| RYBP | Intact | false |
| SMAD4 | Intact | false |
| SPCS2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
