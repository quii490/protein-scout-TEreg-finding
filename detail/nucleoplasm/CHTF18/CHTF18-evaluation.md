---
type: protein-evaluation
gene: "CHTF18"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CHTF18 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHTF18 / C16orf41, CTF18 |
| 蛋白名称 | Chromosome transmission fidelity protein 18 homolog |
| 蛋白大小 | 975 aa / 107.4 kDa |
| UniProt ID | Q8WVB6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 8/10 | x1 | 8 | 975 aa / 107.4 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=64.1; PDB: 8UMT, 8UMU, 8UMV, 8UMW, 8UMY, 8UN0, 8UNJ |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR003593, IPR003959, IPR053016, IPR027417, IPR047 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Ctf18 RFC-like complex (GO:0031390)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf41, CTF18 |

**关键文献**:
1. Disruption of the moonlighting function of CTF18 in a patient with T-lymphopenia.. *Frontiers in immunology*. PMID: 40028343
2. Comprehensive Analysis of Cell Cycle-Related Genes in Patients With Prostate Cancer.. *Frontiers in oncology*. PMID: 35087757
3. Disruption of CHTF18 causes defective meiotic recombination in male mice.. *PLoS genetics*. PMID: 23133398
4. Mesenchymal stem cells reverse thymus aging by reprogramming the DNA methylation of thymic epithelial cells.. *Regenerative therapy*. PMID: 38571892
5. Sequencing of candidate chromosome instability genes in endometrial cancers reveals somatic mutations in ESCO1, CHTF18, and MRE11A.. *PloS one*. PMID: 23755103

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.1 |
| 高置信度残基 (pLDDT>90) 占比 | 8.7% |
| 置信残基 (pLDDT 70-90) 占比 | 42.8% |
| 中等置信 (pLDDT 50-70) 占比 | 12.7% |
| 低置信 (pLDDT<50) 占比 | 35.8% |
| 有序区域 (pLDDT>70) 占比 | 51.5% |
| 可用 PDB 条目 | 8UMT, 8UMU, 8UMV, 8UMW, 8UMY, 8UN0, 8UNJ, 8ZWO, 9IIN |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.1），有序残基占 51.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR003959, IPR053016, IPR027417, IPR047854; Pfam: PF00004 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DSCC1 | 0.999 | 0.990 | — |
| RFC3 | 0.999 | 0.922 | — |
| RFC2 | 0.999 | 0.909 | — |
| CHTF8 | 0.999 | 0.978 | — |
| RFC4 | 0.999 | 0.867 | — |
| RFC5 | 0.999 | 0.943 | — |
| POLE | 0.990 | 0.957 | — |
| WDHD1 | 0.967 | 0.510 | — |
| POLA1 | 0.967 | 0.477 | — |
| ESCO1 | 0.964 | 0.306 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17314511 |
| PHOSPHO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P4HA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RFC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RFC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DSCC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM83H | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CRK | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| STAT3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.1 + PDB: 8UMT, 8UMU, 8UMV, 8UMW, 8UMY,  | pLDDT=64.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CHTF18 -- Chromosome transmission fidelity protein 18 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小975 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WVB6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127586-CHTF18/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHTF18
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WVB6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000127586-CHTF18/subcellular

![](https://images.proteinatlas.org/40976/1047_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/40976/1047_E6_3_red_green.jpg)
![](https://images.proteinatlas.org/40976/1048_E6_3_red_green.jpg)
![](https://images.proteinatlas.org/40976/1048_E6_5_red_green.jpg)
![](https://images.proteinatlas.org/40976/1137_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/40976/1137_F12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WVB6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WVB6 |
| SMART | SM00382; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003593;IPR003959;IPR053016;IPR027417;IPR047854; |
| Pfam | PF00004; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000127586-CHTF18/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CHTF8 | Biogrid | false |
| DSCC1 | Biogrid | false |
| MYC | Biogrid | false |
| PCNA | Biogrid | false |
| RFC2 | Biogrid | false |
| RFC3 | Biogrid | false |
| RFC4 | Biogrid | false |
| RFC5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
