---
type: protein-evaluation
gene: "VOPP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## VOPP1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VOPP1 / ECOP, GASP |
| 蛋白名称 | WW domain binding protein VOPP1 |
| 蛋白大小 | 172 aa / 19.2 kDa |
| UniProt ID | Q96AW1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasmic vesicle membrane; Late endosome membrane; Lysoso |
| 蛋白大小 | 8/10 | ×1 | 8 | 172 aa / 19.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026229 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasmic vesicle membrane; Late endosome membrane; Lysosome membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasmic vesicle membrane (GO:0030659)
- endosome (GO:0005768)
- late endosome (GO:0005770)
- late endosome membrane (GO:0031902)
- lysosomal membrane (GO:0005765)
- lysosome (GO:0005764)
- organelle membrane (GO:0031090)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ECOP, GASP |

**关键文献**:
1. Intracellular localization of GASP/ECOP/VOPP1.. *Journal of molecular histology*. PMID: 20571887
2. Epidermal growth factor receptor-coamplified and overexpressed protein (VOPP1) is a putative oncogene in gastric cancer.. *Clinical and experimental medicine*. PMID: 25398664
3. VOPP1 as a Novel Susceptibility Gene in Rheumatoid Arthritis: Insights Into Its Mechanisms From Mendelian Randomization and Experimental Validation.. *Journal of inflammation research*. PMID: 40771899
4. VOPP1 promotes breast tumorigenesis by interacting with the tumor suppressor WWOX.. *BMC biology*. PMID: 30285739
5. Identification of Key eRNAs for Spinal Cord Injury by Integrated Multinomial Bioinformatics Analysis.. *Frontiers in cell and developmental biology*. PMID: 34708039

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.6 |
| 高置信度残基 (pLDDT>90) 占比 | 2.3% |
| 置信残基 (pLDDT 70-90) 占比 | 39.5% |
| 中等置信 (pLDDT 50-70) 占比 | 33.7% |
| 低置信 (pLDDT<50) 占比 | 24.4% |
| 有序区域 (pLDDT>70) 占比 | 41.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.6），有序残基占 41.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026229 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LANCL2 | 0.682 | 0.000 | — |
| TMEM207 | 0.617 | 0.000 | — |
| SEC61G | 0.613 | 0.000 | — |
| VWA7 | 0.613 | 0.000 | — |
| EGFR | 0.600 | 0.078 | — |
| WWOX | 0.568 | 0.421 | — |
| WBP1 | 0.567 | 0.000 | — |
| VSTM2A | 0.529 | 0.000 | — |
| C7orf25 | 0.499 | 0.000 | — |
| SEPTIN14 | 0.495 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CRIP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MAP7D1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| C8orf33 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GLYAT | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| LAMTOR5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HMOX2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| C8orf30A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SNAPIN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| STMN2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TAC3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.6 + PDB: 无 | pLDDT=65.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle membrane; Late endosome membra / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. VOPP1 — WW domain binding protein VOPP1，非常新颖，仅有少数基础研究。
2. 蛋白大小172 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AW1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154978-VOPP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VOPP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AW1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
