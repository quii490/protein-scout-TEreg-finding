---
type: protein-evaluation
gene: "CAPRIN2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CAPRIN2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CAPRIN2 |
| 蛋白名称 | Caprin-2 |
| 蛋白大小 | 1127 aa / 125.9 kDa |
| UniProt ID | Q6IMN6 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Centrosome; Cytosol; Nucleoplasm (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 1127 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=26 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=51.8; PDB=5 |
| 调控结构域 | 4/10 | ×2 | 8.0 | C1q_dom; Caprin; Caprin-1_C |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=14 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +2 |

### 3. 分析
- Centrosome; Cytosol; Nucleoplasm (Supported)
- PubMed strict=26 broad=38
- AF pLDDT=51.8 PDB=5
- InterPro: C1q_dom; Caprin; Caprin-1_C
- Pfam: C1q; Caprin-1_C; Caprin-1_dimer
- PPI degree=14 ChIP: None
35051932: Transcriptional and Post-Transcriptional Regulation of Oxytocin and Vasopressin  | 26177727: Deficiency of the RNA binding protein caprin2 causes lens defects and features o | 34906599: RNA-binding proteins and post-transcriptional regulation in lens biology and cat

### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


**蛋白全称**: Caprin-2

**功能**: Promotes phosphorylation of the Wnt coreceptor LRP6, leading to increased activity of the canonical Wnt signaling pathway (PubMed:18762581). Facilitates constitutive LRP6 phosphorylation by CDK14/CCNY during G2/M stage of the cell cycle, which may potentiate cells for Wnt signaling (PubMed:27821587). May regulate the transport and translation of mRNAs, modulating for instance the expression of proteins involved in synaptic plasticity in neurons (By similarity). Involved in regulation of growth a

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001073 |
| InterPro | IPR028816 |
| InterPro | IPR022070 |
| InterPro | IPR041637 |
| InterPro | IPR008983 |
| Pfam | PF00386 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| COPS6 | BioGRID | 1 |
| PTEN | BioGRID | 1 |
| MEOX2 | BioGRID | 1 |
| NPM1 | BioGRID | 1 |
| FXR2 | BioGRID | 1 |
| FXR1 | BioGRID | 1 |
| BRD2 | BioGRID | 1 |
| LRP5 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：CAPRIN2（1127 aa，125.9 kDa）是mRNA结合和翻译调控蛋白，含三个特征结构域：N端C1q结构域（IPR001073, Pfam PF00386, ~50-140 aa）、中部Caprin二聚化结构域（IPR028816, IPR022070, Pfam Caprin-1_dimer, ~300-600 aa）和C端Caprin-1_C结构域（IPR041637, ~900-1127 aa）。C1q域折叠为紧凑的β-三明治结构——5条反平行β链形成两个β片层（β-jelly roll拓扑）back-to-back排列——经典功能为免疫防御分子（C1q补体成分、adiponectin、collagen VIII/X）的靶标识别基序，但在CAPRIN2中功能重新定向为RNA结合和蛋白互作。Caprin二聚化域为Caprin家族特征结构域——预测通过coiled-coil螺旋束介导同源二聚化（CAPRIN2/CAPRIN2）和异源二聚化（CAPRIN2/CAPRIN1）以形成功能二聚体或更高阶寡聚体。Caprin-1_C域富含RG/RGG重复序列和富含Pro/Ser区域——RGG box为典型的RNA结合模块，与mRNA通过π-π堆积（Arg guanidinium基团和碱基芳香环）和静电互作形成低亲和力但高动态的RNA-蛋白凝聚体。AlphaFold pLDDT=51.8的低置信度主要反映C1q域和Caprin-1_C域中的固有无序区段（IDR）——C1q域虽为β-三明治折叠核心但两侧长loop pLDDT下降至<50。整体上CAPRIN2以C1q折叠识别模块和Caprin-1_C RGG-IDR-RNA结合区为两级结构组织，通过二聚化域的寡聚化桥接形成高阶RNA-蛋白组装体。

**PPI互作网络解读**：PPI网络连接CAPRIN2至Wnt/β-catenin信号通路，同时揭示其在RNA颗粒生物学和应激颗粒调控中的次要功能。Wnt模块——LRP5（低密度脂蛋白受体相关蛋白5, Wnt共受体, BioGRID）和COPS6（COP9信号体亚基6, CSN6, 26S蛋白酶体盖/19S RP去NEDD化酶）构成核心Wnt调控轴。CAPRIN2通过Caprin-1_C域结合LRP5的胞内PPPSPxS基序→促进CDK14/CCNY磷酸化LRP5的Ser1490→招募Axin/GSK3β降解复合体至LRP5→阻断β-catenin磷酸化降解→β-catenin核转位和Wnt靶基因（MYC, CCND1, AXIN2）转录激活（PMID:18762581, PMID:27821587）。NPM1（核磷蛋白/B23, BioGRID互作）为核质-核仁穿梭蛋白，参与核糖体生物合成、p53-ARF肿瘤抑制通路和mRNA核糖核蛋白颗粒组装——NPM1-CAPRIN2互作提示CAPRIN2在核仁rRNA加工和核糖体亚基组装中具有次要功能位点。RNA颗粒模块——FXR1和FXR2（脆性X智力低下蛋白FMR1的常染色体同源物, BioGRID）为K同源（KH）结构域RNA结合蛋白，形成神经元RNA颗粒（neuronal granule）和应激颗粒（stress granule）的核心组分——CAPRIN2-FXR1/FXR2互作暗示CAPRIN2通过其RGG-box RNA结合域参与应激条件下（氧化应激、热休克、氨基酸饥饿）翻译停滞mRNA的储存和P-body/应激颗粒mRNP相分离动态。PTEN（磷酸酶和张力蛋白同源物, PI3K/AKT通路肿瘤抑制因子）和BRD2（bromodomain-containing protein 2, BET家族组蛋白乙酰化读取器）作为调控伙伴进一步扩展CAPRIN2的信号网络。

**结构解读**：CAPRIN2功能通过相分离机制（液-液相分离, LLPS）驱动。Caprin-1_C IDR中的RG/RGG重复序列为相分离的关键驱动力——精氨酸π-π堆积和π-cation（Arg-Trp/Tyr/Phe）互作提供芳香族氨基酸簇以稳定凝聚体核，而Pro/Ser/Gly赋予柔性和间隔。C1q域的低亲和力识别功能作为凝聚体的"受体"或"捕获模块"以招募特定mRNA底物和蛋白伙伴→增加局部大分子浓度→促进寡聚化和凝聚体成核。二聚化域通过coiled-coil螺旋束倍增结合价（valency）→每个CAPRIN2二聚体携带2个C1q域和2个RGG富含区——多价性是LLPS的主要贡献因素（avidity effect）。物理化学上，CAPRIN2凝聚体为无膜细胞器（非传统颗粒, RNP granule）的实现形式——在分子拥挤（macromolecular crowding ~100-300 mg/mL, 胞质生理条件）条件下，多价CAPRIN2/CAPRIN1同源/异源寡聚体和mRNA经多价弱互作（Kd ~1-10 μM/单个RGG-RNA interaction）超越饱和浓度（C_sat, 典型值~0.1-1 μM）后自发相分离。这一凝聚过程在体外可被1,6-己二醇（aliphatic alcohol, 破坏疏水π-π stacking和hydrogen bonding of LLPS）和盐浓度增加（高离子强度屏蔽charge-charge interaction）所干扰。

**机制模型**：（1）Wnt/β-catenin信号激活——CAPRIN2作为LRP6信号体的支架/适配器（scaffold/adaptor）。在Wnt3a配体结合Frizzled/LRP5/6受体后，CAPRIN2的C1q域识别LRP6胞内tail→Caprin-1_C域将CDK14/CCNY招募至LRP6→促进LRP6 PPPSPxS基序的Ser1490/Thr1479磷酸化→pLRP6为Axin-GSK3β-DVL复合体的高亲和力对接位点→GSK3β被扣押而无法磷酸化β-catenin→β-catenin稳定→核转位。G2/M期CDK14/CCNY活性达峰值，CAPRIN2增强LRP6的基础磷酸化（priming/许可状态），使细胞"准备就绪"以应对Wnt配体信号的突发（PMID:27821587）。（2）mRNA转运和局部翻译——在神经元中，CAPRIN2/CAPRIN1二聚体包裹Wnt信号通路成分的mRNA（Frizzled, LRP5/6, β-catenin/CTNNB1, TCF/LEF转录因子mRNA），作为RNP颗粒沿微管（kinesin-1/KIF5和dynein/dynactin运输系统）运输至树突和突触后致密区→响应突触激活信号的局部mRNA去抑制和翻译激活。CAPRIN2的相分离凝聚体在局部突触刺激（Ca²⁺ influx via NMDA receptors→CaMKII activation→CAPRIN2磷酸化→凝聚体解聚→mRNA释放→翻译激活）中可逆，实现mRNA活性的快速时空调控。（3）核质功能——NPM1-CAPRIN2互作将CAPRIN2连接至核仁-核质交界——核仁为rRNA加工和核糖体亚基组装的主要场所，CAPRIN2可能参与rRNA前体的加工或核糖体蛋白mRNA的核内代谢（选择性剪接、RNA编辑、出核转运）。NPM1的核质穿梭功能（NPM1含双向NLS和NES）可携带CAPRIN2短时进入核质执行特定功能后返回胞质。

**TE调控展望**：CAPRIN2通过Wnt/β-catenin通路和相分离RNA调控间接影响TE命运。Wnt/β-catenin是内源性逆转录病毒（ERV）特别是MMTV（mouse mammary tumor virus）和HERV-K/HML-2转录调控的重要信号通路——TCF/LEF转录因子的Wnt响应元件（WRE）常位于ERV的LTR调控区，β-catenin的核积累直接激活ERV-LTR启动子驱动其转录。CAPRIN2作为Wnt信号的正调控因子，可能间接增强ERV和LTR-TE（特别是MaLR和ERV1/ERVK LTR含cryptic WRE的家族）的转录活性。CAPRIN2的RGG相分离凝聚体可包裹和隔离TE衍生mRNA（如LINE-1 ORF1p-ORF2p bicistronic mRNA和SINE/Alu RNA）——当相分离异常时（如错误折叠蛋白和氧化应激诱导异常凝聚体固化/淀粉样变），释放的TE mRNA急剧增加翻译和转座活性。此外，BRD2（BET bromodomain蛋白, 识别H4K5ac/K8ac/K12ac乙酰化标记）是TE（HIV-1/HTLV-1 LTR）和LINE-1转录的调控因子——BRD2可通过招募CDK9/P-TEFb磷酸化RNA Pol II CTD激活转录延伸。CAPRIN2-BRD2互作可能将CAPRIN2的mRNA调控功能耦合至BRD2的染色质乙酰化信号读取和Pol II转录延伸调控。虽然CAPRIN2本身缺乏直接DNA结合能力，其Wnt信号支架功能和相分离mRNA调控为TE（特别是LTR-ERV）的转录和翻译提供了多层面的间接调控机制。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6IMN6-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000110888-CAPRIN2

![](https://images.proteinatlas.org/39746/425_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/39746/425_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/39746/427_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/39746/427_A9_3_red_green.jpg)
![](https://images.proteinatlas.org/39746/421_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/39746/421_A9_2_red_green.jpg)

### PubMed 文献

**PubMed count: 38**

| 41165022 | Targeting Ferroptosis in Nasopharyngeal Carcinoma: Mechanisms of Therapy Resistance and Therapeutic Opportunities. | Adv Biol (Weinh) 2025 |
| 40858046 | Correction: Structural insights into the Caprin-2 HR1 domain in canonical Wnt signaling. | J Biol Chem 2025 |
| 40837030 | Transcriptomic Profiles and Functional Correlates of Cancer-Related Fatigue: A Cross-Sectional Study in Women Undergoing | Eur J Cancer Care (Engl) 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CAPRIN2

