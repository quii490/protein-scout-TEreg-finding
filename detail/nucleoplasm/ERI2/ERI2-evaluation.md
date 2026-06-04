---
type: protein-evaluation
gene: "ERI2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ERI2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERI2 / EXOD1, KIAA1504 |
| 蛋白名称 | ERI1 exoribonuclease 2 |
| 蛋白大小 | 691 aa / 77.4 kDa |
| UniProt ID | A8K979 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERI2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERI2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 691 aa / 77.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.9; PDB: 7N8V, 7N8W |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051274, IPR047201, IPR013520, IPR012337, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus | Approved |
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
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EXOD1, KIAA1504 |

**关键文献**:
1. Canonical correlation analysis for gene-based pleiotropy discovery.. *PLoS computational biology*. PMID: 25329069
2. Efficient Identification of the MYC Regulator with the Use of the CRISPR Library and Context-Matched Database Screenings.. *International journal of molecular sciences*. PMID: 35887071
3. [Pan-cancer analysis of ubiquitin-specific protease 7 and its expression changes in the carcinogenesis of scar ulcer].. *Zhonghua shao shang yu chuang mian xiu fu za zhi*. PMID: 37805766

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.9 |
| 高置信度残基 (pLDDT>90) 占比 | 30.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 56.4% |
| 有序区域 (pLDDT>70) 占比 | 37.8% |
| 可用 PDB 条目 | 7N8V, 7N8W |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERI2/ERI2-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=58.9），有序残基占 37.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051274, IPR047201, IPR013520, IPR012337, IPR036397; Pfam: PF00929, PF06839 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XRN2 | 0.946 | 0.000 | — |
| DNASE1L2 | 0.712 | 0.000 | — |
| DXO | 0.685 | 0.000 | — |
| TJAP1 | 0.648 | 0.000 | — |
| TDRD12 | 0.603 | 0.000 | — |
| DNAJC12 | 0.566 | 0.566 | — |
| ERI1 | 0.525 | 0.000 | — |
| INTS14 | 0.484 | 0.000 | — |
| L3MBTL2 | 0.462 | 0.000 | — |
| EXD1 | 0.447 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FLNC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAJC12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CASQ2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28611246|imex:IM-25425 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.9 + PDB: 7N8V, 7N8W | pLDDT=58.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Golgi apparatus | 待确认 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ERI2 — ERI1 exoribonuclease 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小691 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A8K979
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196678-ERI2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERI2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8K979
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ERI2/ERI2-PAE.png]]




