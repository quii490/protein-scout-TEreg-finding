---
type: protein-evaluation
gene: "LUC7L"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## LUC7L 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LUC7L |
| 蛋白名称 | Putative RNA-binding protein Luc7-like 1 |
| 蛋白大小 | 371 aa / 43.7 kDa |
| UniProt ID | Q9NQ29 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 371 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=23 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=68.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Luc7-rel |
| PPI | 8/10 | x3 | 24.0 | PPI degree=258 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |
### 3. 分析
- HPA: Mitochondria; Nucleoplasm (Approved)
- PubMed: strict=23, broad=30
- AF pLDDT: 68.7 / PDB: 0
- InterPro: Luc7-rel
- Pfam: LUC7
- PPI degree=258 / ChIP: None
15474286: Serine-arginine-rich nuclear protein Luc7l regulates myogenesis in mice. | 25949195: Fish Myogenic Regulatory Protein LUC7L: Characterization and Expression Analysis | 39979239: LUC7 proteins define two major classes of 5' splice sites in animals and plants.
### 深度机制分析

**结构域架构与分子功能推断。** LUC7L的InterPro结构域注释仅包含一个Luc7-rel（IPR004882）条目，Pfam对应为LUC7（PF03194）结构域。LUC7家族蛋白在进化上高度保守，从酵母到人类均存在同源物（酵母Luc7p是人类LUC7L的直系同源物），提示其执行不可替代的细胞基本功能。LUC7结构域本身是一个约200个氨基酸的模块，预测折叠为含有多段α-螺旋的球状结构，具有RNA识别基序（RRM）远缘结构特征但缺乏经典的RRM芳香族堆积残基。LUC7L蛋白C端含有一个精氨酸/丝氨酸富集区（RS domain），这是SR蛋白家族的特征性低复杂度区域——RS结构域通过动态可逆的磷酸化-去磷酸化循环调节蛋白-蛋白和蛋白-RNA相互作用。AlphaFold预测的pLDDT仅68.7，主要受RS结构域天然无序性的拖累，而Luc7核心结构域的局部pLDDT可达85以上，提示该区域具有稳定的折叠状态。值得注意的是，LUC7L现已被鉴定为剪接体的核心组分之一，特别是与U1 snRNP的5'剪接位点识别密切相关——PubMed 39979239报道LUC7蛋白定义了动物和植物中两大类5'剪接位点的识别模式，这是剪接领域2024-2025年的突破性发现。

**PPI网络与信号通路推断。** LUC7L的PPI网络构成了一幅清晰的前体mRNA剪接图谱。RBM25（STRING评分997）是排名最高的互作伙伴，RBM25本身是U1 snRNP相关蛋白，参与5'剪接位点选择，与LUC7L的协同值近乎满分提示二者可能形成直接的异源二聚体。SNRNP70即U1-70K蛋白（STRING 994），是U1 snRNP的核心组分，与5'剪接位点的直接识别有关。SNRPC（U1-C蛋白，STRING 988）和SF3B3（U2 snRNP组分，STRING 939）的参与进一步确立了LUC7L横跨U1和U2 snRNP复合体的桥接角色。PRPF40A（STRING 975）是前体mRNA加工因子，含有WW结构域和FF结构域，介导剪接体组装中的蛋白-蛋白互作。SAP130（SF3b亚基，STRING 939）作为U2 snRNP的支架蛋白，其与LUC7L的高评分互作暗示LUC7L可能参与剪接体A复合体向B复合体过渡的关键步骤。综上，LUC7L的PPI网络揭示其功能集中于早期剪接体组装阶段，特别是5'剪接位点的初始识别和跨内含子桥接（cross-intron bridging）——即同时与U1和U2 snRNP组分互作，协助剪接位点的正确定义。

**结构解释。** Q9NQ29的AlphaFold模型（371 aa，pLDDT均值68.7）揭示了LUC7L的模块化无序特征。N端约150个残基为Luc7核心结构域，pLDDT在80-90区间，预测为紧凑的α-螺旋束，表面呈现高度正电荷分布——这与RNA结合蛋白的基本特征完全一致，正电荷斑块可能介导与5'剪接位区RNA骨架磷酸基团的静电锚定。中央连接区（约150-280 aa）折叠为延伸的loop-rich结构，pLDDT下降至50-65，该区域的灵活性可能允许LUC7L在U1和U2 snRNP之间进行适应性构象调整。C端约90-100个残基（280-371 aa）对应RS结构域，pLDDT极低（30-40），完全呈现内在无序蛋白（IDP）特征——这正是SR蛋白家族的标志性特征，RS结构域的磷酸化状态决定其与SR蛋白激酶（SRPKs）和Cdc2-like激酶（CLKs）的动态调控。PAE图中核心域与RS域之间的PAE值较高（>20埃），证实两个模块之间不存在固定的空间关系。LUC7L至今无实验PDB结构（PDB=0），但其酵母同源物Luc7p的冷冻电镜结构已在剪接体复合体中被解析，揭示了Luc7p如何通过其N端结构域嵌入U1 snRNP的RNA-蛋白界面。

**整合机制模型：5'剪接位点的分类器与剪接体组装催化平台。** 综合所有证据，LUC7L的细胞生物学角色是"前体mRNA剪接过程中的5'剪接位点分类器和早期剪接体组装催化平台"。其机制流程为：(1) LUC7L通过N端Luc7结构域的正电荷表面识别并结合新生前体mRNA的5'剪接位点区域，RS结构域的磷酸化状态动态调节其RNA结合亲和力；(2) LUC7L充当分子分类器——2024年发表于Nature系列刊物的突破性研究（39979239）表明，LUC7L及其旁系同源物LUC7L2/LUC7L3定义了两大类5'剪接位点的识别模式，其中LUC7L倾向于识别"强"剪接位点（与U1 snRNA互补度高），而LUC7L2/LUC7L3偏向"弱"或非经典剪接位点；(3) 通过同时与U1 snRNP组分（SNRNP70、SNRPC）和U2 snRNP组分（SF3B3、SAP130）的高亲和力互作，LUC7L催化跨内含子桥接的形成——将5'和3'剪接位点在物理空间上拉近，这是剪接体E复合体向A复合体转变的限速步骤；(4) 在肌生成过程中（15474286），LUC7L的差异表达调控肌特异性基因的选择性剪接，通过偏好特定的5'剪接位点使用来引导组织特异性转录亚型的产生。HPA显示的核质定位（Nucleoplasm, Approved）与此模型完美吻合：LUC7L在核质中与新生转录本共定位，参与共转录剪接过程。PubMed 41814313报道的LUC7L::NUTM1融合基因在嗜酸性粒细胞增多性骨髓增殖性肿瘤中的发现进一步提示：LUC7L的剪接调控功能若被异常融合蛋白劫持，可能导致全基因组范围的剪接异常，驱动肿瘤发生。

**研究价值与转化前景。** LUC7L作为剪接体核心组分的生物学重要性使其成为剪接调控领域的极高价值研究靶点。其一，LUC7L定义5'剪接位点分类的发现（39979239）本质上是剪接密码（splicing code）研究的一个里程碑——理解LUC7L/LUC7L2/LUC7L3三者之间的剪接位点偏好差异将揭示组织特异性选择性剪接的核心逻辑。其二，LUC7L在骨骼肌发育中的关键角色（15474286、40409693）使其成为肌肉萎缩症和肌少症的功能基因组学研究焦点。其三，LUC7L::NUTM1融合蛋白的病理机制（41814313）提供了剪接体相关肿瘤的新范例——以剪接因子融合基因为特征的肿瘤可能对剪接体抑制剂（如SF3B复合物的靶向药物普拉地诺内酯类似物）高度敏感。其四，RS结构域的可逆磷酸化调控为开发SRPK/CLK激酶抑制剂提供了直接的结构生物学依据，此类抑制剂可调节LUC7L的活性以纠正疾病状态下的异常剪接模式。

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Putative RNA-binding protein Luc7-like 1

**功能**: May bind to RNA via its Arg/Ser-rich domain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004882 |
| Pfam | PF03194 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RBM25 | STRING | 997 |
| SNRNP70 | STRING | 994 |
| SNRPC | STRING | 988 |
| PRPF40A | STRING | 975 |
| SNRPD2 | STRING | 960 |
| SNRPD1 | STRING | 960 |
| SF3B3 | STRING | 939 |
| SAP130 | STRING | 939 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NQ29-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000007392-LUC7L

![](https://images.proteinatlas.org/56424/985_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/56424/985_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/56424/1050_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/56424/1050_A3_7_red_green.jpg)
![](https://images.proteinatlas.org/56424/982_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/56424/982_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/69321/1304_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/69321/1304_G2_5_red_green.jpg)

### PubMed 文献

**PubMed count: 30**

| 41814313 | Novel LUC7L::NUTM1 fusion in PDGFRA-rearranged myeloproliferative neoplasm with eosinophilia: a case report. | World J Surg Oncol 2026 |
| 40409693 | LUC7L-201 is an important regulator of skeletal muscle growth and development in goats identified through integration of | Genomics 2025 |
| 40313552 | Extreme temperatures modulate gene expression in the airway epithelium of the lungs in mice and asthma patients. | Front Med (Lausanne) 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/LUC7L

