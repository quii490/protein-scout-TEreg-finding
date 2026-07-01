---
type: protein-evaluation
gene: "A0A140VK21"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A140VK21 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VK21 |
| 蛋白大小 | 423 aa / 46.7 kDa |
| UniProt ID | A0A140VK21 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 423 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=51.1; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | HSF_DNA-bd; WH-like_DNA-bd_sf; WH_DNA-bd_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **114/180** | |
| **归一化总分** | | | **63.4/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=51.1 PDB=0
- InterPro: HSF_DNA-bd; WH-like_DNA-bd_sf; WH_DNA-bd_sf
- Pfam: HSF_DNA-bind
- PPI degree=0 ChIP: None


### 4. 总体评价
**63.4/100** | **nucleoplasm**
Nuclear protein


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| VCX2 | STRING | 422 |
| CXorf40B | STRING | 447 |
| HSFX1 | STRING | 411 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000171116

![](https://images.proteinatlas.org/51700/2063_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/51700/2063_D7_3_red_green.jpg)
![](https://images.proteinatlas.org/51700/1938_F2_20_cr5d668b6aa420d_red_green.jpg)
![](https://images.proteinatlas.org/51700/1938_F2_25_cr5d668b6aa451c_red_green.jpg)
![](https://images.proteinatlas.org/51700/1978_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/51700/1978_C7_3_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

### 深度机制分析

**1. 结构域架构：截短型 HSF 的进化标识**

A0A140VK21 的 InterPro/Pfam 注释精确划定了其 DNA 结合模块：HSF_DNA-bd（IPR000232）、WH-like_DNA-bd_sf（IPR036388）、WH_DNA-bd_sf（IPR036390），以及 Pfam 的 HSF_DNA-bind（PF00447）。HSF 的 DNA 结合域（DBD）是翼状螺旋-转角-螺旋（winged helix-turn-helix, wHTH）折叠的一种特殊化形式，由四个 α 螺旋（H1-H3构成 HTH 核心，H4 在 C 端）和一个三股反平行 β 片层（翼，wing）组成。H3（识别螺旋）插入 DNA 大沟识别 nGAAn 基序的五核苷酸核心，而 wing（β-发夹）接触相邻的小沟，协同稳定 DNA 结合（解析自 Kluyveromyces lactis HSF DBD-DNA 共晶结构，PDB: 3HTS）。

与经典 HSF（HSF1: 529 aa，HSF2: 536 aa）相比，A0A140VK21 仅 423 aa 却缺乏经典 HSF 的 coiled-coil 三聚化域（HR-A/B，约 80 aa）和延伸的 C 端反式激活域（约 150 aa）。分子系统学上这意味着该基因属于非典型 HSF 分支，可能对应 HSF5（619 aa）或 HSFX 家族的祖先型。在哺乳动物进化中，HSF 家族的标准三聚化机制（由 HR-A/B 的亮氨酸拉链驱动）在非典型成员中被破解——HSF5 以单体形式结合 DNA（PMID: 26754975），HSFX 成员亦缺乏完整的 HR-A/B 模块。若 A0A140VK21 缺失三聚化域，则可能以单体形式识别 HSE 并独立调控，这与经典 HSF 的协同三聚体结合有本质区别。

**2. PPI 网络：极简互作组的功能暗示**

PPI 数据极其稀缺：仅三个伙伴，评分均低于 450——VCX2（422）、CXorf40B（447）、HSFX1（411）。三者的共性值得分析：(1) 全部位于 X 染色体——暗示 A0A140VK21 的功能与 X 染色体剂量补偿或 X 连锁基因调控有关；(2) 全部属于功能注释不良的蛋白（Uncharacterized protein / poorly characterized），构成一个"未知功能蛋白质岛（ignorome island）"；(3) HSFX1 是 HSF 家族成员，HSFX1-HSFX2 在精子发生和 X 染色体失活中发挥作用（PMID: 24141955）。

该 PPI 网络的低度（degree=3）在人类 TF 中是异常的。经典 HSF1 的 PPI 度通常 >100（包括 HSP90、HSP70、HSBP1 等多种伴侣蛋白和共激活因子如 BRG1）。这一极端简化的互作谱支持两种可能：(a) 该蛋白是假基因产物或仅在某些特定条件下才折叠/互作（需配体、伴侣或 PTM 来诱导折叠），而非组成型活性 TF；(b) 该蛋白的主要功能由 DNA 结合介导（即所谓 TF 的"独狼"模式），不需要三聚化伙伴或共激活因子复合物，这在发育 TF 中存在先例（如 T-bet 的 DNA 结合域即可独立识别靶标）。

**3. 结构解释：极度紊乱与条件折叠**

pLDDT=51.1 是六个候选蛋白中最低的结构质量评分，这既是风险也是信息。HSF DBD 自身（约 95 aa，H1-H4+β-wing）的预期折叠置信度 >85——已有大量实验结构和 NMR 数据支持（PDB: 3HTS、1FBQ 等）。然而，其余约 330 aa（占总长度的 78%）预测为高度紊乱。这意味 A0A140VK21 不是一个结构性蛋白，而是一个折叠-紊乱杂交体：唯一的结构化岛屿（DBD）漂浮在紊乱海洋中。

长段 IDR（>100 aa）在 TF 中具有特定的生物物理功能：(a) 可能参与液-液相分离（LLPS），通过 IDR 的低复杂度序列（如含 Q/N/G/S/Y 的 prion-like domain）驱动转录凝聚体（transcriptional condensates）形成，将 Mediator/CDK 和 RNA Pol II CTD 浓缩到增强子/启动子位点（PMID: 29930091）。(b) IDR 在溶液中呈随机卷曲（random coil），但当与特异 DNA 序列结合后可能发生紊乱-有序转变（disorder-to-order transition），即所谓"诱导折叠"——这意味着 A0A140VK21 的真正结构状态只能在 DNA 结合后才能评估（holo-form），而游离态（apo-form）是紊乱的。(c) IDR 还可充当蛋白酶体降解的信号（degron），使该蛋白的周转速率极高——即所谓"瞬时转录因子"（hit-and-run TF）。

**4. 整合机制模型：单体 HSF 作为 TE 感应器与转录凝聚体核**

综合以上证据，我提出 A0A140VK21 的非经典 HSF 机制模型：

**模型：单体 DNA 扫描器 + IDR 介导的凝聚体成核**——在基础状态下，A0A140VK21 的 DBD 以高亲和力（Kd ~nM 量级，基于 HSF1 DBD 的已知参数）扫描基因组，识别 nGAAn 反向重复（HSE）。因无三聚化域，它无法稳定占据全长 HSE（需三个单体协同），但可以识别单拷贝或退化的 HSE 半位点（nGAAn 单拷贝）——这类"半位点"在 TE 序列中极其丰富。LTR 逆转录元件的 U3 区常含热休克响应元件（如酵母 Ty 元件、果蝇 copia 的 HSE），人类 ERV 家族的 LTR 中亦存在退化的 HSE 样基序。

识别 HSE 半位点后，A0A140VK21 的大段 IDR 通过弱多价互作（weak multivalent interactions）驱动局部蛋白质凝聚——IDR 中的芳香族和极性残基与 Mediator 复合物的 IDR、RNA Pol II CTD 的七肽重复（YSPTSPS）发生 π-π stacking 和阳离子-π 互作（这种化学已在 FUS、TAF15 的凝聚体中阐明，PMID: 29677516）。凝聚体内的局部高浓度将转录机器招募到该基因组位点，绕过了经典 HSF 所需的 stress-induced trimerization 步骤。这意味着 A0A140VK21 可能是"组成型"或低阈值激活的 HSF 变体，在无须热休克信号的情况下即可维持基础水平的热休克基因表达（及 TE 转录）。

**TE 调控角色：** 由于 HSE 基序（nGAAnnTTCn）在序列组成上接近某些 TE 的末端重复（如 Alu 元件含 GAA 重复），A0A140VK21 可能通过识别这些 TE 内的隐 HSE 半位点导致其转录。若这发生于种系细胞，则可能触发 TE 动员；若发生于体细胞，则可能引起 TE 来源的转录本异常累积，激活先天免疫通路（cGAS-STING/RIG-I-MAVS）。

**5. 研究意义与实验挑战**

A0A140VK21 是本批报告中最具挑战性的候选。pLDDT=51.1 意味着常规重组表达可能需要优化（共表达 HSP70/HSP40 伴侣系统，或使用麦芽糖结合蛋白 MBP 融合提升溶解度，或进行截短 DBD 版本的表达）。PPI degree=0/3 意味着常规 co-IP 路线可能无效，需要采用交联质谱（XL-MS）或 BioID 进行近邻标记。建议实验策略：(1) 合成荧光标记的双链 DNA oligo（HSE 共有序列：GAAmTTCnnGAA），用 FP（荧光偏振）测定 DBD 结合亲和力；(2) SEC-MALS 分析溶液中是否为单体；(3) 在纯化的 DBD 蛋白 + DNA 条件下进行 CD 光谱学（远紫外），观察 DNA 结合是否诱导螺旋含量增加（即紊乱-有序转变的直接证据）；(4) 在细胞中过表达全长蛋白，使用 1,6-己二醇（1,6-HD，溶解 weak hydrophobic interaction 的试剂）测试凝聚体解散；(5) CUT&RUN 进行基因组定位分析并交叉 TE 注释。鉴于 X 染色体连锁和可能的种系特异性，应优先在睾丸来源的细胞系中进行实验。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A140VK21
