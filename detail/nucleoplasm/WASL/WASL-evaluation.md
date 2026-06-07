---
type: protein-evaluation
gene: "WASL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WASL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WASL |
| 蛋白名称 | Actin nucleation-promoting factor WASL |
| 蛋白大小 | 505 aa / 54.8 kDa |
| UniProt ID | O00401 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoli; UniProt: Cytoplasm, cytoskeleton; Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 505 aa / 54.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=56 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.7; PDB: 2FF3, 2LNH, 2VCP, 4CC2, 4CC7, 9DLX |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000095, IPR036936, IPR011993, IPR011026, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli | Approved |
| UniProt | Cytoplasm, cytoskeleton; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cap (GO:0030478)
- actin cytoskeleton (GO:0015629)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- endocytic vesicle membrane (GO:0030666)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular exosome (GO:0070062)
- glutamatergic synapse (GO:0098978)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 56 |
| PubMed broad count | 451 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. PLD1 promotes spindle assembly and migration through regulating autophagy in mouse oocyte meiosis.. *Autophagy*. PMID: 38513669
2. Loss of Wasl improves pancreatic cancer outcome.. *JCI insight*. PMID: 32434991
3. Actin-nucleation promoting factor N-WASP influences alpha-synuclein condensates and pathology.. *Cell death & disease*. PMID: 38693139
4. FOXP2 suppresses gastric cancer progression by transcriptionally repressing FBXW2 via WASL degradation.. *Cell death discovery*. PMID: 40721413
5. Regulation of Cdc42 and its effectors in epithelial morphogenesis.. *Journal of cell science*. PMID: 31113848

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.7 |
| 高置信度残基 (pLDDT>90) 占比 | 17.6% |
| 置信残基 (pLDDT 70-90) 占比 | 33.7% |
| 中等置信 (pLDDT 50-70) 占比 | 28.1% |
| 低置信 (pLDDT<50) 占比 | 20.6% |
| 有序区域 (pLDDT>70) 占比 | 51.3% |
| 可用 PDB 条目 | 2FF3, 2LNH, 2VCP, 4CC2, 4CC7, 9DLX |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.7），有序残基占 51.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000095, IPR036936, IPR011993, IPR011026, IPR033927; Pfam: PF00786, PF00568, PF02205 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.999 | 0.867 | — |
| WIPF2 | 0.999 | 0.972 | — |
| ARPC1B | 0.999 | 0.967 | — |
| ACTR3 | 0.999 | 0.962 | — |
| CTTN | 0.999 | 0.631 | — |
| NCK1 | 0.999 | 0.811 | — |
| ACTR2 | 0.999 | 0.985 | — |
| ITSN1 | 0.999 | 0.535 | — |
| WIPF1 | 0.999 | 0.952 | — |
| WIPF3 | 0.999 | 0.923 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Fibp | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Git2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| LCK | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-14503|pubmed:16293614 |
| CDC42 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-14503|pubmed:16293614 |
| PTPN2 | psi-mi:"MI:0434"(phosphatase assay) | imex:IM-14503|pubmed:16293614 |
| GRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15417|pubmed:21706016 |
| EP300 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| FCHSD2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ZNF395 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ITGB1BP2 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.7 + PDB: 2FF3, 2LNH, 2VCP, 4CC2, 4CC7,  | pLDDT=68.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Nucleus; Cytoplasm / Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. WASL — Actin nucleation-promoting factor WASL，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小505 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 56 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00401
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106299-WASL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WASL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00401
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000106299-WASL/subcellular

![](https://images.proteinatlas.org/5750/10_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5750/10_A4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/5750/11_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5750/11_A4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/5750/15_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5750/15_A4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00401-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O00401 |
| SMART | SM00285;SM00461;SM00246; |
| UniProt Domain [FT] | DOMAIN 34..141; /note="WH1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00410"; DOMAIN 203..216; /note="CRIB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00057"; DOMAIN 405..422; /note="WH2 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00406"; DOMAIN 433..450; /note="WH2 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00406" |
| InterPro | IPR000095;IPR036936;IPR011993;IPR011026;IPR033927;IPR000697;IPR003124; |
| Pfam | PF00786;PF00568;PF02205; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106299-WASL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTB | Biogrid, Opencell | true |
| ACTG1 | Biogrid, Opencell | true |
| BAIAP2 | Intact, Biogrid | true |
| CDC42 | Intact, Biogrid | true |
| EGFR | Intact, Biogrid | true |
| GRB2 | Intact, Biogrid | true |
| NCK1 | Intact, Biogrid, Bioplex | true |
| NCK2 | Intact, Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
