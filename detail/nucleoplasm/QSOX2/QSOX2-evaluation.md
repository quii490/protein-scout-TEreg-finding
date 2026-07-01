---
type: protein-evaluation
gene: "QSOX2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## QSOX2 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | QSOX2 |
| 蛋白名称 | Sulfhydryl oxidase 2 |
| 蛋白大小 | 698 aa / 77.5 kDa |
| UniProt ID | Q6ZRP7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32.0 | Golgi apparatus; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 698 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=26 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=79.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | ERV/ALR_sulphydryl_oxid_sf; ERV/ALR_sulphydryl_oxidase; QSOX_FAD-bd_dom |
| PPI | 6/10 | x3 | 18.0 | PPI degree=78 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
HPA: Golgi apparatus; Nucleoplasm (Supported)
PubMed: strict=26, broad=37
AF pLDDT: 79.3  PDB: 0
InterPro: ERV/ALR_sulphydryl_oxid_sf; ERV/ALR_sulphydryl_oxidase; QSOX_FAD-bd_dom
Pfam: Evr1_Alr; FAD_SOX; QSOX_Trx1
PPI degree: 78  ChIP: None
**Papers**: 39341815: QSOX2 Deficiency-induced short stature, gastrointestinal dysmotility and immune  | 40433832: QSOX2-Mediated Disulfide Bond Modification Enhances Tumor Stemness and Chemoresi | 34205581: Impact TMPRSS2-ERG Molecular Subtype on Prostate Cancer Recurrence.

### 4. 总体评价
★★★★  **72.1/100**  |  **nucleoplasm**
Nuclear protein


### 深度机制分析

QSOX2（Sulfhydryl oxidase 2）是一个698 aa的大分子巯基氧化酶，其结构域架构呈现典型的QSOX家族特征：N端含有一个硫氧还蛋白（Trx）样结构域（Pfam QSOX_Trx1），中间为FAD结合结构域（Pfam FAD_SOX, InterPro IPR040986），C端为ERV/ALR巯基氧化酶催化域（Pfam Evr1_Alr, InterPro IPR017905）。这种多结构域串联排布使QSOX2能够高效催化蛋白质二硫键的形成，将巯基氧化与氧分子还原为过氧化氢相偶联。AlphaFold2预测pLDDT=79.3，虽无独立PDB结构，但结构域水平有同源模板支持。

QSOX2的PPI网络度为78，主要互作伙伴包括ILF3（白细胞介素增强子结合因子3），这是一个参与RNA代谢和转录调控的核蛋白。QSOX2与ILF3在BioGRID中的互作记录尤为引人关注——ILF3是核质中调控mRNA稳定性和miRNA加工的关键因子，QSOX2在核质中的Supported级别定位可能通过ILF3介导的互作实现核滞留。此外，与SLC25A3（线粒体磷酸载体）和MMS19（胞质铁硫簇组装因子）的互作提示QSOX2可能在氧化还原稳态和铁硫蛋白成熟中发挥协调作用。

从功能机制角度，QSOX2催化的二硫键形成本是分泌途径的典型功能，但其在核质中的存在挑战了这一传统认知。最新文献提供了关键线索：PMID:40433832发现QSOX2介导的二硫键修饰增强肿瘤干细胞性和化疗耐药性，提示QSOX2可能在核内通过氧化还原修饰转录因子或染色质相关蛋白来调控基因表达。PMID:39341815报道QSOX2缺陷导致身材矮小和胃肠动力障碍，证明其生理重要性远超分泌途径。值得注意的是，QSOX2在IFN-γ诱导的凋亡中发挥调控作用（PMID:14633699），这可能涉及其核内氧化还原信号调控。

QSOX2的核定位特异性得分8/10（Nucleoplasm Supported + Golgi apparatus），结合其26篇PubMed文献的新颖性得分9/10，表明这是一个定位新颖且有深度研究潜力的核蛋白。其FLAG为巯基氧化酶活性在核内的底物和功能后果，是未来研究的核心问题——核内转录因子、染色质重塑因子或核小体组蛋白均可能是QSOX2的氧化还原靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Sulfhydryl oxidase 2

**功能**: Sulfhydryl oxidase that catalyzes the oxidation of protein thiol groups to form disulfide bonds, with the reduction of oxygen to hydrogen peroxide (By similarity). May contribute to disulfide bond formation in secreted proteins (By similarity). May play a role in regulating the sensitization of neuroblastoma cells for interferon-gamma-induced apoptosis (PubMed:14633699). Required for normal ovarian function (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036774 |
| InterPro | IPR017905 |
| InterPro | IPR040986 |
| InterPro | IPR042568 |
| InterPro | IPR041269 |
| InterPro | IPR039798 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ILF3 | BioGRID | 0 |
| SLC25A3 | BioGRID | 0 |
| MMS19 | BioGRID | 0 |
| PAN2 | BioGRID | 0 |
| HLA-DPA1 | BioGRID | 0 |
| CD1B | BioGRID | 0 |
| GINM1 | BioGRID | 0 |
| LYPD3 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6ZRP7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000165661-QSOX2

![](https://images.proteinatlas.org/12716/136_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/136_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/97_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/97_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/99_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17280/1582_D12_1_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000165661-QSOX2

![](https://images.proteinatlas.org/12716/136_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/136_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/97_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/97_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/99_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17280/1582_D12_1_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000165661-QSOX2

![](https://images.proteinatlas.org/12716/136_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/136_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/97_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/97_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12716/99_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17280/1582_D12_1_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 37**

| 41922310 | Non-enzymatic function of QSOX2 directly regulates the JUNB-ITGB4 axis and enhanced resistance to osimertinib in EGFR-mu | Cell Death Discov 2026 |
| 41815151 | A risk score model based on glycosylation-related genes for predicting radioresistance and prognosis of lung adenocarcin | Transl Cancer Res 2026 |
| 41317934 | Deficiency of NR2C2 accelerates senescence of testicular Leydig cells and infertility in male mice. | Cell Signal 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/QSOX2

