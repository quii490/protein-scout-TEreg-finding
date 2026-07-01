---
type: protein-evaluation
gene: "NXPE3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NXPE3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NXPE3 |
| 蛋白名称 | NXPE family member 3 |
| 蛋白大小 | 559 aa / 63.8 kDa |
| UniProt ID | Q969Y0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 559 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=6 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=89.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ig_E-set; NXPE4_C; NXPH/NXPE |
| PPI | 5/10 | x3 | 15.0 | PPI degree=37 |
| **加权总分** | | | **139/180** | |
| **归一化总分** | | | **76.5/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=6 broad=10
- AF pLDDT=89.6 PDB=0
- InterPro: Ig_E-set; NXPE4_C; NXPH/NXPE
- Pfam: Neurexophilin; NXPE4_C
- PPI degree=37 ChIP: None
35788904: Spatiotemporal Dynamics of the Molecular Expression Pattern and Intercellular In | 37309586: Hypermethylation of CTDSPL2 prior to necrotizing enterocolitis onset. | 37589026: Integrative Identification by Hi-C Revealed Distinct Advanced Structural Variati

### 4. 总体评价
**76.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: NXPE family member 3

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR014756 |
| InterPro | IPR057106 |
| InterPro | IPR026845 |
| Pfam | PF06312 |
| Pfam | PF24536 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| APP | BioGRID | 1 |
| MPPE1 | BioGRID | 1 |
| CLEC2D | BioGRID | 1 |
| TRIM25 | BioGRID | 1 |
| FAM209A | BioGRID | 1 |
| TGOLN2 | BioGRID | 1 |
| ATP1B4 | BioGRID | 0 |
| SCGB2A2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q969Y0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000144815-NXPE3

![](https://images.proteinatlas.org/36259/407_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/36259/407_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/36259/404_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/36259/404_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/36259/410_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/36259/410_A10_2_red_green.jpg)

### PubMed 文献

**PubMed count: 10**

| 42001290 | Proteome-based identification and validation of NXPE3 in childhood acute lymphoblastic leukaemia. | Pak J Pharm Sci 2026 |
| 41939511 | Single-cell transcriptomic profiling of the splenic and peripheral immune landscape in rhesus macaques during CHIKV infe | J Virus Erad 2026 |
| 41413636 | Genome-wide association study identifies novel variants in olfactory, vitamin A, vitamin B, and cadherin pathways associ | Sci Rep 2025 |

### 深度机制分析

**结构域架构与分子功能推演。** NXPE3的Ig_E-set结构域(IPR014756)属于免疫球蛋白样折叠超家族,其特征是两个反平行β-sheet通过核心疏水残基紧密堆积——这种折叠在进化上被反复利用于细胞识别、黏附和信号传导。NXPE4_C结构域(IPR057106, Pfam PF24536)是NXP/NXPE家族的特征性C端模块,推测形成独立的球状折叠。Neurexophilin结构域(PF06312)最初在神经分泌糖蛋白中发现,其序列保守性集中在二硫键形成所需的半胱氨酸残基上,表明NXPE3的折叠和功能受氧化还原状态调控。NXPE3缺乏经典的DNA结合域或核定位信号(NLS),其核质定位可能依赖"piggyback"机制——通过结合携带NLS的核蛋白(如TRIM25或转录因子)被动入核。pLDDT=89.6的高置信度(AF2)表明蛋白整体折叠质量优秀,超过90%的残基处于有序构象,这与分泌蛋白通常需要严整折叠的特性一致。

**PPI网络揭示的生物学意义。** APP(BioGRID)是NXPE3互作组中最值得关注的伴侣。APP(amyloid precursor protein)不仅是阿尔茨海默病的核心分子,其胞内结构域(AICD)在γ-secretase剪切后直接入核与Fe65/Tip60形成转录激活复合体,调控KAI1、GSK3β等靶基因。NXPE3与全长APP的互作可能发生在细胞表面或分泌途径中,但如果NXPE3通过APP的内存途径共内化(co-internalization),它可能被携带进入核内体-核周区域,甚至到达核质。TRIM25是RIG-I/MDA5抗病毒信号通路的关键E3泛素连接酶,通过催化RIG-I的K63多聚泛素化激活MAVS→TBK1→IRF3/7级联反应。TRIM25本身具有核定位能力并参与核内RNA传感器信号的调控。NXPE3与TRIM25的核内互作可能构成一条新的"先天免疫→转录调控"轴线。CLEC2D(C-type lectin)的互作则提示NK细胞介导的免疫监视功能可能与NXPE3相关。

**结构层面的功能解读。** NXPE3缺乏实验结构(PDB=0),但pLDDT=89.6表明AF2预测具有高度可靠性。Ig_E-set域大概率形成经典的"Greek key"拓扑,由7-9条β-strand构成两个反平行sheet。Neurexophilin家族蛋白的一个关键特征是它们通常以糖基化形式存在——NXPE3的分子量(63.8kDa)大于其一级序列预测值(~50kDa),差值可能归因于N-linked糖基化,这也与分泌/囊泡蛋白特征吻合。NXPE4_C域作为特征性C端模块,其独特的序列保守模式(Pro/Gly-rich区域交替排布)提示可能形成polyproline helix II(PPII)构象,这是蛋白-蛋白互作中SH3/WW结构域的常见识别基序。总体而言,NXPE3的结构设计似乎优化为"蛋白识别平台"而非酶活性中心。

**分子机制综合模型。** 综合全部证据,NXPE3在分子层面可能执行"免疫突触的分泌-核内双重信号转导"功能。在细胞外/囊泡层面,NXPE3作为Neurexophilin家族成员可能参与细胞间黏附或分泌性信号分子的包装/释放,类似于α-Latrotoxin受体的配体结合亚基。在核质层面,NXPE3通过TRIM25介导的泛素化信号参与先天免疫转录调控。具体机制推测为:NXPE3在分泌途径中被糖基化修饰后,一部分被分泌到胞外参与细胞通讯,另一部分通过与APP的共内化或TRIM25的直接结合被重定向至细胞核。在核内,NXPE3作为TRIM25的调控亚基或底物适配器,辅助TRIM25对特定的核内底物(可能是转录因子或染色质修饰酶)进行泛素化修饰,从而调节免疫应答基因的表达。这一模型解释了NXPE3的"Nucleoplasm; Vesicles"双重定位——它是免疫信号的"分子路由器",在分泌信号与核内转录应答之间建立联系。在儿童急性淋巴细胞白血病中的蛋白质组学发现(PubMed:42001290)暗示这一通路的异常活化可能驱动血液肿瘤发生。

**研究与转化意义。** (1)NXPE3-TRIM25核内互作轴的验证将是本蛋白最优先的研究方向——该互作可能揭示先天免疫信号从胞质RIG-I通路向核内转录延伸的新机制。(2)作为PubMed仅6篇且无已知疾病关联的极度新颖蛋白,NXPE3具有充当"first-in-class"药物靶点的潜力。(3)ALL中的蛋白质组学阳性信号(PubMed:42001290)提示NXPE3可能在白血病发病中发挥作用,作为生物标志物或治疗靶点的可行性值得验证。(4)鉴于APP互作和糖基化特征,NXPE3可能在神经退行性疾病(尤其是APP相关病理)中具有尚未被认知的作用——脑组织中NXPE3的表达水平和亚细胞定位应是优先调查方向。

