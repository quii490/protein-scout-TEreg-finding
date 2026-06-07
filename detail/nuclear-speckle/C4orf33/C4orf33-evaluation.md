---
type: protein-evaluation
gene: "C4orf33"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C4orf33 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C4orf33 |
| 蛋白名称 | UPF0462 protein C4orf33 |
| 蛋白大小 | 199 aa / 23.5 kDa |
| UniProt ID | Q8N1A6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 199 aa / 23.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=95.4; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nuclear bodies | Approved |
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
| PubMed strict count | 2 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Associations between Gene-Gene Interaction and Overweight/Obesity of 12-Month-Old Chinese Infants.. *BioMed research international*. PMID: 35295960
2. rs56405341 Variant Associates with Expression of C4orf33 and C4orf33 Was Downregulated in Alzheimer's Disease and Progressive Supranuclear Palsy.. *Journal of Alzheimer's disease : JAD*. PMID: 37742642

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.4 |
| 高置信度残基 (pLDDT>90) 占比 | 94.5% |
| 置信残基 (pLDDT 70-90) 占比 | 2.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 1.0% |
| 有序区域 (pLDDT>70) 占比 | 97.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=95.4，有序区 97.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TAF11 | 0.496 | 0.000 | — |
| SYNRG | 0.495 | 0.000 | — |
| CCDC185 | 0.479 | 0.000 | — |
| VAC14 | 0.477 | 0.477 | — |
| KHDRBS2 | 0.459 | 0.000 | — |
| GPATCH11 | 0.450 | 0.000 | — |
| PCDH10 | 0.428 | 0.000 | — |
| ZFP37 | 0.420 | 0.000 | — |
| BTAF1 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VAC14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| TRIP13 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| SH3GLB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| LAMP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CASP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ECE1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-30316|pubmed:38413612| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 6
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.4 + PDB: 无 | pLDDT=95.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus; 额外: Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 9 + 6 interactions | 数据充分 |

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
1. C4orf33 — UPF0462 protein C4orf33，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小199 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N1A6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151470-C4orf33/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C4orf33
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N1A6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000151470-C4orf33/subcellular

![](https://images.proteinatlas.org/61199/1118_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61199/1118_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61199/1153_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61199/1153_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61199/1171_F3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61199/1171_F3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N1A6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N1A6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | 未检出 |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000151470-C4orf33/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| VAC14 | Intact, Biogrid | true |
| CASP6 | Intact | false |
| SH3GLB1 | Intact | false |
| TRIP13 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
