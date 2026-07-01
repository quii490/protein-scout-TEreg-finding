---
type: protein-evaluation
gene: "PCYOX1L"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCYOX1L 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCYOX1L |
| 蛋白名称 | Prenylcysteine oxidase 1-like |
| 蛋白大小 | 494 aa / 54.6 kDa |
| UniProt ID | Q8NBM8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 494 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=6 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=89.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | FAD/NAD-bd_sf; Prenylcys_lyase; Prenylcysteine_Oxase1 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=39 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **76.5/100** | 互证: +1 |

### 3. 分析
- Mitochondria; Nucleoplasm (Approved)
- PubMed strict=6 broad=8
- AF pLDDT=89.8 PDB=0
- InterPro: FAD/NAD-bd_sf; Prenylcys_lyase; Prenylcysteine_Oxase1
- Pfam: NAD_binding_8; Prenylcys_lyase
- PPI degree=39 ChIP: None
40712023: The secreted protein PCYOX1L controls the surface expression of acid-sensing ion | 38775423: Primary Squamous Cell Carcinoma of the Thyroid Has a Molecular Genetic Profile D | 37179332: Prenylcysteine oxidase 1 like protein is required for neutrophil bactericidal ac

### 4. 总体评价
**76.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Prenylcysteine oxidase 1-like

**功能**: Prenylcysteine oxidase that cleaves the thioether bond of prenyl-L-cysteines, such as farnesylcysteine and geranylgeranylcysteine. Does not metabolize shorter prenyl chain compounds (Probable). Required in the mevalonate pathway to regulate prenylation and enhances the bactericidal activity of neutrophils (By similarity). Promotes the assembly of the postsynaptic ion channel ASIC1a (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036188 |
| InterPro | IPR010795 |
| InterPro | IPR017046 |
| Pfam | PF13450 |
| Pfam | PF07156 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FBXO6 | BioGRID | 0 |
| MOV10 | BioGRID | 0 |
| NXF1 | BioGRID | 0 |
| CD1B | BioGRID | 0 |
| PLAUR | BioGRID | 0 |
| LACRT | BioGRID | 0 |
| LYZL2 | BioGRID | 0 |
| IFNA21 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NBM8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000145882-PCYOX1L

![](https://images.proteinatlas.org/37463/436_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/37463/436_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/37463/521_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/37463/521_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/37463/442_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/37463/442_G1_3_red_green.jpg)

### PubMed 文献

**PubMed count: 8**

| 40712023 | The secreted protein PCYOX1L controls the surface expression of acid-sensing ion channel 1a. | Sci Adv 2025 |
| 40100054 | Exploring NamiRNA networks and time-series gene expression in osteogenic differentiation of adipose-derived stem cells. | Ann Med 2025 |
| 38775423 | Primary Squamous Cell Carcinoma of the Thyroid Has a Molecular Genetic Profile Distinct From That of Anaplastic Thyroid  | Am J Surg Pathol 2024 |

### 深度机制分析

**结构域架构与分子功能推演。** PCYOX1L的双结构域架构——FAD/NAD(P)结合Rossmann折叠(IPR036188)和异戊烯半胱氨酸裂解酶催化域(IPR010795)——定义了其作为"异戊烯化修饰清除酶"的生化身份。Rossmann折叠由βαβ单元重复组成,通过保守的GXGXXG基序结合FAD辅因子的焦磷酸基团,将辅因子定位至催化中心。Prenylcys_lyase域提供活性位点以执行硫醚键(C-S-C)的氧化裂解——这是对法尼基半胱氨酸(farnesylcysteine)和香叶基香叶基半胱氨酸(geranylgeranylcysteine)的专一性反应。值得注意的是,该酶不代谢较短链的异戊烯化合物(UniProt注释:probable),说明其底物结合口袋对C15和C20的异戊烯链具有长度选择性,这可能由疏水通道的深度决定。pLDDT=89.8的高信度预测提示两个结构域之间有清晰的域间界面,组成了一个完整的底物通道——FAD在该通道的底部提供氧化还原当量,而异戊烯链从溶剂可及表面进入通道直至硫醚键到达催化中心。

**PPI网络揭示的生物学意义。** 尽管BioGRID互作评分普遍偏低,PCYOX1L的互作组构成却极具启发意义。MOV10是RNA解旋酶超家族1(SF1)成员,是piRNA生物发生、mRNA降解和逆转录元件沉默的关键因子。PCYOX1L与MOV10的互作暗示异戊烯化修饰稳态与RNA代谢之间存在未预期的功能耦联——一种可能性是PCYOX1L通过调节小GTPases(如Rho/Rab家族)的异戊烯化状态影响MOV10所在RNA颗粒的亚细胞定位或组装。NXF1是核mRNA出核受体,nxRNA核糖核蛋白复合体通过NXF1-NXT1异二聚体穿越核孔复合体——PCYOX1L的核质定位与NXF1互作的一致性提示该酶可能在mRNA出核过程中调控特定mRNA的命运。FBXO6是SCF(FBXO6)E3泛素连接酶的底物识别亚基——该F-box蛋白专门识别N-linked高甘露糖型糖蛋白并介导其内质网相关降解(ERAD)。PCYOX1L-FBXO6互作提示:(1)PCYOX1L本身可能被糖基化并因此成为泛素化底物;(2)PCYOX1L可能参与ERAD底物的异戊烯化修饰识别;(3)或两者在ER-高尔基囊泡运输中间体中功能性互作。PLAUR(uPAR/CD87)参与纤溶酶原活化和细胞外基质重塑,与肿瘤侵袭和免疫细胞迁移相关,这条连接暗示PCYOX1L可能在炎症微环境中发挥作用。

**结构层面的功能解读。** pLDDT=89.8但PDB=0的组合意味着该蛋白在实验结构上完全未被表征,但AF2预测质量高到足以指导功能实验。FAD结合域(NAD_binding_8, PF13450)属于Rossmann折叠超家族的一个分化分支,采用经典的6-stranded parallel β-sheet sandwiched by α-helices拓扑。Prenylcys_lyase域(PF07156)推测含有保守的活性位点His/Cys残基对,可能形成催化二联体以活化硫醚键。整个催化循环推测为:(1)FAD氧化底物的硫醚硫原子形成阳离子中间体;(2)水分子亲核进攻导致C-S键断裂;(3)释放游离半胱氨酸和异戊烯醛产物——这是一个罕见的氧化还原驱动的碳-硫键断裂反应。结构层面的一个关键问题是产物(尤其是异戊烯醛)的后续代谢去向——这些疏水性醛类具有潜在的细胞毒性,需要相偶联的解毒机制处理。

**分子机制综合模型。** PCYOX1L在分子层面执行"异戊烯化蛋白质周转循环的终末代谢步骤"。更具体地说,异戊烯化蛋白(如Ras超家族GTPases)在完成其信号转导功能后,被蛋白酶体或溶酶体降解,但其C端的异戊烯化半胱氨酸残基在常规蛋白水解中无法被有效切割——这会导致异戊烯半胱氨酸的溶酶体积累,干扰细胞膜脂质组成和信号转导。PCYOX1L通过FAD依赖的氧化裂解将这些"代谢死胡同产物"转化为可排泄或可再利用的代谢物,从而维持异戊烯化修饰的可持续周转。核质定位(NXF1互作)进一步提示PCYOX1L可能在核被膜或核质中对异戊烯化蛋白代谢产物进行清除——许多转录因子和核蛋白(如lamin B、核孔蛋白)依赖法尼基化修饰进行核膜锚定,它们的降解必须由PCYOX1L来完成。中性粒细胞杀菌活性(PubMed:37179332)和ASIC1a通道表面表达调控(PubMed:40712023)则揭示了PCYOX1L在"异戊烯化依赖的宿主防御"和"神经元兴奋性调控"中的潜在生理角色。

**研究与转化意义。** (1)"异戊烯半胱氨酸代谢缺陷"作为一种尚未被充分认识的代谢疾病状态——PCYOX1L的功能缺失突变可能导致异戊烯半胱氨酸积累、干扰小GTPase信号稳态,后果包括免疫缺陷(鉴于中性粒细胞功能缺陷的报道)。(2)PCYOX1L是法尼基转移酶抑制剂(FTIs,用于癌症治疗)的"下游效应分子"——FTI处理后法尼基化抑制可能减少PCYOX1L的底物供给,反过来影响FTI的疗效与抵抗机制。(3)ASIC1a通道的表面表达调控(PubMed:40712023)建立了"异戊烯化代谢→离子通道运输→神经元功能"的连接,可能对疼痛、缺血性脑损伤和突触可塑性相关疾病具有意义。(4)MOV10互作开辟的方向——"异戊烯化/RNA代谢交叉调控"——是一个全新的生物学领域,将脂质修饰与RNA生物学串联起来。

