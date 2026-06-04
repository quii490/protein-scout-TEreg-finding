---
type: protein-evaluation
gene: "TEX264"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TEX264 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEX264 / ZSIG11 |
| 蛋白名称 | Testis-expressed protein 264 |
| 蛋白大小 | 313 aa / 34.2 kDa |
| UniProt ID | Q9Y6I9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; UniProt: Endoplasmic reticulum membrane; Cytoplasmic vesicle, autopha |
| 蛋白大小 | 10/10 | ×1 | 10 | 313 aa / 34.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.1; PDB: 7VEC, 7VED |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011256 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Supported |
| UniProt | Endoplasmic reticulum membrane; Cytoplasmic vesicle, autophagosome; Cytoplasm, cytosol; Nucleus; Chr... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- autophagosome membrane (GO:0000421)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular region (GO:0005576)
- nucleus (GO:0005634)
- platelet alpha granule lumen (GO:0031093)
- replication fork (GO:0005657)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 46 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ZSIG11 |

**关键文献**:
1. Therapeutic regulation of autophagy in hepatic metabolism.. *Acta pharmaceutica Sinica. B*. PMID: 35127371
2. Intrinsically Disordered Protein TEX264 Mediates ER-phagy.. *Molecular cell*. PMID: 31006538
3. Reticulophagy and viral infection.. *Autophagy*. PMID: 39394962
4. ATF4 links ER stress with reticulophagy in glioblastoma cells.. *Autophagy*. PMID: 33111629
5. TEX264 drives selective autophagy of DNA lesions to promote DNA repair and cell survival.. *Cell*. PMID: 39265577

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.1 |
| 高置信度残基 (pLDDT>90) 占比 | 58.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 31.0% |
| 有序区域 (pLDDT>70) 占比 | 67.4% |
| 可用 PDB 条目 | 7VEC, 7VED |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7VEC, 7VED）+ AlphaFold高质量预测（pLDDT=75.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011256 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GABARAP | 0.832 | 0.070 | — |
| CCPG1 | 0.815 | 0.000 | — |
| SEC62 | 0.798 | 0.082 | — |
| ATL3 | 0.789 | 0.000 | — |
| RETREG1 | 0.772 | 0.000 | — |
| RTN3 | 0.729 | 0.000 | — |
| GABARAPL2 | 0.717 | 0.082 | — |
| TMEM79 | 0.681 | 0.675 | — |
| CALCOCO1 | 0.674 | 0.000 | — |
| CD300C | 0.589 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BUB1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TMEM79 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| CREB3L1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| GPR42 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ARL13B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SMIM3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSPAN12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LHFPL5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| COQ9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CLDN2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.1 + PDB: 7VEC, 7VED | pLDDT=75.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Cytoplasmic vesicl / Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TEX264 — Testis-expressed protein 264，非常新颖，仅有少数基础研究。
2. 蛋白大小313 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6I9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164081-TEX264/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEX264
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6I9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
