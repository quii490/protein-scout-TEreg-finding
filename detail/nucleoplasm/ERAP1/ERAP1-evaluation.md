---
type: protein-evaluation
gene: "ERAP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERAP1 — REJECTED (研究热度过高 (PubMed strict=275，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERAP1 / APPILS, ARTS1, KIAA0525 |
| 蛋白名称 | Endoplasmic reticulum aminopeptidase 1 |
| 蛋白大小 | 941 aa / 107.2 kDa |
| UniProt ID | Q9NZ08 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Plasma membrane; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 941 aa / 107.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=275 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.4; PDB: 2YD0, 3MDJ, 3QNF, 3RJO, 5J5E, 6M8P, 6MGQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045357, IPR042097, IPR024571, IPR034016, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.0/180** | |
| **归一化总分** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Plasma membrane | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum lumen (GO:0005788)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 275 |
| PubMed broad count | 626 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APPILS, ARTS1, KIAA0525 |

**关键文献**:
1. Understanding the Pathogenesis of Spondyloarthritis.. *Biomolecules*. PMID: 33092023
2. An observational and genetic investigation into the association between psoriasis and risk of malignancy.. *Nature communications*. PMID: 39261450
3. Combining ERAP1 silencing and entinostat therapy to overcome resistance to cancer immunotherapy in neuroblastoma.. *Journal of experimental & clinical cancer research : CR*. PMID: 39438988
4. Etiopathogenesis of Behçet's disease: A systematic literature review.. *Clinical immunology (Orlando, Fla.)*. PMID: 40571238
5. Mendelian randomization analysis identifies ERAP1 and IL23R as potential drug targets for ankylosing spondylitis.. *Life sciences*. PMID: 40349828

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.4 |
| 高置信度残基 (pLDDT>90) 占比 | 89.1% |
| 置信残基 (pLDDT 70-90) 占比 | 2.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 7.2% |
| 有序区域 (pLDDT>70) 占比 | 91.1% |
| 可用 PDB 条目 | 2YD0, 3MDJ, 3QNF, 3RJO, 5J5E, 6M8P, 6MGQ, 6Q4R, 6RQX, 6RYF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2YD0, 3MDJ, 3QNF, 3RJO, 5J5E, 6M8P, 6MGQ, 6Q4R, 6RQX, 6RYF）+ AlphaFold极高置信度预测（pLDDT=92.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045357, IPR042097, IPR024571, IPR034016, IPR001930; Pfam: PF11838, PF01433, PF17900 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NUCB2 | 0.924 | 0.000 | — |
| HLA-C | 0.887 | 0.000 | — |
| HLA-B | 0.876 | 0.238 | — |
| TPP2 | 0.868 | 0.000 | — |
| TAPBP | 0.827 | 0.000 | — |
| IL23R | 0.800 | 0.000 | — |
| ANTXR2 | 0.776 | 0.000 | — |
| TNF | 0.728 | 0.000 | — |
| TNFRSF1A | 0.699 | 0.230 | — |
| IFNG | 0.676 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IL6R | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:12748171 |
| TNFRSF1A | psi-mi:"MI:0018"(two hybrid) | pubmed:12189246 |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| yapH | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TMEM87A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC16A10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MUL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APOL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ROMO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| USP20 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.4 + PDB: 2YD0, 3MDJ, 3QNF, 3RJO, 5J5E,  | pLDDT=92.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nucleoplasm, Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ERAP1 — Endoplasmic reticulum aminopeptidase 1，研究基础较多，新颖性有限。
2. 蛋白大小941 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 275 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 275 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZ08
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164307-ERAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZ08
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000164307-ERAP1/subcellular

![](https://images.proteinatlas.org/42317/692_B4_6_red_green.jpg)
![](https://images.proteinatlas.org/42317/692_B4_7_red_green.jpg)
![](https://images.proteinatlas.org/42317/754_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/42317/754_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/42317/758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/42317/758_B1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NZ08-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NZ08 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR045357;IPR042097;IPR024571;IPR034016;IPR001930;IPR050344;IPR014782;IPR027268; |
| Pfam | PF11838;PF01433;PF17900; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164307-ERAP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ERAP2 | Intact | false |
| PRNP | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
