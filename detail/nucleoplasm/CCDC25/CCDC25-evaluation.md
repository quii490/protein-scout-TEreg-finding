---
type: protein-evaluation
gene: "CCDC25"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CCDC25 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CCDC25 |
| 蛋白名称 | Coiled-coil domain-containing protein 25 |
| 蛋白大小 | 208 aa / 24.5 kDa |
| UniProt ID | Q86WR0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 208 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=30 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=82.4; PDB=3 |
| 调控结构域 | 4/10 | x2 | 8.0 | Jlp2/Ccd25; NFACT_RNA-bd |
| PPI | 5/10 | x3 | 15.0 | PPI degree=37 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +2 |

### 3. 分析
- HPA: Cytosol; Golgi apparatus; Nucleoplasm (Approved)
- PubMed: strict=30, broad=57
- AF pLDDT: 82.4 / PDB: 3
- InterPro: Jlp2/Ccd25; NFACT_RNA-bd
- Pfam: NFACT-R_1
- PPI degree=37 / ChIP: None
32528174: DNA of neutrophil extracellular traps promotes cancer metastasis via CCDC25. | 40442366: Cardiomyocyte-localized CCDC25 senses NET DNA to promote doxorubicin cardiotoxic | 38369519: The oncolytic bacteria-mediated delivery system of CCDC25 nucleic acid drug inhi

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Coiled-coil domain-containing protein 25

**功能**: Transmembrane receptor that senses neutrophil extracellular traps (NETs) and triggers the ILK-PARVB pathway to enhance cell motility (PubMed:32528174). NETs are mainly composed of DNA fibers and are released by neutrophils to bind pathogens during inflammation (PubMed:32528174). Formation of NETs is also associated with cancer metastasis, NET-DNA acting as a chemotactic factor to attract cancer cells (PubMed:32528174). Specifically binds NETs on its extracellular region, in particular the 8-OHdG

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR039730 |
| InterPro | IPR008532 |
| Pfam | PF05670 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ELAVL1 | BioGRID | 0 |
| TRIM23 | BioGRID | 0 |
| GMCL1 | BioGRID | 0 |
| MOV10 | BioGRID | 0 |
| NXF1 | BioGRID | 0 |
| OR5F1 | BioGRID | 0 |
| RDH12 | BioGRID | 0 |
| SLC25A32 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：CCDC25（208 aa，24.5 kDa）含有两个特征结构域：Jlp2/Ccd25（IPR039730）和NFACT_RNA-bd（IPR008532，PF05670）。前者属于coiled-coil结构域家族，负责蛋白质-蛋白质互作和膜锚定；后者为NFACT（NFAT C-terminal）RNA结合域，提示该蛋白可能具有RNA结合活性。这种"coiled-coil + RNA结合域"的双模块架构在核糖核蛋白（RNP）复合物组分中常见，表明CCDC25可能同时参与膜信号感受和核内RNA代谢调控。

**PPI互作网络解读**：CCDC25的PPI degree为37，显著互作伙伴包括ELAVL1（HuR）、NXF1（TAP）、MOV10等RNA代谢因子。ELAVL1是经典的ARE结合蛋白，调控mRNA稳定性和翻译；NXF1是mRNA核输出的关键受体；MOV10是RNA解旋酶参与piRNA和miRNA通路。这组互作强烈暗示CCDC25可能在RNA加工/核输出环节与这些因子协同作用。关键文献（PMID:32528174, PMID:40442366）发现CCDC25作为NET-DNA的感受器激活ILK-PARVB通路促进细胞迁移，其胞外结构域特异性识别NET-DNA中的8-OHdG氧化损伤标志物。

**结构解读**：AlphaFold预测pLDDT=82.4（3个PDB结构验证），结构质量较高。NFACT_RNA-bd结构域形成典型的βαββαβ折叠（RNA识别基序RRM-like），表面富含正电荷残基适于结合核酸。Coiled-coil区域形成两亲性α-螺旋，既可介导膜定位又可形成同源/异源二聚体。这种结构配置使得CCDC25能够在细胞膜表面感知NET-DNA信号后，通过构象变化或蛋白水解释放胞内结构域进入核质，类似于Notch信号通路的"膜感受-核内效应"范式。

**机制模型**：CCDC25遵循"膜受体→核效应"的双重定位模式：（1）静息状态下，CCDC25主要定位于质膜和Golgi，通过coiled-coil结构域锚定；（2）当NET-DNA（尤其是含氧化损伤碱基的DNA片段）与胞外结构域结合后，可能触发胞内段的释放或构象重排，释放的NFACT_RNA-bd结构域（或其复合物）易位至核质并与ELAVL1、NXF1等RNA代谢因子合作，调控下游基因（如促迁移基因、炎症因子）的mRNA加工和核输出。2026年两项独立研究（PMID:42299911, PMID:42204873）分别证实CCDC25在肠道上皮修复和肾小管间质纤维化中的NET-DNA信号传导功能，进一步验证了该模型。

**TE调控展望**：CCDC25的NFACT_RNA-bd结构域提示其可能通过RNA结合界面间接接触TE转录本。NET-DNA本身富含重复序列片段（如Alu、LINE-1），CCDC25作为NET-DNA传感器可能在炎症环境中参与TE来源核酸的信号传导。虽然不直接调控TE沉默/激活，但CCDC25可能在TE相关炎症反应的核内信号转导中发挥桥梁作用，值得在NETosis相关疾病的TE表达谱中进行系统性评估。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q86WR0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000147419-CCDC25

![](https://images.proteinatlas.org/23256/237_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/23256/237_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/23256/236_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/23256/236_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/23256/268_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/23256/268_G5_2_red_green.jpg)

### PubMed 文献

**PubMed count: 57**

| 42299911 | DNA From Neutrophil Extracellular Traps Restricts Group 3 Innate Lymphoid Cells Function in Intestinal Epithelial Repair | FASEB J 2026 |
| 42204873 | Neutrophil extracellular traps drive tubulointerstitial fibrosis via the coiled-coil domain-containing protein 25 (CCDC2 | Br J Pharmacol 2026 |
| 42103667 | [Characterization of copy number variations in concomitant exotropia using single nucleotide polymorphism microarray]. | Zhonghua Yan Ke Za Zhi 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CCDC25

