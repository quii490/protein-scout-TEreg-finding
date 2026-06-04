---
type: protein-evaluation
gene: "INPP5J"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## INPP5J 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | INPP5J / PIB5PA, PIPP |
| 蛋白名称 | Phosphatidylinositol 4,5-bisphosphate 5-phosphatase A |
| 蛋白大小 | 1006 aa / 107.2 kDa |
| UniProt ID | Q15735 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoli fibrillar center; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1006 aa / 107.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036691, IPR046985, IPR000300, IPR041611; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli fibrillar center | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendritic shaft (GO:0043198)
- growth cone (GO:0030426)
- neuron projection (GO:0043005)
- plasma membrane (GO:0005886)
- ruffle (GO:0001726)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PIB5PA, PIPP |

**关键文献**:
1. PELI1 overexpression contributes to pancreatic cancer progression through upregulating ubiquitination-mediated INPP5J degradation.. *Cellular signalling*. PMID: 38685520
2. Alterations in Blood and Hippocampal mRNA and miRNA Expression, Along with Fat Deposition in Female B6C3F1 Mice Continuously Exposed to Prenatal Low-Dose-Rate Radiation and Their Comparison with Male Mice.. *Cells*. PMID: 39936965
3. Identification of potential tumor antigens and immune subtypes for lung adenocarcinoma.. *Medical oncology (Northwood, London, England)*. PMID: 36809467
4. MiR-661 contributed to cell proliferation of human ovarian cancer cells by repressing INPP5J expression.. *Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*. PMID: 26282217
5. Phosphoinositide 5-phosphatase activities control cell motility in glioblastoma: Two phosphoinositides PI(4,5)P2 and PI(3,4)P2 are involved.. *Advances in biological regulation*. PMID: 28916189

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.3 |
| 高置信度残基 (pLDDT>90) 占比 | 33.4% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 58.9% |
| 有序区域 (pLDDT>70) 占比 | 38.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=59.3），有序残基占 38.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036691, IPR046985, IPR000300, IPR041611; Pfam: PF22669, PF17751 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| INPP5A | 0.991 | 0.000 | — |
| INPP1 | 0.958 | 0.000 | — |
| ITPK1 | 0.942 | 0.000 | — |
| ITPKB | 0.937 | 0.000 | — |
| IPMK | 0.932 | 0.000 | — |
| ITPKA | 0.927 | 0.000 | — |
| ITPKC | 0.919 | 0.000 | — |
| MINPP1 | 0.919 | 0.000 | — |
| INPP5K | 0.907 | 0.000 | — |
| PLCE1 | 0.744 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EFHC2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HSF2BP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PSME3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MEOX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PRKAR1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FXR2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PICK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRIM54 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PELI1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLGA2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.3 + PDB: 无 | pLDDT=59.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. INPP5J — Phosphatidylinositol 4,5-bisphosphate 5-phosphatase A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1006 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15735
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185133-INPP5J/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=INPP5J
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15735
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
