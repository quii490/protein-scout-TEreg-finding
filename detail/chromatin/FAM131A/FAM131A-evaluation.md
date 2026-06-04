---
type: protein-evaluation
gene: "FAM131A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM131A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM131A / C3orf40 |
| 蛋白名称 | Protein FAM131A |
| 蛋白大小 | 366 aa / 39.5 kDa |
| UniProt ID | Q6UXB0 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/FAM131A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/chromatin/FAM131A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli rim; 额外: Mitotic chromosome; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 366 aa / 39.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026782; Pfam: PF15010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli rim; 额外: Mitotic chromosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf40 |

**关键文献**:
1. Normal bronchial field basal cells show persistent methylome-wide impact of tobacco smoking, including in known cancer genes.. *Epigenetics*. PMID: 39980243
2. Gene fusion characterisation of rare aggressive prostate cancer variants-adenosquamous carcinoma, pleomorphic giant-cell carcinoma, and sarcomatoid carcinoma: an analysis of 19 cases.. *Histopathology*. PMID: 32639612
3. [Study on the exposure of polychlorinated biphenyl contamination and DNA methylation in male employees in an e-waste dismantling area in Tianjin].. *Zhonghua yu fang yi xue za zhi [Chinese journal of preventive medicine]*. PMID: 30982271

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.3 |
| 高置信度残基 (pLDDT>90) 占比 | 1.4% |
| 置信残基 (pLDDT 70-90) 占比 | 13.7% |
| 中等置信 (pLDDT 50-70) 占比 | 32.0% |
| 低置信 (pLDDT<50) 占比 | 53.0% |
| 有序区域 (pLDDT>70) 占比 | 15.1% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/chromatin/FAM131A/FAM131A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=52.3），有序残基占 15.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026782; Pfam: PF15010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DPY19L4 | 0.540 | 0.000 | — |
| ILKAP | 0.494 | 0.000 | — |
| VWA5B2 | 0.486 | 0.000 | — |
| OR10V1 | 0.479 | 0.000 | — |
| DHRS13 | 0.479 | 0.000 | — |
| C21orf62 | 0.473 | 0.000 | — |
| ABCF3 | 0.463 | 0.000 | — |
| GFOD2 | 0.463 | 0.000 | — |
| MAP6D1 | 0.436 | 0.000 | — |
| ALG3 | 0.420 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PHYHIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ENST00000340957 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 2
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.3 + PDB: 无 | pLDDT=52.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli rim; 额外: Mitotic chromosome | 待确认 |
| PPI | STRING + IntAct | 10 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM131A — Protein FAM131A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小366 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=52.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UXB0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175182-FAM131A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM131A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UXB0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/FAM131A/FAM131A-PAE.png]]




