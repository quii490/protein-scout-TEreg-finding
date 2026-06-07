---
type: protein-evaluation
gene: "HIPK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HIPK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HIPK1 / KIAA0630, MYAK, NBAK2 |
| 蛋白名称 | Homeodomain-interacting protein kinase 1 |
| 蛋白大小 | 1210 aa / 130.8 kDa |
| UniProt ID | Q86Z02 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Basal body, Cytosol; 额外: Centrosome; UniProt: Nucleus; Cytoplasm; Nucleus speckle |
| 蛋白大小 | 5/10 | ×1 | 5 | 1210 aa / 130.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR017441, IPR008271, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.0/180** | |
| **归一化总分** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Basal body, Cytosol; 额外: Centrosome | Supported |
| UniProt | Nucleus; Cytoplasm; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 73 |
| PubMed broad count | 93 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0630, MYAK, NBAK2 |

**关键文献**:
1. Identification of ROCK1 as a novel biomarker for postmenopausal osteoporosis and pan-cancer analysis.. *Aging*. PMID: 37683138
2. Update on the Regulation of HIPK1, HIPK2 and HIPK3 Protein Kinases by microRNAs.. *MicroRNA (Shariqah, United Arab Emirates)*. PMID: 29793420
3. HIPK1 Inhibition Protects against Pathological Cardiac Hypertrophy by Inhibiting the CREB-C/EBPβ Axis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37098980
4. Characterization of cells and gene-targeted mice deficient for the p53-binding kinase homeodomain-interacting protein kinase 1 (HIPK1).. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 12702766
5. Improved protein expression in HEK293 cells by over-expressing miR-22 and knocking-out its target gene, HIPK1.. *New biotechnology*. PMID: 31425885

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.3 |
| 高置信度残基 (pLDDT>90) 占比 | 25.6% |
| 置信残基 (pLDDT 70-90) 占比 | 4.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 69.0% |
| 有序区域 (pLDDT>70) 占比 | 30.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.3），有序残基占 30.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR008271, IPR050494; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TP53 | 0.967 | 0.296 | — |
| RASSF5 | 0.929 | 0.301 | — |
| DAXX | 0.814 | 0.331 | — |
| PML | 0.674 | 0.000 | — |
| DCAF7 | 0.674 | 0.457 | — |
| FHL3 | 0.643 | 0.630 | — |
| GATA4 | 0.587 | 0.091 | — |
| MDM2 | 0.578 | 0.217 | — |
| PAGE4 | 0.577 | 0.000 | — |
| NKX2-5 | 0.518 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TP53 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12702766 |
| ENSMUSP00000113998.2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:12702766 |
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| 38943" | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| DAXX | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12529400|imex:IM-18883 |
| PML | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:12529400|imex:IM-18883 |
| UBE2I | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| GLUL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| ATP13A2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:22645275|imex:IM-17891 |
| HAX1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.3 + PDB: 无 | pLDDT=51.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Nucleus speckle / Nucleoplasm, Basal body, Cytosol; 额外: Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HIPK1 — Homeodomain-interacting protein kinase 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1210 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 73 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=51.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86Z02
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163349-HIPK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HIPK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86Z02
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000163349-HIPK1/subcellular

![](https://images.proteinatlas.org/16664/2179_C1_39_blue_red_green.jpg)
![](https://images.proteinatlas.org/16664/2179_C1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/16664/2201_D1_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/16664/2201_D1_56_blue_red_green.jpg)
![](https://images.proteinatlas.org/16664/2210_E1_23_blue_red_green.jpg)
![](https://images.proteinatlas.org/16664/2210_E1_50_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86Z02-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86Z02 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 190..518; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR011009;IPR000719;IPR017441;IPR008271;IPR050494; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163349-HIPK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FHL3 | Intact, Biogrid | true |
| TP53 | Intact, Biogrid | true |
| PARK7 | Biogrid | false |
| RASSF5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
