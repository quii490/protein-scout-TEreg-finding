---
type: protein-evaluation
gene: "FIGN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FIGN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FIGN |
| 蛋白名称 | Fidgetin |
| 蛋白大小 | 759 aa / 82.1 kDa |
| UniProt ID | Q5HY92 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus matrix; Cytoplasm, cytoskeleton, microtubule organiz |
| 蛋白大小 | 10/10 | ×1 | 10 | 759 aa / 82.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003593, IPR003959, IPR003960, IPR047828, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus matrix; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- microtubule (GO:0005874)
- nuclear matrix (GO:0016363)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 57 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Distinct subtypes of polycystic ovary syndrome with novel genetic associations: An unsupervised, phenotypic clustering analysis.. *PLoS medicine*. PMID: 32574161
2. Fidgetin impacts axonal growth and branching in a local mTOR signal dependent manner.. *Experimental neurology*. PMID: 36586551
3. Fidgetin as a potential prognostic biomarker for hepatocellular carcinoma.. *International journal of medical sciences*. PMID: 33162817
4. Axonal Regeneration, Growth Cone, and the FIGN Gene Family: A Comprehensive Review.. *Current neuropharmacology*. PMID: 41220267
5. Cytoplasmic Fidgetin Induces Noncanonical Activation of β-catenin to Support Cancer Progression.. *Cancer research*. PMID: 41915830

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.4 |
| 高置信度残基 (pLDDT>90) 占比 | 31.4% |
| 置信残基 (pLDDT 70-90) 占比 | 10.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 53.1% |
| 有序区域 (pLDDT>70) 占比 | 42.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.4），有序残基占 42.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR003959, IPR003960, IPR047828, IPR050304; Pfam: PF00004, PF09336 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBXN7 | 0.665 | 0.624 | — |
| KATNB1 | 0.634 | 0.000 | — |
| LANCL1 | 0.626 | 0.625 | — |
| UFD1 | 0.481 | 0.405 | — |
| CPNE4 | 0.474 | 0.000 | — |
| GRB14 | 0.455 | 0.000 | — |
| KCNH7 | 0.427 | 0.000 | — |
| STPG2 | 0.414 | 0.045 | — |
| ATL2 | 0.409 | 0.087 | — |
| YOD1 | 0.407 | 0.295 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| LANCL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHERP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ERP44 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HGS | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NLN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| NUP54 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| PLXNA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MAP3K4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ORC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 14
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.4 + PDB: 无 | pLDDT=61.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus matrix; Cytoplasm, cytoskeleton, microtubu / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 12 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FIGN — Fidgetin，非常新颖，仅有少数基础研究。
2. 蛋白大小759 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5HY92
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182263-FIGN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FIGN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5HY92
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5HY92-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5HY92 |
| SMART | SM00382; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003593;IPR003959;IPR003960;IPR047828;IPR050304;IPR027417;IPR015415; |
| Pfam | PF00004;PF09336; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182263-FIGN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CHERP | Intact | false |
| HGS | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
