---
type: protein-evaluation
gene: "EVA1A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EVA1A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EVA1A / FAM176A, TMEM166 |
| 蛋白名称 | Protein eva-1 homolog A |
| 蛋白大小 | 152 aa / 17.5 kDa |
| UniProt ID | Q9H8M9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; 额外: Plasma membrane; UniProt: Endoplasmic reticulum membrane; Lysosome membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 152 aa / 17.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052461, IPR039500; Pfam: PF14851 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.5/180** | |
| **归一化总分** | | | **52.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Plasma membrane | Supported |
| UniProt | Endoplasmic reticulum membrane; Lysosome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- endoplasmic reticulum lumen (GO:0005788)
- endoplasmic reticulum membrane (GO:0005789)
- lysosomal membrane (GO:0005765)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 57 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM176A, TMEM166 |

**关键文献**:
1. EVA1A Plays an Important Role by Regulating Autophagy in Physiological and Pathological Processes.. *International journal of molecular sciences*. PMID: 34201121
2. TMEM166/EVA1A interacts with ATG16L1 and induces autophagosome formation and cell death.. *Cell death & disease*. PMID: 27490928
3. EVA1A inhibits GBM cell proliferation by inducing autophagy and apoptosis.. *Experimental cell research*. PMID: 28185834
4. The Emerging Role of EVA1A in Different Types of Cancers.. *International journal of molecular sciences*. PMID: 35743108
5. Glucocorticoids, genes and brain function.. *Progress in neuro-psychopharmacology & biological psychiatry*. PMID: 29180230

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.7 |
| 高置信度残基 (pLDDT>90) 占比 | 11.2% |
| 置信残基 (pLDDT 70-90) 占比 | 22.4% |
| 中等置信 (pLDDT 50-70) 占比 | 50.7% |
| 低置信 (pLDDT<50) 占比 | 15.8% |
| 有序区域 (pLDDT>70) 占比 | 33.6% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.7），有序残基占 33.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052461, IPR039500; Pfam: PF14851 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PTN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SUMO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SAT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GYPA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TSPAN4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SGTB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MS4A13 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MTNR1B | psi-mi:"MI:0018"(two hybrid) | pubmed:26514267|imex:IM-24624 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 8
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.7 + PDB: 无 | pLDDT=64.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Lysosome membrane / Vesicles; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 0 + 8 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EVA1A — Protein eva-1 homolog A，非常新颖，仅有少数基础研究。
2. 蛋白大小152 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H8M9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115363-EVA1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EVA1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H8M9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
