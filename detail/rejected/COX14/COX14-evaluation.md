---
type: protein-evaluation
gene: "COX14"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COX14 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COX14 / C12orf62 |
| 蛋白名称 | Cytochrome c oxidase assembly protein COX14 |
| 蛋白大小 | 57 aa / 6.6 kDa |
| UniProt ID | Q96I36 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion outer membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 57 aa / 6.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029208; Pfam: PF14880 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion outer membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrial outer membrane (GO:0005741)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C12orf62 |

**关键文献**:
1. Defective mitochondrial COX1 translation due to loss of COX14 function triggers ROS-induced inflammation in mouse liver.. *Nature communications*. PMID: 39134548
2. Extreme temperatures modulate gene expression in the airway epithelium of the lungs in mice and asthma patients.. *Frontiers in medicine*. PMID: 40313552
3. Cox25 teams up with Mss51, Ssc1, and Cox14 to regulate mitochondrial cytochrome c oxidase subunit 1 expression and assembly in Saccharomyces cerevisiae.. *The Journal of biological chemistry*. PMID: 21068384
4. A CMC1-knockout reveals translation-independent control of human mitochondrial complex IV biogenesis.. *EMBO reports*. PMID: 28082314
5. Cloning and characterization of COX14, whose product is required for assembly of yeast cytochrome oxidase.. *The Journal of biological chemistry*. PMID: 7797555

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.7 |
| 高置信度残基 (pLDDT>90) 占比 | 49.1% |
| 置信残基 (pLDDT 70-90) 占比 | 40.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 1.8% |
| 有序区域 (pLDDT>70) 占比 | 89.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.7，有序区 89.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029208; Pfam: PF14880 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COA3 | 0.996 | 0.621 | — |
| SURF1 | 0.913 | 0.292 | — |
| COX5B | 0.868 | 0.164 | — |
| COA1 | 0.802 | 0.000 | — |
| MSS51 | 0.801 | 0.000 | — |
| COX5A | 0.785 | 0.161 | — |
| COX17 | 0.753 | 0.422 | — |
| HIGD2A | 0.743 | 0.000 | — |
| COA6 | 0.733 | 0.161 | — |
| UQCR10 | 0.721 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HMT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| COA3 | psi-mi:"MI:0276"(blue native page) | imex:IM-18725|pubmed:23260140 |
| SURF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18725|pubmed:23260140 |
| MT-CO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18725|pubmed:23260140 |
| SLC25A5 | psi-mi:"MI:0276"(blue native page) | imex:IM-18725|pubmed:23260140 |
| GLS | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| NDUFA7 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LETM1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| VAPB | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| SNAP29 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.7 + PDB: 无 | pLDDT=85.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion outer membrane / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. COX14 — Cytochrome c oxidase assembly protein COX14，非常新颖，仅有少数基础研究。
2. 蛋白大小57 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96I36
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178449-COX14/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COX14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96I36
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
