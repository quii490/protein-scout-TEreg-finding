---
type: protein-evaluation
gene: "SPRED3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SPRED3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SPRED3 |
| 蛋白名称 | Sprouty-related, EVH1 domain-containing protein 3 |
| 蛋白大小 | 410 aa / 42.7 kDa |
| UniProt ID | Q2MJR0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 410 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=12 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=65.2; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | KBD; PH-like_dom_sf; SPRE_EVH1 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=1 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=12 broad=24
- AF pLDDT=65.2 PDB=0
- InterPro: KBD; PH-like_dom_sf; SPRE_EVH1
- Pfam: Sprouty; WH1
- PPI degree=1 ChIP: None
40806788: Loss of SPRED3 Causes Primary Hypothyroidism and Alters Thyroidal Expression of  | 36442513: S-acylation of Sprouty and SPRED proteins by the S-acyltransferase zDHHC17 invol | 39627016: Intrauterine fetal growth restriction in sheep leads to sexually dimorphic progr

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Sprouty-related, EVH1 domain-containing protein 3

**功能**: Tyrosine kinase substrate that inhibits growth-factor-mediated activation of MAP kinase (By similarity). Inhibits fibroblast growth factor (FGF)-induced retinal lens fiber differentiation, probably by inhibiting FGF-mediated phosphorylation of ERK1/2 (By similarity). Inhibits TGFB-induced epithelial-to-mesenchymal transition in lens epithelial cells (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR023337 |
| InterPro | IPR011993 |
| InterPro | IPR041937 |
| InterPro | IPR007875 |
| InterPro | IPR000697 |
| Pfam | PF05210 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ZDHHC17 | BioGRID | 0 |



### 深度机制分析

SPRED3（Sprouty-related, EVH1 domain-containing protein 3，410 aa）是Sprouty/SPRED家族的MAPK信号通路的负调控因子。结构域组合为EVH1（WH1）结构域（IPR000697, PF00568）、Sprouty/KBD结构域（IPR007875, PF05210）和PH样超家族（IPR011993）。EVH1识别富含脯氨酸的基序，Sprouty结构域介导膜定位和Cbl E3连接酶互作。AF pLDDT=65.2。PPI度仅为1（ZDHHC17，S-棕榈酰转移酶），但这种单一互作极有意义——ZDHHC17负责SPRED蛋白的S-棕榈酰化修饰（PMID:36442513），该修饰调控其膜定位。关键文献40806788报道SPRED3缺失导致原发性甲减并改变甲状腺ATG5/p62自噬调节因子表达，39227612揭示SPRED3通过NF-kB信号通路调控甲状腺癌并促进增殖。核质定位为Approved。SPRED3作为MAPK/ERK通路的抑制因子（抑制FGF诱导的ERK1/2磷酸化），其核质分布可能代表其功能的动态调控：膜定位时结合Ras/ERK抑制膜近端信号，核定位时可能通过不同于膜支架的机制抑制核内ERK底物（如ELK1、c-Fos等转录因子）。TE调控方面，MAPK/ERK通路激活众多TE来源的增强子RNA和反转录转座子，SPRED3通过抑制ERK活性可能间接下调TE驱动的异常转录。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q2MJR0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000188766-SPRED3

![](https://images.proteinatlas.org/71521/1544_D7_3_red_green.jpg)
![](https://images.proteinatlas.org/71521/1544_D7_4_red_green.jpg)
![](https://images.proteinatlas.org/71521/1589_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/71521/1589_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/71521/1543_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/71521/1543_D7_2_red_green.jpg)

### PubMed 文献

**PubMed count: 24**

| 40806788 | Loss of SPRED3 Causes Primary Hypothyroidism and Alters Thyroidal Expression of Autophagy Regulators LC3, p62, and ATG5  | Int J Mol Sci 2025 |
| 39627016 | Intrauterine fetal growth restriction in sheep leads to sexually dimorphic programming of Preadipocytes' differentiation | Physiol Rep 2024 |
| 39227612 | SPRED3 regulates the NF-κB signaling pathway in thyroid cancer and promotes the proliferation. | Sci Rep 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SPRED3

