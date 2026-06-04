---
type: protein-evaluation
gene: "APMAP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## APMAP — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | APMAP / C20orf3 |
| 蛋白名称 | Adipocyte plasma membrane-associated protein |
| 蛋白大小 | 416 aa / 46.5 kDa |
| UniProt ID | Q9HDC9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 416 aa / 46.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011042, IPR018119; Pfam: PF20067, PF03088 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 54 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf3 |

**关键文献**:
1. Inter-cellular CRISPR screens reveal regulators of cancer cell phagocytosis.. *Nature*. PMID: 34497417
2. Paraoxonase-like APMAP maintains endoplasmic-reticulum-associated lipid and lipoprotein homeostasis.. *Developmental cell*. PMID: 40318637
3. Deciphering the Metabolic Impact and Clinical Relevance of N-Glycosylation in Colorectal Cancer through Comprehensive Glycoproteomic Profiling.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40285620
4. Association of blood APMAP content and meat quality trait in Rex rabbits.. *Animal biotechnology*. PMID: 35001846
5. Direct mapping of ligandable tyrosines and lysines in cells with chiral sulfonyl fluoride probes.. *Nature chemistry*. PMID: 37460812

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.4 |
| 高置信度残基 (pLDDT>90) 占比 | 83.4% |
| 置信残基 (pLDDT 70-90) 占比 | 8.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 7.2% |
| 有序区域 (pLDDT>70) 占比 | 92.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.4，有序区 92.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011042, IPR018119; Pfam: PF20067, PF03088 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOSC10 | 0.868 | 0.000 | — |
| RPL23A | 0.818 | 0.000 | — |
| FDXACB1 | 0.793 | 0.000 | — |
| MTIF2 | 0.784 | 0.000 | — |
| EIF5B | 0.781 | 0.000 | — |
| IMP3 | 0.761 | 0.000 | — |
| MRPL20 | 0.761 | 0.000 | — |
| RPS9 | 0.756 | 0.000 | — |
| POLR2C | 0.741 | 0.000 | — |
| PDCD11 | 0.734 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RASA4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| LOXL3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Q947H0 | psi-mi:"MI:0096"(pull down) | imex:IM-14965|pubmed:20217867 |
| SMAD3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| ATF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22304920|imex:IM-17307 |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| TCOF1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| INTU | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| FAM209A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.4 + PDB: 无 | pLDDT=91.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. APMAP — Adipocyte plasma membrane-associated protein，非常新颖，仅有少数基础研究。
2. 蛋白大小416 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HDC9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101474-APMAP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=APMAP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HDC9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
