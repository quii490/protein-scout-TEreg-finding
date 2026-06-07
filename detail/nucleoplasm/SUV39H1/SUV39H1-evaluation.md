---
type: protein-evaluation
gene: "SUV39H1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SUV39H1 — REJECTED (研究热度过高 (PubMed strict=448，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUV39H1 / KMT1A, SUV39H |
| 蛋白名称 | Histone-lysine N-methyltransferase SUV39H1 |
| 蛋白大小 | 412 aa / 47.9 kDa |
| UniProt ID | O43463 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Chromosome; Nucleus lamina; Nucleus, nucleoplasm; C |
| 蛋白大小 | 10/10 | ×1 | 10 | 412 aa / 47.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=448 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.5; PDB: 3MTS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016197, IPR000953, IPR023780, IPR023779, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Chromosome; Nucleus lamina; Nucleus, nucleoplasm; Chromosome, centromere; Cytoplasmic vesic... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromatin silencing complex (GO:0005677)
- chromosome, centromeric region (GO:0000775)
- condensed nuclear chromosome (GO:0000794)
- cytoplasmic vesicle (GO:0031410)
- eNoSc complex (GO:0061773)
- heterochromatin (GO:0000792)
- nuclear lamina (GO:0005652)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 448 |
| PubMed broad count | 737 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KMT1A, SUV39H |

**关键文献**:
1. ASB7 is a negative regulator of H3K9me3 homeostasis.. *Science (New York, N.Y.)*. PMID: 40440427
2. Establishment of H3K9-methylated heterochromatin and its functions in tissue differentiation and maintenance.. *Nature reviews. Molecular cell biology*. PMID: 35562425
3. FBXO44 promotes DNA replication-coupled repetitive element silencing in cancer cells.. *Cell*. PMID: 33357448
4. Spatial Multiplexed Protein Profiling of Cardiac Ischemia-Reperfusion Injury.. *Circulation research*. PMID: 37249015
5. DNA hypomethylation promotes UHRF1-and SUV39H1/H2-dependent crosstalk between H3K18ub and H3K9me3 to reinforce heterochromatin states.. *Molecular cell*. PMID: 39631394

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.5 |
| 高置信度残基 (pLDDT>90) 占比 | 72.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 6.6% |
| 有序区域 (pLDDT>70) 占比 | 89.8% |
| 可用 PDB 条目 | 3MTS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.5，有序区 89.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016197, IPR000953, IPR023780, IPR023779, IPR011381; Pfam: PF00385, PF05033, PF00856 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CBX5 | 0.999 | 0.909 | — |
| SIRT1 | 0.999 | 0.538 | — |
| CBX3 | 0.998 | 0.695 | — |
| DNMT1 | 0.998 | 0.516 | — |
| DNMT3A | 0.996 | 0.305 | — |
| RRP8 | 0.996 | 0.292 | — |
| HDAC1 | 0.994 | 0.553 | — |
| MECP2 | 0.993 | 0.292 | — |
| DNMT3B | 0.990 | 0.292 | — |
| CBX1 | 0.990 | 0.777 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSBTAP00000101889.1 | psi-mi:"MI:0516"(methyltransferase radiometric ass | pubmed:10949293 |
| H3C1 | psi-mi:"MI:0415"(enzymatic study) | pubmed:10949293 |
| CBX5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CBX4 | psi-mi:"MI:0515"(methyltransferase assay) | pubmed:22078878|imex:IM-16600 |
| - | psi-mi:"MI:0096"(pull down) | imex:IM-12128|pubmed:18485871 |
| RRP8 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12128|pubmed:18485871 |
| PML-RAR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16449642|imex:IM-19552 |
| PML | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16449642|imex:IM-19552 |
| KRTAP10-7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP10-8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.5 + PDB: 3MTS | pLDDT=88.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Nucleus lamina; Nucleus, nucl / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SUV39H1 — Histone-lysine N-methyltransferase SUV39H1，研究基础较多，新颖性有限。
2. 蛋白大小412 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 448 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 448 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43463
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101945-SUV39H1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUV39H1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43463
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43463-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43463 |
| SMART | SM00298;SM00508;SM00468;SM00317; |
| UniProt Domain [FT] | DOMAIN 43..101; /note="Chromo"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00053"; DOMAIN 179..240; /note="Pre-SET"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00157"; DOMAIN 243..366; /note="SET"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00190"; DOMAIN 396..412; /note="Post-SET"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00155" |
| InterPro | IPR016197;IPR000953;IPR023780;IPR023779;IPR011381;IPR050973;IPR003616;IPR007728;IPR001214;IPR046341; |
| Pfam | PF00385;PF05033;PF00856; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000101945-SUV39H1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATE1 | Intact, Biogrid | true |
| BCL11B | Intact, Biogrid | true |
| C8orf74 | Intact, Biogrid | true |
| CBX1 | Intact, Biogrid, Bioplex | true |
| CBX3 | Intact, Biogrid, Bioplex | true |
| CBX5 | Intact, Biogrid, Bioplex | true |
| CDCA4 | Intact, Biogrid | true |
| CLK3 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
