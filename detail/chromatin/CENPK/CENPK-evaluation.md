---
type: protein-evaluation
gene: "CENPK"
date: 2026-06-02
tags: [protein-scout, chromatin, evaluation]
status: scored
---

## CENPK 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | CENPK / ICEN37 |
| 蛋白全名 | Centromere protein K |
| 蛋白大小 | 269 aa / 31.7 kDa |
| UniProt ID | Q9BS16 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | UniProt: Nucleus + Centromere/Kinetochore; GO-CC: nucleoplasm, inner kinetochore; HPA 无 IF |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 269 aa, 31.7 kDa, 中等偏小 |
| 研究新颖性 | 6/10 | ×5 | 30.0 | PubMed strict=50, ≤60 |
| 三维结构 | 7/10 | ×3 | 21.0 | AlphaFold mean pLDDT 81.0; 9 PDB (X-ray + EM, 全蛋白覆盖) |

![[CENPK-PAE.png]]
| 调控结构域 | 3/10 | ×2 | 6.0 | IPR020993, PF11802 — CENP-K domain; 结构域简单 |
| PPI 网络 | 7/10 | ×3 | 21.0 | ComplexPortal 动粒核心成员 (CENPH/CENPI/CENPM/N/O/P/Q/U 等 ≥0.996); IntAct 多 co-IP 确认 |
| **加权总分** | | | **112/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **61.2/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore | 高（文献注释） |
| GO-CC | nucleoplasm (TAS:Reactome), nucleus (NAS:ComplexPortal), inner kinetochore (IPI:ComplexPortal), cytosol (TAS) | 高 |
| Protein Atlas (IF) | HPA 无 IF 图像（no_image_detected） | 未确认 |

**HPA IF 状态**: no_image_detected — HPA 未检测到可用 IF 图像。核定位基于 UniProt + GO-CC。

**结论**: CENPK 核定位证据充分。作为 CENPA-CAD 复合物成员，定位在着丝粒/动粒，GO-CC 确认 nucleoplasm 和 inner kinetochore。虽无 HPA IF 直接验证，但 UniProt 多来源注释 + GO-CC TAS/IPI 证据链完整。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q9BS16-F1 |
| 平均 pLDDT | 81.0 |
| pLDDT >90 | 36.1% |
| pLDDT 70-90 | 43.5% |
| PDB | 9 个结构（X-ray 2.49A 部分+EM 3.20-12.00A 全长），覆盖 CENP-T/W/S/X 及 CCAN 复合物 |
| InterPro | IPR020993 |
| Pfam | PF11802 |

**AlphaFold PAE 状态**: PAE 已下载，结构整体置信度中等（mean pLDDT 81.0），N 末端区域置信度较低。
![[CENPK-PAE.png]]

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 50 |
| PubMed broad | 61 |
| 别名 | ICEN37（未用于 scoring） |

关键文献方向：CENPK 在多种癌症（宫颈癌、前列腺癌、甲状腺癌、胃癌）中作为预后标志物和增殖调控因子被研究（PMID:35418160, 35706799, 33904381, 35715658）。Pan-cancer 分析（PMID:35035680）系统评估其临床意义。功能层面作为着丝粒蛋白参与染色体分离，与 XRCC5 互作促进胃癌增殖迁移。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| CENPH | STRING + IntAct | 0.999 (exp 0.979, co-IP) | Core kinetochore |
| CENPI | STRING + IntAct | 0.999 (exp 0.969, co-IP) | Core kinetochore |
| CENPM | STRING | 0.999 (exp 0.968) | Core kinetochore |
| CENPO | STRING + IntAct | 0.999 (exp 0.941, co-IP) | Core kinetochore |
| CENPQ | STRING + IntAct | 0.999 (exp 0.899, co-IP) | Core kinetochore |
| CENPU | STRING + IntAct | 0.999 (exp 0.922, co-IP) | Core kinetochore |
| CENPN | STRING | 0.999 (exp 0.906) | Core kinetochore |
| CENPL | STRING | 0.999 (exp 0.860) | Core kinetochore |
| ITGB3BP | STRING + IntAct | 0.998 (exp 0.882, co-IP) | Centromere function |
| CENPT | STRING | 0.998 (exp 0.900) | CCAN complex |

PPI 网络极其强大，集中在着丝粒/动粒核心复合物（CENP-H/I/K/L/M/N/O/P/Q/T/U/W 等 ≥0.996）。IntAct 有 CENPH/CENPI/CENPO/CENPQ/CENPU/ITGB3BP 的 co-IP 验证（PMID:19070575, 26496610），以及 KDM5C、HSPB1、NOP2 等额外互作。

**UniProt 记录互作**: CENPH (11 experiments), CENPI (3), MRFAP1L1 (3), PEX14 (3), RTN4IP1 (3), WASHC3 (3)。

### 4. 总体评价
CENPK 是一个着丝粒/动粒核心组件蛋白，核定位证据充分（着丝粒特异性定位），PPI 网络极强（与整个 CENP 家族紧密互作），研究热度中等（PM=50）。缺点是结构域注释简单、无 HPA IF 验证、AF 置信度中等。作为 chromatin 类别候选，功能特异性突出但文献量不低。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BS16
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BS16
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPK
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123219-CENPK（无 IF 原图）

![[Projects/TEreg-finding/protein-interested/detail/chromatin/CENPK/CENPK-PAE.png]]

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/chromatin/CENPK/CENPK-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BS16-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
