---
type: protein-evaluation
gene: "MFSD6"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MFSD6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MFSD6 |
| 蛋白名称 | Major facilitator superfamily domain-containing protein 6 |
| 蛋白大小 | 791 aa / 88.1 kDa |
| UniProt ID | Q6ZSS7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 791 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=8 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=65.7; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | MFS_assoc_dom; MFS_MFSD6; MFS_trans_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=41 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=8 broad=14
- AF pLDDT=65.7 PDB=1
- InterPro: MFS_assoc_dom; MFS_MFSD6; MFS_trans_sf
- Pfam: MFS_1_like
- PPI degree=41 ChIP: None
39798568: MFSD6 is an entry receptor for respiratory enterovirus D68. | 42189918: Decoding the complex receptor landscape of enterovirus D68. | 31906755: Probable role for major facilitator superfamily domain containing 6 (MFSD6) in t

### 4. 总体评价
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Major facilitator superfamily domain-containing protein 6

**功能**: (Microbial infection) Acts as a receptor for respiratory enterovirus D68 (PubMed:39798568, PubMed:40132641). Mechanistically, binds to viral particles and is required for viral cell entry while initial attachment to cells is mainly mediated by interactions with sialic acid (PubMed:40132641)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR024989 |
| InterPro | IPR051717 |
| InterPro | IPR036259 |
| Pfam | PF12832 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

MFSD6（Major facilitator superfamily domain-containing protein 6）是MFS超家族的一员，但其结构域架构包含独特的MFS_assoc_dom（IPR024989）和MFS_MFSD6（IPR051717）专属结构域，提示该蛋白在MFS超家族中具有独特的功能特化。791个氨基酸（88.1 kDa）的大分子量远超典型MFS转运蛋白（通常400-600 aa），表明可能容纳了额外的结构域或调控区域。然而，AlphaFold预测的pLDDT值仅为65.7，在评估队列中属于较低水平，提示存在大量内在无序区域（IDR），可能参与蛋白-蛋白相互作用或翻译后修饰的调控。

MFSD6的功能研究在2024-2026年取得了突破性进展。该蛋白被确证为呼吸道肠道病毒D68（EV-D68）的细胞进入受体（PMID 39798568, PMID 40132641）。机制上，MFSD6与病毒颗粒结合，是病毒进入细胞所必需的——而非负责初始的细胞附着（该步骤由唾液酸介导）（PMID 40132641, PLoS Pathog, 2026）。这一受体功能的发现为经典的MFS转运蛋白增加了重要的 moonlighting功能维度。HPA免疫荧光显示Cytosol; Nucleoplasm (Approved)的定位模式——其核质定位可能与病毒进入后触发的先天性免疫信号通路有关。

PPI网络揭示了MFSD6与神经递质转运体SLC18A1、胆汁酸转运体SLC10A1以及CYB5R3、SYNDIG1、CD79A、NKG7和TSPO2等蛋白的互作。其中KIAA1429（VIRMA）是一个m6A甲基转移酶复合体组分，在RNA修饰和基因表达调控中发挥重要作用。这一互作如果得到验证，MFSD6可能通过调控RNA表观转录组间接影响基因表达——包括重复序列和TE元件的表达。这是该蛋白在TE调控中的潜在间接机制。此外，TSPO2的互作将MFSD6与线粒体功能和胆固醇转运联系起来。

MFSD6的PubMed覆盖为8篇（strict），14篇（broad），属于中等新颖度的候选蛋白。PPI degree=41提示中等复杂度的互作网络。其作为病毒受体的功能虽已被验证，但核质定位的功能意义仍是开放问题。从研究策略角度，建议：（1）鉴定MFSD6的核定位信号和核内结合伙伴；（2）利用EV-D68感染模型分析MFSD6在病毒介导的先天性免疫应答中的核功能；（3）探索其无序区域是否进行液-液相分离（LLPS）形成核内凝集体；（4）明确MFSD6与KIAA1429的互作是否影响m6A修饰图谱。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KIAA1429 | BioGRID | 0 |
| SLC18A1 | BioGRID | 0 |
| CYB5R3 | BioGRID | 0 |
| SLC10A1 | BioGRID | 0 |
| SYNDIG1 | BioGRID | 0 |
| CD79A | BioGRID | 0 |
| NKG7 | BioGRID | 0 |
| TSPO2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6ZSS7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000151690-MFSD6

![](https://images.proteinatlas.org/22274/193_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/22274/193_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/22274/192_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/22274/192_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/22274/194_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/22274/194_A1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 14**

| 42189918 | Decoding the complex receptor landscape of enterovirus D68. | PLoS Pathog 2026 |
| 41600837 | Enterovirus D68 Sequence Variations and Pathogenicity: A Review. | Viruses 2026 |
| 41467840 | Enterovirus D68 receptor usage: from static attachment to dynamic entry. | J Virol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MFSD6

