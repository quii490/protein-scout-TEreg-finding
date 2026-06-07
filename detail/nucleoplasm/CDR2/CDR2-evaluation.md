---
type: protein-evaluation
gene: "CDR2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CDR2 — REJECTED (研究热度过高 (PubMed strict=534，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDR2 / PCD17 |
| 蛋白名称 | Cerebellar degeneration-related protein 2 |
| 蛋白大小 | 454 aa / 51.9 kDa |
| UniProt ID | Q01850 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 454 aa / 51.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=534 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026079 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **71.5/180** | |
| **归一化总分** | | | **39.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 534 |
| PubMed broad count | 1141 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PCD17 |

**关键文献**:
1. Molecular Mechanisms Associated with Antifungal Resistance in Pathogenic Candida Species.. *Cells*. PMID: 37998390
2. Developing drug-like single-domain antibodies (VHH) from in vitro libraries.. *mAbs*. PMID: 40562779
3. CDR2 is a dynein adaptor recruited by kinectin to regulate ER sheet organization.. *The Journal of cell biology*. PMID: 40637585
4. CDR2 and CDR2L line blot performance in PCA-1/anti-Yo paraneoplastic autoimmunity.. *Frontiers in immunology*. PMID: 37841252
5. Roles of CDR2 and CDR2L in Anti-Yo Paraneoplastic Cerebellar Degeneration: A Literature Review.. *International journal of molecular sciences*. PMID: 39795928

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.1 |
| 高置信度残基 (pLDDT>90) 占比 | 47.4% |
| 置信残基 (pLDDT 70-90) 占比 | 11.5% |
| 中等置信 (pLDDT 50-70) 占比 | 17.2% |
| 低置信 (pLDDT<50) 占比 | 24.0% |
| 有序区域 (pLDDT>70) 占比 | 58.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.1，有序区 58.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026079 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDR1 | 0.999 | 0.000 | — |
| MYC | 0.872 | 0.516 | — |
| CDR2L | 0.797 | 0.780 | — |
| BRSK1 | 0.778 | 0.000 | — |
| ITIH4 | 0.771 | 0.000 | — |
| WEE1 | 0.719 | 0.000 | — |
| LOC102723407 | 0.715 | 0.000 | — |
| KTN1 | 0.704 | 0.704 | — |
| C4orf46 | 0.686 | 0.686 | — |
| DUSP5 | 0.671 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| pom1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:21703453|imex:IM-16561 |
| MORF4L2 | psi-mi:"MI:0018"(two hybrid) | pubmed:11988016|imex:IM-19508 |
| ENSP00000268383.2 | psi-mi:"MI:0018"(two hybrid) | pubmed:11988016|imex:IM-19508 |
| ASS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11988016|imex:IM-19508 |
| GMPPA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SSX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCHCR1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| TBC1D22B | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| TXLNA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TCHP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.1 + PDB: 无 | pLDDT=74.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CDR2 — Cerebellar degeneration-related protein 2，研究基础较多，新颖性有限。
2. 蛋白大小454 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 534 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 534 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01850
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140743-CDR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01850
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000140743-CDR2/subcellular

![](https://images.proteinatlas.org/23870/224_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/23870/224_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/23870/226_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/23870/226_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/23870/261_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/23870/261_B3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q01850-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q01850 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026079; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140743-CDR2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C4orf46 | Intact, Biogrid, Bioplex | true |
| CDR2L | Intact, Biogrid, Bioplex | true |
| HGS | Intact, Biogrid | true |
| KTN1 | Intact, Biogrid | true |
| MORF4L2 | Intact, Biogrid | true |
| PKN1 | Intact, Biogrid | true |
| UQCC2 | Intact, Biogrid | true |
| YWHAB | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
