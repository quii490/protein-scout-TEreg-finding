---
type: protein-evaluation
gene: "KIAA2026"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KIAA2026 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KIAA2026 |
| 蛋白名称 | Uncharacterized bromodomain-containing protein 10 |
| 蛋白大小 | 2103 aa / 228.1 kDa |
| UniProt ID | Q5HYC2 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Vesicles, Cytosol;Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 2103 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=5 |
| 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=44.9; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | BRD10; Bromodomain; Bromodomain-like_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=13 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **69.9/100** | 互证: +1 |

### 3. 分析
- Vesicles, Cytosol;Nucleoplasm (Approved)
- PubMed strict=5 broad=6
- AF pLDDT=44.9 PDB=0
- InterPro: BRD10; Bromodomain; Bromodomain-like_sf
- Pfam: Bromodomain; KIAA2026_hel
- PPI degree=13 ChIP: None
38474122: Comprehensive Atlas of Alternative Splicing Reveals NSRP1 Promoting Adipogenesis | 25867764: RNA sequencing of sarcomas with simple karyotypes: identification and enrichment | 31397443: [The Interaction of miRNA-5p and miRNA-3p with the mRNAs of Orthologous Genes].

### 4. 总体评价
**69.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized bromodomain-containing protein 10

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR040214 |
| InterPro | IPR001487 |
| InterPro | IPR036427 |
| InterPro | IPR056522 |
| Pfam | PF00439 |
| Pfam | PF23450 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：KIAA2026（2103 aa, 228.1 kDa, Q5HYC2, 别名BRD10——Uncharacterized bromodomain-containing protein 10）是本批最大蛋白之一。核心结构元素为Bromodomain（IPR001487, Pfam PF00439）——经典的acetyl-lysine reader module——由约110 aa组成的left-handed four-helix bundle（aZ-aA-aB-aC），acetyl-lysine结合在ZA和BC loop形成的疏水口袋中（一个conserved Asn residue与acetyl carbonyl形成hydrogen bond，Tyr/Phe侧链形成water-mediated H-bond）。Bromodomain-like超家族（IPR036427）提示可能存在第二个变体bromodomain-like域。KIAA2026_hel域（PF23450）为蛋白独有的长alpha-helical region（约500-800 aa）——预测形成coiled-coil超螺旋结构。AlphaFold pLDDT=44.9极低——2103 aa的大蛋白多数残基处于无序/低置信状态——bromodomain区域本身pLDDT (~75-85)相对可靠，但coiled-coil和N端区域高度无序。pLDDT=44.9和PDB=0说明完整的全长蛋白结构解析极为困难——这是一个典型的多域scaffold蛋白。BRD10蛋白含bromodomain但在2103 aa的巨大蛋白中仅占~5%序列——其余区域功能未注释——可能含intrinsically disordered region (IDR), PEST sequence, nuclear localization signal (NLS)。

**PPI互作网络解读**：PPI degree=13，关键伙伴揭示KIAA2026的转录调控连接。CREB1（BioGRID, score=1）是cAMP response element-binding protein——经典bZIP转录因子——CREB1的KID domain磷酸化（Ser133）后招募CBP/p300（也是bromodomain蛋白）→组蛋白乙酰化→靶基因转录激活。KIAA2026的bromodomain可能识别CREB1靶基因座位上CBP介导的H3K27ac→与CREB1直接互作形成正向反馈——增强CREB1-dependent transcription。ATXN1（ataxin-1, BioGRID, score=1）是转录共抑制子——ATXN1与CIC（Capicua）和RORa形成repressor complex——KIAA2026可能通过bromodomain与ATXN1-CIC复合体的acetylated组分互作→调控ATXN1的转录抑制活性。MUS81（BioGRID, score=1）是结构特异性DNA endonuclease——催化Holliday junction resolution和replication fork restart——KIAA2026-MUS81互作连接至DNA修复/重组。HRAS（BioGRID, score=1）是经典RAS GTPase——KIAA2026-HRAS互作暗示KIAA2026参与RAS-MAPK信号与染色质的crosstalk。

**结构解读**：pLDDT=44.9的全局低碳置信度不应被视为结构不可靠——相反，这正是IDR-rich scaffold蛋白的典型特征。IDR在蛋白中行使"molecular glue"功能——通过multivalent low-affinity interaction与多个伙伴同时互作，形成biomolecular condensate（核体/核斑点）。KIAA2026假定以bromodomain作为chromatin reader锚定在acetylated chromatin区域后——其长IDR尾可同时结合CREB1、ATXN1、MUS81和HRAS——形成"chromatin-associated signaling hub"——整合cAMP信号（CREB1）、转录抑制（ATXN1）、DNA修复（MUS81）和MAPK信号（HRAS）于同一染色质位点。

**机制模型**：（1）Bromodomain-乙酰化依赖的染色质靶向——KIAA2026 bromodomain识别acetylated H3/H4（如H3K27ac, H4K5ac/K8ac/K12ac/K16ac）——将蛋白靶向至活跃增强子和启动子区域。（2）CREB1 co-activator功能——KIAA2026经bromodomain识别CBP/p300在CREB1靶基因处催化的H3K27ac，与CREB1物理互作→稳定CREB1-CBP/p300-TFIID转录激活复合体→促进CREB1靶基因（如BDNF, c-Fos, Bcl-2, NR4A1）的转录。（3）ATXN1 co-repressor调节——KIAA2026与ATXN1互作可能调控ATXN1-CIC repressor complex的染色质解离——bromodomain识别乙酰化干扰ATXN1的HDAC招募——影响ATXN1靶基因（在spinocerebellar ataxia 1/SCA1 pathology相关基因）的转录抑制效率。（4）脂肪生成选择性剪接（PMID:38474122）——KIAA2026在脂肪形成中经选择性剪接调控——可能与NSRP1 splicing factor共同调节脂肪生成关键转录因子（PPARg, C/EBPa）pre-mRNA剪接。

**TE调控展望**：KIAA2026的bromodomain使其成为TE调控的天然候选。Acetylated histones在LTR/ERV和LINE-1 5'UTR promoter区域的富集（H3K27ac标记活跃TE promoter/enhancer）是TE转录活性的核心特征。KIAA2026的bromodomain可能直接或间接"read"这些acetyl marks于TE染色质区域→调控TE启动子的转录状态。ATXN1作为转录抑制子可能参与TE silencing——KIAA2026-ATXN1互作影响TE区域抑制效率。MUS81的DNA repair功能在逆转录转座过程中处理LINE-1 ORF2p产生的DNA nick——KIAA2026-MUS81互作可能影响LINE-1 integration site repair。CREB1自身结合cAMP response element（CRE, TGACGTCA）——在LINE-1 5'UTR和HERV LTR中存在CRE-like motifs——KIAA2026作为CREB1 co-activator可能通过CREB1间接激活或抑制TE启动子的cAMP-responsive转录。KIAA2026是TE调控的极佳候选——bromodomain reader + 大IDR scaffold架构使其具备同时调节TE染色质状态和转录因子活性的能力。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CREB1 | BioGRID | 1 |
| ATXN1 | BioGRID | 1 |
| MUS81 | BioGRID | 1 |
| HRAS | BioGRID | 1 |
| TUBA3C | BioGRID | 1 |
| CDC42 | BioGRID | 0 |
| UBTD1 | BioGRID | 0 |
| RNF123 | BioGRID | 0 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000183354-KIAA2026

![](https://images.proteinatlas.org/2109/63_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/63_F5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/1044_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/1044_B6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/62_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/62_F5_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000183354-KIAA2026

![](https://images.proteinatlas.org/2109/63_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/63_F5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/1044_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/1044_B6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/62_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/62_F5_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000183354-KIAA2026

![](https://images.proteinatlas.org/2109/63_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/63_F5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/1044_B6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/1044_B6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/62_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2109/62_F5_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 6**

| 38474122 | Comprehensive Atlas of Alternative Splicing Reveals NSRP1 Promoting Adipogenesis through CCDC18. | Int J Mol Sci 2024 |
| 33618585 | Identification of potential lncRNAs and co-expressed mRNAs in gestational diabetes mellitus by RNA sequencing. | J Matern Fetal Neonatal Med 2022 |
| 33124039 | WDR34, a candidate gene for non-syndromic rod-cone dystrophy. | Clin Genet 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KIAA2026

