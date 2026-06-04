---
type: protein-evaluation
gene: "NPHP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NPHP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NPHP3 / KIAA2000 |
| 蛋白名称 | Nephrocystin-3 |
| 蛋白大小 | 1330 aa / 150.9 kDa |
| UniProt ID | Q7Z494 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Primary cilium; 额外: Nucleoplasm, Vesicles, Primary; UniProt: Cell projection, cilium |
| 蛋白大小 | 5/10 | ×1 | 5 | 1330 aa / 150.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=80 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=72.6; PDB: 5L7K |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR056884, IPR056886, IPR056883, IPR027417, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Primary cilium; 额外: Nucleoplasm, Vesicles, Primary cilium tip, Cytosol | Approved |
| UniProt | Cell projection, cilium | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ciliary base (GO:0097546)
- ciliary inversin compartment (GO:0097543)
- cilium (GO:0005929)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 80 |
| PubMed broad count | 112 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA2000 |

**关键文献**:
1. Nephronophthisis-Related Ciliopathies.. **. PMID: 27336129
2. Noncoding variants are a rare cause of recessive developmental disorders in trans with coding variants.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 39243181
3. Mutations in a novel gene, NPHP3, cause adolescent nephronophthisis, tapeto-retinal degeneration and hepatic fibrosis.. *Nature genetics*. PMID: 12872122
4. Nephrocystin-3 is required for ciliary function in zebrafish embryos.. *American journal of physiology. Renal physiology*. PMID: 20462968
5. Mutations of NPHP2 and NPHP3 in infantile nephronophthisis.. *Kidney international*. PMID: 19177160

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.6 |
| 高置信度残基 (pLDDT>90) 占比 | 8.3% |
| 置信残基 (pLDDT 70-90) 占比 | 64.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 18.9% |
| 有序区域 (pLDDT>70) 占比 | 72.8% |
| 可用 PDB 条目 | 5L7K |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=72.6，有序区 72.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056884, IPR056886, IPR056883, IPR027417, IPR011990; Pfam: PF25022, PF24884, PF24883 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NEK8 | 0.991 | 0.000 | — |
| NPHP1 | 0.987 | 0.315 | — |
| NPHP4 | 0.983 | 0.000 | — |
| UNC119B | 0.975 | 0.699 | — |
| INVS | 0.974 | 0.106 | — |
| ANKS6 | 0.974 | 0.106 | — |
| NEK9 | 0.973 | 0.045 | — |
| IQCB1 | 0.951 | 0.088 | — |
| RPGRIP1L | 0.941 | 0.045 | — |
| CEP290 | 0.919 | 0.054 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Nphp1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Prss3b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Ogt | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Invs | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Try5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Hspa8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| trypsinogen | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Try10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| ENSP00000338766.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| DYSF | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.6 + PDB: 5L7K | pLDDT=72.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell projection, cilium / Nucleoli, Primary cilium; 额外: Nucleoplasm, Vesicle | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. NPHP3 — Nephrocystin-3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1330 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 80 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z494
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113971-NPHP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NPHP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z494
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
