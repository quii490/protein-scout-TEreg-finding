---
type: protein-evaluation
gene: "RHNO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RHNO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RHNO1 / C12orf32, RHINO |
| 蛋白名称 | RAD9, HUS1, RAD1-interacting nuclear orphan protein 1 |
| 蛋白大小 | 238 aa / 26.7 kDa |
| UniProt ID | Q9BSD3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 238 aa / 26.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.8; PDB: 6J8Y, 8WU8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029293; Pfam: PF15319 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.5/180** | |
| **归一化总分** | | | **74.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome (GO:0005694)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- site of double-strand break (GO:0035861)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C12orf32, RHINO |

**关键文献**:
1. RHNO1: at the crossroads of DNA replication stress, DNA repair, and cancer.. *Oncogene*. PMID: 39107463
2. Co-regulation and function of FOXM1/RHNO1 bidirectional genes in cancer.. *eLife*. PMID: 33890574
3. RHNO1 disruption inhibits cell proliferation and induces mitochondrial apoptosis via PI3K/Akt pathway in hepatocellular carcinoma.. *Biochemical and biophysical research communications*. PMID: 37364391
4. Unveiling novel potential drug targets for lung cancer through Mendelian randomization analysis.. *Scientific reports*. PMID: 41436647
5. The lncRNA Rhno1/miR-6979-5p/BMP2 Axis Modulates Osteoblast Differentiation.. *International journal of biological sciences*. PMID: 32226305

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.8 |
| 高置信度残基 (pLDDT>90) 占比 | 5.9% |
| 置信残基 (pLDDT 70-90) 占比 | 31.9% |
| 中等置信 (pLDDT 50-70) 占比 | 40.3% |
| 低置信 (pLDDT<50) 占比 | 21.8% |
| 有序区域 (pLDDT>70) 占比 | 37.8% |
| 可用 PDB 条目 | 6J8Y, 8WU8 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.8），有序残基占 37.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029293; Pfam: PF15319 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAD1 | 0.989 | 0.976 | — |
| HUS1 | 0.985 | 0.943 | — |
| TOPBP1 | 0.982 | 0.722 | — |
| RAD9A | 0.970 | 0.897 | — |
| CLSPN | 0.867 | 0.000 | — |
| CHEK1 | 0.866 | 0.000 | — |
| BRIP1 | 0.822 | 0.000 | — |
| BRCA1 | 0.802 | 0.421 | — |
| ATRIP | 0.692 | 0.000 | — |
| RAD17 | 0.667 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| Rabac1 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:30925931|imex:IM-26645 |
| CCNDBP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TFIP11 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| KRTAP10-8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BANP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CYSRT1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLGA2 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| LRRK2 | psi-mi:"MI:0089"(protein array) | pubmed:24947832|imex:IM-22653 |
| - | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.8 + PDB: 6J8Y, 8WU8 | pLDDT=64.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. RHNO1 — RAD9, HUS1, RAD1-interacting nuclear orphan protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小238 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BSD3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171792-RHNO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RHNO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BSD3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BSD3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BSD3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029293; |
| Pfam | PF15319; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171792-RHNO1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BACE2 | Intact | false |
| CYSRT1 | Intact | false |
| GOLGA2 | Intact | false |
| HUS1 | Biogrid | false |
| KRTAP10-8 | Intact | false |
| KRTAP10-9 | Intact | false |
| LZTS2 | Intact | false |
| RAD1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
