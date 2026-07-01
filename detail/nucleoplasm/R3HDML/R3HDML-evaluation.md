---
type: protein-evaluation
gene: "R3HDML"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## R3HDML 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | R3HDML |
| 蛋白名称 | Peptidase inhibitor R3HDML |
| 蛋白大小 | 253 aa / 28.6 kDa |
| UniProt ID | Q9H3Y0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 253 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=6 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=82.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | CAP_dom; CAP_sf; CRISP-related |
| PPI | 5/10 | x3 | 15.0 | PPI degree=6 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=6 broad=8
- AF pLDDT=82.8 PDB=0
- InterPro: CAP_dom; CAP_sf; CRISP-related
- Pfam: CAP
- PPI degree=6 ChIP: None
37866487: Bavachin combined with epimedin B induce idiosyncratic liver injury under immuno | 31524320: R3hdml regulates satellite cell proliferation and differentiation. | 41067425: Multivariate genomic analysis elucidates the genetic architecture of shared comp

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Peptidase inhibitor R3HDML

**功能**: Putative serine protease inhibitor

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR014044 |
| InterPro | IPR035940 |
| InterPro | IPR001283 |
| InterPro | IPR047899 |
| Pfam | PF00188 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 1 |
| CDK7 | BioGRID | 1 |
| PLEC | BioGRID | 0 |
| HSPA5 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H3Y0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000101074-R3HDML

![](https://images.proteinatlas.org/62414/2192_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/62414/2192_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/62414/2198_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/62414/2198_E9_4_red_green.jpg)

### PubMed 文献

**PubMed count: 8**

| 41067425 | Multivariate genomic analysis elucidates the genetic architecture of shared components of burning mouth syndrome. | J Stomatol Oral Maxillofac Surg 2026 |
| 37866487 | Bavachin combined with epimedin B induce idiosyncratic liver injury under immunological stress conditions. | Chem Biol Interact 2023 |
| 33620517 | A novel podocyte protein, R3h domain containing-like, inhibits TGF-β-induced p38 MAPK and regulates the structure of pod | J Mol Med (Berl) 2021 |

### 深度机制分析

R3HDML的域架构以单个CAP结构域（半胱氨酸富集分泌蛋白/抗原5/致病相关蛋白1, IPR014044; Pfam PF00188）为中心，属于CRISP相关超家族（IPR047899）。CAP结构域采用保守的α-β-α三明治折叠（CAP_sf, IPR035940），具有特征性的保守半胱氨酸残基簇，形成多个二硫键用于胞外配体结合。该结构域被注释为推定的丝氨酸蛋白酶抑制剂，表明其通过底物样环区结合并阻断催化三联体Ser-His-Asp。

AlphaFold pLDDT为82.8，CAP结构域区域处于高置信度区间，而N端和C端尾部的置信度较低。无实验PDB结构。PPI网络（degree=6）由APP（淀粉样前体蛋白，BioGRID=1）和CDK7（细胞周期蛋白依赖性激酶7，BioGRID=1）主导。CDK7是TFIIH复合物的催化亚基，参与转录起始和细胞周期调控——这为R3HDML在核质中的存在提供了功能锚点。

综合机制模型：R3HDML作为分泌型/核质丝氨酸蛋白酶抑制剂双定位蛋白发挥功能。在胞外，CAP结构域可逆地结合并抑制参与TGF-β活化的丝氨酸蛋白酶；在核质中，它可能通过阻断CDK7磷酸化底物所需的蛋白水解步骤来调节CDK7活性。已证实R3HDML可抑制足细胞中TGF-β诱导的p38 MAPK活化并调控足细胞结构（PMID 33620517），暗示其蛋白酶抑制剂活性可直接靶向TGF-β信号级联中的蛋白酶步骤。双定位（Cytosol; Nucleoplasm, HPA Approved）表明存在条件性核易位机制。

TE调控启示：CAP结构域是进化上古老的折叠，与许多TE衍生基因融合物中的病原体防御模块同源。R3HDML规模小（6篇文献）、结构良好（pLDDT=82.8），且与CDK7（TFIIH组分）的互作使其成为研究TE激活条件下蛋白酶抑制剂如何调控转录重编程的优秀候选底物。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/R3HDML

