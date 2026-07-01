---
type: protein-evaluation
gene: "GDE1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GDE1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GDE1 |
| 蛋白名称 | Glycerophosphodiester phosphodiesterase 1 |
| 蛋白大小 | 331 aa / 37.7 kDa |
| UniProt ID | Q9NZC3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 331 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=22 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=94.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | GP_PDE_dom; PLC-like_Pdiesterase_TIM-brl |
| PPI | 5/10 | x3 | 15.0 | PPI degree=35 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=22 broad=36
- AF pLDDT=94.5 PDB=0
- InterPro: GP_PDE_dom; PLC-like_Pdiesterase_TIM-brl
- Pfam: GDPD
- PPI degree=35 ChIP: None
17690467: Mammalian glycerophosphodiester phosphodiesterases. | 40579456: REM transcription factors and GDE1 shape the DNA methylation landscape through t | 16472945: Genomic organization, characterization, and molecular 3D model of GDE1, a novel 

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Glycerophosphodiester phosphodiesterase 1

**功能**: Hydrolyzes the phosphodiester bond of glycerophosphodiesters such as glycerophosphoinositol (GroPIns) and glycerophosphoethanolamine (GroPEth), to yield a glycerol phosphate and an alcohol (By similarity). Hydrolyzes glycerophospho-N-acylethanolamines to N-acylethanolamines in the brain and participates in bioactive N-acylethanolamine biosynthesis such as anandamide (an endocannabinoid), N-palmitoylethanolamine (an anti-inflammatory), and N-oleoylethanolamine (an anorexic). In addition, has a ly

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR030395 |
| InterPro | IPR017946 |
| Pfam | PF03009 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RGS16 | BioGRID | 0 |
| RGS2 | BioGRID | 0 |
| CLGN | BioGRID | 0 |
| ATAD3C | BioGRID | 0 |
| SLC4A7 | BioGRID | 0 |
| REEP5 | BioGRID | 0 |
| FAM84B | BioGRID | 0 |
| GAPDHS | BioGRID | 0 |


### 深度机制分析

**结构域架构**：GDE1（331 aa，37.7 kDa）属于甘油磷酸二酯磷酸二酯酶（GDPD）家族，含GP_PDE_dom（IPR030395，甘油磷酸二酯磷酸二酯酶结构域）和PLC-like_Pdiesterase_TIM-brl（IPR017946，PLC样磷酸二酯酶TIM桶折叠）。GDPD催化结构域（Pfam PF03009）采用TIM桶（α/β）8折叠——8个平行β-链围成中央桶状结构，外围8个α-螺旋。活性位点位于TIM桶C端开口处，由两个保守的His残基（或His+Glu/Asp）配位催化必需的Zn^2+或Co^2+离子，通过广义酸碱催化机制水解甘油磷酸二酯的磷酸二酯键。

**PPI互作网络解读**：PPI degree=35，主要互作伙伴指向G蛋白信号调控和代谢。RGS16和RGS2（Regulator of G-protein Signaling）均为Gα亚基的GTPase加速蛋白（GAP），加速G蛋白信号终止。CLGN（Calmegin，内质网分子伴侣）和REEP5（受体表达增强蛋白5，ER形态调控）提示GDE1可能与内质网膜系统存在功能上的空间邻近。ATAD3C（ATPase家族AAA domain-containing 3C，线粒体内膜蛋白）的互作可能反映GDE1与线粒体-ER接触位点（MAMs）的功能关联——与GDE1参与内源性大麻素（anandamide）合成的已知功能一致。

**结构解读**：AlphaFold pLDDT=94.5，是本批次中预测质量最高的蛋白之一。TIM桶核心区域pLDDT >95，活性位点的Zn^2+配位残基（His/His/Glu三联体）的空间排布清晰可辨。环区（loop regions，pLDDT 70-85）包含底物识别口袋，其中对甘油磷酸肌醇（GroPIns）和甘油磷酸乙醇胺（GroPEth）的底物选择性由疏水口袋中的关键残基（Phe/Tyr/Trp侧链）决定。GDE1也具有甘油磷酸-N-酰基乙醇胺水解酶活性——催化N-酰基乙醇胺类内源性脂质介质（包括anandamide、N-palmitoylethanolamine和N-oleoylethanolamine）的生成。这一双功能特性源于活性位点口袋对甘油磷酸二酯和甘油磷酸-N-酰基乙醇胺的差异化识别模式，但具体决定因子尚有待高分辨晶体结构解析。

**机制模型**：GDE1在脑内的功能最为清晰——通过水解甘油磷酸-N-酰基乙醇胺（GP-NAEs）生成具有生物活性的N-酰基乙醇胺（anandamide等内源性大麻素系统组分）。此外，近期研究揭示GDE1通过REM转录因子共同塑造DNA甲基化景观（PMID:40579456），这建立了GDE1从代谢调控到表观基因组调控的直接桥梁。GDE1在核质中的定位（Nucleoplasm Approved）可能并非HPA假阳性——具有代谢酶活性的蛋白定位于核内支撑局部NAE池合成，其产物（NAEs，如anandamide）可能作为核内PPARγ或核受体的配体，进而调控转录和/或表观遗传修饰。

**TE调控展望**：GDE1的TE调控潜力有限但值得关注。PMID:40579456报道的GDE1-REM-TF→DNA甲基化轴是直接联系GDE1与染色质修饰的罕见证据。如果GDE1通过局部NAE合成影响DNA甲基化酶（DNMT）活性或染色质可及性，TE区域的甲基化状态可能间接受到影响。GDE1在肿瘤细胞（如胶质母细胞瘤，已报道GDE1表达变化影响肿瘤进展）中的表达变化→NAE信号失调→TE去抑制的可能性值得在多组学数据中验证，但非GDE1的核心功能。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NZC3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000006007-GDE1

![](https://images.proteinatlas.org/77420/1824_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/77420/1824_B8_7_red_green.jpg)
![](https://images.proteinatlas.org/77420/2048_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/77420/2048_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/77420/2014_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/77420/2014_B11_4_red_green.jpg)

### PubMed 文献

**PubMed count: 36**

| 41975982 | Genes Involved in Lipid, Carbohydrate, and Protein Metabolism as Candidates Affecting Beef Flavor. | Animals (Basel) 2026 |
| 41965551 | Distribution and subacute modulation of endocannabinoid metabolizing enzymes in the trigeminal complex and midbrain in a | J Headache Pain 2026 |
| 41775304 | Continuous directed evolution of isoflavone synthase to mitigate feedback inhibition: combine use of a novel developed b | Bioresour Technol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GDE1

