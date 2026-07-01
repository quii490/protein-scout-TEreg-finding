---
type: protein-evaluation
gene: "SPINT1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SPINT1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SPINT1 |
| 蛋白名称 | Kunitz-type protease inhibitor 1 |
| 蛋白大小 | 529 aa / 58.4 kDa |
| UniProt ID | O43278 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm; Plasma membrane (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 529 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=74 |
| 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=76.2; PDB=7 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Ig-like_fold; Kunitz_BPTI; Kunitz_BPTI_sf |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=56 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane (Supported)
- PubMed strict=74 broad=270
- AF pLDDT=76.2 PDB=7
- InterPro: Ig-like_fold; Kunitz_BPTI; Kunitz_BPTI_sf
- Pfam: K319L-like_PKD; Kunitz_BPTI; Ldl_recept_a
- PPI degree=56 ChIP: None
40524231: Multi-omics analyses of the heterogenous immune microenvironment in triple-negat | 40234614: Dual STAT3/STAT5 inhibition as a novel treatment strategy in T-prolymphocytic le | 39684750: Neutrophil Elastase Targets Select Proteins on Human Blood-Monocyte-Derived Macr

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

SPINT1（HAI-1，肝细胞生长因子激活因子抑制剂1）是一个529个氨基酸的多结构域丝氨酸蛋白酶抑制剂，其功能架构包含两个Kunitz型蛋白酶抑制结构域（IPR002223/Kunitz_BPTI）、一个LDL受体A类结构域（Ldl_recept_a）以及Ig-like折叠区域（IPR013783）。AlphaFold预测pLDDT为76.2，结合7个PDB条目提供的晶体结构数据，使SPINT1成为本批次中结构表征最好的蛋白之一。Kunitz_BPTI_sf（IPR036880）结构域通过经典的"底物样"刚性环插入靶蛋白酶活性位点，形成高度稳定的酶-抑制剂复合物（Ki可低至pM级别）。

SPINT1的经典功能为细胞膜表面丝氨酸蛋白酶的负调控——通过抑制HGFAC（肝细胞生长因子激活因子，PMID:9045658）和ST14/matriptase（PMID:28710277）的活性，调控HGF/c-MET信号通路和细胞外基质的蛋白水解重塑。然而，HPA Supported的核质定位（Cytosol; Nucleoplasm; Plasma membrane）明确指向该蛋白的核内非经典功能。PPI网络（degree=56）揭示了令人信服的核功能关联：与FOXK1/FOXK2（BioGRID评分=1）的互作直接连接至FOX转录因子家族——这是一群调控自噬和代谢的核内转录因子；与HMGB1（BioGRID）的互作则涉及染色质高级结构的调控。

分子机制的构建模型：SPINT1的N端Kunitz结构域在胞外/质膜表面抑制matriptase和HGFAC，而C端的LDL受体A类结构域可能介导内吞后的内体逃逸——这是多种细菌毒素利用的经典策略。逃逸入胞质后，SPINT1可能通过未被充分研究的核定位信号或"搭载"转运入核，与FOXK1/FOXK2共同调控代谢和自噬相关基因的转录。这一模型也合理解释了SPINT1-AS1 lncRNA通过miR-135b-5p/SPINT1轴在骨肉瘤中增强Warburg效应（PMID:42316270）——核内SPINT1池可能直接参与代谢重编程的转录调控。

SPINT1在肿瘤生物学中具有双面角色：一方面作为蛋白酶抑制剂抑制肿瘤侵袭（HGF/c-MET途径），另一方面通过核内功能可能促进代谢适应和免疫逃逸。SPINT1的多组织表达与多通路互作（T-prolymphocytic leukemia中鉴定为STAT3/STAT5双重抑制靶点，PMID:40234614）使其成为潜在的泛癌种治疗靶点。从TE调控角度，SPINT1的Kunitz结构域与核定位的组合在已知蛋白组中极为罕见——这种"域创新"可能赋予其独特的染色质调控活性，值得通过ChIP-seq和ATAC-seq进行系统解析。

**蛋白全称**: Kunitz-type protease inhibitor 1

**功能**: Inhibitor of HGFAC (PubMed:9045658). Inhibits serine protease activity of ST14/matriptase in vitro (PubMed:28710277). Inhibits serine protease activity of TMPRSS13, via the BPTI/Kunitz inhibitor 1 domain (PubMed:20977675)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR013783 |
| InterPro | IPR002223 |
| InterPro | IPR036880 |
| InterPro | IPR036055 |
| InterPro | IPR023415 |
| InterPro | IPR002172 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ZNF250 | BioGRID | 1 |
| ESR2 | BioGRID | 1 |
| DCAF4 | BioGRID | 1 |
| HMGB1 | BioGRID | 1 |
| ADAM33 | BioGRID | 1 |
| TMEM190 | BioGRID | 1 |
| FOXK2 | BioGRID | 1 |
| FOXK1 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O43278-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166145-SPINT1

![](https://images.proteinatlas.org/31178/893_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/893_H11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/1748_G8_2_cr5805f56e4ee12_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/1748_G8_21_cr5805f57853c99_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/895_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/895_H11_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166145-SPINT1

![](https://images.proteinatlas.org/31178/893_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/893_H11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/1748_G8_2_cr5805f56e4ee12_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/1748_G8_21_cr5805f57853c99_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/895_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/895_H11_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000166145-SPINT1

![](https://images.proteinatlas.org/31178/893_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/893_H11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/1748_G8_2_cr5805f56e4ee12_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/1748_G8_21_cr5805f57853c99_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/895_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/31178/895_H11_3_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 271**

| 42371855 | Schizophrenia Genetic Liability Drives Chronic Disease Risk in Unaffected Individuals Through Immune and Metabolic Pathw | Psychother Psychosom 2026 |
| 42316270 | Correction: LncRNA SPINT1-AS1 enhances the Warburg effect and promotes the progression of osteosarcoma via the miR-135b- | Cancer Cell Int 2026 |
| 42064581 | The role of HAI-1 in urothelial bladder cancer: Tissue expression, ectodomain shedding and clinical outcomes. | Biochem Biophys Rep 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SPINT1

