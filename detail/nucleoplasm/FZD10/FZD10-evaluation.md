---
type: protein-evaluation
gene: "FZD10"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## FZD10 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FZD10 |
| 蛋白名称 | Frizzled-10 |
| 蛋白大小 | 581 aa / 65.3 kDa |
| UniProt ID | Q9ULW2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 581 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=93 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=80.6; PDB=2 |
| 调控结构域 | 4/10 | x2 | 8.0 | Frizzled/SFRP; Frizzled/Smoothened_7TM; Frizzled_dom |
| PPI | 6/10 | x3 | 18.0 | PPI degree=98 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=93 broad=149
- AF pLDDT=80.6 PDB=2
- InterPro: Frizzled/SFRP; Frizzled/Smoothened_7TM; Frizzled_dom
- Pfam: Frizzled; Fz
- PPI degree=98 ChIP: None
36764493: N6-Methyladenosine-Mediated Up-Regulation of FZD10 Regulates Liver Cancer Stem C | 38452403: Mechanic evaluation of Wu-Mei-Pill on colitis-associated colorectal cancer: An i | 31349740: FZD10 Carried by Exosomes Sustains Cancer Cell Proliferation.

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Frizzled-10

**功能**: Receptor for Wnt proteins. Functions in the canonical Wnt/beta-catenin signaling pathway (By similarity). The canonical Wnt/beta-catenin signaling pathway leads to the activation of disheveled proteins, inhibition of GSK-3 kinase, nuclear accumulation of beta-catenin and activation of Wnt target genes. A second signaling pathway involving PKC and calcium fluxes has been seen for some family members, but it is not yet clear if it represents a distinct pathway or if it can be integrated in the can

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR015526 |
| InterPro | IPR000539 |
| InterPro | IPR020067 |
| InterPro | IPR036790 |
| InterPro | IPR017981 |
| Pfam | PF01534 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RYK | STRING | 945 |
| WNT2B | STRING | 909 |
| GPC4 | STRING | 904 |
| WNT5A | STRING | 869 |
| DVL3 | STRING | 807 |
| DVL2 | STRING | 797 |
| HILPDA | STRING | 779 |
| CTNNB1 | STRING | 731 |



### 深度机制分析

FZD10（Frizzled-10，581 aa）是Wnt信号通路的7次跨膜受体，属于Frizzled家族。结构域包括Frizzled/SFRP结构域（IPR015526, PF01392）、Frizzled/Smoothened 7TM（IPR000539, PF01534 Fz）和Frizzled胞外CRD结构域（IPR020067, IPR036790），CRD负责Wnt配体结合。AF pLDDT=80.6，PDB=2，跨膜受体结构置信度良好。PPI网络（degree=98）形成经典的Wnt信号体：RYK（945，Wnt共受体）、WNT2B（909）、GPC4（904，共受体）、WNT5A（869）、DVL2/DVL3（797/807，核心信号转导）、CTNNB1/beta-catenin（731）。关键文献41672294报道砷暴露通过E2F2/FZD10轴诱导人正常乳腺上皮细胞干性（Food Chem Toxicol 2026），40958973开发针对FZD10的钇标记免疫放疗用于宫颈癌。Wnt/FZD10/beta-catenin信号通路是公认的转录激活通路——Wnt结合后经DVL抑制GSK-3beta，beta-catenin稳定化并核转位，与TCF/LEF转录因子协同激活靶基因。FZD10自身核定位为Approved，可能通过核内体循环或NLS介导的异位机制进入核内。核内FZD10片段或全蛋白可能直接与TCF/LEF和beta-catenin在染色质上形成复合物，在TE驱动的Wnt响应增强子处调控转录（Wnt通路在进化中与TE密切相关，许多Wnt响应增强子源自TE插入）。FZD10的核定位赋予其不依赖配体结合的核内信号潜能。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9ULW2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000111432-FZD10

![](https://images.proteinatlas.org/14484/2149_D9_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/14484/2149_D9_77_blue_red_green.jpg)
![](https://images.proteinatlas.org/14484/2151_D11_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/14484/2151_D11_20_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000111432-FZD10

![](https://images.proteinatlas.org/14484/2149_D9_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/14484/2149_D9_77_blue_red_green.jpg)
![](https://images.proteinatlas.org/14484/2151_D11_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/14484/2151_D11_20_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000111432-FZD10

![](https://images.proteinatlas.org/14484/2149_D9_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/14484/2149_D9_77_blue_red_green.jpg)
![](https://images.proteinatlas.org/14484/2151_D11_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/14484/2151_D11_20_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 149**

| 41672294 | Arsenic exposure induces stemness in human normal breast epithelial cells via the E2F2/FZD10 axis. | Food Chem Toxicol 2026 |
| 41223982 | Epigenetic mechanisms of PARP inhibitor resistance in ovarian cancer: A systematic review with bioinformatic analysis of | Crit Rev Oncol Hematol 2026 |
| 40958973 | Development of immune radiotherapy with yttrium by targeting Frizzled homologue 10 (FZD10) in cervical cancer. | Gynecol Oncol Rep 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/FZD10

