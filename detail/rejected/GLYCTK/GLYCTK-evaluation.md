---
type: protein-evaluation
gene: "GLYCTK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GLYCTK — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLYCTK / HBEBP4 |
| 蛋白名称 | Glycerate kinase |
| 蛋白大小 | 523 aa / 55.3 kDa |
| UniProt ID | Q8IVS8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; 额外: Golgi apparatus, Rods & Rings; UniProt: Cytoplasm; Cytoplasm; Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 523 aa / 55.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR037035, IPR038614, IPR007835, IPR025286, IPR039 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Golgi apparatus, Rods & Rings | Supported |
| UniProt | Cytoplasm; Cytoplasm; Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HBEBP4 |

**关键文献**:
1. d-Glycerate kinase deficiency in a neuropediatric patient.. *Brain & development*. PMID: 31837836
2. Mitochondrial Dysfunction and Immune Cell Infiltration in Diabetic Kidney Disease: A Mendelian Randomization and Multiomics Study.. *Mediators of inflammation*. PMID: 41498039
3. Genome-wide association analysis links multiple psychiatric liability genes to oscillatory brain activity.. *Human brain mapping*. PMID: 29947131
4. [The Interaction of miRNA-5p and miRNA-3p with the mRNAs of Orthologous Genes].. *Molekuliarnaia biologiia*. PMID: 31397443
5. D-glyceric aciduria is caused by genetic deficiency of D-glycerate kinase (GLYCTK).. *Human mutation*. PMID: 20949620

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.3 |
| 高置信度残基 (pLDDT>90) 占比 | 82.6% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 6.1% |
| 有序区域 (pLDDT>70) 占比 | 91.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.3，有序区 91.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037035, IPR038614, IPR007835, IPR025286, IPR039760; Pfam: PF13660, PF05161 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GRHPR | 0.986 | 0.000 | — |
| TKFC | 0.970 | 0.000 | — |
| ENO1 | 0.945 | 0.000 | — |
| ENO3 | 0.942 | 0.000 | — |
| ENO2 | 0.941 | 0.000 | — |
| ENO4 | 0.938 | 0.000 | — |
| BPGM | 0.935 | 0.000 | — |
| PGAM1 | 0.930 | 0.000 | — |
| ALDH9A1 | 0.929 | 0.000 | — |
| PGAM2 | 0.928 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIP13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| STK33 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| KRTAP6-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NT5C2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ACTMAP | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ZFP90 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ADAMTSL4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRTAP6-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| METTL15 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.3 + PDB: 无 | pLDDT=90.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm; Mitochondrion / Cytosol; 额外: Golgi apparatus, Rods & Rings | 一致 |
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
1. GLYCTK — Glycerate kinase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小523 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IVS8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168237-GLYCTK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLYCTK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IVS8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
