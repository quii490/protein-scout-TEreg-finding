---
type: protein-evaluation
gene: "CCNQ"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCNQ 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCNQ |
| 蛋白名称 | Cyclin-Q |
| 蛋白大小 | 248 aa / 28.4 kDa |
| UniProt ID | Q8N1B3 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCNQ/IF_images/A-431_1.jpg|A 431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCNQ/IF_images/MCF-7_1.jpg|MCF 7]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 248 aa / 28.4 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.9; PDB: 无 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 28 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 1563 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Candidate Transcript Panel in Semen Extracellular Vesicles Can Improve Prediction of Aggressiveness of Prostate Cancer.. *Int J Mol Sci*. PMID: 41096831
2. Toe Polydactyly and Supernumerary Nipple: Broadening the Phenotypic Spectrum of STAR Syndrome.. *Clin Genet*. PMID: 39887729
3. Tribute to Janet Barber, MSN, RN, FAAFS - Editor CCNQ from 1976 to 2023.. *Crit Care Nurs Q*. PMID: 38860946
4. The identification of a novel CCNQ gene tail extension variant contributing to syndactyly, telecanthus and anogenital and renal malformations syndrome.. *Clin Genet*. PMID: 36284407
5. Perceptual Effects of Physical and Visual Accessibilities in Intensive Care Units: A Quasi-experimental Study.. *Crit Care Nurs Q*. PMID: 29494375

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.9 |
| 高置信度残基 (pLDDT>90) 占比 | 69.8% |
| 置信残基 (pLDDT 70-90) 占比 | 21.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 6.9% |
| 有序区域 (pLDDT>70) 占比 | 90.8% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCNQ/CCNQ-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=87.9，有序区 90.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDK10 | 0.000 | 0.000 | — |
| SALL1 | 0.000 | 0.000 | — |
| SALL4 | 0.000 | 0.000 | — |
| CDK13 | 0.000 | 0.000 | — |
| CDK12 | 0.000 | 0.000 | — |
| FLNA | 0.000 | 0.000 | — |
| CT47B1 | 0.000 | 0.000 | — |
| ARGLU1 | 0.000 | 0.000 | — |
| CDK9 | 0.000 | 0.000 | — |
| TMEM9B | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P54829 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P0CG47 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P46379-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NR09 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8N1B3-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q15131-1 | psi-mi:"MI:0727"(lexa b52 complementation) | pubmed:- |
| uniprotkb:P06493 | psi-mi:"MI:0727"(lexa b52 complementation) | pubmed:- |
| uniprotkb:Q00526 | psi-mi:"MI:0727"(lexa b52 complementation) | pubmed:- |
| uniprotkb:Q15131 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P15036 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 28
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 28 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.9 + PDB: 无 | pLDDT=87.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 25 + 28 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CCNQ — Cyclin-Q，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小248 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N1B3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000262919-CCNQ/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCNQ
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N1B3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CCNQ/CCNQ-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N1B3 |
| SMART | SM00385; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013763;IPR036915;IPR048055;IPR048053;IPR043198;IPR006671; |
| Pfam | PF00134;PF21797; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000262919-CCNQ/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
