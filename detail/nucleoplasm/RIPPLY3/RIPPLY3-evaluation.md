---
type: protein-evaluation
gene: "RIPPLY3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RIPPLY3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RIPPLY3 / DSCR6 |
| 蛋白名称 | Protein ripply3 |
| 蛋白大小 | 190 aa / 20.4 kDa |
| UniProt ID | P57055 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 190 aa / 20.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028127; Pfam: PF14998 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DSCR6 |

**关键文献**:
1. Ripply3 overdosage induces mid-face shortening through Tbx1 downregulation in Down syndrome models.. *PLoS genetics*. PMID: 40982554
2. Pre-mandibular pharyngeal pouches in early non-teleost fish embryos.. *Proceedings. Biological sciences*. PMID: 37700650
3. HDAC1-mediated repression of the retinoic acid-responsive gene ripply3 promotes second heart field development.. *PLoS genetics*. PMID: 31091225
4. RIPPLY3 is a retinoic acid-inducible repressor required for setting the borders of the pre-placodal ectoderm.. *Development (Cambridge, England)*. PMID: 22354841
5. Identification of a 3-Gene Prognostic Index for Papillary Thyroid Carcinoma.. *Frontiers in molecular biosciences*. PMID: 35372518

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.4 |
| 高置信度残基 (pLDDT>90) 占比 | 6.8% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 47.4% |
| 低置信 (pLDDT<50) 占比 | 28.9% |
| 有序区域 (pLDDT>70) 占比 | 23.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.4），有序残基占 23.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028127; Pfam: PF14998 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TBX1 | 0.625 | 0.513 | — |
| TIFA | 0.600 | 0.600 | — |
| IQANK1 | 0.529 | 0.000 | — |
| INSM1 | 0.514 | 0.000 | — |
| NEUROG3 | 0.453 | 0.000 | — |
| PIGP | 0.451 | 0.000 | — |
| HMG20A | 0.445 | 0.000 | — |
| PPY | 0.426 | 0.000 | — |
| ARX | 0.423 | 0.000 | — |
| FAM237B | 0.418 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PSMB1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| INCA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MCRS1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TIFA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ORC2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CEP76 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TLE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TBX1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:30241482|imex:IM-27129 |
| A2ML1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 15
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.4 + PDB: 无 | pLDDT=60.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 12 + 15 interactions | 数据充分 |

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
1. RIPPLY3 — Protein ripply3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P57055
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183145-RIPPLY3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RIPPLY3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P57055
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P57055-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
