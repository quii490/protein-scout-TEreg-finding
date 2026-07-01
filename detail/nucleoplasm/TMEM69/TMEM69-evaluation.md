---
type: protein-evaluation
gene: "TMEM69"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM69 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM69 |
| 蛋白名称 | Transmembrane protein 69 |
| 蛋白大小 | 247 aa / 27.6 kDa |
| UniProt ID | Q5SWH9 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 247 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=2 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=74.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | DUF3429 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=20 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=2 broad=5
- AF pLDDT=74.1 PDB=0
- InterPro: DUF3429
- Pfam: DUF3429
- PPI degree=20 ChIP: None
38975141: Unveiling a cuproptosis-related risk model and the role of FARSB in hepatocellul | 24124410: Structure and Expression Analyses of SVA Elements in Relation to Functional Gene

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

TMEM69是一个功能完全未知的跨膜蛋白（247 aa, 27.6 kDa），其唯一已知的结构域为DUF3429（Pfam PF11911, InterPro IPR021836），这是一个功能未表征的保守结构域家族。AlphaFold2预测的整体结构可信度中等（pLDDT=74.1），且无PDB实验结构支持，提示其三维结构仍有较大不确定性。DUF3429结构域通常存在于跨膜蛋白中，推测TMEM69可能定位于细胞内膜系统，但其在核质中的Approved级别定位（HPA）提示可能存在非经典的内膜-核膜穿梭机制。

PPI网络分析显示TMEM69仅有20个互作伙伴（degree=20），其中GPBP1L1（STRING score=746）是最强的预测互作伙伴。GPBP1L1是一个参与转录调控的核蛋白，这一互作线索暗示TMEM69可能在核质中参与转录相关过程。值得注意的是，IMPACT、CMTR1等与RNA代谢相关的互作伙伴也出现在BioGRID数据中，进一步支持TMEM69在核内RNA调控中的潜在角色。

从文献角度看，TMEM69的研究极度匮乏（PubMed=2, strict），使其成为研究新颖性极高的靶标（得分10/10）。PMID:38975141将其纳入铜死亡相关风险模型，提示TMEM69可能与细胞应激应答有关；PMID:24124410涉及SVA逆转录转座子元件的表达分析，暗示TMEM69所在的基因组位点可能受到TE调控。TMEM69被标记为"该蛋白缺乏核定位证据，TE调控潜力极低"的评估可能过于保守——其HPA Nucleoplasm Approved定位和在SVA元件研究中的出现值得重新审视。

作为核质蛋白，TMEM69的高新颖性（PubMed=2）和HPA Approved核定位（得分9/10）构成了其主要优势。DUF3429结构域的功能解析将是理解TMEM69核内角色的关键突破口。该蛋白的低分子量（27.6 kDa）使其可能通过被动扩散进入核内，也可能作为核质中某种复合物的辅助亚基发挥作用。鉴于其在铜死亡和转座子相关研究中的线索，TMEM69可能是一个连接细胞代谢应激与核内基因表达调控的新型节点蛋白。

### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 69

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR021836 |
| Pfam | PF11911 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 69

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR021836 |
| Pfam | PF11911 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 69

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR021836 |
| Pfam | PF11911 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GPBP1L1 | STRING | 746 |
| IMPACT | BioGRID | 1 |
| PBK | BioGRID | 1 |
| KLK3 | BioGRID | 1 |
| PPP2CA | BioGRID | 1 |
| TPP2 | BioGRID | 1 |
| CMTR1 | BioGRID | 1 |
| EGLN3 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5SWH9-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000159596-TMEM69

![](https://images.proteinatlas.org/26993/259_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/26993/259_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/26993/258_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/26993/258_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/26993/260_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/26993/260_F6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 5**

| 38975141 | Unveiling a cuproptosis-related risk model and the role of FARSB in hepatocellular carcinoma. | Heliyon 2024 |
| 33777101 | A Dual Systems Genetics Approach Identifies Common Genes, Networks, and Pathways for Type 1 and 2 Diabetes in Human Isle | Front Genet 2021 |
| 28123428 | Key genes expressed in different stages of spinal cord ischemia/reperfusion injury. | Neural Regen Res 2016 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM69

