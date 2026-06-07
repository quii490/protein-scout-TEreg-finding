---
type: protein-evaluation
gene: "AUP1"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## AUP1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | AUP1 / 无 |
| 蛋白全名 | Lipid droplet-regulating VLDL assembly factor AUP1 |
| 蛋白大小 | 410 aa / 45.8 kDa |
| UniProt ID | Q9Y679 (AUP1_HUMAN) |
| 功能描述 | Plays a role in the translocation of terminally misfolded proteins from the endoplasmic reticulum lumen to the cytoplasm and their degradation by the proteasome (PubMed:18711132, PubMed:21857022). Plays a role in lipid droplet formation (PubMed:21857022). Induces lipid droplet clustering (PubMed:24039768). Recruits ubiquitin-conjugating enzyme UBE2G2 to lipid droplets which facilitates its interac... |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | x4 | 24.0 | HPA main: nucleoplasm, vesicles |
| 蛋白大小 | 10/10 | x1 | 10.0 | 410 aa / 45.8 kDa, 300-800理想区间 |
| 研究新颖性 | 6/10 | x5 | 30.0 | PubMed strict=41（中等偏少，41-60→6分） |
| 三维结构 | 9/10 | x3 | 27.0 | PDB X-ray confirmed (1 entries); AF mean pLDDT 79.5 |
| 调控结构域 | 6/10 | x2 | 12.0 | Ubiquitin pathway enzyme |
| PPI 网络 | 2/10 | x3 | 6.0 | IntAct experiment: 15 partners (0 regulatory: none identified) |
| 互证加分 | — | — | +0.0 | 无 |
| **加权总分** | | | **109/180**************** | |
| **归一化总分 (÷1.83)** | | | **59.6/100**************** | |

### 3. HPA 免疫荧光分析

| HPA 主定位 | Nucleoplasm, Vesicles |
| HPA 额外定位 | 无数据 |
| 抗体可靠性 | Approved |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 4. PubMed 文献

| strict (Title/Abstract + gene/protein) | 41 |
| symbol_only (Title/Abstract) | 48 |
| broad (all fields) | 50 |

1. PMID 33794741: Filali-Mouncef Y, Hunter C, Roccio F (2022 Jan). "The ménage à trois of autophagy, lipid droplets and liver disease.." *Autophagy*.
2. PMID 33590792: Robichaud S, Fairman G, Vijithakumar V (2021 Nov). "Identification of novel lipid droplet factors that regulate lipophagy and cholesterol efflux in macrophage foam cells.." *Autophagy*.
3. PMID 40237449: Wang X-T, Zhu X, Lian Z-H (2025 May 14). "AUP1 and UBE2G2 complex targets STING signaling and regulates virus-induced innate immunity.." *mBio*.
4. PMID 38474353: Frachon N, Demaretz S, Seaayfan E (2024 Feb 24). "AUP1 Regulates the Endoplasmic Reticulum-Associated Degradation and Polyubiquitination of NKCC2.." *Cells*.
5. PMID 29902443: Zhang J, Lan Y, Li MY (2018 Jun 13). "Flaviviruses Exploit the Lipid Droplet Protein AUP1 to Trigger Lipophagy and Drive Virus Production.." *Cell host & microbe*.

### 5. AlphaFold 结构预测

| 平均 pLDDT | 79.5 |
| pLDDT >90 | 25.9% |
| pLDDT 70-90 | 53.2% |
| pLDDT 50-70 | 12.4% |
| pLDDT <50 | 8.5% |

**评价**: AlphaFold 预测整体置信度较高（mean pLDDT 79.5），大部分区域折叠良好。



### 6. PDB 条目

| PDB ID | Method | Resolution | Chains |
|---|---|---|---|
| 2EKF | NMR | - | A=292-345 |
| 7LEW | X-ray | 1.74 A | B=379-410 |

### 7. InterPro/Pfam 结构域

| InterPro | IPR048056 | IPR entry IPR048056 |
| InterPro | IPR003892 | IPR entry IPR003892 |
| Pfam | PF02845 | Pfam entry PF02845 |

**评价**: AUP1 是脂滴相关蛋白，参与ER-associated degradation (ERAD) 和脂质代谢。含CUE domain，结合泛素链。

### 8. PPI 网络

#### STRING Top 10

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|---|
| UBE2G2 | 0.999 | 0.980 | 0.000 | 0.994 |
| SEL1L | 0.995 | 0.810 | 0.540 | 0.949 |
| FAF2 | 0.994 | 0.368 | 0.000 | 0.992 |
| DERL2 | 0.992 | 0.000 | 0.540 | 0.983 |
| SYVN1 | 0.987 | 0.784 | 0.540 | 0.882 |
| OS9 | 0.978 | 0.292 | 0.540 | 0.935 |
| UBE2J1 | 0.950 | 0.515 | 0.000 | 0.902 |
| VCP | 0.943 | 0.597 | 0.000 | 0.851 |
| DERL3 | 0.865 | 0.000 | 0.540 | 0.720 |
| CANX | 0.862 | 0.220 | 0.000 | 0.827 |

#### IntAct Top 10

| Partner | Method | PMID | Interaction |
|---|---|---|---|
| PRO2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 | psi-mi:"MI:0914"(association) |
| ATG12 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| UBE2G2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| BRF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| ILK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| 5901994 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| MAGEA6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| NDN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 | psi-mi:"MI:0915"(physical association) |
| UBE2E3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 | psi-mi:"MI:0915"(physical association) |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 | psi-mi:"MI:0914"(association) |

### 9. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 核定位证据较为充分（得分 6/10）
2. 蛋白大小适中（410 aa），适合重组表达和结构研究

**风险/不确定性**:

**分类**: nucleoplasm
**综合评分**: 60/100

---

**数据来源**: UniProt Q9Y679, HPA ENSG00000115307, AlphaFold AF-Q9Y679-F1, STRING, IntAct

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000115307-AUP1/subcellular

![](https://images.proteinatlas.org/7674/20_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/7674/20_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/7674/21_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/7674/21_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/7674/22_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/7674/22_H5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y679-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y679 |
| SMART | SM00546; |
| UniProt Domain [FT] | DOMAIN 296..338; /note="CUE"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00468" |
| InterPro | IPR048056;IPR003892; |
| Pfam | PF02845; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000115307-AUP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CANX | Biogrid, Opencell | true |
| GPR35 | Intact, Biogrid | true |
| OPRM1 | Intact, Biogrid | true |
| UBE2G2 | Intact, Biogrid | true |
| VCP | Biogrid, Opencell | true |
| AMFR | Biogrid | false |
| APOB | Biogrid | false |
| CLN3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
