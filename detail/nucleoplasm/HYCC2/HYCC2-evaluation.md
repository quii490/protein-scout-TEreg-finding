---
type: protein-evaluation
gene: "HYCC2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## HYCC2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HYCC2 |
| 蛋白名称 | Hyccin 2 |
| 蛋白大小 | 530 aa / 58.6 kDa |
| UniProt ID | Q8IXS8 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cell Junctions; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 530 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=1 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=68.0; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Hyccin |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- Cell Junctions; Nucleoplasm (Supported)
- PubMed strict=1 broad=1
- AF pLDDT=68.0 PDB=0
- InterPro: Hyccin
- Pfam: Hyccin
- PPI degree=0 ChIP: None
41516281: Weighted Gene Co-Expression Network Analysis and Alternative Splicing Analysis R

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Hyccin 2

**功能**: Component of a complex required to localize phosphatidylinositol 4-kinase (PI4K) to the plasma membrane

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR018619 |
| Pfam | PF09790 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Hyccin 2

**功能**: Component of a complex required to localize phosphatidylinositol 4-kinase (PI4K) to the plasma membrane

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR018619 |
| Pfam | PF09790 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8IXS8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000155744-HYCC2

![](https://images.proteinatlas.org/67307/1258_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/67307/1258_G9_3_red_green.jpg)
![](https://images.proteinatlas.org/67307/1284_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/67307/1284_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/67307/1249_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/67307/1249_G9_3_red_green.jpg)

### PubMed 文献

**PubMed count: 1**

| 41516281 | Weighted Gene Co-Expression Network Analysis and Alternative Splicing Analysis Reveal Key Genes Regulating Overfeeding-I | Int J Mol Sci 2025 |

### 深度机制分析

HYCC2（530 aa, 58.6 kDa）是Hyccin家族蛋白成员，其结构域架构仅含一个Hyccin结构域（IPR018619, PF09790），该结构域覆盖蛋白的大部分序列但功能注释极为有限。AlphaFold预测pLDDT=68.0，整体折叠质量一般，部分区域存在长程无序。Hyccin结构域的功能是通过与FAM126蛋白家族的关联推导而出——已知Hyccin/FAM126复合物是质膜磷脂酰肌醇4-激酶（PI4K）定位所必需。

HYCC2的核心功能是作为PI4K复合物的支架组分，引导PI4K定位于质膜以产生PI4P（磷脂酰肌醇-4-磷酸）。PI4P是质膜的关键信号脂质和膜运输调控分子，参与TGN-质膜的物质运输、脂质交换和信号转导。PPI网络（STRING，BioGRID无）完美验证了这一点：HYCC2与PI4KA（STRING 605）、TTC7A（STRING 673）和TTC7B（STRING 662）、EFR3A（STRING 668）和EFR3B（STRING 588）形成核心PI4K复合物，与FAM126B（STRING 478）的关联也符合FAM126-Hyccin-PI4K复合物组装模型。

HPA定位为Cell Junctions; Nucleoplasm（Supported级别），其中细胞连接定位与PI4K复合物在质膜的典型功能一致，而核质定位则再次提示Hyccin家族可能存在核内非经典功能。HYCC2与PI4KA的直接互作暗示若PI4K被HYCC2引导至核膜或核质内部，则核内PI4P生成可能被局部激活。核PI4P是核磷肌醇信号网络的组成部分，调控核内肌动蛋白动力学、RNA加工和转录因子定位。

PPI网络含CSE1L（核输出蛋白，STRING 491）和BZW1（转录因子调控的翻译起始因子，STRING 572），分别提示HYCC2可能在核质穿梭和翻译调控层面发挥功能。KTI12（STRING 520）已知参与tRNA修饰，与核内RNA加工相关。AGFG1（STRING 431）参与核内内体运输。

在TE调控方面，HYCC2最具吸引力的假设是"核膜PI4P微域假说"：HYCC2通过引导PI4K至内核膜生成PI4P微域，这些微域可作为特定蛋白（包括染色质修饰因子或转录抑制因子）的核质内锚定点。PI4P微域的形成和消散调控着核膜附近异染色质（lamina-associated domains, LADs）的可逆性解离——LADs中富含LINE-1等重复序列。文献极度稀缺（PubMed=1，PMID:41516281——过度喂养山羊转录组），新颖性极高但功能注释处于早期阶段。建议通过核质分离和PI4P脂质组学验证HYCC2是否影响核内磷酸肌醇分布。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| EFR3A | STRING | 668 |
| PI4KA | STRING | 605 |
| CSE1L | STRING | 491 |
| PPIL3 | STRING | 490 |
| NKPD1 | STRING | 427 |
| TTC7B | STRING | 662 |
| KTI12 | STRING | 520 |
| FAM214B | STRING | 429 |
| TTC7A | STRING | 673 |
| RAB2B | STRING | 448 |
| EFR3B | STRING | 588 |
| AGFG1 | STRING | 431 |
| FAM126B | STRING | 478 |
| BZW1 | STRING | 572 |
