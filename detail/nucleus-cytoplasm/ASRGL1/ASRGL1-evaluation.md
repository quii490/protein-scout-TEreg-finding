---
type: protein-evaluation
gene: "ASRGL1"
date: 2026-06-03
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## ASRGL1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ASRGL1 / ALP, CRASH |
| 蛋白全名 | Isoaspartyl peptidase/L-asparaginase |
| 蛋白大小 | 308 aa / 32.1 kDa |
| UniProt ID | Q7L266 (ASRGL1_HUMAN) |
| 功能描述 | Has both L-asparaginase and beta-aspartyl peptidase activity. May be involved in the production of L-aspartate, which can act as an excitatory neurotransmitter in some brain regions. Is highly active with L-Asp beta-methyl ester. Besides, has catalytic activity toward beta-aspartyl dipeptides and their methyl esters, including beta-L-Asp-L-Phe, beta-L-Asp-L-Phe methyl ester (aspartame), beta-L-Asp... |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | GO-CC nuclear: nucleus (HDA:UniProtKB) |
| 蛋白大小 | 10/10 | x1 | 10.0 | 308 aa / 32.1 kDa, 300-800理想区间 |
| 研究新颖性 | 8/10 | x5 | 40.0 | PubMed strict=40（低研究量，21-40→8分） |
| 三维结构 | 10/10 | x3 | 30.0 | PDB X-ray (15 entries) + AF pLDDT mean 94.2, 89%>90 |
| 调控结构域 | 3/10 | x2 | 6.0 | No clear regulatory domain identified |
| PPI 网络 | 2/10 | x3 | 6.0 | IntAct experiment: 12 partners (1 regulatory: ERBB2) |
| 互证加分 | — | — | +1.0 | >=2 source nuclear localization; domain annotation + nuclear localization |
| **加权总分** | | | **108/180**************** | |
| **归一化总分 (÷1.83)** | | | **59.0/100**************** | |

### 3. HPA 免疫荧光分析

| HPA 主定位 | Microtubules |
| HPA 额外定位 | Nucleoplasm, Cytokinetic bridge |
| 抗体可靠性 | Approved |
| IF 图像 | 无可用的subcellular IF原图 (HPA image_status: no_image_detected) |

**评价**: HPA 主定位为 Microtubules。标注定位包括: Nucleoplasm, Microtubules, Cytokinetic bridge。抗体可靠性评级: Approved。HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

### 4. PubMed 文献

| strict (Title/Abstract + gene/protein) | 40 |
| symbol_only (Title/Abstract) | 46 |
| broad (all fields) | 59 |

1. PMID 38755145: Garcia-Montojo M, Fathi S, Rastegar C (2024 May 16). "TDP-43 proteinopathy in ALS is triggered by loss of ASRGL1 and associated with HML-2 expression.." *Nature communications*.
2. PMID 32434038: Morais SB, Pirolla RAS, Frota NF (2020 Jul 30). "The role of the quaternary structure in the activation of human L-asparaginase.." *Journal of proteomics*.
3. PMID 40320045: Pei Y, Li C, Zhang B (2025 Aug). "Single-cell transcriptomics and metabolomics reveal the potential role of ASRGL1 in metabolic reprogramming and invasion of nasopharyngeal carcinoma cells.." *The international journal of biochemistry & cell biology*.
4. PMID 38972163: Loukovaara MJ, Huvila JK, Pasanen AM (2024 Sep). "Asparaginase-like protein 1 as a prognostic tissue biomarker in clinicopathologically and molecularly characterized endometrial cancer.." *European journal of obstetrics, gynecology, and reproductive biology*.
5. PMID 36572570: Wang X, Wang Y, Yang L (2023 Jul). "ASRGL1 downregulation suppresses hepatocellular carcinoma tumorigenesis in a CDK1-dependent manner.." *Digestive and liver disease : official journal of the Italian Society of Gastroenterology and the Italian Association for the Study of the Liver*.

### 5. AlphaFold 结构预测

| 平均 pLDDT | 94.2 |
| pLDDT >90 | 88.6% |
| pLDDT 70-90 | 6.5% |
| pLDDT 50-70 | 2.6% |
| pLDDT <50 | 2.3% |

**评价**: AlphaFold 预测整体置信度极高（mean pLDDT 94.2，89% 残基 >90），蛋白折叠预测可靠。



### 6. PDB 条目

| PDB ID | Method | Resolution | Chains |
|---|---|---|---|
| 3TKJ | X-ray | 2.30 A | A/B=2-308 |
| 4ET0 | X-ray | 3.30 A | A/B=2-308 |
| 4O0C | X-ray | 1.50 A | A/B=1-308 |
| 4O0D | X-ray | 1.95 A | A/B=1-308 |
| 4O0E | X-ray | 1.71 A | A/B=1-308 |
| 4O0F | X-ray | 1.92 A | A/B=1-308 |
| 4O0G | X-ray | 2.10 A | A/B=1-308 |
| 4O0H | X-ray | 1.97 A | A/B=1-308 |

### 7. InterPro/Pfam 结构域

| InterPro | IPR033844 | IPR entry IPR033844 |
| InterPro | IPR029055 | IPR entry IPR029055 |
| InterPro | IPR000246 | IPR entry IPR000246 |
| Pfam | PF01112 | Pfam entry PF01112 |

**评价**: 无明确染色质/转录调控结构域。功能注释指向其他细胞过程。

### 8. PPI 网络

#### STRING Top 10

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|---|
| ASNS | 0.959 | 0.000 | 0.937 | 0.374 |
| ASPG | 0.936 | 0.000 | 0.000 | 0.935 |
| GOT1 | 0.927 | 0.000 | 0.911 | 0.171 |
| GOT2 | 0.924 | 0.000 | 0.911 | 0.127 |
| GOT1L1 | 0.921 | 0.000 | 0.911 | 0.101 |
| ADSS2 | 0.916 | 0.000 | 0.900 | 0.140 |
| ADSS1 | 0.910 | 0.000 | 0.900 | 0.084 |
| ASS1 | 0.906 | 0.000 | 0.900 | 0.107 |
| IL4I1 | 0.906 | 0.000 | 0.900 | 0.099 |
| ASPA | 0.905 | 0.000 | 0.900 | 0.048 |

#### IntAct Top 10

| Partner | Method | PMID | Interaction |
|---|---|---|---|
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218203 | psi-mi:"MI:0914"(association) |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 | psi-mi:"MI:0914"(association) |
| ERBB2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 | psi-mi:"MI:0915"(physical association) |
| FLT3 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008|pubmed:31585087|ime | psi-mi:"MI:0914"(association) |
| NMI | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |
| MDM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |
| SLC66A1LP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2 | psi-mi:"MI:0914"(association) |
| PIK3R6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2 | psi-mi:"MI:0914"(association) |
| USB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2 | psi-mi:"MI:0914"(association) |
| STMN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2 | psi-mi:"MI:0914"(association) |

### 9. 总体评价

**推荐等级**: ⭐⭐⭐ (3/5)

**核心优势**:
1. 蛋白大小适中（308 aa），适合重组表达和结构研究

**风险/不确定性**:
1. 核定位证据偏弱（得分 4/10），需要更多的实验验证

**分类**: nucleus-cytoplasm
**综合评分**: 60/100

---

**数据来源**: UniProt Q7L266, HPA ENSG00000162174, AlphaFold AF-Q7L266-F1, STRING, IntAct

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L266-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
