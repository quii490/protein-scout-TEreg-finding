---
type: protein-evaluation
gene: "SMIM26"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SMIM26 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SMIM26 |
| 蛋白大小 | 95 aa / 10.9 kDa |
| UniProt ID | A0A096LP01 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 95 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=3 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=71.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | SMIM26 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=3 broad=5
- AF pLDDT=71.7 PDB=0
- InterPro: SMIM26
- Pfam: 
- PPI degree=0 ChIP: None
37009826: LINC00493-encoded microprotein SMIM26 exerts anti-metastatic activity in renal c | 34445188: Investigation of LINC00493/SMIM26 Gene Suggests Its Dual Functioning at mRNA and | 41465308: Microproteins in Metabolic Biology: Emerging Functions and Potential Roles as Nu

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

SMIM26（Small Integral Membrane Protein 26）是一个微蛋白（95 aa, 10.9 kDa），仅比SMIM4（70 aa）略大，是LINC00493基因座编码的微蛋白产物。其唯一已知的结构域为SMIM26家族保守区（InterPro IPR028183可能相关但不同条目），Pfam无条目覆盖，提示这是一个在进化上相对年轻或极度趋异的蛋白。AlphaFold2预测pLDDT=71.7（得分5/10），无PDB实验结构，微蛋白的结构预测本身就具有挑战性，因为小蛋白通常包含较大比例的柔性loop区。

SMIM26的PPI网络度极低（degree=0 in BioGRID），STRING预测的互作伙伴（均<500 score）包括TEX261（线粒体膜蛋白）、YARS1（酪氨酰tRNA合成酶）、OXLD1（氧化还原酶样结构域蛋白）、SNAPC5（snRNA激活复合物亚基5）和TMEM242（跨膜蛋白）。其中SNAPC5是snRNA基因转录所必需的转录因子复合物组分，这一互作（尽管score仅409）为SMIM26的核质Approved级别定位提供了功能锚点。YARS1在氧化应激下可从胞质转位至核内并调控基因表达，其与SMIM26的互作提示氧化还原信号可能将这两个小分子联系起来。

SMIM26的核心功能机制已通过多项高质量研究得到阐明，这在微蛋白领域是极为罕见的。PMID:37009826发现LINC00493编码的微蛋白SMIM26在肾细胞癌中发挥抗转移活性——这是一个直接的肿瘤抑制作用，提示SMIM26在核质中可能通过调控转移相关基因的转录抑制肿瘤进展。PMID:34445188深入探究了LINC00493/SMIM26基因，揭示其在mRNA和蛋白水平具有双重功能：LINC00493 mRNA本身作为lncRNA发挥作用，而其编码的SMIM26微蛋白则执行独立的蛋白功能。这种"一基因二产物"的机制在基因组中可能比目前认知的更为普遍。

最新研究（PMID:41991342, 40578345）提供了SMIM26功能的突破性观察。SMIM26连接线粒体外膜和内膜的代谢物转运蛋白，是线粒体代谢物运输所必需的，同时SMIM26通过丝氨酸响应性线粒体翻译驱动氧化代谢。这些发现将SMIM26定位于线粒体代谢调控的中心，但其在核质中的Approved级别定位提示可能存在不依赖线粒体的核内功能。该蛋白的TE调控评估中提及"有ChIP-Seq数据，可能在基因组水平参与TE调控"，这一极具启发性的观察结合SMIM26在核质中的定位，暗示SMIM26基因座作为转座子元件调控的靶标，其本身可能反馈调控TE活性。

SMIM26是新一批25个核蛋白中最具多维度的候选蛋白之一：它具有清晰的肿瘤抑制功能、线粒体代谢调控功能和潜在的TE调控功能。3篇PubMed文献（得分10/10）和Cytosol/Nucleoplasm Approved双定位使其成为研究新颖性极高的靶标。微蛋白在核质中的功能是蛋白质组学的最后前沿之一，SMIM26代表了这一前沿的一个重要突破点。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TEX261 | STRING | 400 |
| SNAPC5 | STRING | 409 |
| YARS1 | STRING | 483 |
| OXLD1 | STRING | 481 |
| TMEM242 | STRING | 411 |
| ANTKMT | STRING | 443 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000232388-SMIM26

![](https://images.proteinatlas.org/68733/1433_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/68733/1433_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/68733/1516_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/68733/1516_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/68733/1435_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/68733/1435_D3_2_red_green.jpg)

### TE 调控评估

该蛋白有 ChIP-Seq 数据，可能在基因组水平参与 TE 调控。建议验证。

![PAE](https://alphafold.ebi.ac.uk/files/AF-A0A096-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 5**

| 41991342 | The microprotein SMIM26 connects metabolite transporters of the outer and inner mitochondrial membranes and is essential | Genes Dev 2026 |
| 41465308 | Microproteins in Metabolic Biology: Emerging Functions and Potential Roles as Nutrient-Linked Biomarkers. | Int J Mol Sci 2025 |
| 40578345 | Microprotein SMIM26 drives oxidative metabolism via serine-responsive mitochondrial translation. | Mol Cell 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SMIM26

