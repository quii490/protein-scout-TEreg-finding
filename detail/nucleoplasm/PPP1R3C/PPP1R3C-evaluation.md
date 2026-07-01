---
type: protein-evaluation
gene: "PPP1R3C"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PPP1R3C 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PPP1R3C |
| 蛋白名称 | Protein phosphatase 1 regulatory subunit 3C |
| 蛋白大小 | 317 aa / 36.4 kDa |
| UniProt ID | Q9UQK1 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 317 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=62 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=67.6; PDB=4 |
| 调控结构域 | 4/10 | x2 | 8.0 | CBM21_dom; CBM21_dom_sf; Pase-1_reg-su_3B/C/D_met |
| PPI | 5/10 | x3 | 15.0 | PPI degree=42 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=62 broad=104
- AF pLDDT=67.6 PDB=4
- InterPro: CBM21_dom; CBM21_dom_sf; Pase-1_reg-su_3B/C/D_met
- Pfam: CBM_21
- PPI degree=42 ChIP: None
38099490: Aryl hydrocarbon receptor sulfenylation promotes glycogenolysis and rescues canc | 31181215: PPP1R3C mediates metformin-inhibited hepatic gluconeogenesis. | 41516135: Differentially Expressed Genes Associated with the Development of Cervical Cance

### 4. 总体评价
**66.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein phosphatase 1 regulatory subunit 3C

**功能**: Acts as a glycogen-targeting subunit for PP1 and regulates its activity. Activates glycogen synthase, reduces glycogen phosphorylase activity and limits glycogen breakdown. Dramatically increases basal and insulin-stimulated glycogen synthesis upon overexpression in a variety of cell types

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR005036 |
| InterPro | IPR038175 |
| InterPro | IPR017434 |
| InterPro | IPR030683 |
| InterPro | IPR050782 |
| Pfam | PF03370 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：PPP1R3C（Q9UQK1, PP1 regulatory subunit 3C, 317 aa / 36.4 kDa）的主要结构域注释为CBM21_dom, CBM21_dom_sf, Pase-1_reg-su_3B/C/D_met。Pfam数据库进一步识别到CBM_21等保守域。AlphaFold pLDDT=67.6（中低置信度）——结构预测显示较大无序区域，可能含IDR（intrinsically disordered region）或需要结合伴侣才能有序折叠。该蛋白已有4个实验PDB结构条目，为机械性研究提供直接的结构基础。PubMed=62，该蛋白处于早期研究阶段，深入的机制解析仍属空白。

**PPI互作网络解读**：PPI network（degree=42）——BioGRID数据库记录的互作伙伴包括NHLRC1、EPM2A、SGTA、PPP1CA、ELAVL1、APP。其中NHLRC1、PPP1CA、ELAVL1等具有染色质调控或转录相关功能——提示PPP1R3C可能通过protein-protein interaction平台间接参与核内转录调控网络。

**结构解读**：InterPro注释到3个结构域条目——CBM21_dom、CBM21_dom_sf、Pase-1_reg-su_3B/C/D_met。Pfam域CBM_21的保守性暗示了该蛋白可能执行特定的分子功能（如催化、识别或支架）。有序区域占比是衡量该蛋白是否适合structural biology研究的关键指标。pLDDT=67.6提示存在显著的柔性区段，可能需要在蛋白互作伴侣存在的条件下才能完全折叠。

**机制模型**：PPP1R3C为protein phosphatase 1（PP1）的glycogen-targeting regulatory subunit——其CBM21 domain（carbohydrate binding module family 21）将PP1 catalytic subunit定位至glycogen particle。PPP1R3C通过调控glycogen metabolism间接影响cellular energy homeostasis——其在nucleoplasm中的定位暗示可能参与nutrient sensing-to-chromatin coupling。

**TE调控展望**：PPP1R3C的TE regulation潜力目前缺乏直接的实验证据。TE调控关联性取决于以下几个方面：（1）PPP1R3C是否physical association with chromatin remodeling complex（如SWI/SNF, NuRD, PRC1/2）或transcription factor machinery；（2）PPP1R3C是否能够通过其结构域识别TE-derived DNA/RNA element；（3）PPP1R3C的knockout/knockdown是否改变LINE-1或ERV family的expression level。建议通过affinity purification-MS鉴定PPP1R3C在核内的完整interactome——尤其是chromatin reader/writer/eraser复合体的成员。Combined with RNA-seq upon knockdown/overexpression——可在transcriptome level评估其对TE subfamily expression的潜在影响。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NHLRC1 | BioGRID | 0 |
| EPM2A | BioGRID | 0 |
| SGTA | BioGRID | 0 |
| PPP1CA | BioGRID | 0 |
| ELAVL1 | BioGRID | 0 |
| APP | BioGRID | 0 |
| PPP1CC | BioGRID | 0 |
| PPP1CB | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UQK1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PPP1R3C

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000119938-PPP1R3C

![](https://images.proteinatlas.org/43875/1047_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1047_H4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1422_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1422_B9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1048_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1048_H4_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000119938-PPP1R3C

![](https://images.proteinatlas.org/43875/1047_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1047_H4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1422_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1422_B9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1048_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1048_H4_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000119938-PPP1R3C

![](https://images.proteinatlas.org/43875/1047_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1047_H4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1422_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1422_B9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1048_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43875/1048_H4_2_blue_red_green.jpg)

### PubMed

**Count: 104**

| PMID | Title |
|---|---|
| 42176224 | NR5A2 controls gene expression and chromatin contacts of essential circadian metabolic genes in the liver. |
| 41781186 | PPP1R3C functions as a tumor suppressor in endometrial cancer through promotion of glycogen synthesis. |
| 41516135 | Differentially Expressed Genes Associated with the Development of Cervical Cancer. |
| 41465598 | B-Cell Receptor-Associated Protein 31 Deficiency Aggravates Ethanol-Induced Liver Steatosis and Liver Injury via Attenuating Fatty Acid Oxidation and  |
| 41402325 | Multi-layered transcriptional control of glycogen metabolism coordinates thermogenic remodeling of white adipocytes in male mice. |
