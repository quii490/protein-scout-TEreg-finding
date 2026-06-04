---
type: protein-evaluation
gene: "PADI6"
date: 2026-06-02
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## PADI6 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PADI6 / PAD6 |
| 蛋白全名 | Inactive protein-arginine deiminase type-6 |
| 蛋白大小 | 694 aa / 77.7 kDa |
| UniProt ID | Q6TGC4 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | Cytoplasm + Nucleus (ECO:0000250); GO nucleus IBA; HPA 无IF图像 |
| 蛋白大小 | 10/10 | ×1 | 10.0 | 694 aa, 77.7 kDa, 处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30.0 | PubMed strict=59, symbol_only=82, broad=91 |
| 三维结构 | 8/10 | ×3 | 24.0 | 4 PDB (4DAT/4DAU/8QL0/9FMN, X-ray 1.40-2.44A) + AF pLDDT=85.7 |
| 调控结构域 | 7/10 | ×2 | 14.0 | 10 domains (7 InterPro + 3 Pfam): PAD family, Cupredoxin |
| PPI 网络 | 4/10 | ×3 | 12.0 | IntAct 15 + STRING 15 + UniProt 4; SCMC相关+染色质调控因子 |
| **加权总分** | | | **106/180**** | |
| 互证加分 | | | +1.0 | PDB+AF 互证(+0.5); 多库结构域一致(+0.5) |
| **归一化总分 (÷1.83)** | | | **57.9/100**** | |

![[PADI6-PAE.png]]

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Cytoplasm (ECO:0000269); Cytoplasmic vesicle, secretory vesicle, Cortical granule (ECO:0000250); Nucleus (ECO:0000250) | 混合证据 |
| GO-CC | cortical granule ISS; cytoplasm IDA; cytoplasmic lattice IDA; intermediate filament cytoskeleton IEA; nucleus IBA | 实验+预测 |
| Protein Atlas (IF) | HPA 暂无数据，未获取到 IF 图像 | 未确认 |

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。. 核定位基于 UniProt + GO-CC，但 nucleus 证据为 ECO:0000250 (by similarity) 和 IBA (GO_Central)，非直接实验证据。主要定位在 cytoplasmic lattice (IDA)，是 oocyte 特异性结构。

**结论**: 细胞核+细胞质，核定位证据偏间接，以胞质为主。

#### 3.2 结构与结构域

| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q6TGC4-F1 (v6) |
| 平均 pLDDT | 85.7 |
| pLDDT >90 / 70-90 / 50-70 / <50 | 55.0% / 30.7% / 11.2% / 3.0% |
| PDB | 4DAT (X-ray 1.40A, B=441-449), 4DAU (X-ray 2.00A, B=1-13), 8QL0 (X-ray 1.68A, A=2-694), 9FMN (X-ray 2.44A, A=1-694) |

| 来源 | 结构域 |
|---|---|
| InterPro | IPR008972 (Cupredoxin), IPR004303 (PAD), IPR013530 (PAD_C), IPR036556 (PAD_central_sf), IPR013732 (PAD_N), IPR038685 (PAD_N_sf), IPR013733 (Prot_Arg_deaminase_cen_dom) |
| Pfam | PF03068 (PAD), PF08527 (PAD_M), PF08526 (PAD_N) |

**评价**: AF pLDDT 85.7 表示整体结构预测置信度高。4个X-ray PDB覆盖全长。PAD (peptidyl arginine deiminase) 家族结构域完整，但该蛋白因无法结合 Ca²⁺ 而失活。

#### 3.3 研究现状

| 指标 | 数值 |
|---|---|
| PubMed strict | 59 |
| PubMed symbol_only | 82 |
| PubMed broad | 91 |

**关键文献**:
1. Jentoft IMA et al. (2023). "Mammalian oocytes store proteins for the early embryo on cytoplasmic lattices." *Cell*. PMID: 37922900
2. Giaccari C et al. (2024). "A maternal-effect Padi6 variant causes nuclear and cytoplasmic abnormalities in oocytes..." *Genes Dev*. PMID: 38453481
3. Williams JPC & Walport LJ (2023). "PADI6: What we know about the elusive fifth member of the peptidyl arginine deiminase family." *Philos Trans R Soc Lond B Biol Sci*. PMID: 37778376
4. Liu S et al. (2026). "Molecular basis of oocyte cytoplasmic lattice assembly." *Nature*. PMID: 41845018
5. Sang Q et al. (2021). "Genetic factors as potential molecular markers of human oocyte and embryo quality." *J Assist Reprod Genet*. PMID: 33895934

**评价**: 研究集中在oocyte/early embryo cytoplasmic lattice，2024-2026有多篇高影响因子论文。新颖性中等。

#### 3.4 PPI 网络

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | Relevance |
|---|---|---|---|
| ZNF526 | two hybrid array | 32296183 | — |
| DDIT4L | two hybrid prey pooling | 32296183 | — |
| SUV39H1 | validated two hybrid | 32296183 | H3K9 methyltransferase, chromatin |
| KLHL2 | validated two hybrid | 32296183 | — |
| MTA3 | anti tag coIP | 26028330 | NuRD complex, chromatin |
| MN1 | anti tag coIP | 33961781 | — |
| EBF2 | anti tag coIP | 33961781 | — |
| UHRF1 | anti tag coIP | 33961781 | DNA methylation, chromatin |
| BRMS1 | anti tag coIP | 33961781 | — |
| KLHL28 | anti tag coIP | 33961781 | — |

**STRING 预测互作** (score >0.4):

| Partner | Score | Experimental | Relevance |
|---|---|---|---|
| OOEP | 0.965 | 0 | SCMC |
| TLE6 | 0.950 | 0 | SCMC |
| SFN | 0.904 | 0.900 | SCMC |
| NLRP5 | 0.873 | 0 | SCMC |
| KHDC3L | 0.829 | 0 | SCMC |
| NLRP2 | 0.741 | 0 | SCMC |
| ZBED3 | 0.705 | 0 | — |
| H3C12 | 0.605 | 0 | Histone, chromatin |
| H3C13 | 0.604 | 0 | Histone, chromatin |
| ZAR1 | 0.590 | 0 | oocyte |

**已知复合体**: Subcortical Maternal Complex (SCMC) 关联 (OOEP, TLE6, NLRP5, KHDC3L)

**评价**: PPI 网络主要与 SCMC (subcortical maternal complex) 和 oocyte-specific factors 相关。IntAct 中有 SUV39H1 (H3K9 甲基转移酶)、UHRF1 (DNA 甲基化reader) 等染色质调控因子。整体调控相关性中等。

#### 3.5 多库互证

| 维度 | 来源 | 结果 | 一致性 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 4 PDB + AF 预测 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 10 个 | 多库一致 |
| PPI 网络 | STRING + IntAct + UniProt | 多源 | 部分一致 |
| 核定位 | HPA/UniProt/GO | Nucleus + Cytoplasm | 部分一致 |

**互证加分明细**: PDB+AF互证(+0.5), 多库结构域一致(+0.5), 总计 +1.0

### 4. 总体评价

PADI6 是 cytoplasmic lattice 的结构组分，在早期胚胎发育中起关键作用。蛋白本身无酶活性(PAD inactive)。核定位信号较弱(ECO:0000250 only)，主要定位在 oocyte cytoplasm/cortical granule/cytoplasmic lattice。SCMC 复合体关联和部分染色质调控因子互作(SUV39H1, UHRF1)提供一定调控潜力。4个X-ray PDB结构覆盖全长，结构信息丰富。

**推荐**: 中等优先级。核定位证据偏间接，但染色质调控因子 PPI 和完整结构值得关注。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q6TGC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6TGC4
- PDB: 4DAT, 4DAU, 8QL0, 9FMN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PADI6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000276747-PADI6 (HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。)

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/PADI6/PADI6-PAE.png]]


#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| OOEP | STRING | 0.965 |
| TLE6 | STRING | 0.95 |
| SFN | STRING | 0.904 |
| NLRP5 | STRING | 0.873 |
| KHDC3L | STRING | 0.829 |
| ZNF526 | IntAct | psi-mi:"MI:0397"(two hybrid ar |
| DDIT4L | IntAct | psi-mi:"MI:1112"(two hybrid pr |
| SUV39H1 | IntAct | psi-mi:"MI:1356"(validated two |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/PADI6/PADI6-PAE.png]]
