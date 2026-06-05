---
type: protein-evaluation
gene: "TRIM15"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## TRIM15 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TRIM15 / RNF93, ZNF178, ZNFB7 |
| 蛋白全名 | E3 ubiquitin-protein ligase TRIM15 |
| 蛋白大小 | 465 aa / 52.1 kDa |
| UniProt ID | Q9C019 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | UniProt nucleus (IDA:UniProt); GO nucleus (IDA); 但 HPA 分类为 Centriolar satellite + Cytosol，非核 |
| 蛋白大小 | 5/10 | x1 | 5.0 | 465 aa, 52.1 kDa |
| 研究新颖性 | 8/10 | x5 | 40.0 | PubMed strict=29 |
| 三维结构 | 5/10 | x3 | 15.0 | AF pLDDT 83.9 (49.7% >90); PDB 1个 (7QS2, SPRY domain) |

![[TRIM15-PAE.png]]
| 调控结构域 | 6/10 | x2 | 12.0 | RING finger (E3 ligase) + B-box + SPRY/B30.2 domain; 典型 TRIM 家族架构 |
| PPI 网络 | 5/10 | x3 | 15.0 | STRING 中 PXN (0.63 exp); IntAct 含 AXIN1/TRIM8/CDK6 等 Y2H |
| **加权总分** | | | **103/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **56.3/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus (ECO:0000269), Cytoplasm (ECO:0000269), Focal adhesion | 实验证据 (IDA) |
| GO-CC | nucleus (IDA:UniProt), cytoplasm (IBA) | 直接实验 |
| HPA (IF) | Centriolar satellite, Cytosol (main: Cytosol) | Approved, 但未列核定位 |
| 文献 | PMID:25450970 focal adhesion protein; PMID:34497368 ERK activation | 部分胞质/黏着斑功能 |

**HPA IF 状态**: Approved — 6 张 IF 原图可用，显示 Centriolar satellite + Cytosol 定位，HPA 未确认核定位。![[TRIM15-IF1.jpg]]![[TRIM15-IF2.jpg]]

**结论**: TRIM15 在 UniProt/GO 中有 IDA 级别的核定位证据，但 HPA IF 分类不包含核定位，一致性不足。保留为低置信度核蛋白候选，需独立验证。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q9C019-F1 |
| 平均 pLDDT | 83.9 |
| pLDDT >90 | 49.7% |
| pLDDT <50 | 8.0% |
| PDB | 7QS2 (1.70A, SPRY domain 289-465) |
| InterPro | IPR001870 (B-box), IPR003877 (SPRY), IPR001841 (RING finger), IPR000315 (B30.2) |
| Pfam | PF13765 (B-box), PF00622 (SPRY), PF00643 (B-box), PF00097 (RING finger) |

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 29 |
| PubMed broad | 42 |
| 别名 | RNF93, ZNF178, ZNFB7（未用于 scoring） |

关键文献：PMID:40138455 (OA chondrocyte senescence, 2025), PMID:34497368 (ERK Lys63-ubiquitination, Nature Cell Biology 2021), PMID:38657551 (pancreatic cancer, 2024), PMID:41461634 (Wnt/Axin1, colorectal cancer, 2025), PMID:25450970 (focal adhesion, colon cancer, 2015). 文献集中于 2021-2025，为近年新兴靶点。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| PXN | STRING | 0.63 (exp 0.299) | Focal adhesion scaffold |
| AXIN1 | IntAct+UniProt | Y2H (PMID:26871637) | Wnt 信号 |
| CDK6 | IntAct+UniProt | Y2H | 细胞周期 |
| TRIM8 | IntAct | Y2H | TRIM 家族，NF-kB 调控 |
| MAVS | STRING | 0.495 (exp 0.065) | 抗病毒免疫 |
| EHMT1 | IntAct | Y2H | 组蛋白甲基转移酶 |
| IRF5 | IntAct | Y2H | 干扰素调控因子 |
| FBLIM1 | STRING | 0.461 (exp 0.292) | 细胞粘附 |
| UBE2U | IntAct | Y2H | E2 泛素结合酶 |
| MYBL2 | IntAct | Y2H | 转录因子 |

PPI 网络以 Y2H 互作为主，涵盖 Wnt/Axin1、细胞周期、免疫及黏着斑通路，但物理互作验证多为高通量筛选，独立验证较少。

### 4. 总体评价
TRIM15 为近年关注度上升的 TRIM 家族 E3 ligase（RING + B-box + SPRY），PubMed=29 属中低文献量。HPA IF 不确认核定位为其主要弱点（仅 Cytosol/Centriolar satellite），虽 UniProt IDA 支持核定位，定位证据矛盾需补内源 IF。结构预测中等（AF pLDDT 83.9），SPRY domain 已有晶体结构。建议优先补 IF 确认核定位后再决定是否深入。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9C019
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9C019
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM15
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204610-TRIM15

**HPA IF 状态**: HPA IF 图像已本地嵌入。

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TRIM15/IF_images/TRIM15_IF_807_E7_1_blue_red_green.jpg]]。核定位基于HPA localization/reliability + UniProt + GO-CC。


![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TRIM15/TRIM15-PAE.png]]

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TRIM15/TRIM15-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9C019-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
