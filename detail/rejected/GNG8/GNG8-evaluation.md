---
type: protein-evaluation
gene: "GNG8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNG8 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNG8 / GNG8, GNG9, GNGT8 |
| 蛋白名称 | Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-T2 |
| 蛋白大小 | 69 aa / 7.7 kDa |
| UniProt ID | O14610 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 69 aa / 7.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001770, IPR015898, IPR036284; Pfam: PF00631 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- heterotrimeric G-protein complex (GO:0005834)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GNG8, GNG9, GNGT8 |

**关键文献**:
1. Research into the characteristic molecules significantly affecting liver cancer immunotherapy.. *Frontiers in immunology*. PMID: 36860864
2. Regulation of habenular G-protein gamma 8 on learning and memory via modulation of the central acetylcholine system.. *Molecular psychiatry*. PMID: 32989244
3. Post-GWAS functional characterization of susceptibility variants for chronic lymphocytic leukemia.. *PloS one*. PMID: 22235315
4. FIZZ1 could enhance the angiogenic ability of rat aortic endothelial cells.. *International journal of clinical and experimental pathology*. PMID: 24040449
5. Identification of Regeneration and Hub Genes and Pathways at Different Time Points after Spinal Cord Injury.. *Molecular neurobiology*. PMID: 33484404

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.7 |
| 高置信度残基 (pLDDT>90) 占比 | 66.7% |
| 置信残基 (pLDDT 70-90) 占比 | 20.3% |
| 中等置信 (pLDDT 50-70) 占比 | 13.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 87.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.7，有序区 87.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001770, IPR015898, IPR036284; Pfam: PF00631 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNB4 | 0.998 | 0.995 | — |
| GNB1 | 0.998 | 0.995 | — |
| GNB2 | 0.998 | 0.995 | — |
| GNAS | 0.951 | 0.453 | — |
| CXCR4 | 0.918 | 0.120 | — |
| HTR7 | 0.912 | 0.120 | — |
| MTNR1B | 0.908 | 0.120 | — |
| APLNR | 0.908 | 0.120 | — |
| CCR5 | 0.908 | 0.120 | — |
| PREX1 | 0.900 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Kcnk2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23021213|imex:IM-18125 |
| GNB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| GNAI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| GNGT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| GNB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| GNB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| GNB4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| GNAS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| GNB5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |
| Ntsr1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.7 + PDB: 无 | pLDDT=89.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GNG8 — Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-T2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小69 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14610
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167414-GNG8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNG8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14610
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
