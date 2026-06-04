---
type: protein-evaluation
gene: "MLXIPL"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, re-evaluation, recovery]
status: scored
category: nucleoplasm
normalized_score: 43.4
raw_score: 79.5
nuclear_score: 7
---

## MLXIPL 核蛋白评估报告 (Full Re-evaluation)


### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MLXIPL / BHLHD14, MIO, WBSCR14 |
| 蛋白名称 | Carbohydrate-responsive element-binding protein |
| 蛋白大小 | 852 aa / 93.1 kDa |
| UniProt ID | Q9NP71 |
| PubMed (strict) | 127 |
| PubMed (broad) | 587 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 852 aa / 93.1 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=127 篇 (>100, rejected) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.9，PDB: 6MJL, 6YGJ, 8BTQ, 8BWE, 8BWH, 8C1Y, 9GCP |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR052207; Pfam: PF00010 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners, IntAct 9 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/183** | |
| **归一化总分** | | | **43.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持，部分数据源提示非核定位但核信号主导。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 127 |
| PubMed broad count | 587 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHD14, MIO, WBSCR14 |

**关键文献**:
1. Williams syndrome.. *Nature reviews. Disease primers*. PMID: 34140529
2. The ménage à trois of autophagy, lipid droplets and liver disease.. *Autophagy*. PMID: 33794741
3. Genetic susceptibility to caffeine intake and metabolism: a systematic review.. *Journal of translational medicine*. PMID: 39438936
4. Genetic basis of hypertriglyceridemia.. *Clinica e investigacion en arteriosclerosis : publicacion oficial de la Sociedad Espanola de Arteriosclerosis*. PMID: 39672669
5. A genome-first approach to variants in MLXIPL and their association with hepatic steatosis and plasma lipids.. *Hepatology communications*. PMID: 38668731

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.9 |
| 高置信度残基 (pLDDT>90) 占比 | 15.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.1% |
| 低置信 (pLDDT<50) 占比 | 59.7% |
| 有序区域 (pLDDT>70) 占比 | 27.1% |
| 可用 PDB 条目 | 6MJL, 6YGJ, 8BTQ, 8BWE, 8BWH, 8C1Y, 9GCP |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量有限（pLDDT=53.9），有序残基占 27.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR052207; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MLXIP | 0.992 | 0.000 | — |
| MLX | 0.991 | 0.806 | — |
| PPARGC1B | 0.944 | 0.000 | — |
| TBL2 | 0.935 | 0.000 | — |
| MXD4 | 0.931 | 0.000 | — |
| OGT | 0.926 | 0.095 | — |
| YWHAB | 0.916 | 0.907 | — |
| ACLY | 0.911 | 0.000 | — |
| SREBF1 | 0.900 | 0.091 | — |
| LIPE | 0.900 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| MLX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| EVC2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| YWHAG | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |
| YWHAH | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |
| YWHAQ | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |
| SFN | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |

**已知复合体成员** (GO Cellular Component):
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.9 + PDB: 6MJL, 6YGJ, 8BTQ, 8BWE, 8BWH,  | pLDDT=53.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. MLXIPL — Carbohydrate-responsive element-binding protein，有一定研究基础，但仍存在niche空间。
2. 蛋白大小852 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 127 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=53.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NP71
- Protein Atlas: https://www.proteinatlas.org/ENSG00000009950-MLXIPL
- Protein Atlas Subcellular: https://www.proteinatlas.org/ENSG00000009950-MLXIPL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MLXIPL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NP71
- STRING: https://string-db.org/network
- IntAct: https://www.ebi.ac.uk/intact/search?query=MLXIPL
- Packet data timestamp: 2026-06-03 21:45:49

---

*本报告基于最新的 harvest packet 数据（2026-06-03 21:45:49），各数据库实时抓取。评分严格遵循 /180 加权评分体系：核定位×4 + 大小×1 + 新颖性×5 + 结构×3 + 结构域×2 + PPI×3 + 互证加分（max+3）。PubMed>100 或 核定位≤3 为 REJECTED。*
