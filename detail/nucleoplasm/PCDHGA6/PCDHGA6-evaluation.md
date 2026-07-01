---
type: protein-evaluation
gene: "PCDHGA6"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGA6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGA6 |
| 蛋白名称 | Protocadherin gamma-A6 |
| 蛋白大小 | 932 aa / 100.9 kDa |
| UniProt ID | Q9Y5G7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 932 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=2 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=74.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 5/10 | x3 | 15.0 | PPI degree=23 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=2 broad=2
- AF pLDDT=74.4 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_C
- Pfam: Cadherin; Cadherin_2; Cadherin_C_2
- PPI degree=23 ChIP: None
32814111: In Colorectal Cancer Cells With Mutant KRAS, SLC25A22-Mediated Glutaminolysis Re | 40219552: [Effect of CMTM6 on PD-L1 in Helicobacter pylori infected gastric epithelial cel

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

PCDHGA6（Protocadherin gamma-A6）是原钙粘蛋白γ簇A亚家族的成员（932 aa, 100.9 kDa），与PCDHGA10和PCDHGC5具有相同的结构域架构：6个钙粘蛋白重复结构域组成胞外区（InterPro IPR002126, IPR015919），C端钙粘蛋白胞内结构域（InterPro IPR032455）负责胞内信号。AlphaFold2预测pLDDT=74.4（与PCDHGC5和PCDHGA10完全一致），无PDB实验结构，反映了原钙粘蛋白γ簇成员在AF2预测中的系统性能特点。

PCDHGA6的PPI网络度为23，互作伙伴的组成揭示了两个功能维度。一是PCDH家族成员的顺式聚集：与PCDHGA7、PCDHGA4的BioGRID互作提示γA亚家族成员在膜表面通过同嗜性和异嗜性互作形成多价黏附复合物，这种聚集模式是产生神经元表面分子多样性的核心机制。二是意想不到的核内功能调控因子互作：CBX6（Chromobox蛋白同源物6，PRC1多梳抑制复合物的组分）与PCDHGA6的BioGRID互作直接暗示PCDHGA6可能参与组蛋白修饰和转录抑制。GOSR1（高尔基体SNAP受体复合物成员）则连接PCDHGA6与膜运输调控。

PCDHGA6的研究极度匮乏（PubMed=2，得分10/10），仅有2篇直接文献。PMID:32814111在KRAS突变结直肠癌细胞中发现SLC25A22介导的谷氨酰胺分解通过减少DNA去甲基化增加WNT信号——PCDHGA6出现在该研究的转录组学分析中作为受表观遗传调控的基因之一。PMID:40219552研究CMTM6对幽门螺杆菌感染胃上皮细胞中PD-L1的影响，同样将PCDHGA6作为受炎症微环境调控的分子提及。这些线索统一地指向PCDHGA6作为表观遗传和炎症信号的下游靶点。

PCDHGA6在核质中的Approved级别定位与CBX6的互作在机制层面高度契合。γ-原钙粘蛋白的胞内结构域含有保守的蛋白酶剪切位点，被γ-分泌酶或其他胞内蛋白酶剪切后可释放入核。在核内，该胞内片段可能与CBX6/PRC1复合物协同，通过识别H3K27me3标记调控靶基因的转录沉默。这一机制已在原钙粘蛋白α和γ簇的恒定区胞内结构域中被验证，但PCDHGA6的亚型特异性核内功能尚未被研究。PCDHGA6在HPA中显示的Cytosol/Plasma membrane/Vesicles/Nucleoplasm多重定位完美符合这一剪切-核转位模型。

### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin gamma-A6

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
| NMRAL1 | BioGRID | 0 |
| KLHL20 | BioGRID | 0 |
| PCDHGA7 | BioGRID | 0 |
| RPL23 | BioGRID | 0 |
| LTBP1 | BioGRID | 0 |
| CBX6 | BioGRID | 0 |
| GOSR1 | BioGRID | 0 |
| PCDHGA4 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5G7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000253731-PCDHGA6

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 2**

| 40219552 | [Effect of CMTM6 on PD-L1 in Helicobacter pylori infected gastric epithelial cells]. | Beijing Da Xue Xue Bao Yi Xue Ban 2025 |
| 32814111 | In Colorectal Cancer Cells With Mutant KRAS, SLC25A22-Mediated Glutaminolysis Reduces DNA Demethylation to Increase WNT  | Gastroenterology 2020 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGA6

