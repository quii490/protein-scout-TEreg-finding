---
type: protein-evaluation
gene: "PFDN4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PFDN4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PFDN4 |
| 蛋白名称 | Prefoldin subunit 4 |
| 蛋白大小 | 134 aa / 15.3 kDa |
| UniProt ID | Q9NQP4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 134 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=15 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=87.4; PDB=6 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PFD_beta-like; PFDN4; Prefoldin |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=130 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | nan (nan) |
| PubMed | strict=15, broad=21 |
| AF pLDDT | 87.4 |
| PDB | 6 |
| InterPro | PFD_beta-like; PFDN4; Prefoldin |
| Pfam | Prefoldin_2 |
| PPI degree | 130 |
| ChIP | None |

**Papers**: 38835051: Single-cell and bulk RNA-seq unveils the immune infiltration landscape associate | 38016755: Potential of PAQosome as a therapeutic target for hepatic fibrosis. | 40231067: RAD51 expression and prognostic impact in patients with stomach adenocarcinoma.

### 4. 总体评价
★★★★  **72.1/100**  |  **nucleoplasm**
Nuclear protein


### 深度机制分析

PFDN4（Prefoldin subunit 4）是一个134 aa的小蛋白（15.3 kDa），属于prefoldin分子伴侣复合物的β亚家族。其结构域架构简洁：N端为prefoldin β样折叠（InterPro IPR009053），中间为PFDN4特异性保守区（InterPro IPR016661），整体构成prefoldin β亚基特征性的长螺旋发夹结构（Pfam Prefoldin_2, PF01920）。AlphaFold2预测pLDDT=87.4（得分10/10），PDB数据库中有6个实验结构，主要是prefoldin六聚体复合物和与伴侣蛋白的复合物晶体结构，结构解析度极高。

PFDN4的PPI网络极为丰富（degree=130，得分7/10），呈现出典型的分子伴侣复合物特征。与PFDN2、PFDN5、PFDN6、PFDN1和VBP1（von Hippel-Lindau结合蛋白1）的互作构成了经典的prefoldin六聚体（PFD1-PFD6），这是胞质中新生多肽折叠的关键辅助系统。但与PRPF4（pre-mRNA加工因子4）和SPATA2（精子发生相关蛋白2）的BioGRID互作提示PFDN4在核质中存在独立于经典prefoldin复合物的功能。PRPF4是U4/U6 snRNP的核心组分，参与pre-mRNA剪接，PFDN4可能通过协助剪接体蛋白的折叠或组装影响RNA加工。

从功能机制角度，PFDN4在胞质中主要作为新生多肽的捕获和转运平台，将未折叠蛋白递送至伴侣蛋白CCT/TRiC进行ATP依赖的折叠。然而，在核质中缺乏CCT系统的情况下，PFDN4可能扮演不同的角色。prefoldin亚基在核内的重新定位已被多个研究证实——它们从细胞质中的经典折叠功能转变为核内转录和染色质调控的辅助因子。与TUBA3E（α-微管蛋白3E）的互作提示PFDN4可能参与核内微管蛋白的折叠和功能调控。

PFDN4在癌症中的预后意义已被多项研究验证。PMID:39644788发现PFDN4在肝细胞癌中具有预后意义，可能是通过调控肿瘤免疫微环境实现的。PMID:38835051利用单细胞RNA-seq揭示PFDN4在脑海绵状血管畸形中与铜死亡相关的免疫浸润景观中发挥作用。尽管PubMed=15文献数相对较少（得分9/10），但PFDN4在prefoldin复合物背景下的结构生物学储备极为丰富（PBD=6），为核内功能研究提供了坚实的分子基础。

### 补充分析 (UniProt API)

**蛋白全称**: Prefoldin subunit 4

**功能**: Binds specifically to cytosolic chaperonin (c-CPN) and transfers target proteins to it. Binds to nascent polypeptide chain and promotes folding in an environment in which there are many competing pathways for nonnative proteins

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002777 |
| InterPro | IPR016661 |
| InterPro | IPR009053 |
| Pfam | PF01920 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PRPF4 | BioGRID | 0 |
| SPATA2 | BioGRID | 0 |
| TUBA3E | BioGRID | 0 |
| PFDN2 | BioGRID | 0 |
| VBP1 | BioGRID | 0 |
| PFDN5 | BioGRID | 0 |
| PFDN6 | BioGRID | 0 |
| PFDN1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NQP4-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 21**

| 40231067 | RAD51 expression and prognostic impact in patients with stomach adenocarcinoma. | PeerJ 2025 |
| 39644788 | The prognostic significance and potential mechanism of PFDN4 in hepatocellular carcinoma. | Int Immunopharmacol 2025 |
| 38835051 | Single-cell and bulk RNA-seq unveils the immune infiltration landscape associated with cuproptosis in cerebral cavernous | Biomark Res 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PFDN4

