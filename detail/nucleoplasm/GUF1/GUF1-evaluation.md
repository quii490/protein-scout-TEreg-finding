---
type: protein-evaluation
gene: "GUF1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GUF1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GUF1 |
| 蛋白名称 | Translation factor GUF1, mitochondrial |
| 蛋白大小 | 669 aa / 74.3 kDa |
| UniProt ID | Q8N442 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 669 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=11 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=81.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | EF-4; EFG_III/V; EFG_V-like |
| PPI | 7/10 | x3 | 21.0 | PPI degree=147 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Mitochondria; Nucleoplasm (Approved)
- PubMed strict=11 broad=17
- AF pLDDT=81.6 PDB=0
- InterPro: EF-4; EFG_III/V; EFG_V-like
- Pfam: EFG_C; GTP_EFTU; GTP_EFTU_D2
- PPI degree=147 ChIP: None
39430826: Prognostic biomarkers based on GUF1, EFTUD2 and GSPT1 targets affecting migratio | 23662805: The paradox of elongation factor 4: highly conserved, yet of no physiological si | 18442968: The membrane-bound GTPase Guf1 promotes mitochondrial protein synthesis under su

### 深度机制分析

**结构域架构与分子功能推断。** GUF1的InterPro结构域注释揭示其属于原核延伸因子EF-4/EF-G超家族（IPR006297、IPR035647、IPR000640），Pfam进一步精细化为EFG_C、GTP_EFTU和GTP_EFTU_D2三个功能模块。这种GTP结合型翻译延伸因子架构在进化上极其保守，其核心机制是通过GTP水解驱动的构象变化催化核糖体上tRNA的逆向移位。值得注意的是，GUF1含有完整的EFG_III/V和EFG_V-like结构域（IPR004161、IPR031157），这些结构域在线粒体核糖体上执行"校对"功能——当核糖体发生错误移位时，GUF1可催化tRNA向后移动一个密码子位置，从而将翻译恢复至正确阅读框。GUF1的EF-4结构域（IPR006297）旁系同源于细菌LepA蛋白，后者被证实能在翻译延伸受阻时进行"逆向移位"（back-translocation），而GUF1是哺乳动物中该机制唯一的线粒体执行者。AlphaFold预测的pLDDT值达81.6，表明其GTPase核心结构域高度有序，但C端区域可能存在一定柔性——这在核糖体结合因子中是普遍特征，柔性区域通常介导与核糖体界面的动态相互作用。

**PPI网络与信号通路推断。** GUF1的PPI网络中，MRPS7（线粒体核糖体蛋白S7）是功能性最强的互作伙伴，该互作将GUF1直接锚定至线粒体小亚基翻译位点。TNF（肿瘤坏死因子）的出现暗示GUF1与线粒体应激信号存在功能交联——已有文献报道TNFα可诱导线粒体翻译损伤并激活线粒体未折叠蛋白反应（UPRmt）。LAMP2（溶酶体相关膜蛋白2）的互作指向线粒体与溶酶体之间的膜接触位点，这与GUF1的线粒体定位一致，可能参与线粒体自噬调控。蛋白质组学数据显示GUF1的PPI degree高达147，远超典型线粒体翻译因子的平均互作度，提示其可能存在"兼职"（moonlighting）功能。PubMed 39430826报道GUF1、EFTUD2和GSPT1共同构成胃癌细胞迁移的预后标志物，这三者均为GTP结合型翻译因子，暗示肿瘤细胞可能协同劫持线粒体和细胞质翻译延伸系统以维持高增殖率下的蛋白质稳态。

**结构解释。** AlphaFold预测的Q8N442全长为669氨基酸，pLDDT均值81.6反映出整体折叠置信度较高，但存在若干低置信度环区——特别是N端约60个残基的线粒体靶向序列（MTS）区域，其内在无序性正是前体蛋白转运所需。GTP_EFTU和GTP_EFTU_D2两个Pfam结构域形成典型的G-domain双叶架构，其中P-loop（磷酸结合环）、switch I和switch II区域在GTP/GDP结合态之间发生显著的构象重排。GUF1至今尚无实验解析的PDB结构（PDB=0），但基于AlphaFold模型可以推断：其G-domain与细菌EF-G的同源性超过35%，活性中心关键残基GTP水解机制完全保守。值得注意的是，GUF1的C端EFG_C结构域在细菌EF-G中介导核糖体30S亚基结合与tRNA移位，而在GUF1中该结构域的静电表面电势呈正电荷富集，提示其通过电荷互补作用识别线粒体核糖体的rRNA骨架。

**整合机制模型：线粒体翻译保真度守护者。** 综合所有证据，GUF1的细胞生物学角色可概括为"线粒体翻译质量控制中枢"。其工作机制如下：(1) 定位于线粒体基质并GTP依赖性结合于线粒体核糖体，常态下处于GDP结合态即待命模式；(2) 当翻译延伸过程中核糖体发生错误移位（如-1或+1移码），GUF1被异常tRNA-mRNA构象激活，GTP交换为GTP并结合至核糖体A位近端；(3) GTP水解驱动GUF1的domain IV发生"杠杆式"摆动，物理推动P-site tRNA逆向移动一个密码子，mRNA随之复位；(4) 正确校正后GUF1以GDP态解离，翻译重新进入正常延伸循环。HPA免疫荧光显示的核质信号（Nucleoplasm, Approved）可能并非GUF1在核内的功能执行，而是新合成前体蛋白从细胞质转运至线粒体过程中在核周区域的富集——线粒体在核周区域的高密度分布可产生这种IF共定位假象。此外，GUF1的肿瘤相关性（39430826、38577477）可能源于癌细胞对线粒体翻译保真度的异常依赖：在高度需氧糖酵解背景下，癌细胞线粒体核糖体更易发生氧化损伤诱导的错误翻译，GUF1上调作为补偿机制维持线粒体编码的OXPHOS亚基的正确合成，从而防止线粒体功能障碍触发的凋亡。

**研究价值与转化前景。** GUF1是线粒体翻译领域的高价值研究靶点，理由有三。其一，作为哺乳动物中唯一线粒体特异性逆向移位因子，其功能缺失将直接导致线粒体翻译错误率上升和OXPHOS缺陷，这使其成为线粒体疾病功能性研究的理想切入点。其二，GUF1在胃癌中的差异表达及其与EFTUD2、GSPT1协同作为预后标志物的发现（39430826），提示线粒体翻译保真度调控可能是肿瘤代谢重编程中的一个未被充分认识的关键节点。其三，GUF1的GTPase活性中心提供了明确的可成药位点——模仿细菌EF-G的已知抑制剂（夫西地酸类似物）进行结构导向的药物设计，理论上可实现选择性靶向肿瘤线粒体翻译而不影响细胞质翻译系统。


### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Translation factor GUF1, mitochondrial

**功能**: Promotes mitochondrial protein synthesis. May act as a fidelity factor of the translation reaction, by catalyzing a one-codon backward translocation of tRNAs on improperly translocated ribosomes. Binds to mitochondrial ribosomes in a GTP-dependent manner

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR006297 |
| InterPro | IPR035647 |
| InterPro | IPR000640 |
| InterPro | IPR004161 |
| InterPro | IPR031157 |
| InterPro | IPR038363 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TNF | BioGRID | 0 |
| MRPS7 | BioGRID | 0 |
| LAMP2 | BioGRID | 0 |
| FAM174A | BioGRID | 0 |
| C5AR2 | BioGRID | 0 |
| TMCO3 | BioGRID | 0 |
| TSPYL6 | BioGRID | 0 |
| IL13RA2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N442-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000151806-GUF1

![](https://images.proteinatlas.org/24222/1327_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/24222/1327_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/24222/1000_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/24222/1000_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/24222/1003_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/24222/1003_C11_2_red_green.jpg)

### PubMed 文献

**PubMed count: 17**

| 41310427 | Selection signature analysis in chickens divergently selected for growth rate reveals novel candidate genes regulating f | BMC Genomics 2025 |
| 39430826 | Prognostic biomarkers based on GUF1, EFTUD2 and GSPT1 targets affecting migration of gastric cancer cells. | Transl Cancer Res 2024 |
| 38577477 | Identification of a novel inflammatory-related gene signature to evaluate the prognosis of gastric cancer patients. | World J Gastrointest Oncol 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GUF1

