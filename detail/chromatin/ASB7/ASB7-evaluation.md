---
type: protein-evaluation
gene: "ASB7"
date: 2026-06-03
tags: [protein-scout, chromatin, evaluation]
status: scored
---

## ASB7 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ASB7 / 无 |
| 蛋白全名 | Ankyrin repeat and SOCS box protein 7 |
| 蛋白大小 | 318 aa / 36.0 kDa |
| UniProt ID | Q9H672 (ASB7_HUMAN) |
| 功能描述 | Substrate-recognition component of a cullin-5-RING E3 ubiquitin-protein ligase complex (ECS complex, also named CRL5 complex), which mediates the ubiquitination and subsequent proteasomal degradation of target proteins, such as LZTS1, PSRC1 and SUV39H1 (PubMed:16325183, PubMed:27697924, PubMed:39039081, PubMed:40440427). The ECS(ASB7) complex acts as a negative regulator of H3K9me3 histone mark by... |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | UniProt experimental nuclear localization (Chromosome, Nucleus) |
| 蛋白大小 | 10/10 | x1 | 10.0 | 318 aa / 36.0 kDa, 300-800理想区间 |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed strict=6（极低研究量，≤20→10分） |
| 三维结构 | 10/10 | x3 | 30.0 | PDB X-ray (1 entries) + AF pLDDT mean 92.3, 81%>90 |
| 调控结构域 | 8/10 | x2 | 16.0 | Chromatin-associated regulatory protein |
| PPI 网络 | 7/10 | x3 | 21.0 | IntAct experiment: 15 partners (5 regulatory: CUL5, POLR3A, POLR1A, KMT2A, NPAT) |
| 互证加分 | — | — | +1.0 | >=2 source nuclear localization; domain annotation + nuclear localization |
| **加权总分** | | | **143/180************ | |
| **归一化总分 (÷1.83)** | | | **78.1/100************ | |

### 3. HPA 免疫荧光分析

| HPA 主定位 | Golgi apparatus, Vesicles |
| HPA 额外定位 | Nucleoplasm |
| 抗体可靠性 | Approved |
| IF 图像 | IF images available (6 cell lines) |

**评价**: HPA 主定位为 Golgi apparatus, Vesicles。标注定位包括: Nucleoplasm, Golgi apparatus, Vesicles。抗体可靠性评级: Approved。HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图，仅有display image列表）。核定位基于HPA localization/reliability + UniProt + GO-CC。，显示核内信号分布。

### 4. PubMed 文献

| strict (Title/Abstract + gene/protein) | 6 |
| symbol_only (Title/Abstract) | 12 |
| broad (all fields) | 12 |

1. PMID 40440427: Zhou L, Chen Z, Zou Y (2025 Jul 17). "ASB7 is a negative regulator of H3K9me3 homeostasis.." *Science (New York, N.Y.)*.
2. PMID 33251222: Liu Y, Li X, He Y (2020). "ASB7 Is a Novel Regulator of Cytoskeletal Organization During Oocyte Maturation.." *Frontiers in cell and developmental biology*.
3. PMID 27697924: Uematsu K, Okumura F, Tonogai S (2016 Oct 10). "ASB7 regulates spindle dynamics and genome integrity by targeting DDA3 for proteasomal degradation.." *The Journal of cell biology*.
4. PMID 42045320: Li Z, Sun X, Xie Y (2026 Apr 27). "YKL-40 alleviates the TNF-α-Induced chondrocyte injury in osteoarthritis in vitro.." *Scientific reports*.
5. PMID 29630609: Anasa VV, Manickam M, Talwar P (2018). "Identification of ASB7 as ER stress responsive gene through a genome wide in silico screening for genes with ERSE.." *PloS one*.

### 5. AlphaFold 结构预测

| 平均 pLDDT | 92.3 |
| pLDDT >90 | 80.8% |
| pLDDT 70-90 | 14.2% |
| pLDDT 50-70 | 2.8% |
| pLDDT <50 | 2.2% |

**评价**: AlphaFold 预测整体置信度极高（mean pLDDT 92.3，81% 残基 >90），蛋白折叠预测可靠。



### 6. PDB 条目

| PDB ID | Method | Resolution | Chains |
|---|---|---|---|
| 8Y1U | X-ray | 2.41 A | A=11-318 |

### 7. InterPro/Pfam 结构域

| InterPro | IPR002110 | IPR entry IPR002110 |
| InterPro | IPR036770 | IPR entry IPR036770 |
| InterPro | IPR037326 | IPR entry IPR037326 |
| InterPro | IPR001496 | IPR entry IPR001496 |
| InterPro | IPR036036 | IPR entry IPR036036 |
| Pfam | PF12796 | Pfam entry PF12796 |
| Pfam | PF07525 | Pfam entry PF07525 |

**评价**: SOCS box (PF07525) 是 E3 ubiquitin ligase 复合体的底物识别模块，介导靶蛋白的泛素化降解。ASB7 已实验确认为 H3K9me3 的负调控因子——通过 CBX5/HP1alpha 被招募至 heterochromatin，促进 SUV39H1 的泛素化降解，直接调控组蛋白修饰稳态。Ankyrin repeat (PF12796) 介导蛋白-蛋白相互作用，通常作为底物识别模块。

### 8. PPI 网络

#### STRING Top 10

| Partner | Combined Score | Experimental | Database | Textmining |
|---|---|---|---|---|
| CUL5 | 0.914 | 0.774 | 0.400 | 0.408 |
| RNF7 | 0.838 | 0.610 | 0.400 | 0.350 |
| ZBTB6 | 0.791 | 0.091 | 0.000 | 0.000 |
| RPAP3 | 0.778 | 0.651 | 0.000 | 0.348 |
| TADA2B | 0.724 | 0.091 | 0.000 | 0.624 |
| ELOB | 0.720 | 0.422 | 0.400 | 0.258 |
| KLHL20 | 0.719 | 0.045 | 0.000 | 0.636 |
| FAM104A | 0.718 | 0.000 | 0.000 | 0.708 |
| CCDC127 | 0.716 | 0.000 | 0.000 | 0.713 |
| WDR92 | 0.690 | 0.690 | 0.000 | 0.000 |

#### IntAct Top 10

| Partner | Method | PMID | Interaction |
|---|---|---|---|
| ATF4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 | psi-mi:"MI:0915"(physical association) |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651|doi:10.1016/j.cell.2 | psi-mi:"MI:0914"(association) |
| OGN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |
| HMBOX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| CCDC136 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 | psi-mi:"MI:0915"(physical association) |
| HIF1AN | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| ZFAND2B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 | psi-mi:"MI:0915"(physical association) |
| SEPTIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |
| KIF13B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |
| POLR3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25 | psi-mi:"MI:0914"(association) |

#### UniProt 互作

| Partner | Experiments |
|---|---|
| CCDC136 | 4 |
| CUL5 | 5 |
| HMBOX1 | 4 |
| RNF7 | 5 |
| HIF1AN | 3 |
| PRKN | 3 |
| ZFAND2B | 3 |

### 9. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (5/5)

**核心优势**:
1. 研究新颖性极高：仅 6 篇严格文献，chromatin/epigenetics 方向几乎空白，属于真正的'未被开垦领域'
2. 蛋白大小适中（318 aa），适合重组表达和结构研究

**风险/不确定性**:
1. 核定位证据偏弱（得分 4/10），需要更多的实验验证

**分类**: chromatin
**综合评分**: 79/100

---

**数据来源**: UniProt Q9H672, HPA ENSG00000183475, AlphaFold AF-Q9H672-F1, STRING, IntAct

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。
