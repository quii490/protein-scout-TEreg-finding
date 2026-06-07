---
type: protein-evaluation
gene: "TLCD4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TLCD4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TLCD4 / TMEM56 |
| 蛋白名称 | TLC domain-containing protein 4 |
| 蛋白大小 | 263 aa / 30.0 kDa |
| UniProt ID | Q96MV1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear speckles; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 263 aa / 30.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006634, IPR050846; Pfam: PF03798 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TMEM56 |

**关键文献**:
1. TRAM-LAG1-CLN8 domain-containing protein TMEM56 regulates cell migration by changing intracellular ceramide levels.. *BMC biology*. PMID: 42087192
2. Spatial transcriptomics and single-nucleus RNA sequencing reveal rAAV2- and rAAV9-specific transduction signatures in the mouse liver.. *Gene therapy*. PMID: 41813829
3. TLCD4 as Potential Transcriptomic Biomarker of Cold Exposure.. *Biomolecules*. PMID: 39199323
4. Consensus analysis via weighted gene co-expression network analysis (WGCNA) reveals genes participating in early phase of acute respiratory distress syndrome (ARDS) induced by sepsis.. *Bioengineered*. PMID: 33818300

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.1 |
| 高置信度残基 (pLDDT>90) 占比 | 86.7% |
| 置信残基 (pLDDT 70-90) 占比 | 10.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 0.4% |
| 有序区域 (pLDDT>70) 占比 | 97.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.1，有序区 97.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006634, IPR050846; Pfam: PF03798 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| METTL8 | 0.646 | 0.000 | — |
| HEXIM2 | 0.562 | 0.000 | — |
| LRGUK | 0.521 | 0.509 | — |
| MBOAT2 | 0.503 | 0.000 | — |
| SMIM3 | 0.492 | 0.000 | — |
| KDELR3 | 0.467 | 0.467 | — |
| GATA1 | 0.465 | 0.000 | — |
| DNAJC6 | 0.464 | 0.000 | — |
| GFI1B | 0.459 | 0.102 | — |
| HEMGN | 0.457 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COX4I1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| YIPF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC22A9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KRT1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| GYPA | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| DHRSX | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SEC22B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| UBE2J1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SYNDIG1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MS4A13 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.1 + PDB: 无 | pLDDT=94.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TLCD4 — TLC domain-containing protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小263 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96MV1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152078-TLCD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TLCD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96MV1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000152078-TLCD4/subcellular

![](https://images.proteinatlas.org/46762/1421_H1_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/46762/1421_H1_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/46762/835_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46762/835_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46762/844_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46762/844_D11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96MV1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96MV1 |
| SMART | SM00724; |
| UniProt Domain [FT] | DOMAIN 44..246; /note="TLC"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00205" |
| InterPro | IPR006634;IPR050846; |
| Pfam | PF03798; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000152078-TLCD4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ADGRB3 | Intact | false |
| ADGRE2 | Intact | false |
| ARV1 | Intact | false |
| BNIP3 | Intact | false |
| CACNG1 | Intact | false |
| CCDC167 | Intact | false |
| CDIPT | Intact | false |
| CHPT1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
