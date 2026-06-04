---
type: protein-evaluation
gene: "WSCD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WSCD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WSCD2 / KIAA0789 |
| 蛋白名称 | Sialate:O-sulfotransferase 2 |
| 蛋白大小 | 565 aa / 63.8 kDa |
| UniProt ID | Q2TBF2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 565 aa / 63.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027417, IPR051589, IPR002889; Pfam: PF01822 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0789 |

**关键文献**:
1. Mitochondrial-nuclear epistasis underlying phenotypic variation in breast cancer pathology.. *Scientific reports*. PMID: 35082309
2. Copy number variation as a tool for implementing pregnancy as an aging model.. *Aging*. PMID: 37639552
3. Comprehensive Analyses of Ferroptosis-Related Alterations and Their Prognostic Significance in Glioblastoma.. *Frontiers in molecular biosciences*. PMID: 35720126
4. Comprehensive CRISPR-Cas9 screens identify genetic determinants of drug responsiveness in multiple myeloma.. *Blood advances*. PMID: 33950175
5. Co-Expression Network Analysis Identifies Molecular Determinants of Loneliness Associated with Neuropsychiatric and Neurodegenerative Diseases.. *International journal of molecular sciences*. PMID: 36982982

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.6 |
| 高置信度残基 (pLDDT>90) 占比 | 50.4% |
| 置信残基 (pLDDT 70-90) 占比 | 25.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 17.2% |
| 有序区域 (pLDDT>70) 占比 | 75.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=78.6，有序区 75.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR051589, IPR002889; Pfam: PF01822 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCM | 0.879 | 0.849 | — |
| SGSM1 | 0.468 | 0.000 | — |
| SPATA31A6 | 0.435 | 0.000 | — |
| LRP2BP | 0.417 | 0.070 | — |
| DKK1 | 0.413 | 0.398 | — |
| CDH22 | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 6，IntAct interactions: 0
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.6 + PDB: 无 | pLDDT=78.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 6 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. WSCD2 — Sialate:O-sulfotransferase 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小565 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2TBF2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000075035-WSCD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WSCD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2TBF2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
