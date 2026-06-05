---
type: protein-evaluation
gene: "GFUS"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GFUS 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GFUS / SDR4E1, TSTA3 |
| 蛋白名称 | GDP-L-fucose synthase |
| 蛋白大小 | 321 aa / 35.9 kDa |
| UniProt ID | Q13630 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 321 aa / 35.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=95.8; PDB: 4B8W, 4B8Z, 4BKP, 4BL5, 4E5Y |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001509, IPR028614, IPR036291; Pfam: PF01370 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SDR4E1, TSTA3 |

**关键文献**:
1. Congenital disorders of glycosylation with defective fucosylation.. *Journal of inherited metabolic disease*. PMID: 34389986
2. Genome-Wide Association Study of Lactation Traits in Chinese Holstein Cows in Southern China.. *Animals : an open access journal from MDPI*. PMID: 37570353
3. Bioinformatics and machine learning integration reveals a novel 4-gene (GFUS, ARHGAP8, NBL1, and ACTB) biomarker model for prostate cancer.. *Discover oncology*. PMID: 41721923
4. Identification and Validation of a Novel Glycolysis-Related Gene Signature for Predicting the Prognosis and Therapeutic Response in Triple-Negative Breast Cancer.. *Advances in therapy*. PMID: 36316558
5. Increased expression of fibroblast growth factors in a rabbit skeletal muscle model of exercise conditioning.. *The Journal of clinical investigation*. PMID: 2347914

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.8 |
| 高置信度残基 (pLDDT>90) 占比 | 91.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 98.2% |
| 可用 PDB 条目 | 4B8W, 4B8Z, 4BKP, 4BL5, 4E5Y |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4B8W, 4B8Z, 4BKP, 4BL5, 4E5Y）+ AlphaFold极高置信度预测（pLDDT=95.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001509, IPR028614, IPR036291; Pfam: PF01370 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GMDS | 0.999 | 0.091 | — |
| FPGT | 0.965 | 0.000 | — |
| FAU | 0.949 | 0.945 | — |
| UBE2L5 | 0.902 | 0.066 | — |
| FCSK | 0.825 | 0.000 | — |
| GALE | 0.791 | 0.219 | — |
| UGDH | 0.771 | 0.086 | — |
| SHARPIN | 0.695 | 0.000 | — |
| RPS3A | 0.629 | 0.505 | — |
| RPL23 | 0.623 | 0.507 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000487640.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ID2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RIOK2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CLVS2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PCBP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GOT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| STX17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| OR2A4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TBC1D22B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPP2R2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.8 + PDB: 4B8W, 4B8Z, 4BKP, 4BL5, 4E5Y | pLDDT=95.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GFUS — GDP-L-fucose synthase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小321 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13630
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104522-GFUS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GFUS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13630
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000104522-GFUS/subcellular

![](https://images.proteinatlas.org/23361/284_E4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/23361/284_E4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/23361/285_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23361/285_E4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23361/286_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23361/286_E4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13630-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
