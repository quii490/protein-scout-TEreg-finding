---
type: protein-evaluation
gene: "MORN2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MORN2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MORN2 / MOPT |
| 蛋白名称 | MORN repeat-containing protein 2 |
| 蛋白大小 | 79 aa / 8.9 kDa |
| UniProt ID | Q502X0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasmic vesicle, secretory vesicle, acrosome; Nucleus |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 79 aa / 8.9 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.6; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003409, IPR052849; Pfam: PF02493 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 6 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasmic vesicle, secretory vesicle, acrosome; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MOPT |

**关键文献**:
1. MORN2 regulates the morphology and energy metabolism of mitochondria and is required for male fertility in mice.. *Journal of translational medicine*. PMID: 38443933
2. Characterization of MORN2 stability and regulatory function in LC3-associated phagocytosis in macrophages.. *Biology open*. PMID: 32414768
3. Screening in planarians identifies MORN2 as a key component in LC3-associated phagocytosis and resistance to bacterial infection.. *Cell host & microbe*. PMID: 25211076
4. Quantitative Proteomic Analysis of Outer Membrane Vesicles from Fusobacterium nucleatum Cultivated in the Mimic Cancer Environment.. *Microbiology spectrum*. PMID: 37341631
5. Proteomic characterization of outer membrane vesicles from gut mucosa-derived fusobacterium nucleatum.. *Journal of proteomics*. PMID: 30634002

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.6 |
| 高置信度残基 (pLDDT>90) 占比 | 79.7% |
| 置信残基 (pLDDT 70-90) 占比 | 17.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 97.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 极高置信度预测（pLDDT=91.6，有序区 97.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003409, IPR052849; Pfam: PF02493 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C11orf97 | 0.693 | 0.000 | — |
| C8orf74 | 0.603 | 0.603 | — |
| TMEM239 | 0.506 | 0.000 | — |
| MORN4 | 0.453 | 0.000 | — |
| ARHGEF33 | 0.433 | 0.000 | — |
| SPA17 | 0.426 | 0.000 | — |
| OSCP1 | 0.420 | 0.000 | — |
| ANKRD35 | 0.405 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MPP3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CCDC120 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C8orf74 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GORASP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| RSPH1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |
| ENST00000644631 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 6
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.6 + PDB: 无 | pLDDT=91.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle, secretory vesicle, acrosome;  / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 8 + 6 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. MORN2 — MORN repeat-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小79 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q502X0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188010-MORN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MORN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q502X0
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 21:53:13
