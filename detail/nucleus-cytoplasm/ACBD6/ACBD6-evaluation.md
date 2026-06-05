---
type: protein-evaluation
gene: "ACBD6"
date: 2026-05-31
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## ACBD6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ACBD6 |
| 蛋白全名 | Acyl-CoA-binding domain-containing protein 6 |
| 蛋白大小 | 282 aa / 31.2 kDa |
| UniProt ID | Q9BR61 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | UniProt: Cytoplasm + Nucleus (ECO:0000269); GO: nucleus IDA |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 282 aa, 31.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed strict=21, broad=25 |
| 三维结构 | 6/10 | ×3 | 18.0 | PDB 2COP NMR partial; AlphaFold pLDDT 77.0 |

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/ACBD6/ACBD6-PAE.png]]
![[ACBD6-PAE.png]]
| 调控结构域 | 5/10 | ×2 | 10.0 | Acyl-CoA-binding/ANK-like regions，脂质修饰调控相关 |
| PPI 网络 | 7/10 | ×3 | 21.0 | NMT1/NMT2 在 UniProt、STRING、IntAct 多源出现 |
| **加权总分** | | | **124/180**** | |
| 互证加分 | | | +1.0 | UniProt/GO 定位互证；NMT1/NMT2 PPI 多库互证 |
| **归一化总分 (÷1.83)** | | | **67.8/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Cytoplasm (ECO:0000269); Nucleus (ECO:0000269) | Experimental |
| GO-CC | cytoplasm IDA; cytosol TAS; nucleus IDA | Experimental |
| Protein Atlas (IF) | HPA 暂无数据，未获取到 IF 图像或缩略图 | 未确认 |

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

#### 3.2 结构与结构域
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q9BR61-F1 |
| 平均 pLDDT | 77.0 |
| pLDDT >90 | 41.8% |
| PDB | 2COP, NMR, A=42-137 |
| InterPro | IPR000582, IPR035984, IPR002110, IPR036770, IPR014352 |
| Pfam | PF00887, PF12796 |

![[ACBD6-PAE.png]]

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 21 |
| PubMed broad | 25 |

关键文献包括 ACBD6 神经发育综合征（PMID:37951597）、N-myristoylation 调控（PMID:30642881, 32108178）和脂质/蛋白 acylation remodeling（PMID:36551154）。研究量中等偏低，仍有机制空间。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| NMT1 | UniProt | 7 experiments | N-myristoylation, strong |
| NMT2 | UniProt | 18 experiments | N-myristoylation, strong |
| NMT2 | STRING | 0.917 (exp 0.656) | Strong experimental support |
| NMT1 | STRING | 0.822 (exp 0.648) | Strong experimental support |
| ACBD3 | STRING | 0.620 (textmining) | Low |
| IKBKG | IntAct | protein array (direct, PMID:20098747) | NF-κB signaling |
| NMT2 | IntAct | two hybrid array (PMID:32296183) | N-myristoylation |
| NMT1 | IntAct | validated two hybrid (PMID:32296183) | N-myristoylation |
| TULP3 | IntAct | anti tag coIP (PMID:33961781) | Cilium/transport |
| ATG7 | IntAct | anti tag coIP (PMID:33961781) | Autophagy |

UniProt 记录 NMT1(7 experiments) 与 NMT2(18 experiments)。STRING 对 NMT2(score 0.917, experimental 0.656) 和 NMT1(score 0.822, experimental 0.648) 支持强。IntAct 也记录 NMT1/NMT2 及 IKBKG、TULP3、ATG7 等互作。PPI 明确指向蛋白 N-myristoylation 与脂质修饰网络，而非经典染色质复合体。

### 4. 总体评价
ACBD6 是有实验证据的核-胞质蛋白，主要功能偏脂质/蛋白 acylation 与 myristoylation 调控。它不是典型染色质因子，但核定位证据足够，不应 rejected。建议作为中等优先级核-胞质候选保留。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BR61
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BR61
- PDB: 2COP
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ACBD6
- Protein Atlas: https://www.proteinatlas.org/search/ACBD6（无 IF 原图）

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/ACBD6/ACBD6-PAE.png]]



![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/ACBD6/ACBD6-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000230124-ACBD6/subcellular

![](https://images.proteinatlas.org/28457/1466_A7_3_red_green.jpg)
![](https://images.proteinatlas.org/28457/1466_A7_4_red_green.jpg)
![](https://images.proteinatlas.org/28457/1520_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/28457/1520_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/28457/1521_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/28457/1521_A7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
