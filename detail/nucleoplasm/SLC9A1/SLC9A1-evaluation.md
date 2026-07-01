---
type: protein-evaluation
gene: "SLC9A1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC9A1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC9A1 |
| 蛋白名称 | Sodium/hydrogen exchanger 1 |
| 蛋白大小 | 815 aa / 90.8 kDa |
| UniProt ID | P19634 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm; Plasma membrane (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 815 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=68 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=67.6; PDB=17 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Cation/H_exchanger_CPA1; Cation/H_exchanger_TM; NaH_exchanger |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=150 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Supported)
- PubMed strict=68 broad=708
- AF pLDDT=67.6 PDB=17
- InterPro: Cation/H_exchanger_CPA1; Cation/H_exchanger_TM; NaH_exchanger
- Pfam: Na_H_Exchanger; NEXCaM_BD
- PPI degree=150 ChIP: None
38509618: Deletion of Slc9a1 in Cx3cr1(+) cells stimulated microglial subcluster CREB1 sig | 30302044: Hyperammonemia in Hepatic Encephalopathy. | 39955862: Identifying prognostic biomarkers and immune interactions in ovarian cancer asso

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Sodium/hydrogen exchanger 1

**功能**: Electroneutral Na(+) /H(+) antiporter that extrudes Na(+) in exchange for external protons driven by the inward sodium ion chemical gradient, protecting cells from acidification that occurs from metabolism (PubMed:11350981, PubMed:11532004, PubMed:14680478, PubMed:15035633, PubMed:15677483, PubMed:17073455, PubMed:17493937, PubMed:22020933, PubMed:27650500, PubMed:32130622, PubMed:7110335, PubMed:7603840). Exchanges intracellular H(+) ions for extracellular Na(+) in 1:1 stoichiometry (By similar

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR018422 |
| InterPro | IPR006153 |
| InterPro | IPR004709 |
| InterPro | IPR001970 |
| InterPro | IPR032103 |
| Pfam | PF00999 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CALM3 | STRING | 991 |
| HEL-S-72 | STRING | 948 |
| CALM1 | STRING | 948 |
| MAPK3 | STRING | 946 |
| CALML6 | STRING | 936 |
| MAPK1 | STRING | 921 |
| ERK2 | STRING | 921 |
| ROCK2 | STRING | 916 |


### 深度机制分析

**结构域架构**：SLC9A1（815 aa, 90.8 kDa, NHE1）是CPA1家族（cation/proton antiporter-1）Na⁺/H⁺ exchanger。N端跨膜结构域（aa 1-500）含12个跨膜螺旋（TM1-TM12），形成Na⁺/H⁺交换孔——TM4和TM11中的保守Asp和Glu残基参与离子配位和质子传递。C端胞质调控域（aa 501-815）含NEXCaM_BD（Na⁺/H⁺ exchanger calmodulin-binding domain, Pfam）和多个磷酸化位点——Calmodulin（Ca²⁺-CaM）结合于C端高亲和力位点（aa 636-656），在胞内Ca²⁺升高时促进自抑制释放（autoinhibition relief）。AlphaFold pLDDT=67.6（PDB=17, 共17个晶体/冷冻电镜结构，结构表征极丰富）——TM域pLDDT>85（跨膜螺旋高度有序），C端调控域pLDDT~50-65（部分无序——经典的"fuzzy complex"特征：与多个伴侣（CaM, CHP1/2, PIP2）相互作用时有序化）。

**PPI互作网络解读**：PPI network（degree=150）以CaM信号和MAPK通路为中心。CALM3/CALM1（STRING scores 991/948）——Ca²⁺-bound calmodulin结合NHE1 C端并解除其自抑制——这是细胞内酸化→Na⁺/H⁺交换激活→pH恢复（pH recovery）的核心机制。MAPK3/ERK1和MAPK1/ERK2（STRING scores 946/921）直接磷酸化NHE1 C端Ser703/Ser770/Ser785等位点→增强NHE1活性（growth factor-induced NHE1 activation）。ROCK2（Rho-associated protein kinase 2, STRING score=916）通过RhoA-ROCK信号磷酸化NHE1→调控actin cytoskeleton remodeling→影响细胞迁移中的前沿（leading edge）pH微环境。CALML6（calmodulin-like 6, STRING score=936）作为CaM亚型可能提供组织特异性的NHE1调控。

**结构解读与机制模型**：NHE1以二聚体形式在质膜上行使功能——每个单体独立催化Na⁺（in）/H⁺（out）电中性交换（1:1 stoichiometry）。C端调控域的pH sensor（pH sensing residues His-rich region）感知胞内pH——当pHi<7.0（酸中毒），His残基质子化→构象变化→C端释放对N端TM域的抑制→Na⁺/H⁺交换速率升高。在核质（HPA Supported Nucleoplasm + Plasma membrane）中，NHE1的核内定位意味着核质pH稳态维持的直接角色——细胞核具有独立于胞质的pH调节系统（nuclear pH ~7.3-7.4, 略高于胞质pH ~7.1-7.2）——核内NHE1可能经inner nuclear membrane定位和功能调控染色质的pH依赖状态（组蛋白电荷、DNA电荷）→影响染色质凝聚和转录活性。癌症中NHE1过度活化造成胞外微环境酸化（pH 6.5-6.8）和胞内碱化（pHi >7.4）——碱化的核内pH增强组蛋白乙酰化（HAT活性pH optimum 7.5-8.0），促进常染色质（euchromatin）转录活性。

**TE调控展望**：NHE1通过pH稳态间接参与TE调控。细胞核pH是LINE-1 and ERV转录的重要调节因素——酸性核pH抑制RNA Pol II延伸（降低转录效率），而碱性核pH促进Pol II processivity和转录活性。NHE1驱动的核碱化可增强TE mRNA的转录效率——尤其在癌细胞的pH失调微环境中（nuclear alkalinization）。此外，NHE1-ERK通路（growth factor→ERK→NHE1 Ser phosphorylation→NHE1 activation→pHi升高）可被MEK/ERK通路激活的LINE-1 L1Hs 5'UTR sense promoter增强——ERK磷酸化RUNX3/SOX2等转录因子→直接激活LINE-1 5'UTR——形成正反馈循环（ERK→NHE1→nuclear alkalinization→Pol II processivity↑→LINE-1 expression↑→ORF1p/ORF2p→new insertions）。ROCK-actin remodeling调控逆转录转座复合物（RTC）的胞质运输和核内定位——NHE1-ROCK2互作可能影响LINE-1 RNP的亚细胞运输效率。



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000090020-SLC9A1

![](https://images.proteinatlas.org/52891/844_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52891/844_H1_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/52891/867_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52891/867_E12_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000090020-SLC9A1

![](https://images.proteinatlas.org/52891/844_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52891/844_H1_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/52891/867_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52891/867_E12_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000090020-SLC9A1

![](https://images.proteinatlas.org/52891/844_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52891/844_H1_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/52891/867_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52891/867_E12_3_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 710**

| 42214778 | Effects of obacunone against myocardial fibrosis: Mechanistic insights from network pharmacology and experimental valida | Eur J Pharmacol 2026 |
| 42203519 | Comparative analysis of acidosis defense mechanisms in preimplantation embryos in BALB/c strain mice: in vivo vs in vitr | Reprod Fertil Dev 2026 |
| 42193876 | Acidosis Drives Vasculogenic Mimicry in PDAC CSCs via Na+/H+ Exchanger Isoform 1 (NHE1) and Calcium Entry. | Cells 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC9A1

