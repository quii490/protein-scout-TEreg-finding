---
type: protein-evaluation
gene: "MICAL1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MICAL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MICAL1 |
| 蛋白名称 | [F-actin]-monooxygenase MICAL1 |
| 蛋白大小 | 1067 aa / 117.9 kDa |
| UniProt ID | Q8TDZ2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Basal body; Cytosol; Nucleoplasm; Plasma membrane; (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 1067 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=54 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=74.9; PDB=11 |
| 调控结构域 | 4/10 | x2 | 8.0 | bMERB_dom; CH_dom; CH_dom_sf |
| PPI | 6/10 | x3 | 18.0 | PPI degree=77 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +2 |

### 3. 分析
- Basal body; Cytosol; Nucleoplasm; Plasma membrane; Primary cilium (Approved)
- PubMed strict=54 broad=130
- AF pLDDT=74.9 PDB=11
- InterPro: bMERB_dom; CH_dom; CH_dom_sf
- Pfam: bMERB_dom; CH; FAD_binding_3
- PPI degree=77 ChIP: None
36371204: MICAL1 facilitates pancreatic cancer proliferation, migration, and invasion by a | 39868814: TBC1D20 coordinates vesicle transport and actin remodeling to regulate ciliogene | 36198272: MICAL1 activation by PAK1 mediates actin filament disassembly.

### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


**蛋白全称**: [F-actin]-monooxygenase MICAL1

**功能**: Monooxygenase that promotes depolymerization of F-actin by mediating oxidation of specific methionine residues on actin to form methionine-sulfoxide, resulting in actin filament disassembly and preventing repolymerization (PubMed:29343822). In the absence of actin, it also functions as a NADPH oxidase producing H(2)O(2) (PubMed:21864500, PubMed:26845023, PubMed:29343822). Acts as a cytoskeletal regulator that connects NEDD9 to intermediate filaments. Also acts as a negative regulator of apoptosi

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR022735 |
| InterPro | IPR001715 |
| InterPro | IPR036872 |
| InterPro | IPR050540 |
| InterPro | IPR002938 |
| InterPro | IPR036188 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NEDD9 | STRING | 998 |
| PLXNA1 | STRING | 888 |
| RAB8A | STRING | 871 |
| STK38 | STRING | 744 |
| SRC | BioGRID | 1 |
| GRB2 | BioGRID | 1 |
| ABL1 | BioGRID | 1 |
| CRK | BioGRID | 1 |


### 深度机制分析

**结构域架构**：MICAL1（1067 aa，117.9 kDa）是多模块F-actin氧化还原调控蛋白，含N端bMERB（biallelic MICAL end-binding Rab-binding）结构域（IPR022735, 1-200 aa区域, Pfam bMERB_dom）、中部CH（calponin homology）结构域（IPR001715, IPR036872, Pfam CH_dom_sf）和C端FAD结合-单加氧酶催化结构域（IPR050540, IPR002938, IPR036188, Pfam FAD_binding_3）。AlphaFold pLDDT=74.9，PDB实验结构11个，结构置信度较高。CH结构域（~250-400 aa区域）折叠为反向平行的四螺旋束，经典功能为F-actin结合模块——在α-actinin, filamin, spectrin和fimbrin中通过疏水表面与F-actin沟槽螺旋互作。bMERB结构域为MICAL家族特有，含Rab蛋白结合基序（Rab8/Rab10/Rab35识别），介导MICAL1靶向特定胞内囊泡和膜微区（PMID:36371204）。催化核心——FAD结合域（~600-1067 aa）采用Rossmann折叠，通过NADPH→FAD的电子转移链激活分子氧，产生FAD-C4a-(hydro)peroxy中间体，作为蛋白甲硫氨酸亚砜（MetO）合酶将F-actin的Met44和Met47侧链的硫醚硫氧化为亚砜。MICAL1的1067 aa较大蛋白体积容纳多结构域联动——N端bMERB定位、CH结构域actin识别和C端氧化催化的空间协作。

**PPI互作网络解读**：PPI网络以NEDD9（STRING 998，最高置信度）和PLXNA1（STRING 888）为核心，描绘MICAL1在信号转导-细胞骨架重塑通路中的中心地位。NEDD9/HEF1为CRK/CAS家族支架蛋白，bMERB-CH-FAD三结构域与NEDD9的SH3/SH2结构域形成信号复合体，连接integrin/FAK/Src激酶信号至F-actin氧化解聚（PMID:36198272, PAK1激活MICAL1）。PLXNA1（plexin A1）为Semaphorin 3A受体，其胞内GAP结构域调控R-Ras/Rap GTPase——MICAL1作为plexin/CRMP（collapsin response mediator protein）信号体组分参与神经元引导锥塌陷所需的局部F-actin解聚。STK38（NDR1, 744）为Hippo通路核心激酶，磷酸化后激活MOB1/LATS1/2磷酸化级联——MICAL1-STK38互作连接F-actin氧化还原状态至Hippo启动子YAP/TAZ核转位的细胞密度和机械力感知。RAB8A（871, 初级纤毛和膜蛋白运输Rab GTPase, PMID:39868814, TBC1D20调控纤毛生成和actin重塑）和SRC/GRB2/ABL1/CRK形成又一个信号模块，进一步将MICAL1锚定于酪氨酸磷酸化-细胞骨架信号轴。

**结构解读**：MICAL1的FAD依赖氧化反应遵循乒乓动力学机制——NADPH还原FAD→FADH₂，O₂的亲核攻击产生C4a-hydroperoxyflavin中间体，该中间体将Met的硫醚硫亲电氧化为MetO，自身恢复为氧化态FAD并释放水。CH结构域的actin结合位点（保守的Asp/Glu残基与actin Lys61/Lys68形成盐桥）将actin纤维精确呈递至催化FAD域的活性位点，确保Met44/Met47（位于actin subdomain 2的D-loop, 距核苷酸ATP/ADP结合裂隙仅15-20 Å）的特异性氧化。MetO修饰破坏actin极性——Met为疏水残基，氧化为极性的MetO引入局部负电荷密度并破坏相邻疏水packing，导致D-loop构象转变→Mg²⁺释放→actin亚基间界面的疏水接触丧失→F-actin单体解离（filament severing）。bMERB结构域的Rab识别通过hydrophobic switch（Rab-GTP结合暴露疏水补丁）实现膜局部定位——MICAL1仅在Rab8/Rab10-GTP阳性膜微区中稳定锚定和催化活性。核质定位（HPA Approved Nucleoplasm）提示MICAL1在M期核膜解体和胞质actin丝重组时可能出入核质——其FAD依赖的氧化反应也可能氧化核actin（nuclear actin, 参与染色质重塑、转录调控和DNA损伤修复的核特化actin池），影响转录复合体（RNA Pol II和BAF/chromatin remodeling complexes如SWI/SNF和INO80中均含actin作为结构亚基）的组装和活性。

**机制模型**：（1）F-actin氧化解聚——MICAL1是唯一的actin特异性甲硫氨酸氧化酶，通过将F-actin化学修饰（MetO）驱动细胞前沿（lamellipodia/filopodia）和应力纤维的F-actin塌陷，与cofilin/ADF（切断F-actin去磷酸化依赖）和gelsolin（Ca²⁺依赖切断）形成互补机制。MICAL1的活性受PAK1磷酸化激活（PMID:36198272）——PAK1为Rac1/Cdc42下游效应激酶，经Ser/Thr磷酸化MICAL1的bMERB-CH连接环解除自抑制构象——构成Rac1→PAK1→MICAL1→F-actin disassembly信号转导轴。（2）纤毛生成与中心体功能——MICAL1-RAB8A互作和TBC1D20调控（PMID:39868814）连接actin解聚至初级纤毛——纤毛生成需centriole膜对接和IFT复合体沿axoneme轴丝微管运输，而皮层actin网作为纤毛生成的物理屏障。MICAL1介导的中心体旁actin清除可解除纤毛生成的因子空间阻碍。（3）核质-actin氧化——MICAL1核质池的发现开辟核actin功能调控的新机制。核actin作为染色质重塑复合体（BAF/SWI-SNF, INO80, NuA4/TIP60）和RNA Pol II转录延伸复合体的必需亚基。MICAL1将核F-actin氧化为G-actin的MetO修饰形式可改变染色质重塑复合体的actin结合亲和力→调控染色质可及性→影响基因转录。此外，DNA损伤应答中nuclear actin filaments在DNA双链断裂（DSB）位点处组装并与Arp2/3和WASP形成核actin聚合网以驱动同源重组修复（HR）所需的DNA末端移动和同源搜索——MICAL1对核actin的解聚活性可能调控DSB修复路径选择（HR vs NHEJ）。

**TE调控展望**：MICAL1与TE调控的相关性来自核actin-染色质重塑轴和纤毛信号轴的间接效应。BAF/SWI-SNF染色质重塑复合体是LTR/ERV（特别是IAP和ERVK家族）和LINE-1 5'UTR转录调控的关键因子——BAF的ATPase亚基BRG1/SMARCA4介导核小体滑动和H2A.Z/H3.3组蛋白变体交换，决定TE启动子的染色质可及性。MICAL1通过氧化核actin调控BAF/SWI-SNF的actin亚基（BAF53a/ACTL6A和β-actin/ACTB）的氧化还原状态，可能间接影响BAF复合体在TE启动子上的占据和染色质重塑活性。HDAC6为MICAL1功能的已知调控因子——HDAC6去乙酰化微管蛋白和HSP90（HSP90乙酰化调控其RhoGTPase的分子伴侣活性），而HDAC6也是HIV-1 Tat转录激活和T细胞活化的关键调控因子（Tat乙酰化是其反式激活功能所需）。MICAL1依赖的actin氧化可能经NAD⁺/NADH比率和ROS水平改变HDAC6和Sirtuin去乙酰化酶活性，通过染色质组蛋白乙酰化修饰（H3K9ac, H4K16ac）间接影响TE的转录沉默。虽然MICAL1缺乏DNA结合结构域，其nuclear actin pool调控和对BAF/HDAC6/SWI-SNF的氧化还原依赖性影响构成了TE调控的合理非经典通路，值得通过MICAL1 siRNA/shRNA敲低+ATAC-seq或CUT&RUN检测TE染色质区域的核小体占位变化加以验证。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8TDZ2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000135596-MICAL1

![](https://images.proteinatlas.org/30175/2175_G1_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2175_G1_26_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2206_E1_56_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2206_E1_96_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2232_C1_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2232_C1_68_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000135596-MICAL1

![](https://images.proteinatlas.org/30175/2175_G1_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2175_G1_26_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2206_E1_56_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2206_E1_96_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2232_C1_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2232_C1_68_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000135596-MICAL1

![](https://images.proteinatlas.org/30175/2175_G1_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2175_G1_26_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2206_E1_56_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2206_E1_96_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2232_C1_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/30175/2232_C1_68_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 130**

| 41832877 | Impaired testicular development in male offspring following gestational DEHP exposure: The role of macrophage-Leydig cel | Ecotoxicol Environ Saf 2026 |
| 41777496 | Novel Genetic Insights into Lateral Temporal Lobe Epilepsy: Findings from Whole Exome Sequencing. | Noro Psikiyatr Ars 2026 |
| 41543640 | Integrated machine learning and bioinformatic analyses constructed a sulfur metabolism-related breast cancer risk model  | Discov Oncol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MICAL1

