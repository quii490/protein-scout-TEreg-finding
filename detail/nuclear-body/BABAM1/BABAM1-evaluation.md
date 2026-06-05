---
type: protein-evaluation
gene: "BABAM1"
date: 2026-06-03
tags: [protein-scout, nuclear-body, evaluation]
status: scored
---

## BABAM1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | BABAM1 / C19orf62, MERIT40, NBA1 |
| 蛋白全名 | BRISC and BRCA1-A complex member 1 |
| 蛋白大小 | 329 aa / 36.6 kDa |
| UniProt ID | Q9NWV8 (BABAM1_HUMAN) |
| 功能描述 | Component of the BRCA1-A complex, a complex that specifically recognizes 'Lys-63'-linked ubiquitinated histones H2A and H2AX at DNA lesions sites, leading to target the BRCA1-BARD1 heterodimer to sites of DNA damage at double-strand breaks (DSBs). The BRCA1-A complex also possesses deubiquitinase activity that specifically removes 'Lys-63'-linked ubiquitin on histones H2A and H2AX. In the BRCA1-A ... |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32.0 | UniProt experimental nuclear + (Cytoplasm, Nucleus) |
| 蛋白大小 | 10/10 | x1 | 10.0 | 329 aa / 36.6 kDa, 300-800理想区间 |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed strict=8（极低研究量，≤20→10分） |
| 三维结构 | 8/10 | x3 | 24.0 | PDB cryo-EM (3 entries); AF mean pLDDT 78.2 |
| 调控结构域 | 8/10 | x2 | 16.0 | Chromatin-associated regulatory protein |
| PPI 网络 | 3/10 | x3 | 9.0 | IntAct experiment: 15 partners (0 regulatory: none identified) |
| 互证加分 | — | — | +1.0 | >=2 source nuclear localization; domain annotation + nuclear localization |
| **加权总分** | | | **141/180****** | |
| **归一化总分 (÷1.83)** | | | **77.0/100****** | |

### 3. HPA 免疫荧光分析

| HPA 主定位 | Nuclear bodies |
| HPA 额外定位 | Nucleoplasm, Cytosol |
| 抗体可靠性 | Supported |
| IF 图像 | IF images available (4 cell lines) |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 4. PubMed 文献

| strict (Title/Abstract + gene/protein) | 8 |
| symbol_only (Title/Abstract) | 11 |
| broad (all fields) | 29 |

1. PMID 37664858: Zhao Y, Gao Q, Li B (2023). "Ferroptosis and its potential role in gestational diabetes mellitus: updated evidence from pathogenesis to therapy.." *Frontiers in endocrinology*.
2. PMID 39031745: Gholami M (2024 Jun). "Common and novel haplotype structures between different types of cancer.." *Cancer reports (Hoboken, N.J.)*.
3. PMID 40775447: Chang YH, Bresnahan ST, Taylor Head S (2025 Oct). "Isoform-level analyses of 6 cancers uncover extensive genetic risk mechanisms undetected at the gene-level.." *British journal of cancer*.
4. PMID 28115406: Toth R, Scherer D, Kelemen LE (2017 Jun). "Genetic Variants in Epigenetic Pathways and Risks of Multiple Cancers in the GAME-ON Consortium.." *Cancer epidemiology, biomarkers & prevention : a publication of the American Association for Cancer Research, cosponsored by the American Society of Preventive Oncology*.
5. PMID 23805179: Hass J, Walton E, Kirsten H (2013). "A Genome-Wide Association Study Suggests Novel Loci Associated with a Schizophrenia-Related Brain-Based Phenotype.." *PloS one*.

### 5. AlphaFold 结构预测

| 平均 pLDDT | 78.2 |
| pLDDT >90 | 58.1% |
| pLDDT 70-90 | 10.3% |
| pLDDT 50-70 | 7.3% |
| pLDDT <50 | 24.3% |

**评价**: AlphaFold 预测整体置信度较高（mean pLDDT 78.2），大部分区域折叠良好。



### 6. PDB 条目

| PDB ID | Method | Resolution | Chains |
|---|---|---|---|
| 6H3C | EM | 3.90 A | D/I=1-329 |
| 8PVY | EM | 3.02 A | M/N/O/P=72-329 |
| 8PY2 | EM | 3.32 A | M/N/O/P=72-329 |

### 7. InterPro/Pfam 结构域

| InterPro | IPR026126 | IPR entry IPR026126 |
| InterPro | IPR036465 | IPR entry IPR036465 |

**评价**: BRISC complex 亚基，参与去泛素化 (K63-specific)。该复合体与BRCA1-A complex共享多个亚基，在DNA损伤应答和炎症信号中发挥作用。

### 8. PPI 网络

#### STRING Top 10

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|---|
| UIMC1 | 0.999 | 0.994 | 0.900 | 0.998 |
| ABRAXAS1 | 0.999 | 0.994 | 0.900 | 0.997 |
| BABAM2 | 0.999 | 0.999 | 0.900 | 0.998 |
| BRCA1 | 0.999 | 0.994 | 0.900 | 0.992 |
| ABRAXAS2 | 0.999 | 0.977 | 0.900 | 0.992 |
| BRCC3 | 0.999 | 0.998 | 0.900 | 0.998 |
| BARD1 | 0.998 | 0.063 | 0.900 | 0.986 |
| SHMT2 | 0.997 | 0.966 | 0.900 | 0.252 |
| TNKS | 0.913 | 0.780 | 0.000 | 0.621 |
| TNKS2 | 0.862 | 0.664 | 0.000 | 0.607 |

#### IntAct Top 10

| Partner | Method | PMID | Interaction |
|---|---|---|---|
| ENSP00000471605.1 | psi-mi:"MI:2170"(bimolecular luminiscence complementation) | pubmed:37398436|imex:IM-29926 | psi-mi:"MI:0915"(physical association) |
| BABAM2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 | psi-mi:"MI:0915"(physical association) |
| TNKS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22153077|imex:IM-16612 | psi-mi:"MI:0915"(physical association) |
| BRCC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| ABRAXAS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| PSMA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| SLIRP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| MRPL53 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| NDUFA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |
| PBDC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 | psi-mi:"MI:0914"(association) |

#### UniProt 互作

| Partner | Experiments |
|---|---|
| BABAM1 | 3 |
| BABAM2 | 17 |
| LAMTOR2 | 2 |
| PMF1 | 3 |
| TERF2IP | 2 |
| TNKS2 | 7 |
| TRIM27 | 7 |

### 9. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (5/5)

**核心优势**:
1. 核定位证据充分（得分 8/10），多源验证一致
2. 研究新颖性极高：仅 8 篇严格文献，chromatin/epigenetics 方向几乎空白，属于真正的'未被开垦领域'
3. 蛋白大小适中（329 aa），适合重组表达和结构研究

**风险/不确定性**:

**分类**: nuclear-body
**综合评分**: 78/100

---

**数据来源**: UniProt Q9NWV8, HPA ENSG00000105393, AlphaFold AF-Q9NWV8-F1, STRING, IntAct

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000105393-BABAM1/subcellular

![](https://images.proteinatlas.org/54386/2267_B12_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/54386/2267_B12_39_blue_red_green.jpg)
![](https://images.proteinatlas.org/77609/2267_D12_112_blue_red_green.jpg)
![](https://images.proteinatlas.org/77609/2267_D12_89_blue_red_green.jpg)
![](https://images.proteinatlas.org/54386/849_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/54386/849_F10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
