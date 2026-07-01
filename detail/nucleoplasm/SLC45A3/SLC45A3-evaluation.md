---
type: protein-evaluation
gene: "SLC45A3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC45A3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC45A3 |
| 蛋白名称 | Solute carrier family 45 member 3 |
| 蛋白大小 | 553 aa / 59.3 kDa |
| UniProt ID | Q96JT2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 553 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=51 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=76.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | MFS; MFS_trans_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=17 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Approved)
- PubMed strict=51 broad=69
- AF pLDDT=76.7 PDB=0
- InterPro: MFS; MFS_trans_sf
- Pfam: MFS_1
- PPI degree=17 ChIP: None
22821757: Loss of SLC45A3 protein (prostein) expression in prostate cancer is associated w | 20118910: Prevalence of TMPRSS2-ERG and SLC45A3-ERG gene fusions in a large prostatectomy  | 18172298: Characterization of TMPRSS2:ETV5 and SLC45A3:ETV5 gene fusions in prostate cance

### 4. 总体评价
**66.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Solute carrier family 45 member 3

**功能**: Proton-associated sucrose transporter. May be able to transport also glucose and fructose

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011701 |
| InterPro | IPR036259 |
| Pfam | PF07690 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：SLC45A3（Q96JT2, Solute carrier family 45 member 3, 553 aa / 59.3 kDa）的主要结构域注释为MFS, MFS_trans_sf。Pfam数据库进一步识别到MFS_1等保守域。AlphaFold pLDDT=76.7（中等）——折叠域基本可信，但部分区域置信度较低，建议实验解析。该蛋白暂无实验PDB结构（PDB=0），当前结构信息完全依赖AlphaFold预测。PubMed=51（低文献量），该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=17）——STRING数据库记录的互作伙伴包括ACPP、ETV1、KLK3、KLKB1、TMPRSS2、ELK4。

**结构解读**：AlphaFold预测（pLDDT=76.7）整体折叠可信，MFS构成结构核心。Pfam域MFS_1的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=76.7提示存在显著的柔性区段，可能需要在蛋白互作伴侣存在的条件下才能完全折叠。

**机制模型**：SLC45A3为Major Facilitator Superfamily（MFS）转运蛋白——其12-transmembrane helix架构负责solute translocation across membrane。作为跨膜转运蛋白，SLC45A3的TE调控关联可能通过metabolite/nutrient sensing→signaling cascade→chromatin state间接实现。

**TE调控展望**：SLC45A3的TE regulation潜力目前缺乏直接的实验证据。TE调控关联性取决于以下几个方面：（1）SLC45A3是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）SLC45A3是否能够通过其结构域识别TE-derived DNA/RNA element；（3）SLC45A3的knockout/knockdown是否改变LINE-1或ERV family的expression level。SLC transporter与TE association常通过metabolic reprogramming→epigenetic remodeling pathway实现——metabolite（如alpha-ketoglutarate, acetyl-CoA）作为chromatin modifier的cofactor，直接influence DNA/histone modification状态。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ACPP | STRING | 915 |
| ETV1 | STRING | 892 |
| KLK3 | STRING | 860 |
| KLKB1 | STRING | 860 |
| TMPRSS2 | STRING | 859 |
| ELK4 | STRING | 841 |
| NUCKS1 | STRING | 823 |
| ETV5 | STRING | 811 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96JT2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC45A3

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000158715-SLC45A3

![](https://images.proteinatlas.org/19073/198_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19073/198_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19073/154_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19073/154_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19075/152_G9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19075/152_G9_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000158715-SLC45A3

![](https://images.proteinatlas.org/19073/198_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19073/198_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19073/154_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19073/154_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19075/152_G9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19075/152_G9_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000158715-SLC45A3

![](https://images.proteinatlas.org/19073/198_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19073/198_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19073/154_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19073/154_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19075/152_G9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19075/152_G9_2_blue_red_green.jpg)

### PubMed

**Count: 69**

| PMID | Title |
|---|---|
| 42283571 | CCDC77 and SLC45A3 mediate the genetic mechanism of Hashimoto's thyroiditis through IL-6. |
| 41524821 | Sugar transporter SLC45 gene family members: roles in malignant tumors and research progress. |
| 40268337 | Peripheral blood GATA2 expression impacts RNF213 mutation penetrance and clinical severity in moyamoya disease. |
| 40114082 | Abnormal DNA methylation of EBF1 regulates adipogenesis in chicken. |
| 38745909 | MIR4435-2HG as a possible novel predictive biomarker of chemotherapy response and death in pediatric B-cell ALL. |
