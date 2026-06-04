---
type: protein-evaluation
gene: "CCDC91"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC91 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC91 / GGABP |
| 蛋白全名 | Coiled-coil domain-containing protein 91 |
| 蛋白大小 | 441 aa / 50.0 kDa |
| UniProt ID | Q7Z6B0 |
| 子定位分类 | nucleoplasm |
| HPA IF 主定位 | Nucleoplasm, Golgi apparatus, Acrosome |
| HPA IF 附加定位 | Equatorial segment, Flagellar centriole |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | HPA主定位核 |
| 蛋白大小 | 10/10 | x1 | 10 | 441 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=16 (Extremely novel) |
| 三维结构 | 8/10 | x3 | 24 | PDB实验结构(1条目) + AlphaFold(pLDDT=74.6) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (2条) |
| 互证加分 | — | max+3 | +2.0 | PDB实验结构(1条目) (+1.0); IntAct实验互作丰富(15条) (+0.5); STRING实验分>0.7 (+0.5) |
| **加权总分** | | | **146.0/180** | |
| **归一化总分 (÷1.83)** | | | **79.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Golgi apparatus, Acrosome, Equatorial segment, Flagellar centriole | Approved |
| UniProt | Membrane (ECO:0000269); Golgi apparatus, trans-Golgi network membrane (ECO:0000269); Golgi apparatus, trans-Golgi networ | Swiss-Prot/TrEMBL |
| GO-CC | acrosomal vesicle (IDA:HPA); centriole (IDA:HPA); cytosol (IEA:GOC); Golgi apparatus (IDA:HPA); membrane (IEA:UniProtKB-SubCell) | |

暂无PAE图

HPA IF 图像可用 (2张)，待下载。

**结论**: HPA主定位核

#### 3.2 蛋白大小评估

441 aa (200-800 aa ideal range)

**评价**: 441 aa / 50.0 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 16 |
| PubMed symbol_only | 24 |
| PubMed broad | 24 |
| 别名 | GGABP |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 16 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **HBV DNA integration gene CCDC91 is oncogenic and a potential therapeutic target for hepatocellular carcinoma.** *Communications biology* (2025 Jul 20) PMID:40683971 -- Li M et al.
2. **Genomic Structural Equation Modelling Reveals the Shared Genetic Architecture for Oral Frailty.** *Oral health & preventive dentistry* (2025 Nov 26) PMID:41294023 -- Chen Y et al.
3. **Establishment of a 7-gene expression panel to improve the prognosis classification of gastric cancer patients.** *Frontiers in genetics* (2023) PMID:37772256 -- Velásquez Sotomayor MB et al.
4. **A mutation in CCDC91, Homo sapiens coiled-coil domain containing 91 protein, cause autosomal-dominant acrokeratoelastoidosis.** *European journal of human genetics : EJHG* (2024 Jun) PMID:38627542 -- Zhu Y et al.
5. **A three-gene signature marks the time to locoregional recurrence in luminal-like breast cancer.** *ESMO open* (2023 Aug) PMID:37393630 -- Chiodoni C et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 74.6 |
| pLDDT > 90 (Very High) | 47.6% |
| pLDDT 70-90 (High) | 19.3% |
| pLDDT 50-70 (Medium) | 5.4% |
| pLDDT < 50 (Low) | 27.7% |
| 有序区域 (pLDDT>70) 占比 | 66.9% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 1OM9 (X-ray, 2.50 A, P/Q=2-16) |

暂无PAE图

**评价**: 实验结构（PDB: 1OM9 (X-ray, 2.50 A, P/Q=2-16)）提供可靠信息；AlphaFold pLDDT=74.6，有序区域 67%。

**评分: 8/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 存在注释结构域（0个），但未发现明确染色质/DNA结合域。新颖蛋白基线不扣分。

**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| GGA1 | 0.989 | 0.977 | — |
| C10orf88 | 0.649 | 0.223 | — |
| KLHL42 | 0.592 | 0.000 | — |
| MVK | 0.578 | 0.578 | — |
| STK38L | 0.529 | 0.095 | — |
| ERGIC2 | 0.505 | 0.055 | — |
| GGA2 | 0.489 | 0.292 | — |
| RSPH9 | 0.483 | 0.047 | — |
| OR4K13 | 0.477 | 0.000 | — |
| NUP37 | 0.475 | 0.100 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| ENSP00000445660.2 | 0397(two hybrid array) | imex:IM-23318|pubmed | — |
| EWSR1 | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| TESC | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| MVK | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| ANGPTL3 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| CCDC102A | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| PAAT | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| STARD7 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| PRR5L | 0397(two hybrid array) | pubmed:32296183|imex | — |
| DAPK2 | 0397(two hybrid array) | pubmed:32296183|imex | — |


**已知复合体成员** (GO Cellular Component):
- acrosomal vesicle (IDA:HPA)
- centriole (IDA:HPA)
- cytosol (IEA:GOC)
- Golgi apparatus (IDA:HPA)
- membrane (IEA:UniProtKB-SubCell)
- nucleoplasm (IDA:HPA)
- trans-Golgi network (IDA:UniProtKB)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 13
- 调控相关比例: 0/15 (0%)

**评价**: STRING实验分>0.5 (2条)

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 13 | 数据充分 |

**互证加分明细**:
- PDB实验结构(1条目) (+1.0)
- IntAct实验互作丰富(15条) (+0.5)
- STRING实验分>0.7 (+0.5)
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (79.8/100)

**核心优势**:
1. Extremely novel -- PubMed=16篇
2. HPA主定位核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z6B0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC91
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z6B0
- STRING: https://string-db.org/cgi/network?identifiers=CCDC91&species=9606
