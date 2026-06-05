---
type: protein-evaluation
gene: "SHISA6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHISA6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SHISA6 |
| 蛋白名称 | Protein shisa-6 |
| 蛋白大小 | 500 aa / 55.8 kDa |
| UniProt ID | Q6ZSJ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane; UniProt: Membrane; Postsynaptic density |
| 蛋白大小 | 10/10 | ×1 | 10 | 500 aa / 55.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026910, IPR053891; Pfam: PF13908 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Approved |
| UniProt | Membrane; Postsynaptic density | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- AMPA glutamate receptor complex (GO:0032281)
- asymmetric, glutamatergic, excitatory synapse (GO:0098985)
- dendritic spine membrane (GO:0032591)
- postsynaptic density (GO:0014069)
- postsynaptic density membrane (GO:0098839)
- postsynaptic membrane (GO:0045211)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Epigenetic and Tumor Microenvironment for Prognosis of Patients with Gastric Cancer.. *Biomolecules*. PMID: 37238607
2. Expression Profiling of Coding and Noncoding RNAs in the Endometrium of Patients with Endometriosis.. *International journal of molecular sciences*. PMID: 39408909
3. AMPAR Auxiliary Protein SHISA6 Facilitates Purkinje Cell Synaptic Excitability and Procedural Memory Formation.. *Cell reports*. PMID: 32294428
4. Shisa6 mediates cell-type specific regulation of depression in the nucleus accumbens.. *Molecular psychiatry*. PMID: 34253865
5. Genetic variants in the SHISA6 gene are associated with delayed cognitive impairment in two family datasets.. *Alzheimer's & dementia : the journal of the Alzheimer's Association*. PMID: 35490390

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.4 |
| 高置信度残基 (pLDDT>90) 占比 | 12.2% |
| 置信残基 (pLDDT 70-90) 占比 | 9.0% |
| 中等置信 (pLDDT 50-70) 占比 | 20.4% |
| 低置信 (pLDDT<50) 占比 | 58.4% |
| 有序区域 (pLDDT>70) 占比 | 21.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.4），有序残基占 21.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026910, IPR053891; Pfam: PF13908 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DLG4 | 0.801 | 0.000 | — |
| CNIH2 | 0.749 | 0.000 | — |
| CACNG8 | 0.739 | 0.000 | — |
| CACNG3 | 0.720 | 0.000 | — |
| CACNG2 | 0.700 | 0.000 | — |
| GRIN2B | 0.694 | 0.000 | — |
| GRIA2 | 0.688 | 0.087 | — |
| GRIA1 | 0.682 | 0.066 | — |
| GRIN3A | 0.667 | 0.000 | — |
| SHISA7 | 0.647 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLEKHG4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSSK3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KIF9 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ARMC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FBLIM1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CCDC57 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CARD9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBASH3A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TLE5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| OIP5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.4 + PDB: 无 | pLDDT=55.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Postsynaptic density / Nucleoplasm, Plasma membrane | 一致 |
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
1. SHISA6 — Protein shisa-6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小500 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZSJ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188803-SHISA6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SHISA6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZSJ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000188803-SHISA6/subcellular

![](https://images.proteinatlas.org/23440/192_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23440/192_E10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23440/193_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23440/193_E10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23440/1971_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23440/1971_B8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZSJ9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
