---
type: protein-evaluation
gene: "GTSE1"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## GTSE1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GTSE1 |
| 蛋白全名 | G2 and S phase-expressed protein 1 |
| 蛋白大小 | 739 aa / 78.5 kDa |
| UniProt ID | Q9NYZ3 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | HPA: Nucleoplasm 为 additional (非 main); UniProt: Cytoplasm/cytoskeleton; GO: nucleoplasm TAS only |
| 蛋白大小 | 4/10 | ×1 | 4.0 | 739 aa, 78.5 kDa |
| 研究新颖性 | 2/10 | ×5 | 10.0 | PubMed strict=95, broad=122 |
| 三维结构 | 5/10 | ×3 | 15.0 | PDB 6QNN/6QNP 部分 C-term; AlphaFold pLDDT 50.9, 61% <50 |

| 调控结构域 | 5/10 | ×2 | 10.0 | GTSE1 family; 细胞周期 G2/M 调控; 微管结合 |
| PPI 网络 | 6/10 | ×3 | 18.0 | UniProt PLK1 (6 exp) strong; IntAct 多 partners; STRING 获取失败 |
| **加权总分** | | | **73/180**** | |
| 互证加分 | | | +1.0 | PLK1 强互作; HPA nucleoplasm 信号 |
| **归一化总分 (÷1.83)** | | | **39.9/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Cytoplasm, cytoskeleton | No evidence code |
| GO-CC | cytoplasmic microtubule IDA; cytosol TAS; membrane HDA; nucleoplasm TAS:Reactome | Mixed |
| Protein Atlas (IF) | Plasma membrane + Centrosome (main); Nucleoplasm + Primary cilium + Cytosol (additional); Supported | Supported |

**HPA IF 状态**: IF available (Supported reliability) — HPA 主定位为 Plasma membrane 和 Centrosome，Nucleoplasm 仅列为 additional location，且可靠性评级为 Supported（低于 Approved）。UniProt 和 GO 均以胞质/微管为主要定位，核质仅为 Reactome pathway 推断（TAS）。核定位证据薄弱。

#### 3.2 结构与结构域
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q9NYZ3-F1 |
| 平均 pLDDT | 50.9 |
| pLDDT >90 | 2.0% |
| pLDDT 70-90 | 8.0% |
| pLDDT 50-70 | 29.0% |
| pLDDT <50 | 61.0% |
| PDB | 6QNN (X-ray 2.03A, B=661-726); 6QNP (X-ray 2.70A, H/I/J/K=653-719) |
| InterPro | IPR026657, IPR032768 |
| Pfam | PF15259 |

**AlphaFold PAE 状态**: PAE 已下载，见上图。整体 pLDDT 很低（50.9），61% 残基置信度低于 50。PDB 结构仅覆盖 C 端约 60 个残基。结构信息极为有限。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 95 |
| PubMed broad | 122 |

GTSE1 研究热度较高，接近 rejection 阈值。关键文献覆盖其在非小细胞肺癌中的促增殖作用（PMID:37079439, ERK/MAPK pathway）、肺纤维化 EMT（PMID:39342428）、骨肉瘤微环境（PMID:40831537）、肺癌细胞周期调控（PMID:39026496）及作为泛肿瘤预后生物标志物（PMID:38715380）。研究集中在肿瘤生物学，功能较为明确。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| PLK1 | UniProt | 6 experiments | Cell cycle kinase, strong |
| GGA1 | UniProt | 2 experiments | Golgi trafficking |
| USP11 | IntAct | anti tag coIP (PMID:19615732) | Deubiquitinase |
| PICALM | IntAct | anti tag coIP (PMID:28514442) | Clathrin-mediated endocytosis |
| STAMBPL1 | IntAct | anti tag coIP (PMID:28514442) | Deubiquitinase |
| STAMBP | IntAct | anti tag coIP (PMID:28514442) | Deubiquitinase |
| NCAPH2 | IntAct | anti tag coIP (PMID:28514442) | Condensin II, chromosome |
| RNF213 | IntAct | pull down (PMID:30833792) | Ubiquitin ligase |
| PPP2R3A | IntAct | anti tag coIP (PMID:28514442) | PP2A phosphatase |
| — | STRING | 获取失败 (HTTP 502) | — |

PLK1 是最强互作（UniProt 6 experiments），与 GTSE1 的细胞周期 G2/M 调控功能一致。NCAPH2（condensin II）可能提示染色体关联。STRING 数据未获取。PPI 网络指向细胞周期调控、泛素化和内吞通路。

### 4. 总体评价
GTSE1 在本批中评分最低（40.4/100）。主要问题：核定位仅为 HPA additional（非主定位）、蛋白较大（78.5 kDa）、研究热度高（PM=95）、结构置信度极低。核质定位可能为其在细胞周期特定阶段（G2/S）的瞬时核转运。PLK1 强互作和 condensin II 关联有一定意义，但总体核定位支持不足。建议谨慎保留为低优先级候选。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYZ3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYZ3
- PDB: 6QNN, 6QNP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GTSE1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000075218-GTSE1

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GTSE1/IF_images/1512_G12_3_blue_red_green.jpg]]

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GTSE1/IF_images/1512_G12_1_blue_red_green.jpg]]


HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NYZ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
