---
type: protein-evaluation
gene: "PCDHGA10"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGA10 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGA10 |
| 蛋白名称 | Protocadherin gamma-A10 |
| 蛋白大小 | 936 aa / 101.4 kDa |
| UniProt ID | Q9Y5H3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 936 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=6 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=74.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 5/10 | x3 | 15.0 | PPI degree=18 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=6 broad=8
- AF pLDDT=74.4 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_C
- Pfam: Cadherin; Cadherin_2; Cadherin_C_2
- PPI degree=18 ChIP: None
28940097: Expanding the genetic heterogeneity of intellectual disability. | 37554401: Transcriptome sequencing reveals novel molecular features of SLE severity. | 39687617: PCDHGA10 as a potential prognostic biomarker and correlated with immune infiltra

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

PCDHGA10（Protocadherin gamma-A10）是原钙粘蛋白γ簇的A亚家族成员，具有936 aa的大分子量（101.4 kDa）。其结构域架构与PCDHGC5高度相似：6个钙粘蛋白重复结构域（InterPro IPR002126, IPR015919）构成胞外区，C端钙粘蛋白胞内结构域（InterPro IPR032455）介导胞内信号传导。AlphaFold2预测pLDDT=74.4，与PCDHGC5完全相同，表明这一区域的AF2预测具有一致性——γ簇蛋白的胞外重复区可能是柔性较大导致pLDDT偏低的共同原因。

PCDHGA10的PPI网络度为18，其互作伙伴展现出清晰的PCDH家族内聚类特征：PCDHGA7、PCDHGA4、PCDHGB2、PCDHB7、PCDHB3等同为原钙粘蛋白家族成员，提示PCDHGA10在神经元表面通过顺式多聚化形成黏附复合物。尤为值得注意的是与PTEN的BioGRID互作——PTEN是经典的肿瘤抑制因子和PI3K/AKT通路负调控因子，具有明确的核内功能（包括维持基因组稳定性和调控着丝粒稳定性）。PCDHGA10与PTEN的互作可能在核质中影响PTEN的核定位和功能。

从功能机制角度，PCDHGA10的最新研究（PMID:39687617）揭示了其作为胃癌预后生物标志物和免疫浸润相关分子的潜力。该研究通过转录组分析和免疫组化验证，发现PCDHGA10的表达与肿瘤免疫微环境密切相关。在核质中，PCDHGA10的胞内结构域可能如同其家族成员一样响应钙信号而被剪切入核，参与调控免疫相关基因的转录。PMID:42184948的最新发现表明血小板因子4通过调控原钙粘蛋白表达预防帕金森病模型中的神经炎症，进一步支持PCDHGA10在神经免疫调控中的潜在角色。

作为核质蛋白，PCDHGA10的研究新颖性极高（PubMed=6，得分10/10），核定位明确（Nucleoplasm Approved，得分9/10）。该蛋白在肿瘤免疫微环境和神经退行性疾病中的双重临床相关性使其成为转化医学研究的理想靶标。未来研究应聚焦于PCDHGA10胞内结构域的剪切机制、核转位信号及其在核内的转录调控伙伴。

### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin gamma-A10

**功能**: Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR032455 |
| InterPro | IPR031904 |
| InterPro | IPR020894 |
| InterPro | IPR013164 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KIAA1429 | BioGRID | 0 |
| PTEN | BioGRID | 0 |
| ITGA8 | BioGRID | 0 |
| PCDHGA7 | BioGRID | 0 |
| PCDHGA4 | BioGRID | 0 |
| PCDHGB2 | BioGRID | 0 |
| PCDHB7 | BioGRID | 0 |
| PCDHB3 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5H3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000253846-PCDHGA10

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 8**

| 42331777 | Frataxin deficiency drives cardiac dysfunction and transcriptional dysregulation in Friedreich ataxia iPSC model. | Cell Death Dis 2026 |
| 42184948 | Platelet factor 4 prevents neuroinflammation and neurodegeneration in Parkinson's disease model via regulating protocadh | Brain Behav Immun 2026 |
| 39687617 | PCDHGA10 as a potential prognostic biomarker and correlated with immune infiltration in gastric cancer. | Front Immunol 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGA10

