---
type: protein-evaluation
gene: "FAM102B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM102B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM102B / FAM102B |
| 蛋白名称 | EEIG family member 2 |
| 蛋白大小 | 360 aa / 39.3 kDa |
| UniProt ID | Q5T8I3 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM102B/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM102B/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 360 aa / 39.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039931, IPR019448; Pfam: PF10358 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol | Approved |
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
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM102B |

**关键文献**:
1. Multiple interactions mediate the localization of BLTP2 at ER-PM contacts to control plasma membrane dynamics.. *bioRxiv : the preprint server for biology*. PMID: 39974967
2. Predicting drug-free remission in rheumatoid arthritis: A prospective interventional cohort study.. *Journal of autoimmunity*. PMID: 31280933
3. Population Cohort-Validated PM(2.5)-Induced Gene Signatures: A Machine Learning Approach to Individual Exposure Prediction.. *Toxics*. PMID: 40711007
4. Multiple interactions recruit BLTP2 to ER-PM contacts to control plasma membrane dynamics.. *The Journal of cell biology*. PMID: 40899996

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.2 |
| 高置信度残基 (pLDDT>90) 占比 | 35.3% |
| 置信残基 (pLDDT 70-90) 占比 | 18.6% |
| 中等置信 (pLDDT 50-70) 占比 | 12.8% |
| 低置信 (pLDDT<50) 占比 | 33.3% |
| 有序区域 (pLDDT>70) 占比 | 53.9% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM102B/FAM102B-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=70.2，有序区 53.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039931, IPR019448; Pfam: PF10358 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SEC61G | 0.608 | 0.498 | — |
| GPSM2 | 0.564 | 0.299 | — |
| PCP2 | 0.512 | 0.221 | — |
| FNDC7 | 0.505 | 0.000 | — |
| ANKRD39 | 0.499 | 0.045 | — |
| PI4KB | 0.491 | 0.071 | — |
| PRPF38B | 0.487 | 0.000 | — |
| TMEM167B | 0.471 | 0.000 | — |
| PRDM5 | 0.466 | 0.452 | — |
| AKNAD1 | 0.464 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRDM5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| THOC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cenph | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| VPS26A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MPP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Ppp4r3a | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| BUD13 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.2 + PDB: 无 | pLDDT=70.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM102B — EEIG family member 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小360 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T8I3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162636-FAM102B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM102B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T8I3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM102B/FAM102B-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5T8I3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 1..142; /note="C2 NT-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01186" |
| InterPro | IPR039931;IPR019448; |
| Pfam | PF10358; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162636-FAM102B/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
