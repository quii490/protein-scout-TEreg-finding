---
type: protein-evaluation
gene: "MCRIP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MCRIP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MCRIP2 / C16orf14, FAM195A |
| 蛋白名称 | MAPK regulated corepressor interacting protein 2 |
| 蛋白大小 | 160 aa / 17.8 kDa |
| UniProt ID | Q9BUT9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, Stress granule; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 160 aa / 17.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029428; Pfam: PF14799 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, Stress granule; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf14, FAM195A |

**关键文献**:
1. Cysteine Rich Intestinal Protein 2 is a copper-responsive regulator of skeletal muscle differentiation.. *bioRxiv : the preprint server for biology*. PMID: 38746126
2. ATXN2L primarily interacts with NUFIP2, the absence of ATXN2L results in NUFIP2 depletion, and the ATXN2-polyQ expansion triggers NUFIP2 accumulation.. *Neurobiology of disease*. PMID: 40220918
3. Cysteine Rich Intestinal Protein 2 is a copper-responsive regulator of skeletal muscle differentiation and metal homeostasis.. *PLoS genetics*. PMID: 39637238
4. Patterns of allele frequency differences among domestic cat breeds assessed by a 63K SNP array.. *PloS one*. PMID: 33630878
5. Cysteine rich intestinal protein 2 links copper homeostasis to translational regulation in primary myoblasts.. *microPublication biology*. PMID: 41426955

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.3 |
| 高置信度残基 (pLDDT>90) 占比 | 10.0% |
| 置信残基 (pLDDT 70-90) 占比 | 29.4% |
| 中等置信 (pLDDT 50-70) 占比 | 25.6% |
| 低置信 (pLDDT<50) 占比 | 35.0% |
| 有序区域 (pLDDT>70) 占比 | 39.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.3），有序残基占 39.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029428; Pfam: PF14799 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DDX6 | 0.778 | 0.735 | — |
| LSM12 | 0.745 | 0.737 | — |
| CCNDBP1 | 0.622 | 0.621 | — |
| ATXN2L | 0.617 | 0.482 | — |
| CYC1 | 0.583 | 0.000 | — |
| COMTD1 | 0.541 | 0.000 | — |
| NDUFV1 | 0.538 | 0.000 | — |
| NDUFS8 | 0.516 | 0.000 | — |
| FAM98A | 0.441 | 0.000 | — |
| ZNF280D | 0.419 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PIK3CD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EEF1G | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| env | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| CCNDBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PHC3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:27705803|imex:IM-21659 |
| MPHOSPH8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CASC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PAPSS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DDX6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LSM12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.3 + PDB: 无 | pLDDT=64.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, Stress granule; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MCRIP2 — MAPK regulated corepressor interacting protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小160 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BUT9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172366-MCRIP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MCRIP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BUT9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
