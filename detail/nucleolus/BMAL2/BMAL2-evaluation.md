---
type: protein-evaluation
gene: "BMAL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BMAL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BMAL2 / ARNTL2, BHLHE6, CLIF, MOP9, PASD9 |
| 蛋白名称 | Basic helix-loop-helix ARNT-like protein 2 |
| 蛋白大小 | 636 aa / 70.9 kDa |
| UniProt ID | Q8WYA1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 636 aa / 70.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.9; PDB: 2KDK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050933, IPR036638, IPR001067, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- aryl hydrocarbon receptor complex (GO:0034751)
- chromatin (GO:0000785)
- CLOCK-BMAL transcription complex (GO:1990513)
- cytoplasm (GO:0005737)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 77 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARNTL2, BHLHE6, CLIF, MOP9, PASD9 |

**关键文献**:
1. BMAL2 controls adipose tissue inflammation and metabolic adaptation during obesity.. *Metabolism: clinical and experimental*. PMID: 40983272
2. BMAL2 promotes eCIRP-induced macrophage endotoxin tolerance.. *Frontiers in immunology*. PMID: 38938563
3. Circadian gene variants and breast cancer.. *Cancer letters*. PMID: 28109907
4. Association between brain-muscle-ARNT-like protein-2 (BMAL2) gene polymorphism and type 2 diabetes mellitus in obese Japanese individuals: A cross-sectional analysis of the Japan Multi-institutional Collaborative Cohort Study.. *Diabetes research and clinical practice*. PMID: 26497775
5. Deletion of the Clock Gene Bmal2 Leads to Alterations in Hypothalamic Clocks, Circadian Regulation of Feeding, and Energy Balance.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 38531632

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.9 |
| 高置信度残基 (pLDDT>90) 占比 | 27.4% |
| 置信残基 (pLDDT 70-90) 占比 | 17.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 44.2% |
| 有序区域 (pLDDT>70) 占比 | 44.9% |
| 可用 PDB 条目 | 2KDK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.9），有序残基占 44.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050933, IPR036638, IPR001067, IPR000014; Pfam: PF00010, PF00989, PF14598 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLOCK | 0.999 | 0.891 | — |
| NPAS2 | 0.997 | 0.890 | — |
| ARNTL | 0.940 | 0.777 | — |
| CRY1 | 0.864 | 0.397 | — |
| CIPC | 0.858 | 0.760 | — |
| CRY2 | 0.844 | 0.303 | — |
| SERPINE1 | 0.807 | 0.000 | — |
| PASD1 | 0.778 | 0.391 | — |
| CSNK1E | 0.766 | 0.129 | — |
| PER2 | 0.747 | 0.382 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EPAS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11018023|imex:IM-20044 |
| CLOCK | psi-mi:"MI:0018"(two hybrid) | pubmed:11018023|imex:IM-20044 |
| RORC | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| FAM200C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NPAS2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CTTNBP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BMAL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PER1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MDM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SSRP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.9 + PDB: 2KDK | pLDDT=60.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BMAL2 — Basic helix-loop-helix ARNT-like protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小636 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WYA1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000029153-BMAL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BMAL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WYA1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000029153-BMAL2/subcellular

![](https://images.proteinatlas.org/59074/1020_B11_10_red_green.jpg)
![](https://images.proteinatlas.org/59074/1020_B11_11_red_green.jpg)
![](https://images.proteinatlas.org/59074/993_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/59074/993_B11_3_red_green.jpg)
![](https://images.proteinatlas.org/59074/997_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/59074/997_A12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WYA1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WYA1 |
| SMART | SM00353;SM00091; |
| UniProt Domain [FT] | DOMAIN 107..160; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981"; DOMAIN 178..250; /note="PAS 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00140"; DOMAIN 357..427; /note="PAS 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00140"; DOMAIN 432..475; /note="PAC" |
| InterPro | IPR011598;IPR050933;IPR036638;IPR001067;IPR000014;IPR035965;IPR013767; |
| Pfam | PF00010;PF00989;PF14598; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000029153-BMAL2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CLOCK | Intact, Biogrid | true |
| NPAS2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
