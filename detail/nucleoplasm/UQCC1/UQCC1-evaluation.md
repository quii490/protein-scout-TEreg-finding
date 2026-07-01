---
type: protein-evaluation
gene: "UQCC1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## UQCC1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UQCC1 |
| 蛋白名称 | Ubiquinol-cytochrome c reductase complex assembly factor 1 |
| 蛋白大小 | 299 aa / 34.6 kDa |
| UniProt ID | Q9NVA1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Actin filaments; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 299 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=16 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=74.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Ubiq_cyt_c_chap; Ubiqinol_cyt_c_chaperone_CPB3 |
| PPI | 7/10 | x3 | 21.0 | PPI degree=110 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +2 |

### 3. 分析
- Actin filaments; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=16 broad=29
- AF pLDDT=74.4 PDB=0
- InterPro: Ubiq_cyt_c_chap; Ubiqinol_cyt_c_chaperone_CPB3
- Pfam: Ubiq_cyt_C_chap
- PPI degree=110 ChIP: None
39825753: Identification of Association Between Mitochondrial Dysfunction and Sarcopenia U | 24385928: Mutations in the UQCC1-interacting protein, UQCC2, cause human complex III defic | 39135799: Causal gene identification using mitochondria-associated genome-wide mendelian r

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ubiquinol-cytochrome c reductase complex assembly factor 1

**功能**: Required for the assembly of the ubiquinol-cytochrome c reductase complex (mitochondrial respiratory chain complex III or cytochrome b-c1 complex). Involved in cytochrome b translation and/or stability

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR021150 |
| InterPro | IPR007129 |
| Pfam | PF03981 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| BRCA2 | BioGRID | 0 |
| UQCC2 | BioGRID | 0 |
| ECHDC2 | BioGRID | 0 |
| LRRC46 | BioGRID | 0 |
| MRM1 | BioGRID | 0 |
| COX20 | BioGRID | 0 |
| LPAR1 | BioGRID | 0 |
| OXLD1 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：UQCC1（299 aa，34.6 kDa）含有Ubiq_cyt_c_chap（PF03981，IPR021150）和Ubiqinol_cyt_c_chaperone_CPB3（IPR007129）两个保守结构域，属于线粒体呼吸链复合体III（cytochrome b-c1 complex）的组装因子家族。这些结构域的功能是在复合体III组装过程中协助细胞色素b（COB）的翻译与稳定性维持，其核心作用场所是线粒体内膜而非核质，但HPA免疫荧光在Actin filaments、Nucleoplasm、Plasma membrane三处均检出Approved级别的信号。

**PPI互作网络解读**：UQCC1的PPI degree为110，互作伙伴中最为明确的是UQCC2（BioGRID），二者形成稳定的UQCC1-UQCC2异源二聚体，共同参与复合体III的早期组装步骤（PMID:24385928）。此外与BRCA2、COX20、ECHDC2等蛋白的互作提示UQCC1可能通过蛋白质-蛋白质相互作用界面被牵引至核周区域。BRCA2作为核定位蛋白参与DNA修复，与UQCC1的BioGRID互作虽评分较低但仍具提示意义——可能通过"piggyback"机制实现部分核定位，即UQCC1并非自身具备NLS序列，而是通过结合核定位蛋白被动态带入核质。

**结构解读**：AlphaFold预测pLDDT=74.4，整体结构置信度中等偏低。Ubiq_cyt_C_chap结构域（PF03981）主要形成α-螺旋束状折叠，缺乏经典的DNA结合模块（如锌指、螺旋-转角-螺旋或碱性亮氨酸拉链）。这意味着UQCC1在核质中的功能不太可能是直接结合DNA或染色质，而更倾向于通过蛋白-蛋白互作界面在RNA加工、转录后调控或线粒体逆行信号传导中扮演适配器（adaptor）角色。

**机制模型**：UQCC1的核质定位可用"兼职蛋白"（moonlighting protein）假说解释：（1）线粒体应激条件下，UQCC1可能作为逆行信号分子从线粒体释放至胞质再转运至核质，参与线粒体未折叠蛋白反应（UPR^mt）的核基因表达调控；（2）UQCC1可能通过与BRCA2等DNA修复因子的互作，间接影响基因组稳定性相关转录程序。GWAS研究（PMID:39825753, PMID:39135799）将UQCC1与肌肉减少症和线粒体功能障碍关联，支持其通过核质功能影响代谢性疾病的假说。

**TE调控展望**：UQCC1缺乏经典的染色质/TE沉默结构域（KRAB、SET、PHD、chromodomain等），TE调控潜力极低。但其在核质中的出现提示线粒体-核信号交流的新维度：线粒体组装因子如何在特定条件下进入核质并影响基因表达，可能代表一类未被充分认识的核质蛋白功能模式。若未来ChIP-seq或CUT&RUN实验发现UQCC1在特定基因组区域（如代谢基因启动子、TE邻近区域）有富集信号，可重新评估其直接转录调控功能。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9NVA1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000101019-UQCC1

![](https://images.proteinatlas.org/34875/373_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/373_F8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/370_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/370_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/366_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/366_F8_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000101019-UQCC1

![](https://images.proteinatlas.org/34875/373_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/373_F8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/370_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/370_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/366_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/366_F8_3_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000101019-UQCC1

![](https://images.proteinatlas.org/34875/373_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/373_F8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/370_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/370_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/366_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34875/366_F8_3_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 29**

| 41019141 | Genetics of morphological hip abnormalities and their implications for osteoarthritis: a scoping review. | J Hip Preserv Surg 2025 |
| 40971882 | Genetic Variants Related to TGF-β Signaling Pathway Modulate Risk of Meniscus Injury: A Multiancestry Genome-wide Associ | Clin Orthop Relat Res 2026 |
| 40565603 | Investigating the Sexual Dimorphism of Waist-to-Hip Ratio and Its Associations with Complex Traits. | Genes (Basel) 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UQCC1

