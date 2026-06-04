---
type: protein-evaluation
gene: "GLG1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GLG1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLG1 / CFR1, ESL1, MG160 |
| 蛋白名称 | Golgi apparatus protein 1 |
| 蛋白大小 | 1179 aa / 134.6 kDa |
| UniProt ID | Q92896 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; 额外: Mid piece, Principal piece, End piece; UniProt: Golgi apparatus membrane; Golgi outpost; Cytoplasm, cytoskel |
| 蛋白大小 | 8/10 | ×1 | 8 | 1179 aa / 134.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001893, IPR017873, IPR039728; Pfam: PF00839 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Mid piece, Principal piece, End piece | Supported |
| UniProt | Golgi apparatus membrane; Golgi outpost; Cytoplasm, cytoskeleton, microtubule organizing center | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- extracellular matrix (GO:0031012)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)
- microtubule organizing center (GO:0005815)
- plasma membrane (GO:0005886)
- sperm end piece (GO:0097229)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CFR1, ESL1, MG160 |

**关键文献**:
1. Glycogen Granules Are Degraded by Non-Selective Autophagy in Nitrogen-Starved Komagataella phaffii.. *Cells*. PMID: 38534311
2. FUT3 promotes gastric cancer cell migration by synthesizing Lea on ITGA6 and GLG1, affecting adhesion and vesicle distribution.. *Life sciences*. PMID: 39477144
3. Engineered MSCs enable bone marrow-targeted immunomodulation.. *Cell stem cell*. PMID: 41895281
4. Comparative proteomics analysis of gastric cancer stem cells.. *PloS one*. PMID: 25379943
5. Taurine promotes estrogen synthesis by regulating microRNA-7a2 in mice ovarian granulosa cells.. *Biochemical and biophysical research communications*. PMID: 35988296

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.9 |
| 高置信度残基 (pLDDT>90) 占比 | 26.4% |
| 置信残基 (pLDDT 70-90) 占比 | 50.7% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 10.5% |
| 有序区域 (pLDDT>70) 占比 | 77.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.9，有序区 77.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001893, IPR017873, IPR039728; Pfam: PF00839 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SELE | 0.999 | 0.304 | — |
| SELP | 0.983 | 0.058 | — |
| SELPLG | 0.886 | 0.000 | — |
| F11R | 0.797 | 0.000 | — |
| FGF2 | 0.734 | 0.097 | — |
| VCAM1 | 0.700 | 0.000 | — |
| SELL | 0.693 | 0.052 | — |
| CD44 | 0.675 | 0.000 | — |
| OSBPL8 | 0.619 | 0.606 | — |
| SPN | 0.618 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| vig2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mnat9 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| IntS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| SQSTM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| env | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| HSP78 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| ENSP00000405984.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.9 + PDB: 无 | pLDDT=77.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Golgi outpost; Cytoplasm / Golgi apparatus; 额外: Mid piece, Principal piece, E | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GLG1 — Golgi apparatus protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1179 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92896
- Protein Atlas: https://www.proteinatlas.org/ENSG00000090863-GLG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92896
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
