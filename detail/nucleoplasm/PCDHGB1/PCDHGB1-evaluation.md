---
type: protein-evaluation
gene: "PCDHGB1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGB1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGB1 |
| 蛋白名称 | Protocadherin gamma-B1 |
| 蛋白大小 | 927 aa / 100.4 kDa |
| UniProt ID | Q9Y5G3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Focal adhesion sites; Midbody; Nucleoplasm; Plasma (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 927 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=2 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=74.9; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 6/10 | x3 | 18.0 | PPI degree=75 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
- Focal adhesion sites; Midbody; Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=2 broad=5
- AF pLDDT=74.9 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_C
- Pfam: Cadherin; Cadherin_2; Cadherin_C_2
- PPI degree=75 ChIP: None
37862219: Forebrain excitatory neuron-specific loss of Brpf1 attenuates excitatory synapti | 40343304: DNA methylation in peripheral blood leukocytes in late onset Alzheimer's disease

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin gamma-B1

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


### 深度机制分析

PCDHGB1是Protocadherin Gamma-B1亚家族成员，属于钙粘蛋白(Cadherin)超家族的成簇原钙粘蛋白(Clustered Protocadherin)分支。该蛋白长达927 aa(100.4 kDa)，含有6个串联的Cadherin-like_dom(IPR002126)胞外重复序列和C端Cadherin_C(IPR020894)结构域。每个Cadherin重复由约110个氨基酸组成希腊-钥匙β-折叠桶，6个重复排列成弯曲的棒状结构，整体通过Ca²⁺依赖的同嗜性结合介导细胞间粘附。pLDDT=74.9反映其重复结构域的柔性使整体预测有所下降。

在神经生物学中，成簇原钙粘蛋白的显著性在于其随机单等位基因(random monoallelic)表达模式——每个神经元从5号染色体上的PCDHG基因簇中随机选择表达一个或少数几个亚型，从而创造出极大的单细胞表面粘附多样性。这种多样性是神经突自避(neuronal self-avoidance)和自我/非自我识别(Self/non-self recognition)的分子基础。

HPA显示PCDHGB1定位于Focal adhesion sites、Midbody、Nucleoplasm和Plasma membrane(Approved)。核质定位对于这种经典的细胞粘附分子而言极不寻常。最可能的机制解释是：全长跨膜PCDHGB1经ADAM10/17金属蛋白酶在近膜区剪切(Shedding)释放胞外域后，剩余的C端胞内域(Ectodomain-ICD)通过γ-分泌酶进一步切割(Gamma-secretase processing)，释放的ICD片段随即可携入核质，类似Notch和E-cadherin的经典信号转导模式。

PPI互作网络完全由PCDHG蛋白家族内涵盖——PCDHGB2/3/4、PCDHGA11、PCDHGC3/4和PCDHB2等均为原钙粘蛋白的同嗜/异嗜互作伙伴。同时也观察到PCDH18(BioGRID)的非γ簇互作，其可能作为异嗜性地转移PCDHGB1信号的适配器。核内PCDHGB1-ICD的功能假设为：结合β-catenin或p120-catenin等经典钙粘蛋白的信号伙伴，调控Wnt靶基因启动子的转录激活，进而影响神经突的可塑性基因表达。PubMed仅2篇，核内信号功能是几乎未被探索的研究前沿。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5G3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000254221-PCDHGB1

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/76182/1702_A9_10_cr57eab563a7001_red_green.jpg)
![](https://images.proteinatlas.org/76182/1702_A9_14_cr57eab56ae70a5_red_green.jpg)

### PubMed 文献

**PubMed count: 5**

| 41240871 | Prenatal organophosphate ester exposure and epigenetic changes at birth: a characterization of the methylome in the ECHO | Environ Int 2025 |
| 40343304 | DNA methylation in peripheral blood leukocytes in late onset Alzheimer's disease. | J Alzheimers Dis Rep 2025 |
| 37862219 | Forebrain excitatory neuron-specific loss of Brpf1 attenuates excitatory synaptic transmission and impairs spatial and f | Neural Regen Res 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGB1

