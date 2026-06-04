---
type: protein-evaluation
gene: "HIF3A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HIF3A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HIF3A / BHLHE17, MOP7, PASD7 |
| 蛋白名称 | Hypoxia-inducible factor 3-alpha |
| 蛋白大小 | 669 aa / 72.4 kDa |
| UniProt ID | Q9Y2N7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Plasma membrane; UniProt: Nucleus; Cytoplasm; Nucleus speckle; Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 669 aa / 72.4 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=95 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.1; PDB: 4WN5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR021537, IPR036638, IPR001610, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Plasma membrane | Supported |
| UniProt | Nucleus; Cytoplasm; Nucleus speckle; Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 95 |
| PubMed broad count | 271 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHE17, MOP7, PASD7 |

**关键文献**:
1. HIF3A gene disruption causes abnormal alveoli structure and early neonatal death.. *PloS one*. PMID: 38717999
2. HIF3A association with adiposity: the story begins before birth.. *Epigenomics*. PMID: 26011824
3. HIF3A cord blood methylation and systolic blood pressure at 4 years - a population-based cohort study.. *Epigenetics*. PMID: 32530724
4. DNA methylation and gene expression of HIF3A: cross-tissue validation and associations with BMI and insulin resistance.. *Clinical epigenetics*. PMID: 27594926
5. Prognostic analysis of bladder cancer with neddylation-related genes.. *Hereditas*. PMID: 40524221

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.1 |
| 高置信度残基 (pLDDT>90) 占比 | 32.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 40.4% |
| 有序区域 (pLDDT>70) 占比 | 48.7% |
| 可用 PDB 条目 | 4WN5 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.1），有序残基占 48.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR021537, IPR036638, IPR001610, IPR000014; Pfam: PF23171, PF11413, PF00989 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARNT | 0.999 | 0.792 | — |
| EPAS1 | 0.997 | 0.301 | — |
| HIF1A | 0.994 | 0.516 | — |
| ARNT2 | 0.977 | 0.464 | — |
| EGLN2 | 0.958 | 0.427 | — |
| EGLN1 | 0.950 | 0.427 | — |
| EGLN3 | 0.945 | 0.427 | — |
| VHL | 0.926 | 0.455 | — |
| EPO | 0.858 | 0.000 | — |
| ELOB | 0.753 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=65.1 + PDB: 4WN5 | pLDDT=65.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Nucleus speckle; Mitochondrion / Nucleoplasm, Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. HIF3A — Hypoxia-inducible factor 3-alpha，研究基础较多，新颖性有限。
2. 蛋白大小669 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 95 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2N7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124440-HIF3A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HIF3A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2N7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
