---
type: protein-evaluation
gene: "PYURF"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PYURF 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PYURF |
| 蛋白名称 | Protein preY, mitochondrial |
| 蛋白大小 | 114 aa / 12.7 kDa |
| UniProt ID | Q96I23 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 114 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=3 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=76.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Trm112-like |
| PPI | 5/10 | x3 | 15.0 | PPI degree=14 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=3 broad=5
- AF pLDDT=76.8 PDB=0
- InterPro: Trm112-like
- Pfam: Trm112p
- PPI degree=14 ChIP: None
35614220: Defining mitochondrial protein functions through deep multiomic profiling. | 35881696: Human mitochondrial protein complexes revealed by large-scale coevolution analys | 38718700: Unraveling inbreeding patterns and selection signals in Alpine Grey cattle.

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein preY, mitochondrial

**功能**: In mitochondria, S-adenosylmethionine-dependent methyltransferase chaperone that supports both coenzyme Q biosynthesis, by stabilizing its components, such as COQ5, and NADH:ubiquinone oxidoreductase complex (complex I, MT-ND1) assembly, by stabilizing complex I assembly factors, such as NDUFAF5

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR005651 |
| Pfam | PF03966 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

PYURF(Protein preY, mitochondrial)是保守的Trm112-like甲基转移酶伴侣蛋白，属于Trm112超家族。其核心结构域为Trm112-like(IPR005651/PF03966)，该结构域在进化上极其保守——从酵母Trm112到人类PYURF氨基酸同一性超过30%。Trm112-like结构域采用紧凑的锌指样折叠拓扑，通过识别SAM依赖甲基转移酶(MTases)的N端螺旋区域形成1:1异源二聚体伴侣复合物，稳定MTase的活性构象并增强其底物亲和力。pLDDT=76.8，符合这种伴侣蛋白紧凑折叠的高预测置信度。

在线粒体中，PYURF具有双功能甲基转移酶伴侣活性：(1)辅酶Q(coenzyme Q)生物合成——PYURF与COQ5(甲基转移酶伴侣，BioGRID互作)形成复合物，稳定COQ5结构，使C-甲基转移酶能够完成CoQ前体的芳环甲基化修饰；(2)复合物I(NADH:ubiquinone oxidoreductase)组装——PYURF与NDUFAF5(复合物I装配因子，甲基转移酶)异源二聚，确保MT-ND1亚基的正常整合(PMID:35614220, PMID:35881696)。

HPA定位为Nucleoplasm(Approved)，但PYURF蛋白主序列含N端线粒体靶向序列(MTS)，其成熟形式通常定位于线粒体基质。核质定位可能通过以下非经典机制实现：MTS的"模糊靶向"(ambiguous targeting)导致少部分新生PYURF在胞质合成后未进入线粒体输入通道，而是通过被动扩散进入核孔(分子量仅12.7 kDa，<40 kDa核孔大小限制)，在核质中发挥未知的Trm112-like伴侣功能。

PPI degree仅14，与线粒体代谢酶(COQ5、PDK1、PGD、HINT2、ABAT)形成以BioGRID为主的互作网络。其中，PGD(6-磷酸葡萄糖酸脱氢酶)互作尤为有趣——PGD是戊糖磷酸途径(PPP)第一步氧化反应的催化酶，产生NADPH和核酮糖-5-磷酸。如果PYURF在核质中稳定PGD蛋白水平或活性，则可间接调控核质NADPH/NADP⁺比值，影响核内氧化还原敏感转录因子(Nrf2、HIF-1α等)的活性。PubMed仅3篇，是线粒体-核质Crosstalk研究的前沿候选因子。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96I23-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000145337-PYURF

![](https://images.proteinatlas.org/36455/440_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/36455/440_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/36455/428_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/36455/428_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/36455/433_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/36455/433_F12_2_red_green.jpg)

### PubMed 文献

**PubMed count: 5**

| 38998043 | Genomic Characterization of Local Croatian Sheep Breeds-Effective Population Size, Inbreeding & Signatures of Selection. | Animals (Basel) 2024 |
| 38718700 | Unraveling inbreeding patterns and selection signals in Alpine Grey cattle. | Animal 2024 |
| 35881696 | Human mitochondrial protein complexes revealed by large-scale coevolution analysis and deep learning-based structure mod | Bioinformatics 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PYURF

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| COQ5 | physical | Floyd BJ (2016) |
| PDK1 | physical | Liu X (2018) |
| PGD | physical | Moutaoufik MT (2019) |
| HEBP1 | physical | Moutaoufik MT (2019) |
| HINT2 | physical | Moutaoufik MT (2019) |
| ABAT | physical | Moutaoufik MT (2019) |
| GSTO1 | physical | Moutaoufik MT (2019) |

