---
type: protein-evaluation
gene: "FAM122A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM122A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM122A |
| 蛋白名称 | FAM122A (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | FAM122A |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM122A/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM122A/IF_images/PC-3_1.jpg|PC-3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoplasm, Nuclear bodies; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Supported |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular mechanism of PP2A/B55α phosphatase inhibition by IER5.. *Cell chemical biology*. PMID: 40209703
2. CHK1 Inhibitor Blocks Phosphorylation of FAM122A and Promotes Replication Stress.. *Molecular cell*. PMID: 33108758
3. FAM122A Is Required for Mesendodermal and Cardiac Differentiation of Embryonic Stem Cells.. *Stem cells (Dayton, Ohio)*. PMID: 36715298
4. FAM122A Inhibits Erythroid Differentiation through GATA1.. *Stem cell reports*. PMID: 32763160
5. FAM122A maintains DNA stability possibly through the regulation of topoisomerase IIα expression.. *Experimental cell research*. PMID: 32866497

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |


**PAE**: AlphaFold 数据未获取，无 PAE 可用。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP2R1A | 0.856 | 0.811 | — |
| PPP2R2A | 0.840 | 0.799 | — |
| FAM122B | 0.821 | 0.814 | — |
| RCAN1 | 0.794 | 0.794 | — |
| PPP2R2C | 0.759 | 0.759 | — |
| PPP3CA | 0.751 | 0.748 | — |
| PPP3R1 | 0.648 | 0.648 | — |
| OGFOD1 | 0.616 | 0.000 | — |
| PPP2CB | 0.603 | 0.603 | — |
| PPP2R2D | 0.527 | 0.422 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PKM | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-22313|pubmed:24606918 |
| PPP2R1A | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| PPP2R2B | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| PPP2R2A | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| FHL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP2R2C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PABIR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KIF11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm, Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM122A — FAM122A (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/FAM122A
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187866-PABIR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM122A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/FAM122A
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96E09 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026716; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000187866-PABIR1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
