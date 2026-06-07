---
type: protein-evaluation
gene: "RNASEH1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RNASEH1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RNASEH1 / RNH1 |
| 蛋白名称 | Ribonuclease H1 |
| 蛋白大小 | 286 aa / 32.1 kDa |
| UniProt ID | O60930 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 286 aa / 32.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=57 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.5; PDB: 2QK9, 2QKB, 2QKK, 3BSU, 6VRD, 8SWB, 8SWC |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009027, IPR050092, IPR017067, IPR011320, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 57 |
| PubMed broad count | 113 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNH1 |

**关键文献**:
1. Topoisomerase 1 Inhibition in MYC-Driven Cancer Promotes Aberrant R-Loop Accumulation to Induce Synthetic Lethality.. *Cancer research*. PMID: 37987734
2. R-ChIP Using Inactive RNase H Reveals Dynamic Coupling of R-loops with Transcriptional Pausing at Gene Promoters.. *Molecular cell*. PMID: 29104020
3. Nucleolar RNA polymerase II drives ribosome biogenesis.. *Nature*. PMID: 32669707
4. Design and screening of novel endosomal escape compounds that enhance functional delivery of oligonucleotides in vitro.. *Molecular therapy. Nucleic acids*. PMID: 40235852
5. Mitochondrial DNA maintenance defects.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 28215579

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.5 |
| 高置信度残基 (pLDDT>90) 占比 | 62.6% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 24.5% |
| 有序区域 (pLDDT>70) 占比 | 72.7% |
| 可用 PDB 条目 | 2QK9, 2QKB, 2QKK, 3BSU, 6VRD, 8SWB, 8SWC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2QK9, 2QKB, 2QKK, 3BSU, 6VRD, 8SWB, 8SWC）+ AlphaFold极高置信度预测（pLDDT=79.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009027, IPR050092, IPR017067, IPR011320, IPR037056; Pfam: PF01693, PF00075 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RNASEH2A | 0.951 | 0.828 | — |
| SSBP1 | 0.922 | 0.766 | — |
| TYMS | 0.892 | 0.000 | — |
| TWNK | 0.869 | 0.000 | — |
| NUDT12 | 0.847 | 0.067 | — |
| NADK | 0.825 | 0.000 | — |
| GAPDH | 0.810 | 0.000 | — |
| NUDT13 | 0.809 | 0.000 | — |
| SETX | 0.788 | 0.088 | — |
| GAPDHS | 0.761 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.5 + PDB: 2QK9, 2QKB, 2QKK, 3BSU, 6VRD,  | pLDDT=79.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. RNASEH1 — Ribonuclease H1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小286 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 57 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60930
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171865-RNASEH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RNASEH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60930
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000171865-RNASEH1/subcellular

![](https://images.proteinatlas.org/34817/1056_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/34817/1056_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/34817/1128_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/34817/1128_G9_4_red_green.jpg)
![](https://images.proteinatlas.org/34817/1293_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/34817/1293_G11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60930-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60930 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 136..282; /note="RNase H type-1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00408" |
| InterPro | IPR009027;IPR050092;IPR017067;IPR011320;IPR037056;IPR012337;IPR002156;IPR036397; |
| Pfam | PF01693;PF00075; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171865-RNASEH1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BHLHA15 | Bioplex | false |
| CHCHD2 | Biogrid | false |
| EMD | Intact | false |
| FAM3C | Intact | false |
| LUC7L | Intact | false |
| MZF1 | Bioplex | false |
| NCS1 | Intact | false |
| NRM | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
