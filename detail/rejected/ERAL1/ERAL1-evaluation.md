---
type: protein-evaluation
gene: "ERAL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERAL1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERAL1 / HERA |
| 蛋白名称 | GTPase Era, mitochondrial |
| 蛋白大小 | 437 aa / 48.4 kDa |
| UniProt ID | O75616 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; 额外: Cytosol; UniProt: Mitochondrion matrix; Mitochondrion inner membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 437 aa / 48.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=77.9; PDB: 8CSP, 8CSQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR030388, IPR006073, IPR005662, IPR015946, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Cytosol | Enhanced |
| UniProt | Mitochondrion matrix; Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrial inner membrane (GO:0005743)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HERA |

**关键文献**:
1. Perrault Syndrome Overview.. **. PMID: 25254289
2. The mitochondrial protein ERAL1 suppresses RNA virus infection by facilitating RIG-I-like receptor signaling.. *Cell reports*. PMID: 33472079
3. ERAL1 is associated with mitochondrial ribosome and elimination of ERAL1 leads to mitochondrial dysfunction and growth retardation.. *Nucleic acids research*. PMID: 20430825
4. A homozygous missense mutation in ERAL1, encoding a mitochondrial rRNA chaperone, causes Perrault syndrome.. *Human molecular genetics*. PMID: 28449065
5. New insights into Perrault syndrome, a clinically and genetically heterogeneous disorder.. *Human genetics*. PMID: 34338890

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.9 |
| 高置信度残基 (pLDDT>90) 占比 | 58.8% |
| 置信残基 (pLDDT 70-90) 占比 | 14.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 24.3% |
| 有序区域 (pLDDT>70) 占比 | 73.4% |
| 可用 PDB 条目 | 8CSP, 8CSQ |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8CSP, 8CSQ）+ AlphaFold高质量预测（pLDDT=77.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030388, IPR006073, IPR005662, IPR015946, IPR009019; Pfam: PF01926 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MRPS7 | 0.996 | 0.934 | — |
| DAP3 | 0.993 | 0.920 | — |
| MRPS22 | 0.992 | 0.885 | — |
| MRPS16 | 0.991 | 0.903 | — |
| MRPS2 | 0.989 | 0.918 | — |
| MRPS26 | 0.987 | 0.919 | — |
| PTCD3 | 0.987 | 0.881 | — |
| MRPS9 | 0.987 | 0.871 | — |
| MRPS10 | 0.986 | 0.881 | — |
| MRPS27 | 0.986 | 0.886 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSPD1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| COX14 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| MGST3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TRMT61B | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| AIFM1 | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |
| MAIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| CISD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| COQ9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.9 + PDB: 8CSP, 8CSQ | pLDDT=77.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion matrix; Mitochondrion inner membrane / Mitochondria; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ERAL1 — GTPase Era, mitochondrial，非常新颖，仅有少数基础研究。
2. 蛋白大小437 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75616
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132591-ERAL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERAL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75616
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
