---
type: protein-evaluation
gene: "WDR26"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR26 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR26 / CDW2, MIP2 |
| 蛋白名称 | WD repeat-containing protein 26 |
| 蛋白大小 | 661 aa / 72.1 kDa |
| UniProt ID | Q9H7D7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Mitochondria; UniProt: Cytoplasm; Nucleus; Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 661 aa / 72.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.2; PDB: 8QBN, 8QE8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006595, IPR006594, IPR054532, IPR015943, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Mitochondria | Enhanced |
| UniProt | Cytoplasm; Nucleus; Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- GID complex (GO:0034657)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 70 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CDW2, MIP2 |

**关键文献**:
1. WDR26-Related Intellectual Disability.. **. PMID: 31021590
2. WDR26 depletion alters chromatin accessibility and gene expression profiles in mammalian cells.. *Genomics*. PMID: 39837355
3. Renal tubular GSDME protects cisplatin nephrotoxicity by impeding OGT-STAT3-S100A7A axis in male mice.. *Nature communications*. PMID: 40707439
4. Wdr26 regulates nuclear condensation in developing erythroblasts.. *Blood*. PMID: 31945154
5. Interplay between β-propeller subunits WDR26 and muskelin regulates the CTLH E3 ligase supramolecular complex.. *Communications biology*. PMID: 39702571

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.2 |
| 高置信度残基 (pLDDT>90) 占比 | 53.6% |
| 置信残基 (pLDDT 70-90) 占比 | 22.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 21.8% |
| 有序区域 (pLDDT>70) 占比 | 76.4% |
| 可用 PDB 条目 | 8QBN, 8QE8 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8QBN, 8QE8）+ AlphaFold高质量预测（pLDDT=79.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006595, IPR006594, IPR054532, IPR015943, IPR036322; Pfam: PF17814, PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GID8 | 0.999 | 0.987 | — |
| RMND5A | 0.997 | 0.890 | — |
| RANBP9 | 0.996 | 0.972 | — |
| ARMC8 | 0.996 | 0.885 | — |
| RANBP10 | 0.995 | 0.970 | — |
| RMND5B | 0.980 | 0.694 | — |
| GID4 | 0.972 | 0.720 | — |
| MAEA | 0.969 | 0.694 | — |
| MKLN1 | 0.961 | 0.671 | — |
| GSC | 0.954 | 0.954 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL4B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| DDB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| GRWD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| RNPS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| IMPA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| IMPA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| TTL | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| IMPA3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| UBXN7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.2 + PDB: 8QBN, 8QE8 | pLDDT=79.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Mitochondrion / Nucleoplasm, Cytosol; 额外: Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. WDR26 — WD repeat-containing protein 26，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小661 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H7D7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162923-WDR26/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR26
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H7D7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
