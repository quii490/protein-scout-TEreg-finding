---
type: protein-evaluation
gene: "GRHL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GRHL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GRHL1 / LBP32, MGR, TFCP2L2 |
| 蛋白名称 | Grainyhead-like protein 1 homolog |
| 蛋白大小 | 618 aa / 70.1 kDa |
| UniProt ID | Q9NZI5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 618 aa / 70.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=55 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.1; PDB: 5MPF, 5MPH, 5MPI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007604, IPR057520, IPR040167; Pfam: PF04516, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 55 |
| PubMed broad count | 81 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LBP32, MGR, TFCP2L2 |

**关键文献**:
1. Glucose modulates IRF6 transcription factor dimerization to enable epidermal differentiation.. *Cell stem cell*. PMID: 40120584
2. Recurrent FOXK1::GRHL and GPS2::GRHL fusions in trichogerminoma.. *The Journal of pathology*. PMID: 35049062
3. Exploration of the Correlation Between GRHL1 Expression and Tumor Microenvironment in Endometrial Cancer and Immunotherapy.. *Pharmacogenomics and personalized medicine*. PMID: 38586176
4. GRHL1 acts as tumor suppressor in neuroblastoma and is negatively regulated by MYCN and HDAC3.. *Cancer research*. PMID: 24419085
5. TFCP2/TFCP2L1/UBP1 transcription factors in cancer.. *Cancer letters*. PMID: 29410248

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.1 |
| 高置信度残基 (pLDDT>90) 占比 | 37.1% |
| 置信残基 (pLDDT 70-90) 占比 | 14.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 41.4% |
| 有序区域 (pLDDT>70) 占比 | 51.3% |
| 可用 PDB 条目 | 5MPF, 5MPH, 5MPI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.1），有序残基占 51.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007604, IPR057520, IPR040167; Pfam: PF04516, PF25416 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYP11A1 | 0.609 | 0.049 | — |
| GRHL2 | 0.565 | 0.518 | — |
| ZNF76 | 0.555 | 0.470 | — |
| ESRP1 | 0.539 | 0.000 | — |
| TGM1 | 0.532 | 0.000 | — |
| ZNF750 | 0.532 | 0.000 | — |
| GRHL3 | 0.530 | 0.292 | — |
| OVOL1 | 0.522 | 0.000 | — |
| PPARA | 0.506 | 0.051 | — |
| OVOL2 | 0.502 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRHL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF76 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UTP3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| Erp44 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.1 + PDB: 5MPF, 5MPH, 5MPI | pLDDT=67.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

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
1. GRHL1 — Grainyhead-like protein 1 homolog，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小618 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 55 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZI5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134317-GRHL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GRHL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZI5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GRHL1/IF_images/A-431_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GRHL1/IF_images/NIH-3T3_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000134317-GRHL1/subcellular

![](https://images.proteinatlas.org/6420/1843_H1_31_red_green.jpg)
![](https://images.proteinatlas.org/6420/1843_H1_32_red_green.jpg)
![](https://images.proteinatlas.org/6420/1924_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/6420/1924_B2_5_red_green.jpg)
![](https://images.proteinatlas.org/6420/927_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/6420/927_G2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NZI5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NZI5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 248..474; /note="Grh/CP2 DB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01313" |
| InterPro | IPR007604;IPR057520;IPR040167; |
| Pfam | PF04516;PF25416; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134317-GRHL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GRHL2 | Intact | false |
| GRHL3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
