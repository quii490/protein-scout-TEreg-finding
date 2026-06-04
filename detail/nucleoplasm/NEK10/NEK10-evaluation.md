---
type: protein-evaluation
gene: "NEK10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NEK10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEK10 |
| 蛋白名称 | Serine/threonine-protein kinase Nek10 |
| 蛋白大小 | 1172 aa / 133.3 kDa |
| UniProt ID | Q6ZWH5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 1172 aa / 133.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR011009, IPR042666, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular region (GO:0005576)
- protein kinase complex (GO:1902911)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Primary Ciliary Dyskinesia.. **. PMID: 20301301
2. NEK10 kinase ablation affects mitochondrial morphology, function and protein phosphorylation status.. *Proteome science*. PMID: 39379991
3. Genetic predisposition to persistent fatigue after a diagnosis of colorectal cancer.. *Journal of the National Cancer Institute*. PMID: 40889272
4. NEK10 tyrosine phosphorylates p53 and controls its transcriptional activity.. *Oncogene*. PMID: 32561851
5. NEK10 interactome and depletion reveal new roles in mitochondria.. *Proteome science*. PMID: 32368190

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.7 |
| 高置信度残基 (pLDDT>90) 占比 | 29.5% |
| 置信残基 (pLDDT 70-90) 占比 | 33.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 29.2% |
| 有序区域 (pLDDT>70) 占比 | 63.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.7），有序残基占 63.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR011009, IPR042666, IPR050660; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC4A7 | 0.803 | 0.047 | — |
| COX11 | 0.778 | 0.000 | — |
| TOX3 | 0.770 | 0.071 | — |
| LSP1 | 0.739 | 0.000 | — |
| RAD51B | 0.589 | 0.045 | — |
| FCGR1B | 0.570 | 0.102 | — |
| C1orf194 | 0.536 | 0.139 | — |
| MAP3K1 | 0.466 | 0.070 | — |
| STXBP4 | 0.461 | 0.094 | — |
| SUMO1 | 0.460 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| Map3k1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| MYO9A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KIAA0586 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PFDN6 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| PFDN1 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| VBP1 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| PFDN5 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| PFDN4 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.7 + PDB: 无 | pLDDT=69.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NEK10 — Serine/threonine-protein kinase Nek10，非常新颖，仅有少数基础研究。
2. 蛋白大小1172 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZWH5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163491-NEK10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEK10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZWH5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
