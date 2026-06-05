---
type: protein-evaluation
gene: "GJA3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GJA3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=103，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GJA3 |
| 蛋白名称 | Gap junction alpha-3 protein |
| 蛋白大小 | 435 aa / 47.4 kDa |
| UniProt ID | Q9Y6H8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell junction, gap junction |
| 蛋白大小 | 10/10 | ×1 | 10 | 435 aa / 47.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=103 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000500, IPR002262, IPR034634, IPR019570, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **60.0/180** | |
| **归一化总分** | | | **33.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cell junction, gap junction | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- connexin complex (GO:0005922)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 103 |
| PubMed broad count | 295 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. GJA3 Genetic Variation and Autosomal Dominant Congenital Cataracts and Glaucoma Following Cataract Surgery.. *JAMA ophthalmology*. PMID: 37589989
2. Charged multivesicular body protein 4b forms complexes with gap junction proteins during lens fiber cell differentiation.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 36880430
3. Mutations of CX46/CX50 and Cataract Development.. *Frontiers in molecular biosciences*. PMID: 35223995
4. Connexin46 in the nucleus of cancer cells: a possible role as transcription modulator.. *Cell communication and signaling : CCS*. PMID: 40148950
5. The impact of GJA3 SNPs on susceptibility to age-related cataract.. *International journal of ophthalmology*. PMID: 31236361

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.8 |
| 高置信度残基 (pLDDT>90) 占比 | 29.0% |
| 置信残基 (pLDDT 70-90) 占比 | 21.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 38.2% |
| 有序区域 (pLDDT>70) 占比 | 50.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.8），有序残基占 50.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000500, IPR002262, IPR034634, IPR019570, IPR017990; Pfam: PF00029 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GJA8 | 0.995 | 0.000 | — |
| GJA1 | 0.968 | 0.292 | — |
| GJB2 | 0.957 | 0.207 | — |
| BFSP2 | 0.939 | 0.000 | — |
| CRYGD | 0.931 | 0.000 | — |
| CRYBB2 | 0.929 | 0.000 | — |
| CRYBB1 | 0.923 | 0.000 | — |
| CRYGS | 0.921 | 0.000 | — |
| GJB1 | 0.910 | 0.000 | — |
| GJD3 | 0.907 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GJB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GJB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GJC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRMT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRIM68 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SNX25 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GPRC5C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TMEM9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLHL9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLHL13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.8 + PDB: 无 | pLDDT=67.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, gap junction / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GJA3 — Gap junction alpha-3 protein，研究基础较多，新颖性有限。
2. 蛋白大小435 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 103 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6H8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121743-GJA3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GJA3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6H8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y6H8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
