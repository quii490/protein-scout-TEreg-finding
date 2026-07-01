---
type: protein-evaluation
gene: "PPIH"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PPIH 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PPIH |
| 蛋白名称 | Peptidyl-prolyl cis-trans isomerase H |
| 蛋白大小 | 177 aa / 19.2 kDa |
| UniProt ID | O43447 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 177 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=27 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=96.3; PDB=11 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Cyclophilin-like_dom_sf; Cyclophilin-type_PPIase; Cyclophilin-type_PPIase_CS |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=149 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | nan (nan) |
| PubMed | strict=27, broad=49 |
| AF pLDDT | 96.3 |
| PDB | 11 |
| InterPro | Cyclophilin-like_dom_sf; Cyclophilin-type_PPIase; Cyclophilin-type_PPIase_CS |
| Pfam | Pro_isomerase |
| PPI degree | 149 |
| ChIP | None |

**Papers**: 40895540: eQTL and multi-omics integration reveal PPIH as a prognostic and immunotherapeut | 37874737: PPIH gene regulation system and its prognostic significance in hepatocellular ca | 28935721: The spliceosomal proteins PPIH and PRPF4 exhibit bi-partite binding.

### 4. 总体评价
★★★★  **72.7/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Peptidyl-prolyl cis-trans isomerase H

**功能**: PPIase that catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and may therefore assist protein folding (PubMed:20676357). Participates in pre-mRNA splicing. May play a role in the assembly of the U4/U5/U6 tri-snRNP complex, one of the building blocks of the spliceosome. May act as a chaperone

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029000 |
| InterPro | IPR024936 |
| InterPro | IPR020892 |
| InterPro | IPR002130 |
| Pfam | PF00160 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| USP15 | BioGRID | 0 |
| USP4 | BioGRID | 0 |
| PRPF4 | BioGRID | 0 |
| SART3 | BioGRID | 0 |
| MEPCE | BioGRID | 0 |
| UBC | BioGRID | 0 |
| CUL3 | BioGRID | 0 |
| NHP2L1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O43447-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 49**

| 41675755 | Identification of disulfidptosis-related genes in immunity and immunotherapy in diabetic foot ulcer. | Ann Med Surg (Lond) 2026 |
| 41435608 | Polyphyllin I mitigates psoriasiform inflammation and prevents relapse by modulating CLEC7A and inhibiting pyroptosis. | Phytomedicine 2026 |
| 40895540 | eQTL and multi-omics integration reveal PPIH as a prognostic and immunotherapeutic biomarker. | Front Immunol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PPIH


### 深度机制分析

PPIH（Peptidyl-prolyl cis-trans isomerase H）属于亲环蛋白（Cyclophilin）超家族，其结构由Cyclophilin-type PPIase催化结构域（InterPro:IPR020892, IPR024936）和Cyclophilin-like domain superfamily折叠（IPR029000）构成。Pfam注释为Pro_isomerase（PF00160），确认了其肽基脯氨酰顺反异构酶活性——催化寡肽中脯氨酸亚胺肽键的cis-trans异构化，辅助蛋白质折叠（PubMed:20676357）。AlphaFold预测结构质量极高，全局pLDDT=96.3，意味着整个177个氨基酸的蛋白几乎全部以高置信度折叠。PDB现有11个实验结构条目，为结构导向的功能研究提供了坚实基础。

从蛋白互作网络来看，PPIH拥有149个PPI互作伙伴，其中与剪接体组分的互作最为核心。BioGRID记录显示PPIH与PRPF4（U4/U6 snRNP相关蛋白）、SART3（U4/U5/U6 tri-snRNP组装因子）、NHP2L1（U4/U5/U6 tri-snRNP组分）以及USP4/USP15（去泛素化酶）形成核心互作模块。PPIH-PRPF4的绑合已被证实为双向性（bipartite binding, PMID:28935721），这一定向作用于U4/U5/U6 tri-snRNP的组装过程。在tri-snRNP中，PPIH可能作为分子伴侣，通过PPIase活性催化剪接体蛋白的脯氨酸异构化，驱动构象转变。

PPIH的功能定位集中在pre-mRNA剪接过程。其作为剪接体U4/U5/U6 tri-snRNP的一个重要"建筑模块"（building block），参与剪接体组装的早期阶段。eQTL与多组学整合分析（PMID:40895540）揭示PPIH可作为肝细胞癌的预后和免疫治疗生物标志物，其基因调控系统的功能紊乱与肿瘤免疫微环境相关。另一项研究（PMID:37874737）在肝癌中进一步证实了PPIH的预后意义。

核定位证据方面，PPIH在HPA中缺乏明确的亚细胞定位信号（报告标注为nan）。UniProt注释也未提供直接的核定位实验证据。尽管其功能定位（剪接体）强烈暗示核质定位，但这一推断缺乏独立的HPA IF验证。作为剪接体效应因子的分子伴侣角色是其最核心的机制——PPIH利用PPIase活性催化剪接体蛋白构象重排，间接参与pre-mRNA加工的调控，但其直接参与TE调控的潜力极低。PPIH在HCC等多癌种免疫治疗中的生物标志物价值是独立的临床转化方向。



