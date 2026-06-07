---
type: protein-evaluation
gene: "DNAJC28"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC28 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC28 |
| 蛋白名称 | DnaJ homolog subfamily C member 28 |
| 蛋白大小 | 388 aa / 45.8 kDa |
| UniProt ID | Q9NX36 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/DNAJC28/IF_images/AF22_1.jpg|AF22]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/DNAJC28/IF_images/HEL_1.jpg|HEL]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Centrosome; 额外: Nuclear bodies, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 388 aa / 45.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.1; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 25 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome; 额外: Nuclear bodies, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 9 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Comparative genomic and evolutionary analysis of the heat shock protein gene family in the chicken genome.. *Anim Biotechnol*. PMID: 41632590
2. Identification and Validation of MTFP1 as a Mitochondrial Target Restoring Dynamics and ECM Remodeling in Acute Myocardial Infarction.. *Curr Issues Mol Biol*. PMID: 41899445
3. Melocular Evolution on Cold Temperature Adaptation of Chinese Rhesus Macaques.. *Curr Genomics*. PMID: 39911280
4. A novel signature model based on mitochondrial-related genes for predicting survival of colon adenocarcinoma.. *BMC Med Inform Decis Mak*. PMID: 36273131
5. Genetic Analysis of HSP40/DNAJ Family Genes in Parkinson's Disease: a Large Case-Control Study.. *Mol Neurobiol*. PMID: 35715682

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.1 |
| 高置信度残基 (pLDDT>90) 占比 | 33.8% |
| 置信残基 (pLDDT 70-90) 占比 | 33.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.7% |
| 低置信 (pLDDT<50) 占比 | 19.6% |
| 有序区域 (pLDDT>70) 占比 | 66.8% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/DNAJC28/DNAJC28-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=75.1，有序区 66.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAM120C | 0.000 | 0.000 | — |
| MPLKIP | 0.000 | 0.000 | — |
| ATP5PB | 0.000 | 0.000 | — |
| SUGCT | 0.000 | 0.000 | — |
| FAM3B | 0.000 | 0.000 | — |
| ATP5F1B | 0.000 | 0.000 | — |
| DNAJC24 | 0.000 | 0.000 | — |
| ATP5ME | 0.000 | 0.000 | — |
| DNAJC27 | 0.000 | 0.000 | — |
| CTTNBP2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q09666 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q9NX36 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P06576 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q96FV0 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 10
- 调控相关比例: 5 / 20 = 25%

**评价**: STRING 25 个预测互作，IntAct 10 个实验互作。调控相关配体占比 25%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.1 + PDB: 无 | pLDDT=75.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Centrosome; 额外: Nuclear bodies, Cytos | 待确认 |
| PPI | STRING + IntAct | 25 + 10 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNAJC28 — DnaJ homolog subfamily C member 28，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小388 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NX36
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177692-DNAJC28/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC28
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NX36
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/DNAJC28/DNAJC28-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NX36 |
| SMART | SM00271; |
| UniProt Domain [FT] | DOMAIN 51..115; /note="J"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00286" |
| InterPro | IPR052573;IPR001623;IPR018961;IPR036869; |
| Pfam | PF09350;PF00226; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177692-DNAJC28/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IARS2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
