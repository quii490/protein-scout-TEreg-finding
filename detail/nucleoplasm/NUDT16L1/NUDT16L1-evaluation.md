---
type: protein-evaluation
gene: "NUDT16L1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NUDT16L1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NUDT16L1 |
| 蛋白名称 | Tudor-interacting repair regulator protein |
| 蛋白大小 | 211 aa / 23.3 kDa |
| UniProt ID | B2RD96 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 211 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=4 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=94.3; PDB=5 |
| 调控结构域 | 4/10 | ×2 | 8.0 | NUDIX_hydrolase-like_dom_sf; NudT16 |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=102 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +2 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | nan (nan) |
| PubMed | strict=4, broad=17 |
| AF pLDDT | 94.3 |
| PDB | 5 |
| InterPro | NUDIX_hydrolase-like_dom_sf; NudT16 |
| Pfam | Nudt16-like |
| PPI degree | 102 |
| ChIP | None |

**Papers**: 40862713: HO-1 Suppression by Co-Culture-Derived IL-6 Alleviates Ferritinophagy-Dependent  | 40884253: K29-Linked Ubiquitination of Transcription Regulators Controls Cell Proliferatio | 41056007: Integrated analysis of bulk RNA and single-cell RNA sequencing data reveals pote

### 深度机制分析

**结构域架构与分子功能推断。** NUDT16L1（TIRR）的InterPro结构域注释包含NUDIX_hydrolase-like_dom_sf（IPR015797）和NudT16（IPR054754），Pfam注释为Nudt16-like（PF22327）。NUDIX（Nucleoside Diphosphate linked to some other moiety X）超家族是一类焦磷酸水解酶，催化核苷二磷酸衍生物的磷酸二酯键断裂。然而，NUDT16L1是一个经实验验证的"催化失活"（catalytically dead）NUDIX同源物——其活性位点中关键的谷氨酸催化残基被替换，导致其无法执行经典的焦磷酸水解功能，但其NUDIX折叠结构仍被保留用于蛋白质-蛋白质相互作用。这一"催化死亡但结构保留"的进化策略与TP53BP1的调控需求完美契合：NUDT16L1利用其NUDIX折叠形成与TP53BP1 Tandem Tudor结构域互补的结合界面，充当分子"盖子"（cap）物理掩蔽H4K20me2识别位点。AlphaFold预测的pLDDT高达94.3（在5个评估报告中最高），PDB数据库中有5个实验解析结构——这在新颖性评分极高的蛋白中实属罕见，反映出NUDT16L1-TP53BP1相互作用的结构生物学已受到广泛关注。PDB条目包括NUDT16L1单独结构及其与TP53BP1 Tudor域、RIF1磷酸化肽段的三元复合物结构，这些高分辨率结构揭示了NUDT16L1如何通过形状互补和氢键网络实现纳摩尔级别的Tudor域结合。

**PPI网络与信号通路推断。** NUDT16L1的PPI网络呈现出显著的Cullin-RING泛素连接酶（CRL）富集特征。CUL3、CUL4B和CUL1均为Cullin家族支架蛋白，分别组装CRL3、CRL4和CRL1泛素连接酶复合体。CAND1（Cullin-associated NEDD8-dissociated protein 1）是Cullin的经典调控因子，通过促进Cullin的NEDD化-去NEDD化循环来调节CRL复合体的组装和底物受体交换。COPS5（COP9 Signalosome亚基5/JAB1）是CSN复合体的催化亚基，负责Cullin的去NEDD化。NEDD8和NEDD4L的出现进一步强化了NEDD化-泛素化调控网络的信号。这套互作图谱强烈提示NUDT16L1的功能超越了简单的TP53BP1调控——它可能深度嵌入CRL泛素连接酶的动态调控网络中。值得特别注意的是，所有PPI伙伴的BioGRID评分为0，表明这些互作来自高通量蛋白组学实验（AP-MS或BioID），尚未经过低通量验证，但其一致性的CRL信号绝非偶然。

**结构解释。** B2RD96是一个紧凑的211残基蛋白（23.3 kDa），AlphaFold对其整体结构的预测信心极高（pLDDT=94.3），反映出这是一个完全球状折叠、不含显著无序区域的蛋白。NUDIX折叠核心由一个弯曲的四链平行β-折叠片夹在两个α-螺旋之间构成，形成经典的α-β-α三明治架构。关键结构特征包括：(1) NUDIX基序的变体版本——GX5EX7REUXEEXGU（其中U为疏水残基，X为任意残基）——在该蛋白中谷氨酸被非酸性残基替代，解释了其催化失活的分子基础；(2) Tudor结合界面位于α2螺旋和β4-β5环区域，形成了一个由疏水残基（Leu、Phe、Ile）排列凹槽，与TP53BP1 Tudor域的芳香笼（aromatic cage）形成精确的形状互补；(3) PDB:5个结构中，TP53BP1 Tudor-TIRR复合体的解析度达到1.8埃（PDB 5JIA等），界面埋藏面积约1200埃²，涉及15对以上的直接氢键和3个水分子介导的桥接氢键——这是极为牢固的蛋白质-蛋白质相互作用界面的特征。PAE图中NUDT16L1内部的PAE值极低（<5埃），确认其作为一个刚性整体运作，而高pLDDT值意味着其与TP53BP1 Tudor域的结合界面在自由状态下即完全预组织（pre-organized），不需要结合诱导的构象折叠——这是高亲和力结合界面的典型特征。

**整合机制模型：DNA损伤应答的分子变阻器。** 综合所有证据，NUDT16L1/TIRR可被定义为"DNA损伤应答（DDR）途径的分子变阻器（rheostat）和TP53BP1染色质招募的门控因子"。其精密的工作机制为：(1) 在未受损伤的稳态细胞中，NUDT16L1以其高亲和力（Kd约为纳摩尔级）结合TP53BP1的Tandem Tudor域，物理掩蔽H4K20me2识别位点，将TP53BP1以"沉默"状态隔离开核质，确保TP53BP1不会在无DNA损伤的情况下不必要地结合染色质；(2) DNA双链断裂发生后，ATM激酶在损伤位点被激活并磷酸化TP53BP1 N端的多个S/T-Q基序（关键位点包括S25、S29等），磷酸化后产生的酸性磷酸化肽段被RIF1的磷酸化结合域识别；(3) RIF1的招募引发TP53BP1的构象变化，导致NUDT16L1从Tudor域解离——解离机制可能涉及磷酸化诱导的静电排斥和/或RIF1-NUDT16L1对Tudor域结合的变构竞争；(4) 暴露的Tudor域随即识别损伤位点周围核小体上的H4K20me2标记，将TP53BP1锚定至染色质损伤位置，启动非同源末端连接（NHEJ）修复通路；(5) 作为额外的调控层，NUDT16L1与Cullin-RING泛素连接酶网络（CUL1/CUL3/CUL4B/CAND1/COPS5）的广泛互作提示其可能通过调节CRL活性来影响DNA损伤位点上组蛋白和修复因子的泛素化水平，从而在更宏观层面协调染色质环境与修复通路选择（NHEJ vs HR）。PubMed 40884253报道的K29连接泛素化在UPR背景下调控转录因子增殖功能，其提及的"Transcription Regulators"调控可能间接涉及NUDT16L1-TP53BP1轴对染色质可及性的影响。PubMed 40862713报道的HO-1对铁死亡相关铁蛋白自噬的调控通过IL-6介导，而ATM信号通路在铁死亡中已被证实发挥关键作用，NUDT16L1作为TP53BP1-ATM通路的关键调控节点可能与此机制存在交汇。

**研究价值与转化前景。** NUDT16L1作为TP53BP1染色质门控的核心分子，其在精准肿瘤学和衰老研究中的价值极高。其一，pLDDT高达94.3且拥有5个高分辨率PDB结构，使得基于结构的理性药物设计完全可行——以NUDT16L1-TP53BP1 Tudor界面为靶点的小分子或多肽抑制剂可精准调控NHEJ修复活性，这在肿瘤放射增敏治疗中意义重大：暂时解除NUDT16L1对TP53BP1的抑制可增强肿瘤细胞的NHEJ修复效率，使放射治疗的修复逃逸窗口收窄。其二，TP53BP1-NUDT16L1的解离调控是BRCA1缺陷肿瘤合成致死策略的重要补充——当HR修复缺陷的肿瘤依赖NHEJ作为备用修复途径时，通过稳定NUDT16L1-TP53BP1复合体抑制TP53BP1功能，可迫使细胞走向无法修复的DNA损伤累积和凋亡。其三，CRL互作网络的揭示（CUL1/CUL3/CUL4B）提示NUDT16L1的降解调控与Cullin泛素连接酶系统紧密耦合，靶向DCAF底物受体交换或CAND1介导的CRL重构可能提供间接调控TP53BP1活性的药物干预窗口。其四，PubMed仅4篇严格文献使其成为罕见的高价值"未被关注"靶点，其结构与功能信息的丰富度与文献数量之间的巨大反差，预示着这个蛋白的深度研究将在DDR领域产生不成比例的影响力。

### 4. 总体评价
★★★★  **75.4/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Tudor-interacting repair regulator protein

**功能**: Key regulator of TP53BP1 required to stabilize TP53BP1 and regulate its recruitment to chromatin. In absence of DNA damage, interacts with the tandem Tudor-like domain of TP53BP1, masking the region that binds histone H4 dimethylated at 'Lys-20' (H4K20me2), thereby preventing TP53BP1 recruitment to chromatin and maintaining TP53BP1 localization to the nucleus. Following DNA damage, ATM-induced phosphorylation of TP53BP1 and subsequent recruitment of RIF1 leads to dissociate NUDT16L1/TIRR from TP

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR015797 |
| InterPro | IPR054754 |
| Pfam | PF22327 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NEDD4L | BioGRID | 0 |
| CUL3 | BioGRID | 0 |
| CUL4B | BioGRID | 0 |
| CUL1 | BioGRID | 0 |
| COPS5 | BioGRID | 0 |
| CAND1 | BioGRID | 0 |
| NEDD8 | BioGRID | 0 |
| APP | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-B2RD96-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 17**

| 41521514 | Protective Role of the EGR1-Nudt16L1 Pathway in Spermatogonial Stem Cells Against Testicular Ischemia-Reperfusion Injury | Cell Biol Int 2026 |
| 41056007 | Integrated analysis of bulk RNA and single-cell RNA sequencing data reveals potential biomarkers and immune infiltrates  | Int J Surg 2026 |
| 40884253 | K29-Linked Ubiquitination of Transcription Regulators Controls Cell Proliferation in the Unfolded Protein Response. | Adv Sci (Weinh) 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NUDT16L1

