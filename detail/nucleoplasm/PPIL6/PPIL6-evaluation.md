---
type: protein-evaluation
gene: "PPIL6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPIL6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PPIL6 |
| 蛋白名称 | Probable inactive peptidyl-prolyl cis-trans isomerase-like 6 |
| 蛋白大小 | 311 aa / 35.2 kDa |
| UniProt ID | Q8IXY8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 311 aa / 35.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.2; PDB: 8J07 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029000, IPR002130; Pfam: PF00160 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Obesity impairs ciliary function and mucociliary clearance in the murine airway epithelium.. *American journal of physiology. Lung cellular and molecular physiology*. PMID: 39104315
2. Single-cell full-length transcriptome of human lung reveals genetic effects on isoform regulation beyond gene-level expression.. *bioRxiv : the preprint server for biology*. PMID: 42039472
3. IQUB mutation induces radial spoke 1 deficiency causing asthenozoospermia with normal sperm morphology in humans and mice.. *Cell communication and signaling : CCS*. PMID: 39849482

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.2 |
| 高置信度残基 (pLDDT>90) 占比 | 86.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 5.5% |
| 有序区域 (pLDDT>70) 占比 | 92.0% |
| 可用 PDB 条目 | 8J07 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.2，有序区 92.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029000, IPR002130; Pfam: PF00160 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RSPH3 | 0.578 | 0.130 | — |
| SYF2 | 0.574 | 0.129 | — |
| RSPH14 | 0.508 | 0.134 | — |
| NME5 | 0.506 | 0.138 | — |
| ZBTB24 | 0.500 | 0.090 | — |
| RSPH4A | 0.484 | 0.188 | — |
| ATAD5 | 0.475 | 0.000 | — |
| CFAP300 | 0.469 | 0.076 | — |
| MRPL13 | 0.460 | 0.402 | — |
| MRPL3 | 0.459 | 0.402 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BIVM | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BAG4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SORBS3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| APPBP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.2 + PDB: 8J07 | pLDDT=92.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Vesicles; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PPIL6 — Probable inactive peptidyl-prolyl cis-trans isomerase-like 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小311 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXY8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185250-PPIL6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PPIL6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXY8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
