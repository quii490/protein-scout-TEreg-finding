---
type: protein-evaluation
gene: "PHF19"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## PHF19 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PHF19 / PCL3 |
| 蛋白全名 | PHD finger protein 19 |
| 蛋白大小 | 580 aa / 65.6 kDa |
| UniProt ID | Q5T6S3 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32.0 | UniProt Nucleus (ECO:0000269 x2); GO-CC ESC/E(Z) complex (IDA) + nucleoplasm (TAS) + nucleus (IBA); HPA 无数据 |
| 蛋白大小 | 6/10 | x1 | 6.0 | 580 aa, 65.6 kDa |
| 研究新颖性 | 4/10 | x5 | 20.0 | PubMed strict=62, broad=88 |
| 三维结构 | 7/10 | x3 | 21.0 | 4 PDB; AlphaFold mean pLDDT 69.1; pct_gt_90=43.3%; pct_lt_50=36.6% |

![[PHF19-PAE.png]]
| 调控结构域 | 8/10 | x2 | 16.0 | PHD finger (IPR001965, IPR019786) + Tudor (IPR002999); H3K36me3 reader |
| PPI 网络 | 8/10 | x3 | 24.0 | STRING: PRC2 core (SUZ12 0.998, EZH2 0.989, EED 0.972); IntAct 15 条; UniProt 27 条 |
| **加权总分** | | | **119/180********** | |
| 互证加分 | | | +2.0 | Polycomb PRC2 复合体; H3K36me3 -> H3K27me3 转换 |
| **归一化总分 (÷1.83)** | | | **65.0/100********** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus (ECO:0000269 x2) | Curated, 2 篇文献支持 |
| GO-CC | ESC/E(Z) complex (IDA), nucleoplasm (TAS:Reactome), nucleus (IBA:GO_Central) | 实验 + 推断 |
| Protein Atlas (IF) | 无定位数据 (no_image_detected) | 未确认 |

**HPA IF 状态**: HPA 对 PHF19 无任何定位数据 (subcellular_location=[]，image_status="no_image_detected")。核定位完全依赖 UniProt + GO-CC。

**结论**: PHF19 核定位证据来自 UniProt 双重 curated 和 GO-CC IDA（PRC2 复合体成员）。作为 H3K36me3 reader 和 PRC2 招募因子，必须在核内发挥功能。但缺乏 HPA IF 独立验证。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q5T6S3-F1 (v6) |
| 平均 pLDDT | 69.1 |
| pLDDT >90 | 43.3% |
| pLDDT 70-90 | 14.1% |
| pLDDT <50 | 36.6% |
| PDB | 2E5Q (NMR, Tudor), 4BD3 (NMR, Tudor), 6NQ3 (2.89A, C-term/PRC2), 6WAU (1.75A, PHD finger) |
| InterPro | IPR040477, IPR025894, IPR042017, IPR002999 (Tudor), IPR047400, IPR019786 (PHD), IPR011011, IPR001965 (PHD), IPR019787, IPR013083 |
| Pfam | PF14061, PF00628 (PHD), PF18104 |

AlphaFold 整体置信度中等 (mean 69.1)，36.6% 残基 pLDDT <50，提示蛋白含大量无序区段。但功能结构域（PHD finger, Tudor）均有高分辨率 PDB 覆盖（1.75A PHD, NMR Tudor）。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 62 |
| PubMed symbol only | 79 |
| PubMed broad | 88 |
| 别名 | PCL3（未用于 scoring） |

关键文献：
- PMID:41129231 (Yuan S et al., 2025) -- PHF19-YTHDC1 condensate 切换 EZH2 介导的基因抑制为激活 (前列腺癌)
- PMID:33611744 (Gu W et al., 2021) -- PHF19 通过表观遗传调控 SIRT2 促进心肌肥大
- PMID:34129846 (Xiaoyun S et al., 2021) -- PHF19 激活 Hedgehog 信号促进肝癌发生
- PMID:29898995 (Gollavilli PN et al., 2018) -- EWS/ETS 驱动的 Ewing 肉瘤需要 BET 蛋白
- PMID:22487681 (Ghislin S et al., 2012) -- PHF19 和 Akt 控制黑色素瘤增殖/侵袭转换

PHF19 作为 PRC2 辅助因子，通过 Tudor 域识别 H3K36me3，招募 PRC2 催化 H3K27me3 沉积。研究集中在肿瘤表观遗传学（前列腺癌、肝癌、黑色素瘤、Ewing 肉瘤）。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| SUZ12 | STRING | 0.998 (exp 0.985) | PRC2 core |
| JARID2 | STRING | 0.995 (exp 0.921) | PRC2 accessory |
| RBBP4 | STRING | 0.991 (exp 0.938) | PRC2 core |
| EZH2 | STRING | 0.989 (exp 0.881) | PRC2 catalytic |
| EED | STRING | 0.972 (exp 0.884) | PRC2 core |
| EPOP | STRING | 0.997 (exp 0.743) | PRC2 accessory |
| MTF2 | STRING | 0.975 (exp 0.198) | PRC2 accessory |
| EZH1 | STRING | 0.971 (exp 0.827) | PRC2 paralog |
| RIOX1 | STRING | 0.94 (textmining) | H3K36 demethylase |
| EED | IntAct | co-IP (PMID:28514442) | PRC2 core |
| YTHDC1 | IntAct | validated Y2H (PMID:32296183) | m6A reader + condensate |
| TSPYL2 | IntAct | Y2H (PMID:32296183) | Chromatin |
| SUV39H1 | UniProt | 2 experiments | H3K9 methyltransferase |
| SUV39H2 | UniProt | 2 experiments | H3K9 methyltransferase |
| KDM1A | UniProt | 2 experiments | H3K4 demethylase |
| RCOR3 | UniProt | 3 experiments | CoREST complex |

PPI 网络以 PRC2 复合体为核心，STRING 显示与 SUZ12/EZH2/EED/RBBP4 等核心亚基均有极强实验互作。IntAct co-IP 验证 EED 互作。UniProt 还记录与 SUV39H1/2、KDM1A、RCOR3 等染色质修饰酶的互作。

### 4. 总体评价
PHF19 是 PRC2 复合体的关键辅助因子，介导 H3K36me3 识别到 H3K27me3 沉积的组蛋白修饰转换。核定位有 UniProt curated 支持但缺 HPA IF 验证。结构域覆盖良好（PHD + Tudor），PPI 网络以 PRC2 为核心极为稳固。研究热度中等偏高 (strict=62)，在 Polycomb/染色质调控领域 niche 明确。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T6S3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T6S3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHF19
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119403-PHF19

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PHF19/PHF19-PAE.png]]

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PHF19/PHF19-PAE.png]]
