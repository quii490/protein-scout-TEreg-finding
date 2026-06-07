---
type: protein-evaluation
gene: "PREPL"
date: 2026-06-02
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## PREPL 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PREPL / KIAA0436 |
| 蛋白全名 | Prolyl endopeptidase-like |
| 蛋白大小 | 727 aa / 83.9 kDa |
| UniProt ID | Q4J6C6 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | Cytosol + Golgi + Nucleus (ECO:0000269); GO nucleus IEA |
| 蛋白大小 | 10/10 | ×1 | 10.0 | 727 aa, 83.9 kDa, 处于理想范围 |
| 研究新颖性 | 6/10 | ×5 | 30.0 | PubMed strict=44, symbol_only=96, broad=404 |
| 三维结构 | 8/10 | ×3 | 24.0 | 2 PDB (7OBM X-ray 3.10A, 8RFB EM 4.01A) + AF pLDDT=82.8 |
| 调控结构域 | 7/10 | ×2 | 14.0 | 7 domains (5 InterPro + 2 Pfam): Peptidase_S9, AB_hydrolase |
| PPI 网络 | 3/10 | ×3 | 9.0 | IntAct 15 + STRING 15 + UniProt 0; 代谢/蛋白酶相关 |
| **加权总分** | | | **103/180**** | |
| 互证加分 | | | +1.0 | PDB+AF 互证(+0.5); 多库结构域一致(+0.5) |
| **归一化总分 (÷1.83)** | | | **56.3/100**** | |


### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Cytoplasm, cytosol (ECO:0000269); Golgi apparatus, trans-Golgi network (ECO:0000250); Cytoplasm, cytoskeleton (ECO:0000250); Golgi apparatus (ECO:0000250); Nucleus (ECO:0000269) | 实验证据 |
| GO-CC | cytoskeleton IBA; cytosol IEA; Golgi apparatus IBA; mitochondrion HTP; nucleus IEA; trans-Golgi network IEA | 混合证据 |
| Protein Atlas (IF) | HPA 有 IHC/RNA 数据但 IF 未获取 | 未确认 |

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 — Nucleus 定位有 ECO:0000269 (experimental). 但主要定位在 cytosol/Golgi/cytoskeleton。

**结论**: 多亚细胞定位，nucleus 有实验证据但非主导定位。主要功能在 cytosol 和 Golgi。

#### 3.2 结构与结构域

| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q4J6C6-F1 (v6) |
| 平均 pLDDT | 82.8 |
| pLDDT >90 / 70-90 / 50-70 / <50 | 64.0% / 17.3% / 3.7% / 15.0% |
| PDB | 7OBM (X-ray 3.10A, A=90-727), 8RFB (EM 4.01A, A=90-727) |

| 来源 | 结构域 |
|---|---|
| InterPro | IPR029058 (AB_hydrolase_fold), IPR023302 (Pept_S9A_N), IPR001375 (Peptidase_S9_cat), IPR002470 (Peptidase_S9A), IPR051543 (Serine_Peptidase_S9A) |
| Pfam | PF00326 (Peptidase_S9), PF02897 (Peptidase_S9_N) |

**评价**: AF pLDDT 82.8，结构预测置信度高。2个实验PDB结构覆盖 catalytic domain (90-727)。Prolyl endopeptidase S9A 家族典型结构。N-terminal (1-89) 在PDB中未被解析，15% 残基 pLDDT <50 可能对应于此区域。

#### 3.3 研究现状

| 指标 | 数值 |
|---|---|
| PubMed strict | 44 |
| PubMed symbol_only | 96 |
| PubMed broad | 404 (含非特异) |

**关键文献**:
1. Monnens Y et al. (2024). "Missense variants in CMS22 patients reveal that PREPL has both enzymatic and nonenzymatic functions." *JCI Insight*. PMID: 39078710
2. Kramer NJ et al. (2023). "Regulators of mitonuclear balance link mitochondrial metabolism to mtDNA expression." *Nat Cell Biol*. PMID: 37770567
3. Rosier K et al. (2021). "Prolyl endopeptidase-like is a (thio)esterase involved in mitochondrial respiratory chain function." *iScience*. PMID: 34888501
4. Adam MP et al. (1993). "Congenital Myasthenic Syndromes Overview." PMID: 20301347
5. Dang Y et al. (2021). "Cleavage of PrePL by Lon promotes growth and pathogenesis in Magnaporthe oryzae." *Environ Microbiol*. PMID: 33225564

**评价**: Congenital Myasthenic Syndrome (CMS22) 致病基因，研究集中在神经肌肉疾病和线粒体代谢。strict=44 篇，中等新颖性。

#### 3.4 PPI 网络

**实验验证互作** (IntAct):

| Partner | 方法 | PMID | Relevance |
|---|---|---|---|
| COIL | two hybrid | 16713569 | Cajal body |
| CAPN3 | two hybrid fragment | 23414517 | Calpain protease |
| USP22 | anti tag coIP | 19615732 | Deubiquitinase, chromatin |
| NR4A1 | display technology | 20195357 | Nuclear receptor |
| RGS4 | anti tag coIP | 28514442 | GPCR signaling |
| ACAA2 | anti tag coIP | 28514442 | Mitochondrial |
| HSPD1 | BioID proximity | 29568061 | Mitochondrial chaperone |
| C1QBP | anti tag coIP | 27499296 | Mitochondrial |
| MRPL1 | anti tag coIP | 27499296 | Mitochondrial |

**STRING 预测互作** (score >0.4):

| Partner | Score | Experimental | Relevance |
|---|---|---|---|
| CAMKMT | 0.976 | 0 | Calmodulin-lysine methyltransferase |
| SLC3A1 | 0.972 | 0 | Amino acid transport |
| PPM1B | 0.967 | 0 | Protein phosphatase |
| APEH | 0.580 | 0.242 | Acylaminoacyl-peptidase |

**评价**: PPI 以代谢酶和线粒体蛋白为主 (HSPD1, C1QBP, MRPL1, ACAA2)。USP22 (chromatin deubiquitinase, SAGA complex) 和 NR4A1 (nuclear receptor) 互作提供有限核调控链接。无染色质调控核心网络。

#### 3.5 多库互证

| 维度 | 来源 | 结果 | 一致性 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 2 PDB + AF | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 7 个 | 多库一致 |
| PPI 网络 | IntAct + STRING | 代谢/线粒体为主 | 一致 |
| 核定位 | HPA/UniProt/GO | Nucleus + Cytosol + Golgi | 部分一致 |

**互证加分明细**: PDB+AF互证(+0.5), 多库结构域一致(+0.5), 总计 +1.0

### 4. 总体评价

PREPL 是 serine peptidase S9A 家族成员，主要功能在蛋白水解和线粒体呼吸链。核定位有实验证据但非主导。CMS22 致病基因，疾病关联明确但在 TE/染色质调控背景下不突出。PPI 以代谢蛋白为主，USP22 (chromatin deubiquitinase) 互作提供有限调控价值。2个PDB结构覆盖催化域，AF结构置信度高。

**推荐**: 中等优先级。结构信息丰富，但染色质调控关联有限。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q4J6C6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4J6C6
- PDB: 7OBM, 8RFB
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PREPL
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138078-PREPL (HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。)

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 — HPA 暂无 IF 原图数据。核定位基于 UniProt + GO-CC。



#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| CAMKMT | STRING | 0.976 |
| SLC3A1 | STRING | 0.972 |
| PPM1B | STRING | 0.967 |
| ALG14 | STRING | 0.665 |
| DPAGT1 | STRING | 0.583 |
| COIL | IntAct | psi-mi:"MI:0018"(two hybrid) |
| nagA | IntAct | psi-mi:"MI:0398"(two hybrid po |
| CAPN3 | IntAct | psi-mi:"MI:0399"(two hybrid fr |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q4J6C6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q4J6C6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029058;IPR023302;IPR001375;IPR002470;IPR051543; |
| Pfam | PF00326;PF02897; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138078-PREPL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARHGAP36 | Biogrid | false |
| C1QBP | Biogrid | false |
| CS | Biogrid | false |
| IMMP2L | Biogrid | false |
| MRM1 | Biogrid | false |
| MTG2 | Biogrid | false |
| PMPCA | Biogrid | false |
| TUFM | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
