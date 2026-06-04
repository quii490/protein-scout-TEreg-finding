---
type: protein-evaluation
gene: "PLEKHO2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLEKHO2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLEKHO2 / PLEKHQ1 |
| 蛋白名称 | Pleckstrin homology domain-containing family O member 2 |
| 蛋白大小 | 490 aa / 53.4 kDa |
| UniProt ID | Q8TD55 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 490 aa / 53.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011993, IPR001849, IPR043448; Pfam: PF00169 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PLEKHQ1 |

**关键文献**:
1. Single-Cell Sequencing Combined with Transcriptome Sequencing to Explore the Molecular Mechanisms Related to Skin Photoaging.. *Journal of inflammation research*. PMID: 39713718
2. PLEKHO2 is essential for M-CSF-dependent macrophage survival.. *Cellular signalling*. PMID: 28627369
3. PLEKHO2 inhibits TNFα-induced cell death by suppressing RIPK1 activation.. *Cell death & disease*. PMID: 34272357
4. Interrogation of macrophage-related prognostic signatures reveals a potential immune-mediated therapy strategy by histone deacetylase inhibition in glioma.. *Frontiers in oncology*. PMID: 40548122
5. The role of miR-4469 as a tumor suppressor regulating inflammatory cell infiltration in colorectal cancer.. *Computational and structural biotechnology journal*. PMID: 35891783

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.2 |
| 高置信度残基 (pLDDT>90) 占比 | 18.2% |
| 置信残基 (pLDDT 70-90) 占比 | 19.0% |
| 中等置信 (pLDDT 50-70) 占比 | 20.6% |
| 低置信 (pLDDT<50) 占比 | 42.2% |
| 有序区域 (pLDDT>70) 占比 | 37.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.2），有序残基占 37.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011993, IPR001849, IPR043448; Pfam: PF00169 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAPZB | 0.778 | 0.729 | — |
| CAPZA1 | 0.735 | 0.723 | — |
| IL10RB | 0.528 | 0.000 | — |
| THEMIS2 | 0.516 | 0.000 | — |
| FAM184A | 0.469 | 0.469 | — |
| CYTH4 | 0.453 | 0.000 | — |
| MAP3K6 | 0.444 | 0.422 | — |
| VEZT | 0.424 | 0.424 | — |
| FLAD1 | 0.420 | 0.420 | — |
| MYO1F | 0.411 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Capza1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCNC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CAPZA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAP3K6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZMYM6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAPZB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAAP100 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNF20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.2 + PDB: 无 | pLDDT=62.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane, Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLEKHO2 — Pleckstrin homology domain-containing family O member 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小490 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TD55
- Protein Atlas: https://www.proteinatlas.org/ENSG00000241839-PLEKHO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLEKHO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TD55
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
