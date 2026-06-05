---
type: protein-evaluation
gene: "GMNC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GMNC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GMNC / GEMC1 |
| 蛋白名称 | Geminin coiled-coil domain-containing protein 1 |
| 蛋白大小 | 334 aa / 37.9 kDa |
| UniProt ID | A6NCL1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 334 aa / 37.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.5; PDB: 5C9N, 9HIU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR059237 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular region (GO:0005576)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 53 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GEMC1 |

**关键文献**:
1. Genome-wide meta-analysis for Alzheimer's disease cerebrospinal fluid biomarkers.. *Acta neuropathologica*. PMID: 36066633
2. Multiciliated cells: Development, functions and disease relevance.. *Seminars in cell & developmental biology*. PMID: 41067115
3. Gmnc Is a Master Regulator of the Multiciliated Cell Differentiation Program.. *Current biology : CB*. PMID: 26778655
4. Collection of trace amounts of DNA/mRNA molecules using genomagnetic nanocapturers.. *Analytical chemistry*. PMID: 14570200
5. Repurposing of the multiciliation gene regulatory network in fate specification of Cajal-Retzius neurons.. *Developmental cell*. PMID: 37321213

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.5 |
| 高置信度残基 (pLDDT>90) 占比 | 17.4% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 21.3% |
| 低置信 (pLDDT<50) 占比 | 48.5% |
| 有序区域 (pLDDT>70) 占比 | 30.3% |
| 可用 PDB 条目 | 5C9N, 9HIU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.5），有序残基占 30.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR059237 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCIDAS | 0.901 | 0.000 | — |
| E2F5 | 0.898 | 0.000 | — |
| TOPBP1 | 0.749 | 0.000 | — |
| E2F4 | 0.711 | 0.000 | — |
| OSTN | 0.689 | 0.000 | — |
| FOXJ1 | 0.686 | 0.000 | — |
| CCNO | 0.666 | 0.000 | — |
| RFX2 | 0.643 | 0.000 | — |
| TICRR | 0.631 | 0.000 | — |
| DEUP1 | 0.622 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCNE1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.5 + PDB: 5C9N, 9HIU | pLDDT=59.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GMNC — Geminin coiled-coil domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NCL1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205835-GMNC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GMNC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NCL1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NCL1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
