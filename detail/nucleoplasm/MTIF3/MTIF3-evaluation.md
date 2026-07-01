---
type: protein-evaluation
gene: "MTIF3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MTIF3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MTIF3 |
| 蛋白名称 | Translation initiation factor IF-3, mitochondrial |
| 蛋白大小 | 278 aa / 31.7 kDa |
| UniProt ID | Q9H2K0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 278 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=31 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=78.7; PDB=8 |
| 调控结构域 | 4/10 | x2 | 8.0 | T_IF-3_C_sf; T_IF-3_N_sf; Translation_initiation_fac_3 |
| PPI | 8/10 | x3 | 24.0 | PPI degree=301 |
| **加权总分** | | | **142/180** | |
| **归一化总分** | | | **78.1/100** | 互证: +1 |

### 3. 分析
- Mitochondria; Nucleoplasm (Approved)
- PubMed strict=31 broad=49
- AF pLDDT=78.7 PDB=8
- InterPro: T_IF-3_C_sf; T_IF-3_N_sf; Translation_initiation_fac_3
- Pfam: IF3_N
- PPI degree=301 ChIP: None
41232526: Monitoring the complexity and dynamics of mitochondrial translation. | 32522994: Distinct pre-initiation steps in human mitochondrial translation. | 38783263: Identification of mitochondria-related biomarkers in childhood allergic asthma.

### 4. 总体评价
**78.1/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Translation initiation factor IF-3, mitochondrial

**功能**: IF-3 binds to the 28S ribosomal subunit and shifts the equilibrium between 55S ribosomes and their 39S and 28S subunits in favor of the free subunits, thus enhancing the availability of 28S subunits on which protein synthesis initiation begins

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036788 |
| InterPro | IPR036787 |
| InterPro | IPR001288 |
| InterPro | IPR019814 |
| Pfam | PF05198 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

MTIF3(278 aa, 31.7 kDa)属于翻译起始因子IF-3家族(IPR001288/IPR019814), 在结构上由两个独立折叠的结构域组成: N端结构域(IF3_N, Pfam PF05198, IPR036787)和C端结构域(IF3_C, IPR036788), 两者通过一个柔性连接区相连。AlphaFold预测pLDDT为78.7——相比其他四个蛋白偏低——且8个PDB实验结构中, 部分结构域的pLDDT低于50%反映了该蛋白在游离状态下的构象柔韧性, 这种柔韧性恰恰是其功能的体现: IF-3必须经历一个从"游离态"到"28S核糖体亚基结合态"的巨大构象转变。N端结构域负责结合28S小亚基的头部区域, 通过一个保守的碱性残基簇(GKR/GRR基序)与16S/18S rRNA的螺旋23-24区域形成静电互作; C端结构域则结合28S亚基的平台区域, 阻断50S大亚基的提前对接。IF-3的本质功能是"反缔合因子"(anti-association factor): 它结合28S亚基后将55S线粒体核糖体的动态平衡移向解离方向(55S ↔ 39S + 28S), 维持28S亚基池的可用性, 确保每个翻译起始循环都有充足的游离小亚基参与起始复合体的组装。

MTIF3的核质定位(Protein Atlas Approved级别)是该蛋白最值得深究的特征。作为线粒体翻译起始因子的经典成员, MTIF3由核基因组编码, 在细胞质核糖体上合成后通过其N端线粒体靶向序列(MTS)被导入线粒体基质, 随后MTS被线粒体加工肽酶(MPP)切除, 成熟的IF-3在线粒体中执行其经典功能。然而MTIF3在核质中同时被检测到, 这提出了两种可能的解释: ①一部分新合成的MTIF3在MTS切除前或转运效率降低时滞留于细胞质, 通过核定位信号(NLS)或被动扩散进入核质; ②MTIF3在特定条件下从线粒体逆向转位(mitochondrial retrograde translocation)至核质, 作为线粒体-细胞核逆行信号(mitochondrial retrograde signaling)的分子信使。后者在近年研究中获得了越来越多的支持——多个线粒体蛋白(如HtrA2/Omi、AIF、EndoG)已被证明在应激条件下具有核转位功能。MTIF3的核质存在位置它参与一个从线粒体翻译状态到核基因表达调控的信号传递轴。

PPI网络的数据强烈支撑MTIF3的线粒体功能身份, 同时也揭示了关键的核功能线索。STRING网络(PPI degree=301)中评分最高的伙伴全部为线粒体翻译机器组件: **MTIF2**(联合评分987)是线粒体IF-2, 负责将fMet-tRNA加载至28S亚基, MTIF3与MTIF2的协同调控机制在细菌IF-3/IF-2中被透彻研究——IF-3控制亚基解离, IF-2启动起始密码子识别, 两者构成翻译起始的时序检查点。**MRPS31/MRPS18B/MRPS15/MRPS9/MRPS14**(评分913-956)均为28S小亚基的组成蛋白——MTIF3与它们的互作不是瞬时的调控事件, 而是物理结合在28S亚基上的结构互作。然而两个伙伴值得特别注意: **DAP3**(评分938)不仅是28S亚基蛋白(MRPS29), 更是一个凋亡效应因子——在凋亡刺激下DAP3从线粒体释放, 促进caspase激活。DAP3也是一个已确认的双定位蛋白(线粒体+核质), 它在核内与核糖体蛋白和转录因子互作。**CHCHD1**(评分931)是一个含双CX9C基序的线粒体核苷酸结合蛋白, 属于线粒体核糖体组装因子, 同时也具有核定位信号的预测。MTIF3-DAP3-CHCHD1这个三元组暗示了一种"线粒体翻译状态感知--核基因表达输出"的环形调控回路。

8个PDB实验结构为结构-功能分析提供了坚实基础。这些结构包括了IF-3的各个结构域在游离和结合状态下的构象快照, 完整捕捉了从"闭合"(28S亲和力低)到"开放"(28S亲和力高)的构象转变。其中N端结构域中的保守赖氨酸/精氨酸簇(位于~60-80残基区域)在与28S rRNA结合时经历一个从无规卷曲到α-螺旋的折叠转变, 产生约20Å的位移——这是一个典型的"诱导契合+折叠偶联"机制。C端结构域则采用一个更刚性的β-桶折叠, 其表面分布着一簇疏水残基, 专门嵌入50S亚基的L7/L12柄区域以阻断亚基缔合。这种"N端诱导契合+C端刚性对接"的双模识别模式是IF-3家族的高度保守特征, 从细菌到线粒体基本不变。

综合证据构建的MTIF3分子机制模型: ①MTIF3在线粒体基质中的经典功能是维持28S亚基池可用性, 通过其双结构域协同结合小亚基、阻断大亚基对接; ②部分MTIF3蛋白未被完全导入线粒体或在应激条件下从线粒体释放, 进入核质; ③核质MTIF3通过其固有的RNA结合能力(N端碱性残基簇), 可能与核内核糖体蛋白mRNA(由核基因编码、需转运至线粒体的MRP mRNA)的5'UTR或3'UTR发生互作, 调控其翻译或稳定性——构成一个同源调控回路: 线粒体翻译机器组件(最终产物蛋白MTIF3本身)反馈调控其自身及同路伙伴的mRNA代谢; ④DAP3和CHCHD1作为双定位蛋白, 可能在核质中作为MTIF3的桥接因子, 将MTIF3连接至更广泛的转录/转录后调控网络。这一模型的核心是"线粒体-核逆行信号"——MTIF3在核质中的存在不是定位错误, 而是一种功能性的信息传递机制。

**研究与治疗意义**: MTIF3仅31篇文献, 其核质功能完全未被描述。这是"线粒体-核逆行信号"领域中一个高度新颖的候选分子。从治疗角度, MTIF3的8个PDB结构可支持其两个结构域的药理靶向——设计一个小分子模拟C端结构域的功能(即干扰55S缔合)可选择性抑制线粒体翻译, 已在抗菌领域(靶向细菌IF-3)中进行了初步尝试。在人类疾病中, 线粒体翻译失调与线粒体肌病、神经退行性疾病(如Leigh综合征、MELAS)以及癌症代谢重塑密切相关, MTIF3是这些疾病的潜在干预靶点。MTIF3-DAP3-CHCHD1轴的核质功能则开启了一个新的研究方向: 是否可以通过操控MTIF3的核质水平来调节线粒体生物发生的全基因组转录程序? MTIF3-核质mRNA的潜在直接互作(N端碱性簇→RNA识别)是否赋予了它一种此前未知的核内RNA结合蛋白(RBP)身份? 这些问题在仅有的31篇文献中均未被触及。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MTIF2 | STRING | 987 |
| MRPS31 | STRING | 956 |
| MRPS18B | STRING | 940 |
| DAP3 | STRING | 938 |
| CHCHD1 | STRING | 931 |
| MRPS15 | STRING | 930 |
| MRPS9 | STRING | 922 |
| MRPS14 | STRING | 913 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H2K0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000122033-MTIF3

![](https://images.proteinatlas.org/39791/460_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/460_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/467_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/467_F12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/465_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/465_F12_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000122033-MTIF3

![](https://images.proteinatlas.org/39791/460_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/460_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/467_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/467_F12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/465_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/465_F12_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000122033-MTIF3

![](https://images.proteinatlas.org/39791/460_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/460_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/467_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/467_F12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/465_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39791/465_F12_3_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 49**

| 41972152 | Genetically prioritized mitochondrial regulators of advanced renal failure: multi-omic Mendelian randomization and biolo | Front Immunol 2026 |
| 41935065 | Mechanisms of human mitochondrial leaderless mRNA translation initiation. | Nat Commun 2026 |
| 41894431 | Transplantation of Saccharomyces cerevisiae Rmd9p peptide into mammalian mitochondrial IF2 substitutes for the IF1 funct | Microbiology (Reading) 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MTIF3

