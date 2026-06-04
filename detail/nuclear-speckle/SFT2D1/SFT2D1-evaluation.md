---
type: protein-evaluation
gene: "SFT2D1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SFT2D1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SFT2D1 / C6orf83 |
| 蛋白名称 | Vesicle transport protein SFT2A |
| 蛋白大小 | 159 aa / 17.8 kDa |
| UniProt ID | Q8WV19 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; 额外: Nucleoplasm, Cytosol; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 159 aa / 17.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007305, IPR011691; Pfam: PF04178 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endomembrane system (GO:0012505)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf83 |

**关键文献**:
1. Unraveling the role of histone acetylation in sepsis biomarker discovery.. *Frontiers in molecular biosciences*. PMID: 40370519
2. A Transcriptome-Wide Association Study Identifies Candidate Susceptibility Genes for Pancreatic Cancer Risk.. *Cancer research*. PMID: 32907841
3. Biomarker identification for rheumatoid arthritis with inadequate response to DMARD and TNF therapies using multidimensional analyses.. *Immunobiology*. PMID: 40288069
4. Identification of a minimal region of loss on chromosome 6q27 associated with poor survival of high-risk neuroblastoma patients.. *Cancer biology & therapy*. PMID: 31959052
5. Identification of a new gene signature for prognostic evaluation in cervical cancer: based on cuproptosis-associated angiogenesis and multi-omics analysis.. *Cancer cell international*. PMID: 38200479

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 64.8% |
| 中等置信 (pLDDT 50-70) 占比 | 35.2% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 64.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=74.3，有序区 64.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007305, IPR011691; Pfam: PF04178 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRR18 | 0.651 | 0.000 | — |
| C6orf118 | 0.593 | 0.000 | — |
| RPS6KA2 | 0.554 | 0.000 | — |
| GOLT1A | 0.519 | 0.298 | — |
| SFT2D3 | 0.518 | 0.000 | — |
| CTDNEP1 | 0.497 | 0.000 | — |
| FAM43A | 0.496 | 0.000 | — |
| TMEM60 | 0.452 | 0.000 | — |
| UNC93A | 0.447 | 0.000 | — |
| MAL2 | 0.446 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| glmU | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CERCAM | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SLC10A1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SYT16 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RETREG3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DIABLO | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SDCBP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SCN3B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.3 + PDB: 无 | pLDDT=74.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nuclear bodies; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SFT2D1 — Vesicle transport protein SFT2A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小159 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WV19
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198818-SFT2D1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SFT2D1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WV19
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
