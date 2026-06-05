---
type: protein-evaluation
gene: "GEMIN6"
date: 2026-06-02
tags: [protein-scout, nuclear-body, evaluation]
status: scored
---

## GEMIN6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | GEMIN6 / — |
| 蛋白全名 | Gem-associated protein 6 |
| 蛋白大小 | 167 aa / 18.8 kDa |
| UniProt ID | Q8WXD5 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | UniProt: Nucleoplasm + Gem + Cytoplasm; GO-CC: nuclear body (IDA), nucleoplasm (IDA), Gemini of Cajal bodies (IDA); HPA "Supported": Nucleoplasm + Nuclear bodies |
| 蛋白大小 | 8/10 | ×1 | 8.0 | 167 aa, 18.8 kDa, 小型蛋白 |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=18, ≤20 |
| 三维结构 | 7/10 | ×3 | 21.0 | AlphaFold mean pLDDT 86.7; 2 PDB (X-ray, 1.52-2.00A) |

![[GEMIN6-PAE.png]]
| 调控结构域 | 4/10 | ×2 | 8.0 | IPR047574/5, IPR009422, PF06372+PF20417 — Sm 样结构域; GEMIN6/7 heterodimer 结构已知 |
| PPI 网络 | 7/10 | ×3 | 21.0 | SMN complex 核心成员 (GEMIN7/2/5/8, SMN1/DDX20 ≥0.989); IntAct 含 GEMIN7/SMN1/SNRPE 多 co-IP |
| **加权总分** | | | **140/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **76.5/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus, nucleoplasm (ECO:0000269); Nucleus, gem (ECO:0000269); Cytoplasm (ECO:0000269) | 高（实验证据） |
| GO-CC | nuclear body (IDA:UniProtKB), nucleoplasm (IDA:UniProtKB), Gemini of Cajal bodies (IDA), SMN complex (IDA), SMN-Sm protein complex (IDA), cytoplasm/cytosol (IDA) | 高（多 IDA） |
| Protein Atlas (IF) | HPA "Supported": Nucleoplasm + Nuclear bodies | 高（IF 验证） |

**HPA IF 状态**: IF images available (HPA reliability "Supported") — HPA 确认 GEMIN6 定位于 Nucleoplasm 和 Nuclear bodies。IF 图像存在于 proteinatlas.org（三种抗体验证）。

**结论**: GEMIN6 核定位证据极为充分。UniProt + GO-CC + HPA IF 三源一致确认 nucleoplasm/nuclear body/Gem 定位。GO-CC 多处 IDA 实验级别证据，HPA 抗体 validated。作为 SMN 复合物核心成员，定位于 Gemini of Cajal bodies（nuclear body 子结构）和 nucleoplasm。是核定位证据最强的一个候选。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q8WXD5-F1 |
| 平均 pLDDT | 86.7 |
| pLDDT >90 | 38.9% |
| pLDDT 70-90 | 51.5% |
| PDB | 2 个结构（X-ray 1.52-2.00A），覆盖 N 端 GEMIN6/7 heterodimer 结构域 |
| InterPro | IPR047574, IPR009422, IPR046856, IPR046857, IPR047575 |
| Pfam | PF06372 (Gemin6), PF20417 (Gemin6_C) |

**AlphaFold PAE 状态**: PAE 已下载，模型置信度良好（mean pLDDT 86.7）。GEMIN6/7 heterodimer 结构已通过 X-ray 解析（PDB:1Y96, 7BBL），结构生物学基础稳固。
![[GEMIN6-PAE.png]]

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 18 |
| PubMed broad | 25 |
| 别名 | 无 |

关键文献：GEMIN6 文献量低（strict=18）。核心文献包括 GEMIN6/7 heterodimer 结构鉴定（PMID:15939020, 2.00A X-ray, Sm-like fold）、GEMIN6/7/8 在 SMN complex 中的组装架构（PMID:17023415, 12065586）、GEMIN6 在肺腺癌中的预后意义（PMID:36284636）、以及 LGI3-GEMIN6/AURKB 轴促进 TFE3 重排肾细胞癌进展（PMID:40849584）。功能核心围绕 SMN 复合物介导的 snRNP 组装（spliceosome biogenesis）。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| GEMIN7 | STRING + IntAct | 0.999 (exp 0.991; two hybrid + co-IP) | Heterodimer partner |
| GEMIN8 | STRING | 0.999 (exp 0.980) | SMN complex |
| STRAP | STRING | 0.999 (exp 0.838) | SMN complex |
| GEMIN5 | STRING | 0.999 (exp 0.605) | SMN complex snRNA binding |
| GEMIN2 | STRING + IntAct | 0.999 (exp 0.836; co-IP) | SMN complex scaffold |
| DDX20 | STRING | 0.999 (exp 0.837) | SMN complex |
| GEMIN4 | STRING | 0.998 (exp 0.823) | SMN complex |
| SMN1 | STRING + IntAct | 0.990 (exp 0.873; co-IP) | SMN core |
| SNRPE | STRING + IntAct | 0.989 (exp 0.678; co-IP) | Sm core protein |
| SNRPF | STRING | 0.978 (exp 0.763) | Sm core protein |

PPI 网络强大且以 SMN 复合物为中心，实验验证充分（co-IP, pull-down, two hybrid）。IntAct 包含 GEMIN7 双杂交 (PMID:16189514)、SMN1 co-IP (PMID:19928837)、SNRPE/GEMIN2/SNRNP70 等 co-IP (PMID:28514442) 等多条验证。UniProt 记录 GEMIN7 (23 experiments)、STRAP (6)、SNRPE (6)、SNRPF (6) 等强互作。

### 4. 总体评价
GEMIN6 是本批次评价很高的候选（76.5/100）。核心优势：极低文献量（PM=18）、三源核定位确认（UniProt/GO-CC/HPA IF 一致）、高实验验证的 SMN complex PPI 网络、结构已知（GEMIN6/7 heterodimer 高分辨晶体结构）。作为 nuclear-body 类别候选，GEMIN6 是 SMN 复合物的核心成员，定位于 Gemini of Cajal bodies，功能涉及剪接体 snRNP 组装。主要局限：结构域功能深度有限、蛋白仅 167 aa。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXD5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXD5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GEMIN6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152147-GEMIN6（IF: Supported）

![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/GEMIN6/IF_images/1443_G3_2_blue_red_green.jpg]]

![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/GEMIN6/IF_images/1443_G3_1_blue_red_green.jpg]]

![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/GEMIN6/IF_images/PC-3_1.jpg]]

![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/GEMIN6/GEMIN6-PAE.png]]

HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/GEMIN6/GEMIN6-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WXD5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
