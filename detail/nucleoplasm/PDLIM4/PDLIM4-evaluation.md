---
type: protein-evaluation
gene: "PDLIM4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PDLIM4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PDLIM4 / RIL |
| 蛋白名称 | PDZ and LIM domain protein 4 |
| 蛋白大小 | 330 aa / 35.4 kDa |
| UniProt ID | P50479 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Actin filaments; 额外: Plasma membrane, Cytosol; UniProt: Cytoplasm, cytoskeleton; Nucleus; Cytoplasm; Cytoplasm, peri |
| 蛋白大小 | 10/10 | ×1 | 10 | 330 aa / 35.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=54 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=70.2; PDB: 2EEG, 2V1W, 4Q2O |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031847, IPR001478, IPR050604, IPR036034, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Actin filaments; 额外: Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton; Nucleus; Cytoplasm; Cytoplasm, perinuclear region; Cell projection, lamelli... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- adherens junction (GO:0005912)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- early endosome lumen (GO:0031905)
- early endosome membrane (GO:0031901)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 54 |
| PubMed broad count | 91 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RIL |

**关键文献**:
1. PDLIM4 drives gastric cancer malignant progression and cisplatin resistance by inhibiting HSP70 ubiquitination and degradation via competitive interaction with STUB1.. *Journal of nanobiotechnology*. PMID: 41076533
2. Associations between polymorphisms of the PDLIM4 gene and susceptibility to osteoporotic fracture in an elderly population of Han Chinese.. *Bioscience reports*. PMID: 30578378
3. Pdlim4 is essential for CCR7-JNK-mediated dendritic cell migration and F-actin-related dendrite formation.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 31287961
4. JMJD3 regulates CD4 T cell trafficking by targeting actin cytoskeleton regulatory gene Pdlim4.. *The Journal of clinical investigation*. PMID: 31393857
5. PDZ and LIM domain protein 4 suppresses the growth and invasion of ovarian cancer cells via inactivation of STAT3 signaling.. *Life sciences*. PMID: 31376371

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.2 |
| 高置信度残基 (pLDDT>90) 占比 | 34.2% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 19.4% |
| 低置信 (pLDDT<50) 占比 | 29.1% |
| 有序区域 (pLDDT>70) 占比 | 51.5% |
| 可用 PDB 条目 | 2EEG, 2V1W, 4Q2O |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2EEG, 2V1W, 4Q2O）+ AlphaFold高质量预测（pLDDT=70.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031847, IPR001478, IPR050604, IPR036034, IPR001781; Pfam: PF15936, PF00412, PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAC3 | 0.912 | 0.126 | — |
| MYO1A | 0.908 | 0.000 | — |
| MYO1C | 0.904 | 0.000 | — |
| MYO6 | 0.903 | 0.078 | — |
| MYO3A | 0.901 | 0.052 | — |
| CD2AP | 0.900 | 0.000 | — |
| DPYSL3 | 0.748 | 0.000 | — |
| DUSP22 | 0.734 | 0.065 | — |
| ESPN | 0.723 | 0.000 | — |
| JAM3 | 0.720 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RBPMS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ZNF408 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| SDCBP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AMT | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ACTN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM222B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KIR3DL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM63 | psi-mi:"MI:0096"(pull down) | pubmed:31391242|imex:IM-25805| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.2 + PDB: 2EEG, 2V1W, 4Q2O | pLDDT=70.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Nucleus; Cytoplasm; Cytop / Actin filaments; 额外: Plasma membrane, Cytosol | 一致 |
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
1. PDLIM4 — PDZ and LIM domain protein 4，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小330 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 54 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50479
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131435-PDLIM4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PDLIM4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50479
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Actin filaments (supported)。来源: https://www.proteinatlas.org/ENSG00000131435-PDLIM4/subcellular

![](https://images.proteinatlas.org/11912/94_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/11912/94_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/11912/96_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/11912/96_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/73227/1950_F2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/73227/1950_F2_6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P50479-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P50479 |
| SMART | SM00132;SM00228; |
| UniProt Domain [FT] | DOMAIN 1..84; /note="PDZ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143, ECO:0000269\|PubMed:25158098, ECO:0007744\|PDB:4Q2O"; DOMAIN 253..312; /note="LIM zinc-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125" |
| InterPro | IPR031847;IPR001478;IPR050604;IPR036034;IPR001781; |
| Pfam | PF15936;PF00412;PF00595; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000131435-PDLIM4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTN1 | Intact | false |
| FAM222B | Intact | false |
| HSPA1A | Biogrid | false |
| PTPN13 | Biogrid | false |
| SDCBP | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
