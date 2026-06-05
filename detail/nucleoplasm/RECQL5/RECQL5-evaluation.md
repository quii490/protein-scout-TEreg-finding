---
type: protein-evaluation
gene: "RECQL5"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## RECQL5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | RECQL5 / RECQ5 |
| 蛋白全名 | ATP-dependent DNA helicase Q5 |
| 蛋白大小 | 991 aa / 108.9 kDa |
| UniProt ID | O94762 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | UniProt nucleoplasm (ECO:0000269 x3); HPA Nucleoplasm (main); GO nucleoplasm (IDA:HPA) |
| 蛋白大小 | 2/10 | x1 | 2.0 | 991 aa, 108.9 kDa，大蛋白 |
| 研究新颖性 | 4/10 | x5 | 20.0 | PubMed strict=70 |
| 三维结构 | 6/10 | x3 | 18.0 | PDB 25个结构 (含 EM 全长 9EI1-9EI4); AF pLDDT 70.1 |

![[RECQL5-PAE.png]]
| 调控结构域 | 5/10 | x2 | 10.0 | DEAD/DEAH helicase + helicase C-terminal + HRDC domain; RecQ 家族 DNA 解旋酶 |
| PPI 网络 | 8/10 | x3 | 24.0 | STRING FANCM (0.991 exp), RAD51 (0.947 exp), POLR2A (0.886 exp); 核心 DNA 修复+转录 |
| **加权总分** | | | **110/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **60.1/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleoplasm (ECO:0000269 x3), Nucleus (ECO:0000269), Cytoplasm | 多源实验证据 |
| GO-CC | nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB), chromosome, replication fork, transcription preinitiation complex | 多源高置信度 |
| HPA (IF) | Nucleoplasm (main), Cytosol | Supported, 无IF原图 |
| 功能 | DNA helicase, DNA replication/repair/transcription | 核心核功能 |

**HPA IF 状态**: HPA 分类为 Nucleoplasm (main) + Cytosol, Supported 级可信度, 但无 IF 原图。核定位由 UniProt + GO + HPA 三源交叉验证。

**结论**: RECQL5 核定位证据极为坚实，UniProt 实验证据标注 3 次 nucleoplasm + HPA IDA nucleoplasm + 功能即为核内 DNA 代谢。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-O94762-F1 |
| 平均 pLDDT | 70.1 |
| pLDDT >90 | 38.3% |
| pLDDT <50 | 34.3% |
| PDB | 25 个结构：X-ray (helicase domain 11-453/526) + EM (全长 1-991, 包括 8QQ2, 8QW8-9, 8RL5-9RLA, 9EI1-4) |
| InterPro | IPR011545 (DEAD/DEAH helicase), IPR001650 (Helicase C), IPR004589 (RecQ), IPR010716 (HRDC) |
| Pfam | PF00270 (DEAD), PF00271 (Helicase C), PF06959 (HRDC), PF16124 (RecQ), PF08236 (HRDC) |

结构数据丰富 — 包含 25 个 PDB 结构（helicase domain 晶体 + 全长 cryo-EM），远超大多数候选蛋白。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 70 |
| PubMed broad | 157 |
| 别名 | RECQ5（未用于 scoring） |

关键文献：PMID:39284827 (USP50 suppresses RecQ helicases, 2024), PMID:38530355 (RNF4/Myc, 2024), PMID:26586793 (breast cancer prognostic, 2016), PMID:40540553 (senataxin/DNA-PKcs, NHEJ, 2025), PMID:38796829 (transcription-associated genome instability, 2024). 文献持续产出，以 DNA 修复/基因组稳定性为核心主题。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| FANCM | STRING | 0.991 (exp 0.967) | Fanconi anemia, DNA repair |
| RAD51 | STRING | 0.947 (exp 0.711) | Homologous recombination |
| TOP3A | STRING | 0.946 (exp 0.641) | DNA topology |
| FBH1 | STRING | 0.938 (exp 0.608) | DNA helicase, replication stress |
| RPRD1B | STRING | 0.930 (exp 0.836) | RNA Pol II regulation |
| POLR2A | STRING+UniProt | 0.886 (exp 0.836) / 8 exp | RNA Pol II largest subunit |
| POLR2G/D/M | STRING | 0.84-0.89 (exp 0.82-0.84) | RNA Pol II subunits |
| MUS81 | STRING | 0.888 (exp 0.576) | DNA repair endonuclease |
| TP53BP1 | STRING | 0.858 (exp 0.706) | DNA damage response |
| DNA2 | STRING | 0.885 (exp 0.317) | DNA replication/repair |

PPI 网络极为丰富：以 RNA Pol II 全酶（POLR2A/G/D/M 强实验互作）和 DNA 修复（FANCM/RAD51/TOP3A/MUS81）为双核心。UniProt 记录 POLR2A 8 个实验互作，RECQL5 的直接功能角色（转录延伸中与 Pol II 结合抑制基因组不稳定性）已有明确机制。

### 4. 总体评价
RECQL5 为 RecQ 家族 DNA 解旋酶，核定位证据坚实（三源一致），结构数据极其丰富（25 个 PDB，含全长 cryo-EM），PPI 网络在 DNA 修复+转录领域广泛而深入。主要限制为 PubMed=70 文献量偏高（仍可接受）和蛋白较大（991 aa）。作为 RNA Pol II 转录延伸的直接结合伙伴和基因组稳定性关键因子，在 TE 调控与转录偶联的 DNA 损伤修复方面有潜在的交叉角色，值得进一步评估 TE 调控相关的可能功能。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94762
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94762
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RECQL5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108469-RECQL5

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RECQL5/RECQL5-PAE.png]]

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RECQL5/IF_images/RECQL5_IF_326_F5_1_red_green.jpg]]

HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/RECQL5/RECQL5-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94762-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
