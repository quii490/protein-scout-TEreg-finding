---
type: protein-evaluation
gene: "GABARAPL2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GABARAPL2 — REJECTED (研究热度过高 (PubMed strict=132，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GABARAPL2 / FLC3A, GEF2 |
| 蛋白名称 | Gamma-aminobutyric acid receptor-associated protein-like 2 |
| 蛋白大小 | 117 aa / 13.7 kDa |
| UniProt ID | P60520 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Nuclear bodies; UniProt: Cytoplasmic vesicle, autophagosome; Endoplasmic reticulum me |
| 蛋白大小 | 8/10 | ×1 | 8 | 117 aa / 13.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=132 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.8; PDB: 4CO7, 6H8C, 7LK3, 7YO8, 8Q6Q |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004241, IPR029071; Pfam: PF02991 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.0/180** | |
| **归一化总分** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nuclear bodies | Uncertain |
| UniProt | Cytoplasmic vesicle, autophagosome; Endoplasmic reticulum membrane; Golgi apparatus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- autophagosome (GO:0005776)
- autophagosome membrane (GO:0000421)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 132 |
| PubMed broad count | 269 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FLC3A, GEF2 |

**关键文献**:
1. SIRT5 regulation of ammonia-induced autophagy and mitophagy.. *Autophagy*. PMID: 25700560
2. LC3/GABARAP family proteins: autophagy-(un)related functions.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 27601442
3. IRGQ-mediated autophagy in MHC class I quality control promotes tumor immune evasion.. *Cell*. PMID: 39481378
4. Identification and analysis of type 2 diabetes-mellitus-associated autophagy-related genes.. *Frontiers in endocrinology*. PMID: 37223013
5. Keratinocyte autophagy enables the activation of keratinocytes and fibroblastsand facilitates wound healing.. *Autophagy*. PMID: 32866426

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.8 |
| 高置信度残基 (pLDDT>90) 占比 | 90.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 97.4% |
| 可用 PDB 条目 | 4CO7, 6H8C, 7LK3, 7YO8, 8Q6Q |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4CO7, 6H8C, 7LK3, 7YO8, 8Q6Q）+ AlphaFold极高置信度预测（pLDDT=94.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004241, IPR029071; Pfam: PF02991 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATG12 | 0.999 | 0.292 | — |
| SQSTM1 | 0.999 | 0.892 | — |
| NBR1 | 0.999 | 0.852 | — |
| ATG7 | 0.999 | 0.916 | — |
| ATG5 | 0.999 | 0.332 | — |
| ATG3 | 0.999 | 0.919 | — |
| BNIP3L | 0.999 | 0.329 | — |
| ATG4B | 0.999 | 0.853 | — |
| OPTN | 0.998 | 0.425 | — |
| BNIP3 | 0.997 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000037243.2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| CALCOCO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BCL2L13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBA5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MLX | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TBC1D5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SQSTM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ATG4B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| LRSAM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ATG7 | psi-mi:"MI:0404"(comigration in non denaturing gel | imex:IM-14513|pubmed:16303767 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.8 + PDB: 4CO7, 6H8C, 7LK3, 7YO8, 8Q6Q | pLDDT=94.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle, autophagosome; Endoplasmic re / Nucleoplasm, Cytosol; 额外: Nuclear bodies | 一致 |
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
1. GABARAPL2 — Gamma-aminobutyric acid receptor-associated protein-like 2，研究基础较多，新颖性有限。
2. 蛋白大小117 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 132 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 132 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P60520
- Protein Atlas: https://www.proteinatlas.org/ENSG00000034713-GABARAPL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GABARAPL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P60520
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000034713-GABARAPL2/subcellular

![](https://images.proteinatlas.org/36726/422_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/36726/422_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/36726/423_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/36726/423_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/36726/426_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/36726/426_D11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P60520-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
