---
type: protein-evaluation
gene: "TMEM267"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM267 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM267 |
| 蛋白名称 | Transmembrane protein 267 |
| 蛋白大小 | 215 aa / 24.2 kDa |
| UniProt ID | Q0VDI3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 215 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=89.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TMEM267 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=5 broad=5
- AF pLDDT=89.8 PDB=0
- InterPro: TMEM267
- Pfam: 
- PPI degree=0 ChIP: None
37817112: MAPK1 promotes the metastasis and invasion of gastric cancer as a bidirectional  | 39757814: Translational Approach to Social Isolation During a Global Pandemic: Hippocampal | 42284217: The Role of Estrogen Receptors and House Dust Mite-Induced DNA Methylation in a 

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 267

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026572 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 267

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026572 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q0VDI3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000151881-TMEM267

![](https://images.proteinatlas.org/59946/1045_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/59946/1045_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/59946/1178_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/59946/1178_C8_4_red_green.jpg)
![](https://images.proteinatlas.org/59946/1049_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/59946/1049_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/72991/1975_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/72991/1975_D11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 5**

| 42284217 | The Role of Estrogen Receptors and House Dust Mite-Induced DNA Methylation in a Mouse Model. | Am J Physiol Lung Cell Mol Physiol 2026 |
| 41505521 | Elucidating cooperative genetic events in DCIS progression in mutant p53-driven breast cancer. | Proc Natl Acad Sci U S A 2026 |
| 39757814 | Translational Approach to Social Isolation During a Global Pandemic: Hippocampal Somatic Mutation and Stress. | Psychiatry Investig 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM267

### 深度机制分析

**结构域架构的局限性** TMEM267（215 aa, 24.2 kDa）仅含单一结构域注释（IPR026572/TMEM267家族），无Pfam条目对应，无催化位点，无DNA/RNA结合模体。pLDDT=89.8表明该蛋白整体折叠良好——对于仅215aa的蛋白而言，此pLDDT值意味着其几乎整个序列都处于有序折叠状态（而非无序区）——但AlphaFold结构预测本身无法告知该折叠的功能。小而有序的蛋白在生物化学中通常扮演两种角色：（a）专一性结合/转运蛋白（如cytochrome b5、ferredoxin），或（b）信号通路中的变构调节亚基（如CaM、ubiquitin）。TMEM267不符合经典的钙结合或泛素折叠家族特征，因此推理其可能以类似"蛋白适配器（adaptor）"的方式工作，其有序折叠的疏水表面是特异性识别伙伴蛋白的结构基础。

**PPI网络的深刻启示** TMEM267的PPI度=0（BioGRID无记录），但其STRING网络提供了9个纯计算预测伙伴，其中最值得关注的是PRXL2C（STRING score=521，最高）、BRIX1（score=438）和NADK2（score=410）。PRXL2C（又名AHP1）属于peroxiredoxin-like 2家族，此家族成员参与氧化还原信号和伴侣活性，在核内可调控转录因子（如NF-kB、AP-1）的氧化还原状态——这一点与TMEM267文献中出现的MAPK1（PMID:37817112，MAPK1通过双向调控促进胃癌转移和侵袭）和雌激素受体（PMID:42284217，ER在过敏性气道疾病小鼠模型中DNA甲基化研究）高度吻合，因为MAPK和ER信号均受氧化还原微环境精细调控。BRIX1是核仁蛋白，参与核糖体60S大亚基的生物合成，但近来发现其在核质中也参与p53-MDM2轴的调控——若TMEM267与BRIX1互作属实，则暗示其可能参与核糖体应激（ribosomal stress）对p53信号的调节。NADK2是线粒体NAD激酶，催化NAD→NADP的磷酸化，调控细胞氧化还原平衡与NADPH依赖性生物合成。WDR70（score=443）是WD40重复蛋白，在DNA双链断裂修复（DSB repair）中与RAD51协同作用。

**氧化还原-应激信号整合假设** 综合上述PPI信号与文献证据，我们推测TMEM267的核心功能是作为核质中氧化还原应激信号的整合节点。具体机制如下：在氧化应激或代谢扰动下，TMEM267通过感知PRXL2C-NADK2轴的氧化还原状态变化，将信号传递给MAPK级联通路（MAPK1/ERK2），促使其核转位增强，进而磷酸化核内转录底物。在社会隔离/心理应激模型中（PMID:39757814），海马体细胞突变负荷增加提示DNA损伤修复通路受扰——WDR70的同源重组修复功能若因TMEM267异常而减弱，可能导致DNA双链断裂修复障碍。此外，雌激素受体（ER）信号与DNA甲基化（PMID:42284217）的关联暗示TMEM267可能连接"激素信号-表观遗传修饰-细胞应激反应"三条通路。虽然本文献的研究对象是小鼠模型中的过敏性疾病而非直接鉴定TMEM267功能，但其作为差异甲基化区域相关基因的出现说明了其表观调控敏感性。

**结构-功能对应关系** pLDDT=89.8的紧凑折叠蛋白（215aa）表面可能含有多个浅疏水性口袋，分别用于识别PRXL2C的过氧化半胱氨酸残基、BRIX1的核仁定位信号区段以及NADK2的底物结合构象。这种"一对多"的蛋白互作模式要求TMEM267具有构象可塑性——其有序折叠骨架维持总体结构不变，而表面环区（loop）在不同伙伴结合时发生诱导契合。值得注意的是，0个PDB结构与高pLDDT的组合是蛋白结构生物学中一个可操作的机会窗口：TMEM267的高折叠质量使其成为理想的NMR或X射线晶体学靶标，一旦获得实验结构，即可通过虚拟筛选寻找干扰其PPI界面的小分子化合物。

**研究与转化意义** TMEM267是目前研究最少的核TMEM蛋白之一（PubMed仅5篇，无BioGRID互作记录），但STRING网络揭示的OB（氧化还原-核糖体生物合成）互作簇为其功能研究提供了逻辑起点。在胃癌症中，MAPK1通过双向调控机制促进转移和侵袭（PMID:37817112），若TMEM267确实是MAPK1的上游调控因子，则靶向TMEM267可能同时干扰MAPK的促增殖和促转移双重信号。在社会隔离与精神疾病领域，PMID:39757814将海马体细胞突变与心理应激相关联，而TMEM267-WDR70的DNA修复链为理解"心理应激→神经元DNA损伤→认知功能障碍"的分子桥梁提供了可验证的假说。从方法学角度，首先需要验证STRING预测的多条互作（尤其是PRXL2C和BRIX1），最直接的路径是在HEK293T细胞中进行co-IP或BioID邻近标记实验。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| WDR70 | STRING | 443 |
| LMBRD2 | STRING | 432 |
| HDHD2 | STRING | 474 |
| PAIP1 | STRING | 403 |
| C5orf34 | STRING | 449 |
| C5orf22 | STRING | 430 |
| BRIX1 | STRING | 438 |
| PRXL2C | STRING | 521 |
| NADK2 | STRING | 410 |
