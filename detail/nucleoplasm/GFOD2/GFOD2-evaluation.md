---
type: protein-evaluation
gene: "GFOD2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GFOD2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GFOD2 |
| 蛋白名称 | Glucose-fructose oxidoreductase domain-containing protein 2 |
| 蛋白大小 | 385 aa / 42.3 kDa |
| UniProt ID | Q3B7J2 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm (Uncertain) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 385 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=4 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=92.0; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Gfo/Idh/MocA-like_OxRdtase_N; Gfo/Idh/MocA_oxidrdct_glycsds; GFO_IDH_MocA-like_d |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=10 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Uncertain)
- PubMed strict=4 broad=7
- AF pLDDT=92.0 PDB=0
- InterPro: Gfo/Idh/MocA-like_OxRdtase_N; Gfo/Idh/MocA_oxidrdct_glycsds; GFO_IDH_MocA-like_dom
- Pfam: GFO_IDH_MocA; GFO_IDH_MocA_C3
- PPI degree=10 ChIP: None
32197942: Distribution of transcripts of the GFOD gene family members gfod1 and gfod2 in t | 25260659: Omental adipose tissue gene expression, gene variants, branched-chain amino acid | 24064143: Effect of a GFOD2 variant on responses in total and LDL cholesterol in Mexican s

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Glucose-fructose oxidoreductase domain-containing protein 2

**功能**: Promotes matrix assembly

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000683 |
| InterPro | IPR050463 |
| InterPro | IPR055170 |
| InterPro | IPR036291 |
| Pfam | PF01408 |
| Pfam | PF22725 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TGDS | STRING | 739 |
| TRIM25 | BioGRID | 1 |
| GFOD1 | BioGRID | 0 |
| NKIRAS2 | BioGRID | 0 |
| TXLNA | BioGRID | 0 |
| IFITM1 | BioGRID | 0 |
| DPP4 | BioGRID | 0 |
| RHOQ | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q3B7J2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000141098-GFOD2

![](https://images.proteinatlas.org/40939/2268_F9_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/40939/2268_F9_65_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000141098-GFOD2

![](https://images.proteinatlas.org/40939/2268_F9_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/40939/2268_F9_65_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000141098-GFOD2

![](https://images.proteinatlas.org/40939/2268_F9_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/40939/2268_F9_65_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 7**

| 41142807 | Integrated bioinformatics and molecular docking analysis reveal potential hub genes and targeted therapeutics in sepsis- | Front Immunol 2025 |
| 38946427 | Molecular insight into the potential functional role of pseudoenzyme GFOD1 via interaction with NKIRAS2. | Acta Biochim Biophys Sin (Shanghai) 2024 |
| 35477560 | Effects of stressful life-events on DNA methylation in panic disorder and major depressive disorder. | Clin Epigenetics 2022 |

### 深度机制分析

GFOD2（385 aa, 42.3 kDa）属于GFO/IDH/MocA氧化还原酶超家族，其结构域架构由N端的GFO/IDH/MocA样氧化还原酶结构域（IPR000683）和C端的辅助折叠区域（GFO_IDH_MocA_C3, PF22725）组成。该家族以葡萄糖-果糖氧化还原酶（GFOR）为原型，催化NADPH依赖的氧化还原反应。AlphaFold预测pLDDT高达92.0，为该25个候选蛋白中预测质量最高者之一，提示该蛋白折叠紧凑、有序程度高——这对于潜在的酶活性口袋结构解析极为有利。然而，无PDB实验结构验证，底物特异性和催化机制仍属推测。

GFOD2的已知功能是促进基质组装（matrix assembly），但具体生化机制未明。GOF/IDH/MocA家族的酶活性通常涉及糖类底物的氧化或异构化，因此GFOD2可能作为胞外基质修饰酶或胶原交联调控因子发挥作用。PPI网络（BioGRID degree=10）中，与TGDS（TDP-葡萄糖4,6-脱水酶，STRING评分739）和GFOD1（同家族蛋白）的互作提示存在代谢通路协作；与TRIM25（E3泛素连接酶）和NKIRAS2（NF-kappaB信号抑制因子）的互作则暗示GFOD2与炎症和先天免疫通路可能有非催化的蛋白-蛋白互作功能。

HPA将GFOD2定位为Cytosol; Nucleoplasm（Uncertain级别），定位可靠性低于Approved和Supported。这种模糊定位可能反映该蛋白在胞质和核质之间呈动态分布，也可能是细胞类型特异性的。IFITM1（干扰素诱导跨膜蛋白1）和DPP4（二肽基肽酶4）在PPI网络中的存在加强了GFOD2与炎症/代谢交叉调控的关联。

在TE调控语境下，GFOD2的氧化还原酶活性若延伸至核质，则可能通过以下方式影响TE表达：调控核内NADPH/NADP+平衡→影响组蛋白去甲基化酶（如LSD1，依赖FAD）和TET蛋白（依赖α-KG和Fe2+）的活性→改变TE位点的DNA甲基化和组蛋白修饰状态。氧化还原代谢与表观基因组的偶联是新兴领域。PMID:25260659报道的GFOD2变异与支链氨基酸代谢的关联，以及PMID:35477560提示的应激生活事件通过DNA甲基化调控GFOD2，为"代谢→表观遗传→TE"轴提供了线索。建议通过代谢组学联合CUT&Tag实验，验证GFOD2敲低是否改变全局和TE位点的表观遗传标记。

