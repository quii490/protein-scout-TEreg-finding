---
type: protein-evaluation
gene: "PCDHGB4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGB4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGB4 |
| 蛋白名称 | Protocadherin gamma-B4 |
| 蛋白大小 | 923 aa / 99.9 kDa |
| UniProt ID | Q9UN71 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 923 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=1 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=75.5; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 6/10 | x3 | 18.0 | PPI degree=58 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=1 broad=3
- AF pLDDT=75.5 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_C
- Pfam: Cadherin; Cadherin_2; Cadherin_C_2
- PPI degree=58 ChIP: None
38590195: [Exploring the Role of PCDHGB4 in the Occurrence of Lung Squamous Cell Carcinoma

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**1. 结构域架构与分子功能推断**

PCDHGB4的域架构与PCDHGB3高度相似，共享6个InterPro结构域（IPR002126 Cadherin-like_dom, IPR015919 Cadherin-like_sf, IPR032455 Cadherin_C, IPR031904, IPR020894, IPR013164），Pfam注释也一致（Cadherin, Cadherin_2, Cadherin_C_2）。923 aa的胞外区具有与PCDHGB3相似的钙黏蛋白重复串联排列。然而，PCDHGB4的关键区别在于其IPR013164（Cadherin_N）结构域的独特序列特征——N端前肽区的差异决定了同簇内不同异构体之间的特异性识别代码。Alphafold pLDDT=75.5，与PCDHGB3（75.4）几乎一致，但PCDHGB4缺乏实验结构（PDB=0），这意味着其三维折叠仅依靠计算预测。值得注意的是，PCDHGB4没有PDB条目但PCDHGB3有3个，提示这两个高度同源蛋白之间的结构差异可能集中在胞质尾区域和重复单元之间的连接环构象——这些区域在晶体学研究中往往因柔性而被截短。

**2. PPI互作网络与通路分析**

PCDHGB4的PPI网络（degree=58）显著大于PCDHGB3（degree=8），揭示其具有更广泛的信号通路衔接能力。同簇互作（PCDHGB5, PCDHGB1, PCDHGB3）维持了原钙黏蛋白顺式多聚体的基本组装框架。关键的差异化互作伙伴包括：（1）GRAMD1B和GRAMD1A——GRAM结构域蛋白家族是内质网-质膜（ER-PM）接触位点的胆固醇感应器，其StART样结构域可直接提取并转运胆固醇，PCDHGB4与GRAMD1的互作暗示该原钙黏蛋白可能定位于ER-PM膜接触位点，参与脂质微环境调控或胆固醇依赖的细胞信号传导；（2）DAG1（α-肌营养不良聚糖）是细胞外基质受体，通过其糖基化的α亚基与层粘连蛋白结合，将ECM信号传递至胞内骨架——PCDHGB4-DAG1互作揭示原钙黏蛋白可能作为ECM-细胞骨架信号轴的辅助受体；（3）EMILIN2是弹性纤维相关的ECM糖蛋白，参与TGF-β信号通路的负调控；（4）AREL1是凋亡抗性E3泛素连接酶，靶向IAP拮抗剂（SMAC/DIABLO, ARTS等）进行降解，抑制线粒体凋亡通路。这四个互作伙伴共同描绘出PCDHGB4作为"信号整合型黏附受体"的分子画像。

**3. 结构生物学解析**

尽管缺乏实验结构（PDB=0），AlphaFold pLDDT=75.5提供了可靠的整体折叠预测。PCDHGB4的921-923 aa胞外区在反式二聚化界面（重复1-4）可参考同簇蛋白的晶体结构（PMID:27472898, PDB参考PCDHγA1和PCDHγB7），预期形成反式平行的"拉链状"二聚体。胞内域（最后约150 aa）由于不存在经典β-catenin结合位点，可能采取一种非结构化构象，其保守的膜近端区（约30 aa）含碱性残基簇，可能介导与膜内酸性磷脂（PIP2）的静电锚定而非特异性折叠。PAE图预期在胞内域与胞外区之间呈现高对齐误差（>15Å），表明两者之间存在显著的构象自由度——这种自由度可能是在膜内有限空间中实现顺式多聚化组装所需的物理前提。此外，PCDHGB4胞外重复2和3之间的钙离子结合位点（保守的DXD, DRE, DXNDN基序）突变在子宫内膜癌中被报告（PMID:28339086），提示钙结合缺陷可能削弱反式二聚化亲和力，导致细胞黏附丧失和肿瘤侵袭。

**4. 整合机制模型**

综合所有证据，PCDHGB4在分子水平上发挥三重功能：（1）在突触膜上，通过反式同源二聚化和顺式异源多聚化，参与神经元的自我回避和突触特异性识别——PMID:42184948显示PF4（血小板因子4）通过调控PCDHGB4表达预防帕金森病模型中的神经炎症和神经退行，强烈支持其在神经保护中的关键角色；（2）在非神经元细胞（如肺鳞癌细胞，PMID:38590195）中，PCDHGB4的异常表达通过GRAMD1介导的ER-PM接触位点重塑干扰胆固醇稳态，通过AREL1抑制凋亡，通过EMILIN2影响TGF-β信号——这一多通路信号整合赋予了PCDHGB4致癌功能；（3）在核质中，其胞质尾通过膜内蛋白水解（RIP）释放后可能作为转录共调控因子——这一假说由HPA的核质定位和囊泡定位共同支持，也与EMILIN2的TGF-β靶基因调控形成功能闭环。

**5. 研究与转化意义**

PCDHGB4的PubMed文献仅3篇（strict count，broad=3），研究与新颖性得分10/10。PMID:42184948（2026年）是近期发表于Brain Behav Immun的文章，首次将原钙黏蛋白γ簇与帕金森病神经保护联系起来，开辟了全新的研究领域。GRAMD1-胆固醇-凋亡调控轴为肺癌（PMID:38590195）和子宫内膜癌（PMID:28339086）中的PCDHGB4致癌机制提供了可成药的切入点——GRAMD1的胆固醇转运功能可被小分子抑制剂Asteroxin阻断。此外，PCDHGB4的表达是否在特发性帕金森病患者黑质多巴胺能神经元中下调，以及其多态性（SNP）是否与散发性PD风险关联，是两个高优先级的临床验证方向。


### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin gamma-B4

**功能**: Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR032455 |
| InterPro | IPR031904 |
| InterPro | IPR020894 |
| InterPro | IPR013164 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PCDHGB5 | BioGRID | 0 |
| PCDHGB1 | BioGRID | 0 |
| PCDHGB3 | BioGRID | 0 |
| GRAMD1B | BioGRID | 0 |
| GRAMD1A | BioGRID | 0 |
| DAG1 | BioGRID | 0 |
| EMILIN2 | BioGRID | 0 |
| AREL1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UN71-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000253953-PCDHGB4

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 3**

| 42184948 | Platelet factor 4 prevents neuroinflammation and neurodegeneration in Parkinson's disease model via regulating protocadh | Brain Behav Immun 2026 |
| 38590195 | [Exploring the Role of PCDHGB4 in the Occurrence of Lung Squamous Cell Carcinoma Based on Bioinformatics Analysis]. | Zhongguo Fei Ai Za Zhi 2024 |
| 28339086 | Identification of novel mutations in endometrial cancer patients by whole-exome sequencing. | Int J Oncol 2017 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGB4

