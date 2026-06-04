---
type: protein-evaluation
gene: "FAM174B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM174B — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM174B |
| 蛋白名称 | Membrane protein FAM174B |
| 蛋白大小 | 159 aa / 17.0 kDa |
| UniProt ID | Q3ZCQ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Intermediate filaments; UniProt: Cell membrane; Golgi apparatus |
| 蛋白大小 | 8/10 | ×1 | 8 | 159 aa / 17.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009565; Pfam: PF06679 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.5/180** | |
| **归一化总分** | | | **59.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Intermediate filaments | Approved |
| UniProt | Cell membrane; Golgi apparatus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular and Spatial Signatures of Mouse Embryonic Endothelial Cells at Single-Cell Resolution.. *Circulation research*. PMID: 38348657
2. Single Gene Prognostic Biomarkers in Ovarian Cancer: A Meta-Analysis.. *PloS one*. PMID: 26886260
3. Determination of candidate genes involved in schizophrenia using the whole-exome sequencing.. *Bratislavske lekarske listy*. PMID: 30226068
4. Construction and validation of prognostic model for colorectal mucinous adenocarcinoma patients and identification of a new prognosis related gene FAM174B.. *Translational cancer research*. PMID: 39525028
5. Genomic and Immunologic Correlates in Prostate Cancer with High Expression of KLK2.. *International journal of molecular sciences*. PMID: 38396898

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.6 |
| 高置信度残基 (pLDDT>90) 占比 | 5.7% |
| 置信残基 (pLDDT 70-90) 占比 | 23.9% |
| 中等置信 (pLDDT 50-70) 占比 | 49.7% |
| 低置信 (pLDDT<50) 占比 | 20.8% |
| 有序区域 (pLDDT>70) 占比 | 29.6% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=63.6），有序残基占 29.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009565; Pfam: PF06679 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LYSMD4 | 0.574 | 0.000 | — |
| ST8SIA2 | 0.522 | 0.000 | — |
| FAM124B | 0.521 | 0.000 | — |
| LYSMD3 | 0.496 | 0.000 | — |
| SCAMP4 | 0.477 | 0.000 | — |
| NUDT8 | 0.467 | 0.000 | — |
| GAK | 0.457 | 0.000 | — |
| DEPDC1 | 0.453 | 0.000 | — |
| XXYLT1 | 0.444 | 0.000 | — |
| LCN10 | 0.438 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.6 + PDB: 无 | pLDDT=63.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Golgi apparatus / Intermediate filaments | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FAM174B — Membrane protein FAM174B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小159 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3ZCQ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185442-FAM174B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM174B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3ZCQ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
