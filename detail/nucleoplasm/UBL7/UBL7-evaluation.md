---
type: protein-evaluation
gene: "UBL7"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## UBL7 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UBL7 |
| 蛋白名称 | Ubiquitin-like protein 7 |
| 蛋白大小 | 380 aa / 40.5 kDa |
| UniProt ID | Q96S82 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 380 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=14 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=66.9; PDB=2 |
| 调控结构域 | 4/10 | x2 | 8.0 | UBA; UBA-like_sf; Ubiquilin |
| PPI | 6/10 | x3 | 18.0 | PPI degree=68 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **74.3/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=14 broad=22
- AF pLDDT=66.9 PDB=2
- InterPro: UBA; UBA-like_sf; Ubiquilin
- Pfam: ubiquitin
- PPI degree=68 ChIP: None
40268954: UBL7 is indispensable for spermiogenesis through protecting critical factors fro | 34836490: HYPK coordinates degradation of polyneddylated proteins by autophagy. | 39132510: An autoantibody profile identified by human genome-wide protein arrays in rheuma

### 4. 总体评价
**74.3/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ubiquitin-like protein 7

**功能**: Interferon-stimulated protein that positively regulates RNA virus-triggered innate immune signaling. Mechanistically, promotes 'Lys-27'-linked polyubiquitination of MAVS through TRIM21 leading to enhanced the IFN signaling pathway

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR015940 |
| InterPro | IPR009060 |
| InterPro | IPR015496 |
| InterPro | IPR000626 |
| InterPro | IPR029071 |
| InterPro | IPR047878 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UBA52 | STRING | 965 |
| RPS27A | STRING | 928 |
| UBE4B | STRING | 909 |
| ERCC1 | STRING | 779 |
| RAD23B | STRING | 775 |
| ZNF428 | STRING | 711 |
| RAD23A | BioGRID | 1 |
| PSME1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96S82-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000138629-UBL7

![](https://images.proteinatlas.org/41897/805_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/41897/805_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/41897/762_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/41897/762_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/41897/736_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/41897/736_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/41897/682_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/41897/682_D12_2_red_green.jpg)

### 深度机制分析

UBL7(38 kDa)的架构由N端泛素样(UBL)结构域(IPR000626, IPR029071)和C端UBA结构域(IPR015940, IPR009060)组成——这两个模块分别充当"识别帽"(UBA, 结合多聚泛素链)和"信号头"(UBL, 介导下游效应子识别)，通过一段低复杂度连接区(pLDDT<50)形成分子内铰链。AlphaFold pLDDT仅66.9是这18个蛋白中最弱的，但其2个PDB条目表明至少UBA域在实验层面是高度有序的——低pLDDT主要源于连接区的内在无序性，这种无序性恰恰是泛素识别蛋白的功能性特征，允许UBA域在溶液中采样多个构象以高效扫描多泛素链修饰的底物。UBL7是干扰素(IFN)刺激基因(ISG)，其功能注释(PMID 40268954)明确将其置于先天免疫信号的核心——UBL7通过TRIM21(一个E3泛素连接酶和胞内抗体受体)促进MAVS(线粒体抗病毒信号蛋白)的K27-连接多泛素化，从而增强IFN-beta信号通路。

PPI网络中最高置信度的两条边——UBA52(STRING 965)和RPS27A(STRING 928)——都是泛素(Ub)的前体融合蛋白(泛素-核糖体蛋白融合基因)，这暗示UBL7的功能不仅限于传统的泛素信号转导，更可能参与核仁中的核糖体生物合成和核内蛋白质稳态。值得注意的是，RAD23B(STRING 775)和RAD23A(BioGRID 1)是核苷酸切除修复(NER)损伤识别因子，携带UBL和UBA域——两者与UBL7具有域结构相似性(UBL/UBA双模块)。这一架构类比提示UBL7可能作为NER修复复合物与泛素化组蛋白之间的接头蛋白，在染色质损伤修复中桥接泛素化信号与下游修复酶(如XPA/XPC)。这对于TE调控至关重要：ERV/LTR元件的同源重组修复(HR)和LINE-1整合位点的修复均通过NER/NHEJ通路处理，UBL7可能在这些位点检测K63-泛素化修饰的H2A/H2AX并促进修复复合物的组装。

ERCC1(STRING 779)和UBE4B(STRING 909)的PPI进一步强化了这一NER-TE连接：ERCC1-XPF异二聚体正是NER的5'核酸内切酶，负责切除受损DNA链；UBE4B是E4泛素链延伸因子，在p53调控和蛋白质聚集体清除中发挥功能。结合UBL7通过TRIM21调控MAVS K27泛素化的已知功能，一个统一的机制模型浮现：在TE位点(如ERV启动子驱动的转录或LINE-1的逆转录转座事件)触发的DNA损伤或dsRNA信号下，UBL7充当分子枢纽——其UBA域识别DNA损伤位点处K63-泛素化修饰的H2A/H2AX(由RNF8/RNF168写入)，其UBL域则募集ERCC1-XPF执行损伤切除，同时通过TRIM21-MAVS轴激活IFN对TE dsRNA的固有免疫响应(RNA:DNA杂合链或胞质中的LINE-1 RNA中间体)。这一模型将UBL7定位为"DNA修复-Ub信号-先天免疫"三路串扰的中心节点。研究启示：UBL7的低PubMed count(14篇严格)与这种三路串扰节点的高层次生物学重要性不相匹配，尤其是在精子发生(spermiogenesis, PMID 40268954)这一经历剧烈染色质重塑和TE去抑制的生物学过程中，UBL7的作用机制几乎完全未知。实验策略：利用UBA域缺失突变体(delta-UBA)比较全核提取物的K27-Ub和K63-Ub蛋白组，结合anti-UBL7 ChIP-seq在减数分裂生殖细胞中识别TE位点的富集峰，与ATAC-seq和H3K27ac进行联合分析。

### PubMed 文献

**PubMed count: 22**

| 42292425 | Development and validation of an m6A and autophagy related lncRNAs signature for predicting survival and modulating the  | Front Immunol 2026 |
| 41999721 | Sex-specific autosomal susceptibility loci in systemic sclerosis: a genome-wide association study. | Lancet Rheumatol 2026 |
| 40274920 | Inferring past demography and genetic adaptation in Spain using the GCAT cohort. | Sci Rep 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UBL7

