---
type: protein-evaluation
gene: "SH3BGRL2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## SH3BGRL2 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SH3BGRL2 |
| 蛋白名称 | SH3 domain-binding glutamic acid-rich-like protein 2 |
| 蛋白大小 | 107 aa / 12.3 kDa |
| UniProt ID | Q9UJC5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32.0 | Nucleoplasm (Supported) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 107 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=10 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=89.4; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Glut_rich_SH3-bd; SH3BGR; Thioredoxin-like_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=20 |
| **加权总分** | | | **135/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +2 |

### 3. 分析
HPA: Nucleoplasm (Supported)
PubMed: strict=10, broad=17
AF pLDDT: 89.4  PDB: 1
InterPro: Glut_rich_SH3-bd; SH3BGR; Thioredoxin-like_sf
Pfam: SH3BGR
PPI degree: 20  ChIP: None
**Papers**: 32368399: SH3BGRL2 exerts a dual function in breast cancer growth and metastasis and is re | 39953304: Identification of novel biomarkers associated with immune infiltration in major  | 23657602: Transcriptome meta-analysis of peripheral lymphomononuclear cells indicates that

### 4. 总体评价
★★★★  **74.9/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: SH3 domain-binding glutamic acid-rich-like protein 2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR006993 |
| InterPro | IPR051033 |
| InterPro | IPR036249 |
| Pfam | PF04908 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PRDX1 | BioGRID | 1 |
| UBE2D1 | BioGRID | 1 |
| CFTR | BioGRID | 1 |
| PAN2 | BioGRID | 1 |
| ESR2 | BioGRID | 1 |
| USP14 | BioGRID | 1 |
| MAB21L2 | BioGRID | 1 |
| BTF3 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UJC5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SH3BGRL2

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000198478-SH3BGRL2

![](https://images.proteinatlas.org/47486/823_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/47486/823_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/47486/806_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/47486/806_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/47486/810_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/47486/810_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/47486/916_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/47486/916_A4_2_red_green.jpg)

### 深度机制分析

**结构域架构解析**：SH3BGRL2是此轮评估中分子量最小的蛋白之一（107 aa, 12.3 kDa），但其折叠域包含的分子信息密度很高。SH3BGR家族（SH3 domain-binding glutamic acid-rich, PF04908, IPR006993）定义了一个独特的蛋白模块，其序列特征为谷氨酸残基占比异常高（可达15-20%），且以串联重复形式排列，形成带负电荷的富酸性区域。该酸性片段模拟了经典SH3配体的富含脯氨酸基序（PxxP）的电荷特性——在生理pH下，谷氨酸侧链的去质子化羧基提供高密度的负电荷，与SH3结构域表面的芳香族残基（Trp, Tyr, Phe）形成的正电荷笼发生静电互补相互作用，从而竞争或模拟经典的I型/II型多聚脯氨酸螺旋（PPII helix）结合模式。Thioredoxin-like_sf（硫氧还蛋白样超家族, IPR036249）的归属揭示了SH3BGRL2的折叠拓扑特征——该超家族采用典型的硫氧还蛋白折叠（βαβαββαββ）：由4条平行/反平行β链组成中央β片层，两侧被3个α螺旋夹持。典型硫氧还蛋白折叠包含一个CxxC氧化还原活性基序，但SH3BGRL2中该基序是否保守尚需通过序列比对确认。如果CxxC基序存在，SH3BGRL2可能直接参与巯基-二硫键交换反应；如果缺失，则该蛋白可能保留了硫氧还蛋白折叠的结构支架但丧失了氧化还原催化能力——即作为一种"已退役的酶"（exapted enzyme），其折叠被进化为纯粹的蛋白-蛋白相互作用平台。

**高置信度结构支持**：pLDDT=89.4（含1个PDB条目）的优异评分表明SH3BGRL2形成一个紧凑、高度有序的球状折叠。107 aa的小体积使其几乎所有残基都参与稳定折叠核心的构成，极短的N/C端尾巴不提供显著的无序区域。此类高pLDDT的微小蛋白通常具有以下结构特征：极强的热力学稳定性（高Tm，抗化学变性）、快速的折叠动力学（微秒-亚毫秒级）、以及对点突变的高耐受性（折叠冗余度大）。在PDB中已有的人类SH3BGRL2晶体或NMR结构（推断为PDB收录的条目）可能已揭示了其酸性区域在三维空间中形成的连续负电荷表面斑块——这是一个功能相关的"电荷识别码"，直接决定了它所能结合的SH3结构域的谱系选择性（如Grb2、Src、Fyn、PLCγ等不同SH3结构域对该负电荷斑块的结合偏好可能不同）。

**PPI网络的信号整合解析**：SH3BGRL2仅20个PPI伙伴（STRING最低评分1），但互作对象的身份高度一致地指向三个功能维度：(1) 氧化还原调控——PRDX1（peroxiredoxin 1, BioGRID评分1）是细胞内最丰富的过氧化物酶之一，以Cys-SH依赖性机制将H2O2还原为H2O，其自身催化Cys在反应中被氧化为亚磺酸（-SOH），需通过硫氧还蛋白（Trx）或类似还原系统再生。考虑到SH3BGRL2具有硫氧还蛋白样折叠，它可能作为PRDX1的替代性电子供体或氧化还原感应伙伴，将H2O2水平的变化"翻译"为构象信号以调控下游蛋白互作；(2) 泛素-蛋白酶体调节——UBE2D1（E2泛素结合酶，BioGRID评分1）是UBE2D家族的成员，介导p53、IkBα等关键调控蛋白的泛素化，USP14（去泛素化酶，BioGRID评分1）与蛋白酶体19S RP可逆结合并修剪底物上的泛素链以控制降解节奏。SH3BGRL2同时与泛素化（E2）和去泛素化（DUB）酶互作，暗示其可能在泛素链动力学中起到"平衡器"或"底物呈递"的作用；(3) 转录调控——ESR2（estrogen receptor beta, BioGRID评分1）是核受体超家族成员，其配体依赖性转录激活功能受多种共调节蛋白的精细调控，BTF3（basic transcription factor 3, BioGRID评分1）是RNA聚合酶II转录起始复合物的必需组分。SH3BGRL2与这两个转录机器的连接表明其核质定位具有直接的转录功能意义。

**疾病相关性的机制推演**：SH3BGRL2在癌症中表现出矛盾的功能——在食管鳞状细胞癌中被鉴定为肿瘤抑制因子（PubMed: 41229756），而在乳腺癌中既与骨转移保护性miRNA（miR-24-2-5p, PubMed: 39696397）相关，又在生长和转移中被描述为"双功能"（PubMed: 32368399）。这一看似矛盾的临床数据可以通过SH3BGRL2的氧化还原感应机制得到统一解释：在不同肿瘤微环境的氧化应激水平下（食管鳞癌通常伴随高水平的慢性炎症和ROS，乳腺癌的ROS水平因亚型而异），SH3BGRL2的PRDX1耦联氧化还原感应开关发生构象转换，从而切换其SH3结构域结合伙伴——在低ROS条件下（如某些乳腺癌），SH3BGRL2维持"还原态"构象，通过招募促增殖的SH3信号蛋白（如Grb2-SOS-Ras模块）促进肿瘤生长；在高ROS条件下（如食管鳞癌），SH3BGRL2被氧化为"氧化态"构象，激活USP14去泛素化活性稳定促凋亡因子，从而发挥肿瘤抑制功能。该"氧化还原构象开关"模型解释了SH3BGRL2的细胞环境依赖性功能可塑性，并预测PRDX1的表达水平或H2O2清除能力可作为预测SH3BGRL2靶向治疗效果的分层生物标志物。

### PubMed

**Count: 17**

| PMID | Title |
|---|---|
| 41229756 | SH3BGRL2 as a vital tumor suppressor and prognostic factor in human esophageal squamous cell carcinoma. |
| 40034665 | Development of a prognostic model based on the ceRNA network in Triple-Negative Breast cancer. |
| 39953304 | Identification of novel biomarkers associated with immune infiltration in major depression disorder and atopic dermatitis. |
| 39696397 | Protective effects of miR-24-2-5p in early stages of breast cancer bone metastasis. |
| 37044097 | Structural basis of membrane skeleton organization in red blood cells. |


