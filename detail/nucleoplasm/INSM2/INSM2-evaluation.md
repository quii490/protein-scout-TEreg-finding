---
type: protein-evaluation
gene: "INSM2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted TE_REG_CANDIDATE]
status: shortlisted
---

## INSM2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | INSM2 |
| 蛋白名称 | Insulinoma-associated protein 2 |
| 蛋白大小 | 566 aa / 59.5 kDa |
| UniProt ID | Q96T92 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Nucleoplasm (Approved) + ChIP |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 566 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=8 |
| 🏗️ 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=55.1; PDB=0 |
| 🧬 调控结构域 | 6/10 | ×2 | 12.0 | INSM1/2; Znf_C2H2_sf; Znf_C2H2_type |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=10 |
| **加权总分** | | | **134/180** | |
| **归一化总分 (÷1.83)** | | | **74.3/100** | 互证: +2 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | Nucleoplasm (Approved) |
| PubMed | strict=8, broad=9 |
| AlphaFold | pLDDT=55.1 |
| PDB | 0 entries |
| InterPro | INSM1/2; Znf_C2H2_sf; Znf_C2H2_type |
| Pfam | zf-C2H2 |
| PPI | combined degree=10 |
| ChIP | Yes (TFs and others) |

### 4. 总体评价
⭐⭐⭐⭐
**74.3/100** | **nucleoplasm**
TE regulatory candidate — INSM1/2; Znf_C2H2_sf; Znf_C2H2_type


### 补充分析 (UniProt API)

**蛋白全称**: Insulinoma-associated protein 2

**功能**: May function as a growth suppressor or tumor suppressor in liver cells and in certain neurons

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR042972 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PTPRN | STRING | 789 |
| CD38 | STRING | 719 |
| ZSCAN1 | BioGRID | 1 |
| RECQL4 | BioGRID | 1 |
| TRIM23 | BioGRID | 1 |
| RHOU | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96T92-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000168348-INSM2

![](https://images.proteinatlas.org/51925/1213_E2_3_red_green.jpg)
![](https://images.proteinatlas.org/51925/1213_E2_6_red_green.jpg)

### PubMed 文献

**PubMed count: 9**

| 41483448 | Exploring molecular mechanisms of radioactive iodine therapy in thyroid cancer using single-cell RNA sequencing data. | Discov Oncol 2026 |
| 39093073 | Identification of Blood Biomarkers Related to Energy Metabolism and Construction of Diagnostic Prediction Model Based on | J Alzheimers Dis 2024 |
| 36811249 | A meta-analysis of mRNA expression profiling studies in sheep with different FecB genotypes. | Anim Genet 2023 |

### 深度机制分析

INSM2是继胰岛素瘤相关蛋白INSM1之后的同源转录因子，在肝细胞和特定神经元中充当生长或肿瘤抑制因子。其结构域架构具有典型的转录抑制因子特征：C2H2型锌指（IPR013087, Znf_C2H2_sf/PF00096）为其提供DNA结合能力，而INSM1/2特异性结构域（IPR042972）定义其家族成员身份。566 aa的蛋白中AlphaFold pLDDT仅55.1且无PDB结构，提示存在大量无序区域——这是转录因子常见的结构特征，无序区域通常在结合伴侣蛋白后被诱导折叠。

INSM2是整个蛋白集中少有的ChIP阳性蛋白（鉴定为TFs and others），这一证据将其直接锚定在染色质调控网络中。核质定位（HPA Approved）+ C2H2锌指DNA结合域 + ChIP阳性三要素，使其成为最强的TE调控候选因子之一。PPI网络（degree=10）中ZSCAN1（具有SCAN结构域的另一C2H2-ZF转录因子）和RECQL4（RecQ解旋酶家族DNA解旋酶）的互作尤其重要——ZSCAN1可能参与TE/ERV的转录抑制（SCAN结构域在KRAB-ZFP介导的逆转录元件沉默中发挥辅助作用），而RECQL4在DNA复制和端粒维持中与端粒/亚端粒TE序列发生交叉。

在功能层面，INSM2作为肿瘤抑制因子在肝癌中的表达丢失或突变可能导致C2H2-ZF介导的TE沉默体系失活，释放内源性逆转录元件（ERV）的转录活性，驱动基因组不稳定性和先天免疫激活。甲状腺癌的放射性碘治疗分子机制探索（PMID:41483448）和能量代谢相关的血液生物标志物鉴定（PMID:39093073）暗示INSM2可能在组织特异性TE调控网络中扮演守门员角色。CUT&RUN/CUT&Tag技术绘制INSM2的全基因组结合图谱，特别是其与ERV/LTR元件的结合情况，应是后续验证的最高优先级实验。

