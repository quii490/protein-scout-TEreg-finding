---
type: protein-evaluation
gene: "PIWIL4"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## PIWIL4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PIWIL4 / HIWI2, PIWI |
| 蛋白全名 | Piwi-like protein 4 |
| 蛋白大小 | 852 aa / 96.6 kDa |
| UniProt ID | Q7Z3Z4 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28.0 | UniProt Nucleus; Cytoplasm, HPA Nucleoplasm + Mitochondria |
| 蛋白大小 | 6/10 | x1 | 6.0 | 852 aa, 96.6 kDa，偏大 |
| 研究新颖性 | 2/10 | x5 | 10.0 | PubMed strict=91 (≤100 区间) |
| 三维结构 | 7/10 | x3 | 21.0 | AlphaFold pLDDT 85.2；无 PDB 实验结构；AF 预测质量高 |
| 调控结构域 | 8/10 | x2 | 16.0 | PIWI + PAZ 双域，piRNA 通路核心，参与转座子沉默和 H3K9 甲基化 |
| PPI 网络 | 7/10 | x3 | 21.0 | STRING TDRD9 0.995, TDRKH 0.980, DICER1 0.956；IntAct 15+ 互作 |
| **加权总分** | | | **102/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **55.7/100**** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt Subcellular Location | Nucleus (ECO:0000269 x2); Cytoplasm (ECO:0000269 x3) | 高（实验证据） |
| GO-CC | nucleoplasm (IDA:HPA), nucleus (IDA:UniProtKB), cytoplasm (IDA:UniProtKB), P granule (ISS), piP-body (ISS) | 高 |
| HPA IF | Nucleoplasm + Mitochondria (Supported 可靠性) | 中-高 |
| Literature | PIWIL4 在核内通过 piRNA 通路介导转座子沉默和 DNA 甲基化；核质分布为主 | 强 |

**HPA IF 状态**: IF available -- HPA 可靠性 Supported，定位 Nucleoplasm + Mitochondria。

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PIWIL4/IF_images/PIWIL4_IF_red_green.jpg]]

**结论**: PIWIL4 在核和细胞质双重定位，核质为主导。UniProt 和 GO 均有实验证据支持核定位。HPA IF 确认为 Nucleoplasm（附加 Mitochondria）。在 piRNA 通路中负责核内转座子沉默和 DNA 甲基化。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q7Z3Z4-F1 |
| 平均 pLDDT | 85.2 |
| pLDDT >90 | 64.6% |
| pLDDT 70-90 | 23.2% |
| pLDDT <50 | 9.7% |
| PDB | 无实验结构 |

AlphaFold 预测质量高（pLDDT 85.2），>90 区域占 64.6%，PIWI 和 PAZ 域折叠良好。无 PDB 实验结构。


| InterPro | Pfam |
|---|---|
| IPR003100 (PAZ domain), IPR036085 (PAZ superfamily), IPR003165 (Piwi domain), IPR012337 (RNase H-like), IPR036397 (RNase H superfamily) | PF02170 (Piwi), PF02171 (PAZ), PF23278 |

**染色质调控潜力**: PIWIL4 直接参与 piRNA 介导的 DNA 甲基化和 H3K9 甲基化，通过 piRNA 靶向转座子基因组位点，是表观遗传沉默的核心因子。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 91 |
| PubMed broad | 159 |
| 别名 | HIWI2, PIWI（未用于 scoring） |

关键文献：
- PMID:17544373: PIWIL4 通过 piRNA 通路诱导 H3K9 甲基化，参与染色质修饰
- PMID:39294378: "Two-factor authentication underpins the precision of the piRNA pathway." (Nature, 2024) -- piRNA 通路机制
- PMID:37146239: "A noncanonical enzymatic function of PIWIL4 maintains genomic integrity and leukemic growth in AML." (Blood, 2023) -- AML 中的非典型酶活功能
- PMID:30174296: "Single-Cell RNA Sequencing Analysis Reveals Sequential Cell Fate Transition during Human Spermatogenesis." (Cell Stem Cell, 2018)

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| TDRD9 | STRING | 0.995 (exp 0.188, db 0.8) | piRNA 通路 Tudor 蛋白 |
| TDRKH | STRING | 0.980 (exp 0.269, db 0.8) | piRNA 生物合成 |
| TDRD1 | STRING | 0.957 (exp 0.451, db 0.5) | piRNA 通路 |
| MAEL | STRING | 0.957 (exp 0.089, db 0.8) | piRNA 通路 |
| DICER1 | STRING | 0.956 (exp 0.501) | miRNA/siRNA 加工 |
| HSP90AA1 | STRING | 0.889 (exp 0.194) | 蛋白折叠伴侣 |
| HSP90AB1 | IntAct | luminescence based (PMID:25036637) | 实验验证 |
| H1-5 | IntAct | cross-linking (PMID:30021884) | 接头组蛋白 |
| BEND3 | IntAct | coIP (PMID:33961781) | 染色质调控 |

PIWIL4 的 PPI 网络以 piRNA 通路为核心，TDRD9/TDRKH/TDRD1 构成 Tudor 蛋白家族互作网。DICER1 连接至 small RNA 加工通路。HSP90AA1/HSP90AB1 复合成伴侣机制与 PIWI 蛋白折叠相关。H1-5 和 BEND3 的互作提示染色质层面功能。

### 4. 总体评价
PIWIL4 是 piRNA 通路核内效应器，直接参与转座子沉默和表观遗传调控。主要限制是 PubMed 91 篇（新颖性 2/10），研究热度中等偏高。优势包括：核定位明确、PIWI+PAZ 双域完整、AlphaFold 结构预测质量高、PPI 网络以 piRNA 通路为核心且有多条实验验证互作。但其 852 aa 偏大，无 PDB 实验结构。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z3Z4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z3Z4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PIWIL4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134627-PIWIL4

HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z3Z4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
