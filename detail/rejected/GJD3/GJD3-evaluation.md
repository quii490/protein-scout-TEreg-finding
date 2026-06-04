---
type: protein-evaluation
gene: "GJD3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GJD3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GJD3 / GJA11, GJC1 |
| 蛋白名称 | Gap junction delta-3 protein |
| 蛋白大小 | 294 aa / 31.9 kDa |
| UniProt ID | Q8N144 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell junction, gap junction |
| 蛋白大小 | 10/10 | ×1 | 10 | 294 aa / 31.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000500, IPR019570, IPR017990, IPR013092, IPR038 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cell junction, gap junction | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- connexin complex (GO:0005922)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GJA11, GJC1 |

**关键文献**:
1. A rare haplotype of the GJD3 gene segregating in familial Meniere's disease interferes with connexin assembly.. *Genome medicine*. PMID: 39815343
2. Using Gjd3-CreEGFP mice to examine atrioventricular node morphology and composition.. *Scientific reports*. PMID: 30765799
3. Presenilin-1-Derived Circular RNAs: Neglected Epigenetic Regulators with Various Functions in Alzheimer's Disease.. *Biomolecules*. PMID: 37759801
4. Integrative Analyses Identify Potential Key Genes and Calcium-Signaling Pathway in Familial Atrioventricular Nodal Reentrant Tachycardia Using Whole-Exome Sequencing.. *Frontiers in cardiovascular medicine*. PMID: 35924220
5. Spatial Transcriptomics Shows a Distinctive Tumour Microenvironment in the Invasive Versus Premalignant Portion of Early Cutaneous Squamous Cell Carcinoma.. *Experimental dermatology*. PMID: 40462294

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.3 |
| 高置信度残基 (pLDDT>90) 占比 | 44.6% |
| 置信残基 (pLDDT 70-90) 占比 | 25.5% |
| 中等置信 (pLDDT 50-70) 占比 | 16.7% |
| 低置信 (pLDDT<50) 占比 | 13.3% |
| 有序区域 (pLDDT>70) 占比 | 70.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.3，有序区 70.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000500, IPR019570, IPR017990, IPR013092, IPR038359; Pfam: PF00029 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GJA3 | 0.907 | 0.000 | — |
| GJB2 | 0.906 | 0.000 | — |
| GJA8 | 0.906 | 0.000 | — |
| TJP1 | 0.897 | 0.292 | — |
| GJC1 | 0.793 | 0.124 | — |
| GJB4 | 0.757 | 0.000 | — |
| GJB1 | 0.757 | 0.000 | — |
| GJA1 | 0.753 | 0.088 | — |
| GJA5 | 0.752 | 0.000 | — |
| GJE1 | 0.702 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TJP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12154091|imex:IM-20451 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.3 + PDB: 无 | pLDDT=77.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, gap junction / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GJD3 — Gap junction delta-3 protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小294 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N144
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183153-GJD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GJD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N144
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
