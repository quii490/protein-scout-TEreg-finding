---
type: protein-evaluation
gene: "HEYL"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## HEYL 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | HEYL / BHLHB33, HRT3 |
| 蛋白全名 | Hairy/enhancer-of-split related with YRPW motif-like protein |
| 蛋白大小 | 328 aa / 35.1 kDa |
| UniProt ID | Q9NQ87 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | UniProt: Nucleus; GO: nucleus IDA, nucleoplasm TAS; HPA: Nucleoli fibrillar center Approved |
| 蛋白大小 | 8/10 | ×1 | 8.0 | 328 aa, 35.1 kDa |
| 研究新颖性 | 2/10 | ×5 | 10.0 | PubMed strict=90, broad=705 |
| 三维结构 | 6/10 | ×3 | 18.0 | AlphaFold pLDDT 65.0; 34.1% <50; 无 PDB |

| 调控结构域 | 8/10 | ×2 | 16.0 | bHLH + Orange domain; Notch 信号下游转录抑制因子; 心血管发育关键 |
| PPI 网络 | 7/10 | ×3 | 21.0 | UniProt MDFI (7 exp), RBPMS (4 exp); IntAct Hand1/2, ATXN1, BANP 等丰富 |
| **加权总分** | | | **105/180**** | |
| 互证加分 | | | +1.0 | Notch 信号通路 TF; MDFI 强互作多源确认 |
| **归一化总分 (÷1.83)** | | | **57.4/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus (ECO:0000255) | Predicted |
| GO-CC | chromatin (ISA:NTNU_SB); cytoplasm (ISS:UniProtKB); nucleoplasm (TAS:Reactome); nucleus (IDA:UniProtKB) | Mixed (IDA for nucleus) |
| Protein Atlas (IF) | Nucleoli fibrillar center (Approved) | Approved |

**HPA IF 状态**: IF available (Approved reliability) — HPA 定位为 Nucleoli fibrillar center Approved，与 UniProt Nucleus 和 GO nucleus IDA 互证。HEYL 是 Notch 信号通路的下游转录抑制因子，结合 E-box 序列 5'-CACGTG-3'，抑制 GATA4/GATA6 转录活性。核定位高度可信。

#### 3.2 结构与结构域
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q9NQ87-F1 |
| 平均 pLDDT | 65.0 |
| pLDDT >90 | 23.2% |
| pLDDT 70-90 | 12.5% |
| pLDDT 50-70 | 30.2% |
| pLDDT <50 | 34.1% |
| PDB | 无 |
| InterPro | IPR011598 (bHLH), IPR050370, IPR036638 (Orange), IPR003650 |
| Pfam | PF07527 (Hairy_orange), PF00010 (HLH) |

**AlphaFold PAE 状态**: PAE 已下载，见上图。pLDDT 中等（65.0），34% 残基低于 50。bHLH 和 Orange 结构域区域可能是较可靠折叠部分，其余区域可能为转录因子常见的 IDR。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 90 |
| PubMed broad | 705 |
| 别名 | BHLHB33, HRT3（未用于 scoring） |

研究热度较高。关键文献涵盖 Notch 通路突变体表达分析（PMID:11044625）、神经祖细胞分化（PMID:21259317）、乳腺肿瘤血管生成（PMID:33520697）、结直肠癌预后（PMID:41062962）和 Notch 信号基因网络。broad 高达 705 说明该基因名在文献中被广泛提及但很多非 primary 研究，strict=90 反映真实研究量。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| MDFI | UniProt | 7 experiments | Transcription inhibitor, strong |
| MDFI | IntAct | validated Y2H (PMID:32296183) | Transcription inhibitor |
| RBPMS | UniProt | 4 experiments | RNA-binding protein |
| RBPMS | IntAct | two hybrid pooling (PMID:16189514) | RNA-binding protein |
| BANP | UniProt | 3 experiments | BTG3-associated nuclear protein |
| BANP | IntAct | validated Y2H (PMID:32296183) | Nuclear protein |
| Hand1 | IntAct | pull down (PMID:10924525) | Cardiac TF |
| Hand2 | IntAct | pull down (PMID:10924525) | Cardiac TF |
| ATXN1 | IntAct | two hybrid (PMID:23275563) | Ataxin-1 |
| HTT | IntAct | two hybrid (PMID:23275563) | Huntingtin |
| FNTA | IntAct | anti tag coIP (PMID:28514442) | Farnesyltransferase |
| PGGT1B | IntAct | anti tag coIP (PMID:28514442) | Geranylgeranyltransferase |
| GRAP2 | IntAct | anti tag coIP (PMID:33961781) | GRB2-related adaptor |
| — | STRING | 获取失败 (SSL error) | — |

MDFI 是最强互作（7 experiments in UniProt + validated Y2H in IntAct），RBPMS 和 BANP 也经多源确认。Hand1/2 的 pull down 互作支持其在心血管发育中的转录调控功能。缺少 STRING 数据是一大遗憾。

### 4. 总体评价
HEYL 是 Notch 信号通路的核心转录抑制因子，核定位强（GO nucleus IDA + HPA Approved nucleoli）、bHLH-Orange 结构域支持转录调控功能、PPI 网络指向 Hand1/2、MDFI、BANP 等核蛋白。主要劣势是研究热度较高（PM=90），但鉴于其 Notch 效应子的独特位置和丰富的 PPI 网络，仍值得作为中等优先级核质候选保留。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQ87
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQ87
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HEYL
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163909-HEYL

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HEYL/IF_images/Rh30_1.jpg]]

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HEYL/IF_images/AF22_1.jpg]]


HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQ87-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
