---
type: protein-evaluation
gene: "PTAFR"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PTAFR 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PTAFR |
| 蛋白名称 | Platelet-activating factor receptor |
| 蛋白大小 | 342 aa / 39.2 kDa |
| UniProt ID | P25105 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm; Plasma membrane; Vesicles (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 342 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=72 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=86.5; PDB=3 |
| 调控结构域 | 4/10 | ×2 | 8.0 | GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; PAF_rcpt |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=58 |
| **加权总分** | | | **126/180** | |
| **归一化总分** | | | **69.9/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane; Vesicles (Supported)
- PubMed strict=72 broad=96
- AF pLDDT=86.5 PDB=3
- InterPro: GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; PAF_rcpt
- Pfam: 7tm_1
- PPI degree=58 ChIP: None
39709510: Identifying PTAFR as a hub gene in atherosclerosis: implications for NETosis and | 36449602: Generation and multiomic profiling of a TP53/CDKN2A double-knockout gastroesopha | 40670400: Adipose tissue-derived PRXL2A suppresses hepatic lipogenesis in a study with mal

### 4. 总体评价
**69.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Platelet-activating factor receptor

**功能**: Receptor for platelet activating factor, a chemotactic phospholipid mediator that possesses potent inflammatory, smooth-muscle contractile and hypotensive activity. Seems to mediate its action via a G protein that activates a phosphatidylinositol-calcium second messenger system

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000276 |
| InterPro | IPR017452 |
| InterPro | IPR002282 |
| Pfam | PF00001 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

PTAFR（Platelet-activating factor receptor，UniProt: P25105，342 aa / 39.2 kDa）的结构域架构分析显示：InterPro结构域包括IPR000276, IPR002282, IPR017452；Pfam注释为PF00001。 AlphaFold预测的pLDDT均值为86.5，表明结构预测置信度较高，核心结构域折叠可靠，但部分柔性区域可能存在构象不确定性。

蛋白质互作网络分析揭示PTAFR与以下关键因子存在相互作用：ARRB2、PTK2、JAK2、TYK2、ARRB1（PPI度为58）。 功能注释显示Receptor for platelet activating factor, a chemotactic phospholipid mediator that possesses potent inflammatory, smooth-muscle contractile and hypotensive activity. Seems to mediate its action via a G。 这些互作伙伴暗示该蛋白可能通过多蛋白复合物参与细胞过程调控，其互作网络的拓扑位置值得进一步实验验证。

从结构-功能机制角度分析，PTAFR的亚细胞定位为，具有明确的核/核周定位特征，提示其可能直接参与染色质水平或核内体的调控过程。 评估综合得分69.9/100，属于中等兴趣候选，在明确核定位后其TE调控潜力可能显著提升。

对于TE调控机制的意义而言，PTAFR的结构域组成不直接指向经典染色质调控因子，但其在核内的存在（若经实验确认）可能暗示非经典TE调控途径。 研究新颖性方面，PubMed检索获得72篇文献，已有较多文献积累，需从TE调控这一非经典视角寻找差异化研究切入点。 代表性文献包括PMID:42292208, 42201776, 41998824等。

综上所述，PTAFR作为一个342 aa / 39.2 kDa的定位蛋白，具有一定的TE调控研究价值，建议首先通过亚细胞分级和免疫荧光明确其在核内的分布模式，再设计针对性的功能实验。 AlphaFold pLDDT=86.5的结构预测可作为设计突变体和结构-功能关系研究的起点。


---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ARRB2 | BioGRID | 0 |
| PTK2 | BioGRID | 0 |
| JAK2 | BioGRID | 0 |
| TYK2 | BioGRID | 0 |
| ARRB1 | BioGRID | 0 |
| CLTC | BioGRID | 0 |
| CALM1 | BioGRID | 0 |
| GTPBP3 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P25105-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000169403-PTAFR

![](https://images.proteinatlas.org/27543/256_B10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/256_B10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/255_B10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/255_B10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/257_B10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/257_B10_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000169403-PTAFR

![](https://images.proteinatlas.org/27543/256_B10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/256_B10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/255_B10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/255_B10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/257_B10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/257_B10_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000169403-PTAFR

![](https://images.proteinatlas.org/27543/256_B10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/256_B10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/255_B10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/255_B10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/257_B10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27543/257_B10_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 96**

| 42292208 | Integrated systems toxicology identifies TCDD-responsive targets linked to immune dysregulation and treatment response i | Front Med (Lausanne) 2026 |
| 42201776 | Role of Lipid Signaling by PTAFR in Tubular Epithelial Cells in AKI-to-CKD Transition. | J Am Soc Nephrol 2026 |
| 41998824 | Basophil FCER1A and PTAFR Gene Expression Profiles Correlate With Disease Severity in Chronic Spontaneous Urticaria. | Clin Transl Allergy 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PTAFR

