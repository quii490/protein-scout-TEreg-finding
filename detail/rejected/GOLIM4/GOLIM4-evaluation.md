---
type: protein-evaluation
gene: "GOLIM4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GOLIM4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOLIM4 / GIMPC, GOLPH4, GPP130 |
| 蛋白名称 | Golgi integral membrane protein 4 |
| 蛋白大小 | 696 aa / 81.9 kDa |
| UniProt ID | O00461 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; UniProt: Golgi apparatus, Golgi stack membrane; Endosome membrane; Me |
| 蛋白大小 | 10/10 | ×1 | 10 | 696 aa / 81.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042336 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Enhanced |
| UniProt | Golgi apparatus, Golgi stack membrane; Endosome membrane; Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cis-Golgi network (GO:0005801)
- endocytic vesicle (GO:0030139)
- endosome membrane (GO:0010008)
- Golgi apparatus (GO:0005794)
- Golgi cisterna membrane (GO:0032580)
- Golgi lumen (GO:0005796)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GIMPC, GOLPH4, GPP130 |

**关键文献**:
1. Chromosomal 3q amplicon encodes essential regulators of secretory vesicles that drive secretory addiction in cancer.. *The Journal of clinical investigation*. PMID: 38662435
2. Targeting the secretory program of 3q-amplified lung cancers.. *The Journal of clinical investigation*. PMID: 40047887
3. Role of the AP-5 adaptor protein complex in late endosome-to-Golgi retrieval.. *PLoS biology*. PMID: 29381698
4. Monensin suppresses EMT-driven cancer cell motility by inducing Golgi pH-dependent exocytosis of GOLIM4.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40632561
5. Golgi integral membrane protein 4 manipulates cellular proliferation, apoptosis, and cell cycle in human head and neck cancer.. *Bioscience reports*. PMID: 30068697

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.6 |
| 高置信度残基 (pLDDT>90) 占比 | 37.9% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.2% |
| 低置信 (pLDDT<50) 占比 | 37.5% |
| 有序区域 (pLDDT>70) 占比 | 49.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.6），有序残基占 49.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042336 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STX5 | 0.847 | 0.000 | — |
| GOLGA5 | 0.781 | 0.000 | — |
| GOSR1 | 0.778 | 0.000 | — |
| COG3 | 0.746 | 0.000 | — |
| COG4 | 0.744 | 0.000 | — |
| COG8 | 0.744 | 0.000 | — |
| GOLPH3 | 0.734 | 0.094 | — |
| COG1 | 0.714 | 0.000 | — |
| COG2 | 0.701 | 0.000 | — |
| COG7 | 0.687 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| CD79B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRDN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HLA-DPA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC39A4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POMK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| B3GAT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FUT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.6 + PDB: 无 | pLDDT=67.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, Golgi stack membrane; Endosome me / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GOLIM4 — Golgi integral membrane protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小696 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00461
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173905-GOLIM4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOLIM4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00461
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
