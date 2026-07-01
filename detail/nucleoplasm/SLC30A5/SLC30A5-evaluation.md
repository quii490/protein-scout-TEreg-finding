---
type: protein-evaluation
gene: "SLC30A5"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC30A5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC30A5 |
| 蛋白名称 | Proton-coupled zinc antiporter SLC30A5 |
| 蛋白大小 | 765 aa / 84.0 kDa |
| UniProt ID | Q8TAD4 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Golgi apparatus; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 765 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=23 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=76.2; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Cation_efflux; Cation_efflux_TM; Cation_efflux_TMD_sf |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=141 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +2 |

### 3. 分析
- Golgi apparatus; Nucleoplasm (Supported)
- PubMed strict=23 broad=62
- AF pLDDT=76.2 PDB=0
- InterPro: Cation_efflux; Cation_efflux_TM; Cation_efflux_TMD_sf
- Pfam: Cation_efflux
- PPI degree=141 ChIP: None
19021537: Mechanisms of mammalian zinc-regulated gene expression. | 15070437: Intestinal and placental zinc transport pathways. | 39006068: Integrated pan-cancer genomic analysis reveals the role of SLC30A5 in the prolif

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Proton-coupled zinc antiporter SLC30A5

**功能**: Together with SLC30A6 forms a functional proton-coupled zinc ion antiporter mediating zinc entry into the lumen of organelles along the secretory pathway (PubMed:11904301, PubMed:15525635, PubMed:15994300, PubMed:19366695, PubMed:22529353). By contributing to zinc ion homeostasis within the early secretory pathway, regulates the activation and folding of enzymes like alkaline phosphatases and enzymes involved in phosphatidylinositol glycan anchor biosynthesis (PubMed:15525635, PubMed:15994300, P

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002524 |
| InterPro | IPR058533 |
| InterPro | IPR027469 |
| InterPro | IPR045316 |
| Pfam | PF01545 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SLC30A9 | STRING | 868 |
| SLC39A7 | STRING | 859 |
| ELAVL1 | BioGRID | 1 |
| SRSF1 | BioGRID | 1 |
| HNRNPD | BioGRID | 1 |
| TCTN3 | BioGRID | 1 |
| SPPL2B | BioGRID | 1 |
| CD70 | BioGRID | 1 |


### 深度机制分析

SLC30A5编码质子偶联锌转运蛋白（也称为ZNT5），属于阳离子外排家族（Cation_efflux; Pfam: PF01545），与SLC30A6协同介导锌离子向分泌途径细胞器腔内的转运（PMID:11904301, PMID:15525635）。虽然其经典功能定位为高尔基体膜蛋白，但HPA显示其同时具有核质信号（Nucleoplasm Supported, 核定位特异性8/10），提示SLC30A5可能在核周或核内高尔基体相关膜结构上发挥锌稳态调控功能。蛋白质大小适中（765 aa / 84.0 kDa），AlphaFold预测pLDDT为76.2，跨膜区域的构象预测置信度相对较低，可能影响核定位机制的解释。

值得注意的是，SLC30A5拥有相对丰富的PPI网络（PPI degree=141），其中与多种核RNA结合蛋白存在互作，包括ELAVL1/HuR、SRSF1/HNRNPD等（BioGRID评分1）。ELAVL1是ARE介导的mRNA稳定性调控的关键核蛋白，其活性依赖于锌离子环境，SLC30A5可能通过局部锌浓度调节影响这些RNA结合蛋白的构象与功能。与STRING来源的高分伙伴SLC30A9（score=868）和SLC39A7（score=859）的互作则表明其参与锌转运蛋白网络（zinc transport network）的协同调控，可能在核膜与内质网-高尔基体中间区室间的锌信号传导中扮演关键角色。

从机制模型角度，SLC30A5在核质中的存在可能解释为：该蛋白通过其跨膜结构域锚定于核膜内层或核内高尔基体相关膜系统，利用质子梯度驱动锌离子注入核质局部微环境，从而调控依赖于锌指的泛素连接酶活性或转录因子（如核受体ESR1）的功能。近期研究揭示SLC30A亚家族在ESR1配体非依赖性激活中的作用（PMID:41790496），进一步支持这一假说。鉴于SLC30A5仅有23篇PubMed文献且无实验结构（PDB=0），其核内功能的验证需要结合锌离子成像、APEX邻近标记及核内锌指蛋白活性的高通量分析。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8TAD4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000145740-SLC30A5

![](https://images.proteinatlas.org/35373/413_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/35373/413_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/35373/420_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/35373/420_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/35373/417_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/35373/417_D1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 62**

| 41790496 | SLC30A1, SLC30A5, and SLC30A9 transporters play crucial role in ligand-independent activation of ESR1 signalling in brea | Metallomics 2026 |
| 41153455 | Computational Identification of Genetic Background of Infertility and Calculating Inbreeding Coefficient in Dromedary Ca | Genes (Basel) 2025 |
| 40385401 | Testing for Causal Association between Serum Urate, Gout, and Prostatic Cancer in European Males. | medRxiv 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC30A5

