---
type: protein-evaluation
gene: "DENND10"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DENND10 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DENND10 / FAM45A |
| 蛋白名称 | DENN domain-containing protein 10 |
| 蛋白大小 | 357 aa / 40.5 kDa |
| UniProt ID | Q8TCE6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Vesicles; UniProt: Late endosome |
| 蛋白大小 | 10/10 | x1 | 10 | 357 aa / 40.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=4 篇 (<=20->10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=90.7; PDB: 8P0V |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR042431, IPR037516; Pfam: PF08616 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Late endosome | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- late endosome (GO:0005770)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM45A |

**关键文献**:
1. Structure and interactions of the endogenous human Commander complex.. *Nature structural & molecular biology*. PMID: 38459129
2. Endosomal protein DENND10 promotes developmental competence of neurite extension.. *iScience*. PMID: 40330880
3. Endosomal protein DENND10/FAM45A integrates extracellular vesicle release with cancer cell migration.. *BMC biology*. PMID: 38987765
4. Commander Complex-A Multifaceted Operator in Intracellular Signaling and Cargo.. *Cells*. PMID: 34943955

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.7 |
| 高置信度残基 (pLDDT>90) 占比 | 77.0% |
| 置信残基 (pLDDT 70-90) 占比 | 15.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 2.2% |
| 有序区域 (pLDDT>70) 占比 | 92.1% |
| 可用 PDB 条目 | 8P0V |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.7，有序区 92.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042431, IPR037516; Pfam: PF08616 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS29 | 0.956 | 0.830 | — |
| AVL9 | 0.940 | 0.000 | — |
| CCDC22 | 0.938 | 0.835 | — |
| DENND11 | 0.937 | 0.000 | — |
| DENND6A | 0.936 | 0.000 | — |
| VPS26C | 0.931 | 0.785 | — |
| COMMD1 | 0.926 | 0.830 | — |
| VPS35L | 0.919 | 0.785 | — |
| CCDC93 | 0.912 | 0.837 | — |
| COMMD3 | 0.891 | 0.835 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DENND10P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ALDH2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TMEM256 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| COMMD3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| COMMD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS26C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NMT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCDC93 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS35L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COMMD7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.7 + PDB: 8P0V | pLDDT=90.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Late endosome / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: *** (REJECTED)

**核心优势**:
1. DENND10 -- DENN domain-containing protein 10，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小357 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TCE6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119979-DENND10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DENND10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TCE6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
