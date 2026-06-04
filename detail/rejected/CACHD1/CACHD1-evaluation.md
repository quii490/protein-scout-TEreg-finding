---
type: protein-evaluation
gene: "CACHD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CACHD1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CACHD1 / KIAA1573, VWCD1 |
| 蛋白名称 | VWFA and cache domain-containing protein 1 |
| 蛋白大小 | 1274 aa / 142.3 kDa |
| UniProt ID | Q5VU97 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1274 aa / 142.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051173, IPR029151, IPR002035, IPR036465 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- voltage-gated calcium channel complex (GO:0005891)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1573, VWCD1 |

**关键文献**:
1. Natural variation in gene expression and viral susceptibility revealed by neural progenitor cell villages.. *Cell stem cell*. PMID: 36796362
2. Cachd1 interacts with Wnt receptors and regulates neuronal asymmetry in the zebrafish brain.. *Science (New York, N.Y.)*. PMID: 38696577
3. The substrate repertoire of γ-secretase/presenilin.. *Seminars in cell & developmental biology*. PMID: 32616437
4. Cache Domain Containing 1 Is a Novel Marker of Non-Alcoholic Steatohepatitis-Associated Hepatocarcinogenesis.. *Cancers*. PMID: 33802238
5. α(2)δ-4 and Cachd1 Proteins Are Regulators of Presynaptic Functions.. *International journal of molecular sciences*. PMID: 36077281

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051173, IPR029151, IPR002035, IPR036465 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CACNA1B | 0.785 | 0.249 | — |
| CACNG1 | 0.775 | 0.531 | — |
| CACNA1E | 0.762 | 0.249 | — |
| CACNA1S | 0.761 | 0.249 | — |
| CACNA1A | 0.757 | 0.249 | — |
| CACNA1F | 0.750 | 0.249 | — |
| CACNB4 | 0.734 | 0.302 | — |
| CACNA1D | 0.719 | 0.249 | — |
| CACNB1 | 0.712 | 0.302 | — |
| CACNA1C | 0.702 | 0.249 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BICRAL | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| XAB2 | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| RANBP10 | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| ZMIZ1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| SLAMF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ST8SIA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM131B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SCGB1D1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMEM52B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BTRC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / 暂无HPA定位数据 | 一致 |
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
1. CACHD1 — VWFA and cache domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1274 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VU97
- Protein Atlas: https://www.proteinatlas.org/search/CACHD1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CACHD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VU97
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CACHD1/CACHD1-PAE.png]]
