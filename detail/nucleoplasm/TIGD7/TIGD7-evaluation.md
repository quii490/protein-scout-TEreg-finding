---
type: protein-evaluation
gene: "TIGD7"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## TIGD7 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TIGD7 |
| 蛋白名称 | Tigger transposable element-derived protein 7 |
| 蛋白大小 | 549 aa / 63.2 kDa |
| UniProt ID | Q6NT04 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | nan (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 549 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=5 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=71.9; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=9 |
| **加权总分** | | | **133/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +2 |

### 3. 分析
- HPA: nan (Supported)
- PubMed: strict=5, broad=6
- AF pLDDT: 71.9 / PDB: 0
- InterPro: CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf
- Pfam: CENP-B_N; DDE_1; HTH_Tnp_Tc5
- PPI degree: 9 / ChIP: None
**Papers**: 23289938: Genomic signatures of a global fitness index in a multi-ethnic cohort of women. | 36265781: A more novel and robust gene signature predicts outcome in patients with esophag | 15487591: Isolation and characterization of a Jerky and JRK/JH8 like gene, tigger transpos

### 4. 总体评价
★★★★  **73.8/100**  |  **nucleoplasm**
**TE candidate**: CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf


### 补充分析 (UniProt API)

**蛋白全称**: Tigger transposable element-derived protein 7

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050863 |
| InterPro | IPR004875 |
| InterPro | IPR009057 |
| InterPro | IPR006600 |
| InterPro | IPR007889 |
| Pfam | PF04218 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FBP1 | BioGRID | 1 |
| HSPA8 | BioGRID | 1 |
| GAPDH | BioGRID | 1 |
| EIF4E | BioGRID | 1 |
| CYP17A1 | BioGRID | 0 |
| RAB3IL1 | BioGRID | 0 |
| UACA | BioGRID | 0 |
| PRMT8 | BioGRID | 0 |


### 深度机制分析

TIGD7属于Tigger转座子衍生蛋白家族（CenT-Element_Derived; Pfam: CENP-B_N），是DNA转座子在哺乳动物基因组中的"驯化"残余。其结构域架构揭示了TE来源的分子化石特征：N端CENP-B型DNA结合域（IPR004875/DDE_1）与C端整合酶/转座酶相关结构域（HTH_Tnp_Tc5; Homeodomain-like_sf）的组合表明其起源于Mariner/Tc1超家族的DNA转座子。HPA证据支持核定位（Nucleoplasm Supported），与TE衍生蛋白作为基因组调控因子的功能假说一致。蛋白大小549 aa / 63.2 kDa暗示其保留了相当完整的祖先转座酶架构，而非高度降解的TE碎片。

从进化驯化（domestication）视角看，CENP-B蛋白家族（包括CENP-B本身及其旁系同源物）在哺乳动物中已被招募为着丝粒功能和转录调控因子。TIGD7的CENP-B_N结构域保留了序列特异性DNA结合表面，可能识别TE来源的着丝粒重复序列或散布的Tigger家族TE残留（~2800个人类基因组拷贝）。AlphaFold pLDDT仅71.9，PDB=0，表明该蛋白可能含有柔性区域——这符合许多TE衍生蛋白的特征，其结构可塑性允许其"探索"新的功能空间。

PPI网络揭示了TIGD7与代谢和翻译关键蛋白（FBP1、GAPDH、EIF4E）的互作（BioGRID评分1），以及与表观遗传修饰酶PRMT8的潜在关联。虽然ChIP和直接靶标TE数据缺失，但其Homeodomain-like折叠和DDE内切核酸酶超家族关联暗示TIGD7可能在核质中扮演"分子考古学家"的角色——识别、结合并可能切割或重塑TE来源的DNA元件，从而参与基因组稳定性和TE抑制。5篇PubMed使其成为极端新颖靶标（10/10新颖性），其作为人类基因组中稀有的"活化石"转座子衍生蛋白，具有独特的DE>TEG>DNA相互作用模式的发现潜力。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6NT04-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000140993-TIGD7

![](https://images.proteinatlas.org/41357/539_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/539_A7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/552_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/552_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/534_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/534_A7_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000140993-TIGD7

![](https://images.proteinatlas.org/41357/539_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/539_A7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/552_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/552_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/534_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/534_A7_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000140993-TIGD7

![](https://images.proteinatlas.org/41357/539_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/539_A7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/552_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/552_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/534_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41357/534_A7_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 6**

| 41521457 | Tobacco Smoke Exposure From Prenatal To Adolescent Periods Drives IBD Pathogenesis: Dynamic DNA Methylation Signatures A | Adv Sci (Weinh) 2026 |
| 38618725 | Exploration of Diagnostic Markers Associated with Inflammation in Chronic Kidney Disease Based on WGCNA and Machine Lear | Crit Rev Immunol 2024 |
| 36265781 | A more novel and robust gene signature predicts outcome in patients with esophageal squamous cell carcinoma. | Clin Res Hepatol Gastroenterol 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TIGD7

