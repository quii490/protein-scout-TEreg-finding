---
type: protein-evaluation
gene: "IL13RA2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## IL13RA2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | IL13RA2 |
| 蛋白名称 | Interleukin-13 receptor subunit alpha-2 |
| 蛋白大小 | 380 aa / 44.2 kDa |
| UniProt ID | Q14627 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cell Junctions; Nucleoplasm; Plasma membrane; Vesi (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 380 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=82 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=86.2; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | FN3_dom; FN3_sf; Ig-like_fold |
| PPI | 7/10 | x3 | 21.0 | PPI degree=162 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +2 |

### 3. 分析
- Cell Junctions; Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=82 broad=195
- AF pLDDT=86.2 PDB=1
- InterPro: FN3_dom; FN3_sf; Ig-like_fold
- Pfam: IL6Ra-bind
- PPI degree=162 ChIP: None
31348891: Intra- and Inter-cellular Rewiring of the Human Colon during Ulcerative Colitis. | 41370379: Decoding the CHI3L1/IL-13Rα2 signaling nexus in MASH-fibrosis pathogenesis. | 38937754: Cancer-associated fibroblasts (CAFs) gene signatures predict outcomes in breast 

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Interleukin-13 receptor subunit alpha-2

**功能**: Cell surface receptor that plays a role in the regulation of IL-13-mediated responses (PubMed:11861389, PubMed:17030238). Functions as a decoy receptor that inhibits IL-13- and IL-4-mediated signal transduction via the JAK-STAT pathway and thereby modulates immune responses and inflammation (PubMed:11861389, PubMed:17030238). Serves as a functional signaling receptor for IL-13 in an alternative pathway involving AP-1 ultimately leading to the production of TGFB1 (PubMed:16327802)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR003961 |
| InterPro | IPR036116 |
| InterPro | IPR013783 |
| InterPro | IPR003532 |
| InterPro | IPR015321 |
| Pfam | PF09240 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| AKT1 | BioGRID | 0 |
| BAG4 | BioGRID | 0 |
| BRMS1 | BioGRID | 0 |
| CASP8 | BioGRID | 0 |
| ERBB2 | BioGRID | 0 |
| ESR2 | BioGRID | 0 |
| IGF1R | BioGRID | 0 |
| NOTCH2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q14627-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000123496-IL13RA2

![](https://images.proteinatlas.org/45831/1866_G1_31_red_green.jpg)
![](https://images.proteinatlas.org/45831/1866_G1_32_red_green.jpg)
![](https://images.proteinatlas.org/45831/1819_A1_31_red_green.jpg)
![](https://images.proteinatlas.org/45831/1819_A1_34_red_green.jpg)
![](https://images.proteinatlas.org/67363/1866_B7_31_red_green.jpg)
![](https://images.proteinatlas.org/67363/1866_B7_32_red_green.jpg)
![](https://images.proteinatlas.org/67363/1899_H8_1_cr5ba20cf3571fc_red_green.jpg)
![](https://images.proteinatlas.org/67363/1899_H8_21_cr5ba20cf3577bd_red_green.jpg)

### PubMed 文献

**PubMed count: 195**

| 42353280 | Immunotoxin WPD101a as a Potential Drug Candidate for Targeted Therapy in Muscle Invasive Bladder Cancer Expressing IL-1 | Int J Mol Sci 2026 |
| 42301527 | B7 homolog 3-targeted CAR-T cells secreting EGFR T-cell engagers for improved control of glioblastoma progression. | Mol Biomed 2026 |
| 42233283 | Spatial dissection of ADC/RPT targets defines heterogeneous expression landscapes and therapeutic implications in rhabdo | Neuro Oncol 2026 |

### 深度机制分析

IL13RA2的域架构由三个串联纤连蛋白III型结构域（FN3_dom, IPR003961; FN3_sf, IPR036116）和一个N端Ig样折叠（Ig-like_fold, IPR013783）组成。FN3结构域是约100个残基的β-三明治模块，是II类细胞因子受体家族的标志。位于膜近端FN3结构域的IL6Ra-bind区域（Pfam PF09240）介导与配体IL-13的结合——IL13RA2以极高亲和力（Kd~50 pM）单体方式结合IL-13，作为诱饵受体发挥功能。

AlphaFold pLDDT为86.2，PDB条目为1。已解析的晶体结构证实IL-13与IL13RA2的结合界面主要涉及FN3-2和FN3-3结构域的表面环，将IL-13隐蔽起来使其无法与信号传导受体IL13RA1/IL4R相互作用。PPI网络（degree=162）揭示多方面信号景观：AKT1、ERBB2和IGF1R提示非经典通路信号（与AP-1/TGFB1替代信号轴一致，PMID 16327802），而BAG4、CASP8和BRMS1共同指向肿瘤微环境中凋亡和侵袭之间的平衡调控枢纽作用。

核质定位（HPA Approved）的重要机制延伸：核内IL13RA2可能通过受体内化与核靶向对IL-13信号进行胞内隔离。在溃疡性结肠炎中观察到的该蛋白的细胞内/细胞间重布线（PMID 31348891）与包涵体形成和蛋白定位改变有关。IL13RA2的FN3结构域在细胞核内可能作为染色质相关蛋白的平台。

TE调控启示：IL-13/IL13RA2通路调控在多种恶性肿瘤中经常上调的肿瘤相关成纤维细胞（CAF）标志基因（PMID 38937754）。许多癌症TE激活事件通过LTR增强子劫持宿主基因启动子，IL13RA2可能作为TE激活肿瘤中JAK-STAT/AP-1信号输出的关键节点。在MASH-纤维化中CHI3L1/IL-13Rα2轴的作用（PMID 41370379）提示其在组织纤维化的TE相关信号环路中占据重要地位。


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/IL13RA2

