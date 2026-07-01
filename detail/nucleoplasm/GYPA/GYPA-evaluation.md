---
type: protein-evaluation
gene: "GYPA"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GYPA 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GYPA |
| 蛋白名称 | Glycophorin-A |
| 蛋白大小 | 150 aa / 16.4 kDa |
| UniProt ID | P02724 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 150 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=88 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=59.4; PDB=16 |
| 调控结构域 | 4/10 | x2 | 8.0 | Glycophorin; Glycophorin_CS; GYPA_B |
| PPI | 8/10 | x3 | 24.0 | PPI degree=216 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=88 broad=250
- AF pLDDT=59.4 PDB=16
- InterPro: Glycophorin; Glycophorin_CS; GYPA_B
- Pfam: Glycophorin_A
- PPI degree=216 ChIP: None
36224278: Genetic variation of glycophorins and infectious disease. | 24916810: MN typing discrepancies based on GYPA-B-A hybrid. | 37846713: [Polymorphism of the Full-Length mRNA Sequences of MNS blood group-related genes

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Glycophorin-A

**功能**: Component of the ankyrin-1 complex, a multiprotein complex involved in the stability and shape of the erythrocyte membrane (PubMed:35835865). Glycophorin A is the major intrinsic membrane protein of the erythrocyte. The N-terminal glycosylated segment, which lies outside the erythrocyte membrane, has MN blood group receptors. Appears to be important for the function of SLC4A1 and is required for high activity of SLC4A1. May be involved in translocation of SLC4A1 to the plasma membrane

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001195 |
| InterPro | IPR018938 |
| InterPro | IPR049535 |
| Pfam | PF01102 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GYPB | STRING | 999 |
| KLF1 | STRING | 898 |
| ATAD1 | STRING | 884 |
| HEMGN | STRING | 834 |
| CD34 | STRING | 793 |
| KEL | STRING | 790 |
| GATA1 | STRING | 777 |
| CD38 | STRING | 747 |


### 深度机制分析

**结构域架构**：GYPA/Glycophorin-A（150 aa，16.4 kDa）是红细胞膜上最丰富的整合膜蛋白之一（每个红细胞约10^6拷贝），含Glycophorin结构域（IPR001195，Glycophorin_CS IPR018938，GYPA_B IPR049535，PF01102 Glycophorin_A）。蛋白结构极端简洁：N端胞外域（72 aa）富含O-糖基化位点（约15个O-glycan链）和一个N-糖基化位点，携带MN血型抗原；单次跨膜α-螺旋（19 aa）；C端胞质尾（39 aa）通过Band 3/SLC4A1和ankyrin-1锚定于膜下细胞骨架（spectrin-actin网络，PMID:35835865）。GYPA的胞外域形成高度糖基化的粘蛋白样结构，产生显著的空间位阻和负电荷密度（唾液酸化糖链），构成红细胞糖萼的核心组分。

**PPI互作网络解读**：PPI degree=216，反映其在红细胞生物学中的枢纽地位。核心互作包括：GYPB（Glycophorin-B，STRING 999分，MNS血型系统的密切同源物）、KLF1（Erythroid Kruppel-like factor，STRING 898分，红系分化的主调控转录因子——可能调控GYPA的转录而非直接蛋白互作）、HEMGN（Hemogen，红细胞生成调节因子，STRING 834分）、GATA1（红系转录因子GATA1，STRING 777分，与KLF1类似提示转录调控关系）。与CD34（造血干/祖细胞标志物）、KEL（Kell血型抗原）和CD38（NAD+糖基水解酶）的互作进一步定位其在红系发育和红细胞膜结构中的功能网络。

**结构解读**：AlphaFold pLDDT=59.4（但16个PDB条目可用，结构实验数据丰富），低pLDDT由胞外粘蛋白域的内在无序性导致——高度糖基化区域在预测中因缺乏稳定的二级结构而被AlphaFold以低置信度呈现。跨膜α-螺旋（pLDDT >90）和C端胞质尾（pLDDT 60-75）的预测在实验结构中得到了良好验证。GYPA的跨膜螺旋含GxxxG二聚化基序（Gly79-X-X-X-Gly83），通过螺旋-螺旋互作形成同源二聚体，此为受体型膜蛋白的常见寡聚化机制。GYPA的NMR和晶体结构（PDB: 1AFO等）已详细解析了跨膜二聚化界面。

**机制模型**：GYPA的核心功能框架扎根于红细胞生物学：（1）糖萼形成：胞外域的糖基化产生高度负电荷的表面，形成空间位阻和静电排斥，防止红细胞的自发凝集和机械损伤；（2）膜稳定性：C端胞质尾通过Band 3和ankyrin-1锚定于spectrin-actin细胞骨架，将膜与胞内骨架网络物理连接（类似于Glycophorin C/D的4.1R复合物，但GYPA使用不同的锚定通路）；（3）血型抗原：MN血型由GYPA N端前5个氨基酸残基决定（Ser1/Leu1 + Gly5/Glu5多态性）——这是人类最早被识别的血型系统之一（Landsteiner定律，此处GYPA是MNS系统的核心载体）。

**TE调控展望**：GYPA是典型的谱系限制性标记蛋白（红细胞/红系祖细胞特异性），其核质定位（Cytosol; Nucleoplasm; Plasma membrane Approved）几乎可以确定是红细胞去核过程中的检测假象——哺乳动物红细胞在终末分化中排出细胞核，但残留的核膜碎片、核孔复合物和相关蛋白可能在免疫荧光中产生核质信号。GYPA的"TE调控潜力"为0，但其在血型抗原遗传学（PMID:36224278综述Glycophorin基因变异与传染病易感性、PMID:37846713分析MNS基因的多态性）中作为遗传标记的运用对理解TE驱动的基因家族扩增（如GYP基因簇通过不等交换和基因转换持续演化）具有参考价值。GYPA所在的GYPB-GYPA-GYPE基因簇本身即为TE插入和重组驱动的基因组结构变异的模型系统。


![PAE](https://alphafold.ebi.ac.uk/files/AF-P02724-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 251**

| 42365354 | CD163(+) macrophages coordinate erythroblastic Island formation and iron metabolism to enable glucocorticoid-induced ery | Biomark Res 2026 |
| 42327276 | A Pan-pangenome illuminates complex structural variation and selection in humans, chimpanzees, and bonobos. | bioRxiv 2026 |
| 42295875 | Establishment of a high-resolution melting assay for detection of GYP*Mur allele zygosity. | Blood Transfus 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GYPA

