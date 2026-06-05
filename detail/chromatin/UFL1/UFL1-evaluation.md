---
type: protein-evaluation
gene: "UFL1"
date: 2026-06-01
tags: [protein-scout, chromatin, evaluation]
status: scored
---

## UFL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | UFL1 / KIAA0776, MAXER, NLBP, RCAD |
| 蛋白全名 | E3 UFM1-protein ligase 1 |
| 蛋白大小 | 794 aa / 89.6 kDa |
| UniProt ID | O94874 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | UniProt ER membrane (ECO:0000269 ×7) + Cytosol + Nucleus + Chromosome (ECO:0000269)；GO-CC nucleus IDA, site of DSB IDA；HPA 无 IF/无定位 |
| 蛋白大小 | 4/10 | ×1 | 4.0 | 794 aa, 89.6 kDa，大型 E3 连接酶 |
| 研究新颖性 | 2/10 | ×5 | 10.0 | PubMed strict=92, broad=140 |
| 三维结构 | 7/10 | ×3 | 21.0 | AlphaFold pLDDT 80.5 (pct>90: 38.8%)；PDB 9 个结构 (X-ray+EM, 全蛋白 Cryo-EM 2.20A) |

![[UFL1-PAE.png]]
| 调控结构域 | 7/10 | ×2 | 14.0 | E3 UFM1 ligase (IPR018611, PF09743)；ufmylation 通路核心酶，调控核糖体回收、ER-phagy、DNA 损伤应答 |
| PPI 网络 | 5/10 | ×3 | 15.0 | STRING: CDK5RAP3 (0.999 exp 0.856), DDRGK1 (0.996), UFM1 (0.975)；IntAct 部分 (多为 fly Y2H)；UniProt 3 条 |
| **加权总分** | | | **80/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **43.7/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Endoplasmic reticulum membrane (ECO:0000269 ×7, primary location)；Cytoplasm, cytosol (ECO:0000269)；Nucleus (ECO:0000269)；Chromosome (ECO:0000269) | 中 (核定位仅为次要定位) |
| GO-CC | endoplasmic reticulum (IDA:HPA), endoplasmic reticulum membrane (IDA), nucleus (IDA:UniProtKB), site of double-strand break (IDA:UniProtKB), cytoplasm (IDA), cytosol, mitochondrial outer membrane | 中 |
| Protein Atlas (IF) | HPA 无 IF 数据，无 ensembl ID，无 subcellular location 注释 | 未确认 |

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 — HPA 搜索 UFL1 仅返回 IHC/RNA 相关图像，无 IF 数据且无定位注释（page_found_no_if_image_detected）。HPA 数据中 ensembl=null, subcellular_location=[]。

**结论**: UFL1 主要是内质网膜蛋白（UniProt 7 条实验证据），核/染色质定位是次要或条件性定位（DNA 损伤时招募至 DSB 位点）。核定位特异性和置信度均较低。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-O94874-F1 |
| 平均 pLDDT | 80.5 |
| pLDDT >90 | 38.8% |
| pLDDT 70-90 | 42.8% |
| pLDDT <50 | 12.0% |
| PDB | 9 个 (8B9X/X-ray 3.07A, 8C0D/X-ray 2.56A, 8OHD/EM 3.10A, 8OJ0/EM 3.30A, 8OJ5/EM 2.90A, 8OJ8/EM 3.30A, 8QFC/EM 3.20A, 8QFD/EM 2.20A, 9GY4/EM 3.00A)，多个为全蛋白 Cryo-EM 结构 |
| InterPro | IPR018611 (UFL1), IPR056761, IPR056580, IPR056579 |
| Pfam | PF09743 (DUF2042/UFL1), PF23659, PF25041, PF25870 |

**AlphaFold PAE 状态**: PAE 已下载。pLDDT 良好 (80.5, 81.6% >70)，12.0% <50。PDB 已有多个 Cryo-EM 全蛋白结构（最高 2.20A），与 DDRGK1/CDK5RAP3/UFC1 复合体结构解析充分。

![[UFL1-PAE.png]]

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 92 |
| PubMed broad | 140 |
| 别名 | KIAA0776, MAXER, NLBP, RCAD（未用于 scoring） |

关键文献：UFL1 是 UFM1 修饰系统（ufmylation）的核心 E3 连接酶，参与核糖体 60S 亚基回收（RPL26 ufmylation）、ER-phagy (CYB5R3)、DNA 损伤应答（histone H4 和 MRE11 ufmylation）和免疫调节 (PD-1/PD-L1)。代表性文献：PMID:38383785 (Nature, 60S ribosome recycling), PMID:36543799 (Nature Communications, ER-phagy via CYB5R3), PMID:37945409 (Trends Biochem Sci, ufmylation review)。文献量较高（strict=92），ufmylation 领域近年爆发式增长。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| CDK5RAP3 | STRING+UniProt | 0.999 (exp 0.856), 13 exp | Substrate adaptor, UFM1 ligase complex |
| DDRGK1 | STRING+UniProt | 0.996 (exp 0.841), 10 exp | Substrate adaptor, ER membrane anchor |
| UFM1 | STRING | 0.975 (exp 0.492) | Ubiquitin-like modifier |
| UFC1 | STRING+UniProt | 0.96 (exp 0.696), 9 exp | E2 conjugating enzyme |
| UBA5 | STRING | 0.944 (textmining 0.933) | E1 activating enzyme |
| UFSP2 | STRING | 0.879 (textmining 0.858) | Deufmylase |
| RPL26 | STRING | 0.572 (exp 0.164) | 60S ribosomal substrate |

PPI 网络以 UFM1 通路为核心，CDK5RAP3-DDRGK1-UFL1 三聚体复合物实验互作高置信（exp 0.856/0.841），UniProt 实验记录丰富。IntAct 人源互作较少（多为 Drosophila Y2H），但 STRING 和 UniProt 数据充分支持网络完整性。

### 4. 总体评价
UFL1 是 ufmylation 通路的核心 E3 连接酶，在 ER-phagy、核糖体回收和 DNA 损伤应答中发挥关键功能。优势在于 PDB 结构解析充分（9 个结构，包括全蛋白 Cryo-EM），PPI 网络以高置信度实验互作为主（CDK5RAP3-DDRGK1-UFL1 复合体）。主要不足：文献量高 (PM=92)，核定位仅为条件性/次要定位（主要是 ER 膜蛋白），HPA 无 IF 数据，核定位特异性低。考虑到其 DNA 损伤时被招募至染色质/DSB 的功能，归类为 chromatin 候选但信心较低。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94874
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94874
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UFL1
- Protein Atlas: https://www.proteinatlas.org/search/UFL1

![[Projects/TEreg-finding/protein-interested/detail/chromatin/UFL1/UFL1-PAE.png]]

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/UFL1/UFL1-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94874-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
