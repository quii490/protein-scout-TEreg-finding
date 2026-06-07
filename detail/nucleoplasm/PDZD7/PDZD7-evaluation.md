---
type: protein-evaluation
gene: "PDZD7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PDZD7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PDZD7 / PDZK7 |
| 蛋白名称 | PDZ domain-containing protein 7 |
| 蛋白大小 | 1033 aa / 111.8 kDa |
| UniProt ID | Q9H5P4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Primary cilium; 额外: Basal body; UniProt: Cell projection, cilium; Nucleus; Cell projection, stereocil |
| 蛋白大小 | 8/10 | ×1 | 8 | 1033 aa / 111.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.7; PDB: 2EEH, 7PC5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001478, IPR036034, IPR042786, IPR051844; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Primary cilium; 额外: Basal body | Approved |
| UniProt | Cell projection, cilium; Nucleus; Cell projection, stereocilium | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- extracellular space (GO:0005615)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- stereocilia ankle link (GO:0002141)
- stereocilia ankle link complex (GO:0002142)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 54 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PDZK7 |

**关键文献**:
1. Targeted next generation sequencing for molecular diagnosis of Usher syndrome.. *Orphanet journal of rare diseases*. PMID: 25404053
2. Deafness-related protein PDZD7 forms complex with the C-terminal tail of FCHSD2.. *The Biochemical journal*. PMID: 35695292
3. Deafness-Associated ADGRV1 Mutation Impairs USH2A Stability through Improper Phosphorylation of WHRN and WDSUB1 Recruitment.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37066759
4. Exon Skipping Therapy Restores Ciliary Function in USH2A-Related Retinal Degeneration.. *Investigative ophthalmology & visual science*. PMID: 40970667
5. Localization of PDZD7 to the stereocilia ankle-link associates this scaffolding protein with the Usher syndrome protein network.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 23055499

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.7 |
| 高置信度残基 (pLDDT>90) 占比 | 13.4% |
| 置信残基 (pLDDT 70-90) 占比 | 23.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 56.2% |
| 有序区域 (pLDDT>70) 占比 | 36.6% |
| 可用 PDB 条目 | 2EEH, 7PC5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.7），有序残基占 36.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001478, IPR036034, IPR042786, IPR051844; Pfam: PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADGRV1 | 0.997 | 0.292 | — |
| USH2A | 0.995 | 0.330 | — |
| USH1G | 0.968 | 0.099 | — |
| WHRN | 0.946 | 0.000 | — |
| USH1C | 0.915 | 0.000 | — |
| VEZT | 0.889 | 0.000 | — |
| MYO7A | 0.840 | 0.078 | — |
| FCHSD2 | 0.811 | 0.797 | — |
| CLRN1 | 0.802 | 0.000 | — |
| CIB2 | 0.777 | 0.077 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HIST2H2BF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| VANGL1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| DGKK | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| MAP2K2 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| ARHGEF16 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| ASIC3 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| SHROOM4 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| SLC16A1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| SLC2A1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.7 + PDB: 2EEH, 7PC5 | pLDDT=56.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell projection, cilium; Nucleus; Cell projection, / Nucleoplasm, Primary cilium; 额外: Basal body | 一致 |
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
1. PDZD7 — PDZ domain-containing protein 7，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1033 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=56.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H5P4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186862-PDZD7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PDZD7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H5P4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000186862-PDZD7/subcellular

![](https://images.proteinatlas.org/74542/1647_E5_31_red_green.jpg)
![](https://images.proteinatlas.org/74542/1647_E5_32_red_green.jpg)
![](https://images.proteinatlas.org/74542/1735_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/74542/1735_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/74542/1855_G10_31_red_green.jpg)
![](https://images.proteinatlas.org/74542/1855_G10_32_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H5P4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H5P4 |
| SMART | SM00228; |
| UniProt Domain [FT] | DOMAIN 86..168; /note="PDZ 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143"; DOMAIN 210..293; /note="PDZ 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143"; DOMAIN 862..934; /note="PDZ 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143" |
| InterPro | IPR001478;IPR036034;IPR042786;IPR051844; |
| Pfam | PF00595; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000186862-PDZD7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ADGRV1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
