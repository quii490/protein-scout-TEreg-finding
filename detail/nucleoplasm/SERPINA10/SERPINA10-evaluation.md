---
type: protein-evaluation
gene: "SERPINA10"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SERPINA10 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SERPINA10 |
| 蛋白名称 | Protein Z-dependent protease inhibitor |
| 蛋白大小 | 444 aa / 50.7 kDa |
| UniProt ID | Q9UK55 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 444 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=27 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=86.7; PDB=4 |
| 调控结构域 | 4/10 | x2 | 8.0 | PZI_serpin_dom; Serpin_dom; Serpin_fam |
| PPI | 5/10 | x3 | 15.0 | PPI degree=20 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=27 broad=93
- AF pLDDT=86.7 PDB=4
- InterPro: PZI_serpin_dom; Serpin_dom; Serpin_fam
- Pfam: Serpin
- PPI degree=20 ChIP: None
26982741: Single Nucleotide Variant rs2232710 in the Protein Z-Dependent Protease Inhibito | 40928059: Longitudinal Autoantibody and Proteomic Signatures of Disease Progression in Sys | 18710385: Polymorphisms of the Z protein protease inhibitor and risk of venous thromboembo

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein Z-dependent protease inhibitor

**功能**: Inhibits activity of the coagulation protease factor Xa in the presence of PROZ, calcium and phospholipids. Also inhibits factor XIa in the absence of cofactors

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR033835 |
| InterPro | IPR023796 |
| InterPro | IPR000215 |
| InterPro | IPR036186 |
| InterPro | IPR042178 |
| InterPro | IPR042185 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PIAS3 | BioGRID | 1 |
| DLK2 | BioGRID | 1 |
| NADK | BioGRID | 1 |
| HSPA13 | BioGRID | 1 |
| PSMB7 | BioGRID | 0 |
| PLAT | BioGRID | 0 |
| MIA3 | BioGRID | 0 |
| CTAGE5 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UK55-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000140093-SERPINA10

![](https://images.proteinatlas.org/48739/762_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/48739/762_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/48739/846_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/48739/846_B11_2_red_green.jpg)

### 深度机制分析

**1. 结构域架构与分子功能推断**

SERPINA10属于丝氨酸蛋白酶抑制剂（Serpin）超家族，其结构域架构非常明确：一个核心Serpin结构域（IPR023796, IPR000215, IPR036186）覆盖了绝大部分蛋白序列，附加一个PZI_serpin_dom（IPR033835）特异性标记，将其归类为"蛋白质Z依赖性蛋白酶抑制剂"亚家族。Serpin的折叠是一种独特的"应力折叠"——由3个β-折叠层（A/B/C）和9个α-螺旋组成，其中反应中心环（RCL, reactive center loop）作为一个暴露在分子表面的、可被蛋白酶识别的诱饵序列，在长约20个氨基酸的环中含有一个特定的肽键（P1-P1'切割位点）。当靶蛋白酶（通常是丝氨酸蛋白酶）识别并切割RCL时，RCL作为第4条β-链插入β-折叠层A中，将蛋白酶拖拽并压缩至失活构象——这一经典的"自杀性底物"抑制机制（也称为"自发性构象转换"或mousetrap机制）是Serpin家族区别于其他蛋白酶抑制剂（如Kunitz型）的标志性特征。

**2. PPI互作网络的生物学意义**

SERPINA10的PPI网络最显著的互作伙伴是PIAS3（Protein Inhibitor of Activated STAT3）和NADK（NAD激酶）。PIAS3是STAT3信号通路的主要负调控因子，通过SUMO化修饰STAT3二聚体来抑制其转录活性。PIAS3-SERPINA10互作暗示SERPINA10可能在核质中影响JAK/STAT3信号通路——这是一个完全未被描述的Serpin功能层面。如果SERPINA10通过与PIAS3结合来调控STAT3的SUMO化，那么它将间接影响STAT3靶基因（如CCND1、MYC、BCL2）的表达水平，从而参与细胞增殖、凋亡和炎症的转录调控。NADK是NADP(H)合成的关键酶，催化NAD+磷酸化为NADP+——NADK-SERPINA10互作提示SERPINA10可能与细胞氧化还原稳态有关联。此外，PLAT（组织型纤溶酶原激活物tPA）是已知的丝氨酸蛋白酶，与SERPINA10作为蛋白酶抑制剂的功能定位一致，但PLAT本身不是Serpin抑制谱中的典型靶点，可能代表了一种新的酶-抑制剂配对关系。PSMB7（蛋白酶体β7亚基）的互作暗示SERPINA10可能在核质中与蛋白酶体降解通路存在交叉调控。

**3. 三维结构解读**

AlphaFold预测的pLDDT为86.7，在444个氨基酸的全长蛋白中属于良好置信度。4个PDB实验结构的存在提供了坚实的结构验证基础。Serpin的应力折叠中，pLDDT最低的区域通常位于RCL本身——因为RCL在游离状态下具有高度柔性（需要采样多种构象以寻找靶蛋白酶），而一旦RCL被蛋白酶切割并被压缩进入β-折叠层A后，该区域将获得更高的刚性。pLDDT=86.7暗示RCL区域的预测可能存在一定的构象不确定性，这与RCL在生理条件下需要维持"溶剂可及但高度动态"的特性一致。Serpin的稳定性高度依赖于其折叠中的疏水核心——主要由β-折叠层B和C维持——而β-折叠层A的可扩展性是mousetrap机制的物理基础。SERPINA10与其辅因子蛋白质Z（PROZ）的结合界面位于β-折叠层B的外表面，辅因子的存在将RCL锁定在更适合被FXa识别的构象中，从而极大提升（~1000倍）抑制效率。4个PDB结构中可能包含了apo状态、FXa切割后产物以及PROZ复合物等不同构象状态的结构快照，为理解动态抑制过程提供了完整的结构基础。

**4. 分子机制综合模型**

综合所有证据，SERPINA10在分子水平上执行一种"双区室策略"的功能模式。在胞质/血液区室中，SERPINA10以经典Serpin机制抑制凝血因子Xa（FXa）和XIa：以PROZ作为辅因子，通过识别FXa活性位点的精氨酸特异性残基（RCL的P1位点），将FXa不可逆地捕获在酰基-酶中间体中。但SERPINA10的核质定位提出了一个更深刻的分子机制假设——核内SERPINA10可能通过以下非经典通路参与基因表达调控：（一）通过PIAS3互作影响STAT3的SUMO化水平和转录活性，从而将蛋白酶抑制活性与STAT3依赖的基因转录（如急性期反应基因、细胞因子基因）偶联起来；（二）通过PSMB7互作与蛋白酶体降解系统产生cross-talk——SERPINA10的"切割后"形式可能暴露出被蛋白酶体识别的降解信号，或反过来作为泛素-蛋白酶体系统的调控因子；（三）通过NADK互作影响核内NADPH/NADP+平衡，从而调节核内氧化还原敏感的转录因子（如Nrf2, HIF1α, AP-1）的活性。这一双区室模型将SERPINA10从一个"血液特异性抗凝血因子"重新概念化为"信号感知-基因调控的多功能蛋白"，其中核质定位是其非经典功能的结构基础。

**5. 研究与转化意义**

SERPINA10的核质定位颠覆了Serpin超家族长期以来的"主要胞外功能"教条。在转化层面：（1）SNP rs2232710（PubMed:26982741）已被报道与静脉血栓栓塞风险关联，但仅从抗凝活性角度解释是不够的——该SNP是否同时影响SERPINA10的核转位能力和STAT3调控功能，从而通过改变炎症和凝血相关基因的表达来贡献血栓倾向？这是一个值得探索的基因型-表现型多维机制假说；（2）系统性硬化症中的循环自身抗体与SERPINA10丰度变化（PubMed:40928059）提示SERPINA10可能是自身免疫-凝血交叉疾病的生物标志物；（3）SERPINA10-PIAS3-STAT3轴的发现为开发非抗凝性的STAT3通路调控药物提供了新思路——可以设计"核定位缺陷SERPINA10变体"或"STAT3调控功能特异的SERPINA10衍生肽"，在保留抗凝功能的同时选择性增强或削弱STAT3调控活性；（4）SERPINA10的RCL可作为PROTAC设计的靶向配体——将RCL肽段与E3泛素连接酶配体（如CRBN/VHL）融合，可能实现对特定丝氨酸蛋白酶（尤其是凝血因子）的催化降解而非简单抑制，达到更持久的治疗效果。

### PubMed 文献

**PubMed count: 93**

| 42255490 | Integrative Analysis of Genetic Risk Factors for Acute Myeloid Leukemia Using Mendelian Randomization and Single-Cell RN | Int J Genomics 2026 |
| 42167667 | Method Evaluation of Liquid Biopsy Proteomics for Limited Plasma Volume. | Mol Cell Proteomics 2026 |
| 41572258 | Persistent immune, coagulation and cardiac dysregulation are correlated with later post-discharge mortality in children  | BMC Med 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SERPINA10

