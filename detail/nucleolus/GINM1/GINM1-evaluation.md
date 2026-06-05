---
type: protein-evaluation
gene: "GINM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GINM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GINM1 / C6orf72 |
| 蛋白名称 | Glycoprotein integral membrane protein 1 |
| 蛋白大小 | 330 aa / 36.8 kDa |
| UniProt ID | Q9NU53 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Plasma membrane; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 330 aa / 36.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042319 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Plasma membrane | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf72 |

**关键文献**:
1. Dissecting immune cell-specific genetics in migraine: a multi-omics framework for target discovery and therapeutic prioritization.. *The journal of headache and pain*. PMID: 41029193
2. Identification of genes associated with testicular germ cell tumor susceptibility through a transcriptome-wide association study.. *American journal of human genetics*. PMID: 39999848
3. Investigating the Causal Effects of Exercise-Induced Genes on Sarcopenia.. *International journal of molecular sciences*. PMID: 39409102
4. Urinary glycoproteomic profiling of non-muscle invasive and muscle invasive bladder carcinoma patients reveals distinct N-glycosylation pattern of CD44, MGAM, and GINM1.. *Oncotarget*. PMID: 32922663
5. Comprehensive analyses of biological function and tumor microenvironment with cuproptosis regulators and construction of a cuproptosis-related scoring system in thyroid cancer based on bioinformatics and experimental validation.. *Frontiers in genetics*. PMID: 41836061

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.1 |
| 高置信度残基 (pLDDT>90) 占比 | 43.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 35.2% |
| 有序区域 (pLDDT>70) 占比 | 59.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.1，有序区 59.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042319 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LCTL | 0.572 | 0.000 | — |
| S100A5 | 0.521 | 0.000 | — |
| JRKL | 0.518 | 0.000 | — |
| UBE2G1 | 0.517 | 0.000 | — |
| PIP4K2C | 0.507 | 0.000 | — |
| S100A14 | 0.488 | 0.000 | — |
| LRP11 | 0.467 | 0.235 | — |
| HBS1L | 0.448 | 0.000 | — |
| KRTAP11-1 | 0.446 | 0.000 | — |
| ILF2 | 0.440 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ITGB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCDHGA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HS3ST2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EPO | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MPPE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TNFRSF10B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NRP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| B4GALT5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ADCY9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TPST1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.1 + PDB: 无 | pLDDT=70.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoli fibrillar center, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GINM1 — Glycoprotein integral membrane protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小330 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NU53
- Protein Atlas: https://www.proteinatlas.org/ENSG00000055211-GINM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GINM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NU53
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NU53-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
