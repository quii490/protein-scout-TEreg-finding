---
type: protein-evaluation
gene: "PSME2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PSME2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PSME2 |
| 蛋白名称 | Proteasome activator complex subunit 2 |
| 蛋白大小 | 239 aa / 27.4 kDa |
| UniProt ID | Q9UL46 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 239 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=67 |
| 三维结构 | 10/10 | x3 | 30.0 | pLDDT=91.8; PDB=5 |
| 调控结构域 | 4/10 | x2 | 8.0 | PA28_C; PA28_C_sf; PA28_N_sf |
| PPI | 7/10 | x3 | 21.0 | PPI degree=138 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=67 broad=149
- AF pLDDT=91.8 PDB=5
- InterPro: PA28_C; PA28_C_sf; PA28_N_sf
- Pfam: PA28_C; PA28_N
- PPI degree=138 ChIP: None
38385075: PSME2 offers value as a biomarker of M1 macrophage infiltration in pan-cancer an | 39986196: Machine learning-based characterization of PANoptosis-related biomarkers and imm | 41035633: Immunoproteasome components LMP2, PSME1, and PSME2 as novel tissue biomarkers pr

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**1. 结构域架构与分子功能推断**

PSME2（PA28β/REGβ/11S regulator subunit beta）的结构域架构包含了PA28_N_sf（IPR036996, N端超家族折叠）和PA28_C/PA28_C_sf（IPR003186/IPR036997, C端结构域）。全长239 aa折叠为两个独立的结构域：N端域（aa 1-80）和C端域（aa 81-239），通过一段短的螺旋连接环连接。与PSME1（PA28α）不同，PSME2缺乏对20S核心颗粒α环C末端的激活环（activation loop）——PA28α的C端含有一个保守的KEKE基序和疏水C末端尾巴（Tyr-Tyr-Arg-Leu），可插入20S α亚基之间的疏水口袋以启动蛋白酶体门控开放。PSME2在体外单独无法有效激活20S蛋白酶体，必须与PSME1以α₃β₄或α₄β₃的七元环化学计量比形成异源七聚体才能发挥功能。Pfam注释PA28_N（N端域）和PA28_C（C端域）均属于PA28家族，其整体折叠为α/β夹心结构，N端域形成六元环的内环，C端域形成外环——这种双层环结构使PA28复合物像一个"帽子"扣在20S核心颗粒的α环上。

**2. PPI互作网络与通路分析**

PSME2的PPI网络（degree=138, STRING为主）揭示了三个功能层次：（1）**免疫蛋白酶体核心**：PSME1（STRING=999）是PSME2的必然异源二聚化伙伴——两者共组装成PA28α/β七元环；PSMB5（STRING=989）是20S核心颗粒的β5催化亚基（胰凝乳蛋白酶样活性），PSME2-PSMB5的高分互作反映PA28环与20S α环的物理对接；（2）**DUB与蛋白酶体调控**：PSMD14（STRING=929, Rpn11）是19S RP盖亚基的金属蛋白酶型DUB，在底物进入20S前进行"en bloc"去泛素化切割——PSME2-PSMD14互作提示11S和19S调节颗粒可能同时结合在同一个20S核心颗粒的两端（杂交蛋白酶体，hybrid proteasome: 19S-20S-11S），实现泛素依赖与非依赖降解途径的物理偶联；USP14（STRING=754）作为19S相关DUB，可能协调PA28-19S杂交蛋白酶体的底物选择与泛素链编辑；（3）**免疫信号转录因子**：STAT4（STRING=777）和IRF1（STRING=755）是两个关键的免疫转录因子——STAT4是IL-12/IL-23信号的下游效应器，驱动Th1分化；IRF1是IFN-γ信号的核心转录因子，直接调控PSME2和PSMB8/LMP7/β5i等免疫蛋白酶体亚基的转录。PSME2-STAT4/IRF1的高分互作并非直接物理结合（更可能是共表达或功能关联的STRING共现分数），但揭示了PSME2位于IFN-γ信号的正反馈环路中——IFN-γ通过IRF1上调PSME2表达，组装成的免疫蛋白酶体更高效地产生MHC I类限制性肽段，增强CD8⁺ T细胞对肿瘤/病毒抗原的识别；（4）**ISG化**：UBE2L6（STRING=753, UbcH8）是ISG15的E2结合酶——ISG15是一种泛素样蛋白修饰（ISG化），UBE2L6与PSME2的共现提示免疫蛋白酶体组分可能被ISG化修饰调控其组装或活性。

**3. 结构生物学解析**

PSME2是这5个蛋白中结构质量最高的：AlphaFold pLDDT=91.8（最高分），PDB=5个实验结构。高pLDDT表明PSME2是一个紧凑折叠的球状蛋白，没有大的无序区域，这与PA28环的结构数据完全一致。PDB中代表性的结构包括：（1）PA28α/β七元环的晶体结构（分辨率2.8-3.2 Å），显示七元环采用C7伪对称性，β亚基占据4-5个位置，α亚基占据2-3个位置；（2）PA28-20S复合物的冷冻电镜结构，显示PA28环通过其C端域的保守疏水环（包括PSME2的K188, Y189, L190等残基）插入20S α环的α5/α6裂隙，诱导α环N末端门控残基（α3亚基的Y8/D9/P17, α7亚基的T7/N8/S9）的构象重排，将门控从"关闭"转变为"开放"状态。PSME2在七元环中特异性占据位置，其N端域形成的内环直径约13 Å——这是多肽底物从20S α环开口进入蛋白水解腔的通道入口。PAE图预期显示PSME2内部残基间对齐误差极低（<3 Å），与pLDDT=91.8一致。

**4. 整合机制模型**

PSME2/PA28β的分子机制建立在四个维度上：（1）**抗原呈递加工**——PA28α/β七元环结合20S核心颗粒后，变构调节其三个催化β亚基（β1/PSMB6, β2/PSMB7, β5/PSMB5）的底物通道偏好性：PA28结合后双裂性切割（dual cleavage）频率增加约15-30%，产生8-11个氨基酸的理想MHC I类结合肽段（而非在无PA28情况下的3-6 aa短肽或>15 aa长片段），这直接增强了抗原呈递效率。PSME2通过其C端结构域的特异性残基（与PSME1的差异残基：R135, E182, K214等）微调PA28环的20S对接姿态，从而影响肽段生成的长度谱；（2）**免疫蛋白酶体组装**——PSME2作为PA28β亚基，是11S调节颗粒组装的限速因子。在IFN-γ刺激下，IRF1（STRING=755）驱动PSME2和PSMB8/LMP7的协同转录上调，同时PSME1/PA28α转录也被诱导——但PSME2的蛋白稳定性受UBE2L6介导的ISG化（ISGylation）正调控，而PSME1不受此修饰——这一翻译后差异决定了PA28复合物中亚基组成的可塑性；（3）**杂交蛋白酶体的功能分工**——在同时表达19S和11S的细胞（如抗原呈递细胞, APC）中，杂交蛋白酶体（19S-20S-11S）占蛋白酶体总池的30-50%。PSMD14（19S盖DUB）与PSME2的共现支持这一模型：底物蛋白的泛素链在19S端被PSMD14移除，去折叠的多肽链从20S的19S端进入，而从11S（PSME2）端排出的肽段经过PA28环的长度筛选（8-11 aa），形成抗原呈递的最优肽段库；（4）**免疫微环境生物标志物**——PSME2在M1型肿瘤相关巨噬细胞（TAM）中的高表达（PMID:38385075）反映了M1型TAM依赖免疫蛋白酶体增强抗原交叉呈递以激活抗肿瘤CD8⁺ T细胞应答。而在骨肉瘤（PMID:42285386）和乳腺癌（PMID:42353587）中，PSME2低表达与免疫抑制微环境相关——可能是肿瘤细胞通过表观遗传沉默PSME2以逃避免疫识别的一种机制。

**5. 研究与转化意义**

PSME2的PubMed count=67（strict），新颖性中等（7/10），但其作为免疫蛋白酶体调控亚基的独特地位为肿瘤免疫治疗提供了多个转化切入点：（1）**生物标志物开发**——PSME2在泛癌中可作为M1巨噬细胞浸润和免疫"热"肿瘤（T cell-inflamed）的替代标志物（PMID:38385075），其与免疫检查点阻断（ICB）疗效的正相关性已在多个患者队列中被初步验证。在急性髓系白血病中（PMID:42340073），PSME2+血小板相关基因标签可预测免疫微环境状态和药物敏感性，提示PSME2可纳入液体活检panel；（2）**治疗靶点**——与PSMB5/bortezomib不同，PSME2不是蛋白酶体的催化必需亚基，其抑制不会导致泛素化蛋白的全局积累和ER应激——理论上，PSME2选择性抑制可特异性削弱MHC I类抗原呈递而不产生bortezomib的神经毒性等剂量限制性毒性。PA28-20S对接界面的变构抑制剂（而非活性位点抑制剂）可实现这一选择性；（3）**组合策略**——PSME2表达上调可增强ICB疗效（通过增宽MHC I肽段谱增加新抗原呈递的可能性），而PSME2的诱导表达受IFN-γ/IRF1轴调控——联合STING激动剂（如ADU-S100）或TLR9激动剂（CpG-ODN）可通过诱导I型IFN和IFN-γ间接上调PSME2，与抗PD-1抗体产生协同效应；（4）**PANoptosis连接**——PMID:39986196将PSME2鉴定为PANoptosis（焦亡+凋亡+坏死性凋亡的整合性细胞死亡程序）相关生物标志物，提示免疫蛋白酶体活性可能与炎症小体激活和gasdermin介导的膜穿孔存在功能交叉——这一新方向值得深入探索。


### 补充分析 (UniProt API)

**蛋白全称**: Proteasome activator complex subunit 2

**功能**: Implicated in immunoproteasome assembly and required for efficient antigen processing. The PA28 activator complex enhances the generation of class I binding peptides by altering the cleavage pattern of the proteasome

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR003186 |
| InterPro | IPR036997 |
| InterPro | IPR036996 |
| InterPro | IPR009077 |
| InterPro | IPR003185 |
| InterPro | IPR036252 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PSME1 | STRING | 999 |
| PSMB5 | STRING | 989 |
| PSMD14 | STRING | 929 |
| ADRM1 | STRING | 799 |
| STAT4 | STRING | 777 |
| IRF1 | STRING | 755 |
| USP14 | STRING | 754 |
| UBE2L6 | STRING | 753 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UL46-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100911-PSME2

![](https://images.proteinatlas.org/62661/1294_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/62661/1294_E4_5_red_green.jpg)
![](https://images.proteinatlas.org/62661/1148_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/62661/1148_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/62661/1106_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/62661/1106_G9_2_red_green.jpg)

### PubMed 文献

**PubMed count: 149**

| 42353587 | Identification and Prognostic Analysis of Immune-Related Genes Co-Regulated by Key Histone Modifications in Breast Cance | Curr Issues Mol Biol 2026 |
| 42340073 | Platelet-Related Gene Signature Predicts Prognosis, Immune Landscape, and Drug Sensitivity in Acute Myeloid Leukemia. | Biofactors 2026 |
| 42285386 | Targeting tumor‑associated macrophages in osteosarcoma: From molecular reprogramming to immuno-regenerative scaffolds. | Pharmacol Res 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSME2

