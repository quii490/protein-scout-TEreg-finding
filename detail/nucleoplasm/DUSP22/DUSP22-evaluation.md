---
type: protein-evaluation
gene: "DUSP22"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUSP22 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP22 / JSP1, LMWDSP2, MKPX |
| 蛋白名称 | Dual specificity protein phosphatase 22 |
| 蛋白大小 | 184 aa / 20.9 kDa |
| UniProt ID | Q9NRW4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 184 aa / 20.9 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=99 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.9; PDB: 1WRM, 4WOH, 6L1S, 6LMY, 6LOT, 6LOU, 6LVQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000340, IPR029021, IPR000387, IPR020422; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- filamentous actin (GO:0031941)
- leading edge of lamellipodium (GO:0061851)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 99 |
| PubMed broad count | 212 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: JSP1, LMWDSP2, MKPX |

**关键文献**:
1. Hepatocyte phosphatase DUSP22 mitigates NASH-HCC progression by targeting FAK.. *Nature communications*. PMID: 36209205
2. DUSP22 suppresses prostate cancer proliferation by targeting the EGFR-AR axis.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 31693867
3. Protein phosphatases in systemic autoimmunity.. *Immunometabolism (Cobham, Surrey)*. PMID: 39944077
4. MAP4K Family Kinases and DUSP Family Phosphatases in T-Cell Signaling and Systemic Lupus Erythematosus.. *Cells*. PMID: 31766293
5. Immunohistochemical Approach to Genetic Subtyping of Anaplastic Large Cell Lymphoma.. *The American journal of surgical pathology*. PMID: 35941721

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.9 |
| 高置信度残基 (pLDDT>90) 占比 | 90.8% |
| 置信残基 (pLDDT 70-90) 占比 | 1.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 91.9% |
| 可用 PDB 条目 | 1WRM, 4WOH, 6L1S, 6LMY, 6LOT, 6LOU, 6LVQ, 7C8S |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1WRM, 4WOH, 6L1S, 6LMY, 6LOT, 6LOU, 6LVQ, 7C8S）+ AlphaFold极高置信度预测（pLDDT=93.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000340, IPR029021, IPR000387, IPR020422; Pfam: PF00782 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAC3 | 0.739 | 0.099 | — |
| PDLIM4 | 0.734 | 0.065 | — |
| ESPN | 0.727 | 0.068 | — |
| DPYSL3 | 0.721 | 0.000 | — |
| CD2AP | 0.720 | 0.000 | — |
| MYO1C | 0.720 | 0.000 | — |
| MYO1A | 0.720 | 0.000 | — |
| JAM3 | 0.720 | 0.000 | — |
| MYO6 | 0.720 | 0.000 | — |
| MYO3A | 0.720 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.9 + PDB: 1WRM, 4WOH, 6L1S, 6LMY, 6LOT,  | pLDDT=93.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Vesicles | 一致 |
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
1. DUSP22 — Dual specificity protein phosphatase 22，研究基础较多，新颖性有限。
2. 蛋白大小184 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 99 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRW4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112679-DUSP22/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRW4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000112679-DUSP22/subcellular

![](https://images.proteinatlas.org/31394/321_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/31394/321_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/31394/323_G7_3_red_green.jpg)
![](https://images.proteinatlas.org/31394/323_G7_4_red_green.jpg)
![](https://images.proteinatlas.org/31394/326_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/31394/326_G7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRW4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NRW4 |
| SMART | SM00195; |
| UniProt Domain [FT] | DOMAIN 4..144; /note="Tyrosine-protein phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160" |
| InterPro | IPR000340;IPR029021;IPR000387;IPR020422; |
| Pfam | PF00782; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112679-DUSP22/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HRAS | Biogrid | false |
| RAP1A | Biogrid | false |
| SVIP | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
