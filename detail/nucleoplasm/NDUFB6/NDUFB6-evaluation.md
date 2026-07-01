---
type: protein-evaluation
gene: "NDUFB6"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NDUFB6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NDUFB6 |
| 蛋白名称 | NADH dehydrogenase [ubiquinone] 1 beta subcomplex subunit 6 |
| 蛋白大小 | 128 aa / 15.5 kDa |
| UniProt ID | O95139 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 128 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=45 |
| 三维结构 | 10/10 | x3 | 30.0 | pLDDT=90.1; PDB=7 |
| 调控结构域 | 4/10 | x2 | 8.0 | NADH_DH_b-subcmplx_su6 |
| PPI | 7/10 | x3 | 21.0 | PPI degree=125 |
| **加权总分** | | | **141/180** | |
| **归一化总分** | | | **78.1/100** | 互证: +2 |

### 3. 分析
- Mitochondria; Nucleoplasm (Approved)
- PubMed strict=45 broad=55
- AF pLDDT=90.1 PDB=7
- InterPro: NADH_DH_b-subcmplx_su6
- Pfam: NDUF_B6
- PPI degree=125 ChIP: None
38240888: Multi-level profiling unravels mitochondrial dysfunction in myotonic dystrophy t | 39583859: Exploring Cuproptosis-Related Genes and Diagnostic Models in Renal Ischemia-Repe | 38994365: Identification and validation of cuproptosis-related genes in acetaminophen-indu

### 4. 总体评价
**78.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

NDUFB6（NADH dehydrogenase [ubiquinone] 1 beta subcomplex subunit 6, O95139）是线粒体呼吸链复合体I（Complex I，NADH:ubiquinone oxidoreductase）的一个附属亚基，其128个氨基酸的序列由IPR019174（NADH_DH_b-subcmplx_su6）和PF09782（NDUF_B6 Pfam）唯一注释。在复合体I的45亚基（哺乳动物）巨型架构中，NDUFB6属于β亚复合体的膜臂模块（membrane arm），定位在复合体的P_P-b模块交界区域。根据已解析的高分辨率冷冻电镜结构（PDB: 7个条目），NDUFB6是一个以α-螺旋为主的跨膜蛋白，含有单个N端跨膜螺旋锚定于线粒体内膜，C端小结构域面向膜间隙（intermembrane space）。其被描述为"非催化附属亚基"意味着NDUFB6不含铁硫簇、FMN或泛醌结合位点等氧化还原活性辅因子，但这并不削弱其功能重要性——附属亚基在稳定巨型复合体构象、辅助组装以及调控活性氧（ROS）产生等方面发挥关键作用。

pLDDT=90.1的高置信度（五蛋白中最高）和7个PDB条目使得NDUFB6成为这五个核蛋白中结构表征最充分的成员,这得益于复合体I全酶的密集结构生物学研究。高pLDDT值主要反映了其跨膜α-螺旋区域的刚性折叠。然而，NDUFB6在核质中同时定位（HPA: Mitochondria; Nucleoplasm, Approved）的数据才是该蛋白最具挑战性的功能线索——线粒体呼吸链亚基为何出现在核质？目前已有多个线粒体蛋白（如AIFM1、HTRA2、CYC1、PDK1等）被报道具有"兼业行为"（moonlighting），即除线粒体经典功能外在胞核或胞质执行其他功能。NDUFB6的PPI网络中，PALB2（STRING 946）和PWWP3A（STRING 732）的强互作为此提供了关键线索。PALB2是BRCA2的搭档定位因子（partner and localizer），是DNA同源重组修复通路的核心组分，负责招募BRCA2-RAD51到DNA双链断裂位点；PWWP3A（MUM1）含PWWP结构域，该结构域特异识别三甲基化组蛋白H3K36me3，是染色质结合模块。这两个互作的存在暗示NDUFB6在核质中可能参与DNA损伤应答或染色质相关过程的调控。

PPI网络中其他高置信度伙伴同样富有信息量：NDUFA9（STRING 999）和ACP1（STRING 999）均为复合体I的固有亚基（NDUFA9位于泛醌结合模块，ACP1为酰基载体蛋白），反映NDUFB6在复合体I组装和稳态维持中的标准角色。DGUOK（脱氧鸟苷激酶，STRING 716）定位于线粒体基质，负责线粒体dNTP池的维持——这一互作暗示复合体I功能与核苷酸代谢之间存在耦合。APP（淀粉样前体蛋白，BioGRID 1）的互作虽然在BioGRID中得分较低，但在阿尔茨海默病背景下，复合体I功能障碍和APP信号传导的异常激活常常并行出现，NDUFB6可能构成这一病理交叉的分子纽带。YME1L1（i-AAA蛋白酶，BioGRID 1）定位在线粒体内膜，负责线粒体蛋白质量控制——NDUFB6作为复合体I亚基，与YME1L1的互作可能反映其在组装后或损伤条件下的降解/更新途径。

综合机制模型：NDUFB6在线粒体中的首要功能是作为复合体I的结构亚基，通过其跨膜螺旋和膜间隙C端结构域稳定膜臂模块的构象，维持从NADH氧化到泛醌还原的电子传递效率。在核质中，NDUFB6可能执行一种线粒体-核逆行信号（retrograde signaling）的兼业功能——通过其与PALB2和PWWP3A的互作，在线粒体应激条件下（如复合体I功能障碍导致ROS升高或NAD⁺/NADH比值改变），NDUFB6可能从受损线粒体中外泄至胞质并转入核内,参与DNA损伤修复的调控或H3K36me3标记染色质区域的转录调节。这一假说与近年关于线粒体应激触发核基因重编程的"线粒体未折叠蛋白应答"（UPR-mt）框架一致。此外，NDUFB6相关的文献（PMID 38240888涉及肌强直性营养不良中的线粒体功能障碍；PMID 42273709涉及NDUF家族蛋白在口腔鳞癌中通过VCP介导的泛素-蛋白酶体通路的作用）进一步支持NDUFB6的异常表达或功能障碍与疾病存在紧密关联。鉴于复合体I在代谢重编程中的核心地位以及NDUFB6的PALB2/PWWP3A连接，该蛋白在DNA修复缺陷和代谢异常交叉的肿瘤（如BRCA突变型乳腺/卵巢癌）中可能具有尚未被认识的生物标志物或合成致死靶点价值。


### 补充分析 (UniProt API)

**蛋白全称**: NADH dehydrogenase [ubiquinone] 1 beta subcomplex subunit 6

**功能**: Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR019174 |
| Pfam | PF09782 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NDUFA9 | STRING | 999 |
| ACP1 | STRING | 999 |
| PALB2 | STRING | 946 |
| PWWP3A | STRING | 732 |
| DGUOK | STRING | 716 |
| APP | BioGRID | 1 |
| IKBIP | BioGRID | 1 |
| YME1L1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O95139-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000165264-NDUFB6

![](https://images.proteinatlas.org/44001/2211_G3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/44001/2211_G3_29_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000165264-NDUFB6

![](https://images.proteinatlas.org/44001/2211_G3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/44001/2211_G3_29_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000165264-NDUFB6

![](https://images.proteinatlas.org/44001/2211_G3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/44001/2211_G3_29_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 55**

| 42273709 | Sialylated Immunoglobulin G Promotes the Malignant Progression of Oral Squamous Cell Carcinoma through VCP-Mediated NDUF | Research (Wash D C) 2025 |
| 42256164 | Putative Genomic Signatures of Local Adaptation in Five Local Indonesian Sheep Reveal Selection on Immunity, Reproductio | Ecol Evol 2026 |
| 42230543 | An integrative mendelian randomisation and drug mechanism framework for target prioritisation and therapeutic repurposin | Transl Psychiatry 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/NDUFB6

