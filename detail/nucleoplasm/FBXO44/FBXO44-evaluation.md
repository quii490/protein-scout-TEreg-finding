---
type: protein-evaluation
gene: "FBXO44"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO44 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO44 / FBG3, FBX30, FBX44, FBX6A, FBXO6A |
| 蛋白名称 | F-box only protein 44 |
| 蛋白大小 | 255 aa / 29.7 kDa |
| UniProt ID | Q9H4M3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 255 aa / 29.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=92.4; PDB: 3WSO, 5B4N |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007397, IPR036047, IPR001810, IPR039752, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBG3, FBX30, FBX44, FBX6A, FBXO6A |

**关键文献**:
1. Integrative proteomic characterization of adenocarcinoma of esophagogastric junction.. *Nature communications*. PMID: 36774361
2. FBXO44 promotes DNA replication-coupled repetitive element silencing in cancer cells.. *Cell*. PMID: 33357448
3. FBXO44 Regulates FOXP1 Degradation Through AURKA-Dependent Phosphorylation to Promote Colorectal Cancer Progression.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 41051444
4. Role for the F-box proteins in heart diseases.. *Pharmacological research*. PMID: 39577754
5. The F-box protein FBXO44 mediates BRCA1 ubiquitination and degradation.. *The Journal of biological chemistry*. PMID: 23086937

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.4 |
| 高置信度残基 (pLDDT>90) 占比 | 80.8% |
| 置信残基 (pLDDT 70-90) 占比 | 14.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 94.9% |
| 可用 PDB 条目 | 3WSO, 5B4N |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3WSO, 5B4N）+ AlphaFold高质量预测（pLDDT=92.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007397, IPR036047, IPR001810, IPR039752, IPR008979; Pfam: PF12937, PF04300 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.991 | 0.928 | — |
| CUL1 | 0.962 | 0.841 | — |
| CUL4B | 0.895 | 0.510 | — |
| DDB1 | 0.865 | 0.510 | — |
| RBX1 | 0.769 | 0.512 | — |
| RGS2 | 0.703 | 0.510 | — |
| MAD2L2 | 0.687 | 0.000 | — |
| FBXO17 | 0.623 | 0.000 | — |
| FBXO27 | 0.595 | 0.000 | — |
| CUL2 | 0.562 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SKP1 | psi-mi:"MI:0231"(mammalian protein protein interac | pubmed:19159283|imex:IM-20301 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DDX21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SPG21 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KCNJ5-AS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BLOC1S1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BORCS6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.4 + PDB: 3WSO, 5B4N | pLDDT=92.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBXO44 — F-box only protein 44，非常新颖，仅有少数基础研究。
2. 蛋白大小255 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H4M3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132879-FBXO44/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO44
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H4M3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000132879-FBXO44/subcellular

![](https://images.proteinatlas.org/3363/77_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/3363/77_B7_2_red_green.jpg)
![](https://images.proteinatlas.org/3363/78_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/3363/78_B7_2_red_green.jpg)
![](https://images.proteinatlas.org/3363/92_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/3363/92_B7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H4M3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H4M3 |
| SMART | SM01198;SM00256; |
| UniProt Domain [FT] | DOMAIN 3..50; /note="F-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00080"; DOMAIN 71..252; /note="FBA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00482" |
| InterPro | IPR007397;IPR036047;IPR001810;IPR039752;IPR008979; |
| Pfam | PF12937;PF04300; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132879-FBXO44/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SKP1 | Intact, Biogrid | true |
| BORCS6 | Intact | false |
| BRCA1 | Biogrid | false |
| COPS6 | Biogrid | false |
| CUL1 | Biogrid | false |
| CUL4B | Biogrid | false |
| DDB1 | Biogrid | false |
| RBX1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
