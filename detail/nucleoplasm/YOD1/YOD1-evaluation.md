---
type: protein-evaluation
gene: "YOD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YOD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YOD1 / DUBA8, HIN7, OTUD2 |
| 蛋白名称 | Ubiquitin thioesterase OTU1 |
| 蛋白大小 | 348 aa / 38.3 kDa |
| UniProt ID | Q5VVQ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Plasma membrane, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 348 aa / 38.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=70 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=80.8; PDB: 4BOQ, 4BOS, 4BOZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR048857, IPR003323, IPR038765, IPR029071, IPR057 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.0/180** | |
| **归一化总分** | | | **56.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 70 |
| PubMed broad count | 104 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DUBA8, HIN7, OTUD2 |

**关键文献**:
1. Cardiomyocyte-derived YOD1 promotes pathological cardiac hypertrophy by deubiquitinating and stabilizing STAT3.. *Science advances*. PMID: 40561034
2. Identification of novel therapeutic targets for chronic kidney disease and kidney function by integrating multi-omics proteome with transcriptome.. *Genome medicine*. PMID: 38898508
3. KDELR3 and YOD1 proteins as critical endoplasmic reticulum stress mediators and potential therapeutic targets in diabetic foot ulcers: An integrated bioinformatics analysis.. *International journal of biological macromolecules*. PMID: 40354856
4. YOD1 regulates microglial homeostasis by deubiquitinating MYH9 to promote the pathogenesis of Alzheimer's disease.. *Acta pharmaceutica Sinica. B*. PMID: 40041897
5. Linear ubiquitination at damaged lysosomes induces local NFKB activation and controls cell survival.. *Autophagy*. PMID: 39744815

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.8 |
| 高置信度残基 (pLDDT>90) 占比 | 48.6% |
| 置信残基 (pLDDT 70-90) 占比 | 30.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 17.5% |
| 有序区域 (pLDDT>70) 占比 | 78.8% |
| 可用 PDB 条目 | 4BOQ, 4BOS, 4BOZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4BOQ, 4BOS, 4BOZ）+ AlphaFold高质量预测（pLDDT=80.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048857, IPR003323, IPR038765, IPR029071, IPR057766; Pfam: PF02338, PF21403, PF24560 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VCP | 0.998 | 0.905 | — |
| UBC | 0.996 | 0.995 | — |
| PLAA | 0.995 | 0.967 | — |
| UFD1 | 0.989 | 0.967 | — |
| RPS27A | 0.988 | 0.986 | — |
| UBB | 0.982 | 0.979 | — |
| UBXN6 | 0.981 | 0.570 | — |
| NPLOC4 | 0.949 | 0.882 | — |
| UBA52 | 0.948 | 0.947 | — |
| UBE4B | 0.923 | 0.840 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Gapdh2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG11327 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Hey | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG17855 | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| amls | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| TXNDC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| THOC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| BIRC2 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| RBCK1 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| TANK | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.8 + PDB: 4BOQ, 4BOS, 4BOZ | pLDDT=80.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. YOD1 — Ubiquitin thioesterase OTU1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小348 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 70 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VVQ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180667-YOD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YOD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VVQ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000180667-YOD1/subcellular

![](https://images.proteinatlas.org/28400/322_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/28400/322_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/28400/327_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/28400/327_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/28400/335_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/28400/335_E3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VVQ6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5VVQ6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 149..274; /note="OTU"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00139" |
| InterPro | IPR048857;IPR003323;IPR038765;IPR029071;IPR057766;IPR013087; |
| Pfam | PF02338;PF21403;PF24560; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000180667-YOD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TRAF6 | Intact, Biogrid | true |
| UBC | Intact, Biogrid | true |
| UBXN6 | Intact, Biogrid | true |
| VCP | Intact, Biogrid | true |
| CDK1 | Biogrid | false |
| DAZAP2 | Intact | false |
| DDIT4L | Intact | false |
| FAF2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
