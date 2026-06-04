---
type: protein-evaluation
gene: "TLE6"
date: 2026-06-02
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## TLE6 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TLE6 / GRG6 |
| 蛋白全名 | Transducin-like enhancer protein 6 |
| 蛋白大小 | 572 aa / 63.5 kDa |
| UniProt ID | Q9H808 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | Cytoplasm (ECO:0000269, 3x) + Nucleus (ECO:0000250); GO nucleus IBA, transcription regulator complex IBA |
| 蛋白大小 | 10/10 | ×1 | 10.0 | 572 aa, 63.5 kDa, 处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed strict=40, symbol_only=58, broad=63 |
| 三维结构 | 8/10 | ×3 | 24.0 | 2 PDB (8X7V/8X7W, EM 3.01-3.36A) + AF pLDDT=66.3 |
| 调控结构域 | 7/10 | ×2 | 14.0 | 5 domains (4 InterPro + 1 Pfam): WD40 repeats, Groucho_enhancer |
| PPI 网络 | 4/10 | ×3 | 12.0 | IntAct 15 + STRING 15 + UniProt 5; SCMC + transcription regulation |
| **加权总分** | | | **116/180**** | |
| 互证加分 | | | +1.0 | PDB+AF 互证(+0.5); 多库结构域一致(+0.5) |
| **归一化总分 (÷1.83)** | | | **63.4/100**** | |

![[TLE6-PAE.png]]

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Cytoplasm (ECO:0000269, 3x); Nucleus (ECO:0000250); Cytoplasm (ECO:0000269, 2x) | 实验证据(胞质) + by similarity(核) |
| GO-CC | cell cortex ISS; cytoplasm IDA; cytoplasmic lattice IDA; nucleus IBA; protein-containing complex IMP; sperm midpiece ISS; subcortical maternal complex IDA; transcription regulator complex IBA | 实验+预测 |
| Protein Atlas (IF) | HPA 无图像数据 | 无数据 |

**HPA IF 状态**: No HPA data — 核定位证据为 ECO:0000250 (by similarity) 和 IBA，非直接实验。主要定位在 cytoplasm/cytoplasmic lattice (IDA) 和 SCMC (IDA)。

**结论**: 胞质定位为主(SCMC component)。Nucleus 定位证据较弱(by similarity + IBA)。Transcription regulator complex (IBA) 关联暗示潜在核功能。

#### 3.2 结构与结构域

| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q9H808-F1 (v6) |
| 平均 pLDDT | 66.3 |
| pLDDT >90 / 70-90 / 50-70 / <50 | 37.2% / 16.4% / 10.1% / 36.2% |
| PDB | 8X7V (EM 3.01A, C=146-572), 8X7W (EM 3.36A, C/F=146-572) |

| 来源 | 结构域 |
|---|---|
| InterPro | IPR009146 (Groucho_enhancer), IPR015943 (WD40/YVTN_repeat-like_dom_sf), IPR036322 (WD40_repeat_dom_sf), IPR001680 (WD40_rpt) |
| Pfam | PF00400 (WD40) |

**评价**: TLE/Groucho 家族成员。WD40 repeat domain (C-terminal 146-572) 有2个 EM 实验结构。AF pLDDT 66.3，N-terminal 区域置信度低(36.2% <50)。Groucho_enhancer domain 暗示其与 TLE 转录辅抑制功能的进化关系。

#### 3.3 研究现状

| 指标 | 数值 |
|---|---|
| PubMed strict | 40 |
| PubMed symbol_only | 58 |
| PubMed broad | 63 |

**关键文献**:
1. Campos G et al. (2023). "Total fertilization failure after ICSI: insights into pathophysiology, diagnosis, and management through artificial oocyte activation." *Hum Reprod Update*. PMID: 36977357
2. Sang Q et al. (2021). "Genetic factors as potential molecular markers of human oocyte and embryo quality." *J Assist Reprod Genet*. PMID: 33895934
3. Li R et al. (2024). "Biallelic Recessive Mutations in TLE6 and NLRP5 Cause Female Infertility Characterized by Human Early Embryonic Arrest." *Hum Mutat*. PMID: 40225929
4. Chi P et al. (2024). "Structural basis of the subcortical maternal complex and its implications in reproductive disorders." *Nat Struct Mol Biol*. PMID: 38177687
5. Rui X et al. (2024). "Variants in NLRP2 and ZFP36L2, non-core components of the human subcortical maternal complex, cause female infertility..." *Mol Hum Reprod*. PMID: 39178021

**评价**: 研究集中在 early embryonic development 和 SCMC (subcortical maternal complex)。Human infertility 致病基因。新颖性中等(40 strict)。

#### 3.4 PPI 网络

**UniProt 实验互作**:

| Partner | Experiments | Relevance |
|---|---|---|
| BDNF | 3 | Neurotrophin |
| KLK6 | 3 | Serine protease |
| KHDC3L | 2 | SCMC component |
| NLRP5 | 2 | SCMC core |
| OOEP | 2 | SCMC core |

**STRING 预测互作** (score >0.4):

| Partner | Score | Experimental | Relevance |
|---|---|---|---|
| OOEP | 0.999 | 0.300 | SCMC |
| NLRP5 | 0.994 | 0.300 | SCMC |
| KHDC3L | 0.993 | 0.292 | SCMC |
| PADI6 | 0.950 | 0 | SCMC |
| NLRP2 | 0.813 | 0 | SCMC |
| HLF | 0.788 | 0 | Transcription factor |
| TLE5 | 0.781 | 0.050 | TLE family |
| TCF3 | 0.665 | 0.069 | Wnt/transcription |

**已知复合体**: Subcortical maternal complex (GO:0106333, IDA); Transcription regulator complex (GO:0005667, IBA)

**评价**: PPI 以 SCMC (OOEP/NLRP5/KHDC3L/PADI6) 为绝对核心。同时有 transcription regulator complex (IBA) 和 TCF3/TLE5 互作暗示转录调控潜力。TLE/Groucho 家族是经典转录辅抑制因子家族。

#### 3.5 多库互证

| 维度 | 来源 | 结果 | 一致性 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 2 PDB (EM) + AF | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 5 个 (WD40/Groucho) | 多库一致 |
| PPI 网络 | STRING + IntAct + UniProt | SCMC core | 多源一致 |
| 核定位 | HPA/UniProt/GO | Cytoplasm + Nucleus | 部分一致 |

**互证加分明细**: PDB+AF互证(+0.5), 多库结构域一致(+0.5), 总计 +1.0

### 4. 总体评价

TLE6 是 SCMC (subcortical maternal complex) 的核心组分，属于 TLE/Groucho 转录辅抑制因子家族。SCMC 功能明确(early embryonic development)，且是 human infertility 致病基因。TLE 家族本身是经典转录 repressor，但 TLE6 的核定位证据较弱(by similarity)。WD40 结构域有实验结构。PPI 以 SCMC 为核心，TCF3/TLE5 互作提供转录调控潜力。

**推荐**: 中等优先级。TLE/Groucho 家族背景暗示转录调控潜力，但核定位证据不足，以 cytoplasmic lattice/SCMC 功能为主。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q9H808
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H808
- PDB: 8X7V, 8X7W
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TLE6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104953-TLE6 (no data)

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 — HPA 暂无 IF 原图数据。核定位基于 UniProt + GO-CC。

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/TLE6/TLE6-PAE.png]]


#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| OOEP | STRING | 0.999 |
| NLRP5 | STRING | 0.994 |
| KHDC3L | STRING | 0.993 |
| PADI6 | STRING | 0.95 |
| NLRP2 | STRING | 0.813 |
| RPL14 | IntAct | psi-mi:"MI:0397"(two hybrid ar |
| NUDC | IntAct | psi-mi:"MI:0729"(luminescence  |
| KLK6 | IntAct | psi-mi:"MI:0397"(two hybrid ar |

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/TLE6/TLE6-PAE.png]]
