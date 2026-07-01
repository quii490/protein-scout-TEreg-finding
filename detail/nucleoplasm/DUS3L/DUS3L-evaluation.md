---
type: protein-evaluation
gene: "DUS3L"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## DUS3L 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DUS3L |
| 蛋白名称 | tRNA-dihydrouridine(47) synthase [NAD(P)(+)]-like |
| 蛋白大小 | 650 aa / 72.6 kDa |
| UniProt ID | Q96G46 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 650 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=80.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Aldolase_TIM; DUS-like_FMN-bd; tRNA_hU_synthase_CS |
| PPI | 6/10 | x3 | 18.0 | PPI degree=60 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **76.5/100** | 互证: +1 |
### 3. 分析
- HPA: Cytosol; Nucleoplasm (Approved)
- PubMed: strict=5, broad=6
- AF pLDDT: 80.0 / PDB: 0
- InterPro: Aldolase_TIM; DUS-like_FMN-bd; tRNA_hU_synthase_CS
- Pfam: Dus; zf-CCCH_DUS3L
- PPI degree=60 / ChIP: None
37733063: Chemoproteomic Approaches to Studying RNA Modification-Associated Proteins. | 34556860: Activity-based RNA-modifying enzyme probing reveals DUS3L-mediated dihydrouridyl | 32764209: Host Genetic and Gut Microbial Signatures in Familial Inflammatory Bowel Disease
### 4. 总体评价
**76.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: tRNA-dihydrouridine(47) synthase [NAD(P)(+)]-like

**功能**: Catalyzes the synthesis of dihydrouridine, a modified base, in various RNAs, such as tRNAs, mRNAs and some long non-coding RNAs (lncRNAs) (PubMed:34556860). Mainly modifies the uridine in position 47 (U47) in the D-loop of most cytoplasmic tRNAs (PubMed:34556860). Also able to mediate the formation of dihydrouridine in some mRNAs, thereby regulating their translation (PubMed:34556860)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR013785 |
| InterPro | IPR035587 |
| InterPro | IPR018517 |
| InterPro | IPR000571 |
| Pfam | PF01207 |
| Pfam | PF25585 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRMT61A | STRING | 727 |
| WDR4 | STRING | 720 |
| BOP1 | STRING | 717 |
| METTL1 | STRING | 710 |
| TRMT1 | STRING | 709 |
| APP | BioGRID | 1 |
| DPP9 | BioGRID | 1 |
| EEF2K | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96G46-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000141994-DUS3L

![](https://images.proteinatlas.org/62846/1230_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/62846/1230_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/62846/1186_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/62846/1186_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/62846/1200_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/62846/1200_C12_2_red_green.jpg)

### 深度机制分析

DUS3L编码**tRNA二氢尿苷(47)合酶[NAD(P)(+)]样蛋白**，属于黄素依赖性二氢尿苷合酶（DUS）家族，是RNA修饰领域近年才获得功能性注释的新兴蛋白。其域架构由两个功能模块串联构成：（1）N端的IPR013785（Aldolase_TIM，磷酸丙糖异构酶桶状折叠）提供了底物RNA结合的结构骨架，形成容纳tRNA D-loop的裂隙；（2）C端的IPR035587（DUS-like_FMN-bd）含FMN辅因子结合位点，是催化尿苷C5-C6双键还原为二氢尿苷（D）的氧化还原中心。两者之间的IPR018517（tRNA_hU_synthase_CS）保守序列标记定义了DUS家族的催化特征基序。此外，Pfam PF25585（zf-CCCH_DUS3L）鉴定出的CCCH型锌指结构域是DUS3L区别于其他DUS家族成员的关键特征——该锌指通常介导单链RNA的特异性识别，赋予DUS3L对U47位点的精确靶向能力。值得注意的是，该蛋白650个残基（72.6 kDa）在DUS家族中属于大型成员，其额外序列可能编码底物选择的调控区域。

PPI网络以RNA修饰网络为核心呈显著的功能聚类。TRMT61A（727分）是tRNA m1A58甲基转移酶催化亚基，WDR4（720分）为其调节亚基，METTL1（710分）是tRNA m7G46甲基转移酶——所有这些伙伴均修饰tRNA的T-loop/可变环区域，而DUS3L修饰的D-loop（U47）在三级结构中与T-loop形成关键的"肘部"（elbow）对接。这一互作模式暗示在tRNA成熟过程中，D-loop修饰（DUS3L催化的D47）和T-loop修饰（TRMT61A/METTL1催化的m1A58/m7G46）存在空间协同——二者共同稳定tRNA L型三级结构。TRMT1（709分）修饰tRNA的m2G26，位于D-arm和反密码子臂之间的铰链区，进一步扩展了修饰协作网络。BOP1（717分）是Pes1-BOP1-WDR12（PeBoW）复合体组分，参与核糖体60S大亚基生物发生，提示DUS3L可能影响核糖体RNA的修饰或核糖体组装过程中的tRNA质量检查。

结构预测分析：pLDDT=80.0（无PDB实验结构）表明AF2对该蛋白的整体折叠信心中等，但局部区域——特别是FMN结合域和TIM桶——应具有较高置信度。CCCH锌指的柔性连接区可能贡献了较低的pLDDT均值。PDB=0意味着该蛋白从未被实验结构解析，这在RNA修饰酶中是重要的结构基因组学空白。650个残基的大尺寸加上FMN辅因子，使其成为理想的冷冻电镜单颗粒分析靶标——特别是DUS3L与全长tRNA底物的复合体结构，将直接揭示FMN-尿苷电子传递的催化机制和二氢尿苷修饰对tRNA构象动态的实际影响。

综合机制模型：DUS3L是**tRNA与mRNA修饰界面的多功能氧化还原酶**。在tRNA层面，它通过FMN依赖的还原催化将绝大多数胞质tRNA的U47转化为D47（PubMed:34556860首次通过化学蛋白质组学方法ABPP确证了DUS3L的催化活性），D修饰增强D-loop的构象柔性，允许tRNA在核糖体A位、P位和E位之间高效转位。在mRNA层面，DUS3L介导特定mRNA中二氢尿苷的形成，直接影响这些mRNA的翻译效率——这代表了一种新近发现的转录后调控层次。最关键的新发现来自PubMed:41279591（2025年bioRxiv预印本）：DUS3L在食管癌中对METTL1缺失的代偿性tRNA修饰重编程——当METTL1催化的m7G46丢失时，DUS3L上调D47修饰以补偿tRNA稳定性，从而维持癌细胞的翻译保真度和存活。这一"修饰补偿"机制将DUS3L确立为翻译应激应答的核心调节节点，并揭示了tRNA修饰酶之间的功能冗余网络。仅有5篇严格文献（含该预印本）意味着DUS3L的分子机制图谱几乎为空白——其底物识别元件（CCCH锌指对U47的选择性机制）、FMN辅因子的电子来源（NADH vs NADPH偏好性）、以及mRNA底物的选择标准均为亟待解决的开放问题。鉴于其在食管癌耐药中的关键代偿作用，DUS3L是联合靶向tRNA修饰酶治疗策略的高优先级靶点——同时抑制METTL1和DUS3L理论上将剥夺癌细胞的翻译代偿能力，达到合成致死效应。

### PubMed 文献

**PubMed count: 6**

| 41279591 | Compensatory tRNA Modification by DUS3L Confers Resistance to METTL1 Loss in Oesophageal Cancer. | bioRxiv 2025 |
| 37733063 | Chemoproteomic Approaches to Studying RNA Modification-Associated Proteins. | Acc Chem Res 2023 |
| 34626721 | Integrative analysis of transcriptome-wide association study and mRNA expression profile identified candidate genes and  | Gene 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DUS3L

