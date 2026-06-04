---
type: protein-evaluation
gene: "CD1E"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CD1E 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CD1E / — |
| 蛋白名称 | T-cell surface glycoprotein CD1e, membrane-associated |
| 蛋白大小 | 388 aa / 43.6 kDa |
| UniProt ID | P15812 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoli; UniProt: Golgi apparatus membrane; Early endosome; Late endosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 388 aa / 43.6 kDa |
| 研究新颖性 | 7/10 | ×5 | 35 | PubMed strict=61 篇 |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=81.5; PDB: 暂无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007110, IPR036179, IPR013783, IPR003597, IPR050208, IPR011161, IPR037055, IPR011162; Pfam: PF07654, PF16497 |
| PPI 网络 | 9/10 | ×3 | 27 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **127.2/180** | |
| **归一化总分 (÷1.83)** | | | **69.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Supported |
| UniProt | Golgi apparatus membrane | —
| UniProt | Early endosome | —
| UniProt | Late endosome | —
| UniProt | Lysosome lumen | —

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- early endosome (GO:0005769) [IEA:UniProtKB-SubCell]
- external side of plasma membrane (GO:0009897) [IBA:GO_Central]
- extracellular space (GO:0005615) [IBA:GO_Central]
- Golgi apparatus (GO:0005794) [IDA:HPA]
- Golgi membrane (GO:0000139) [IEA:UniProtKB-SubCell]
- late endosome (GO:0005770) [IEA:UniProtKB-SubCell]
- lysosomal lumen (GO:0043202) [IEA:UniProtKB-SubCell]
- nucleolus (GO:0005730) [IDA:HPA]

**结论**: HPA: Golgi apparatus; 额外: Nucleoli; UniProt: Golgi apparatus membrane; Early endosome; Late endosome; Lysosome lumen

#### 3.2 蛋白大小评估

**评价**: 388 aa / 43.6 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 61 |
| PubMed 搜索链接 | [CD1E PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CD1E) |

**关键文献**:
暂无文献记录。

**评价**: 有一定研究基础。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.5 |
| 高置信度残基 (pLDDT>90) 占比 | 66.5% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.5% |
| 低置信 (pLDDT<50) 占比 | 17.0% |
| 有序区域 (pLDDT>70) 占比 | 74.5% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007110, IPR036179, IPR013783, IPR003597, IPR050208, IPR011161, IPR037055, IPR011162; Pfam: PF07654, PF16497 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD1B | 0.998 | 0.000 | — |
| CD207 | 0.956 | 0.000 | — |
| CD83 | 0.916 | 0.000 | — |
| CD68 | 0.906 | 0.000 | — |
| B2M | 0.868 | 0.506 | — |
| CD86 | 0.806 | 0.000 | — |
| CD4 | 0.793 | 0.000 | — |
| CD80 | 0.789 | 0.000 | — |
| CD1A | 0.788 | 0.000 | — |
| CD5 | 0.781 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MIA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| SUSD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| MAN1A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PLXNA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| C1QL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| SEMA4F | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| CANX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| MAN2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| FCGRT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| B2M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=81.5, v6 | 预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Early endosome; Late endosome; Lysosome lumen / Golgi apparatus | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**归一化总分**: 69.5/100

**核心优势**:
1. CD1E — T-cell surface glycoprotein CD1e, membrane-associated，较新颖，PubMed 61 篇。
2. 蛋白大小388 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold pLDDT=81.5，结构预测质量高。

**风险/不确定性**:
1. 核定位信号较弱，多源数据支持有限。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P15812
- Protein Atlas: https://www.proteinatlas.org/search/CD1E
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CD1E
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P15812
- STRING: https://string-db.org/network/9606.CD1E
- Packet data timestamp: 2026-06-03 04:44:41
