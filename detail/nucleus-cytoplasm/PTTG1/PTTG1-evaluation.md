---
type: protein-evaluation
gene: "Pttg1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Pttg1 — REJECTED (研究热度过高 (PubMed strict=453，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Pttg1 / EAP1, PTTG, TUTR1 |
| 蛋白名称 | Securin |
| 蛋白大小 | 202 aa / 22.0 kDa |
| UniProt ID | O95997 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoli; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 202 aa / 22.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=453 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.1; PDB: 7NJ0, 7NJ1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006940; Pfam: PF04856 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 453 |
| PubMed broad count | 543 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EAP1, PTTG, TUTR1 |

**关键文献**:
1. PTTG1 Reprograms Asparagine Metabolism to Promote Hepatocellular Carcinoma Progression.. *Cancer research*. PMID: 37159932
2. Integrative network and computational toxicology reveal the molecular mechanisms in PFOA-induced spermatogenic disorder.. *Journal of environmental management*. PMID: 40367801
3. Identification of novel gene signature for lung adenocarcinoma by machine learning to predict immunotherapy and prognosis.. *Frontiers in immunology*. PMID: 37583701
4. Computational analysis for identification of early diagnostic biomarkers and prognostic biomarkers of liver cancer based on GEO and TCGA databases and studies on pathways and biological functions affecting the survival time of liver cancer.. *BMC cancer*. PMID: 34238253
5. The Role of RAC2 and PTTG1 in Cancer Biology.. *Cells*. PMID: 40072059

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.5% |
| 置信残基 (pLDDT 70-90) 占比 | 35.6% |
| 中等置信 (pLDDT 50-70) 占比 | 40.6% |
| 低置信 (pLDDT<50) 占比 | 23.3% |
| 有序区域 (pLDDT>70) 占比 | 36.1% |
| 可用 PDB 条目 | 7NJ0, 7NJ1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.1），有序残基占 36.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006940; Pfam: PF04856 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESPL1 | 0.999 | 0.999 | — |
| CDC20 | 0.999 | 0.923 | — |
| FZR1 | 0.990 | 0.923 | — |
| CDK1 | 0.985 | 0.000 | — |
| CCNB1 | 0.984 | 0.000 | — |
| UBE2C | 0.980 | 0.000 | — |
| BUB1B | 0.978 | 0.336 | — |
| CDC27 | 0.976 | 0.735 | — |
| CCNB2 | 0.970 | 0.000 | — |
| AURKA | 0.967 | 0.329 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000430642.1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CLTC | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Espl1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| DECR1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ACTBL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PMS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| HSPG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TTLL5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ZCCHC17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ZC3H3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.1 + PDB: 7NJ0, 7NJ1 | pLDDT=63.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. Pttg1 — Securin，研究基础较多，新颖性有限。
2. 蛋白大小202 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 453 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 453 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95997
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164611-PTTG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Pttg1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95997
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95997-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95997 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR006940; |
| Pfam | PF04856; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164611-PTTG1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DECR1 | Intact, Biogrid | true |
| ESPL1 | Intact, Biogrid | true |
| ANAPC11 | Biogrid | false |
| ANAPC2 | Biogrid | false |
| BUB1B | Biogrid | false |
| CDC20 | Biogrid | false |
| CDC27 | Biogrid | false |
| CUL1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
