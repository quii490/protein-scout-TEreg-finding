---
type: protein-evaluation
gene: "RRAD"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RRAD 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RRAD |
| 蛋白名称 | GTP-binding protein RAD |
| 蛋白大小 | 308 aa / 33.2 kDa |
| UniProt ID | P55042 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Flagellar centriole; Golgi apparatus; Nucleoplasm; (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 308 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=66 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=73.4; PDB=5 |
| 调控结构域 | 4/10 | x2 | 8.0 | P-loop_NTPase; RGK; RGK_GTP-binding_reg |
| PPI | 5/10 | x3 | 15.0 | PPI degree=20 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **69.9/100** | 互证: +1 |

### 3. 分析
- Flagellar centriole; Golgi apparatus; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=66 broad=179
- AF pLDDT=73.4 PDB=5
- InterPro: P-loop_NTPase; RGK; RGK_GTP-binding_reg
- Pfam: Ras
- PPI degree=20 ChIP: None
36979412: Friend or Foe: Regulation, Downstream Effectors of RRAD in Cancer. | 41032675: RRAD-reduction reveals efficacy of targeting L-type calcium channel regulation f | 32984315: The Cardiac Syndecan-2 Interactome.

### 4. 总体评价
**69.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: GTP-binding protein RAD

**功能**: May regulate basal voltage-dependent L-type Ca(2+) currents and be required for beta-adrenergic augmentation of Ca(2+) influx in cardiomyocytes, thereby regulating increases in heart rate and contractile force (By similarity). May play an important role in cardiac antiarrhythmia via the strong suppression of voltage-gated L-type Ca(2+) currents (By similarity). Regulates voltage-dependent L-type calcium channel subunit alpha-1C trafficking to the cell membrane (By similarity). Inhibits cardiac h

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR017358 |
| InterPro | IPR051641 |
| InterPro | IPR005225 |
| InterPro | IPR001806 |
| Pfam | PF00071 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

RRAD（GTP-binding protein RAD，UniProt: P55042，308 aa / 33.2 kDa）的结构域架构分析显示：InterPro结构域包括IPR001806, IPR005225, IPR017358, IPR027417, IPR051641；Pfam注释为PF00071。 AlphaFold预测的pLDDT均值为73.4，整体结构置信度中等，部分区域可能为内在无序区，需要注意其构象柔性对功能的影响。

蛋白质互作网络分析揭示RRAD与以下关键因子存在相互作用：YWHAZ、CAMK2G、TPM2、NME1、PRKACA（PPI度为20）。 功能注释显示May regulate basal voltage-dependent L-type Ca(2+) currents and be required for beta-adrenergic augmentation of Ca(2+) influx in cardiomyocytes, thereby regulating increases in heart rate and contract。 这些互作伙伴暗示该蛋白可能通过多蛋白复合物参与细胞过程调控，其互作网络的拓扑位置值得进一步实验验证。

从结构-功能机制角度分析，RRAD的亚细胞定位为，具有明确的核/核周定位特征，提示其可能直接参与染色质水平或核内体的调控过程。 评估综合得分69.9/100，属于中等兴趣候选，在明确核定位后其TE调控潜力可能显著提升。

对于TE调控机制的意义而言，RRAD的结构域组成不直接指向经典染色质调控因子，但其在核内的存在（若经实验确认）可能暗示非经典TE调控途径。 研究新颖性方面，PubMed检索获得66篇文献，已有较多文献积累，需从TE调控这一非经典视角寻找差异化研究切入点。 代表性文献包括PMID:41809502, 41377509, 41342134等。

综上所述，RRAD作为一个308 aa / 33.2 kDa的定位蛋白，具有一定的TE调控研究价值，建议首先通过亚细胞分级和免疫荧光明确其在核内的分布模式，再设计针对性的功能实验。 AlphaFold pLDDT=73.4的结构预测可作为设计突变体和结构-功能关系研究的起点。


---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| YWHAZ | BioGRID | 0 |
| CAMK2G | BioGRID | 0 |
| TPM2 | BioGRID | 0 |
| NME1 | BioGRID | 0 |
| PRKACA | BioGRID | 0 |
| PRKCA | BioGRID | 0 |
| CSNK2A1 | BioGRID | 0 |
| CSNK2B | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P55042-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166592-RRAD

![](https://images.proteinatlas.org/41755/2184_E4_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/41755/2184_E4_55_blue_red_green.jpg)
![](https://images.proteinatlas.org/41755/2239_F3_26_blue_red_green.jpg)
![](https://images.proteinatlas.org/41755/2239_F3_32_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166592-RRAD

![](https://images.proteinatlas.org/41755/2184_E4_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/41755/2184_E4_55_blue_red_green.jpg)
![](https://images.proteinatlas.org/41755/2239_F3_26_blue_red_green.jpg)
![](https://images.proteinatlas.org/41755/2239_F3_32_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166592-RRAD

![](https://images.proteinatlas.org/41755/2184_E4_43_blue_red_green.jpg)
![](https://images.proteinatlas.org/41755/2184_E4_55_blue_red_green.jpg)
![](https://images.proteinatlas.org/41755/2239_F3_26_blue_red_green.jpg)
![](https://images.proteinatlas.org/41755/2239_F3_32_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 179**

| 41809502 | Plasma p-tau217 and APOE genotype: Prodromal Alzheimer's disease staging. | Alzheimers Dement (Amst) 2026 |
| 41377509 | A Functional Resting-State Network Atlas Based on 420 Older Adults with Hypertension. | bioRxiv 2025 |
| 41342134 | L-Type Ca(v)1.3 and HCN Channels Mediate Heart Rate Acceleration by Catecholamines. | Circ Res 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RRAD

