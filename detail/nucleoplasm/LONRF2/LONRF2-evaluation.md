---
type: protein-evaluation
gene: "LONRF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LONRF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LONRF2 / RNF192 |
| 蛋白名称 | LON peptidase N-terminal domain and RING finger protein 2 |
| 蛋白大小 | 754 aa / 83.7 kDa |
| UniProt ID | Q1L5Z9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 754 aa / 83.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003111, IPR046336, IPR015947, IPR011990, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF192 |

**关键文献**:
1. LONRF2 is a protein quality control ubiquitin ligase whose deficiency causes late-onset neurological deficits.. *Nature aging*. PMID: 37474791
2. Transcriptomic characterization of Lonrf1 at the single-cell level under pathophysiological conditions.. *Journal of biochemistry*. PMID: 36888978
3. Comprehensive Analysis of miRNA-Mediated Regulatory Network and Identification of Prognosis Biomarkers in Rectal Cancer.. *Frontiers in genetics*. PMID: 35495167
4. Identification of miRNAs and target genes associated with lymph node metastasis in cervical cancer using bioinformatics analysis.. *Toxicology mechanisms and methods*. PMID: 37125668
5. Abnormal expression of mRNA, microRNA alteration and aberrant DNA methylation patterns in rectal adenocarcinoma.. *PloS one*. PMID: 28350845

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.2 |
| 高置信度残基 (pLDDT>90) 占比 | 50.5% |
| 置信残基 (pLDDT 70-90) 占比 | 26.3% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 18.6% |
| 有序区域 (pLDDT>70) 占比 | 76.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.2，有序区 76.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003111, IPR046336, IPR015947, IPR011990, IPR019734; Pfam: PF02190, PF13432, PF13923 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AFF3 | 0.665 | 0.045 | — |
| CHST10 | 0.612 | 0.000 | — |
| MYO9A | 0.540 | 0.124 | — |
| NFX1 | 0.526 | 0.000 | — |
| SUPT16H | 0.521 | 0.000 | — |
| SYNCRIP | 0.496 | 0.000 | — |
| MVB12B | 0.492 | 0.000 | — |
| GNAO1 | 0.489 | 0.000 | — |
| PDZRN4 | 0.487 | 0.000 | — |
| PPP4C | 0.480 | 0.054 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| OTUD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| PLA2G10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DPYSL5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNX24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZFYVE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCL22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARL15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XRCC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LONRF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.2 + PDB: 无 | pLDDT=78.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LONRF2 — LON peptidase N-terminal domain and RING finger protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小754 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q1L5Z9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170500-LONRF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LONRF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q1L5Z9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000170500-LONRF2/subcellular

![](https://images.proteinatlas.org/57366/1001_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/57366/1001_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/57366/990_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/57366/990_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/57366/992_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/57366/992_G7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q1L5Z9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
