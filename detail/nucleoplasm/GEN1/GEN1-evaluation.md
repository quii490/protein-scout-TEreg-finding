---
type: protein-evaluation
gene: "GEN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GEN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GEN1 |
| 蛋白名称 | Flap endonuclease GEN homolog 1 |
| 蛋白大小 | 908 aa / 102.9 kDa |
| UniProt ID | Q17RS7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 908 aa / 102.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=69 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.2; PDB: 5T9J |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036279, IPR041012, IPR008918, IPR029060, IPR006 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.0/180** | |
| **归一化总分** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 69 |
| PubMed broad count | 215 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. GEN1 regulates cell proliferation, migration, apoptosis and ferroptosis in gastric cancer.. *World journal of gastrointestinal oncology*. PMID: 40837761
2. GEN1 Endonuclease: Purification and Nuclease Assays.. *Methods in enzymology*. PMID: 29458773
3. Robo2 and Gen1 Coregulate Ureteric Budding by Activating the MAPK/ERK Signaling Pathway in Mice.. *Frontiers in medicine*. PMID: 35071283
4. Molecular Profiling of Sinonasal Adenoid Cystic Carcinoma: Canonical and Noncanonical Gene Fusions and Mutation.. *The American journal of surgical pathology*. PMID: 39760648
5. Analysis of GEN1 as a Breast Cancer Susceptibility Gene in Polish Women.. *International journal of molecular sciences*. PMID: 40649769

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.2 |
| 高置信度残基 (pLDDT>90) 占比 | 28.4% |
| 置信残基 (pLDDT 70-90) 占比 | 18.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 45.6% |
| 有序区域 (pLDDT>70) 占比 | 46.6% |
| 可用 PDB 条目 | 5T9J |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.2），有序残基占 46.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036279, IPR041012, IPR008918, IPR029060, IPR006086; Pfam: PF18704, PF00867, PF00752 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CYCA2-1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| CYCA2-3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| CYCA3-4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20706207|imex:IM-17301 |
| CEP135 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| ODF2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| TNFRSF1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PLOD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HUNK | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |
| YWHAH | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |
| YWHAG | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 11
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.2 + PDB: 5T9J | pLDDT=61.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 11 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GEN1 — Flap endonuclease GEN homolog 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小908 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 69 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q17RS7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178295-GEN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GEN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q17RS7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
