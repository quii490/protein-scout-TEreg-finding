---
type: protein-evaluation
gene: "CENPN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CENPN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPN / C16orf60 / ICEN32 |
| 蛋白名称 | Centromere protein N |
| 蛋白大小 | 339 aa / 39.6 kDa |
| UniProt ID | Q96H22 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | ×4 | 40 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, centromere, kinetochore |
| 蛋白大小 | 10/10 | ×1 | 10 | 339 aa / 39.6 kDa |
| 研究新颖性 | 7/10 | ×5 | 35 | PubMed strict=61 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.6; PDB: 暂无 |
| 调控结构域 | 10/10 | ×2 | 20 | InterPro: IPR052011, IPR007902; Pfam: PF05238 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **163.5/180** | |
| **归一化总分 (÷1.83)** | | | **89.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | —
| UniProt | Chromosome, centromere, kinetochore | —

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytosol (GO:0005829) [TAS:Reactome]
- inner kinetochore (GO:0000939) [IPI:ComplexPortal]
- nucleoplasm (GO:0005654) [IDA:HPA]
- nucleus (GO:0005634) [NAS:ComplexPortal]

**结论**: HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, centromere, kinetochore

#### 3.2 蛋白大小评估

**评价**: 339 aa / 39.6 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 61 |
| PubMed 搜索链接 | [CENPN PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CENPN) |

**关键文献**:
暂无文献记录。

**评价**: 有一定研究基础。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.6 |
| 高置信度残基 (pLDDT>90) 占比 | 62.2% |
| 置信残基 (pLDDT 70-90) 占比 | 23.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 6.2% |
| 有序区域 (pLDDT>70) 占比 | 85.5% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052011, IPR007902; Pfam: PF05238 |

**染色质调控潜力分析**: 存在染色质/调控相关结构域/功能特征: nucleosome, centromere, kinetochore

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CENPT | 0.999 | 0.800 | — |
| CENPQ | 0.999 | 0.970 | — |
| CENPH | 0.999 | 0.888 | — |
| CENPL | 0.999 | 0.953 | — |
| CENPC | 0.999 | 0.900 | — |
| CENPI | 0.999 | 0.906 | — |
| CENPU | 0.999 | 0.970 | — |
| CENPM | 0.999 | 0.953 | — |
| CENPA | 0.999 | 0.955 | — |
| CENPO | 0.999 | 0.976 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CENPH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12152|pubmed:19070575 |
| AKTIP | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| NCL | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| ALKBH7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| OSGIN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSSK3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DNAAF19 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GORASP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| RBM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PCDHGB4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=85.6, v6 | 预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere, kinetochore / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 多库定位一致 (HPA+UniProt): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 89.3/100

**核心优势**:
1. CENPN — Centromere protein N，较新颖，PubMed 61 篇。
2. 蛋白大小339 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold pLDDT=85.6，结构预测质量高。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计 ChIP-seq/CUT&RUN 验证染色质结合
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96H22
- Protein Atlas: https://www.proteinatlas.org/search/CENPN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96H22
- STRING: https://string-db.org/network/9606.CENPN
- Packet data timestamp: 2026-06-03 04:46:15
