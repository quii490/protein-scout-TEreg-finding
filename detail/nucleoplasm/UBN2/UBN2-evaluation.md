---
type: protein-evaluation
gene: "UBN2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## UBN2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UBN2 |
| 蛋白名称 | Ubinuclein-2 |
| 蛋白大小 | 1347 aa / 146.1 kDa |
| UniProt ID | Q6ZU65 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Enhanced) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 1347 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=14 |
| 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=51.1; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | HRD; UBN_middle_dom |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=84 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **67.2/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Enhanced)
- PubMed strict=14 broad=21
- AF pLDDT=51.1 PDB=0
- InterPro: HRD; UBN_middle_dom
- Pfam: HUN; UBN_AB
- PPI degree=84 ChIP: None
39509271: HIRA protects telomeres against R-loop-induced instability in ALT cancer cells. | 40455860: Ubinuclein 2 is essential for mouse development and functions in X chromosome in | 36229758: Circ_0060967 facilitates proliferation, migration, and invasion of non-small-cel

### 4. 总体评价
**67.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ubinuclein-2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR014840 |
| InterPro | IPR026947 |
| Pfam | PF08729 |
| Pfam | PF14075 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Ubinuclein-2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR014840 |
| InterPro | IPR026947 |
| Pfam | PF08729 |
| Pfam | PF14075 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HIRA | STRING | 881 |
| CABIN1 | STRING | 872 |
| ASF1A | STRING | 831 |
| ASF1B | STRING | 793 |
| EWSR1 | BioGRID | 1 |
| CDX1 | BioGRID | 1 |
| TFAP4 | BioGRID | 1 |
| TEAD2 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6ZU65-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UBN2

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000157741-UBN2

![](https://images.proteinatlas.org/19743/198_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/19743/198_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/20122/222_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/20122/222_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/20122/221_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/20122/221_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/20122/248_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/20122/248_H6_2_red_green.jpg)

### 深度机制分析

**结构域架构**：UBN2（Ubinuclein-2, 1347 aa / 146.1 kDa）的主要结构域注释为IPR014840（HRD domain, Hpc2-related domain）和IPR026947（UBN middle domain）。Pfam识别到PF08729（HUN domain, Hpc2-Ubinuclein）和PF14075（UBN_AB domain）。该蛋白的pLDDT=51.1（低置信度）——结构预测显示largely disordered protein with isolated folded domains, 反映其adaptor/scaffold protein性质。无实验PDB结构。PubMed=14（低文献量），但核心研究质量极高——UBN2 is essential for mouse development and functions in X chromosome inactivation (PMID:40455860)。Nucleoplasm定位为Enhanced confidence。

**PPI互作网络解读**：PPI network（degree=84）——STRING记录的高分互作partner包括HIRA（score=881, histone chaperone, H3.3 deposition）、CABIN1（score=872, calcineurin binding protein 1, HIRA complex subunit）、ASF1A（score=831, anti-silencing function 1A, histone H3-H4 chaperone）和ASF1B（score=793, ASF1 paralog）。BioGRID记录到EWSR1（Ewing sarcoma breakpoint region 1, FET family RNA-binding protein, transcriptional regulator）、CDX1（caudal type homeobox 1, transcription factor）、TFAP4（transcription factor AP-4）和TEAD2（TEA domain transcription factor 2, Hippo pathway effector）。该PPI网络清晰地将UBN2定位在histone H3.3 deposition pathway（HIRA-H3.3 chaperone complex）和transcription factor network的交叉点。

**结构解读**：UBN2的HRD domain (IPR014840) 是HIRA complex的core subunit signature——该domain shared with Hpc2 (yeast ortholog) and mediates histone chaperone activity。UBN_AB domain (PF14075) 为ubonuclein-specific conserved region——可能参与substrate recognition或complex stabilization。pLDDT=51.1和1347 aa的长度与scaffold protein的biophysical profile一致——large disordered regions serve as flexible platforms for multi-protein complex assembly, while folded domains (HRD, UBN_AB) provide specific molecular recognition interfaces。

**机制模型**：UBN2是目前机制最明确的nucleoplasm蛋白之一，其function可以总结为：(1) Histone H3.3 chaperoning axis——UBN2作为HIRA complex的core subunit，与HIRA/CABIN1/ASF1A协作deposit histone variant H3.3 into nucleosome-depleted regions——这是replication-independent chromatin assembly的主通路；(2) X chromosome inactivation axis——UBN2 essential for XCI in mouse development (PMID:40455860), 可能通过H3.3 deposition at the inactive X chromosome (Xi) 维持chromatin silencing；(3) Transcription regulation axis——UBN2与EWSR1/CDX1/TFAP4/TEAD2等transcription factor的互作提示其可能同时function as transcriptional co-regulator, recruiting HIRA-H3.3 deposition activity to specific genomic loci。

**TE调控展望**：UBN2的TE regulation潜力为中-高等级，基于其H3.3 chaperone function。TE调控关联性取决于：(1) HIRA complex-mediated H3.3 deposition may directly influence TE chromatin state——H3.3 enrichment at specific TE subfamilies (e.g., ERVK, young LINE-1) associated with transcriptional competence；(2) UBN2在X chromosome inactivation（XCI）中的作用可能与L1-mediated Xist spreading有关——LINE-1 elements serve as "way stations" for Xist RNA coating during XCI, and H3.3 deposition at Xi may modulate this process；(3) HIRA complex dysfunction has been linked to derepression of pericentromeric repeats in senescent cells。建议通过UBN2 ChIP-seq on H3.3-HA tagged lines确定HIRA-dependent H3.3 deposition at TE loci, 结合UBN2 knockdown/knockout条件下的TE RNA-seq确定哪些TE subfamilies are most affected by UBN2 loss, 以及proximity labeling (BioID)鉴定UBN2在核内的full interactome。

### PubMed

**Count: 21**

| PMID | Title |
|---|---|
| 40936337 | Identifying Gene Predictors of Chemicals Linked With Breast Cancer: A Machine Learning Analysis of MCF7 Cellular Transcriptomic Screening Data. |
| 40455860 | Ubinuclein 2 is essential for mouse development and functions in X chromosome inactivation. |
| 39509271 | HIRA protects telomeres against R-loop-induced instability in ALT cancer cells. |
| 37805161 | MiR-455-3p mediates PPARα through UBN2 to promote apoptosis and autophagy in acute myeloid leukemia cells. |
| 36978083 | Potential miRNA-gene interactions determining progression of various ATLL cancer subtypes after infection by HTLV-1 oncovirus. |


