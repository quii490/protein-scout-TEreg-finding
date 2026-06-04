---
type: protein-evaluation
gene: "SNUPN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SNUPN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SNUPN / RNUT1, SPN1 |
| 蛋白名称 | Snurportin-1 |
| 蛋白大小 | 360 aa / 41.1 kDa |
| UniProt ID | O95149 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 360 aa / 41.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.8; PDB: 1XK5, 2P8Q, 2Q5D, 2QNA, 3GB8, 3GJX, 3LWW |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002652, IPR017336, IPR024721, IPR047857; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- NLS-dependent protein nuclear import complex (GO:0042564)
- nuclear pore (GO:0005643)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 58 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNUT1, SPN1 |

**关键文献**:
1. Uncovering novel protein pathways regulating bioavailable testosterone through sex hormone-binding globulin.. *Computational biology and chemistry*. PMID: 41161126
2. Biallelic variants in SNUPN cause a limb girdle muscular dystrophy with myofibrillar-like features.. *Brain : a journal of neurology*. PMID: 38366623
3. SNUPN-Related Muscular Dystrophy: Novel Phenotypic, Pathological and Functional Protein Insights.. *Annals of clinical and translational neurology*. PMID: 41054283
4. Pinpointing novel targets for osteoarthritis: A comprehensive cross-omics integration analysis.. *Medicine*. PMID: 40859561
5. Identifying therapeutic targets for breast cancer: insights from systematic Mendelian randomization analysis.. *Frontiers in oncology*. PMID: 38887235

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.8 |
| 高置信度残基 (pLDDT>90) 占比 | 58.1% |
| 置信残基 (pLDDT 70-90) 占比 | 22.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.1% |
| 低置信 (pLDDT<50) 占比 | 13.3% |
| 有序区域 (pLDDT>70) 占比 | 80.6% |
| 可用 PDB 条目 | 1XK5, 2P8Q, 2Q5D, 2QNA, 3GB8, 3GJX, 3LWW, 3NBY, 3NBZ, 3NC0 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1XK5, 2P8Q, 2Q5D, 2QNA, 3GB8, 3GJX, 3LWW, 3NBY, 3NBZ, 3NC0）+ AlphaFold极高置信度预测（pLDDT=82.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002652, IPR017336, IPR024721, IPR047857; Pfam: PF11538, PF21974 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XPO1 | 0.999 | 0.983 | — |
| KPNB1 | 0.998 | 0.952 | — |
| RAN | 0.985 | 0.938 | — |
| NUP214 | 0.964 | 0.900 | — |
| SNRPB | 0.901 | 0.605 | — |
| SNRPE | 0.880 | 0.696 | — |
| DDX20 | 0.863 | 0.292 | — |
| TOE1 | 0.860 | 0.830 | — |
| MEX3B | 0.849 | 0.363 | — |
| SNRPD1 | 0.844 | 0.589 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PEX5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ENO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PAFAH1B2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BTBD8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RPL17 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TNNT3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GCNT3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TOE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLEC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.8 + PDB: 1XK5, 2P8Q, 2Q5D, 2QNA, 3GB8,  | pLDDT=82.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm, Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SNUPN — Snurportin-1，非常新颖，仅有少数基础研究。
2. 蛋白大小360 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95149
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169371-SNUPN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SNUPN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95149
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
