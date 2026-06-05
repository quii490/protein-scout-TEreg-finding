---
type: protein-evaluation
gene: "GARNL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GARNL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GARNL3 |
| 蛋白名称 | GTPase-activating Rap/Ran-GAP domain-like protein 3 |
| 蛋白大小 | 1013 aa / 112.9 kDa |
| UniProt ID | Q5VVW2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 1013 aa / 112.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001180, IPR035974, IPR000331, IPR050989; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
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
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. GARNL3 identified as a crucial target for overcoming temozolomide resistance in EGFRvIII-positive glioblastoma.. *American journal of translational research*. PMID: 38883343
2. Identification of key modules and hub genes in glioblastoma multiforme based on co-expression network analysis.. *FEBS open bio*. PMID: 33423377
3. Microdeletions in 9q33.3-q34.11 in five patients with intellectual disability, microcephaly, and seizures of incomplete penetrance: is STXBP1 not the only causative gene?. *Molecular cytogenetics*. PMID: 26421060
4. Immune Landscape and Prognostic Significance of Gene Expression Profiles in Bladder Cancer: Insights from Immune Cell Infiltration and Risk Modeling.. *Iranian journal of allergy, asthma, and immunology*. PMID: 40696737
5. Expression of New Gene Markers Regulating Protein Metabolism in Porcine Ovarian Granulosa Cells In Vitro.. *International journal of molecular sciences*. PMID: 41465369

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.1 |
| 高置信度残基 (pLDDT>90) 占比 | 37.8% |
| 置信残基 (pLDDT 70-90) 占比 | 27.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.1% |
| 低置信 (pLDDT<50) 占比 | 24.3% |
| 有序区域 (pLDDT>70) 占比 | 65.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.1，有序区 65.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001180, IPR035974, IPR000331, IPR050989; Pfam: PF00780, PF02145 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| INPP5A | 0.623 | 0.000 | — |
| RALGPS1 | 0.608 | 0.000 | — |
| CARNMT1 | 0.537 | 0.000 | — |
| RGS8 | 0.521 | 0.000 | — |
| PCP4 | 0.503 | 0.000 | — |
| TBRG1 | 0.493 | 0.000 | — |
| HOMER3 | 0.481 | 0.000 | — |
| GRID2 | 0.469 | 0.000 | — |
| GRAMD1B | 0.462 | 0.000 | — |
| EI24 | 0.443 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLC16A1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ENST00000373387 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 2
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.1 + PDB: 无 | pLDDT=73.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Vesicles; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 13 + 2 interactions | 数据充分 |

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
1. GARNL3 — GTPase-activating Rap/Ran-GAP domain-like protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1013 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VVW2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136895-GARNL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GARNL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VVW2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000136895-GARNL3/subcellular

![](https://images.proteinatlas.org/28757/1836_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28757/1836_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28757/301_F2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28757/301_F2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28757/342_F2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28757/342_F2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VVW2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
