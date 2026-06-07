---
type: protein-evaluation
gene: "FBXO7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXO7 — REJECTED (研究热度过高 (PubMed strict=132，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO7 / FBX7 |
| 蛋白名称 | F-box only protein 7 |
| 蛋白大小 | 522 aa / 58.5 kDa |
| UniProt ID | Q9Y3I1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus; Mitochondrion; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 522 aa / 58.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=132 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.4; PDB: 4L9C, 4L9H |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR047118, IPR021625, IPR029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Mitochondrion; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- classical Lewy body (GO:0097414)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- glial cytoplasmic inclusion (GO:0097409)
- Lewy body core (GO:1990037)
- Lewy body corona (GO:1990038)
- Lewy neurite (GO:0097462)
- mitochondrion (GO:0005739)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 132 |
| PubMed broad count | 182 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX7 |

**关键文献**:
1. Monogenic Parkinson's Disease: Genotype, Phenotype, Pathophysiology, and Genetic Testing.. *Genes*. PMID: 35328025
2. Mitochondrial Tumor Suppressor 1A Attenuates Myocardial Infarction Injury by Maintaining the Coupling Between Mitochondria and Endoplasmic Reticulum.. *Circulation*. PMID: 40583767
3. FBXO7 ubiquitinates PRMT1 to suppress serine synthesis and tumor growth in hepatocellular carcinoma.. *Nature communications*. PMID: 38839752
4. New insights into the role of mitochondrial metabolic dysregulation and immune infiltration in septic cardiomyopathy by integrated bioinformatics analysis and experimental validation.. *Cellular & molecular biology letters*. PMID: 38291374
5. The role of genetics in Parkinson's disease: a large cohort study in Chinese mainland population.. *Brain : a journal of neurology*. PMID: 32613234

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.4 |
| 高置信度残基 (pLDDT>90) 占比 | 12.8% |
| 置信残基 (pLDDT 70-90) 占比 | 41.4% |
| 中等置信 (pLDDT 50-70) 占比 | 12.5% |
| 低置信 (pLDDT<50) 占比 | 33.3% |
| 有序区域 (pLDDT>70) 占比 | 54.2% |
| 可用 PDB 条目 | 4L9C, 4L9H |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.4），有序残基占 54.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR047118, IPR021625, IPR029071; Pfam: PF12937, PF11566 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.997 | 0.927 | — |
| PINK1 | 0.995 | 0.510 | — |
| CUL1 | 0.992 | 0.916 | — |
| PSMF1 | 0.976 | 0.884 | — |
| RBX1 | 0.965 | 0.839 | — |
| PRKN | 0.917 | 0.331 | — |
| PLA2G6 | 0.897 | 0.000 | — |
| GIGYF2 | 0.886 | 0.126 | — |
| ATP13A2 | 0.885 | 0.000 | — |
| PARK7 | 0.864 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16278047 |
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16278047 |
| SEC24C | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| glpA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| RBBP6 | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PSMF1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PSMB9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.4 + PDB: 4L9C, 4L9H | pLDDT=66.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Mitochondrion; Cytoplasm, cyto / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FBXO7 — F-box only protein 7，研究基础较多，新颖性有限。
2. 蛋白大小522 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 132 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 132 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3I1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100225-FBXO7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3I1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000100225-FBXO7/subcellular

![](https://images.proteinatlas.org/32113/1004_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/32113/1004_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/32113/1182_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/32113/1182_B5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y3I1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y3I1 |
| SMART | SM00256; |
| UniProt Domain [FT] | DOMAIN 329..375; /note="F-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00080" |
| InterPro | IPR036047;IPR001810;IPR047118;IPR021625;IPR029071; |
| Pfam | PF12937;PF11566; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100225-FBXO7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| COPS6 | Biogrid, Bioplex | true |
| CUL1 | Biogrid, Bioplex | true |
| PINK1 | Intact, Biogrid | true |
| PRKN | Intact, Biogrid | true |
| PSMA2 | Biogrid, Bioplex | true |
| PSMA3 | Intact, Biogrid | true |
| PSMA5 | Biogrid, Bioplex | true |
| PSMB2 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
