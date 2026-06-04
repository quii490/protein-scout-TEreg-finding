---
type: protein-evaluation
gene: "FAM163B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM163B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM163B / C9orf166 |
| 蛋白名称 | Protein FAM163B |
| 蛋白大小 | 166 aa / 18.2 kDa |
| UniProt ID | P0C2L3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies, Plasma membrane, Cytosol; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 166 aa / 18.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029379, IPR040280; Pfam: PF15069 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Plasma membrane, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf166 |

**关键文献**:
1. Identification of Breast Cancer Metastasis Markers from Gene Expression Profiles Using Machine Learning Approaches.. *Genes*. PMID: 37761960
2. Neural-Specific Expression and Membrane Localization of FAM163B Regulates SAP97 Expression.. *Journal of neurochemistry*. PMID: 40999800
3. Genome-wide meta-analysis associates GPSM1 with type 2 diabetes, a plausible gene involved in skeletal muscle function.. *Journal of human genetics*. PMID: 31959871

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.6 |
| 高置信度残基 (pLDDT>90) 占比 | 12.7% |
| 置信残基 (pLDDT 70-90) 占比 | 6.6% |
| 中等置信 (pLDDT 50-70) 占比 | 35.5% |
| 低置信 (pLDDT<50) 占比 | 45.2% |
| 有序区域 (pLDDT>70) 占比 | 19.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.6），有序残基占 19.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029379, IPR040280; Pfam: PF15069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZC2HC1B | 0.735 | 0.000 | — |
| ZDHHC22 | 0.689 | 0.000 | — |
| SEC22C | 0.644 | 0.000 | — |
| VWC2L | 0.576 | 0.000 | — |
| CHRNB3 | 0.541 | 0.000 | — |
| SARDH | 0.512 | 0.000 | — |
| LRRTM2 | 0.502 | 0.000 | — |
| CACFD1 | 0.493 | 0.000 | — |
| HTR5A | 0.466 | 0.000 | — |
| SNCB | 0.433 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DLG1 | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| DLG3 | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| SCRIB | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| UBQLN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PPP3CA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CAMK2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CAMK2G | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CAMK2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| QNG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DPP9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.6 + PDB: 无 | pLDDT=57.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nuclear bodies, Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM163B — Protein FAM163B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小166 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0C2L3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196990-FAM163B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM163B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0C2L3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
