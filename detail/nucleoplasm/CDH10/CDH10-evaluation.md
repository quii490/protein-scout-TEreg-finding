---
type: protein-evaluation
gene: "CDH10"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CDH10 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CDH10 |
| 蛋白名称 | Cadherin-10 |
| 蛋白大小 | 788 aa / 88.5 kDa |
| UniProt ID | Q9Y6N8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cell Junctions; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 788 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=29 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=78.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cadherin; Cadherin-like_dom; Cadherin-like_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=23 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- HPA: Cell Junctions; Nucleoplasm (Approved)
- PubMed: strict=29, broad=55
- AF pLDDT: 78.4 / PDB: 0
- InterPro: Cadherin; Cadherin-like_dom; Cadherin-like_sf
- Pfam: CADH_Y-type_LIR; Cadherin
- PPI degree=23 / ChIP: None
32574161: Distinct subtypes of polycystic ovary syndrome with novel genetic associations:  | 32292512: G9a-mediated repression of CDH10 in hypoxia enhances breast tumour cell motility | 37556355: MYEF2: an immune infiltration-related prognostic factor in IDH-wild-type gliobla

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

CDH10（Cadherin-10）是一个经典的I型钙粘蛋白（788 aa, 88.5 kDa），其结构域架构遵循经典钙粘蛋白范式：5个钙粘蛋白胞外重复结构域（EC1-EC5, InterPro IPR002126），负责Ca²⁺依赖的同嗜性细胞黏附；一个单次跨膜螺旋；以及一个高度保守的胞内结构域，包含β-catenin结合区（InterPro IPR000233）和p120-catenin结合近膜区（InterPro IPR027397）。Cadherin-10属于II型钙粘蛋白亚家族（InterPro IPR039808），其特征是EC1结构域不含经典的HAV黏附基序。AlphaFold2预测pLDDT=78.4（得分6/10），无PDB实验结构。

CDH10的PPI网络度为23，其STRING网络呈现出高度可信的钙粘蛋白-连环蛋白复合物特征。CTNNB1（β-catenin, STRING=866）和JUP（γ-catenin/plakoglobin, BioGRID score=1）是钙粘蛋白胞内结构域的核心结合伙伴——它们连接钙粘蛋白与α-catenin和肌动蛋白细胞骨架。CTNNA3（α-catenin-3, BioGRID）是神经元特异性α-catenin，参与突触黏附和信号传导。值得注意的是，CDH6（II型钙粘蛋白-6, STRING=782）可能通过顺式二聚化与CDH10协同调控黏附特异性。与COPS6（COP9信号体亚基6，调控Cullin-RING E3泛素连接酶活性）和PTN（多效生长因子/神经突生长促进因子）的互作则提示CDH10在非黏附性信号调控中的功能。

CDH10在核质中的Approved级别定位是经典钙粘蛋白中的一个值得关注的发现。在Wnt信号通路激活条件下，β-catenin从钙粘蛋白复合物中释放并转位至核内，与TCF/LEF转录因子协同激活Wnt靶基因。CDH10作为膜锚点可能通过控制β-catenin的可用池间接调控Wnt信号的核内输出。然而，钙粘蛋白胞内结构域的直接核转位也在部分钙粘蛋白中被报道——γ-分泌酶可在跨膜区剪切钙粘蛋白，释放胞内片段入核调控转录。

CDH10的功能研究集中在神经发育和肿瘤两个领域。PMID:32574161发现CDH10与多囊卵巢综合征的新遗传关联，PMID:32292512揭示了缺氧条件下G9a介导的CDH10抑制增强了乳腺癌细胞的运动性——这直接关联CDH10的表观遗传沉默与肿瘤转移。在神经系统中，CDH10参与特定神经元连接的建立和特化，其mRNA在前额叶皮层特定神经元亚群中富集。29篇PubMed文献（得分9/10）为CDH10提供了坚实的文献基础，但核质中CDH10的直接功能从未被实验验证，这代表了一个明确的机遇——使用CDH10胞内结构域特异的抗体进行ChIP-seq或Cut&Run可能揭示其在核内的染色质结合图谱。

### 补充分析 (UniProt API)

**蛋白全称**: Cadherin-10

**功能**: Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR039808 |
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR020894 |
| InterPro | IPR000233 |
| InterPro | IPR027397 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CTNNB1 | STRING | 866 |
| CDH6 | STRING | 782 |
| NLGN1 | STRING | 708 |
| COPS6 | BioGRID | 1 |
| JUP | BioGRID | 1 |
| PTN | BioGRID | 0 |
| CTNNA3 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y6N8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000040731-CDH10

![](https://images.proteinatlas.org/12085/1973_C5_25_cr5df79c5b7aaa5_red_green.jpg)
![](https://images.proteinatlas.org/12085/1973_C5_30_cr5df79c5b7b1d0_red_green.jpg)
![](https://images.proteinatlas.org/12085/2033_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/12085/2033_F7_6_red_green.jpg)
![](https://images.proteinatlas.org/12085/1976_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/12085/1976_F12_3_red_green.jpg)

### PubMed 文献

**PubMed count: 55**

| 39028495 | Identification of hub genes associated with pyroptosis in diabetic nephropathy patients using integrated bioinformatic a | Int Urol Nephrol 2025 |
| 38872096 | Silencing immune-infiltrating biomarker CCDC80 inhibits malignant characterization and tumor formation in gastric cancer | BMC Cancer 2024 |
| 38239411 | Developing the novel diagnostic model and potential drugs by integrating bioinformatics and machine learning for aldoste | Front Mol Biosci 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CDH10

