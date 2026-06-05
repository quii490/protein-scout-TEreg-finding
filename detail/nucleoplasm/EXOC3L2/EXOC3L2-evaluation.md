---
type: protein-evaluation
gene: "EXOC3L2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EXOC3L2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOC3L2 / XTP7 |
| 蛋白名称 | Exocyst complex component 3-like protein 2 |
| 蛋白大小 | 802 aa / 87.5 kDa |
| UniProt ID | Q2M3D2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus, Vesicles; 额外: Nucleoplasm, Nucleoli, Mid pi; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 802 aa / 87.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010326, IPR042532; Pfam: PF06046 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles; 额外: Nucleoplasm, Nucleoli, Mid piece | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- exocyst (GO:0000145)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: XTP7 |

**关键文献**:
1. Characterizing the morbid genome of ciliopathies.. *Genome biology*. PMID: 27894351
2. Association between EXOC3L2 rs597668 polymorphism and Alzheimer's disease.. *CNS neuroscience & therapeutics*. PMID: 23663385
3. Biallelic mutations in EXOC3L2 cause a novel syndrome that affects the brain, kidney and blood.. *Journal of medical genetics*. PMID: 30327448
4. Polygenic Analysis of Late-Onset Alzheimer's Disease from Mainland China.. *PloS one*. PMID: 26680604
5. Gene-based aggregate SNP associations between candidate AD genes and cognitive decline.. *Age (Dordrecht, Netherlands)*. PMID: 27005436

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.5 |
| 高置信度残基 (pLDDT>90) 占比 | 38.5% |
| 置信残基 (pLDDT 70-90) 占比 | 27.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 27.8% |
| 有序区域 (pLDDT>70) 占比 | 65.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.5，有序区 65.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010326, IPR042532; Pfam: PF06046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOC4 | 0.951 | 0.720 | — |
| EXOC7 | 0.868 | 0.587 | — |
| EXOC2 | 0.864 | 0.619 | — |
| EXOC5 | 0.847 | 0.475 | — |
| EXOC8 | 0.847 | 0.594 | — |
| EXOC1 | 0.832 | 0.585 | — |
| EXOC6 | 0.818 | 0.469 | — |
| EXOC1L | 0.794 | 0.491 | — |
| EXOC6B | 0.785 | 0.469 | — |
| EXOC3L1 | 0.726 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BIK | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MRPL12 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GPR148 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TNFSF18 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIAH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MIPEP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENSP00000400713.2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ATG16L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31015422|imex:IM-29997 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.5 + PDB: 无 | pLDDT=73.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus, Vesicles; 额外: Nucleoplasm, Nucleo | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EXOC3L2 — Exocyst complex component 3-like protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小802 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2M3D2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000283632-EXOC3L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOC3L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2M3D2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000283632-EXOC3L2/subcellular

![](https://images.proteinatlas.org/41595/1849_A3_24_cr5afc1e8db1419_blue_red_green.jpg)
![](https://images.proteinatlas.org/41595/1849_A3_28_cr5afc1e8db31b5_blue_red_green.jpg)
![](https://images.proteinatlas.org/41595/2186_F5_30_blue_red_green.jpg)
![](https://images.proteinatlas.org/41595/2186_F5_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/41595/2229_F8_18_blue_red_green.jpg)
![](https://images.proteinatlas.org/41595/2229_F8_43_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q2M3D2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
