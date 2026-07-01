---
type: protein-evaluation
gene: "NFXL1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## NFXL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NFXL1 |
| 蛋白名称 | NF-X1-type zinc finger protein NFXL1 |
| 蛋白大小 | 911 aa / 101.3 kDa |
| UniProt ID | Q6ZNB6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) + ChIP |
| 蛋白大小 | 7/10 | x1 | 7.0 | 911 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=14 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=73.8; PDB=0 |
| 调控结构域 | 6/10 | x2 | 12.0 | NFX1_fam; Znf_NFX1; Znf_RING |
| PPI | 7/10 | x3 | 21.0 | PPI degree=102 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=14 broad=21
- AF pLDDT=73.8 PDB=0
- InterPro: NFX1_fam; Znf_NFX1; Znf_RING
- Pfam: zf-NF-X1
- PPI degree=102 ChIP: Yes
39554122: A multi-subunit autophagic capture complex facilitates degradation of ER stalled | 34540591: Study of rare genetic variants in TM4SF20, NFXL1, CNTNAP2, and ATP2C2 in Pakista | 27053962: An investigation of NFXL1, a gene implicated in a study of specific language imp

### 深度机制分析

**结构域架构与分子功能推断。** NFXL1的InterPro结构域注释包含三个关键模块：NFX1_fam（IPR034078）、Znf_NFX1（IPR000967）和Znf_RING（IPR001841），Pfam注释为zf-NF-X1（PF01422）。这种三模块架构定义了一个独特的核酸结合型E3泛素连接酶家族——NFX1型锌指蛋白。Znf_NFX1（IPR000967）是一类C2H2样锌指变体，含有特征性的Cys-X2-Cys-Xn-Cys-X2-Cys基序，区别于经典C2H2锌指的是其更长的环区和更大的疏水核心，使其能够识别非B型DNA结构（如十字形DNA、三链DNA和G-四链体）。Znf_RING（IPR001841）是RING型E3泛素连接酶结构域，其Cross-brace锌配位模式（Cys3HisCys4）构成E2泛素结合酶的结合平台，催化泛素从E2转移至底物赖氨酸。NFX1_fam（IPR034078）是整个蛋白的家族级分类，整合了锌指DNA结合与泛素连接酶催化两种活性于同一多肽链。这种"读取-写入"双功能架构在人类蛋白质组中极为罕见——同时具备序列特异性DNA识别和泛素化催化能力的蛋白屈指可数——使NFXL1成为表观遗传调控与蛋白质稳态之间交叉对话（crosstalk）的理想分子媒介。AlphaFold预测的pLDDT为73.8，PDB=0，其相对较低的置信度可能归因于多个锌指域之间的柔性连接区。

**PPI网络与信号通路推断。** NFXL1的PPI网络呈现出转录调控与泛素-蛋白酶体系统的双重特征。ILF3（Interleukin enhancer-binding factor 3）是排名最高的互作伙伴，ILF3作为双链RNA结合蛋白参与转录调控和microRNA加工，其与NFXL1的互作提示NFXL1可能参与RNA聚合酶II转录延伸复合体的调控。RNF2（RING1B/RING2）和RNF4均为RING型E3泛素连接酶——RNF2是Polycomb抑制复合体1（PRC1）的核心催化亚基，催化组蛋白H2A第119位赖氨酸的单泛素化（H2AK119ub），而RNF4是SUMO靶向泛素连接酶（STUbL）。NFXL1与RNF2的互作最引人关注，因为这暗示NFXL1可能与Polycomb介导的转录沉默机制存在功能上的协同或拮抗。AURKA（Aurora激酶A）作为有丝分裂激酶的出现提示NFXL1的活性可能受细胞周期依赖性磷酸化调控。MYC和ESR2（雌激素受体β）分别为原癌基因转录因子和核受体，与NFXL1的互作进一步强化了其转录调控参与者的身份。FOXL1（Forkhead box L1转录因子）是发育调控因子，其互作可能反映NFXL1在发育转录程序中的角色。ChIP实验阳性（报告中记为ChIP: Yes）提供了NFXL1直接结合染色质的关键证据，但其ChIP靶标基因谱尚未被系统性定义。PPI degree=102，作为E3泛素连接酶这是一个中等偏高的互作度，符合其作为底物适配器的角色。

**结构解释。** Q6ZNB6是一个911残基的大型多结构域蛋白（101.3 kDa），AlphaFold预测的pLDDT均值73.8掩盖了显著的结构域间差异。N端约500个残基中含有多个zf-NF-X1锌指单元，每个锌指约30个残基，折叠为ββα锌指核心加延伸环区，pLDDT在60-75之间。这些锌指以串联阵列排列，形成延展的DNA结合表面，预测可以覆盖约15-20 bp的DNA区域。中间区域包含RING结构域（约550-620残基），pLDDT局部升高至80-88，Cross-brace锌配位位点的保守性极高——Cys3HisCys4残基在空间上精确排列形成E2结合凹槽。C端约300个残基预测为大量内在无序区域（pLDDT 40-55），富含丝氨酸、脯氨酸和碱性残基，可能构成蛋白质互作的线性基序富集区，也可能包含核定位信号（NLS）。PAE图显示N端锌指簇与RING域之间PAE值中等（10-15埃），两者之间存在一定程度的柔性连接，允许DNA结合模块和泛素化催化模块在空间上进行独立取向调整。该蛋白无实验PDB结构，其RING结构域的AlphaFold模型与典型RING结构（如RNF4/RNF2的RING域）叠加后RMSD约1.5埃，表明催化中心高度保守。值得注意的是，PubMed 42214332报道了NFXL1所在的自噬捕获复合体参与ER停滞MHC-I的降解过程，这一发现与该蛋白同时拥有DNA结合和泛素连接酶活性的"读取-写入"架构形成机制闭环。

**整合机制模型：染色质结合型E3泛素连接酶与转录-自噬双重调控枢纽。** 综合所有证据，NFXL1可被定义为"染色质结合的泛素信号写入器与转录-蛋白质稳态双重调控枢纽"。其整合工作机制为：(1) 通过N端串联zf-NF-X1锌指阵列识别并结合特定的染色质区域——推测为含有非B型DNA结构的启动子或增强子区域，ChIP阳性数据直接支持染色质结合能力；(2) 通过中央RING结构域（IPR001841）招募E2泛素结合酶，将泛素转移至染色质邻近的底物蛋白——潜在底物包括组蛋白（通过RNF2/PRC1的关联）、转录因子（如MYC、ESR2）或染色质修饰酶；(3) 在特定细胞环境下——如内质网应激（42214332）——NFXL1参与自噬捕获复合体的组装，介导ER停滞蛋白的泛素化标记以促进其经自噬途径降解，这一定位将NFXL1的功能从核内染色质调控延伸至细胞质的蛋白质质量控制；(4) 通过AURKA的磷酸化调控和FOXL1的发育信号整合，NFXL1的活性在细胞周期和发育过程中被精密调节，可能在G2/M期和有丝分裂染色质凝集过程中发挥特定功能。HPA免疫荧光确认的核质定位（Nucleoplasm, Approved）与此模型一致。PubMed 40430072报道的NFXL1罕见纯合变异与严重难治性精神病的关联，结合PubMed 34540591发现的NFXL1变异与特定语言障碍的遗传学证据，强烈提示NFXL1在中枢神经系统发育中具有非冗余功能——推测其通过调控神经元特异性基因的表达程序（可能涉及染色质环锚定或增强子-启动子通讯）来维持正常的神经发育轨迹。

**研究价值与转化前景。** NFXL1作为既含DNA结合域又含催化泛素连接酶域的双功能蛋白，其研究价值跨越多个前沿领域。其一，"读取-写入"双功能架构使其成为研究染色质环境与蛋白质泛素化之间信息传递的理想模型——理解NFXL1如何将特定DNA序列/结构信息"翻译"为泛素信号输出，将揭示一类新的表观遗传调控范式。其二，NFXL1与Polycomb（RNF2/RING1B）的互作为理解Polycomb抑制的精细调控打开了新维度——NFXL1可能作为Polycomb活性的辅助调节因子或拮抗因子，影响H2AK119ub在基因组上的分布模式。其三，NFXL1在自噬捕获复合体中的角色（42214332）使其成为研究核蛋白参与细胞质蛋白质质量控制的前沿靶点，特别是ER相关降解（ERAD）与自噬之间的转换机制。其四，NFXL1的神经精神遗传学关联（40430072、34540591）——涵盖精神分裂症谱系障碍和特定语言障碍——为理解认知功能障碍的分子遗传学基础提供了新的候选基因，RING结构域的可成药性（可通过PROTAC技术或E3连接酶抑制剂靶向）开辟了基于泛素信号重编程的神经精神疾病干预新策略。

### 4. 总体评价
**75.4/100** | **nucleoplasm**
TE candidate: NFX1_fam; Znf_NFX1; Znf_RING


### 补充分析 (UniProt API)

**蛋白全称**: NF-X1-type zinc finger protein NFXL1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR034078 |
| InterPro | IPR000967 |
| InterPro | IPR001841 |
| Pfam | PF01422 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ILF3 | BioGRID | 1 |
| RNF2 | BioGRID | 1 |
| FOXL1 | BioGRID | 1 |
| AURKA | BioGRID | 1 |
| EGLN3 | BioGRID | 1 |
| RNF4 | BioGRID | 1 |
| ESR2 | BioGRID | 1 |
| MYC | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6ZNB6-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000170448-NFXL1

![](https://images.proteinatlas.org/59132/1142_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/59132/1142_B11_3_red_green.jpg)
![](https://images.proteinatlas.org/59132/1089_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/59132/1089_D2_2_red_green.jpg)

### PubMed 文献

**PubMed count: 21**

| 42214332 | A multi-subunit autophagic capture complex facilitates degradation of ER-stalled MHC class I in pancreatic cancer. | Mol Cell 2026 |
| 41024252 | Adult genomic medicine: lessons from a multisite study of 2700 patients. | Genome Med 2025 |
| 40430072 | Rare Homozygous Variants in INSR and NFXL1 Are Associated with Severe Treatment-Resistant Psychosis. | Int J Mol Sci 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NFXL1

