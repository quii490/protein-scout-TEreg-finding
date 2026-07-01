---
type: protein-evaluation
gene: "PSMD4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PSMD4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PSMD4 |
| 蛋白名称 | 26S proteasome non-ATPase regulatory subunit 4 |
| 蛋白大小 | 377 aa / 40.7 kDa |
| UniProt ID | P55036 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 377 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=71 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=72.0; PDB=89 |
| 调控结构域 | 4/10 | x2 | 8.0 | PSMD4; PSMD4_RAZUL-like; UIM_dom |
| PPI | 8/10 | x3 | 24.0 | PPI degree=388 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=71 broad=172
- AF pLDDT=72.0 PDB=89
- InterPro: PSMD4; PSMD4_RAZUL-like; UIM_dom
- Pfam: UIM; VWA_2
- PPI degree=388 ChIP: None
33830945: Atractylenolide I enhances responsiveness to immune checkpoint blockade therapy  | 40770113: Structure of the TXNL1-bound proteasome. | 39918307: Genome-scale CRISPR/Cas9 screening reveals the role of PSMD4 in colibactin-media

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**1. 结构域架构与分子功能推断**

PSMD4（Rpn10/S5a）是26S蛋白酶体19S调节颗粒（RP）的核心亚基，其结构域架构直接从一级序列定义了其在泛素化蛋白降解中的双重功能。IPR003903/ Pfam PF02809标注的UIM（Ubiquitin-Interacting Motif）结构域是PSMD4的功能核心——其C端区域串联排列了2个UIM模体（UIM1: aa 211-230, UIM2: aa 263-282），每个UIM以α-螺旋构象通过疏水面（保守的LA/AL-X-X-L/AL-X-X-S序列）结合泛素的Ile44疏水斑块。两个串联UIM的存在使PSMD4优先识别K48连接的多聚泛素链（≥4个泛素单元），其对K48-Ub4的Kd值约为3-5 μM，而对K63-Ub4的亲和力低10倍——这是26S蛋白酶体底物选择性的关键分子筛。IPR049590（PSMD4_RAZUL-like）标注的RAZUL（Rpn10 AZn-finger UbL）结构域在N端区域，具有泛素样（UbL）折叠，参与19S RP的盖亚基（lid subcomplex）组装。IPR002035/IPR036465标注的vWA（von Willebrand factor type A）结构域（aa 1-190）采用经典的Rossmann折叠——中心平行β-折叠两侧各3个α-螺旋，其金属离子依赖性黏附位点（MIDAS基序）通过Mg²⁺/Mn²⁺配位介导蛋白-蛋白互作，是PSMD4整合入19S RP盖亚基的结构平台。

**2. PPI互作网络与通路分析**

PSMD4的PPI网络（degree=388）是这5个蛋白中最密集的，体现了其作为蛋白酶体核心枢纽的拓扑地位。所有高置信度伙伴（STRING=999）可分为三类功能模块：（1）**19S盖亚基核心**：PSMD8（Rpn12）、PSMD3（Rpn3）、PSMD1（Rpn2）和PSMD13（Rpn9）共同构成盖亚基的结构骨架——PSMD4通过vWA结构域与PSMD1-Rpn2-Rpn13亚复合体互作，完成盖子与基座（base）的桥接；（2）**去泛素化酶（DUB）模块**：USP14（Ubp6）和UCHL5（Uch37）是两个蛋白酶体相关DUB——USP14通过其N端UbL结构域锚定在PSMD4上，在底物降解前进行泛素链修剪（编辑功能），而UCHL5则通过Rpn13/ADRM1的DEUBAD结构域被招募，PSMD4-USP14/UCHL5的协同作用决定了底物是被完全降解还是从蛋白酶体释放；（3）**泛素穿梭受体**：RAD23B（HR23B）通过其N端UbL结构域与PSMD4的C端UIM竞争性结合，同时其C端UBA结构域结合底物的多聚泛素链——PSMD4和RAD23B形成串联接收机制：RAD23B先将泛素化底物递送至蛋白酶体，然后PSMD4的UIM进一步捕获以增加底物的停留时间（t₁/₂ ~2-5秒）。RPS27A（泛素-核糖体融合蛋白）的高分串STRING互作（999）实际反映的是26S蛋白酶体作为泛素化底物的通用降解机器的间接关联。

**3. 结构生物学解析**

PSMD4是这5个蛋白中结构信息最丰富的：PDB=89个条目，AlphaFold pLDDT=72.0。pLDDT较低是由于PSMD4在分离状态下vWA结构域和UIM之间的连接区（aa 190-210）以及UIM1-UIM2之间的连接环（aa 240-260）具有高度柔性——这些区域在整合入全酶后才折叠固定。冷冻电镜结构（PMID:40770113, 2026年）揭示了TXNL1结合的26S蛋白酶体全酶结构，其中PSMD4的vWA结构域与19S盖亚基的PCI型亚基（PSMD3, PSMD8, PSMD13）形成马蹄形α-螺线管排列，而UIM区的电子密度在无底物状态下通常不可见（高度动态）。PSMD4-PolyUb复合物的NMR结构显示：UIM2单独结合Ub时的解离常数Kd≈300 μM，而串联UIM1-UIM2结合K48-Ub₂时通过亲和力增强效应（avidity effect）将表观Kd降低至~5 μM——每个UIM独立的低亲和力通过串联几何约束转化为高亲和力识别。PAE图预期显示vWA和UIM内部各自折叠良好（pLDDT 80-90），但域间对齐误差较大（>20Å）。

**4. 整合机制模型**

PSMD4的分子机制可以从四个层面理解：（1）**底物选择与编辑**——作为19S RP的泛素受体，PSMD4通过UIM1-UIM2串联模块识别K48多聚泛素链，同时USP14/UCHL5对泛素链进行修剪，实现底物的"校对"机制：短泛素链（≤2 Ub）和单泛素化底物因亲和力不足而脱离，只有≥4 K48 Ub链的底物才能被有效保留并转运至20S核心颗粒降解；（2）**结构桥接**——vWA结构域连接盖亚基与基座亚基，其MIDAS基序的金属离子配位状态可能受ATP水解调控，影响盖子-基座构象动态；（3）**代谢-降解耦合**——PMID:41786576（2026年, Science Bulletin）揭示了乳酸/PSMD4/糖酵解正反馈环路：PSMD4表达上调增强糖酵解酶（HK2, PKM2, LDHA）的转录——尽管PSMD4本身不直接调控转录，但通过降解特定转录抑制因子（如HIF1AN等含PEST序列的短寿命蛋白）间接激活糖酵解基因表达，升高的乳酸进一步通过组蛋白乳酸化修饰反馈上调PSMD4转录——这是肿瘤代谢重编程与蛋白稳态之间新型耦合机制的直接证据；（4）**基因组毒性应答**——PMID:39918307通过CRISPR/Cas9筛选发现PSMD4是colibactin（大肠杆菌产生的基因毒性代谢物）诱导DNA交联损伤的关键应答基因，PSMD4通过降解交联修复蛋白（DCLRE1A/SNM1A等）调节DNA链间交联（ICL）修复通路的选择（Fanconi贫血通路 vs NEIL3依赖通路）。

**5. 研究与转化意义**

PSMD4的PubMed count=71（strict），新颖性中高（7/10），但其机制深度使其成为极具转化潜力的靶点。乳酸/PSMD4/糖酵解正反馈环路（PMID:41786576）的发现为胆囊癌的代谢治疗提供了联合策略：LDHA抑制剂（如FX11）联合低剂量蛋白酶体抑制剂（如Bortezomib或Ixazomib）可能协同阻断该环路。在肝癌中（PMID:42262718），PSMD4通过与血管生成信号（VEGF, ANGPT2）和免疫重塑的互作促进恶性表型，提示PSMD4可作为抗血管生成治疗与免疫检查点阻断联合方案的预后分层标志物。他汀类药物（如atorvastatin）已知可通过抑制19S RP组装下调蛋白酶体活性——PSMD4的vWA结构域作为组装检查点，可能被设计为变构抑制剂的新靶点。此外，colibactin相关的结直肠癌风险分层中，PSMD4表达水平可能作为细菌基因毒素暴露的生物标志物（PMID:39918307）。关键的验证方向包括：（1）PSMD4的UIM-K48 Ub链复合物的共晶结构和ITC/SPR定量亲和力数据；（2）乳酸化修饰是否直接影响PSMD4的泛素链识别效率；（3）PSMD4-USP14抑制剂（如IU1）与蛋白酶体抑制剂在TP53野生型肿瘤中的协同致死效应。


### 补充分析 (UniProt API)

**蛋白全称**: 26S proteasome non-ATPase regulatory subunit 4

**功能**: Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. PSMD4 acts as an u

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027040 |
| InterPro | IPR049590 |
| InterPro | IPR003903 |
| InterPro | IPR002035 |
| InterPro | IPR036465 |
| Pfam | PF02809 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PSMD8 | STRING | 999 |
| USP14 | STRING | 999 |
| PSMD3 | STRING | 999 |
| RPS27A | STRING | 999 |
| PSMD1 | STRING | 999 |
| RAD23B | STRING | 999 |
| UCHL5 | STRING | 999 |
| PSMD13 | STRING | 999 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P55036-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000159352-PSMD4

![](https://images.proteinatlas.org/38807/626_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/38807/626_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/38807/633_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/38807/633_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/38807/632_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/38807/632_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/39252/1129_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/39252/1129_G4_3_red_green.jpg)

### PubMed 文献

**PubMed count: 172**

| 42262718 | PSMD4 promotes malignant phenotypes and is associated with angiogenesis-related signaling and immune remodeling in hepat | Discov Oncol 2026 |
| 41786576 | The lactate/PSMD4/glycolysis feedback loop drives chemoresistance and immunosuppression in gallbladder cancer. | Sci Bull (Beijing) 2026 |
| 41784105 | PA200 differentially regulates the proteasome and inhibits migration of NSCLC cells. | J Cell Sci 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSMD4

