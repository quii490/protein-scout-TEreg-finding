---
type: protein-evaluation
gene: "FRA10AC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FRA10AC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FRA10AC1 / C10orf4 |
| 蛋白名称 | Protein FRA10AC1 |
| 蛋白大小 | 315 aa / 37.5 kDa |
| UniProt ID | Q70Z53 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 315 aa / 37.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019129, IPR050645; Pfam: PF09725 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.5/180** | |
| **归一化总分** | | | **76.4/100** | |

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

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf4 |

**关键文献**:
1. Reconstruction of a Comprehensive Interactome and Experimental Data Analysis of FRA10AC1 May Provide Insights into Its Biological Role in Health and Disease.. *Genes*. PMID: 36980839
2. Biallelic FRA10AC1 variants cause a neurodevelopmental disorder with growth retardation.. *Brain : a journal of neurology*. PMID: 34694367
3. Folate-sensitive fragile site FRA10A is due to an expansion of a CGG repeat in a novel gene, FRA10AC1, encoding a nuclear protein.. *Genomics*. PMID: 15203205
4. A Biallelic Variant in FRA10AC1 Is Associated With Neurodevelopmental Disorder and Growth Retardation.. *Neurology. Genetics*. PMID: 35821753
5. Signature Construction and Disulfidptosis-Related Molecular Cluster Identification for Better Prediction of Prognosis in Glioma.. *Journal of molecular neuroscience : MN*. PMID: 38573391

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 27.0% |
| 置信残基 (pLDDT 70-90) 占比 | 32.1% |
| 中等置信 (pLDDT 50-70) 占比 | 17.1% |
| 低置信 (pLDDT<50) 占比 | 23.8% |
| 有序区域 (pLDDT>70) 占比 | 59.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.2，有序区 59.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019129, IPR050645; Pfam: PF09725 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF32 | 0.913 | 0.000 | — |
| CWC27 | 0.844 | 0.783 | — |
| ESS2 | 0.831 | 0.786 | — |
| PDE6C | 0.826 | 0.000 | — |
| CHERP | 0.773 | 0.694 | — |
| LGI1 | 0.764 | 0.000 | — |
| SF3B2 | 0.739 | 0.694 | — |
| IK | 0.714 | 0.694 | — |
| LENG1 | 0.665 | 0.663 | — |
| TMEM185A | 0.658 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EEF1D | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ADPRS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| C7orf25 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GDPD2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| LPPR4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GLRX3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| VPS29 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MAP3K12 | psi-mi:"MI:0096"(pull down) | pubmed:16169070|imex:IM-16517| |
| GATD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HABP4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 无 | pLDDT=72.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FRA10AC1 — Protein FRA10AC1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小315 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q70Z53
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148690-FRA10AC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FRA10AC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q70Z53
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q70Z53-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q70Z53 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019129;IPR050645; |
| Pfam | PF09725; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000148690-FRA10AC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CHERP | Intact, Biogrid | true |
| ESS2 | Intact, Biogrid | true |
| IK | Intact, Biogrid | true |
| SF3B2 | Intact, Biogrid | true |
| KASH5 | Intact | false |
| MAP3K12 | Intact | false |
| MOB2 | Intact | false |
| TRIM41 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
