---
type: protein-evaluation
gene: "SNAPC5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## SNAPC5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SNAPC5 |
| 蛋白名称 | snRNA-activating protein complex subunit 5 |
| 蛋白大小 | 98 aa / 11.3 kDa |
| UniProt ID | O75971 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Supported) + ChIP |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 98 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=4 |
| 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=76.6; PDB=5 |
| 调控结构域 | 5/10 | ×2 | 10.0 | SNAPC5 |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=54 |
| **加权总分** | | | **143/180** | |
| **归一化总分** | | | **79.8/100** | 互证: +3 |

### 3. 分析
- HPA: Nucleoplasm (Supported)
- PubMed: strict=4, broad=8
- AF pLDDT: 76.6 / PDB: 5
- InterPro: SNAPC5
- Pfam: SNAPC5
- PPI degree=54 ChIP: Yes
39833228: Brain gliomas new transcriptomic discoveries from differentially expressed genes | 39747245: Structural insights into distinct mechanisms of RNA polymerase II and III recrui | 38312596: Long noncoding RNA lnc-SNAPC5-3:4 inhibits malignancy by directly upregulating m

### 4. 总体评价
★★★★  **79.8/100**  **nucleoplasm**
TE candidate: SNAPC5


### 补充分析 (UniProt API)

**蛋白全称**: snRNA-activating protein complex subunit 5

**功能**: Part of the SNAPc complex required for the transcription of both RNA polymerase II and III small-nuclear RNA genes. Binds to the proximal sequence element (PSE), a non-TATA-box basal promoter element common to these 2 types of genes. Recruits TBP and BRF2 to the U6 snRNA TATA box

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029138 |
| Pfam | PF15497 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SNAPC1 | STRING | 999 |
| SNAPC4 | STRING | 999 |
| SNAPC2 | STRING | 997 |
| GTF2B | STRING | 959 |
| TBP | STRING | 956 |
| GTF2A2 | STRING | 906 |
| GTF2A1 | STRING | 895 |
| BRF2 | STRING | 724 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-O75971-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000174446-SNAPC5

![](https://images.proteinatlas.org/24379/1139_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/24379/1139_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/24379/1291_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/24379/1291_B12_3_red_green.jpg)
![](https://images.proteinatlas.org/24379/1132_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/24379/1132_B1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 8**

| 39833228 | Brain gliomas new transcriptomic discoveries from differentially expressed genes to therapeutic targets. | Sci Rep 2025 |
| 39747245 | Structural insights into distinct mechanisms of RNA polymerase II and III recruitment to snRNA promoters. | Nat Commun 2025 |
| 38312596 | Long noncoding RNA lnc-SNAPC5-3:4 inhibits malignancy by directly upregulating miR-224-3p in non-small cell lung cancer. | Heliyon 2024 |

### 深度机制分析

SNAPC5是snRNA激活蛋白复合体（SNAPc）的核心组分之一，其唯一的SNAPC5结构域（IPR029138/PF15497）高度特化，不存在于SNAPc之外的其他蛋白家族中。该蛋白仅98个氨基酸（11.3 kDa），属于超小型衔接亚基，但其在整个SNAPc复合体中的结构角色至关重要——作为SNAPc与Pol II/Pol III通用转录机器之间的分子桥梁。AF2预测pLDDT为76.6分，相对较低，这与其在游离态下可能存在的本质无序区一致，只有在结合SNAPC1/SNAPC4等伴侣蛋白后才获得稳定构象。5个PDB条目提供了复合体状态下的结构约束，2025年Nature Communications发表的结构研究（PMID: 39747245）更是直接揭示了Pol II与Pol III被差异性招募至snRNA启动子的分子机制——SNAPC5极有可能是这种差异化招募的关键决定因子。

PPI网络展现了SNAPC5的卓越连接性：与SNAPC1（999）、SNAPC4（999）、SNAPC2（997）形成的核心四元交联几乎不可分离，说明SNAPc是一个高度稳定的预组装复合体，而非动态组装的转录因子。更值得注意的是，SNAPC5与通用转录因子GTF2B（959）、TBP（956）、GTF2A2（906）、GTF2A1（895）以及Pol III特异性因子BRF2（724）的广泛互作，凸显了其作为"通用转录机器招募平台"的核心地位。这种独特的双重特异性——同时介导Pol II（U1/U2 snRNA）和Pol III（U6 snRNA）转录机器的启动子锚定——在真核转录因子中是极为罕见的，提示SNAPC5可能是一个深度保守的转录调控枢纽。

该蛋白在临床转化方面的前景引人注目：2024年Heliyon研究（PMID: 38312596）揭示lnc-SNAPC5-3:4通过上调miR-224-3p抑制非小细胞肺癌的恶性进展，暗示SNAPC5的表达水平可通过lncRNA进行精细调控；2025年Scientific Reports（PMID: 39833228）将SNAPC5列为脑胶质瘤的关键差异表达基因。鉴于SNAPc通过调控snRNA转录间接影响全基因组pre-mRNA剪接效率，SNAPC5的异常表达或突变理论上可能通过干扰剪接体snRNA（U1、U2、U4、U5、U6）的稳态水平，产生广泛且多样的剪接异常——这是多种癌症和神经发育疾病的共同分子特征。因此，SNAPC5代表了一类"转录上部调控因子"（upstream transcription regulator），其病理意义远超其蛋白大小所暗示的重要性，值得作为剪接相关疾病的新型治疗靶点进行深入验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SNAPC5

