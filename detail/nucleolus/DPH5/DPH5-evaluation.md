---
type: protein-evaluation
gene: "DPH5"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## DPH5 核蛋白评估报告（HPA复核救回）

**IF 图像

![[Projects/TEreg-finding/protein-interested/detail/nucleolus/DPH5/IF_images/DPH5_Rh30_4.jpg]]**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/DPH5/IF_images/DPH5_Rh30_1.jpg]]

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli (Reliability: Approved)，确认为核蛋白。

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DPH5 |
| 蛋白名称 | Diphthine methyl ester synthase |
| 蛋白大小 | 285 aa |
| UniProt ID | [Q9H2P9](https://www.uniprot.org/uniprotkb/Q9H2P9) |
| HPA 核定位 (IF) | Nucleoli |
| HPA 可靠性 | Approved |
| PubMed 总数 | 15 |
| AlphaFold pLDDT | 92.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 285 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 15篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 92.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **132/183** |  |
| **归一化总分** |  |  | **72.1/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 DPH5 定位：
- **亚细胞定位**: Nucleoli
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Fan C et al. (2025). "Integrated bulk and single-cell RNA sequencing to identify potential biomarkers in intervertebral disc degeneration". *Eur J Med Res*. PMID: 39953636
2. Zhang XG et al. (2022). "A diarylheptanoid compound from Alpinia officinarum Hance ameliorates high glucose-induced insulin resistance by regulating PI3K/AKT-Nrf2-GSK3β signaling pathways in HepG2 cells". *J Ethnopharmacol*. PMID: 35605918
3. Shankar SP et al. (2022). "A novel DPH5-related diphthamide-deficiency syndrome causing embryonic lethality or profound neurodevelopmental disorder". *Genet Med*. PMID: 35482014
4. Tsuda-Sakurai K et al. (2020). "Diphthamide modification of eEF2 is required for gut tumor-like hyperplasia induced by oncogenic Ras". *Genes Cells*. PMID: 31828897
5. Politano D et al. (2025). "Expanding the Phenotypic Spectrum Associated with DPH5-Related Diphthamide Deficiency". *Genes (Basel)*. PMID: 40725455

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| EFT1 | inferred by author | 16429126 | — | — |
| MAS2 | inferred by author | 16429126 | — | — |
| MAS1 | inferred by author | 16429126 | — | — |
| RPL6B | inferred by author | 16429126 | — | — |
| NimC1 | two hybrid | 14605208 | — | — |
| hsamir7695p | clash | 23622248 | — | — |
| EBI-25609177 | clash | 23622248 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 7 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli
2. **研究新颖性**: PubMed仅15篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 92.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/DPH5)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9H2P9)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=DPH5%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9H2P9)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




