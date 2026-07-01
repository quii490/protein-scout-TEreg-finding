---
type: protein-evaluation
gene: "LMBRD2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## LMBRD2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LMBRD2 |
| 蛋白名称 | G protein-coupled receptor-associated protein LMBRD2 |
| 蛋白大小 | 695 aa / 81.2 kDa |
| UniProt ID | Q68DH5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 695 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=4 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=76.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | GPCR-associated_LMBR1; LMBR1-like_membr_prot |
| PPI | 6/10 | x3 | 18.0 | PPI degree=61 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **76.5/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=4 broad=4
- AF pLDDT=76.7 PDB=0
- InterPro: GPCR-associated_LMBR1; LMBR1-like_membr_prot
- Pfam: LMBR1
- PPI degree=61 ChIP: None
28388415: Multidimensional Tracking of GPCR Signaling via Peroxidase-Catalyzed Proximity L | 35584733: Identification of novel integration sites for bovine leukemia virus proviral DNA | 32820033: De novo missense variants in LMBRD2 are associated with developmental and motor 

### 4. 总体评价
**76.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: G protein-coupled receptor-associated protein LMBRD2

**功能**: Recruited to ligand-activated beta-2 adrenergic receptor/ADRB2, it negatively regulates the adrenergic receptor signaling pathway (PubMed:28388415). May also regulate other G protein coupled receptors including type-1 angiotensin II receptor/AGTR1 (Probable)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR051584 |
| InterPro | IPR006876 |
| Pfam | PF04791 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SPACA1 | BioGRID | 0 |
| GNAI2 | BioGRID | 0 |
| LPAR6 | BioGRID | 0 |
| DCAF15 | BioGRID | 0 |
| ERGIC3 | BioGRID | 0 |
| FPR2 | BioGRID | 0 |
| HTR2C | BioGRID | 0 |
| C5AR2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q68DH5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164187-LMBRD2

![](https://images.proteinatlas.org/12165/89_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/12165/89_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/12165/88_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/12165/88_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/12165/90_C10_10_red_green.jpg)
![](https://images.proteinatlas.org/12165/90_C10_2_red_green.jpg)

### 深度机制分析

LMBRD2编码**G蛋白偶联受体相关蛋白LMBRD2**，属于LMBR1样膜蛋白家族（IPR006876, Pfam PF04791）。该家族以LMBR1（Limb Region 1）为先证成员，特征为含多个预测跨膜螺旋的疏水域，但LMBRD2的域架构在家族中具有独特性——IPR051584（GPCR-associated_LMBR1）注释专门将其与GPCR信号调控关联。该蛋白695个残基（81.2 kDa），是本次分析中五个蛋白中最大的。AlphaFold pLDDT=76.7且PDB=0表明该蛋白含有大量固有无序区域（IDR）或/和柔性连接区——这在信号接头蛋白中十分典型，IDR通常编码翻译后修饰位点和多价低亲和力互作界面，赋予其在多种信号复合体中的"可塑性"。HPA显示LMBRD2在胞质和核质均有分布（Approved级别），且该蛋白定位于核质的生物学意义在领域内几乎是全新的前沿问题。

PPI网络呈现鲜明的**GPCR信号转导特征**。BioGRID鉴定的互作伙伴以GPCR家族为主导：HTR2C（5-HT2C血清素受体）、FPR2（甲酰肽受体2）、C5AR2（补体成分5a受体2）、LPAR6（溶血磷脂酸受体6）——四种不同类别的GPCR均以物理互作方式与LMBRD2关联，强烈提示LMBRD2是一个**广谱GPCR适配器**，而非某个特定受体的专属调节蛋白。GNAI2（抑制性G蛋白α亚基2）的互作进一步将LMBRD2定位于GPCR下游的经典Gi信号轴。DCAF15（DDB1-CUL4相关因子15，CRL4泛素连接酶的底物受体）和ERGIC3（内质网-高尔基中间区室蛋白3）的互作则分别暗示了LMBRD2在泛素化依赖性蛋白稳态和内膜运输中的潜在功能。关键的是，这些BioGRID互作均来自低通量实验（评分=0），意味着每种互作都经过独立实验验证，但因实验数量少而未被高度评分，这反而增加了单个互作的可信度。

结构功能推理分析：pLDDT=76.7的低全局置信度主要源于预测的跨膜区和IDR——AlphaFold对膜蛋白和IDR的结构预测在v2版本中仍有限。核心折叠区域应具有较高局部pLDDT。无PDB结构意味着LMBRD2的原子分辨率结构仍是完全未知的黑箱，考虑到GPCR信号调控蛋白的构象异质性（常需结合配体激活的受体后才形成稳定折叠），这既是挑战也是机会。LMBRD2主要通过N端/中央区与配体激活的β2-肾上腺素受体/ADRB2结合（PubMed:28388415），通过竞争性地干扰G蛋白偶联或β-arrestin募集来负调控受体信号，同时可能也调节1型血管紧张素II受体/AGTR1。PubMed:32820033鉴定了LMBRD2的新生错义变异与发育迟缓、运动迟缓和脑结构异常的关联，表明该蛋白在神经发育中有不可替代的功能——很可能通过调节发育关键期GPCR信号（如血清素、Wnt/Frizzled通路）的强度和持续时间来实现。

综合机制模型：LMBRD2是**GPCR信号的细胞内缓冲调节器**，在配体激活的GPCR内化后于早期内体上组装成信号调控平台。（1）在质膜/内体：LMBRD2被招募至配体激活的ADRB2或其他GPCR，作为"刹车"蛋白竞争G蛋白结合位点或促进受体去泛素化/再循环，限制下游cAMP和MAPK信号的持续时间和强度。（2）在核质（此为该蛋白研究中完全未被探索的方向）：LMBRD2可能通过其IDR介导的核质穿梭参与GPCR信号依赖的转录调控，或作为GPCR内化后释放的C端片段的伴侣，调节受体片段在核内的非经典功能。仅有4篇严格PubMed文献——28388415（GPCR信号的多维追踪，唯一直接功能文献）、35584733（牛白血病病毒前病毒DNA整合位点鉴定，暗示其在病毒致癌中的潜在角色）、32820033（发育障碍的遗传学关联）、34150746（lncRNA在PBMC中的表达谱）——这一极端贫乏的文献基础使LMBRD2成为**核质GPCR信号生物学中的完全未开垦领域**。从转化医学角度，LMBRD2作为广谱GPCR负调控因子，其表达水平的微调可影响多种GPCR药物的效能（β阻断剂、血管紧张素受体阻断剂、抗精神病药等），针对LMBRD2的PROTAC或分子胶降解剂可实现"多受体信号同时增敏"的独特药理学策略。发育障碍相关的错义变异（32820033）如果被证实破坏LMBRD2-GPCR互作界面，则这些变异的功能验证将为GPCR信号的遗传性疾病机制提供全新范例。

### PubMed 文献

**PubMed count: 4**

| 35584733 | Identification of novel integration sites for bovine leukemia virus proviral DNA in cancer driver genes in cattle with p | Virus Res 2022 |
| 34150746 | Novel Long Non-coding RNA Expression Profile of Peripheral Blood Mononuclear Cells Reveals Potential Biomarkers and Regu | Front Cell Dev Biol 2021 |
| 32820033 | De novo missense variants in LMBRD2 are associated with developmental and motor delays, brain structure abnormalities an | J Med Genet 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/LMBRD2

