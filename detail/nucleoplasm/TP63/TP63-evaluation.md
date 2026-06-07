---
type: protein-evaluation
gene: "TP63"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TP63 — REJECTED (研究热度过高 (PubMed strict=693，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TP63 / KET, P63, P73H, P73L, TP73L |
| 蛋白名称 | Tumor protein 63 |
| 蛋白大小 | 680 aa / 76.8 kDa |
| UniProt ID | Q9H3D4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 680 aa / 76.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=693 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 1RG6, 2NB1, 2RMN, 2Y9T, 2Y9U, 3QYM, 3QYN |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008967, IPR012346, IPR057064, IPR011615, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 693 |
| PubMed broad count | 2519 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KET, P63, P73H, P73L, TP73L |

**关键文献**:
1. Ectodermal dysplasias: Classification and organization by phenotype, genotype and molecular pathway.. *American journal of medical genetics. Part A*. PMID: 30703280
2. TP63-Related Disorders.. **. PMID: 20556892
3. Wnt-deficient and hypoxic environment orchestrates squamous reprogramming of human pancreatic ductal adenocarcinoma.. *Nature cell biology*. PMID: 39232216
4. Proteogenomic Analysis of Salivary Adenoid Cystic Carcinomas Defines Molecular Subtypes and Identifies Therapeutic Targets.. *Clinical cancer research : an official journal of the American Association for Cancer Research*. PMID: 33172898
5. Dysregulation of MYBL2 impairs extravillous trophoblast lineage development and function, contributing to recurrent spontaneous abortion.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40294258

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 34.6% |
| 置信残基 (pLDDT 70-90) 占比 | 14.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 43.2% |
| 有序区域 (pLDDT>70) 占比 | 48.9% |
| 可用 PDB 条目 | 1RG6, 2NB1, 2RMN, 2Y9T, 2Y9U, 3QYM, 3QYN, 3US0, 3US1, 3US2 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 48.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR012346, IPR057064, IPR011615, IPR036674; Pfam: PF00870, PF07710, PF07647 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TP73 | 0.997 | 0.977 | — |
| TP53 | 0.953 | 0.819 | — |
| SOX2 | 0.930 | 0.166 | — |
| PERP | 0.930 | 0.076 | — |
| MDM2 | 0.900 | 0.759 | — |
| CSNK1D | 0.900 | 0.900 | — |
| GABPB1 | 0.900 | 0.900 | — |
| ITCH | 0.894 | 0.837 | — |
| KRT5 | 0.861 | 0.292 | — |
| EP300 | 0.850 | 0.792 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000110965.3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:21335238|imex:IM-16609 |
| ENSMUSP00000110963.3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:21335238|imex:IM-16609 |
| ENSMUSP00000038117.7 | psi-mi:"MI:0071"(molecular sieving) | pubmed:21335238|imex:IM-16609 |
| ENSP00000264731.3 | psi-mi:"MI:0077"(nuclear magnetic resonance) | pubmed:21335238|imex:IM-16609 |
| NIPSNAP3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| ORM1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| COPS6 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CCNC | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| GCGR | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| HP | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 1RG6, 2NB1, 2RMN, 2Y9T, 2Y9U,  | pLDDT=63.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. TP63 — Tumor protein 63，研究基础较多，新颖性有限。
2. 蛋白大小680 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 693 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 693 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H3D4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000073282-TP63/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TP63
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H3D4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000073282-TP63/subcellular

![](https://images.proteinatlas.org/6289/1843_E1_11_cr5af96f44b4a7b_red_green.jpg)
![](https://images.proteinatlas.org/6289/1843_E1_9_cr5af96f44b42f8_red_green.jpg)
![](https://images.proteinatlas.org/6289/1868_D2_31_red_green.jpg)
![](https://images.proteinatlas.org/6289/1868_D2_32_red_green.jpg)
![](https://images.proteinatlas.org/6289/1941_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/6289/1941_G1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H3D4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H3D4 |
| SMART | SM00454; |
| UniProt Domain [FT] | DOMAIN 541..607; /note="SAM" |
| InterPro | IPR008967;IPR012346;IPR057064;IPR011615;IPR036674;IPR010991;IPR002117;IPR001660;IPR013761;IPR037611; |
| Pfam | PF00870;PF07710;PF07647; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000073282-TP63/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HNRNPAB | Intact, Biogrid | true |
| ITCH | Intact, Biogrid | true |
| NIPSNAP3A | Intact, Biogrid | true |
| SATB2 | Intact, Biogrid | true |
| TP53 | Intact, Biogrid | true |
| TP73 | Intact, Biogrid | true |
| YAP1 | Intact, Biogrid | true |
| ANAPC2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
