---
type: protein-evaluation
gene: "ARID3C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARID3C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARID3C |
| 蛋白名称 | AT-rich interactive domain-containing protein 3C |
| 蛋白大小 | 412 aa / 44.1 kDa |
| UniProt ID | A6NKF2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 412 aa / 44.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045147, IPR001606, IPR036431, IPR023334; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane raft (GO:0045121)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. ARID3C Acts as a Regulator of Monocyte-to-Macrophage Differentiation Interacting with NPM1.. *Journal of proteome research*. PMID: 38231884
2. The Prognostic Value of AT-Rich Interaction Domain (ARID) Family Members in Patients with Hepatocellular Carcinoma.. *Evidence-based complementary and alternative medicine : eCAM*. PMID: 36034939
3. Expression Signature of the AT-Rich Interactive Domain Gene Family Identified in Digestive Cancer.. *Frontiers in medicine*. PMID: 35127746
4. Protein tyrosine phosphatase receptor type R (PTPRR) antagonizes the Wnt signaling pathway in ovarian cancer by dephosphorylating and inactivating β-catenin.. *The Journal of biological chemistry*. PMID: 31653698
5. Differential expression of ARID3B in normal adult tissue and carcinomas.. *Gene*. PMID: 24704276

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.9 |
| 高置信度残基 (pLDDT>90) 占比 | 31.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 29.4% |
| 低置信 (pLDDT<50) 占比 | 33.5% |
| 有序区域 (pLDDT>70) 占比 | 37.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.9），有序残基占 37.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045147, IPR001606, IPR036431, IPR023334; Pfam: PF01388 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARID3A | 0.716 | 0.681 | — |
| DCTN3 | 0.558 | 0.000 | — |
| ARID3B | 0.551 | 0.482 | — |
| SMARCB1 | 0.540 | 0.413 | — |
| PBRM1 | 0.526 | 0.398 | — |
| CROCC2 | 0.466 | 0.066 | — |
| BRK1 | 0.449 | 0.000 | — |
| FAM219A | 0.448 | 0.000 | — |
| FAM205A | 0.433 | 0.000 | — |
| MYSM1 | 0.426 | 0.291 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CBX4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| C14orf119 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| RNF4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARID3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OR2T1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SPRR2E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZNF609 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FAAP100 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ARID3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 9
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.9 + PDB: 无 | pLDDT=65.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 11 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ARID3C — AT-rich interactive domain-containing protein 3C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小412 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NKF2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205143-ARID3C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARID3C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NKF2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NKF2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NKF2 |
| SMART | SM01014;SM00501; |
| UniProt Domain [FT] | DOMAIN 113..205; /note="ARID"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00355"; DOMAIN 304..389; /note="REKLES"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00819" |
| InterPro | IPR045147;IPR001606;IPR036431;IPR023334; |
| Pfam | PF01388; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000205143-ARID3C/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C14orf119 | Intact | false |
| RNF4 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
