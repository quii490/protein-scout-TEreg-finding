---
type: protein-evaluation
gene: "SSX5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SSX5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SSX5 |
| 蛋白名称 | Protein SSX5 |
| 蛋白大小 | 188 aa / 21.7 kDa |
| UniProt ID | O60225 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm, Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 188 aa / 21.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003655, IPR001909, IPR036051, IPR019041; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The cancer-related protein SSX2 interacts with the human homologue of a Ras-like GTPase interactor, RAB3IP, and a novel nuclear protein, SSX2IP.. *Genes, chromosomes & cancer*. PMID: 12007189
2. Expression and immunotherapeutic targeting of the SSX family of cancer-testis antigens in prostate cancer.. *Cancer research*. PMID: 21880588
3. Detection of the SYT-SSX fusion transcripts in formaldehyde-fixed, paraffin-embedded tissue: a reverse transcription polymerase chain reaction amplification assay useful in the diagnosis of synovial sarcoma.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 9688183
4. Heterogeneous expression of the SSX cancer/testis antigens in human melanoma lesions and cell lines.. *Cancer research*. PMID: 10749136
5. SSX cancer testis antigens are expressed in most multiple myeloma patients: co-expression of SSX1, 2, 4, and 5 correlates with adverse prognosis and high frequencies of SSX-positive PCs.. *Journal of immunotherapy (Hagerstown, Md. : 1997)*. PMID: 16224274

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.1 |
| 高置信度残基 (pLDDT>90) 占比 | 25.5% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 45.2% |
| 低置信 (pLDDT<50) 占比 | 21.3% |
| 有序区域 (pLDDT>70) 占比 | 33.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.1），有序残基占 33.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003655, IPR001909, IPR036051, IPR019041; Pfam: PF09514 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SS18 | 0.737 | 0.000 | — |
| ZNF117 | 0.688 | 0.000 | — |
| ZNF83 | 0.687 | 0.000 | — |
| SSX2 | 0.516 | 0.198 | — |
| IGSF22 | 0.511 | 0.000 | — |
| AGTRAP | 0.478 | 0.478 | — |
| MAGEB1 | 0.460 | 0.000 | — |
| MAGEC2 | 0.430 | 0.000 | — |
| CTAG1B | 0.424 | 0.000 | — |
| MAGEA3 | 0.419 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AGTRAP | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| AKAP9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SYP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SSX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CMTM5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLGA6L9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZSCAN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| NFE2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| PCBD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 9
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.1 + PDB: 无 | pLDDT=66.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 14 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SSX5 — Protein SSX5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小188 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60225
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165583-SSX5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SSX5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60225
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000165583-SSX5/subcellular

![](https://images.proteinatlas.org/45683/1397_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1397_A4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1402_A4_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1402_A4_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1440_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1440_H11_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60225-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
