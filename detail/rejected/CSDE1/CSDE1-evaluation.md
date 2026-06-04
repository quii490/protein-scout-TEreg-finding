---
type: protein-evaluation
gene: "CSDE1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CSDE1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSDE1 / D1S155E, KIAA0885, NRU, UNR |
| 蛋白名称 | Cold shock domain-containing protein E1 |
| 蛋白大小 | 798 aa / 88.9 kDa |
| UniProt ID | O75534 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; 额外: Endoplasmic reticulum, Golgi apparatus, Plasma ; UniProt: Cytoplasm; Cytoplasm, Stress granule; Cytoplasm, P-body |
| 蛋白大小 | 10/10 | x1 | 10 | 798 aa / 88.9 kDa |
| 研究新颖性 | 2/10 | x5 | 10 | PubMed strict=85 篇 (≤100→2) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=79.5; PDB: 1WFQ, 1X65, 2YTV, 2YTX, 2YTY |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR011129, IPR019844, IPR056400, IPR002059, IPR012 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Endoplasmic reticulum, Golgi apparatus, Plasma membrane | Supported |
| UniProt | Cytoplasm; Cytoplasm, Stress granule; Cytoplasm, P-body | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- CRD-mediated mRNA stability complex (GO:0070937)
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- mCRD-mediated mRNA stability complex (GO:0106002)
- P-body (GO:0000932)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 85 |
| PubMed broad count | 142 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: D1S155E, KIAA0885, NRU, UNR |

**关键文献**:
1. Comprehensive Molecular Characterization of Pheochromocytoma and Paraganglioma.. *Cancer cell*. PMID: 28162975
2. Assembloid CRISPR screens reveal impact of disease genes in human neurodevelopment.. *Nature*. PMID: 37758944
3. High-Density Proximity Mapping Reveals the Subcellular Organization of mRNA-Associated Granules and Bodies.. *Molecular cell*. PMID: 29395067
4. CSDE1 promotes miR-451 biogenesis.. *Nucleic acids research*. PMID: 37493604
5. Epigenetic modification of CSDE1 locus dictates immune recognition of nascent tumorigenic cells.. *Science translational medicine*. PMID: 36724242

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.5 |
| 高置信度残基 (pLDDT>90) 占比 | 29.9% |
| 置信残基 (pLDDT 70-90) 占比 | 48.0% |
| 中等置信 (pLDDT 50-70) 占比 | 14.5% |
| 低置信 (pLDDT<50) 占比 | 7.5% |
| 有序区域 (pLDDT>70) 占比 | 77.9% |
| 可用 PDB 条目 | 1WFQ, 1X65, 2YTV, 2YTX, 2YTY |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=79.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011129, IPR019844, IPR056400, IPR002059, IPR012340; Pfam: PF00313, PF23456, PF12901 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PABPC1 | 0.985 | 0.244 | — |
| SYNCRIP | 0.984 | 0.207 | — |
| STRAP | 0.977 | 0.625 | — |
| YBX1 | 0.975 | 0.620 | — |
| HNRNPU | 0.947 | 0.084 | — |
| IGF2BP1 | 0.932 | 0.199 | — |
| HNRNPD | 0.931 | 0.097 | — |
| DHX9 | 0.929 | 0.091 | — |
| PAIP1 | 0.919 | 0.312 | — |
| G3BP1 | 0.858 | 0.675 | — |

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
| 三维结构 | AlphaFold pLDDT=79.5 + PDB: 1WFQ, 1X65, 2YTV, 2YTX, 2YTY | pLDDT=79.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, Stress granule; Cytoplasm, P / Cytosol; 额外: Endoplasmic reticulum, Golgi apparatu | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CSDE1 -- Cold shock domain-containing protein E1，研究基础较多，新颖性有限。
2. 蛋白大小798 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 85 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75534
- Protein Atlas: https://www.proteinatlas.org/ENSG00000009307-CSDE1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSDE1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75534
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
