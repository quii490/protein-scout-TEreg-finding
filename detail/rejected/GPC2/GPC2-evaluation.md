---
type: protein-evaluation
gene: "GPC2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPC2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPC2 |
| 蛋白名称 | Glypican-2 |
| 蛋白大小 | 579 aa / 62.8 kDa |
| UniProt ID | Q8N158 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Secreted, extracellular space |
| 蛋白大小 | 10/10 | ×1 | 10 | 579 aa / 62.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.0; PDB: 6WJL, 7T62 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001863, IPR019803; Pfam: PF01153 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Secreted, extracellular space | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- endoplasmic reticulum (GO:0005783)
- extracellular region (GO:0005576)
- Golgi lumen (GO:0005796)
- lysosomal lumen (GO:0043202)
- plasma membrane (GO:0005886)
- side of membrane (GO:0098552)
- synapse (GO:0045202)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.0 |
| 高置信度残基 (pLDDT>90) 占比 | 62.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 23.1% |
| 有序区域 (pLDDT>70) 占比 | 72.4% |
| 可用 PDB 条目 | 6WJL, 7T62 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6WJL, 7T62）+ AlphaFold高质量预测（pLDDT=79.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001863, IPR019803; Pfam: PF01153 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IGHV3-43D | 0.900 | 0.900 | — |
| GPC3 | 0.835 | 0.103 | — |
| MDK | 0.794 | 0.000 | — |
| SDC2 | 0.783 | 0.166 | — |
| SDC3 | 0.753 | 0.000 | — |
| SDC1 | 0.703 | 0.127 | — |
| CSPG5 | 0.680 | 0.000 | — |
| GPC4 | 0.674 | 0.000 | — |
| GLCE | 0.661 | 0.073 | — |
| NDST3 | 0.660 | 0.067 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HADHA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HPN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TMPRSS13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLEC12B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ST14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SYNGAP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |
| CACNA1C | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35063084|imex:IM-29773 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.0 + PDB: 6WJL, 7T62 | pLDDT=79.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Secreted, extracellular space / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPC2 — Glypican-2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小579 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N158
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213420-GPC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N158
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N158-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
