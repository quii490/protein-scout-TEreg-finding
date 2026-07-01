---
type: protein-evaluation
gene: "RAB9A"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RAB9A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RAB9A |
| 蛋白名称 | Ras-related protein Rab-9A |
| 蛋白大小 | 201 aa / 22.8 kDa |
| UniProt ID | P51151 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 201 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=40 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=91.1; PDB=2 |
| 调控结构域 | 4/10 | ×2 | 8.0 | P-loop_NTPase; Rab9; Small_GTP-bd |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=596 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Uncertain)
- PubMed strict=40 broad=122
- AF pLDDT=91.1 PDB=2
- InterPro: P-loop_NTPase; Rab9; Small_GTP-bd
- Pfam: Ras
- PPI degree=596 ChIP: None
32264724: Sex differences in autophagy-mediated diseases: toward precision medicine. | 21808068: RUTBC1 protein, a Rab9A effector that activates GTP hydrolysis by Rab32 and Rab3 | 22637480: RUTBC2 protein, a Rab9A effector and GTPase-activating protein for Rab36.

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ras-related protein Rab-9A

**功能**: The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB9A is involved in the transport of proteins between the endosomes and the trans-Golgi network (TGN) (

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR041824 |
| InterPro | IPR005225 |
| InterPro | IPR001806 |
| Pfam | PF00071 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GCC2 | STRING | 976 |
| NDE1 | STRING | 914 |
| VPS33A | STRING | 846 |
| STX12 | STRING | 716 |
| CHM | STRING | 706 |
| CHML | STRING | 702 |
| TRIP13 | BioGRID | 1 |
| CUL7 | BioGRID | 1 |


### 深度机制分析

**结构域架构**：RAB9A（201 aa，22.8 kDa）是Ras超家族Rab亚家族的核心成员，含三个高度保守的特征性结构域/基序：（1）P-loop_NTPase（IPR027417）构成GTP/Mg^2+结合的催化核心；（2）Rab9特异性结构域（IPR041824）赋予其区别于其他Rab蛋白（60+成员）的效应器结合特异性；（3）Small_GTP-bd（IPR005225）和Small_GTPase（IPR001806）形成典型的G域折叠。由于Ras超家族折叠在真核生物极度保守（酵母到人类高度同源），其G1-G5 motif的序列特征已得到大量晶体学和生化学验证。C端CAAX盒经geranylgeranylation修饰后锚定于内体/溶酶体和反式高尔基网络（TGN）膜。

**PPI互作网络解读**：PPI degree=596（本批次第二高，仅次于RHOJ的626），反映了RAB9A在内体-TGN膜运输中的核心地位。关键互作伙伴分为三个功能层：（1）膜运输机制：GCC2（GCC185，TGN定位的GRIP域卷曲螺旋蛋白，STRING 976分，RAB9A的直接效应器）、VPS33A（HOPS/CORVET系留复合物的SM蛋白亚基，STRING 846分）、STX12（Syntaxin-12，内体定位的SNARE蛋白，STRING 716分）、NDE1（NudE Neurodevelopment Protein 1，STRING 914分——连接膜运输和微管/中心体动力学）；（2）Rab调节因子：CHM（Rab escort protein 1/REP-1，STRING 706分——Rab蛋白的geranylgeranylation所必需）、CHML（REP-2，STRING 702分）；（3）泛素连接酶：TRIP13（BioGRID 1分）、CUL7（BioGRID 1分）。

**结构解读**：AlphaFold pLDDT=91.1（2个PDB实验结构验证），预测质量极佳。GTP结合态（PDB: 1WMS, 2OCB等）显示紧密的switch I/II构象，效应器结合面完全暴露。Switch I（E/Q-x-x-x-R-F/Y-R/K，残基约35-45）在GTP结合时形成短α-螺旋和β-发夹，Mg^2+由switch I的Thr/Ser羟基和GTP的γ-磷酸共同配位，稳定活性构象。Switch II（残基约60-75）的构象重排涉及与GCC2的卷曲螺旋区域的识别（通过疏水性界面和盐桥网络）。GDP结合态的switch I/II松弛无序（RAB9A在此状态下无法有效结合效应器）。C端高度柔性的超变区（hypervariable region）pLDDT极低（<50），但在与REP-1/CHM结合和随后的脂质修饰中发挥关键作用。

**机制模型**：RAB9A遵循经典的Rab分子开关模式调控内体到TGN的逆行运输：（1）GDP→GTP交换（由RabGEF催化）后，活性RAB9A-GTP锚定于晚期内体膜，通过GCC2效应器招募系留复合物（如GCC185-HOPS），促进内体与TGN膜的靠近；（2）RUTBC1和RUTBC2作为RAB9A的直接效应器和RabGAP（GTPase活化蛋白，PMID:21808068, PMID:22637480），通过加速GTP水解触发活性终止——此负反馈环路确保逆行运输的时间精确控制；（3）RAB9A的核质信号（Cytosol; Nucleoplasm Uncertain）可能反映其在胞质中通过CHM/REP-1复合物进行geranylgeranylation修饰和膜提取-重新递送循环——Rab蛋白在GDP结合态时被GDI（GDP dissociation inhibitor）从膜上提取并保护在胞质中，核质信号可能捕捉到这一胞质池。

**TE调控展望**：RAB9A与TE调控的直接联系极弱，但通过以下间接途径可能相关：（1）RAB9A通过调控内体-溶酶体系的货物分选影响自噬（autophagy）——自噬缺陷导致TE来源的胞质DNA积累和cGAS-STING通路激活，RAB9A已知参与自噬体成熟（与ATG5-ATG12/ATG16L1通路交叉）；（2）NDE1互作连接了内体运输和微管组织中心（MTOC）——NDE1是LIS1/PAFAH1B1的效应器，调控动力蛋白（dynein）功能，而动力蛋白介导的内体向核周逆行运输对核周信号传导至关重要；（3）CUL7泛素连接酶互作提示RAB9A可能被泛素化修饰——泛素化已被报道调控Rab蛋白的稳定性、活性和效应器选择性，若CUL7泛素化RAB9A发生在核周区域，可能影响RAB9A在核膜-内体接触位点的局部富集。


![PAE](https://alphafold.ebi.ac.uk/files/AF-P51151-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000123595-RAB9A

![](https://images.proteinatlas.org/16411/948_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/16411/948_D6_3_red_green.jpg)
![](https://images.proteinatlas.org/16411/951_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/16411/951_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/16411/943_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/16411/943_D6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 122**

| 41930813 | Dehydroandrographolide succinate alleviates ulcerative colitis via regulating RAB9A/NF-κB axis-mediated macrophage polar | Phytomedicine 2026 |
| 41898876 | Genetic Variants and Molecular Components Associated with Metabolic Dysfunctional-Associated Steatotic Liver Disease and | Genes (Basel) 2026 |
| 41865346 | Effect of PET-MPs exposure on the toxicology of PCOS: a multi-platform computational toxicology investigation. | Mol Divers 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RAB9A

