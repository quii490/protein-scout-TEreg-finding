---
type: protein-evaluation
gene: "GJD4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GJD4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GJD4 / CX40.1 |
| 蛋白名称 | Gap junction delta-4 protein |
| 蛋白大小 | 370 aa / 40.1 kDa |
| UniProt ID | Q96KN9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell junction, gap junction |
| 蛋白大小 | 10/10 | ×1 | 10 | 370 aa / 40.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.9; PDB: 8GN7, 8GN8, 8GNB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000500, IPR019570, IPR017990, IPR013092, IPR038 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cell junction, gap junction | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- connexin complex (GO:0005922)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CX40.1 |

**关键文献**:
1. Gap-junction-mediated bioelectric signaling required for slow muscle development and function in zebrafish.. *Current biology : CB*. PMID: 38936363
2. Gap junction mediated bioelectric coordination is required for slow muscle development, organization, and function.. *bioRxiv : the preprint server for biology*. PMID: 38187655
3. Connexin39 deficient mice display accelerated myogenesis and regeneration of skeletal muscle.. *Experimental cell research*. PMID: 21272575
4. QTL Mapping of Endocochlear Potential Differences between C57BL/6J and BALB/cJ mice.. *Journal of the Association for Research in Otolaryngology : JARO*. PMID: 26980469
5. In-depth computational analysis reveals the significant dysregulation of key gap junction proteins (GJPs) driving thoracic aortic aneurysm development.. *Hellenic journal of cardiology : HJC = Hellenike kardiologike epitheorese*. PMID: 39800318

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.9 |
| 高置信度残基 (pLDDT>90) 占比 | 37.0% |
| 置信残基 (pLDDT 70-90) 占比 | 15.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 40.5% |
| 有序区域 (pLDDT>70) 占比 | 52.9% |
| 可用 PDB 条目 | 8GN7, 8GN8, 8GNB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.9），有序残基占 52.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000500, IPR019570, IPR017990, IPR013092, IPR038359; Pfam: PF00029 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FXYD4 | 0.961 | 0.000 | — |
| GJE1 | 0.582 | 0.000 | — |
| ZBBX | 0.524 | 0.000 | — |
| TBC1D22B | 0.511 | 0.000 | — |
| GJA8 | 0.482 | 0.000 | — |
| NRSN2 | 0.480 | 0.000 | — |
| CALHM1 | 0.475 | 0.000 | — |
| GJD3 | 0.463 | 0.000 | — |
| PLCD4 | 0.461 | 0.000 | — |
| GJB3 | 0.456 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000315070.1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| STXBP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| STXBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FOXK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| STXBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MBLAC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DPP9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PTER | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZNF708 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.9 + PDB: 8GN7, 8GN8, 8GNB | pLDDT=67.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, gap junction / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GJD4 — Gap junction delta-4 protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小370 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96KN9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177291-GJD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GJD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96KN9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96KN9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
