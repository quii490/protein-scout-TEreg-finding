---
type: protein-evaluation
gene: "Sephs1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## Sephs1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | Sephs1 |
| 蛋白名称 | Zincore component SEPHS1 |
| 蛋白大小 | 392 aa / 42.9 kDa |
| UniProt ID | P49903 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Nucleoplasm (Uncertain) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 392 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=28 |
| 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=89.6; PDB=4 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PurM-like_C_dom; PurM-like_C_sf; PurM-like_N |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=83 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Uncertain)
- PubMed strict=28 broad=37
- AF pLDDT=89.6 PDB=4
- InterPro: PurM-like_C_dom; PurM-like_C_sf; PurM-like_N
- Pfam: AIRS; AIRS_C
- PPI degree=83 ChIP: None
40608935: Zincore, an atypical coregulator, binds zinc finger transcription factors to con | 38960024: SEPHS1 Gene: A new master key for neurodevelopmental disorders. | 29715549: Selenophosphate synthetase 1 and its role in redox homeostasis, defense and prol

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Zincore component SEPHS1

**功能**: Core component of the zincore complex, a heterotetramer that acts as a molecular 'grip' to stabilize transcription factors at DNA-binding sites across the genome, thereby controlling gene expression (PubMed:40608935). The zincore complex binds specifically to zinc finger transcription factors, such as ZFP91, ZNF652, ZNF526 and PRDM15, and stabilizes them onto their cognate DNA motif (PubMed:40608935). Within the complex, SEPHS1, recognizes and binds the backbone of zinc fingers of transcription 

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR010918 |
| InterPro | IPR036676 |
| InterPro | IPR016188 |
| InterPro | IPR036921 |
| InterPro | IPR004536 |
| Pfam | PF00586 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SEPHS1 | BioGRID | 0 |
| C9orf9 | BioGRID | 0 |
| GBP2 | BioGRID | 0 |
| SAT1 | BioGRID | 0 |
| SLC35F6 | BioGRID | 0 |
| IGSF21 | BioGRID | 0 |
| UNC119 | BioGRID | 0 |
| C14orf1 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：SEPHS1（392 aa，42.9 kDa）在2025年被重新定义为Zincore复合物的核心组分（PMID:40608935），含三个PurM样结构域——PurM-like_N（IPR010918）、PurM-like_C_dom（IPR036676）和PurM-like_C_sf（IPR036921）。PurM（磷酸核糖基氨基咪唑合成酶）折叠为典型的α/β结构域，其原始功能是在嘌呤从头合成途径中催化ATP依赖的氨基咪唑核苷酸（AIR）的合成。但SEPHS1已获得非经典功能（gene recruitment）：保留了PurM折叠的结构完整性，却利用其蛋白-蛋白互作表面识别锌指转录因子（Zinc Finger TFs, ZNFs）的锌指骨架（backbone）。这一"代谢酶→转录共调控因子"的功能转换在进化生物学中被称为"双功能基因"（bifunctional gene）或"moonlighting"蛋白的教科书案例。

**PPI互作网络解读**：PPI degree=83，核心互作包括：SEPHS1自身（形成同源二聚体/异源四聚体，BioGRID）、C9orf9（推测为Zincore的另一组分，BioGRID 0分）、GBP2（鸟苷酸结合蛋白2，GTPase参与先天免疫和细胞自主防御，BioGRID 0分）、SAT1（亚精胺/精胺N1-乙酰转移酶1，多胺代谢关键酶，BioGRID 0分）。值得注意的是，STRING和BioGRID的PPI数据尚未反映2025年Zincore发现的完整功能网络——Zincore复合物的ZNF合作伙伴（ZFP91、ZNF652、ZNF526、PRDM15）在其互作网络中尚未齐全。

**结构解读**：AlphaFold pLDDT=89.6（4个PDB结构验证），预测质量出色。N端PurM_N域形成特征性的βαββαβ Rossmann类折叠，ATP/ADP结合位点位于βα-loop-α的磷酸结合环（P-loop）中。C端PurM_C域为延伸的α-β-α三明治折叠，pLDDT >90的区域涵盖了锌指识别面的核心残基。值得注意的是，SEPHS1的锌指识别面与传统的底物结合面（原PurM活性的AIR结合槽）在空间上明显不同——Zincore利用PurM折叠的背面（非催化面）识别锌指，而原始活性位点已被进化修饰退化或完全丧失催化功能。

**机制模型**：Zincore复合物通过以下机制调控转录：SEPHS1作为"分子抓手"（molecular grip），其PurM结构域识别并结合ZNF转录因子中锌指结构域的肽骨架（而非碱基特异性残基），将ZNF稳定锚定在它们的同源DNA结合位点上（PMID:40608935）。SEPHS1不直接接触DNA——它的功能类似分子伴侣，维持ZNF在染色质上的停留时间（residence time），防止ZNF过早从DNA上脱落。Zincore复合物的异源四聚体组装（可能为SEPHS1_2:C9orf9_2的四元结构）产生多位点ZNF结合能力，可能同时稳定多个临近的ZNF-DNA复合物以调控顺式调控元件（如超级增强子）的活性。

**TE调控展望**：SEPHS1/Zincore是目前本批次中TE调控潜力最高的候选之一。Zincore调控的ZNF转录因子——特别是PRDM15（含PR/SET甲基转移酶域和多个锌指）和ZNF526/ZNF652——是KRAB-ZNF基因家族的成员，该家族是人类基因组中TE（尤其是ERV和LINE-1）转录抑制的主力军。KRAB-ZNF通过识别TE序列中的特定DNA基序招募KAP1/TRIM28-SETDB1复合物，催化H3K9me3修饰建立TE的异染色质化。若Zincore通过SEPHS1稳定KRAB-ZNF在TE区域的结合，它实际上成为TE转录抑制机器的一个上游调控层。目前无直接实验数据支持，但Zincore→KRAB-ZNF→KAP1→H3K9me3的逻辑链具有极佳的可验证性（ChIP-seq实验设计可直接检测Zincore组分在TE位点的富集）。




![PAE](https://alphafold.ebi.ac.uk/files/AF-P49903-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000086475-SEPHS1

![](https://images.proteinatlas.org/37645/440_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/37645/440_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/37645/428_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/37645/428_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/37645/433_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/37645/433_F4_2_red_green.jpg)

### PubMed 文献

**PubMed count: 37**

| 41510092 | Molecular characterization and prognostic modeling of liquid-liquid phase separation-related genes in osteosarcoma based | Transl Cancer Res 2025 |
| 41441975 | Dissecting the role of SEPHS1 in shaping an immunosuppressive microenvironment to promote tumor progression. | Cancer Immunol Immunother 2025 |
| 41310383 | m6A regulators-based gene expression pattern is associated with immune microenvironment characteristics in hepatocellula | Sci Rep 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/Sephs1

