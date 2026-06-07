---
type: protein-evaluation
gene: "PTTG1IP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PTTG1IP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PTTG1IP / C21orf1, C21orf3 |
| 蛋白名称 | Pituitary tumor-transforming gene 1 protein-interacting protein |
| 蛋白大小 | 180 aa / 20.3 kDa |
| UniProt ID | P53801 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Membrane; Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 180 aa / 20.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016201, IPR052304 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Membrane; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 68 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C21orf1, C21orf3 |

**关键文献**:
1. Sp4 Regulates PTTG1IP Gene Transcription and Expression.. *DNA and cell biology*. PMID: 36383136
2. PTTG1IP Orchestrates Epithelial-Mesenchymal Transition and DNA Damage Response in Thyroid Cancer Progression.. *Frontiers in bioscience (Landmark edition)*. PMID: 41074439
3. PTTG1-interacting protein (PTTG1IP/PBF) predicts breast cancer survival.. *BMC cancer*. PMID: 29078751
4. Gene Expression Pattern of ESPL1, PTTG1 and PTTG1IP Can Potentially Predict Response to TKI First-Line Treatment of Patients with Newly Diagnosed CML.. *Cancers*. PMID: 37174118
5. Super-Enhancer LncRNA LINC00162 Promotes Progression of Bladder Cancer.. *iScience*. PMID: 33344916

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.2 |
| 高置信度残基 (pLDDT>90) 占比 | 30.6% |
| 置信残基 (pLDDT 70-90) 占比 | 33.9% |
| 中等置信 (pLDDT 50-70) 占比 | 30.6% |
| 低置信 (pLDDT<50) 占比 | 5.0% |
| 有序区域 (pLDDT>70) 占比 | 64.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.2，有序区 64.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016201, IPR052304 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PTTG1 | 0.893 | 0.292 | — |
| JAM2 | 0.691 | 0.000 | — |
| SYNJ1 | 0.678 | 0.000 | — |
| TP53 | 0.661 | 0.593 | — |
| PKNOX1 | 0.641 | 0.000 | — |
| STX7 | 0.629 | 0.616 | — |
| NDUFV3 | 0.619 | 0.000 | — |
| ADAMTS1 | 0.595 | 0.000 | — |
| WDR4 | 0.550 | 0.000 | — |
| RCAN1 | 0.548 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257125 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:19463016|imex:IM-17246 |
| RAB4A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SLC22A23 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TNFSF14 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AMIGO1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM106C | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMPRSS2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SGCB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ATP6AP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| STX7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.2 + PDB: 无 | pLDDT=77.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PTTG1IP — Pituitary tumor-transforming gene 1 protein-interacting protein，非常新颖，仅有少数基础研究。
2. 蛋白大小180 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P53801
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183255-PTTG1IP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTTG1IP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P53801
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000183255-PTTG1IP/subcellular

![](https://images.proteinatlas.org/61827/1241_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/61827/1241_H6_5_red_green.jpg)
![](https://images.proteinatlas.org/61827/1245_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/61827/1245_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/61827/1261_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/61827/1261_A10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P53801-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P53801 |
| SMART | SM00423; |
| UniProt Domain [FT] | DOMAIN 39..92; /note="PSI" |
| InterPro | IPR016201;IPR052304; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183255-PTTG1IP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AMIGO1 | Intact | false |
| ATP6AP2 | Intact | false |
| CANX | Opencell | false |
| CLEC7A | Intact | false |
| CRYAA | Intact | false |
| KLK6 | Intact | false |
| LAMP1 | Opencell | false |
| LDLRAD1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
