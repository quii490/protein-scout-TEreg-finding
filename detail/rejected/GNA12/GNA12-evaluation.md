---
type: protein-evaluation
gene: "GNA12"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNA12 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNA12 |
| 蛋白名称 | Guanine nucleotide-binding protein subunit alpha-12 |
| 蛋白大小 | 381 aa / 44.3 kDa |
| UniProt ID | Q03113 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cell membrane; Lateral cell membrane; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 381 aa / 44.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.4; PDB: 7YDJ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000469, IPR001019, IPR011025, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cell membrane; Lateral cell membrane; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- brush border membrane (GO:0031526)
- cytoplasm (GO:0005737)
- focal adhesion (GO:0005925)
- heterotrimeric G-protein complex (GO:0005834)
- lateral plasma membrane (GO:0016328)
- neuron projection (GO:0043005)
- neuronal cell body (GO:0043025)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 81 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of GNA12-driven gene signatures and key signaling networks in ovarian cancer.. *Oncology letters*. PMID: 34429759
2. Risk Variants Associated With Normal Pressure Hydrocephalus: Genome-Wide Association Study in the FinnGen Cohort.. *Neurology*. PMID: 39141892
3. RhoA-mediated G(12)-G(13) signaling maintains muscle stem cell quiescence and prevents stem cell loss.. *Cell discovery*. PMID: 39009565
4. Acid sphingomyelinase activity suggests a new antipsychotic pharmaco-treatment strategy for schizophrenia.. *Molecular psychiatry*. PMID: 39825014
5. c-Jun Contributes to Transcriptional Control of GNA12 Expression in Prostate Cancer Cells.. *Molecules (Basel, Switzerland)*. PMID: 28394299

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.4 |
| 高置信度残基 (pLDDT>90) 占比 | 77.7% |
| 置信残基 (pLDDT 70-90) 占比 | 13.4% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 91.1% |
| 可用 PDB 条目 | 7YDJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.4，有序区 91.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000469, IPR001019, IPR011025, IPR027417; Pfam: PF00503 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARHGEF1 | 0.999 | 0.593 | — |
| ARHGEF11 | 0.999 | 0.555 | — |
| ARHGEF12 | 0.999 | 0.555 | — |
| LPAR1 | 0.995 | 0.133 | — |
| S1PR3 | 0.993 | 0.125 | — |
| GNA13 | 0.992 | 0.472 | — |
| S1PR2 | 0.992 | 0.125 | — |
| S1PR5 | 0.990 | 0.125 | — |
| S1PR4 | 0.989 | 0.354 | — |
| RHOA | 0.988 | 0.115 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IL3RA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| A0A1J9V4P0 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| GNAS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Hmga2 | psi-mi:"MI:0096"(pull down) | imex:IM-23312|pubmed:26045162 |
| GNA13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RIC8A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| GNG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.4 + PDB: 7YDJ | pLDDT=89.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Lateral cell membrane; Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GNA12 — Guanine nucleotide-binding protein subunit alpha-12，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小381 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q03113
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146535-GNA12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNA12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q03113
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
