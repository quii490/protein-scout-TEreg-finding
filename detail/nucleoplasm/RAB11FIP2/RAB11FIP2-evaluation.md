---
type: protein-evaluation
gene: "RAB11FIP2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RAB11FIP2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RAB11FIP2 |
| 蛋白名称 | Rab11 family-interacting protein 2 |
| 蛋白大小 | 512 aa / 58.3 kDa |
| UniProt ID | Q7L804 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm; Vesicles (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 512 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=37 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=61.5; PDB=6 |
| 调控结构域 | 4/10 | ×2 | 8.0 | C2_dom; C2_domain_sf; FIP-RBD_C_sf |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=81 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Vesicles (Supported)
- PubMed strict=37 broad=69
- AF pLDDT=61.5 PDB=6
- InterPro: C2_dom; C2_domain_sf; FIP-RBD_C_sf
- Pfam: C2; RBD-FIP
- PPI degree=81 ChIP: None
33937069: The LncRNA CASC11 Promotes Colorectal Cancer Cell Proliferation and Migration by | 37788908: Peptide derived from SLAMF1 prevents TLR4-mediated inflammation in vitro and in  | 30622149: Rab11FIP proteins link endocytic recycling vesicles for cytoskeletal transport a

### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

RAB11FIP2（Rab11 family-interacting protein 2）是512个氨基酸的RAB11效应蛋白，属于RAB11FIP家族（FIP1-FIP5）的核心成员。其多结构域架构体现为：一个C端C2结构域（IPR000008/C2_dom）负责磷脂结合，中间区域的螺旋束形成Rab11结合域（FIP-RBD_C_sf, IPR037245），N端则富含预测的内在无序区。C2结构域是经典的Ca2+依赖性磷脂结合模块，采用β-三明治折叠，含3个Ca2+配位环——但RAB11FIP2的C2结构域进化出优先识别磷脂酰肌醇-3,4,5-三磷酸（PtdInsP3）和磷脂酸（PA）而非Ca2+依赖性膜招募。AlphaFold预测pLDDT为61.5，较低的置信度主要源于N端大的IDR区段——这些柔性区域可能作为分子海绵招募多价互作伙伴。

Rab11结合域的RBD-FIP（PF09457）采用独特的全α-螺旋折叠，以不同于经典Rab效应蛋白（如Rabaptin、Rabenosyn）的方式识别Rab11。这种"非经典Rab效应蛋白"结合模式赋予RAB11FIP2在回收内体（recycling endosome）膜上形成功能性hub的能力。PPI网络（degree=81）中与RAB11FIP3（STRING=965）和RAB11FIP5（STRING=953）的强互作暗示FIP蛋白在回收内体表面形成动态的异源寡聚体——不同FIP蛋白的组合决定了回收膜泡的靶向目的地（质膜vs高尔基体vs胞内特定区域）。

HPA Supported的核质定位（Nucleoplasm; Vesicles）是该蛋白最令人困惑的特征——作为一个经典的胞质膜运输蛋白，其在核质中的存在是如何实现的？可能机制包括：（1）RAB11FIP2的IDR区域含有不被经典算法识别的核定位信号；（2）与MYO5B/REPS1等马达蛋白的互作使其沿细胞骨架被主动运输至核周，随后通过核孔扩散入核；（3）细胞周期依赖性的核膜破裂-重建过程中残留在核内。核内的RAB11FIP2可能参与核膜处回收内体-核孔复合体接触位点的形成，或调节胰岛素颗粒的分泌——这些过程在有丝分裂后的核膜重建中至关重要。

最新发表的关键发现——GTPase Rab11b和效应因子Rab11-FIP2促进NLRP3炎症小体在priming阶段的蛋白质稳定性（PMID:41882227）——揭示了RAB11FIP2在先天免疫中的全新功能维度。RAB11FIP2通过防止蛋白酶体降解维持NLRP3蛋白水平，这一功能可能与Vesicles>Nucleoplasm的定位动态变化相关。从TE调控角度来看，虽然RAB11FIP2本身为非经典候选，但其作为膜运输-先天免疫-核质的连接枢纽，可能间接影响CGAS-STING通路对逆转录转座子来源胞质DNA的感知——这是TE调控研究中一个极富前景的间接作用模式。

**蛋白全称**: Rab11 family-interacting protein 2

**功能**: A Rab11 effector binding preferentially phosphatidylinositol 3,4,5-trisphosphate (PtdInsP3) and phosphatidic acid (PA) and acting in the regulation of the transport of vesicles from the endosomal recycling compartment (ERC) to the plasma membrane. Involved in insulin granule exocytosis. Also involved in receptor-mediated endocytosis and membrane trafficking of recycling endosomes, probably originating from clathrin-coated vesicles. Required in a complex with MYO5B and RAB11 for the transport of 

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000008 |
| InterPro | IPR035892 |
| InterPro | IPR037245 |
| InterPro | IPR037789 |
| InterPro | IPR019018 |
| Pfam | PF00168 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RAB11FIP3 | STRING | 965 |
| RAB11FIP5 | STRING | 953 |
| EHD3 | STRING | 879 |
| REPS1 | STRING | 821 |
| CXCR2 | BioGRID | 1 |
| RAB11FIP2 | BioGRID | 1 |
| YWHAG | BioGRID | 1 |
| ITSN1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q7L804-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000107560-RAB11FIP2

![](https://images.proteinatlas.org/37726/436_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/436_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/521_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/521_C2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/442_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/442_C2_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000107560-RAB11FIP2

![](https://images.proteinatlas.org/37726/436_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/436_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/521_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/521_C2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/442_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/442_C2_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000107560-RAB11FIP2

![](https://images.proteinatlas.org/37726/436_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/436_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/521_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/521_C2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/442_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37726/442_C2_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 69**

| 41882227 | GTPase Rab11b and effector Rab11-FIP2 promote NLRP3 stability during inflammasome priming. | EMBO J 2026 |
| 40004102 | Meta-Analysis of QTL Mapping and GWAS Reveal Candidate Genes for Heat Tolerance in Small Yellow Croaker, Larimichthys po | Int J Mol Sci 2025 |
| 39868462 | Breast Cancer-Derived Extracellular Vesicles Modulate the Cytoplasmic and Cytoskeletal Dynamics of Blood-Brain Barrier E | J Extracell Vesicles 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RAB11FIP2

