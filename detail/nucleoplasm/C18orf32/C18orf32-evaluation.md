---
type: protein-evaluation
gene: "C18orf32"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C18orf32 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C18orf32 |
| 蛋白名称 | UPF0729 protein C18orf32 |
| 蛋白大小 | 76 aa / 8.7 kDa |
| UniProt ID | Q8TCD1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Endoplasmic reticulum; Lipid droplet |
| 蛋白大小 | 5/10 | ×1 | 5 | 76 aa / 8.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026776; Pfam: PF14975 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | Endoplasmic reticulum; Lipid droplet | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- lipid droplet (GO:0005811)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Longitudinal APOE4- and amyloid-dependent changes in the blood transcriptome in cognitively intact older adults.. *Alzheimer's research & therapy*. PMID: 37438770
2. C18orf32 loss-of-function is associated with a neurodevelopmental disorder with hypotonia and contractures.. *Human genetics*. PMID: 35107634
3. Overexpression of KLHL23 protein from read-through transcription of PHOSPHO2-KLHL23 in gastric cancer increases cell proliferation.. *FEBS open bio*. PMID: 27833855

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.7 |
| 高置信度残基 (pLDDT>90) 占比 | 6.6% |
| 置信残基 (pLDDT 70-90) 占比 | 36.8% |
| 中等置信 (pLDDT 50-70) 占比 | 34.2% |
| 低置信 (pLDDT<50) 占比 | 22.4% |
| 有序区域 (pLDDT>70) 占比 | 43.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.7），有序残基占 43.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026776; Pfam: PF14975 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDUFS5 | 0.523 | 0.000 | — |
| OCIAD1 | 0.496 | 0.000 | — |
| ATP5ME | 0.485 | 0.000 | — |
| UQCR10 | 0.482 | 0.000 | — |
| RPL23A | 0.479 | 0.000 | — |
| UBAC2 | 0.474 | 0.000 | — |
| NDUFA5 | 0.471 | 0.000 | — |
| RPS14 | 0.469 | 0.000 | — |
| PHOSPHO2 | 0.446 | 0.000 | — |
| ETFRF1 | 0.444 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| TCTN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| GLP1R | psi-mi:"MI:1320"(membrane yeast two hybrid) | pubmed:23864651|imex:IM-30241 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.7 + PDB: 无 | pLDDT=65.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum; Lipid droplet / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

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
1. C18orf32 — UPF0729 protein C18orf32，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小76 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TCD1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177576-C18orf32/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C18orf32
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TCD1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000177576-C18orf32/subcellular

![](https://images.proteinatlas.org/40921/418_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/40921/418_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/40921/424_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/40921/424_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/40921/429_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/40921/429_G5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TCD1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TCD1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026776; |
| Pfam | PF14975; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177576-C18orf32/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GLP1R | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
