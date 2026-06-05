---
type: protein-evaluation
gene: "FAM198A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM198A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM198A / C3orf41, FAM198A |
| 蛋白名称 | Golgi-associated kinase 1A |
| 蛋白大小 | 575 aa / 63.6 kDa |
| UniProt ID | Q9UFP1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles; UniProt: Secreted; Endoplasmic reticulum; Golgi apparatus; Membrane,  |
| 蛋白大小 | 10/10 | ×1 | 10 | 575 aa / 63.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029207; Pfam: PF15051 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Supported |
| UniProt | Secreted; Endoplasmic reticulum; Golgi apparatus; Membrane, caveola | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- caveola (GO:0005901)
- endoplasmic reticulum (GO:0005783)
- extracellular region (GO:0005576)
- Golgi apparatus (GO:0005794)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf41, FAM198A |

**关键文献**:
1. Fam198a, a member of secreted kinase, secrets through caveolae biogenesis pathway.. *Acta biochimica et biophysica Sinica*. PMID: 30188967

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.4 |
| 高置信度残基 (pLDDT>90) 占比 | 46.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 38.6% |
| 有序区域 (pLDDT>70) 占比 | 54.1% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.4），有序残基占 54.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029207; Pfam: PF15051 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAM20B | 0.714 | 0.000 | — |
| FAM20C | 0.714 | 0.000 | — |
| FJX1 | 0.683 | 0.000 | — |
| FAM20A | 0.665 | 0.000 | — |
| ZNF662 | 0.606 | 0.000 | — |
| RNF225 | 0.606 | 0.000 | — |
| ARMC7 | 0.506 | 0.000 | — |
| OR4D6 | 0.474 | 0.000 | — |
| HEXD | 0.448 | 0.000 | — |
| ALG10B | 0.418 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LYZL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IFNE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LYPD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CEACAM8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLEC12B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SCGB2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LLCFC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 7
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.4 + PDB: 无 | pLDDT=68.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted; Endoplasmic reticulum; Golgi apparatus;  / Vesicles | 一致 |
| PPI | STRING + IntAct | 12 + 7 interactions | 数据充分 |

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
1. FAM198A — Golgi-associated kinase 1A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小575 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UFP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144649-GASK1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM198A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UFP1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UFP1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
