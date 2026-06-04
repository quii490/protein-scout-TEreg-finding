---
type: protein-evaluation
gene: "ANKRD30A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKRD30A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKRD30A |
| 蛋白名称 | Ankyrin repeat domain-containing protein 30A |
| 蛋白大小 | 1397 aa / 158.8 kDa |
| UniProt ID | Q9BXX3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1397 aa / 158.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.6; PDB: 6R2L |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050657, IPR002110, IPR036770, IPR039497; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Uncertain |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Bioinformatic Identification of a Breast-Specific Transcript Profile.. *Proteomics. Clinical applications*. PMID: 32558282
2. Meta-analysis of shared genetic architecture across ten pediatric autoimmune diseases.. *Nature medicine*. PMID: 26301688
3. Verification and Validation of a Four-Gene Panel as a Prognostic Indicator in Triple Negative Breast Cancer.. *Frontiers in oncology*. PMID: 35387118
4. Microarray expression profiling of dysregulated long non-coding RNAs in triple-negative breast cancer.. *Cancer biology & therapy*. PMID: 25996380
5. Comprehensive Molecular and Genomic Analysis of NCI-MATCH Subprotocol Y: Capivasertib in Patients With an AKT1 E17K-Mutated Tumor.. *JCO precision oncology*. PMID: 40153687

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.6 |
| 高置信度残基 (pLDDT>90) 占比 | 13.6% |
| 置信残基 (pLDDT 70-90) 占比 | 29.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 52.3% |
| 有序区域 (pLDDT>70) 占比 | 43.0% |
| 可用 PDB 条目 | 6R2L |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.6），有序残基占 43.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050657, IPR002110, IPR036770, IPR039497; Pfam: PF12796, PF14915 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASZ1 | 0.611 | 0.092 | — |
| SCGB2A2 | 0.572 | 0.000 | — |
| ANKRD30B | 0.492 | 0.360 | — |
| ASB15 | 0.489 | 0.092 | — |
| CDKN2D | 0.479 | 0.092 | — |
| ANKRD39 | 0.475 | 0.092 | — |
| RANBP2 | 0.463 | 0.091 | — |
| CDKN2C | 0.453 | 0.092 | — |
| MAP4 | 0.447 | 0.058 | — |
| ASB9 | 0.443 | 0.092 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| SCLT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAB3IP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SPAG5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ANKRD30B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.6 + PDB: 6R2L | pLDDT=55.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ANKRD30A — Ankyrin repeat domain-containing protein 30A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1397 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXX3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148513-ANKRD30A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANKRD30A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXX3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
