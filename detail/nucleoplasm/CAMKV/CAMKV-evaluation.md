---
type: protein-evaluation
gene: "CAMKV"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CAMKV 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CAMKV |
| 蛋白名称 | CaM kinase-like vesicle-associated protein |
| 蛋白大小 | 501 aa / 54.4 kDa |
| UniProt ID | Q8NCB2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytokinetic bridge; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 501 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=17 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=70.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Kinase-like_dom_sf; Prot_kinase_dom |
| PPI | 7/10 | x3 | 21.0 | PPI degree=108 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
- HPA: Cytokinetic bridge; Nucleoplasm (Approved)
- PubMed: strict=17, broad=47
- AF pLDDT: 70.6 / PDB: 0
- InterPro: Kinase-like_dom_sf; Prot_kinase_dom
- Pfam: Pkinase
- PPI degree=108 / ChIP: None
41001472: The genetic architecture of fibromyalgia across 2.5 million individuals. | 38634529: Paraneoplastic Calmodulin Kinase-Like Vesicle-Associated Protein (CAMKV) Autoimm | 41088254: Protein fingerprints of brain-derived extracellular vesicles predict types of ta

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: CaM kinase-like vesicle-associated protein

**功能**: Does not appear to have detectable kinase activity

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011009 |
| InterPro | IPR000719 |
| Pfam | PF00069 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

CAMKV是CaM Kinase-like Vesicle-associated Protein，属于钙/钙调蛋白依赖性蛋白激酶(CaMK)家族的非典型成员。其结构域包含经典的Kinase-like_dom_sf(IPR011009)折叠和Prot_kinase_dom(IPR000719)，但与所有其他CaMK超家族成员的一个根本区别在于：CAMKV已被证实缺乏可检测的激酶催化活性(UniProt: "Does not appear to have detectable kinase activity")。催化失活的分子基础可能是催化环(HRD基序)、镁结合环(DFG基序)或激活环中的关键残基发生非保守替换，使得ATP的γ-磷酸无法被转移。

pLDDT仅70.6，是这批核蛋白中结构预测置信度最低的蛋白之一，但其较长的柔性区域(501 aa)暗示一个可能的结构模型：CAMKV通过催化失活的伪激酶结构域作为CaM诱导的蛋白-蛋白互作支架，而非行使磷酸化酶活性。在细胞质中，CAMKV依赖Ca²⁺/CaM信号被招募至囊泡膜，参与神经递质/神经肽的囊泡运输与分泌调节。

CAMKV的HPA定位为Cytokinetic bridge和Nucleoplasm(Approved)。胞质分裂桥中的定位与已知的CaMK家族在细胞周期中的功能一致——CaMKII在末期参与肌动蛋白收缩环的调节。然而，核质定位提示CAMKV可能具有独立于囊泡运输的核功能。PPI网络揭示了几个关键线索：TCEA2(转录延伸因子A2)是RNA聚合酶II延伸复合体的组成部分；UBTF(上游结合转录因子)是RNA聚合酶I的转录因子，负责rRNA基因的转录调控；NUFIP1(核FMRP互作蛋白1)与RNA代谢和mRNA的核质穿梭有关。

综合来看，CAMKV在核质中的机制模型为：CAMKV作为CaM诱导的骨架蛋白在Ca²⁺内流时发生构象变化，通过其伪激酶结构域的特异性PPI界面结合TCEA2、UBTF或NUFIP1，间接调控转录延伸效率。这种"催化死亡、变构支架"的功能模式已在多个伪激酶(如HER3、STRADα)中被证实是进化中的保守机制。值得注意的是，CAMKV自身抗体已被报道为副肿瘤性神经综合征的致病因子(PMID:38634529)，且其在纤维肌痛的GWAS中被鉴定为风险位点(PMID:41001472)，提示其在神经-免疫信号中具有关键的生物医学重要性。PubMed仅17篇，亟需CRISPR敲除功能研究来验证上述假设模型。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NCB2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164076-CAMKV

![](https://images.proteinatlas.org/7656/1032_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/7656/1032_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/7656/1222_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/7656/1222_D8_2_red_green.jpg)

### PubMed 文献

**PubMed count: 47**

| 42218517 | Integrative single-cell and bulk transcriptomics define cell death patterns and ZDHHC22 in gastric cancer progression. | BMC Med Genomics 2026 |
| 42171443 | Long-Term Outcomes in Stiff Person Spectrum Disorder. | Eur J Neurol 2026 |
| 41476076 | Clinical course, risk factors and mitigating strategies for Immune effector cell-associated late onset neurotoxicities a | Blood Cancer J 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CAMKV

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TCEA2 | physical | Stelzl U (2005) |
| COPS5 | physical | Bennett EJ (2010) |
| APP | physical | Olah J (2011) |
| HSP90AA1 | physical | Taipale M (2012) |
| ARMC1 | physical | Huttlin EL (2015) |
| HAX1 | physical | Huttlin EL (2015) |
| NUFIP1 | physical | Huttlin EL (2015) |
| DGUOK | physical | Huttlin EL (2015) |
| DNAAF2 | physical | Huttlin EL (2015) |
| UBTF | physical | Huttlin EL (2017) |

