---
type: protein-evaluation
gene: "TSPAN5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TSPAN5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TSPAN5 |
| 蛋白名称 | Tetraspanin-5 |
| 蛋白大小 | 268 aa / 30.3 kDa |
| UniProt ID | P62079 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 268 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=33 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=89.2; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Tetraspanin/Peripherin; Tetraspanin_animals; Tetraspanin_CS |
| PPI | 6/10 | x3 | 18.0 | PPI degree=80 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=33 broad=64
- AF pLDDT=89.2 PDB=0
- InterPro: Tetraspanin/Peripherin; Tetraspanin_animals; Tetraspanin_CS
- Pfam: Tetraspanin
- PPI degree=80 ChIP: None
35992081: The role of tetraspanins pan-cancer. | 33510640: Selective Serotonin Reuptake Inhibitor Pharmaco-Omics: Mechanisms and Prediction | 32753686: TSPAN5 influences serotonin and kynurenine: pharmacogenomic mechanisms related t

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

TSPAN5（Tetraspanin-5）是tetraspanin超家族的典型成员，具有四次跨膜螺旋拓扑结构（268 aa, 30.3 kDa）。其结构域架构包含特征性的tetraspanin保守特征：一个小的胞外环（EC1）、一个大的胞外环（EC2）含保守的CCG基序和两对保守半胱氨酸（InterPro IPR018503），以及胞内N/C端短尾。Pfam Tetraspanin（PF00335）结构域覆盖整个蛋白。AlphaFold2预测pLDDT=89.2（得分7/10），高度可信，无PDB实验结构但tetraspanin折叠已有多个同源结构支持。

TSPAN5的PPI网络度为80（得分6/10），其核心功能伙伴为ADAM10金属蛋白酶——TSPAN5属于TspanC8亚家族，该亚家族的6个成员均与ADAM10形成化学计量复合物，调控ADAM10从内质网的出口、酶成熟和底物特异性（PMID:26686862, 28600292, 37516108）。不同TspanC8/ADAM10复合物具有不同的底物偏好，TSPAN5特异性促进ADAM10对CD44的剪切。在PPI网络中，与APP的BioGRID互作提示TSPAN5可能在ADAM10介导的APP加工和Aβ生成中发挥作用。

在核质环境中，TSPAN5的Approved级别定位挑战了传统认知。作为典型的质膜tetraspanin，TSPAN5如何进入核质是一个悬而未决的问题。一种可能性是TSPAN5通过retromer介导的逆行转运从内体-溶酶体系统泄漏至核周区域并入核。TSPAN5调控VE-cadherin表达的发现（UniProt功能注释）暗示核质TSPAN5可能通过ADAM10介导的剪切事件释放胞内片段，该片段可能入核调控转录。与THAP11（THAP结构域蛋白11，含锌指的转录调控因子）的BioGRID互作支持这一核内功能假设。

TSPAN5在神经精神疾病中具有突出的临床相关性。PMID:32753686和33510640揭示TSPAN5影响血清素和犬尿氨酸通路，与选择性血清素再摄取抑制剂（SSRI）的药物基因组学机制相关。犬尿氨酸通路是色氨酸代谢的关键分支，其代谢产物（如喹啉酸）是NMDA受体调节剂，而TSPAN5通过调控ADAM10活性可能影响神经递质受体在突触后膜的表达。PMID:41485015发现Cldn11缺失通过Tspan5依赖性方式加重骨关节炎，进一步支持TSPAN5在非神经组织中的调控功能。

TSPAN5是核质蛋白研究中的一个独特案例——经典的膜tetraspanin在核质中可能执行与质膜定位完全不同的信号调控功能。33篇PubMed文献（得分8/10）和Nucleoplasm Approved定位（得分9/10）的组合使其成为一个研究深度适中但核内机制几乎没有被探索的理想靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Tetraspanin-5

**功能**: Part of TspanC8 subgroup, composed of 6 members that interact with the transmembrane metalloprotease ADAM10. This interaction is required for ADAM10 exit from the endoplasmic reticulum and for enzymatic maturation and trafficking to the cell surface as well as substrate specificity. Different TspanC8/ADAM10 complexes have distinct substrates (PubMed:26686862, PubMed:28600292, PubMed:37516108). Promotes ADAM10-mediated cleavage of CD44 (PubMed:26686862). Seems to regulate VE-cadherin expression i

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR018499 |
| InterPro | IPR000301 |
| InterPro | IPR018503 |
| InterPro | IPR008952 |
| Pfam | PF00335 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 1 |
| ALG8 | BioGRID | 1 |
| THAP11 | BioGRID | 1 |
| KLHL2 | BioGRID | 1 |
| TMUB1 | BioGRID | 1 |
| EFNB1 | BioGRID | 1 |
| LEMD2 | BioGRID | 1 |
| NDC1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P62079-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000168785-TSPAN5

![](https://images.proteinatlas.org/79522/2213_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/79522/2213_F4_3_red_green.jpg)
![](https://images.proteinatlas.org/79522/1972_G5_19_cr5e16e7f462fd4_red_green.jpg)
![](https://images.proteinatlas.org/79522/1972_G5_29_cr5e16e7f463490_red_green.jpg)
![](https://images.proteinatlas.org/79522/2102_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/79522/2102_D1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 64**

| 41801554 | Prognostic Significance and Immune Landscape of Migrasome-Related Genes in Pancreatic Cancer. | Appl Biochem Biotechnol 2026 |
| 41485015 | Cldn11 deficiency aggravates osteoarthritis by inhibiting Notch signalling in a Tspan5-dependent manner. | J Orthop Surg Res 2026 |
| 41367385 | Decoding the peripheral transcriptomic and meta-genomic response to music in autism spectrum disorder via saliva-based R | Front Mol Biosci 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TSPAN5

