---
type: protein-evaluation
gene: "DBNDD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DBNDD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DBNDD1 |
| 蛋白名称 | Dysbindin domain-containing protein 1 |
| 蛋白大小 | 158 aa / 17.0 kDa |
| UniProt ID | Q9H9R9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nuclear speckles; 额外: Cytosol, Equatorial segment, Mid piece; UniProt: 无注释 |
| 蛋白大小 | 8/10 | x1 | 8 | 158 aa / 17.0 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=60.8; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR007531; Pfam: PF04440 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol, Equatorial segment, Mid piece, Principal piece, End piece | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 11 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Backbone and side chain resonance assignment of the intrinsically disordered human DBNDD1 protein.. *Biomolecular NMR assignments*. PMID: 35474152
2. Gene Expression-Based Colorectal Cancer Prediction Using Machine Learning and SHAP Analysis.. *Genes*. PMID: 41595533
3. Functional annotation of melanoma risk loci identifies novel susceptibility genes.. *Carcinogenesis*. PMID: 31630191
4. Association of DBNDD1 with prognostic and immune biomarkers in invasive breast cancer.. *Discover oncology*. PMID: 39979699
5. Synergistic DBNDD1-GDF15 Signaling Activates the NF-κB Pathway to Promote Colorectal Cancer Progression.. *Molecular cancer research : MCR*. PMID: 41182793

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.8 |
| 高置信度残基 (pLDDT>90) 占比 | 3.2% |
| 置信残基 (pLDDT 70-90) 占比 | 27.2% |
| 中等置信 (pLDDT 50-70) 占比 | 41.1% |
| 低置信 (pLDDT<50) 占比 | 28.5% |
| 有序区域 (pLDDT>70) 占比 | 30.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.8），有序残基占 30.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007531; Pfam: PF04440 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DEF8 | 0.675 | 0.000 | — |
| DTNB | 0.600 | 0.000 | — |
| SPATA33 | 0.560 | 0.000 | — |
| SPIRE2 | 0.540 | 0.000 | — |
| VPS9D1 | 0.512 | 0.000 | — |
| FANCA | 0.509 | 0.000 | — |
| DBNDD2 | 0.504 | 0.000 | — |
| CSNK1D | 0.497 | 0.497 | — |
| CDK10 | 0.493 | 0.000 | — |
| SPATA2L | 0.489 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.8 + PDB: 无 | pLDDT=60.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles; 额外: Cytosol, Equatorial segment, | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DBNDD1 -- Dysbindin domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小158 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H9R9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000003249-DBNDD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DBNDD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H9R9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000003249-DBNDD1/subcellular

![](https://images.proteinatlas.org/43018/2191_F7_40_red_green.jpg)
![](https://images.proteinatlas.org/43018/2191_F7_54_red_green.jpg)
![](https://images.proteinatlas.org/43018/468_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/43018/468_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/43018/470_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/43018/470_F9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H9R9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
