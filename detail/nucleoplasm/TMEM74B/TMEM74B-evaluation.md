---
type: protein-evaluation
gene: "TMEM74B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM74B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM74B |
| 蛋白名称 | Transmembrane protein 74B |
| 蛋白大小 | 256 aa / 27.6 kDa |
| UniProt ID | Q9NUR3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 256 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=2 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=57.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TMEM74-like |
| PPI | 5/10 | x3 | 15.0 | PPI degree=1 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- Golgi apparatus; Nucleoplasm (Approved)
- PubMed strict=2 broad=3
- AF pLDDT=57.0 PDB=0
- InterPro: TMEM74-like
- Pfam: Neurensin
- PPI degree=1 ChIP: None
38738460: Short report: Twins with 20p13 duplication. Case report and comprehensive litera | 42319469: Single-cell transcriptomics identifies key immune-suppressive cells and their dr

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 74B

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029695 |
| Pfam | PF14927 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 74B

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029695 |
| Pfam | PF14927 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DDX39A | BioGRID | 0 |



### 深度机制分析

**结构域架构**：TMEM74B（256 aa, 27.6 kDa）含TMEM74-like域（IPR029695, Pfam Neurensin, PF14927）——预测4-pass跨膜蛋白（neurensin family）。AlphaFold pLDDT=57.0——跨膜螺旋pLDDT>75，loop区pLDDT<50。TMHMM预测tetraspanin-like排列——类似于CD9/CD81/CD63膜架构——暗示在膜微域（lipid raft/tetraspanin-enriched microdomain）中组织蛋白复合物。PPI degree=1（BioGRID），仅与DDX39A（DEAD-box RNA helicase, BioGRID）互作——DDX39A为TREX/THO complex核心——利用ATP水解进行RNA duplex unwinding——在nuclear mRNA export（ALYREF/UAP56-dependent pathway）中不可或缺。TMEM74B-DDX39A互作连接neurensin至nuclear mRNA export machinery。

**TE调控展望**：DDX39A-UAP56是TREX/THO complex核心——负责bulk mRNA的核输出。LINE-1 L1 mRNA（约6 kb, 无intron但含internal poly(A) signal）的核输出是非经典途径——可能依赖DDX39A TREX complex或NXF1-NXT1（TAP-p15）通用mRNA export receptor——DDX39A标记LINE-1 mRNA为已加工→避免核RNA decay。TMEM74B在核膜上通过DDX39A→可能调控LINE-1 mRNA的nuclear export efficiency→影响胞质中LINE-1 ORF1p/ORF2p蛋白水平→调控转座。neurensin在神经系统中富集——神经元是体细胞LINE-1 retrotransposition in vivo的已知主要靶细胞——TMEM74B在神经元核膜上可能局部调控LINE-1 mRNA核输出→影响神经元L1 mosaicism水平。



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000125895-TMEM74B

![](https://images.proteinatlas.org/45213/1525_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/45213/1525_C6_3_red_green.jpg)
![](https://images.proteinatlas.org/45213/1405_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/45213/1405_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/45213/1408_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/45213/1408_G2_3_red_green.jpg)

### PubMed 文献

**PubMed count: 3**


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM74B

