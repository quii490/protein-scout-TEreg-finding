---
type: protein-evaluation
gene: "KIAA1217"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KIAA1217 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KIAA1217 / SKT |
| 蛋白名称 | Sickle tail protein homolog |
| 蛋白大小 | 1943 aa / 214.1 kDa |
| UniProt ID | Q5T5P2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 5/10 | ×1 | 5 | 1943 aa / 214.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=46.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR022782, IPR051825; Pfam: PF03915 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SKT |

**关键文献**:
1. KIAA1217 Promotes Epithelial-Mesenchymal Transition and Hepatocellular Carcinoma Metastasis by Interacting with and Activating STAT3.. *International journal of molecular sciences*. PMID: 35008530
2. KIAA1217: A novel candidate gene associated with isolated and syndromic vertebral malformations.. *American journal of medical genetics. Part A*. PMID: 32369272
3. The adaptor protein SKT interacts with PSD-95 and SHANK3 and affects synaptic functions.. *Cell reports*. PMID: 40892546
4. Design and characterization of a high-resolution multiple-SNP capture array by target sequencing for sheep.. *Journal of animal science*. PMID: 36402741
5. Androgen receptor-mediated repression of novel target genes.. *The Prostate*. PMID: 17624924

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 46.2 |
| 高置信度残基 (pLDDT>90) 占比 | 7.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 72.5% |
| 有序区域 (pLDDT>70) 占比 | 20.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=46.2），有序残基占 20.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022782, IPR051825; Pfam: PF03915 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IDH3A | 0.824 | 0.000 | — |
| ACAN | 0.710 | 0.071 | — |
| IDH2 | 0.649 | 0.000 | — |
| FBLN1 | 0.515 | 0.052 | — |
| TRIB2 | 0.500 | 0.488 | — |
| GFM1 | 0.492 | 0.000 | — |
| RET | 0.478 | 0.000 | — |
| TMEM270 | 0.477 | 0.000 | — |
| MAPRE1 | 0.459 | 0.458 | — |
| FBLN2 | 0.447 | 0.052 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GCC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRT15 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FXR2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SORBS3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NCK2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EXOSC5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TEX11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ECI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| ECH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| Cyfip2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=46.2 + PDB: 无 | pLDDT=46.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Nucleoplasm, Cytosol | 一致 |
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
1. KIAA1217 — Sickle tail protein homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1943 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=46.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T5P2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120549-KIAA1217/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KIAA1217
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T5P2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000120549-KIAA1217/subcellular

![](https://images.proteinatlas.org/4941/79_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/4941/79_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/4941/80_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/4941/80_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/4941/81_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/4941/81_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5T5P2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5T5P2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR022782;IPR051825; |
| Pfam | PF03915; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120549-KIAA1217/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MAPRE1 | Biogrid, Opencell | true |
| ABI2 | Biogrid | false |
| KRT15 | Biogrid | false |
| NINL | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
