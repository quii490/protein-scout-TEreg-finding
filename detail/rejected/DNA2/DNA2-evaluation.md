---
type: protein-evaluation
gene: "DNA2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNA2 — REJECTED (核定位证据不足 (核定位得分 3/10 <= 3); 研究热度过高 (PubMed strict=693，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNA2 |
| 蛋白名称 | DNA replication ATP-dependent helicase/nuclease DNA2 |
| 蛋白大小 | 1060 aa / 120.4 kDa |
| UniProt ID | P51530 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | x4 | 12 | HPA: Mitochondria; UniProt: Nucleus; Mitochondrion |
| 蛋白大小 | 8/10 | x1 | 8 | 1060 aa / 120.4 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=693 篇 (>100->REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=87.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **66.5/180** | |
| **归一化总分** | | | **36.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Nucleus; Mitochondrion | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 693 |
| PubMed broad count | 723 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Label-Free Fluorescent Detection of T4 PNK Using a DNA Mimic Green Fluorescent Protein-Based Turn-On Biosensor.. *J Fluoresc*. PMID: 42209914
2. Whole exome sequencing reveals rare DNA repair gene variants in BRCA1/2-negative Arab early-onset breast cancer patients.. *Sci Rep*. PMID: 42098349
3. PARP1-mediated 5' flap dynamics facilitate Okazaki fragment maturation.. *bioRxiv*. PMID: 42094445
4. DNA-mediated synergistic proximity ligation for ultrasensitive electrochemiluminescence detection of microcystin-LR.. *Anal Methods*. PMID: 41919953
5. A Guanine-Enhanced Graphene-DNA Paper-Based Sensing Platform Enabling Sensitive Hg(2+) Detection.. *Biosensors (Basel)*. PMID: 42041434

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.8 |
| 高置信度残基 (pLDDT>90) 占比 | 61.4% |
| 置信残基 (pLDDT 70-90) 占比 | 30.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 1.4% |
| 有序区域 (pLDDT>70) 占比 | 92.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.8，有序区 92.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WRN | 0.000 | 0.000 | — |
| EXO1 | 0.000 | 0.000 | — |
| TOP3A | 0.000 | 0.000 | — |
| WDHD1 | 0.000 | 0.000 | — |
| RPA1 | 0.000 | 0.000 | — |
| FEN1 | 0.000 | 0.000 | — |
| RMI1 | 0.000 | 0.000 | — |
| BLM | 0.000 | 0.000 | — |
| RAD51 | 0.000 | 0.000 | — |
| RBBP8 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9W2Z4 | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8IRL9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P26793 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:P38859 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q04377 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P22336 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P10592 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P11484 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P32589 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.8 + PDB: 无 | pLDDT=87.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Mitochondrion / Mitochondria | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ** (REJECTED)

**核心优势**:
1. DNA2 -- DNA replication ATP-dependent helicase/nuclease DNA2，研究基础较多，新颖性有限。
2. 蛋白大小1060 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 693 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51530
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138346-DNA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51530
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
