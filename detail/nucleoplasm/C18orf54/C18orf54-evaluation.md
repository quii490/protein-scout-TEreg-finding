---
type: protein-evaluation
gene: "C18orf54"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## C18orf54

### 1. Basic Info
| Item | Value |
|---|---|
| Gene | C18orf54 |
| Protein Name | Lung adenoma susceptibility protein 2 |
| Size | 372 aa / 41.8 kDa |
| UniProt | Q8IYD9 |
| Date | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol; Nucleoplasm; Vesicles (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 372 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=2 |
| 🏗️ 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=59.7; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | Cell_Prolif_Regulator; LAS2 |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=11 |
| **加权总分** | | | **130.0/180** | |
| **归一化总分 (÷1.83)** | | | **71.0/100** | 互证: +1.0 |

### 3. Analysis
- HPA: Cytosol; Nucleoplasm; Vesicles (Approved)
- PubMed: strict=2, broad=3
- AF pLDDT: 59.7 / PDB: 0
- InterPro: Cell_Prolif_Regulator; LAS2
- Pfam: LAS2
- PPI degree=11 ChIP: None
39878408: Transcriptome-Wide Association Study Identified Novel Blood Tissue Gene Biomarke | 37692934: C18ORF54 promotes immune infiltration and poor prognosis as a potential biomarke

### 4. Assessment
★★★★  **71.6/100**  **nucleoplasm**
Nuclear protein


### 深度机制分析

C18orf54（LAS2，肺腺瘤易感蛋白2）是372个氨基酸的功能未知蛋白，其唯一可识别的结构特征是LAS2保守结构域（IPR031587/PF15792）和Cell_Prolif_Regulator分类（IPR052679）。LAS2结构域的功能至今完全未被生化表征——无已知的酶活性、配体结合能力或结构同源性——使C18orf54成为"暗蛋白质组"（dark proteome）的典型代表。AlphaFold预测pLDDT仅59.7（无PDB条目），反映该蛋白可能具有高度柔性或部分无序的结构，这与功能未知蛋白中常见的特征一致——结构信息稀少暗示缺乏高度约束的催化/配体结合口袋。

HPA Approved的核质定位（Cytosol; Nucleoplasm; Vesicles）是三个相互独立的空间局部化模式，暗示该蛋白可能在细胞内膜系统与核质之间进行动态循环。PPI网络（degree=11）中与KDM1A（LSD1，H3K4me1/me2去甲基化酶）和ELAVL1（HuR，RNA结合蛋白）的互作（BioGRID=0）是高度推测性的，但如果获实验验证，将直接将C18orf54连接至两个完全不同的核功能领域——组蛋白去甲基化和mRNA稳定性调控。KDM1A-LAS2互作轴极具吸引力，因为LSD1是谱系决定和白血病发生中的核心表观遗传调控因子。

C18orf54在疾病中的功能暗示来自GWAS和转录组关联研究（TWAS）。作为C18orf54（也被称为RTFC）已被鉴定为甲状腺分化和功能的调节因子（PMID:28230092）及家族性非髓样甲状腺癌的新易感基因（PMID:27864143）。更深远的发现来自C18ORF54在肝细胞癌中促进免疫浸润并指示不良预后的报道（PMID:37692934）。TWAS发现C18orf54是与前列腺癌风险相关的新型血液组织基因生物标志物（PMID:39878408），而更新的败血症易感性研究则涉及C18orf54在免疫应答中的全局调控角色（PMID:40705358）。

从结构-功能-疾病三维框架来看，C18orf54虽然信息极度匮乏，但其在多种上皮来源癌症中的一致关联以及在免疫浸润中的功能性证据，共同指向这一"暗蛋白"可能是肿瘤微环境免疫调控中的隐藏节点。作为PubMed仅3篇的新颖蛋白（新颖性10/10），任何功能发现都可能成为该领域的首创性贡献。从实验设计角度，建议的优先路线为：（1）CRISPR-Cas9敲除后进行RNA-seq以鉴定C18orf54调控的靶基因网络；（2）TurboID邻近标记鉴定核内互作伙伴；（3）评估C18orf54缺失对H3K4甲基化全局水平的影响（验证与KDM1A的功能性关联）。其核定位与细胞增殖调控（2/3的PubMed涉及增殖/癌症）的耦合使其成为TE调控研究中值得优先关注的"暗蛋白"。

**蛋白全称**: Lung adenoma susceptibility protein 2

**功能**: Might play a role in cell proliferation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR052679 |
| InterPro | IPR031587 |
| Pfam | PF15792 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MAGEA11 | BioGRID | 0 |
| ELAVL1 | BioGRID | 0 |
| KDM1A | BioGRID | 0 |
| TP63 | BioGRID | 0 |
| CNTLN | BioGRID | 0 |
| MAGOHB | BioGRID | 0 |
| ENKD1 | BioGRID | 0 |
| HSF2BP | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8IYD9-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166845-C18orf54

![](https://images.proteinatlas.org/77475/2197_G4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/2197_G4_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/2088_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/2088_H2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/1890_M8_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/1890_M8_63_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166845-C18orf54

![](https://images.proteinatlas.org/77475/2197_G4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/2197_G4_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/2088_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/2088_H2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/1890_M8_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/1890_M8_63_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166845-C18orf54

![](https://images.proteinatlas.org/77475/2197_G4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/2197_G4_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/2088_H2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/2088_H2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/1890_M8_62_blue_red_green.jpg)
![](https://images.proteinatlas.org/77475/1890_M8_63_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 3**

| 40705358 | Novel Susceptibility Genes for Sepsis Revealed by a Cross-Tissue Transcriptome-Wide Association Study. | Shock 2026 |
| 39878408 | Transcriptome-Wide Association Study Identified Novel Blood Tissue Gene Biomarkers for Prostate Cancer Risk. | Prostate 2025 |
| 37692934 | C18ORF54 promotes immune infiltration and poor prognosis as a potential biomarker for hepatocellular carcinoma. | Am J Transl Res 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C18orf54

