---
type: protein-evaluation
gene: "KLF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## KLF1 — REJECTED (研究热度过高 (PubMed strict=366，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLF1 / EKLF |
| 蛋白名称 | Krueppel-like factor 1 |
| 蛋白大小 | 362 aa / 38.2 kDa |
| UniProt ID | Q13351 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 362 aa / 38.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=366 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.0; PDB: 2L2I, 2MBH, 2N23 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031786, IPR031784, IPR036236, IPR013087; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 366 |
| PubMed broad count | 515 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EKLF |

**关键文献**:
1. A single-cell atlas identifies pretreatment features of primary imatinib resistance in chronic myeloid leukemia.. *Blood*. PMID: 36857629
2. Lutheran.. *Immunohematology*. PMID: 20406022
3. An expanded registry of candidate cis-regulatory elements.. *Nature*. PMID: 41501460
4. HDAC7 is a potential therapeutic target in acute erythroid leukemia.. *Leukemia*. PMID: 39277669
5. Transcription Factor TAL1 in Erythropoiesis.. *Advances in experimental medicine and biology*. PMID: 39017847

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.0 |
| 高置信度残基 (pLDDT>90) 占比 | 0.8% |
| 置信残基 (pLDDT 70-90) 占比 | 25.7% |
| 中等置信 (pLDDT 50-70) 占比 | 24.3% |
| 低置信 (pLDDT<50) 占比 | 49.2% |
| 有序区域 (pLDDT>70) 占比 | 26.5% |
| 可用 PDB 条目 | 2L2I, 2MBH, 2N23 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.0），有序残基占 26.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031786, IPR031784, IPR036236, IPR013087; Pfam: PF16832, PF16833, PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GATA1 | 0.997 | 0.091 | — |
| RPS27A | 0.959 | 0.959 | — |
| UBC | 0.950 | 0.949 | — |
| HBG1 | 0.934 | 0.000 | — |
| TAL1 | 0.928 | 0.070 | — |
| UBA52 | 0.910 | 0.907 | — |
| UBB | 0.908 | 0.905 | — |
| AHSP | 0.906 | 0.000 | — |
| GYPA | 0.898 | 0.000 | — |
| EPB42 | 0.894 | 0.046 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RBM4B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EFEMP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MKRN3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DVL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SNRPC | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PATZ1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CCDC57 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HNRNPF | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| VPS37C | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HNRNPK | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.0 + PDB: 2L2I, 2MBH, 2N23 | pLDDT=57.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. KLF1 — Krueppel-like factor 1，研究基础较多，新颖性有限。
2. 蛋白大小362 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 366 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 366 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13351
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105610-KLF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13351
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
