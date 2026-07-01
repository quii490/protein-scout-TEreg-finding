---
type: protein-evaluation
gene: "TIGD6"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## TIGD6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TIGD6 |
| 蛋白名称 | Tigger transposable element-derived protein 6 |
| 蛋白大小 | 521 aa / 58.7 kDa |
| UniProt ID | Q17RP2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Actin filaments; Nucleoplasm; Vesicles (Approved) + ChIP |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 521 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=4 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=76.6; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=22 |
| **加权总分** | | | **140/180** | |
| **归一化总分** | | | **78.1/100** | 互证: +3 |

### 3. 分析
- HPA: Actin filaments; Nucleoplasm; Vesicles (Approved)
- PubMed: strict=4, broad=6
- AF pLDDT: 76.6 / PDB: 0
- InterPro: CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf
- Pfam: CENP-B_N; DDE_1; HTH_Tnp_Tc5
- PPI degree: 22 / ChIP: Yes
**Papers**: 38342959: A Treg-related riskscore model may improve the prognosis evaluation of colorecta | 35817785: Genomic instability genes in lung and colon adenocarcinoma indicate organ specif | 27421018: Exome sequencing in Thai patients with familial obesity.

### 4. 总体评价
★★★★  **78.1/100**  |  **nucleoplasm**
**TE candidate**: CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf


### 深度机制分析

TIGD6（Tigger transposable element-derived protein 6, Q17RP2）是哺乳动物基因组中转座子驯化（transposon domestication）的一个典型范例，其521个氨基酸包含三组功能明确的转座子衍生结构域：N端CENP-B_N（Pfam: CENP-B_N, InterPro: CenT-Element_Derived）、中部DDE_1（Pfam: DDE_1, InterPro: DDE_SF_endonuclease_dom）以及C端HTH_Tnp_Tc5（Pfam: HTH_Tnp_Tc5, InterPro: Homeodomain-like_sf）。CENP-B_N结构域是一类源自pogo-like转座酶的DNA结合模块，在着丝粒蛋白CENP-B中以序列特异性方式识别着丝粒卫星DNA（CENP-B box），但TIGD6中该结构域的靶序列可能与着丝粒DNA不同，而是识别基因组中残留的Tigger/Tc1-like转座子末端反向重复序列或其他富AT元件。DDE_1催化核心是三氨基酸基序（Asp-Asp-Glu）构成的RNase H样折叠，在原始转座酶中负责DNA链的切割与链转移——在驯化后的TIGD6中，该催化残基是否保留活性是一个关键问题：若活性保留，TIGD6可能仍具有DNA切割能力，参与染色体重排或DNA修复过程；若催化残基突变失活，则DDE结构域可能演化为一个结构支架或蛋白-蛋白互作界面。

TIGD6的PPI网络虽然较小（degree=22），但其互作伙伴的组合富含功能暗示。NUP54（核孔复合体蛋白54）的互作提示TIGD6在核质与核孔之间存在物理关联，这可能与TIGD6在核内执行DNA结合功能后需要通过核孔穿梭有关。MTA1（转移相关蛋白1）是NuRD染色质重塑与去乙酰化复合体的核心组分，负责转录抑制——若TIGD6通过其同源异型结构域样折叠（Homeodomain-like_sf）识别特定基因组位点并招募MTA1/NuRD复合体，则TIGD6可能作为一个序列特异性转录抑制因子发挥功能。CHAF1A（染色质组装因子1亚基A）是CAF-1复合体的核心亚基，负责在DNA复制偶联的核小体装配中将组蛋白H3-H4四聚体沉积到新合成的DNA上——TIGD6与CHAF1A的互作暗示其可能参与复制叉或DNA修复位点的染色质重塑。此外，ZRANB2（含锌指的RNA结合蛋白）与MAGED2（黑色素瘤抗原家族成员）的存在进一步拓宽了TIGD6的调控维度，可能涉及RNA加工和泛素化信号的交叉。

AlphaFold预测的pLDDT值76.6可能低估了单个结构域的实际折叠质量——521 aa的大蛋白中，三个离散的结构域可能通过灵活的无序连接区（linker）连接，连接区的低置信度拉低了整体pLDDT均值。PAE图（Predicted Aligned Error）在这类多结构域蛋白中通常揭示明显的分块模式：三个结构域块内具有低PAE（高置信度相对位置），而结构域间PAE高（相对取向不确定），表明TIGD6的结构域间连接区可能具有显著的构象柔性，这种柔韧性对于扫描基因组DNA并同时与多个蛋白质伙伴互作可能至关重要。PDB条目为0的事实说明TIGD6目前完全缺乏实验结构数据，这是其三维结构维度的主要短板，但对于一个PubMed仅4篇的新蛋白而言是完全预期的。

从分子机制层面综合推断，TIGD6最可能的功能模型是：通过CENP-B_N和HTH_Tnp_Tc5双DNA结合模块锚定基因组中的特定转座子衍生序列，利用DDE催化核心（如保留活性）或变构调控（如催化失活）来介导局部染色质重塑，并通过MTA1/NuRD和CHAF1A/CAF-1等互作伙伴实现对靶位点的转录抑制或染色质状态维护。这种驯化转座酶的调控模式在哺乳动物中已有先例——RAG1/RAG2重组酶、SETMAR/Metnase和PGBD5均属于转座子驯化后获得新功能（VDJ重组、DNA修复、神经元基因调控）的案例。TIGD6在胃癌（PMID 41121403）和肝细胞癌（PMID 41775084）中的预后价值提示该蛋白的异常表达可能通过解除转座子衍生序列的转录抑制或破坏染色质边界，导致基因组不稳定和癌基因激活。作为高度新颖（PubMed=4）的TE来源核蛋白，TIGD6代表了以转座子驯化蛋白为切入点的功能基因组学研究的理想靶标，其作用机制的阐明可能揭示一套全新的转座子-宿主共演化调控语言。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MAPT | BioGRID | 1 |
| UBE2V2 | BioGRID | 1 |
| MTA1 | BioGRID | 1 |
| ZRANB2 | BioGRID | 1 |
| CHAF1A | BioGRID | 1 |
| MAGED2 | BioGRID | 1 |
| SS18L2 | BioGRID | 1 |
| NUP54 | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000164296-TIGD6

![](https://images.proteinatlas.org/44599/1129_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/44599/1129_A7_3_red_green.jpg)
![](https://images.proteinatlas.org/44599/1021_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/44599/1021_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/44599/1019_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/44599/1019_G6_3_red_green.jpg)
![](https://images.proteinatlas.org/57538/2172_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/57538/2172_B3_3_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q17RP2-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 6**

| 41775084 | Single-cell analysis of TIGD genes in hepatocellular carcinoma: Prognostic value and functional characterization. | Transl Oncol 2026 |
| 41121403 | TIGD6 in gastric cancer: exploring its prognostic value and therapeutic potential through molecular and clinical investi | Eur J Med Res 2025 |
| 40722386 | Detection of LUAD-Associated Genes Using Wasserstein Distance in Multiomics Feature Selection. | Bioengineering (Basel) 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TIGD6

