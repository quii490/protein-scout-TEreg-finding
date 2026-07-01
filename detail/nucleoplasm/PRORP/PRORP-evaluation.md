---
type: protein-evaluation
gene: "PRORP"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PRORP 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PRORP |
| 蛋白名称 | Mitochondrial ribonuclease P catalytic subunit |
| 蛋白大小 | 583 aa / 67.3 kDa |
| UniProt ID | O15091 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Mitochondria; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 583 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=60 |
| 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=78.9; PDB=5 |
| 调控结构域 | 4/10 | ×2 | 8.0 | MRPP3_PIN_dom; PRORP_C; TPR-like_helical_dom_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=29 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.9/100** | 互证: +2 |

### 3. 分析
- Mitochondria; Nucleoplasm (Supported)
- PubMed strict=60 broad=159
- AF pLDDT=78.9 PDB=5
- InterPro: MRPP3_PIN_dom; PRORP_C; TPR-like_helical_dom_sf
- Pfam: PRORP
- PPI degree=29 ChIP: None
25254289: Perrault Syndrome Overview. | 39503847: Cytosolic N6AMT1-dependent translation supports mitochondrial RNA processing. | 36370850: Gambogic acid and juglone inhibit RNase P through distinct mechanisms.

### 4. 总体评价
**69.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Mitochondrial ribonuclease P catalytic subunit

**功能**: Catalytic ribonuclease component of mitochondrial ribonuclease P, a complex composed of TRMT10C/MRPP1, HSD17B10/MRPP2 and PRORP/MRPP3, which cleaves tRNA molecules in their 5'-ends (PubMed:18984158, PubMed:25953853, PubMed:34715011). The presence of TRMT10C/MRPP1, HSD17B10/MRPP2 is required to catalyze tRNA molecules in their 5'-ends (PubMed:25953853)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR033495 |
| InterPro | IPR031595 |
| InterPro | IPR011990 |
| Pfam | PF16953 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：PRORP（583 aa, 67.3 kDa, O15091, 别名MRPP3）是线粒体RNase P的催化亚基——tRNA 5'末端加工的金属离子依赖RNase。结构域组成：（1）MRPP3_PIN域（IPR033495, N-terminal PIN domain）——PIN（PilT N-terminal）domain是RNA酶结构域，采用alpha-beta-alpha的三层sandwich折叠，含四个conserved acidic residues（Asp/Glu）配位两个二价金属离子（Mg2+或Mn2+）——执行single-stranded RNA的5'-leader sequence的phosphodiester bond水解；（2）PRORP_C域（IPR031595, Pfam PF16953）——约250 aa的C端结构域，由pentatricopeptide repeat（PPR）-like motifs组成，呈solenoid形超螺旋——PPR motifs识别单链RNA的特定核苷酸序列（每个PPR motif识别一个nt碱基）；（3）TPR-like helical domain（IPR011990）——tetratricopeptide repeat折叠模块——介导蛋白-蛋白互作和复合物组装。AlphaFold pLDDT=78.9, PDB=5——结构可信度高。PIN域pLDDT>90，折叠可靠；PRORP_C域pLDDT约75-85。

**PPI互作网络解读**：PPI degree=29，富集RNase P/MRP复合物亚基。TRMT10C（MRPP1, STRING 999）是线粒体RNase P的non-catalytic亚基——含N1-methyladenosine（m1A）和N1-methylguanosine（m1G）甲基转移酶活性（对tRNA进行m1A9/m1G9修饰）和S-adenosylmethionine（SAM）结合域。POP5/POP4/POP7（STRING 963/944/937）是核RNase P/MRP的蛋白亚基（核RNase P由H1 RNA ribozyme + 10 protein subunits组成）——这些互作提示PRORP（线粒体蛋白）可能与核RNase P共享部分蛋白亚基或在双定位（nucleoplasm+mitochondria）中使用同一套蛋白伙伴。POP1（STRING 932）是RNase P/MRP的最大亚基（~120 kDa），含多个coiled-coil域作为scaffold。RPP30/RPP38/RPP21（STRING 932）是核RNase P autoantigenic protein subunits。PRORP与核RNase P亚基的广泛互作强力支持其核质定位（HPA: Mitochondria; Nucleoplasm Supported）。

**结构解读**：PIN domain催化机制是two-metal-ion catalysis——两个Mg2+离子（MeA, MeB）分别作为Lewis acid（激活水分子亲核攻击）和transition state stabilization（稳定pentacovalent phosphorane transition state）——剪断tRNA precursor的5'-leader sequence phosphodiester bond，生成成熟tRNA 5'-monophosphate和3'-OH of upstream fragment。PRORP_C域（PPR-like）以modular "one-repeat-per-nucleotide"方式识别tRNA precursor的5'-leader RNA序列→将scissile phosphate精确定位在PIN域活性中心的Mg2+离子位点上。TPR域介导TRMT10C/MRPP1（含tRNA methyltransferase activity）和HSD17B10/MRPP2的组装——三者形成稳定的heterotrimeric MRPP1/2/3 RNase P holoenzyme。

**机制模型**：（1）线粒体tRNA 5'末端加工——PRORP（MRPP3）与MRPP1（TRMT10C）和MRPP2（HSD17B10）形成MRPP1/2/3复合体——识别线粒体tRNA precursor的cloverleaf二级结构——在5'leader和成熟tRNA 5'端交界处催化endonucleolytic cleavage——生成成熟tRNA 5'-monophosphate。（2）Perrault综合征（PMID:25254289）——PRORP变异导致卵巢发育不全和感音神经性耳聋（Perrault syndrome 3/PRLTS3）——由线粒体tRNA maturation缺陷→线粒体翻译受损→高能耗组织（卵母细胞、耳蜗毛细胞）功能丧失。（3）胞质N6AMT1翻译支持（PMID:39503847）——胞质N6AMT1-dependent translation影响线粒体RNA加工——揭示胞质-线粒体翻译的crosstalk。（4）Gambogic acid/Juglone抑制（PMID:36370850）——天然产物Gambogic acid和juglone（naphthoquinone）通过抑制RNase P活性发挥抗癌作用——机制尚待充分阐明。

**TE调控展望**：PRORP的TE调控为高度间接途径。线粒体功能与TE调控之间存在线粒体-核 retrograde signaling。线粒体tRNA加工缺陷→线粒体翻译受阻→mtDNA-encoded OXPHOS subunit合成减少→mitochondrial stress→mitochondrial unfolded protein response (UPRmt)→ATFS-1/ATF5/DVE-1 nuclear translocation→激活核基因（包括染色质修饰酶和转录因子）→可能影响TE区域的染色质状态。核质中的PRORP（与核RNase P/MRP亚基互作）可能参与核内非tRNA底物的RNA加工——包括含tRNA-like structure的TE RNA（如某些SINE/Alu和tRNA-derived SINE重复片段）——PRORP可能作为RNase P切割这些TE RNA→调控其表达和转座中间体。但此推测需实验支持。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRMT10C | STRING | 999 |
| POP5 | STRING | 963 |
| POP4 | STRING | 944 |
| POP7 | STRING | 937 |
| POP1 | STRING | 932 |
| RPP30 | STRING | 932 |
| RPP38 | STRING | 932 |
| RPP21 | STRING | 931 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O15091-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000100890-PRORP

![](https://images.proteinatlas.org/20459/1294_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/20459/1294_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/20459/1232_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/20459/1232_D4_3_red_green.jpg)
![](https://images.proteinatlas.org/20459/1199_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/20459/1199_D4_5_red_green.jpg)

### PubMed 文献

**PubMed count: 161**

| 42283975 | Comprehensive Insights into Perrault Syndrome: Genetic Diversity and Clinical Implications. | Reprod Sci 2026 |
| 41772230 | Expanding the genotypic spectrum of combined oxidative phosphorylation deficiency 54. | Neurogenetics 2026 |
| 41743505 | Isolated Lateral Meniscal Allograft Transplantation With an All-Soft Tissue Graft and Centralization. | Video J Sports Med 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PRORP

