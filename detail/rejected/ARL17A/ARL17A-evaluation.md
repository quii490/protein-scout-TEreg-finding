---
type: protein-evaluation
gene: "ARL17A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ARL17A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARL17A / ARF1P2, ARL17P1 |
| 蛋白名称 | Putative ADP-ribosylation factor-like protein 17A |
| 蛋白大小 | 177 aa / 19.4 kDa |
| UniProt ID | Q8IVW1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 177 aa / 19.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031687, IPR027417, IPR024156, IPR006689; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.5/180** | |
| **归一化总分** | | | **59.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- Golgi apparatus (GO:0005794)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARF1P2, ARL17P1 |

**关键文献**:
1. Genetic architectures of the human hippocampus and those involved in neuropsychiatric traits.. *BMC medicine*. PMID: 39394562
2. Cell-Type-Specific Causal Inference Unveils Novel Targets for Parkinson's Disease.. *Movement disorders : official journal of the Movement Disorder Society*. PMID: 41684331
3. Leveraging Alzheimer's Disease Omics to Identify Pleiotropic Genes Contributing to Neurodegeneration in Primary Open-Angle Glaucoma.. *Molecular neurobiology*. PMID: 40411683
4. Association of Gene Expression and Tremor Network Structure.. *Movement disorders : official journal of the Movement Disorder Society*. PMID: 38769620
5. Gene expression, methylation and neuropathology correlations at progressive supranuclear palsy risk loci.. *Acta neuropathologica*. PMID: 27115769

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 31.6% |
| 中等置信 (pLDDT 50-70) 占比 | 14.7% |
| 低置信 (pLDDT<50) 占比 | 53.7% |
| 有序区域 (pLDDT>70) 占比 | 31.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=53.4），有序残基占 31.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031687, IPR027417, IPR024156, IPR006689; Pfam: PF00025, PF15840 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KANSL1 | 0.769 | 0.000 | — |
| LRRC37A2 | 0.742 | 0.100 | — |
| LRRC37A | 0.731 | 0.100 | — |
| LRRC37A3 | 0.729 | 0.100 | — |
| ARHGAP27 | 0.583 | 0.097 | — |
| ITSN2 | 0.536 | 0.497 | — |
| ITSN1 | 0.535 | 0.497 | — |
| PLEKHM1 | 0.512 | 0.000 | — |
| SPPL2C | 0.479 | 0.000 | — |
| GBF1 | 0.477 | 0.398 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RNF19B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LHFPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ARL17B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| TMEM74 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CX3CL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KCNE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MICB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PIPSL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FTL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.4 + PDB: 无 | pLDDT=53.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ARL17A — Putative ADP-ribosylation factor-like protein 17A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小177 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=53.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IVW1
- Protein Atlas: https://www.proteinatlas.org/search/ARL17A
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARL17A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IVW1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ARL17A/ARL17A-PAE.png]]
