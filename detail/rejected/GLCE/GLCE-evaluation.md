---
type: protein-evaluation
gene: "GLCE"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GLCE — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLCE / KIAA0836 |
| 蛋白名称 | D-glucuronyl C5-epimerase |
| 蛋白大小 | 617 aa / 70.1 kDa |
| UniProt ID | O94923 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 617 aa / 70.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.5; PDB: 6HZZ, 6I01, 6I02 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010598, IPR039721, IPR059154; Pfam: PF06662, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.0/180** | |
| **归一化总分** | | | **57.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 69 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0836 |

**关键文献**:
1. Hepatic glucuronyl C5-epimerase combats obesity by stabilising GDF15.. *Journal of hepatology*. PMID: 37217020
2. Cell-surface d-glucuronyl C5-epimerase binds to porcine deltacoronavirus spike protein facilitating viral entry.. *Journal of virology*. PMID: 39078176
3. D-glucuronyl C5-Epimerase Binds to EGFR to Suppress Kidney Fibrosis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40788059
4. The TCF4/β-catenin pathway and chromatin structure cooperate to regulate D-glucuronyl C5-epimerase expression in breast cancer.. *Epigenetics*. PMID: 22805760
5. A high effective expression of human D-glucuronyl C5-epimerase with dimer structure in Escherichia coli.. *Frontiers in microbiology*. PMID: 40822398

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.5 |
| 高置信度残基 (pLDDT>90) 占比 | 81.5% |
| 置信残基 (pLDDT 70-90) 占比 | 4.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 12.2% |
| 有序区域 (pLDDT>70) 占比 | 85.6% |
| 可用 PDB 条目 | 6HZZ, 6I01, 6I02 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6HZZ, 6I01, 6I02）+ AlphaFold高质量预测（pLDDT=88.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010598, IPR039721, IPR059154; Pfam: PF06662, PF21174 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HS2ST1 | 0.897 | 0.094 | — |
| HS6ST1 | 0.873 | 0.125 | — |
| NDST1 | 0.757 | 0.111 | — |
| HS3ST1 | 0.736 | 0.000 | — |
| HS2ST1-2 | 0.736 | 0.094 | — |
| NDST2 | 0.726 | 0.111 | — |
| EXT1 | 0.703 | 0.000 | — |
| SDC2 | 0.690 | 0.088 | — |
| NDST3 | 0.687 | 0.111 | — |
| NDST4 | 0.686 | 0.111 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| cbbS | psi-mi:"MI:0018"(two hybrid) | pubmed:18000013 |
| EBI-1610629 | psi-mi:"MI:0018"(two hybrid) | pubmed:18000013 |
| H1-0 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ATP5F1B | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ARL6IP1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TNIK | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| HAUS7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DEFA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PEX19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GINM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.5 + PDB: 6HZZ, 6I01, 6I02 | pLDDT=88.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GLCE — D-glucuronyl C5-epimerase，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小617 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94923
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138604-GLCE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLCE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94923
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
