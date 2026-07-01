---
type: protein-evaluation
gene: "F8A3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## F8A3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | F8A3 |
| 蛋白名称 | 40-kDa huntingtin-associated protein |
| 蛋白大小 | 371 aa / 39.1 kDa |
| UniProt ID | P23610 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 371 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=4 |
| 三维结构 | 9/10 | x3 | 27.0 | pLDDT=77.5; PDB=10 |
| 调控结构域 | 4/10 | x2 | 8.0 | F8A; TPR-like_helical_dom_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=3 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=4 broad=4
- AF pLDDT=77.5 PDB=10
- InterPro: F8A; TPR-like_helical_dom_sf
- Pfam: 
- PPI degree=3 ChIP: None
26089202: Regulation of SPRY3 by X chromosome and PAR2-linked promoters in an autism susce | 11593511: PCR assay for the inversion causing severe Hemophilia A and its application. | 34745201: Development and Validation of a Five-RNA-Based Signature and Identification of C

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

F8A3是40-kDa亨廷顿蛋白相关蛋白（HAP40），属于F8A基因家族（F8A1/F8A2/F8A3），371个氨基酸的蛋白骨架以F8A保守结构域（IPR039494）和TPR-like helical domain超折叠（IPR011990）为特征。TPR（三十四肽重复）类结构域通常形成右手超螺旋，介导蛋白-蛋白互作——这与F8A3作为RAB5A效应分子的功能完全一致。AlphaFold预测pLDDT为77.5，配合10个PDB条目（晶体/冷冻电镜），F8A3拥有本批次中最好的结构表征之一。然而HPA核定位为"nan"（核定位特异性5/10），提示其在核质中的存在可能尚未被免疫荧光染色有效捕捉。

F8A3的核心功能为早期内体的囊泡运输调控：通过作为RAB5A效应分子被招募至早期内体膜，HTT-F8A1/F8A2/F8A3-RAB5A复合体刺激早期内体与肌动蛋白丝（actin filaments）的相互作用，同时抑制微管结合——从而降低内体沿微管的远距离运动性（PMID:16476778）。这种"内体锚定"机制确保内体在特定胞内区域进行有效分选。TPR-like超螺旋结构域可能介导F8A3与HTT N端的直接结合——HTT含有多聚谷氨酰胺（polyQ）重复，其在亨廷顿病（HD）中的异常扩展可能破坏F8A3介导的内体动力学。

PPI网络（degree=3但高度特异性）进一步强化了内体运输框架：与HTT（STRING=947）和F8A2/F8A1（STRING=801/434）的互作反映F8A家族的冗余性与组合性；而与ANKRD24（STRING=420）的互作则提供了未被探索的功能线索——含锚蛋白重复的蛋白通常作为大分子复合体的支架。F8A3所在Xq28区域的SPRY3启动子调控与自闭症易感性相关（PMID:26089202），暗示该基因组区域的染色质环境可能受表观遗传精细调控。

从TE调控角度审视，F8A3虽并非典型核蛋白，但其与HTT的紧密功能性耦合使其间接涉及HD病理中著名的转录失调现象。突变HTT导致转录因子隔离（sequestration）和染色质结构异常——F8A3作为HTT结合蛋白可能增强或减弱这一效应。F8A家族在神经母细胞瘤中被列入预后相关基因特征（PMID:34745201），但核内功能的探索完全空白。建议将F8A3视为HTT内体复合体的"核伴侣"进行功能解析——内体信号传导（endosomal signaling）正成为核转录调控的新前沿。

**蛋白全称**: 40-kDa huntingtin-associated protein

**功能**: RAB5A effector molecule that is involved in vesicular trafficking of early endosomes (PubMed:16476778). Mediates the recruitment of HTT by RAB5A onto early endosomes. The HTT-F8A1/F8A2/F8A3-RAB5A complex stimulates early endosomal interaction with actin filaments and inhibits interaction with microtubules, leading to the reduction of endosome motility (PubMed:16476778)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR039494 |
| InterPro | IPR011990 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-P23610-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 4**

| 38027357 | Comprehensive Transcriptomic Investigation of Rett Syndrome Reveals Increasing Complexity Trends from Induced Pluripoten | ACS Omega 2023 |
| 34745201 | Development and Validation of a Five-RNA-Based Signature and Identification of Candidate Drugs for Neuroblastoma. | Front Genet 2021 |
| 26089202 | Regulation of SPRY3 by X chromosome and PAR2-linked promoters in an autism susceptibility region. | Hum Mol Genet 2015 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/F8A3

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HTT | STRING | 947 |
| F8A2 | STRING | 801 |
| ANKRD24 | STRING | 420 |
| F8A3 | STRING | 418 |
| F8A1 | STRING | 434 |

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HTT | STRING | 947 |
| F8A2 | STRING | 801 |
| ANKRD24 | STRING | 420 |
| F8A3 | STRING | 418 |
| F8A1 | STRING | 434 |

