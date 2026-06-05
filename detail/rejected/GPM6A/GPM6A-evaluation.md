---
type: protein-evaluation
gene: "GPM6A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPM6A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPM6A / M6A |
| 蛋白名称 | Neuronal membrane glycoprotein M6-a |
| 蛋白大小 | 278 aa / 31.2 kDa |
| UniProt ID | P51674 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell projection, axon; Cell projection, growt |
| 蛋白大小 | 10/10 | ×1 | 10 | 278 aa / 31.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001614, IPR018237; Pfam: PF01275 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cell projection, axon; Cell projection, growth cone; Cell projection, dendritic spine... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axonal growth cone (GO:0044295)
- dendritic spine (GO:0043197)
- extracellular exosome (GO:0070062)
- extracellular vesicle (GO:1903561)
- filopodium (GO:0030175)
- glutamatergic synapse (GO:0098978)
- neuron projection (GO:0043005)
- neuronal cell body (GO:0043025)

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
| AlphaFold 平均 pLDDT | 82.7 |
| 高置信度残基 (pLDDT>90) 占比 | 43.2% |
| 置信残基 (pLDDT 70-90) 占比 | 37.8% |
| 中等置信 (pLDDT 50-70) 占比 | 14.0% |
| 低置信 (pLDDT<50) 占比 | 5.0% |
| 有序区域 (pLDDT>70) 占比 | 81.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.7，有序区 81.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001614, IPR018237; Pfam: PF01275 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLCN3 | 0.840 | 0.000 | — |
| SYP | 0.752 | 0.129 | — |
| SYN1 | 0.714 | 0.420 | — |
| OPRM1 | 0.670 | 0.098 | — |
| GRIA2 | 0.588 | 0.389 | — |
| TIAM2 | 0.586 | 0.000 | — |
| MAPT | 0.570 | 0.408 | — |
| SNAP25 | 0.567 | 0.249 | — |
| UPK1B | 0.561 | 0.000 | — |
| RAP2A | 0.560 | 0.090 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| NUFIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ADGRG5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EDA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAAF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARMC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HAX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSPAN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GP1BB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MGAT5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.7 + PDB: 无 | pLDDT=82.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cell projection, axon; Cell project / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPM6A — Neuronal membrane glycoprotein M6-a，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小278 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51674
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150625-GPM6A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPM6A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51674
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P51674-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
