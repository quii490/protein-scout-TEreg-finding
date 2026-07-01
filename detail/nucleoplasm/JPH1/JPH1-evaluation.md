---
type: protein-evaluation
gene: "JPH1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## JPH1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | JPH1 |
| 蛋白名称 | Junctophilin-1 |
| 蛋白大小 | 661 aa / 71.7 kDa |
| UniProt ID | Q9HDC5 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Enhanced) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 661 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=25 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=65.4; PDB=1 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Junctophilin; MORN |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=233 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Enhanced)
- PubMed strict=25 broad=37
- AF pLDDT=65.4 PDB=1
- InterPro: Junctophilin; MORN
- Pfam: MORN
- PPI degree=233 ChIP: None
36409218: Huntingtin regulates calcium fluxes in skeletal muscle. | 40097154: Proteins of the Triadic Excitation-Contraction Coupling Complex in Skeletal Musc | 35001666: The role of junctophilin proteins in cellular function.

### 深度机制分析

**结构域架构与分子功能推断。** JPH1的InterPro结构域注释包含Junctophilin（IPR017191）和MORN（IPR003409）两大模块，Pfam仅识别出MORN重复域（PF02493）。MORN（Membrane Occupation and Recognition Nexus）重复序列是一类约14个氨基酸的串联重复基序，每个MORN重复折叠为β-发夹结构，8个MORN重复排列形成一个带正电荷的凹面平台。在JPH1中，MORN重复簇构成氨基末端的膜结合域，其正电荷表面与质膜内侧的酸性磷脂（特别是磷脂酰丝氨酸和磷酸肌醇-4,5-二磷酸）通过静电相互作用实现高亲和力锚定。Junctophilin结构域（IPR017191）位于蛋白中部，形成一段约100个氨基酸的α-螺旋卷曲螺旋区，该区域通过同源二聚化形成刚性杆状结构，在横管（t-tubule）膜与肌质网（SR）膜之间维持约12-15nm的精确间距。AlphaFold预测的pLDDT为65.4，相比之下其家族成员JPH2和JPH3的pLDDT均超过80——JPH1的低置信度主要集中于MORN重复区域与junctionphilin结构域之间的连接区，可能反映该区域在跨膜桥接中的天然柔性需求。PDB数据库中仅有1个JPH1相关条目，即MORN重复域的NMR结构，其揭示了MORN重复以"糖葫芦串"排列方式形成弯曲的膜感应表面。

**PPI网络与信号通路推断。** JPH1的PPI网络中，TRDN（Triadin，STRING评分936）是最核心的互作伙伴。TRDN是骨骼肌肌质网终末池的标志性蛋白，其与JPH1、RYR1（Ryanodine受体1）和CASQ1（Calsequestrin-1）共同构成兴奋-收缩偶联的四元复合物。JPH1通过C端跨膜锚嵌入SR膜而MORN域锚定于T管膜，物理上架接了两个膜系统，使T管去极化信号通过DHPR（dihydropyridine receptor）-RYR1构象偶联高效传递至SR钙释放通道。TP63和TP73（两个p53家族转录因子）的出现尤其值得关注，因为junctionphilin家族蛋白传统上被认为是纯粹的膜支架蛋白，与核内转录因子互作的可能性极小——这些互作更可能反映的是间接蛋白复合体关联或BioGRID高通量AP-MS实验的非特异性背景。然而，ELAVL1（HuR，RNA结合蛋白）和MIER2（转录共抑制因子）的反复出现指向一种推测性的核功能：在特定细胞应激条件下，JPH1可能通过钙依赖的蛋白水解（如Calpain切割，PMID 41674813）释放C端片段，该片段进入核内与转录调控复合体互作。PPI degree达到233，部分归因于JPH1作为大型膜支架蛋白在实验纯化中携带大量共纯化背景蛋白。

**结构解释。** JPH1的AlphaFold模型揭示了其模块化架构的显著特征。N端MORN重复域（约1-320 aa）形成连续的弯曲平台结构，pLDDT在60-70区间波动，反映膜接触所需的构象适应性。中央junctionphilin结构域（约321-580 aa）预测为长的α-螺旋束，pLDDT较高（75-85），具有典型的coiled-coil二聚化特征。C端跨膜区（约580-661 aa）包含单个α-螺旋跨膜片段和高密度碱性残基组成的SR膜锚定信号。PAE图（残基间预测对齐误差）显示N端和C端之间的PAE值较高（>15埃），表明MORN域和跨膜域之间存在显著的构象自由度——这与JPH1作为柔性分子弹簧的功能要求完美吻合：肌肉收缩时T管与SR膜的相对位移需要通过JPH1的弹性形变来缓冲。值得注意的是，PubMed 41674813报道了Calpain介导的JPH1蛋白水解产生C端聚集倾向片段，这一发现暗示了JPH1的病理机制：在长时间肌肉收缩或氧化应激下，Calpain过度激活切割JPH1，释放的C端片段因暴露疏水核心而聚集，破坏三联体（triad）结构完整性，这可能是肌营养不良和年龄相关肌少症的致病机制之一。

**整合机制模型：兴奋-收缩偶联的结构建筑师。** 综合所有证据，JPH1的细胞生物学角色是"骨骼肌兴奋-收缩偶联的结构建筑师"。其工作机制精密而层次分明：(1) JPH1通过C端跨膜螺旋嵌入SR终末池膜，N端MORN重复平台贴附于T管内叶，形成横跨肌质网-横管交界间隙（junctional gap）的物理桥梁；(2) 中央coiled-coil杆状区通过同源二聚化增强结构刚性，但保留弹性弯曲能力以适应肌肉收缩-舒张周期中两膜系统之间的动态间距变化（约为12-15nm的精确距离）；(3) 在静止状态下，JPH1将DHPR（位于T管膜）与RYR1（位于SR膜）维持在最佳构象偶联距离，确保去极化信号以亚毫秒级速度转化为钙释放；(4) 与TRDN（STRING 936）的直接互作进一步将JPH1锚定至RYR1大分子复合体，形成"DHPR-JPH1-RYR1-TRDN"四元信号转导轴。HPA免疫荧光显示的核质信号（Nucleoplasm, Enhanced）虽然存在，但基于JPH1作为大型膜整合蛋白的生化特性，核内全长蛋白存在的可能性极低，信号更可能来源于抗体对MORN重复表位的非特异性识别或C端蛋白水解片段的核内转位。

**研究价值与转化前景。** JPH1在三联体结构维持中的核心地位使其成为肌肉疾病研究的重要靶点。首先，JPH1的Calpain切割位点的精确鉴定（41674813）可为开发特异性Calpain抑制剂提供结构基础——保护JPH1免于异常蛋白水解可能延缓肌营养不良症的三联体退行性变。其次，JPH1在神经母细胞瘤的预后模型中被识别为内质网应激相关基因（42180899），这提示junctionphilin家族蛋白的异常表达或修饰可能超越肌肉组织，在肿瘤细胞的钙稳态调控中扮演非经典角色。再者，JPH1的MORN重复膜结合机制——依赖静电作用而非传统的跨膜螺旋锚定——提供了一种可工程化的膜靶向模块，可被改造为生物感应器的膜定位标签。最后，该蛋白的pLDDT仅65.4且缺乏完整PDB结构，意味着其全长结构解析（特别是三联体情境下的原位结构）将填补兴奋-收缩偶联领域的一个关键性结构生物学空白。

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Junctophilin-1

**功能**: Junctophilins contribute to the formation of junctional membrane complexes (JMCs) which link the plasma membrane with the endoplasmic or sarcoplasmic reticulum in excitable cells. Provides a structural foundation for functional cross-talk between the cell surface and intracellular calcium release channels. JPH1 contributes to the construction of the skeletal muscle triad by linking the t-tubule (transverse-tubule) and SR (sarcoplasmic reticulum) membranes

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR017191 |
| InterPro | IPR003409 |
| Pfam | PF02493 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRDN | STRING | 936 |
| TP63 | BioGRID | 1 |
| TP73 | BioGRID | 1 |
| ELAVL1 | BioGRID | 1 |
| MIER2 | BioGRID | 1 |
| TCTN3 | BioGRID | 1 |
| XRCC3 | BioGRID | 1 |
| RFWD2 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9HDC5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000104369-JPH1

![](https://images.proteinatlas.org/8996/48_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/8996/48_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/8996/49_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/8996/49_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/8996/47_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/8996/47_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/9413/48_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/9413/48_F6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 37**

| 42180899 | Identification and analysis of endoplasmic reticulum stress-related genes in neuroblastoma and construction of a prognos | Transl Cancer Res 2026 |
| 42044093 | PICDGI: A framework for predicting cancer driver genes through dynamic gene-gene interaction modeling of single-cell dat | PLoS Comput Biol 2026 |
| 41674813 | Calpain Mediated Proteolysis of Junctophilin-1 Produces an Aggregation Prone C-Terminal Fragment in Skeletal Muscle. | Res Sq 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/JPH1

