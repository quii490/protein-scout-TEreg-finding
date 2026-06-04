---
type: protein-evaluation
gene: "MANBAL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MANBAL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MANBAL |
| 蛋白名称 | Protein MANBAL |
| 蛋白大小 | 85 aa / 9.5 kDa |
| UniProt ID | Q9NQG1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 85 aa / 9.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009621; Pfam: PF06783 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Impact of liver failure on the circulating extracellular vesicle miRNA repertoire.. *Hepatology research : the official journal of the Japan Society of Hepatology*. PMID: 37060575
2. Screening and cellular validation of prognostic genes regulated by super enhancers in oral squamous cell carcinoma.. *Bioengineered*. PMID: 34709988
3. Integrated genomic approaches identify major pathways and upstream regulators in late onset Alzheimer's disease.. *Scientific reports*. PMID: 26202100
4. Using weighted gene co-expression network analysis to identify key modules and hub genes in tongue squamous cell carcinoma.. *Medicine*. PMID: 31517839
5. Characterizing the KRAS G12C mutation in metastatic colorectal cancer: a population-based cohort and assessment of expression differences in The Cancer Genome Atlas.. *Therapeutic advances in medical oncology*. PMID: 35694189

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.0 |
| 高置信度残基 (pLDDT>90) 占比 | 20.0% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 42.4% |
| 低置信 (pLDDT<50) 占比 | 24.7% |
| 有序区域 (pLDDT>70) 占比 | 32.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.0），有序残基占 32.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009621; Pfam: PF06783 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STPG4 | 0.506 | 0.000 | — |
| ZNF574 | 0.499 | 0.000 | — |
| DPY19L1 | 0.490 | 0.000 | — |
| POMT2 | 0.438 | 0.000 | — |
| ERICH5 | 0.427 | 0.000 | — |
| LRRC57 | 0.411 | 0.000 | — |
| TMEM115 | 0.405 | 0.124 | — |
| ZNF112 | 0.403 | 0.000 | — |
| KCMF1 | 0.403 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CACNA1A | psi-mi:"MI:0018"(two hybrid) | pubmed:21078624|imex:IM-17207 |
| TMEM262 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ATP13A1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CMTM2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| VKORC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MALL | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NIPAL3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM203 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KLK5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PIGF | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 15
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.0 + PDB: 无 | pLDDT=65.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 9 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MANBAL — Protein MANBAL，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小85 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQG1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101363-MANBAL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MANBAL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQG1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
