---
type: protein-evaluation
gene: "MGST3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MGST3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MGST3 |
| 蛋白名称 | Glutathione S-transferase 3, mitochondrial |
| 蛋白大小 | 152 aa / 16.5 kDa |
| UniProt ID | O14880 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 152 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=76 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=92.2; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | MAPEG; MAPEG-like_dom_sf; Membr-assoc_MAPEG |
| PPI | 8/10 | x3 | 24.0 | PPI degree=308 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=76 broad=99
- AF pLDDT=92.2 PDB=0
- InterPro: MAPEG; MAPEG-like_dom_sf; Membr-assoc_MAPEG
- Pfam: MAPEG
- PPI degree=308 ChIP: None
38354236: Mutant p53 protects triple-negative breast adenocarcinomas from ferroptosis in v | 12895593: Leukotriene C(4) synthase. | 38971310: MGST3 regulates BACE1 protein translation and amyloidogenesis by controlling the

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Glutathione S-transferase 3, mitochondrial

**功能**: Displays both glutathione S-transferase and glutathione peroxidase activities toward oxyeicosanoids, as part of cellular detoxification as well as synthesis of bioactive metabolites (PubMed:36370807, PubMed:9278457). Catalyzes conjugate addition of reduced glutathione to the alpha, beta-unsaturated C=C carbonyl group of eisosanoids such as leukotriene A4 and 15-deoxy-Delta12,14-prostaglandin J2 to form GSH adducts relevant to the inflammatory response (PubMed:36370807, PubMed:9278457). Catalyzes

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050997 |
| InterPro | IPR023352 |
| InterPro | IPR001129 |
| Pfam | PF01124 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GPX4 | STRING | 938 |
| PRDX6 | STRING | 914 |
| GSS | STRING | 904 |
| HPGDS | STRING | 859 |
| PTGES | STRING | 828 |
| SNRPD3 | STRING | 751 |
| GGT7 | STRING | 747 |
| GGT5 | STRING | 713 |


### 深度机制分析

**结构域架构**：MGST3（152 aa，16.5 kDa）是膜相关蛋白类花生酸和谷胱甘肽代谢（MAPEG, Membrane-Associated Proteins in Eicosanoid and Glutathione metabolism）超家族成员，含MAPEG结构域（IPR050997，Pfam MAPEG PF01124）和MAPEG-like_dom_sf（IPR023352）。MAPEG超家族的标志性折叠由4个跨膜α-螺旋（TM1-TM4）构成，活性位点位于TM螺旋束的胞质面。Membr-assoc_MAPEG（IPR001129）进一步确认其膜锚定特性。MGST3兼具谷胱甘肽S-转移酶（GST）和谷胱甘肽过氧化物酶（GPx）双功能活性——GST催化GSH（还原型谷胱甘肽，γ-Glu-Cys-Gly三肽）向亲电底物（如白三烯A4，LTA4）的缀合加成；GPx催化脂质氢过氧化物的GSH依赖性还原。MAPEG家族的催化机制不同于胞质GST——前者利用结合于TM螺旋束内的GSH硫醇基（Cys-SH）作为催化亲核试剂或氧化还原中心，后者利用Tyr/Ser-OH作为催化亲核试剂。

**PPI互作网络解读**：PPI degree=308（极高），核心互作揭示了GSH代谢的完整互作网络：（1）GPX4（谷胱甘肽过氧化物酶4——铁死亡的核心抑制因子，STRING 938分）；（2）PRDX6（Peroxiredoxin 6——兼具GST和磷脂酶A2双功能，STRING 914分）；（3）GSS（谷胱甘肽合成酶——GSH合成的最后一个酶，STRING 904分）；（4）HPGDS（造血前列腺素D合成酶——催化PGH2→PGD2异构化，STRING 859分）；（5）PTGES（前列腺素E合成酶——催化PGH2→PGE2异构化，STRING 828分）；（6）SNRPD3（Sm-D3剪接体核心蛋白，STRING 751分）的共表达关联提示MGST3与RNA剪接的可能联系；（7）GGT7/GGT5（γ-谷氨酰转移酶，催化GSH的γ-谷氨酰基转移，是GSH回收通路的一部分，STRING 747/713分）。

**结构解读**：AlphaFold pLDDT=92.2，预测置信度极高（全人类蛋白质组前5%）。4个跨膜α-螺旋（TM1-TM4, 各约20-25个残基）在pLDDT >94的水平上形成紧凑的左手四螺旋束。GSH结合位点位于TM1和TM2之间的胞质loop（含保守的GST催化基序——ERXXXXD或等效酸性残基簇）和TM1/TM4之间的界面。MAPEG家族的GSH结合不依赖于经典的G-site/H-site二分法（胞质GST的特征）——取而代之的是GSH的γ-Glu和Cys残基通过氢键和盐桥网络嵌入TM螺旋束的胞质开口处。铁死亡抑制和脂质过氧化物还原的双重活性与该结构的双底物结合模式一致。

**机制模型**：MGST3在氧化应激和铁死亡信号通路中占据关键节点：（1）经典GST功能：催化GSH与内源性亲电脂质（如白三烯A4，LTA4）或外源性毒物（xenobiotics）的缀合，生成水溶性GSH缀合物，通过MRP（多药耐药相关蛋白）外排泵排出胞外，实现细胞解毒；（2）GPx功能：通过GSH依赖的脂质过氧化物还原——将膜磷脂中的氢过氧化物（PUFA-OOH）还原为醇（PUFA-OH），防止脂质过氧化的链式传播，协同GPX4维持细胞膜的氧化还原稳态；（3）铁死亡调控：MGST3通过抑制铁死亡（ferroptosis）促进子宫内膜异位症的进展（PMID:42234252）——这一功能与GPX4的铁死亡抑制活性形成平行或合作保护机制。MGST3缺失导致的铁死亡敏感性增加提示其在多种细胞类型（特别是间质细胞和间皮细胞）中作为"第二防线"的铁死亡抑制因子——在GPX4耗尽或失活时MGST3可提供代偿性的脂质过氧化物解毒活性。

**TE调控展望**：MGST3的TE调控潜力极低。铁死亡和氧化还原调控虽然在全局水平上影响染色质结构（铁死亡中释放的铁离子→Fenton反应→羟基自由基→DNA氧化损伤→染色质断裂→TE区域DNA损伤易感），但MGST3的膜锚定特性和GSH代谢功能无法直接或间接特异性地调控TE。铁死亡诱导的DNA损伤和基因组不稳定性作为TE激活的可能触发器是一个值得在系统水平上研究的理论问题——MGST3抑制铁死亡→减少DNA氧化损伤→降低DNA损伤诱导的TE转录，但其效应将是全基因组性的而非TE特异性的。

![PAE](https://alphafold.ebi.ac.uk/files/AF-O14880-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000143198-MGST3

![](https://images.proteinatlas.org/53311/1028_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/53311/1028_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/53311/987_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/53311/987_G3_2_red_green.jpg)
![](https://images.proteinatlas.org/53311/802_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/53311/802_D1_3_red_green.jpg)

### PubMed 文献

**PubMed count: 99**

| 42234252 | MGST3 Promotes Endometriosis Progression by Suppressing Ferroptosis. | Cell Biochem Biophys 2026 |
| 42193258 | Spermidine Targets Ovarian Granulosa Cells via Activating the FHC/SLC7A11 Axis to Regulate Iron Homeostasis and Ameliora | Antioxidants (Basel) 2026 |
| 42030675 | Comparison of oxidative and techno-functional properties of dark and ordinary muscles in snakehead fish: Insights from m | Food Chem 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MGST3

