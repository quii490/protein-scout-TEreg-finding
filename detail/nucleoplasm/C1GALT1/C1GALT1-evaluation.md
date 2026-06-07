---
type: protein-evaluation
gene: "C1GALT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## C1GALT1 — REJECTED (研究热度过高 (PubMed strict=105，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C1GALT1 |
| 蛋白名称 | Glycoprotein-N-acetylgalactosamine 3-beta-galactosyltransferase 1 |
| 蛋白大小 | 363 aa / 42.2 kDa |
| UniProt ID | Q9NS00 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies, Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 363 aa / 42.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=105 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026050, IPR003378; Pfam: PF02434 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 105 |
| PubMed broad count | 207 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. C1GALT1 in health and disease.. *Oncology letters*. PMID: 34149900
2. The O-glycosyltransferase C1GALT1 promotes EWSR1::FLI1 expression and is a therapeutic target for Ewing sarcoma.. *Nature communications*. PMID: 39894896
3. Expression and Impact of C1GalT1 in Cancer Development and Progression.. *Cancers*. PMID: 34944925
4. Molecular Recognition of GalNAc in Mucin-Type O-Glycosylation.. *Accounts of chemical research*. PMID: 36815693
5. Bioinformatic Analysis of C1GALT1 in Cancer: Insights Into Prognosis, Metastasis and Therapeutic Potential.. *Cancer reports (Hoboken, N.J.)*. PMID: 40548474

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 66.4% |
| 置信残基 (pLDDT 70-90) 占比 | 22.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 3.6% |
| 有序区域 (pLDDT>70) 占比 | 88.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.2，有序区 88.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026050, IPR003378; Pfam: PF02434 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ST6GALNAC1 | 0.980 | 0.000 | — |
| C1GALT1C1 | 0.978 | 0.510 | — |
| GCNT1 | 0.974 | 0.000 | — |
| ST3GAL1 | 0.973 | 0.000 | — |
| B3GNT6 | 0.972 | 0.000 | — |
| GCNT3 | 0.971 | 0.000 | — |
| GCNT4 | 0.969 | 0.000 | — |
| ST3GAL2 | 0.949 | 0.000 | — |
| B3GALT5 | 0.943 | 0.000 | — |
| C1GALT1C1L | 0.923 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRRC15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSP90B1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CRP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DPEP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CD27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NTRK3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CX3CL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CSPG5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HPN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TMPRSS13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 无 | pLDDT=88.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nuclear bodies, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. C1GALT1 — Glycoprotein-N-acetylgalactosamine 3-beta-galactosyltransferase 1，研究基础较多，新颖性有限。
2. 蛋白大小363 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 105 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 105 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NS00
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106392-C1GALT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C1GALT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NS00
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000106392-C1GALT1/subcellular

![](https://images.proteinatlas.org/12819/136_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/12819/136_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/12819/97_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/12819/97_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/12819/99_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/12819/99_C5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NS00-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NS00 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026050;IPR003378; |
| Pfam | PF02434; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106392-C1GALT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GOLPH3 | Biogrid | false |
| GOLPH3L | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
