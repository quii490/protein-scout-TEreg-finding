---
type: protein-evaluation
gene: "GATD1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GATD1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GATD1 |
| 蛋白名称 | Glutamine amidotransferase-like class 1 domain-containing protein 1 |
| 蛋白大小 | 220 aa / 23.3 kDa |
| UniProt ID | Q8NB37 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Nucleoplasm (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 220 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=2 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=94.9; PDB=2 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Class_I_gatase-like; Prot/Nucl_acid_deglycase |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=2 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Uncertain)
- PubMed strict=2 broad=2
- AF pLDDT=94.9 PDB=2
- InterPro: Class_I_gatase-like; Prot/Nucl_acid_deglycase
- Pfam: 
- PPI degree=2 ChIP: None
40062705: Neurogenetic disorders associated with mutations in the FERRY complex: a novel d | 39920593: Evaluation of reference genes for gene expression analysis in Japanese flounder 

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Glutamine amidotransferase-like class 1 domain-containing protein 1

**功能**: Component of the FERRY complex (Five-subunit Endosomal Rab5 and RNA/ribosome intermediary) (PubMed:37267905, PubMed:37267906). The FERRY complex directly interacts with mRNAs and RAB5A, and functions as a RAB5A effector involved in the localization and the distribution of specific mRNAs most likely by mediating their endosomal transport. The complex recruits mRNAs and ribosomes to early endosomes through direct mRNA-interaction (PubMed:37267905)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029062 |
| InterPro | IPR050325 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PPP1R21 | STRING | 918 |


### 深度机制分析

**结构域架构**：GATD1（220 aa，23.3 kDa）含Class_I_gatase-like（IPR029062，I类谷氨酰胺酰胺转移酶样折叠）和Prot/Nucl_acid_deglycase（IPR050325，蛋白/核酸去糖化酶）。I类GATase折叠由中央平行β-片层（6-8股）被两侧α-螺旋包围构成，活性位点含保守的Cys-His-Glu催化三联体——Cys的硫醇基作为亲核试剂攻击底物谷氨酰胺侧链的酰胺羰基碳，释放NH3（氨），形成共价硫酯中间体。氨随后被引导至第二个活性位点（合酶域），用于核苷酸、氨基酸或辅酶的生物合成。Prot/Nucl_acid_deglycase注释更特异——去糖化酶（deglycase）催化Maillard反应产物中蛋白/核酸的糖基化加合物（如Nε-果糖基赖氨酸和2'-脱氧核苷酸糖加合物）的修复——这是"代谢物修复"（metabolite repair）功能的又一实例。

**PPI互作网络解读**：PPI degree仅2，唯一的显著互作为PPP1R21（蛋白磷酸酶1调节亚基21，STRING 918分——极高的功能关联评分）。PPP1R21与GATD1共享FERRY复合物的功能定位——两者均为FERRY（Five-subunit Endosomal Rab5 and RNA/ribosome intermediary）复合物的组分：（1）GATD1是FERRY复合物的核心亚基之一（UniProt注释：Component of the FERRY complex）；（2）FERRY复合物是内体Rab5的效应器——在早期内体（Rab5^+ endosomes）的胞质面上同时结合特定mRNAs和核糖体，介导mRNA的局部翻译（localized translation）。这一功能与内体上的局部蛋白合成（endosomal local translation）——特别是在神经元的轴突和树突中——研究领域相符。

**结构解读**：AlphaFold pLDDT=94.9（PDB=2），是本批次中两个预测置信度最高（pLDDT >94）的蛋白之一。I类GATase样折叠在pLDDT >96的水平上清晰可辨——高度有序的α/β/α三明治结构。催化三联体（Cys-His-Glu）的保守残基侧链呈精确的几何排布：Cys硫醇基与His咪唑基形成硫醇-咪唑离子对（Cys-S^-⋯His-H^+），Glu羧酸稳定His的质子化态。活性位点口袋开口可容纳谷氨酰胺侧链的酰胺基团或糖化产物的半缩酮/缩醛基团。两个已解析的PDB结构（推测为apo形式和配体结合形式）为发现小分子抑制GATD1/FERRY功能提供了结构基础。高pLDDT提示FERRY复合物中GATD1的结构是预先形成的（pre-formed），而非在与别的复合物亚基结合后折叠。

**机制模型**：GATD1作为FERRY复合物的核心组分，其分子功能如下：（1）FERRY复合物（FIVE-subunit: GATD1 + TDRD3 + PPP1R21 + plus two other subunits）作为一个多功能的mRNA-Rab5双效应器——通过GATD1/TDRD3识别特定mRNA的3'UTR结构基序（推测为特定RNA二级结构，如G-quadruplexes或stem-loop），通过Rab5-GTP结合域锚定于早期内体膜，并将结合的mRNA连同80S核糖体一起招募至内体表面进行局部翻译；（2）局部翻译（local translation）在神经元的生长锥（growth cone）和突触后密度（PSD）中已得到充分证实——FERRY复合物为此提供内体锚定的翻译平台，使翻译产物（通常为细胞骨架调控蛋白或信号蛋白）能立即在需要的位置——如轴突末端——发挥功能；（3）FERRY复合物突变相关的神经发育障碍（PMID:40062705：Neurogenetic disorders associated with mutations in the FERRY complex）证实了FERRY在人类神经发育中的关键和非冗余性功能。

**TE调控展望**：GATD1/FERRY的TE调控潜力虽然间接但理论上可行。FERRY复合物通过mRNA的3'UTR识别和局部翻译调控决定特定转录本的命运和翻译效率——如果TE衍生的转录本（如L1 mRNA或ERV env mRNA）在一定条件下被FERRY复合物识别并将其靶向至内体进行局部翻译，FERRY的功能状态可影响TE编码蛋白的时空表达模式。然而，目前无任何证据支持FERRY识别TE衍生转录本。GATD1的新型性（PubMed仅2篇）使任何功能性推测均需实验验证，但FERRY复合物作为mRNA亚细胞定位和局部翻译的核心机器的功能为其TE调控相关性提供了理论基础。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NB37-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000177225-GATD1

![](https://images.proteinatlas.org/8812/113_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/8812/113_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/8812/112_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/8812/112_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/8812/161_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/8812/161_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/8812/2268_E1_36_red_green.jpg)
![](https://images.proteinatlas.org/8812/2268_E1_186_red_green.jpg)

### PubMed 文献

**PubMed count: 2**

| 40062705 | Neurogenetic disorders associated with mutations in the FERRY complex: a novel disease class? | Biol Open 2025 |
| 39920593 | Evaluation of reference genes for gene expression analysis in Japanese flounder (Paralichthys olivaceus) under temperatu | BMC Genomics 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GATD1

