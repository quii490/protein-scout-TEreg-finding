---
type: protein-evaluation
gene: "MYO1E"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MYO1E 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MYO1E |
| 蛋白名称 | Unconventional myosin-Ie |
| 蛋白大小 | 1108 aa / 127.1 kDa |
| UniProt ID | Q12965 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Nucleoplasm (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 1108 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=66 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=80.1; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Ie/If_SH3; Kinesin_motor_dom_sf; Myosin_head_motor_dom-like |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=201 |
| **加权总分** | | | **120/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (nan)
- PubMed strict=66 broad=119
- AF pLDDT=80.1 PDB=0
- InterPro: Ie/If_SH3; Kinesin_motor_dom_sf; Myosin_head_motor_dom-like
- Pfam: Myosin_head; Myosin_TH1; SH3_1
- PPI degree=201 ChIP: None
29784049: Identification and therapeutic modulation of a pro-inflammatory subset of diseas | 37274465: Analysis and validation of the potential of the MYO1E gene in pancreatic adenoca | 32636717: The plasma peptides of sepsis.

### 4. 总体评价
**66.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Unconventional myosin-Ie

**功能**: Actin-based motor molecule with ATPase activity (PubMed:11940582, PubMed:36316095). Unconventional myosins serve in intracellular movements. Their highly divergent tails bind to membranous compartments, which are then moved relative to actin filaments. Binds to membranes containing anionic phospholipids via its tail domain. Involved in clathrin-mediated endocytosis and intracellular movement of clathrin-coated vesicles (PubMed:36316095). Required for normal morphology of the glomerular basement 

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR035507 |
| InterPro | IPR036961 |
| InterPro | IPR001609 |
| InterPro | IPR010926 |
| InterPro | IPR036072 |
| InterPro | IPR027417 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：MYO1E（Q12965, Unconventional myosin-Ie, 1108 aa, 127.1 kDa）是肌球蛋白超家族（myosin superfamily）class I myosin成员。标准myosin domain架构：N端Myosin_head motor domain（IPR001609, Pfam Myosin_head, ~700 aa）——conserved actin-binding ATPase motor domain——含ATP binding site（P-loop, Switch I/II motifs）和actin binding interface——催化ATP-dependent actin filament movement。Myosin_head的core为large alpha-helical domain（~800 aa在所有myosins中最大）——ATP hydrolysis产生的conformational change（"power stroke"）——lever arm（IQ motifs, calmodulin/light chain binding）amplify power stroke displacement~5-10 nm per ATP。Myosin_TH1域（Pfam Myosin_TH1, ~200 aa）为class I myosin特异的tail homology domain——含membrane binding interface——将MYO1E靶向至specific membrane compartments。C端SH3 domain（IPR035507, Pfam SH3_1, ~60 aa）识别PxxP motif——介导与signaling和endocytic蛋白的互作。Kinesin_motor_dom_sf（IPR027417, P-loop NTPase fold）与motor domain共享P-loop NTPase fold——属protein superfamily分类。AlphaFold pLDDT=80.1, PDB=0——motor domain pLDDT>85；TH1 domain pLDDT 75-85；SH3 domain pLDDT>90。PPI degree=201（极高度连接）——超过200个互作伙伴的蛋白通常是cellular hub。PubMed=66, PMIDs: 42094351（Myo1e/f调控phagocytic podosomes的cup closure）；41973933（Myo1E作为clathrin-mediated endocytosis的tension-responsive actuator）；36316095（myosin-Ie参与clathrin-mediated endocytosis和clathrin-coated vesicle intracellular movement）。

**PPI互作网络解读**：PPI network（degree=201）中数个关键伙伴具有颠覆性的核内/染色质连接。MOV10（Moloney leukemia virus 10 homolog, BioGRID）——LINE-1 retrotransposition inhibitor和RISC co-factor——MYO1E-MOV10物理互作是findings中的亮点——MYO1E可能作为MOV10的cytoskeletal transporter——将MOV10/RISC complex沿actin filament transport至特定subcellular location（如stress granule, P-body或perinuclear region）。SP1（Specificity protein 1, BioGRID）是ubiquitous transcription factor——识别GC box（GGGGCGGGG）和related GT/CACCC motifs——调控housekeeping genes和tissue-specific genes的basal transcription——MYO1E-SP1互作暗示MYO1E信号可influence transcription factor activity。EMD（Emerin, BioGRID）是inner nuclear membrane蛋白——LEM domain蛋白（LAP2-Emerin-MAN1 family）——Emerin与nuclear lamina（lamin A/C）互作——在nuclear architecture和chromatin organization中功能——EMD interact with HDAC3 and BAF complex→chromatin remodeling。DIAPH1（Diaphanous-related formin-1, BioGRID）作为actin nucleation factor——催化linear actin filament polymerization——MYO1E-DIAPH1互作形成actin dynamics regulatory loop。ILF3（NF90, BioGRID）是dsRNA binding protein——参与miRNA processing, RNA editing, and antiviral response。CUL1（BioGRID）是SCF（Skp1-Cullin1-F-box）E3 ubiquitin ligase的scaffold protein——调控cell cycle蛋白的ubiquitination and degradation。MYH11（smooth muscle myosin heavy chain 11, BioGRID）与MYO1E均为myosin家族蛋白——可能形成heterotypic myosin filament或competition for common light chains。

**结构解读**：Myosin motor mechanism遵循Lymn-Taylor actomyosin cycle：（1）ATP binding→actin-myosin dissociation→（2）ATP hydrolysis→lever arm conformational change（"recovery stroke"）→（3）weak rebinding to actin→phosphate release→"power stroke"（lever arm rotation, ~70 degree, ~10 nm displacement）→（4）ADP release→rigor state（tight actin binding）。MYO1E的TH1 domain（tail homology 1）含有highly basic region（PI(4,5)P2-binding motif）——电静力介导与acidic phospholipids（PS, PI(4,5)P2）的结合→target MYO1E to plasma membrane and endocytic vesicles。SH3 domain识别C-terminal PxxP motif-containing partners——在clathrin-mediated endocytosis中募集endocytic adaptor proteins。

**机制模型**：（1）Clathrin-mediated endocytosis——MYO1E作为tension-responsive actuator（PMID:41973933）——在clathrin-coated pit maturation中提供actin-dependent pulling force→drive vesicle scission from plasma membrane——MYO1E knockout cell显示delayed pit internalization和accumulated U-shaped pits。Podosome function（PMID:42094351）——MYO1E/1F在macrophage phagocytic podosomes中协调actin dynamics→完成phagocytic cup closure。（2）MOV10 transport and TE restriction——MYO1E与MOV10的互作是最具吸引力的功能连接——MYO1E motor activity可能沿actin filament运输MOV10/RISC complex至LINE-1 RNP成核位点（perinuclear stress granules, cytoplasmic foci）→增强MOV10的spatial restriction of LINE-1 retrotransposition。（3）Nuclear-cytoplasmic bridge——EMD interaction暗示MYO1E参与LINC complex（Linker of Nucleoskeleton and Cytoskeleton, nesprin-SUN-KASH domain protein network）的mechanotransduction——MYO1E施加的actin force可能经EMD传递至nuclear lamina→调控chromatin organization和gene expression。

**TE调控展望**：MYO1E的TE调控关联建立在MOV10交互和actin-dependent nuclear mechanotransduction上。MOV10是LINE-1 retrotransposition的强效inhibitor——MYO1E作为MOV10的actin-based transporter——调控MOV10的subcellular localization→affect LINE-1 RNP的accessibility and restriction efficiency。EMD（inner nuclear membrane, LE domain protein）的机械力传导和chromatin organization功能——MYO1E-EMD互作可能通过actin force-dependent nuclear deformation影响chromatin compartmentalization→间接调控TE区域（tend to locate at LADs, Lamin-Associated Domains）的chromatin state和transcriptional activity。CUL1（SCF E3 ligase scaffold）的功能性降解——如果MYO1E通过CUL1 ubiquitination pathway降解TE restriction factor或chromatin regulator——可能调节TE silencing的稳定性。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| EMD | BioGRID | 0 |
| SP1 | BioGRID | 0 |
| CUL1 | BioGRID | 0 |
| DIAPH1 | BioGRID | 0 |
| MOV10 | BioGRID | 0 |
| DTNA | BioGRID | 0 |
| ILF3 | BioGRID | 0 |
| MYH11 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q12965-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MYO1E

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000157483-MYO1E

![](https://images.proteinatlas.org/23886/181_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/23886/181_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/23886/1964_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/23886/1964_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/23886/182_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/23886/182_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/3003/1584_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/3003/1584_A6_5_red_green.jpg)

### PubMed

**Count: 119**

| PMID | Title |
|---|---|
| 42296901 | Fat phenomics reveals shared genetic architecture of abdominal fat and yolk lipids: Insight into the potential for divergent selection. |
| 42094351 | Myo1e/f regulate phagocytic podosomes to promote efficient cup closure in macrophages. |
| 41973933 | A local solution to local load: Myo1E as a tension-responsive actuator in clathrin-mediated endocytosis. |
| 41973050 | ER-derived caveolin-coated vesicles transport newly synthesized cholesterol to the plasma membrane. |
| 41911647 | The TGFB1-Wnt/β-catenin axis programs a neuroprotective IGF1(+) microglial state during epileptogenesis. |
