---
type: protein-evaluation
gene: "TMEM126A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM126A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM126A |
| 蛋白名称 | Transmembrane protein 126A |
| 蛋白大小 | 195 aa / 21.5 kDa |
| UniProt ID | Q9H061 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 195 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=18 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=90.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | TMEM126 |
| PPI | 6/10 | x3 | 18.0 | PPI degree=99 |
| **加权总分** | | | **135/180** | |
| **归一化总分** | | | **74.9/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=18 broad=22
- AF pLDDT=90.0 PDB=0
- InterPro: TMEM126
- Pfam: TMEM126
- PPI degree=99 ChIP: None
38199007: Identification of TMEM126A as OXA1L-interacting protein reveals cotranslational  | 36317462: The top 10 most frequently involved genes in hereditary optic neuropathies in 21 | 33879611: Optic atrophy-associated TMEM126A is an assembly factor for the ND4-module of mi

### 4. 总体评价
**74.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 126A

**功能**: Protein required for the cotranslational protein quality control in the inner membrane of the mitochondria (PubMed:38199007). Associates with newly synthesized polypeptides and may act as a chaperone that cooperates with OXA1L for the insertion of newly synthesized mitochondrial proteins into the inner membrane (PubMed:38199007). Required for the assembly of the ND4 module of mitochondrial complex I (PubMed:33879611, PubMed:33882309)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009801 |
| Pfam | PF07114 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

### 深度机制分析

TMEM126A（Transmembrane protein 126A）是一个功能上属于线粒体蛋白质量控制和复合体I组装因子的蛋白，但其HPA免疫荧光定位显示Cytosol; Nucleoplasm (Approved)，颠覆了其作为纯线粒体蛋白的认知。195个氨基酸（21.5 kDa）的小分子量和pLDDT=90.0的极高结构置信度使其成为结构生物学研究的理想候选。唯一的InterPro/Pfam结构域为TMEM126（IPR009801 / PF07114），这是一个功能定义尚不清晰的结构域家族，但AlphaFold的高pLDDT表明该结构域折叠良好。

TMEM126A的线粒体功能已在多个研究中被充分阐述。该蛋白是OXA1L插入酶的互作伙伴（PMID 38199007），在线粒体内膜上参与新合成蛋白的共翻译质量控制——作为分子伴侣协助OXA1L将新合成蛋白插入内膜。同时，TMEM126A是线粒体复合体I的ND4模块组装所必需的（PMID 33879611, PMID 33882309），其突变与遗传性视神经萎缩相关（PMID 36317462, 2021）。然而，核质定位的发现对TMEM126A功能模型提出了重要挑战：为什么一个线粒体膜蛋白装配因子会出现在核质中？

PPI网络揭示了极具启发性的连接。STRING数据库显示OPA3（932分）是最高置信度的互作伙伴——OPA3同样是一个线粒体蛋白，突变导致3-甲基戊烯二酸尿症和视神经萎缩。然而，BioGRID数据提示了核功能的线索：EWSR1（Ewing肉瘤RNA结合蛋白）、SRSF2和SRSF3（丝氨酸/精氨酸富集剪接因子）、CDK4（细胞周期激酶）和CSNK2A2（酪蛋白激酶2亚基）均为核内蛋白。特别是SRSF2和SRSF3作为mRNA剪接调控因子，与TMEM126A的互作暗示线粒体蛋白质量控制状态可通过核内RNA加工反馈回路进行交流——这可能是线粒体-核逆行信号（mitochondrial retrograde signaling）的新机制。

从TE调控角度，TMEM126A的核定位可能通过以下途径间接影响TE元件：（1）线粒体功能障碍触发的逆行信号可导致表观遗传重编程和重复序列去抑制，TMEM126A可能在此信号通路中作为中间环节；（2）与SRSF2/SRSF3的互作可能影响TE衍生转录本的剪接——许多TE元件作为可变外显子被纳入宿主基因转录本。PPI degree=99的高互作度提示该蛋白位于多种细胞通路的交汇点。建议通过线粒体应激诱导实验结合TMEM126A的ChIP-seq和RNA免疫共沉淀来解析其核内功能。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| OPA3 | STRING | 932 |
| EWSR1 | BioGRID | 1 |
| SRSF2 | BioGRID | 1 |
| SRSF3 | BioGRID | 1 |
| CDK4 | BioGRID | 1 |
| CSNK2A2 | BioGRID | 1 |
| BAG3 | BioGRID | 1 |
| ZWINT | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H061-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000171202-TMEM126A

![](https://images.proteinatlas.org/46648/747_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/46648/747_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/46648/714_C4_3_red_green.jpg)
![](https://images.proteinatlas.org/46648/714_C4_4_red_green.jpg)
![](https://images.proteinatlas.org/46648/713_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/46648/713_C4_2_red_green.jpg)

### PubMed 文献

**PubMed count: 22**

| 41154849 | Genome-Wide Association Study Revealed Candidate Genes Associated with Litter Size, Weight, and Body Size Traits in Tian | Biology (Basel) 2025 |
| 39644219 | Integrative Molecular Dynamics Simulations Untangle Cross-Linking Data to Unveil Mitochondrial Protein Distributions. | Angew Chem Int Ed Engl 2025 |
| 39006949 | A hot and cold tumor‑related prognostic signature for stage II colorectal cancer. | Oncol Lett 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM126A

