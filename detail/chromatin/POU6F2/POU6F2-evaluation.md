---
type: protein-evaluation
gene: "POU6F2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## POU6F2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POU6F2 / RPF1 |
| 蛋白名称 | POU domain, class 6, transcription factor 2 |
| 蛋白大小 | 691 aa / 73.3 kDa |
| UniProt ID | P78424 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 691 aa / 73.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR009057, IPR010982, IPR013847, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 59 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RPF1 |

**关键文献**:
1. The murine Pou6f2 gene is temporally and spatially regulated during kidney embryogenesis and its human homolog is overexpressed in a subset of Wilms tumors.. *Journal of pediatric hematology/oncology*. PMID: 17164647
2. Identification of a novel somatic mutation of POU6F2 by whole-genome sequencing in prolactinoma.. *Molecular genetics & genomic medicine*. PMID: 31692290
3. Long non-coding RNA POU6F2-AS2 promotes cell proliferation and drug resistance in colon cancer by regulating miR-377/BRD4.. *Journal of cellular and molecular medicine*. PMID: 32100443
4. Bayesian Networks Predict Neuronal Transdifferentiation.. *G3 (Bethesda, Md.)*. PMID: 29848620
5. Long noncoding RNA POU6F2-AS1 regulates lung cancer aggressiveness through sponging miR-34c-5p to modulate KCNJ4 expression.. *Genetics and molecular biology*. PMID: 33999092

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.3 |
| 高置信度残基 (pLDDT>90) 占比 | 6.9% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 72.4% |
| 有序区域 (pLDDT>70) 占比 | 18.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.3），有序残基占 18.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR010982, IPR013847, IPR000327; Pfam: PF00046, PF00157 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OBSCN | 0.777 | 0.000 | — |
| WT1 | 0.771 | 0.053 | — |
| AMER1 | 0.740 | 0.000 | — |
| RP9 | 0.582 | 0.000 | — |
| REST | 0.511 | 0.053 | — |
| GPC3 | 0.491 | 0.000 | — |
| PALM3 | 0.446 | 0.000 | — |
| CNGA1 | 0.444 | 0.000 | — |
| IRX2 | 0.433 | 0.000 | — |
| GLRA1 | 0.433 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZBTB24 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TTC19 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| OPLAH | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDC37 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| STRA8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PDE6H | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAGEA12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| VAX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENSP00000384004.1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NUP62CL | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.3 + PDB: 无 | pLDDT=47.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

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
1. POU6F2 — POU domain, class 6, transcription factor 2，非常新颖，仅有少数基础研究。
2. 蛋白大小691 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=47.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78424
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106536-POU6F2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POU6F2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78424
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P78424-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P78424 |
| SMART | SM00389;SM00352; |
| UniProt Domain [FT] | DOMAIN 476..586; /note="POU-specific"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00530" |
| InterPro | IPR001356;IPR009057;IPR010982;IPR013847;IPR000327;IPR050255; |
| Pfam | PF00046;PF00157; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106536-POU6F2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTN3 | Intact | false |
| AGR2 | Intact | false |
| ARHGEF6 | Intact | false |
| BFSP2 | Intact | false |
| BHLHE40 | Intact | false |
| C1orf109 | Intact | false |
| C5 | Intact | false |
| CCNC | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
