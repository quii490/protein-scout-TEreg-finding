---
type: protein-evaluation
gene: "KRBOX1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## KRBOX1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KRBOX1 |
| 蛋白名称 | KRAB domain-containing protein 1 |
| 蛋白大小 | 128 aa / 14.9 kDa |
| UniProt ID | C9JBD0 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 128 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=4 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=66.9; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | KRAB; KRAB_dom_sf; Krueppel_C2H2_ZnF |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=4 broad=4
- AF pLDDT=66.9 PDB=0
- InterPro: KRAB; KRAB_dom_sf; Krueppel_C2H2_ZnF
- Pfam: KRAB
- PPI degree=0 ChIP: None
33015181: Comprehensive Analysis of Differential Immunocyte Infiltration and Potential ceR | 34204705: In Silico Identification of miRNA-lncRNA Interactions in Male Reproductive Disor | 28593875: Intrauterine growth restriction and placental gene expression in severe preeclam

### 4. 总体评价
**73.8/100** | **nucleoplasm**
TE candidate: KRAB; KRAB_dom_sf; Krueppel_C2H2_ZnF


### 补充分析 (UniProt API)

**蛋白全称**: KRAB domain-containing protein 1

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001909 |
| InterPro | IPR036051 |
| InterPro | IPR050169 |
| Pfam | PF01352 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-C9JBD0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000240747-KRBOX1

![](https://images.proteinatlas.org/46901/1331_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/46901/1331_B2_3_red_green.jpg)
![](https://images.proteinatlas.org/46901/1830_F1_61_red_green.jpg)
![](https://images.proteinatlas.org/46901/1830_F1_63_red_green.jpg)

### PubMed 文献

**PubMed count: 4**

| 34204705 | In Silico Identification of miRNA-lncRNA Interactions in Male Reproductive Disorder Associated with COVID-19 Infection. | Cells 2021 |
| 33015181 | Comprehensive Analysis of Differential Immunocyte Infiltration and Potential ceRNA Networks Involved in the Development  | Biomed Res Int 2020 |
| 28721901 | PSMB8 as a Candidate Marker of Responsiveness to Preoperative Radiation Therapy in Rectal Cancer Patients. | Int J Radiat Oncol Biol Phys 2017 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KRBOX1

### 深度机制分析

KRBOX1是目前已知最小的KRAB锌指超家族成员之一（128 aa / 14.9 kDa），其结构域架构包含经典的KRAB（Krueppel-associated box）抑制结构域（InterPro: IPR001909; Pfam: PF01352）和Krueppel C2H2锌指基序（KRAB_dom_sf; Krueppel_C2H2_ZnF）。KRAB结构域是KRAB-ZNF蛋白的核心功能模块，通过招募KAP1/TRIM28-SETDB1复合物催化H3K9me3沉积，建立可遗传的异染色质状态，从而沉默内源性逆转录元件（ERVs）和其他TE序列。HPA验证KRBOX1的核质定位（Nucleoplasm Approved, 核定位特异性9/10）与这一表观遗传沉默功能高度一致。

尽管KRBOX1含有TE调控的核心结构域且被标记为"TE_REG_CANDIDATE"，其蛋白大小极不寻常——全长仅128 aa，远小于典型KRAB-ZNF蛋白（通常400-800 aa），可能仅包含单个C2H2锌指。这意味着其DNA识别能力极为有限（每个锌指识别约3bp），暗示KRBOX1可能不具备独立序列特异性DNA结合能力，而是作为KRAB-ZNF沉默复合物的辅助因子或"迷你适配器"发挥作用：通过KRAB结构域桥接KAP1-SETDB1复合物，而通过其有限的C2H2锌指识别TE共有基序或通过蛋白-蛋白相互作用靶向特定基因组位点。

AlphaFold预测pLDDT仅66.9，PDB=0，且蛋白尺寸限制了折叠熵，提示其可能部分为无序结构。PPI网络显示其仅与3个蛋白互作（MPP6、RFLNB、KRTAP19-4，均来自STRING，无BioGRID验证），缺乏与KAP1的已知互作记录（但KRAB-KAP1互作是结构保守的，可能在STRING中未被捕获）。PubMed仅4篇使其成为极端新颖的候选靶标。从机制上，KRBOX1可能是哺乳动物基因组的"轻量级"TE防御哨兵——通过最小化的KRAB-C2H2组合提供基础水平的TE转录沉默，补充或协同大型KRAB-ZNF蛋白的全基因组TE监视网络。解析其靶标TE家族及与KAP1的结合亲和力是验证这一假说的关键。



### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MPP6 | STRING | 437 |
| RFLNB | STRING | 418 |
| KRTAP19-4 | STRING | 692 |

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MPP6 | STRING | 437 |
| RFLNB | STRING | 418 |
| KRTAP19-4 | STRING | 692 |

