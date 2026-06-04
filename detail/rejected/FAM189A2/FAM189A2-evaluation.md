---
type: protein-evaluation
gene: "FAM189A2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM189A2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM189A2 / C9orf61, FAM189A2, X123 |
| 蛋白名称 | Endosomal transmembrane epsin interactor 1 |
| 蛋白大小 | 450 aa / 49.7 kDa |
| UniProt ID | Q15884 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Early endosome membrane; Late endosome membrane; Recycling e |
| 蛋白大小 | 10/10 | ×1 | 10 | 450 aa / 49.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR030431 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Early endosome membrane; Late endosome membrane; Recycling endosome membrane; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- early endosome membrane (GO:0031901)
- late endosome membrane (GO:0031902)
- plasma membrane (GO:0005886)
- recycling endosome membrane (GO:0055038)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf61, FAM189A2, X123 |

**关键文献**:
1. A subset of transposable elements as mechano-response enhancer elements in controlling human embryonic stem cell fate.. *Nature cell biology*. PMID: 40962935
2. ENTREP/FAM189A2 encodes a new ITCH ubiquitin ligase activator that is downregulated in breast cancer.. *EMBO reports*. PMID: 34927784
3. SNARE-ing the Reason for Post-Cardiac Surgery Critical Illness-Related Corticosteroid Insufficiency.. *Genes*. PMID: 38275610
4. Integration of single cell and bulk transcriptomic analyses identifies FAM189A2 as a key prognostic gene in lung cancer.. *Frontiers in immunology*. PMID: 41567189
5. Early Progression Prediction in Korean Crohn's Disease Using a Korean-Specific PrediXcan Model.. *International journal of molecular sciences*. PMID: 40243508

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.6 |
| 高置信度残基 (pLDDT>90) 占比 | 6.2% |
| 置信残基 (pLDDT 70-90) 占比 | 32.7% |
| 中等置信 (pLDDT 50-70) 占比 | 17.1% |
| 低置信 (pLDDT<50) 占比 | 44.0% |
| 有序区域 (pLDDT>70) 占比 | 38.9% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.6），有序残基占 38.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030431 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TJP2 | 0.854 | 0.000 | — |
| TSPO | 0.830 | 0.076 | — |
| TMC1 | 0.761 | 0.000 | — |
| WWP2 | 0.655 | 0.651 | — |
| FAM189B | 0.655 | 0.610 | — |
| BAAT | 0.644 | 0.000 | — |
| WWP1 | 0.617 | 0.613 | — |
| ITCH | 0.611 | 0.590 | — |
| APBA1 | 0.555 | 0.000 | — |
| HECW2 | 0.550 | 0.545 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| WWP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| ENTREP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| UBQLN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:34927784|imex:IM-29244 |
| UBAC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:34927784|imex:IM-29244 |
| RPS27A | psi-mi:"MI:0018"(two hybrid) | pubmed:34927784|imex:IM-29244 |
| TRIM32 | psi-mi:"MI:0018"(two hybrid) | pubmed:34927784|imex:IM-29244 |
| UBB | psi-mi:"MI:0018"(two hybrid) | pubmed:34927784|imex:IM-29244 |
| TDP2 | psi-mi:"MI:0018"(two hybrid) | pubmed:34927784|imex:IM-29244 |
| RNF216 | psi-mi:"MI:0018"(two hybrid) | pubmed:34927784|imex:IM-29244 |
| SPRTN | psi-mi:"MI:0018"(two hybrid) | pubmed:34927784|imex:IM-29244 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.6 + PDB: 无 | pLDDT=60.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Early endosome membrane; Late endosome membrane; R / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FAM189A2 — Endosomal transmembrane epsin interactor 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小450 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15884
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135063-ENTREP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM189A2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15884
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
