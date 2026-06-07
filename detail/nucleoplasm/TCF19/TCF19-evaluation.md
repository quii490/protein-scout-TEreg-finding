---
type: protein-evaluation
gene: "TCF19"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TCF19 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCF19 / SC1 |
| 蛋白名称 | Transcription factor 19 |
| 蛋白大小 | 345 aa / 37.2 kDa |
| UniProt ID | Q9Y242 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 345 aa / 37.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000253, IPR008984, IPR042803, IPR039095, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 68 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SC1 |

**关键文献**:
1. Deciphering the TCF19/miR-199a-5p/SP1/LOXL2 pathway: Implications for breast cancer metastasis and epithelial-mesenchymal transition.. *Cancer letters*. PMID: 38851313
2. TCF19 expression and significance analysis in breast cancer: integrated bioinformatics analysis and histological validation.. *Discover oncology*. PMID: 40493298
3. TCF19/CDKN2A Regulates Glycolysis and Macrophage M2 Polarization for Osteosarcoma Progression.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 40193126
4. Downregulation of TCF19 and ATAD2 causes endothelial cell cycle arrest at the transition from cardiac hypertrophy to heart failure.. *Basic research in cardiology*. PMID: 40962957
5. TCF7l2 Regulates Fatty Acid Chain Elongase HACD3 during Lipid-Induced Stress.. *Biochemistry*. PMID: 40172138

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.6 |
| 高置信度残基 (pLDDT>90) 占比 | 11.6% |
| 置信残基 (pLDDT 70-90) 占比 | 32.8% |
| 中等置信 (pLDDT 50-70) 占比 | 12.2% |
| 低置信 (pLDDT<50) 占比 | 43.5% |
| 有序区域 (pLDDT>70) 占比 | 44.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.6），有序残基占 44.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000253, IPR008984, IPR042803, IPR039095, IPR019786; Pfam: PF00498, PF00628 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCHCR1 | 0.799 | 0.000 | — |
| HLA-C | 0.757 | 0.000 | — |
| POU5F1 | 0.710 | 0.000 | — |
| PRMT5 | 0.706 | 0.000 | — |
| CDCA8 | 0.653 | 0.047 | — |
| CDK1 | 0.646 | 0.000 | — |
| CDSN | 0.646 | 0.000 | — |
| CDCA3 | 0.613 | 0.000 | — |
| BIRC5 | 0.602 | 0.052 | — |
| PSORS1C1 | 0.594 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| DNAJA3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| GOLGA2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PRKAB2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| HSF2BP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNF474 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PDLIM7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRIB3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NFKBID | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RHOH | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.6 + PDB: 无 | pLDDT=62.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli | 一致 |
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
1. TCF19 — Transcription factor 19，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小345 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y242
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137310-TCF19/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCF19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y242
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000137310-TCF19/subcellular

![](https://images.proteinatlas.org/47093/1607_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/47093/1607_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/47093/1667_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/47093/1667_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/47093/1717_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/47093/1717_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y242-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y242 |
| SMART | SM00240;SM00249; |
| UniProt Domain [FT] | DOMAIN 31..88; /note="FHA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00086" |
| InterPro | IPR000253;IPR008984;IPR042803;IPR039095;IPR019786;IPR011011;IPR001965;IPR019787;IPR013083; |
| Pfam | PF00498;PF00628; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137310-TCF19/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BLZF1 | Intact | false |
| CEP76 | Intact | false |
| DDIT4L | Intact | false |
| E2F6 | Intact | false |
| GOLGA2 | Intact | false |
| H3-4 | Biogrid | false |
| H4C16 | Biogrid | false |
| HSF2BP | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
