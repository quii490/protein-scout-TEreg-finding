---
type: protein-evaluation
gene: "CCSER2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCSER2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCSER2 / FAM190B, KIAA1128 |
| 蛋白名称 | Serine-rich coiled-coil domain-containing protein 2 |
| 蛋白大小 | 834 aa / 93.5 kDa |
| UniProt ID | Q9H7U1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 8/10 | ×1 | 8 | 834 aa / 93.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029627 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- microtubule cytoskeleton (GO:0015630)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM190B, KIAA1128 |

**关键文献**:
1. Downregulation of MALAT1 in triple-negative breast cancer cells.. *Biochemistry and biophysics reports*. PMID: 38088951
2. Tumor-Infiltrated CD8+ T Cell 10-Gene Signature Related to Clear Cell Renal Cell Carcinoma Prognosis.. *Frontiers in immunology*. PMID: 35812454
3. CCSer2 gates dynein activity at the cell periphery.. *The Journal of cell biology*. PMID: 40261303
4. Characterization of human Ccser2 as a protein tracking the plus-ends of microtubules.. *BMC research notes*. PMID: 37684684
5. CCSer2 gates dynein activity at the cell periphery.. *bioRxiv : the preprint server for biology*. PMID: 38915497

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.3 |
| 高置信度残基 (pLDDT>90) 占比 | 6.0% |
| 置信残基 (pLDDT 70-90) 占比 | 1.8% |
| 中等置信 (pLDDT 50-70) 占比 | 17.5% |
| 低置信 (pLDDT<50) 占比 | 74.7% |
| 有序区域 (pLDDT>70) 占比 | 7.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.3），有序残基占 7.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029627 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDEL1 | 0.825 | 0.628 | — |
| DYDC1 | 0.555 | 0.000 | — |
| NDE1 | 0.514 | 0.000 | — |
| SYNE1 | 0.504 | 0.000 | — |
| DYDC2 | 0.483 | 0.000 | — |
| PUM1 | 0.460 | 0.000 | — |
| CCDC141 | 0.460 | 0.000 | — |
| TSPAN14 | 0.458 | 0.000 | — |
| LUZP1 | 0.444 | 0.000 | — |
| SYMPK | 0.443 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATRX | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CRADD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GTF2H1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PSMD11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| STX1A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TCEA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NDEL1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| EXOC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| Nde1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.3 + PDB: 无 | pLDDT=48.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / Nucleoplasm, Cytosol | 一致 |
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
1. CCSER2 — Serine-rich coiled-coil domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小834 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=48.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H7U1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107771-CCSER2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCSER2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H7U1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000107771-CCSER2/subcellular

![](https://images.proteinatlas.org/37482/537_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/37482/537_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/37482/540_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/37482/540_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/37482/553_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/37482/553_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H7U1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H7U1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029627; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000107771-CCSER2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NDEL1 | Intact, Biogrid | true |
| DYNLL1 | Biogrid | false |
| DYNLL2 | Biogrid | false |
| DYRK2 | Biogrid | false |
| EXOC1 | Intact | false |
| MAPRE1 | Biogrid | false |
| PAFAH1B1 | Biogrid | false |
| YWHAB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
