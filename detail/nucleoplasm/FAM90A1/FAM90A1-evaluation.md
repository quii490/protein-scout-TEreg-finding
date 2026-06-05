---
type: protein-evaluation
gene: "FAM90A1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM90A1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM90A1 |
| 蛋白名称 | Protein FAM90A1 |
| 蛋白大小 | 464 aa / 49.8 kDa |
| UniProt ID | Q86YD7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 464 aa / 49.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039213, IPR041670; Pfam: PF15288 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Sequencing Analysis Demonstrates That a Complex Genetic Architecture Contributes to Risk for Spina Bifida.. *Birth defects research*. PMID: 41013918
2. Integrated analysis of DNA methylation and mRNA expression profiles to identify key genes involved in the regrowth of clinically non-functioning pituitary adenoma.. *Aging*. PMID: 32015217
3. The effect of host genetics on the gut microbiome.. *Nature genetics*. PMID: 27694959
4. Whole-exome sequencing study of opioid dependence offers novel insights into the contributions of exome variants.. *medRxiv : the preprint server for health sciences*. PMID: 39371181
5. DNA methylation as a predictor of pituitary neuroendocrine tumour behaviour: A systematic review.. *Journal of neuroendocrinology*. PMID: 41866138

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.0 |
| 高置信度残基 (pLDDT>90) 占比 | 3.9% |
| 置信残基 (pLDDT 70-90) 占比 | 6.2% |
| 中等置信 (pLDDT 50-70) 占比 | 21.1% |
| 低置信 (pLDDT<50) 占比 | 68.8% |
| 有序区域 (pLDDT>70) 占比 | 10.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.0），有序残基占 10.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039213, IPR041670; Pfam: PF15288 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RFPL4A | 0.835 | 0.835 | — |
| BRD3 | 0.786 | 0.786 | — |
| ALG1 | 0.767 | 0.000 | — |
| BRD2 | 0.698 | 0.698 | — |
| FAM90A26 | 0.629 | 0.622 | — |
| KDM5B | 0.596 | 0.596 | — |
| MTMR14 | 0.535 | 0.535 | — |
| CLEC4A | 0.518 | 0.000 | — |
| BRD4 | 0.491 | 0.492 | — |
| SUFU | 0.451 | 0.451 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SRPK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| ZNF212 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| FHL3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| EFEMP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MYOG | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CCDC57 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TFIP11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NUDT21 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FXR1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KLHL12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.0 + PDB: 无 | pLDDT=50.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli | 待确认 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM90A1 — Protein FAM90A1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小464 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=50.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86YD7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171847-FAM90A1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM90A1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86YD7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000171847-FAM90A1/subcellular

![](https://images.proteinatlas.org/60078/1431_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/60078/1431_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/60078/1503_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/60078/1503_H6_3_red_green.jpg)
![](https://images.proteinatlas.org/60078/1975_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/60078/1975_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86YD7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
