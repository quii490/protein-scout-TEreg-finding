---
type: protein-evaluation
gene: "CRYZL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CRYZL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRYZL1 |
| 蛋白名称 | CRYZL1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | CRYZL1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 5/10 | x1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=8 篇 (<=20->10) |
| 三维结构 | 4/10 | x3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.5/180** | |
| **归一化总分** | | | **59.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 8 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Neurogenetic disorders associated with mutations in the FERRY complex: a novel disease class?. *Biology open*. PMID: 40062705
2. Leveraging Methylation Alterations to Discover Potential Causal Genes Associated With the Survival Risk of Cervical Cancer in TCGA Through a Two-Stage Inference Approach.. *Frontiers in genetics*. PMID: 34149809
3. Identification of a zeta-crystallin (quinone reductase)-like 1 gene (CRYZL1) mapped to human chromosome 21q22.1.. *Genomics*. PMID: 10191096
4. BRINP3 promotes lung adenocarcinoma by enhancing CLOCK-mediated transcriptional regulation of CRYZL1 and activating the AKT pathway.. *Carcinogenesis*. PMID: 40799124
5. Integrating plasma proteomes with genome-wide association data for causal protein identification in hepatocellular carcinoma: A bidirectional Mendelian randomization study.. *Medicine*. PMID: 41578465

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: AlphaFold数据未获取。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP1R21 | 0.942 | 0.939 | — |
| LAP3 | 0.864 | 0.000 | — |
| GATD1 | 0.819 | 0.800 | — |
| MT2A | 0.767 | 0.000 | — |
| SLC40A1 | 0.715 | 0.000 | — |
| C12orf4 | 0.627 | 0.609 | — |
| PSMG1 | 0.570 | 0.000 | — |
| ITPK1 | 0.567 | 0.561 | — |
| FASN | 0.557 | 0.297 | — |
| CRYL1 | 0.557 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-2824812 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TAFA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCP10L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL6R | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ITPK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLXNA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBXL14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CFAP52 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Tbck | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Ctnnbl1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CRYZL1 -- CRYZL1 (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/CRYZL1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205758-CRYZL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRYZL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CRYZL1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000205758-CRYZL1/subcellular

![](https://images.proteinatlas.org/34129/924_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/34129/924_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/34129/932_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/34129/932_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/34129/971_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/34129/971_E12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95825 |
| SMART | SM00829; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013154;IPR042633;IPR020843;IPR011032;IPR036291; |
| Pfam | PF08240; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000205758-CRYZL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PPP1R21 | Intact, Biogrid | true |
| BRCA1 | Biogrid | false |
| C12orf4 | Intact | false |
| GAMT | Bioplex | false |
| GATD1 | Intact | false |
| ITPK1 | Intact | false |
| PLXNA4 | Intact | false |
| TCP10L | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
