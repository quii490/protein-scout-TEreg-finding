---
type: protein-evaluation
gene: "PRKAB2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PRKAB2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PRKAB2 |
| 蛋白名称 | 5'-AMP-activated protein kinase subunit beta-2 |
| 蛋白大小 | 272 aa / 30.3 kDa |
| UniProt ID | O43741 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 272 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=54 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=77.8; PDB=17 |
| 调控结构域 | 4/10 | x2 | 8.0 | AMPK1_CBM; ASC_dom; ASC_dom_sf |
| PPI | 8/10 | x3 | 24.0 | PPI degree=271 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **76.0/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=54 broad=105
- AF pLDDT=77.8 PDB=17
- InterPro: AMPK1_CBM; ASC_dom; ASC_dom_sf
- Pfam: AMPK1_CBM; AMPKBI
- PPI degree=271 ChIP: None
38884729: Human Genetics of Ventricular Septal Defect. | 38539429: Low PRKAB2 Expression Is Associated with Poor Outcomes in Pediatric Adrenocortic | 41612594: PRKAB2 as a tumor suppressor in renal cell carcinoma: inhibiting mitophagy via t

### 4. 总体评价
**76.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: 5'-AMP-activated protein kinase subunit beta-2

**功能**: Non-catalytic subunit of AMP-activated protein kinase (AMPK), an energy sensor protein kinase that plays a key role in regulating cellular energy metabolism. In response to reduction of intracellular ATP levels, AMPK activates energy-producing pathways and inhibits energy-consuming processes: inhibits protein, carbohydrate and lipid biosynthesis, as well as cell growth and proliferation. AMPK acts via direct phosphorylation of metabolic enzymes, and by longer-term effects via phosphorylation of 

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR032640 |
| InterPro | IPR006828 |
| InterPro | IPR037256 |
| InterPro | IPR050827 |
| InterPro | IPR013783 |
| InterPro | IPR014756 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PRKAG1 | STRING | 999 |
| PRKAG3 | STRING | 999 |
| PRKAA2 | STRING | 999 |
| PRKAA1 | STRING | 999 |
| PRKAG2 | STRING | 999 |
| PRKAB1 | STRING | 997 |
| STK11 | STRING | 976 |
| CAMKK2 | STRING | 975 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O43741-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000131791-PRKAB2

![](https://images.proteinatlas.org/44342/2253_B7_104_blue_red_green.jpg)
![](https://images.proteinatlas.org/44342/2253_B7_167_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000131791-PRKAB2

![](https://images.proteinatlas.org/44342/2253_B7_104_blue_red_green.jpg)
![](https://images.proteinatlas.org/44342/2253_B7_167_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000131791-PRKAB2

![](https://images.proteinatlas.org/44342/2253_B7_104_blue_red_green.jpg)
![](https://images.proteinatlas.org/44342/2253_B7_167_blue_red_green.jpg)

### 深度机制分析

**结构域架构与分子功能推断** PRKAB2是AMPK异源三聚体的非催化β亚基，包含三个核心结构域：AMPK1_CBM（糖原结合模块，InterPro: IPR032640）、ASC结构域（IPR006828）和ASC超家族折叠（IPR037256），同时被归类为AMPK β亚基家族（IPR050827）。AMPK1_CBM是PRKAB2功能标志——它是糖原结合结构域（GBD/CBM），直接感知细胞内糖原水平，将AMPK锚定到糖原颗粒上。ASC结构域介导与α催化亚基（PRKAA1/PRKAA2）和γ调节亚基（PRKAG1/PRKAG2/PRKAG3）的异源三聚体组装。272 aa（30.3 kDa）与该双结构域架构吻合。PDB=17个实验结构使这是五个蛋白中结构数据最丰富的，AF pLDDT=77.8与已知结构高度一致。

**PPI网络与信号通路解析** STRING网络是经典的AMPK核心复合物：PRKAG1（999）、PRKAG3（999）、PRKAA2（999）、PRKAA1（999）、PRKAG2（999）均为AMPK的α/γ亚基，形成标准的αβγ异源三聚体。PRKAB1（997）是β1旁系同源物。上游激酶STK11/LKB1（976）和CAMKK2（975）的高分直接连接到AMPK激活信号——LKB1通过磷酸化α亚基的T172残基在能量应激时激活AMPK，而CAMKK2在钙信号下提供替代激活路径。PPI度高达271反映了AMPK作为核心代谢传感器在数百个下游信号事件中的枢纽地位。PRKAB2的特异性体现在其糖原结合能力——不同于β1亚基，β2亚基的CBM对糖原的亲和力和组织分布有所不同。

**结构解读** 17个PDB结构中，AMPK全酶复合物结构提供了原子级别的理解。β2亚基的C端ASC结构域通过假激酶折叠与α和γ亚基形成紧凑的异源三聚体核心。N端CBM（约残基1-90）通过柔性连接区与ASC结构域相连，形成一个可变构象的糖原感知模块。pLDDT=77.8中较低的置信区域正好对应CBM-ASC连接区，反映了糖原结合时的构象变化需求。γ亚基的CBS（胱硫醚β合酶）重复形成腺嘌呤核苷酸结合位点，而β2的ASC结构域正位于该位点上方，机械性地将ATP/AMP/ADP结合状态传递给α激酶域的T-loop磷酸化状态。

**分子机制模型** PRKAB2在AMPK能量感知中扮演"糖原哨兵"和"信号整合器"双重角色。当细胞内糖原充足时，PRKAB2的CBM结构域将AMPK复合物束缚在糖原颗粒上，使AMPK处于低活性状态（"糖原满足"信号）。当糖原耗尽，PRKAB2释放AMPK进入胞质，此时γ亚基感知升高的AMP/ATP比例，构象变化通过β2的ASC结构域传导至α亚基，触发LKB1/CAMKK2对T172的磷酸化激活。活化的AMPK磷酸化数百个下游靶标以抑制合成代谢并促进分解代谢。核质定位（HPA Approved级别）具有特殊意义——AMPK可直接磷酸化核内转录因子和转录共激活因子（如PGC-1α、FOXO、SREBP1c），协调代谢基因的转录重编程。PRKAB2的核内定位可能使AMPK在核内维持局部活性，不依赖全细胞AMP波动。

**研究与治疗意义** PRKAB2在肾细胞癌中的抑癌作用（PubMed: 41612594）通过抑制线粒体自噬实现，提示β2亚基的选择性调控可能提供AMPK靶向治疗的新窗口——避免α亚基的广泛代谢效应。小儿肾上腺皮质肿瘤中PRKAB2低表达与不良预后相关（PubMed: 38539429），进一步支持β2作为癌症代谢生物标志物的价值。心室间隔缺损的遗传学关联（PubMed: 38884729）揭示了AMPK β2在心脏发育中的特异角色，可能通过转录因子FOXO/PGC-1α轴调控心肌细胞分化。未来研究方向包括：开发β2-CBM选择性的小分子调节剂以独立调控AMPK的糖原响应而不影响全局AMPK活性；解析PRKAB2核内伙伴组——哪些转录因子和染色质修饰酶是AMPK在细胞核内的直接靶标？

### PubMed 文献

**PubMed count: 105**

| 42338208 | [Revealing the role of Hippo pathway in osteoarthritis based on transcriptomic analysis]. | Zhongguo Gu Shang 2026 |
| 42180867 | A novel programmed-cell-death-related prognostic risk model for cervical cancer based on mitochondrial genes. | Transl Cancer Res 2026 |
| 42001553 | Human genetics of HIV infection. | Curr Opin Virol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PRKAB2

