---
type: protein-evaluation
gene: "C3orf62"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C3orf62 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C3orf62 |
| 蛋白名称 | Uncharacterized protein C3orf62 |
| 蛋白大小 | 267 aa / 30.2 kDa |
| UniProt ID | Q6ZUJ4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 267 aa / 30.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031670; Pfam: PF15830 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
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
| PubMed strict count | 8 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Brain and blood transcriptome-wide association studies identify five novel genes associated with Alzheimer's disease.. *Journal of Alzheimer's disease : JAD*. PMID: 40111921
2. Pediatric-type Myoid Neoplasms of Somatic Soft Tissue: A Clinicopathological and Molecular Genetic Study of 78 Tumors, Highlighting Indolent Clinical Behavior and Frequent SRF Gene Rearrangements.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 39864664
3. Shared genetic architecture between schizophrenia and gastrointestinal diseases: insights from large-scale genome-wide cross-trait analysis.. *Annals of general psychiatry*. PMID: 41606734
4. Brain and Blood Transcriptome-Wide Association Studies Identify Five Novel Genes Associated with Alzheimer's Disease.. *medRxiv : the preprint server for health sciences*. PMID: 38699333
5. The male pachynema-specific protein MAPS drives phase separation in vitro and regulates sex body formation and chromatin behaviors in vivo.. *Cell reports*. PMID: 38175751

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.9 |
| 高置信度残基 (pLDDT>90) 占比 | 16.5% |
| 置信残基 (pLDDT 70-90) 占比 | 15.0% |
| 中等置信 (pLDDT 50-70) 占比 | 32.6% |
| 低置信 (pLDDT<50) 占比 | 36.0% |
| 有序区域 (pLDDT>70) 占比 | 31.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.9），有序残基占 31.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031670; Pfam: PF15830 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EP300 | 0.620 | 0.594 | — |
| CREBBP | 0.585 | 0.549 | — |
| MRFAP1L1 | 0.533 | 0.533 | — |
| ANKRD65 | 0.479 | 0.000 | — |
| KNCN | 0.477 | 0.000 | — |
| MANSC1 | 0.453 | 0.000 | — |
| ZNF570 | 0.451 | 0.000 | — |
| SUSD6 | 0.446 | 0.000 | — |
| LSMEM1 | 0.445 | 0.000 | — |
| OR52B6 | 0.434 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| mtaD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000341139.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HAUS1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| BFSP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RFPL3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRT3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LMNTD2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MRFAP1L1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| RB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RBL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.9 + PDB: 无 | pLDDT=62.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. C3orf62 — Uncharacterized protein C3orf62，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小267 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZUJ4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188315-C3orf62/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C3orf62
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZUJ4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000188315-C3orf62/subcellular

![](https://images.proteinatlas.org/43328/498_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/43328/498_C1_3_red_green.jpg)
![](https://images.proteinatlas.org/43328/501_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/43328/501_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/43328/512_C1_3_red_green.jpg)
![](https://images.proteinatlas.org/43328/512_C1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZUJ4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
