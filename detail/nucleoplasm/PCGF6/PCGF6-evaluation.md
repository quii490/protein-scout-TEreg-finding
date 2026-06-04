---
type: protein-evaluation
gene: "PCGF6"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## PCGF6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PCGF6 / MBLR, RNF134 |
| 蛋白全名 | Polycomb group RING finger protein 6 |
| 蛋白大小 | 350 aa / 39.0 kDa |
| UniProt ID | Q9BYE7 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | UniProt Nucleus (ECO:0000269 x2); GO-CC nucleoplasm (TAS) + nucleus (IDA) + PcG complex (IDA) + PRC1 complex (IDA); HPA 无数据 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 350 aa, 39.0 kDa, 小型 Polycomb 蛋白 |
| 研究新颖性 | 8/10 | x5 | 40.0 | PubMed strict=31, broad=74 |
| 三维结构 | 5/10 | x3 | 15.0 | 1 PDB (2DJB, NMR); AlphaFold mean pLDDT 72.0; pct_gt_90=37.7% |

![[PCGF6-PAE.png]]
| 调控结构域 | 7/10 | x2 | 14.0 | RING finger (IPR001841) + Zinc finger (IPR013083); PRC1.6 核心; H2A ubiquitination |
| PPI 网络 | 8/10 | x3 | 24.0 | STRING: RING1 0.999, RNF2 0.999, L3MBTL2 0.997, E2F6 0.997; IntAct 15 条; UniProt 5 条 |
| **加权总分** | | | **138/180********** | |
| 互证加分 | | | +2.0 | PRC1.6 complex; 非经典 Polycomb; H2AK119ub |
| **归一化总分 (÷1.83)** | | | **75.4/100********** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus (ECO:0000269 x2) | Curated, 2 篇文献支持 |
| GO-CC | nucleoplasm (TAS:Reactome), nucleus (IDA:UniProtKB), PcG protein complex (IDA), PRC1 complex (IDA) | 实验支持 |
| Protein Atlas (IF) | 无定位数据 (no_image_detected) | 未确认 |
| Function | PRC1.6 复合体核心; 转录抑制; H2AK119 monoubiquitination | 核内功能 |

**HPA IF 状态**: HPA 对 PCGF6 无任何定位数据 (subcellular_location=[]，image_status="no_image_detected")，完全无 IF 图像或缩略图。核定位完全依赖 UniProt + GO-CC。

**结论**: PCGF6 核定位证据来自 UniProt 双重 curated (ECO:0000269) 和 GO-CC 多重 IDA（PcG complex, PRC1 complex, nucleus），功能上作为 PRC1.6 核心催化 H2AK119ub。但缺乏 HPA IF 独立验证。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q9BYE7-F1 (v6) |
| 平均 pLDDT | 72.0 |
| pLDDT >90 | 37.7% |
| pLDDT 70-90 | 20.6% |
| pLDDT <50 | 26.9% |
| PDB | 2DJB (NMR, RING domain, aa 124-182) |
| InterPro | IPR051507, IPR046979, IPR032443, IPR029071, IPR001841 (RING finger), IPR013083 (ZnF), IPR017907 (ZnF) |
| Pfam | PF16207, PF13923 (zf-C3HC4_2, RING) |

AlphaFold 置信度中等 (mean 72.0)，26.9% 残基 pLDDT <50。仅 1 个 PDB 结构 (2DJB, NMR) 覆盖 RING domain。整体结构覆盖有限，但 RING 域有实验验证。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 31 |
| PubMed symbol only | 38 |
| PubMed broad | 74 |
| 别名 | MBLR, RNF134（未用于 scoring） |

关键文献：
- PMID:36890610 (Zhu M et al., 2023) -- PCGF6/MAX/KDM5D 通过启动子低甲基化促进 MAZ/CDK4 表达和 pRCC 进展
- PMID:35364009 (Zhu Y et al., 2022) -- Polycomb 复合体在维持胚胎干细胞多能性中的功能冗余
- PMID:25591775 (Sun J et al., 2015) -- PCGF6 敲低调控小鼠雄性生殖细胞体外分化
- PMID:29381691 (Stielow B et al., 2018) -- MGA/L3MBTL2/E2F6 决定非经典 PRC1.6 的基因组结合
- PMID:35933409 (Lan X et al., 2022) -- PCGF6 通过激活 SOX2 表达控制人多能干细胞神经外胚层特化

PCGF6 研究集中在 Polycomb 生物学和干细胞分化。PRC1.6 是非经典 PRC1 复合体（含 MGA/L3MBTL2/E2F6/MAX），与经典 PRC1 (CBX/PHC/SCM) 不同。文献量低 (strict=31)，新颖性良好。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| RING1 | STRING | 0.999 (exp 0.899) | PRC1 core, UniProt 6 exps |
| RNF2 | STRING | 0.999 (exp 0.920) | PRC1 catalytic, UniProt 9 exps |
| YAF2 | STRING | 0.999 (exp 0.795) | PRC1 accessory |
| L3MBTL2 | STRING | 0.997 (exp 0.844) | PRC1.6 unique component |
| E2F6 | STRING | 0.997 (exp 0.839) | PRC1.6 unique component |
| RYBP | STRING | 0.996 (exp 0.846) | PRC1 variant |
| CBX3 | STRING | 0.996 (exp 0.805) | Chromobox protein |
| CBX7 | STRING | 0.989 (exp 0.756) | Chromobox, UniProt 6 exps |
| CBX8 | STRING | 0.986 (exp 0.679) | Chromobox, UniProt 5 exps |
| BMI1 | STRING | 0.988 (exp 0.421) | PRC1 core |
| RING1 | IntAct | Y2H (PMID:22493164) | PRC1 core |
| RNF2 | IntAct | Y2H (PMID:22493164), pull-down | PRC1 catalytic |
| Rybp | IntAct | co-IP (PMID:22325148) | PRC1 variant |
| Cbx7 | IntAct | co-IP (PMID:22325148) | Chromobox |
| H3C1 | IntAct | BioID (PMID:29568061) | Histone H3 (proximity) |
| CBX4 | UniProt | 2 experiments | Chromobox |
| CBX7 | UniProt | 6 experiments | Chromobox |
| CBX8 | UniProt | 5 experiments | Chromobox |

PCGF6 PPI 网络极为完整，以 PRC1.6 非经典 Polycomb 复合体为核心：RING1/RNF2 催化核心 (STRING >0.999)、L3MBTL2/E2F6 PRC1.6 特征组分 (STRING >0.997)、CBX 家族 chromobox 蛋白。多来源互证（STRING + IntAct + UniProt）。

### 4. 总体评价
PCGF6 是本批次评分最高的基因之一。作为非经典 PRC1.6 复合体核心，核定位有强大的 UniProt/GO-CC 支持，PPI 网络极为完整（PRC1 多组分实验互作）。研究热度低 (strict=31)，新颖性良好。结构数据中等（仅 1 PDB, mean pLDDT 72.0）。PRC1.6 作为与经典 PRC1 不同的 Polycomb 变体，niche 空间充足。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BYE7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BYE7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCGF6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156374-PCGF6

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PCGF6/PCGF6-PAE.png]]

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PCGF6/PCGF6-PAE.png]]
