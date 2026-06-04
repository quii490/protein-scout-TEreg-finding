---
type: protein-evaluation
gene: "BCDIN3D"
date: 2026-06-03
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## BCDIN3D 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | BCDIN3D / 无 |
| 蛋白全名 | RNA 5'-monophosphate methyltransferase |
| 蛋白大小 | 292 aa / 33.2 kDa |
| UniProt ID | Q7Z5W3 (BCDIN3D_HUMAN) |
| 功能描述 | O-methyltransferase that specifically monomethylates 5'-monophosphate of cytoplasmic histidyl tRNA (tRNA(His)), acting as a capping enzyme by protecting tRNA(His) from cleavage by DICER1 (PubMed:28119416, PubMed:31329584, PubMed:31919512). Also able, with less efficiently, to methylate the 5' monophosphate of a subset of pre-miRNAs, acting as a negative regulator of miRNA processing (PubMed:230631... |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | GO-CC nuclear: nucleoplasm (IDA:HPA) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 292 aa / 33.2 kDa, <300或>800 |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed strict=5（极低研究量，≤20→10分） |
| 三维结构 | 9/10 | x3 | 27.0 | PDB X-ray confirmed (1 entries); AF mean pLDDT 84.5 |
| 调控结构域 | 4/10 | x2 | 8.0 | Some regulatory association (1 keywords) |
| PPI 网络 | 4/10 | x3 | 12.0 | IntAct experiment: 11 partners (2 regulatory: CUL3, RELL2) |
| 互证加分 | — | — | +1.0 | >=2 source nuclear localization; domain annotation + nuclear localization |
| **加权总分** | | | **119/180************ | |
| **归一化总分 (÷1.83)** | | | **65.0/100************ | |

### 3. HPA 免疫荧光分析

| HPA 主定位 | Cytosol |
| HPA 额外定位 | Nucleoplasm, Plasma membrane |
| 抗体可靠性 | Supported |
| IF 图像 | IF images available (12 cell lines) |

**评价**: HPA 主定位为 Cytosol。标注定位包括: Nucleoplasm, Plasma membrane, Cytosol。抗体可靠性评级: Supported。HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图，仅有display image列表）。核定位基于HPA localization/reliability + UniProt + GO-CC。，显示核内信号分布。

### 4. PubMed 文献

| strict (Title/Abstract + gene/protein) | 5 |
| symbol_only (Title/Abstract) | 21 |
| broad (all fields) | 21 |

1. PMID 30127802: Tomita K, Liu Y (2018). "Human BCDIN3D Is a Cytoplasmic tRNA(His)-Specific 5'-Monophosphate Methyltransferase.." *Frontiers in genetics*.
2. PMID 38263329: Ipas H, Gouws EB, Abell NS (2024 Mar). "ChemRAP uncovers specific mRNA translation regulation via RNA 5' phospho-methylation.." *EMBO reports*.
3. PMID 33664453: Reinsborough CW, Ipas H, Abell NS (2021 Apr). "BCDIN3D RNA methyltransferase stimulates Aldolase C expression and glycolysis through let-7 microRNA in breast cancer cells.." *Oncogene*.
4. PMID 36102151: Soto-Pedre E, Newey PJ, Srinivasan S (2022 Nov 25). "Identification of 4 New Loci Associated With Primary Hyperparathyroidism (PHPT) and a Polygenic Risk Score for PHPT.." *The Journal of clinical endocrinology and metabolism*.
5. PMID 33157501: Jin M, Wang L, Zheng T (2021 Feb). "MiR-195-3p inhibits cell proliferation in cervical cancer by targeting BCDIN3D.." *Journal of reproductive immunology*.

### 5. AlphaFold 结构预测

| 平均 pLDDT | 84.5 |
| pLDDT >90 | 64.4% |
| pLDDT 70-90 | 14.7% |
| pLDDT 50-70 | 9.6% |
| pLDDT <50 | 11.3% |

**评价**: AlphaFold 预测整体置信度较高（mean pLDDT 84.5），大部分区域折叠良好。



### 6. PDB 条目

| PDB ID | Method | Resolution | Chains |
|---|---|---|---|
| 6L8U | X-ray | 2.92 A | A/B/C/D=14-284 |

### 7. InterPro/Pfam 结构域

| InterPro | IPR039772 | IPR entry IPR039772 |
| InterPro | IPR010675 | IPR entry IPR010675 |
| InterPro | IPR024160 | IPR entry IPR024160 |
| InterPro | IPR029063 | IPR entry IPR029063 |
| Pfam | PF06859 | Pfam entry PF06859 |

**评价**: RNA methyltransferase，催化特定tRNA/piRNA的甲基化修饰。在精子发生中调控piRNA成熟和转座子沉默。

### 8. PPI 网络

#### STRING Top 10

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|---|
| FAIM2 | 0.764 | 0.000 | 0.000 | 0.764 |
| SEC16B | 0.691 | 0.000 | 0.000 | 0.691 |
| GNPDA2 | 0.653 | 0.000 | 0.000 | 0.645 |
| KCTD15 | 0.646 | 0.000 | 0.000 | 0.645 |
| SCYL3 | 0.623 | 0.000 | 0.000 | 0.000 |
| TMEM18 | 0.600 | 0.000 | 0.000 | 0.597 |
| SH2B1 | 0.598 | 0.000 | 0.000 | 0.598 |
| MTCH2 | 0.581 | 0.000 | 0.000 | 0.581 |
| NEGR1 | 0.571 | 0.000 | 0.000 | 0.571 |
| BIN3 | 0.567 | 0.000 | 0.000 | 0.567 |

#### IntAct Top 10

| Partner | Method | PMID | Interaction |
|---|---|---|---|
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651|doi:10.1016/j.cell.2 | psi-mi:"MI:0914"(association) |
| Amus | psi-mi:"MI:0018"(two hybrid) | pubmed:16603075|imex:IM-19959 | psi-mi:"MI:0915"(physical association) |
| SIX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |
| N | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 | psi-mi:"MI:0914"(association) |
| ZFP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 | psi-mi:"MI:0915"(physical association) |
| NetB | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 | psi-mi:"MI:0914"(association) |
| sals | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 | psi-mi:"MI:0914"(association) |
| Ten-m | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 | psi-mi:"MI:0914"(association) |
| RELL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2 | psi-mi:"MI:0914"(association) |
| ACACB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2 | psi-mi:"MI:0915"(physical association) |

#### UniProt 互作

| Partner | Experiments |
|---|---|
| ZFP2 | 3 |

### 9. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (4/5)

**核心优势**:
1. 研究新颖性极高：仅 5 篇严格文献，chromatin/epigenetics 方向几乎空白，属于真正的'未被开垦领域'

**风险/不确定性**:
1. 核定位证据偏弱（得分 4/10），需要更多的实验验证

**分类**: nucleus-cytoplasm
**综合评分**: 66/100

---

**数据来源**: UniProt Q7Z5W3, HPA ENSG00000186666, AlphaFold AF-Q7Z5W3-F1, STRING, IntAct

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。
