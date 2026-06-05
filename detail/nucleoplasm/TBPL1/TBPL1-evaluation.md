---
type: protein-evaluation
gene: "TBPL1"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## TBPL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | TBPL1 / TLF, TLP, TLP21, TRF2, TRP |
| 蛋白全名 | TATA box-binding protein-like 1 |
| 蛋白大小 | 186 aa / 20.9 kDa |
| UniProt ID | P62380 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24.0 | UniProt Cytoplasm+Nucleus (ECO:0000250)；GO-CC male germ cell nucleus IEA, TFIIA complex IEA；HPA Supported, Nucleoplasm (main) + Nucleoli |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 186 aa, 20.9 kDa，小型 TBP 家族转录因子 |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=16, broad=39 |
| 三维结构 | 7/10 | ×3 | 21.0 | AlphaFold pLDDT 95.0 (pct>90: 93.5%)；无 PDB 结构 |

![[TBPL1-PAE.png]]
| 调控结构域 | 7/10 | ×2 | 14.0 | TBP domain (PF00352, IPR000814, IPR012295)；TATA box 结合蛋白同源域，转录因子核心域 |
| PPI 网络 | 7/10 | ×3 | 21.0 | STRING: GTF2B (0.996 exp 0.81), GTF2A1 (0.993 exp 0.931), GTF2A2 (0.976 exp 0.936)；IntAct 15 条；UniProt 8 条 |
| **加权总分** | | | **139/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **76.0/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Cytoplasm (ECO:0000250), Nucleus (ECO:0000250) | 低 (序列相似性推断) |
| GO-CC | cytoplasm (IEA:UniProtKB-SubCell), male germ cell nucleus (IEA:Ensembl), transcription factor TFIIA complex (IEA:Ensembl) | 低-中 |
| Protein Atlas (IF) | HPA Supported, Nucleoplasm (main) + Nucleoli (additional) | 中 (HPA 确认) |

**HPA IF 状态**: HPA IF 图像已本地嵌入。

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TBPL1/IF_images/TBPL1_IF_1510_H9_1_red_green.jpg]]。核定位基于HPA localization/reliability + UniProt + GO-CC。


**结论**: TBPL1 核定位主要依赖 HPA（Supported），UniProt/GO-CC 证据较弱（均为同源推断或电子注释）。但作为 TBP 家族转录因子，核定位在功能逻辑上高度合理。HPA 支持的 Nucleoplasm + Nucleoli 定位与已知的 ribosomal protein gene 转录调控功能一致。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-P62380-F1 |
| 平均 pLDDT | 95.0 |
| pLDDT >90 | 93.5% |
| pLDDT 70-90 | 2.2% |
| pLDDT <50 | 1.6% |
| PDB | 无 |
| InterPro | IPR000814 (TBP), IPR015445 (TBP-like), IPR012295 (TBP domain superfamily) |
| Pfam | PF00352 (TBP) |

**AlphaFold PAE 状态**: PAE 已下载。pLDDT 极高 (95.0, 93.5% >90)，仅 1.6% <50，结构预测极为可靠。TBPL1 为小型蛋白 (186 aa)，虽无 PDB 实验结构，但 AlphaFold 预测置信度足以支持结构相关研究。

![[TBPL1-PAE.png]]

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 16 |
| PubMed broad | 39 |
| 别名 | TLF, TLP, TLP21, TRF2, TRP（未用于 scoring） |

关键文献：TBPL1 是 TATA box-binding protein (TBP) 家族成员，通过识别 TCT 启动子元件介导 ribosomal protein genes 的转录（不结合 TATA box）。功能区别于经典 TBP，但在转录调控中角色独立且重要。代表性文献：PMID:35122989 (c-MYC 通过 miR-9-5p 调控 TBPL1 参与 IPF), PMID:35597524 (TBP 家族在转录调控中的角色综述), PMID:19515240 (TIPT2 和 geminin 与 basal transcription factors 协同)。文献量极低（strict=16），属于高度新颖靶标。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| GTF2B | STRING | 0.996 (exp 0.81, database 0.9) | Basal transcription factor |
| GTF2A1 | STRING+IntAct+UniProt | 0.993 (exp 0.931), Co-IP, 8 exp | TFIIA complex |
| GTF2A2 | STRING+IntAct+UniProt | 0.976 (exp 0.936), Co-IP, 4 exp | TFIIA complex |
| TBP | STRING | 0.941 (exp 0.277, database 0.9) | TBP family |
| TBPL2 | STRING | 0.938 (exp 0.277, database 0.9) | TBP family |
| TAF2 | STRING | 0.881 (exp 0.743) | TFIID complex |
| TAF12 | STRING | 0.868 (exp 0.743) | TFIID complex |
| BTAF1 | STRING | 0.87 (exp 0.749) | TBP regulator |

PPI 网络以基础转录机器（GTF2B/GTF2A1/GTF2A2/TBP/TAFs）为核心，实验验证丰富且多样化（Co-IP, Y2H, protein array, cross-linking）。GTF2A1-GTF2A2 的 Co-IP 和 Y2H 验证极为充分（exp 0.931/0.936）。IntAct 和 UniProt 记录相互独立验证相同互作伙伴（GTF2A1, GTF2A2），提供 PPI 网络的三源互证。

### 4. 总体评价
TBPL1 是一个文献量极低（strict=16）、结构预测可靠（pLDDT 95.0）、蛋白小型（20.9 kDa）的转录因子候选。作为 TBP 家族中独立于 TATA box 的 ribosomal protein gene 特异转录因子，其功能新颖且有区分度。优势：极高结构预测置信度、PPI 网络丰富且实验验证充分（GTF2A1/GTF2B 等）。主要不足：无 PDB 实验结构，核定位 UniProt/GO-CC 证据偏弱（依赖同源推断），但 HPA Supported 定位 + 功能逻辑强烈支持核定位。综合评分在 nucleoplasm 类别中具有竞争力。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P62380
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P62380
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBPL1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000028839-TBPL1

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TBPL1/TBPL1-PAE.png]]

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TBPL1/TBPL1-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P62380-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
