---
type: protein-evaluation
gene: "THSD7B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## THSD7B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | THSD7B / KIAA1679 |
| 蛋白名称 | Thrombospondin type-1 domain-containing protein 7B |
| 蛋白大小 | 1606 aa / 179.2 kDa |
| UniProt ID | Q9C0I4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1606 aa / 179.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051418, IPR000884, IPR036383, IPR044004, IPR056 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1679 |

**关键文献**:
1. Genomic Landscape of Thrombosis Recurrence Risk Across Venous Thromboembolism Subtypes.. *medRxiv : the preprint server for health sciences*. PMID: 39677447
2. Exercise-augmented THSD7B exhibited a positive prognostic implication and tumor-suppressed functionality in pan-cancer.. *Frontiers in immunology*. PMID: 39161765
3. THSD7B Mutation Induces Platinum Resistance in Small Cell Lung Cancer Patients.. *Drug design, development and therapy*. PMID: 35685767
4. A meta-analysis of two genome-wide association studies identifies 3 new loci for alcohol dependence.. *Journal of psychiatric research*. PMID: 21703634
5. Molecular characterisation of tumours of the lacrimal apparatus.. *Histopathology*. PMID: 37706251

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 54.6% |
| 中等置信 (pLDDT 50-70) 占比 | 31.5% |
| 低置信 (pLDDT<50) 占比 | 13.9% |
| 有序区域 (pLDDT>70) 占比 | 54.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.1），有序残基占 54.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051418, IPR000884, IPR036383, IPR044004, IPR056991; Pfam: PF19030, PF19028, PF23308 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF595 | 0.582 | 0.000 | — |
| SNTG2 | 0.473 | 0.000 | — |
| PGLYRP3 | 0.453 | 0.000 | — |
| PGLYRP4 | 0.452 | 0.000 | — |
| MAP3K19 | 0.441 | 0.000 | — |
| OR5L1 | 0.421 | 0.000 | — |
| KIAA0040 | 0.418 | 0.000 | — |
| CSMD1 | 0.411 | 0.000 | — |
| POFUT2 | 0.401 | 0.000 | — |
| B3GLCT | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RANBP10 | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| HSPD1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H3-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SLC30A8 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| GPR37L1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KIR3DL1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DARS2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PLEKHO1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CISD2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FKBP7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.1 + PDB: 无 | pLDDT=67.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. THSD7B — Thrombospondin type-1 domain-containing protein 7B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1606 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9C0I4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144229-THSD7B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=THSD7B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9C0I4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000144229-THSD7B/subcellular

![](https://images.proteinatlas.org/56745/1433_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/56745/1433_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/56745/1435_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/56745/1435_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/56745/1524_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/56745/1524_F9_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9C0I4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
