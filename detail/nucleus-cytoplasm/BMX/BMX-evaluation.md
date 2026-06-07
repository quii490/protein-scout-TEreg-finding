---
type: protein-evaluation
gene: "BMX"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BMX — REJECTED (研究热度过高 (PubMed strict=187，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BMX |
| 蛋白名称 | Cytoplasmic tyrosine-protein kinase BMX |
| 蛋白大小 | 675 aa / 78.0 kDa |
| UniProt ID | P51813 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 675 aa / 78.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=187 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.7; PDB: 2EKX, 2YS2, 3SXR, 3SXS, 6I99, 8X2A |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035875, IPR011009, IPR050198, IPR011993, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- ruffle membrane (GO:0032587)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 187 |
| PubMed broad count | 479 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Single-cell transcriptomic profiling unravels the adenoma-initiation role of protein tyrosine kinases during colorectal tumorigenesis.. *Signal transduction and targeted therapy*. PMID: 35221332
2. Lactylation-driven USP4-mediated ANXA2 stabilization and activation promotes maintenance and radioresistance of glioblastoma stem cells.. *Cell death and differentiation*. PMID: 40185997
3. Integrative single-cell RNA sequencing and metabolomics decipher the imbalanced lipid-metabolism in maladaptive immune responses during sepsis.. *Frontiers in immunology*. PMID: 37180171
4. Retraction.. *Journal of cellular biochemistry*. PMID: 34288062
5. Mycobacterium tuberculosis modulates phosphorylation of host ATP6V1E1 to promote intracellular survival.. *Nature communications*. PMID: 41651829

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.7 |
| 高置信度残基 (pLDDT>90) 占比 | 43.6% |
| 置信残基 (pLDDT 70-90) 占比 | 26.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 21.8% |
| 有序区域 (pLDDT>70) 占比 | 70.4% |
| 可用 PDB 条目 | 2EKX, 2YS2, 3SXR, 3SXS, 6I99, 8X2A |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2EKX, 2YS2, 3SXR, 3SXS, 6I99, 8X2A）+ AlphaFold极高置信度预测（pLDDT=75.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035875, IPR011009, IPR050198, IPR011993, IPR001849; Pfam: PF00779, PF00169, PF07714 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STAT3 | 0.956 | 0.838 | — |
| RUFY1 | 0.876 | 0.356 | — |
| CASP3 | 0.860 | 0.311 | — |
| STAP1 | 0.773 | 0.054 | — |
| PLEK | 0.713 | 0.000 | — |
| PLEK2 | 0.705 | 0.000 | — |
| PRDM1 | 0.691 | 0.677 | — |
| RUFY2 | 0.648 | 0.292 | — |
| KIZ | 0.634 | 0.634 | — |
| PTPN21 | 0.596 | 0.455 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PIM1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14937|pubmed:16186805| |
| TP53 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14937|pubmed:16186805| |
| Prkce | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11139474 |
| NOPCHAP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| AP3M1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| GRWD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| CCT7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| HSPH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.7 + PDB: 2EKX, 2YS2, 3SXR, 3SXS, 6I99,  | pLDDT=75.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. BMX — Cytoplasmic tyrosine-protein kinase BMX，研究基础较多，新颖性有限。
2. 蛋白大小675 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 187 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 187 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51813
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102010-BMX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BMX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51813
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000102010-BMX/subcellular

![](https://images.proteinatlas.org/1048/1751_G2_18_cr58009842c82e5_red_green.jpg)
![](https://images.proteinatlas.org/1048/1751_G2_2_cr57fd24c6a75b7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P51813-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P51813 |
| SMART | SM00107;SM00233;SM00252;SM00219; |
| UniProt Domain [FT] | DOMAIN 4..111; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145"; DOMAIN 296..392; /note="SH2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00191"; DOMAIN 417..675; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR035875;IPR011009;IPR050198;IPR011993;IPR001849;IPR000719;IPR017441;IPR001245;IPR000980;IPR036860;IPR008266;IPR020635;IPR001562; |
| Pfam | PF00779;PF00169;PF07714;PF00017; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000102010-BMX/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PTPN21 | Intact, Biogrid | true |
| STAT3 | Intact, Biogrid | true |
| BIRC2 | Intact | false |
| HSP90AA1 | Biogrid | false |
| HSP90AB1 | Intact | false |
| PAK1 | Biogrid | false |
| PDCD2L | Biogrid | false |
| PTK2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
