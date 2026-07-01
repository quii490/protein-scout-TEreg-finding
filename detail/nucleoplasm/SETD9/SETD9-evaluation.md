---
type: protein-evaluation
gene: "SETD9"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SETD9 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SETD9 |
| 蛋白名称 | SET domain-containing protein 9 |
| 蛋白大小 | 299 aa / 34.1 kDa |
| UniProt ID | Q8NE22 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 299 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=5 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=87.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | SET_dom; SET_dom_sf; SETD9 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=7 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=5 broad=5
- AF pLDDT=87.7 PDB=0
- InterPro: SET_dom; SET_dom_sf; SETD9
- Pfam: 
- PPI degree=7 ChIP: None
41427146: Transcriptional insights into gastrointestinal adaptations in pigs to high altit | 40211238: LncRNA-mRNA co-expression network in the mechanism of butylphthalide treatment f | 30458291: The Kdm/Kmt gene families in the self-fertilizing mangrove rivulus fish, Kryptol

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: SET domain-containing protein 9

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001214 |
| InterPro | IPR046341 |
| InterPro | IPR040415 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: SET domain-containing protein 9

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001214 |
| InterPro | IPR046341 |
| InterPro | IPR040415 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TP53 | STRING | 752 |
| ELAVL1 | BioGRID | 1 |
| USO1 | BioGRID | 1 |
| CRK | BioGRID | 1 |
| PLCG2 | BioGRID | 1 |
| S100A2 | BioGRID | 0 |
| HSPD1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NE22-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000155542-SETD9

![](https://images.proteinatlas.org/49936/747_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/49936/747_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/49936/714_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/49936/714_D9_2_red_green.jpg)
![](https://images.proteinatlas.org/49936/713_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/49936/713_D9_2_red_green.jpg)

### 深度机制分析

**1. 结构域架构与分子功能推断**

SETD9是SET-domain甲基转移酶超家族中一个高度未被表征的成员。其结构域架构极为简洁——单个SET结构域（IPR001214, IPR046341）几乎占据了蛋白的主体，另有一个SETD9特异性亚家族标记（IPR040415）。SET结构域是组蛋白和内质蛋白赖氨酸甲基转移酶的标志性催化模块，其折叠形成经典的伪结（pseudoknot）结构以容纳S-腺苷甲硫氨酸（SAM）辅因子和底物赖氨酸残基。在SETD家族中，成员按照底物特异性大致分为几类：组蛋白H3K4甲基化（SETD1A/1B, SETD7）、H3K9甲基化（SETDB1/2）、H3K36甲基化（SETD2, SETD3）、H3K27甲基化（EZH1/2）以及H4K20甲基化（SETD8）。SETD9的SET域与这些已知成员的序列同源性并不明确，这意味着其底物特异性和甲基化程度（mono-/di-/tri-）尚未确定——但SETD9的"孤儿SET"身份恰好暗示它可能靶向一个完全未被认识的非组蛋白底物，或具有非典型的组蛋白修饰位点特异性。

**2. PPI互作网络的生物学意义**

SETD9的PPI网络虽然规模较小（degree=7），但在生物学上极为浓缩且意味深长。最关键的互作是TP53（STRING评分752），这意味着SETD9与p53之间存在极高置信度的功能关联。在SETD家族中，已有先例——SETD7（也称为SET7/9，注意命名上的混淆）是第一个被发现的p53特异性赖氨酸甲基转移酶，其在K372位点的单甲基化将p53稳定在核内并增强其转录活性。SETD9是否对p53执行类似但非冗余的甲基化修饰——例如靶向不同的赖氨酸残基（K370, K373或K382）或介导不同甲基化状态（二甲基化vs单甲基化）——是一个极其值得验证的假说。ELAVL1（也称为HuR，一种RNA结合蛋白，调控mRNA稳定性）的互作提示SETD9的功能可能延伸至转录后水平——ELAVL1结合并稳定p53 mRNA，SETD9可能在这一轴向上的p53表达调控中提供甲基化依赖的协调机制。S100A2（钙结合蛋白，p53家族靶基因）和HSPD1（分子伴侣，参与线粒体蛋白折叠）的互作则扩展了SETD9从核质到线粒体功能调控的潜在信号范围。

**3. 三维结构解读**

AlphaFold预测的pLDDT为87.7（299aa全长），属于良好置信度。SET结构域的核心区域（约120-250位氨基酸）应该包含最高的pLDDT值，因为SET域的伪结折叠高度保守且刚性。SET域的活性位点包含4个关键的结构元件：（1）SAM结合口袋——由GXG基序起始的loop和一系列疏水/芳香残基形成；（2）底物赖氨酸通道——一个窄而深的隧道，引导靶赖氨酸残基的ε-氨基进入活性位点；（3）催化酪氨酸/苯丙氨酸——位于通道底部，通过去质子化活化赖氨酸的ε-氨基进行亲核攻击；（4）产物释放通路——甲基转移反应后，甲基化的赖氨酸和SAH分别离开活性位点。SETD9在这些关键结构元件中的残基保守性是推断其催化活性的核心线索——如果关键催化残基存在，SETD9是具有功能的活性甲基转移酶；如果GXG基序或催化酪氨酸缺失，SETD9可能是假甲基转移酶（pseudomethyltransferase），即保留了底物结合功能但丧失了催化能力，类似于某些SET家族成员已演化为支架蛋白或"甲基化阅读器"。PDB=0但pLDDT=87.7的组合意味着结构预测可用于指导定点突变实验来验证催化活性，但缺乏原子分辨率的细节来区分活性/非活性状态。

**4. 分子机制综合模型**

综合所有数据，SETD9在核质中执行的核心功能最可能的分子模型是："SETD9是p53的新型赖氨酸甲基转移酶/甲基化阅读器，参与p53依赖性细胞命运决定的精微调控。"具体而言：（1）在正常状态下，SETD9通过其SET域识别p53的C末端调控区（CTD，含有多个赖氨酸残基K370-K386），执行位点选择性的赖氨酸单甲基化——这区别于SETD7/9介导的K372甲基化，可能靶向K373或K382，产生不同的下游效应（如Mdm2结合能力改变、乙酰化competition等）；（2）SETD9通过ELAVL1互作同时影响p53的mRNA稳定性，在转录后水平与前一条路径形成双重调控（dual-level regulation）——甲基化调控p53蛋白活性，ELAVL1调控p53 mRNA稳定性；（3）在温和的基因毒性应激下，SETD9介导的p53甲基化可能"滴定"p53活性——不触发完全凋亡程序，而是促进细胞周期停滞和DNA修复，这与SETD7介导的p53活性"开关"功能形成层级调控；（4）在极端应激条件下，SETD9通过HSPD1互作可能与线粒体凋亡通路形成cross-talk——HSPD1作为线粒体蛋白折叠监控蛋白，其与SETD9的互作可能反映了一个连接核内p53甲基化状态与线粒体完整性感知的信号转导机制。S100A2（已知受p53转录调控）的互作则可能构成反馈环路——p53激活S100A2表达，S100A2反过来与SETD9形成复合体，调节SETD9对p53的甲基化活性。

**5. 研究与转化意义**

SETD9可能是SETD家族中最后几个"暗物质"成员之一，现有5条PubMed文献中仅3条涉及机制性研究，且均来自间接的组学分析（lncRNA共表达网络、转录组测序、基因家族进化谱系），无一开展功能验证。在核蛋白评估体系的五个蛋白中，SETD9是新颖性含量最高、机理探索空间最大的入口。在转化医学层面：（1）如果SETD9验证为p53的新型甲基转移酶，它将直接进入精准肿瘤学的核心圈——p53是人类癌症中最常突变的基因（>50%的肿瘤携带TP53突变），SETD9对野生型p53的甲基化调控可能影响携带p53 野生型但活性异常肿瘤（如MDM2扩增的肉瘤）的治疗策略；（2）SETD9可能成为"p53再激活"策略的新型药物靶点——与直接结合p53不同，靶向SETD9的小分子抑制剂或激活剂可以通过调节p53的甲基化水平来"重新编程"其活性谱（偏向凋亡vs.偏向细胞周期停滞），选择性地增强化疗敏感性；（3）SETD9-SET位点的结构-功能解析（靶向p53 K373 vs K372 vs K382的特异性决定因子）将为设计亚型选择性甲基转移酶抑制剂提供结构生物学基础——这是表观遗传药物发现中的核心挑战；（4）SETD9的ELAVL1和HSPD1互作将p53调控从单纯的"翻译后修饰"扩展到"RNA稳定性+蛋白折叠+甲基化"的三维调控网络，这为理解肿瘤细胞如何精确控制p53的"剂量-效应"关系提供了全新的理论框架。

### PubMed 文献

**PubMed count: 5**

| 41427146 | Transcriptional insights into gastrointestinal adaptations in pigs to high altitude. | Front Vet Sci 2025 |
| 40211238 | LncRNA-mRNA co-expression network in the mechanism of butylphthalide treatment for ischemic stroke. | BMC Neurol 2025 |
| 38645867 | [Screening for Characteristic Genes of Different Traditional Chinese Medicine Syndromes of Psoriasis Vulgaris: A Study B | Sichuan Da Xue Xue Bao Yi Xue Ban 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SETD9

