---
type: protein-evaluation
gene: "EVA1B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EVA1B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EVA1B / C1orf78, FAM176B |
| 蛋白名称 | Protein eva-1 homolog B |
| 蛋白大小 | 165 aa / 18.4 kDa |
| UniProt ID | Q9NVM1 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EVA1B/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EVA1B/IF_images/PC-3_1.jpg|PC-3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoplasm, Cytosol; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 165 aa / 18.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052461, IPR039500; Pfam: PF14851 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf78, FAM176B |

**关键文献**:
1. Molecular Characteristics, Oncogenic Roles, and Relevant Immune and Pharmacogenomic Features of EVA1B in Colorectal Cancer.. *Frontiers in immunology*. PMID: 35250982
2. Epigenomic Profiles of African-American Transthyretin Val122Ile Carriers Reveals Putatively Dysregulated Amyloid Mechanisms.. *Circulation. Genomic and precision medicine*. PMID: 33428857
3. Identification of a basement membrane-related gene signature for predicting prognosis and estimating the tumor immune microenvironment in breast cancer.. *Frontiers in endocrinology*. PMID: 36531485
4. Identification of DNA-Methylated CpG Islands Associated With Gene Silencing in the Adult Body Tissues of the Ogye Chicken Using RNA-Seq and Reduced Representation Bisulfite Sequencing.. *Frontiers in genetics*. PMID: 31040866
5. Construction and Validation of a Prognostic Model Based on mRNAsi-Related Genes in Breast Cancer.. *Computational and mathematical methods in medicine*. PMID: 36267313

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.1 |
| 高置信度残基 (pLDDT>90) 占比 | 9.1% |
| 置信残基 (pLDDT 70-90) 占比 | 17.6% |
| 中等置信 (pLDDT 50-70) 占比 | 50.3% |
| 低置信 (pLDDT<50) 占比 | 23.0% |
| 有序区域 (pLDDT>70) 占比 | 26.7% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EVA1B/EVA1B-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=62.1），有序残基占 26.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052461, IPR039500; Pfam: PF14851 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLFN13 | 0.767 | 0.000 | — |
| SH3D21 | 0.514 | 0.000 | — |
| MTG2 | 0.474 | 0.000 | — |
| C11orf68 | 0.470 | 0.000 | — |
| CMPK2 | 0.442 | 0.000 | — |
| DECR2 | 0.427 | 0.000 | — |
| TMEM252 | 0.410 | 0.000 | — |
| ETNK2 | 0.407 | 0.000 | — |
| XPNPEP3 | 0.404 | 0.000 | — |
| OASL | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CYSRT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HOXA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CA14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SGTA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM131L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SLC37A4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TSPAN9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HMGCR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.1 + PDB: 无 | pLDDT=62.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

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
1. EVA1B — Protein eva-1 homolog B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小165 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVM1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142694-EVA1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EVA1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVM1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EVA1B/EVA1B-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NVM1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052461;IPR039500; |
| Pfam | PF14851; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000142694-EVA1B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACP2 | Bioplex | false |
| ACVR2A | Bioplex | false |
| ANXA1 | Intact | false |
| CA14 | Bioplex | false |
| CALR | Intact | false |
| CYSRT1 | Intact | false |
| DCAKD | Bioplex | false |
| DLST | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
