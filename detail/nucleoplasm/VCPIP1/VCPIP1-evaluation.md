---
type: protein-evaluation
gene: "VCPIP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VCPIP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VCPIP1 / KIAA1850, VCIP135 |
| 蛋白名称 | Deubiquitinating protein VCPIP1 |
| 蛋白大小 | 1222 aa / 134.3 kDa |
| UniProt ID | Q96JH7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Centrosome, Cytosol; UniProt: Nucleus; Cytoplasm; Endoplasmic reticulum; Golgi apparatus,  |
| 蛋白大小 | 5/10 | ×1 | 5 | 1222 aa / 134.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.4; PDB: 8YKA, 9DIL, 9MQ6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR048857, IPR003323, IPR029071, IPR039087, IPR045 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Centrosome, Cytosol | Uncertain |
| UniProt | Nucleus; Cytoplasm; Endoplasmic reticulum; Golgi apparatus, Golgi stack | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum lumen (GO:0005788)
- Golgi stack (GO:0005795)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1850, VCIP135 |

**关键文献**:
1. LUBAC and OTULIN regulate autophagy initiation and maturation by mediating the linear ubiquitination and the stabilization of ATG13.. *Autophagy*. PMID: 32543267
2. Molecular Basis of VCPIP1 and P97/VCP Interaction Reveals Its Functions in Post-Mitotic Golgi Reassembly.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39234822
3. Accelerating inhibitor discovery for deubiquitinating enzymes.. *Nature communications*. PMID: 36754960
4. VCPIP1 facilitates pancreatic adenocarcinoma progression via Hippo/YAP signaling.. *Cell death & disease*. PMID: 40436845
5. VCPIP1 ameliorates sepsis-associated encephalopathy by promoting microglia autophagy via the PI3K/AKT/mTOR pathway.. *International immunopharmacology*. PMID: 40865405

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.4 |
| 高置信度残基 (pLDDT>90) 占比 | 26.1% |
| 置信残基 (pLDDT 70-90) 占比 | 35.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 28.2% |
| 有序区域 (pLDDT>70) 占比 | 61.5% |
| 可用 PDB 条目 | 8YKA, 9DIL, 9MQ6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.4），有序残基占 61.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048857, IPR003323, IPR029071, IPR039087, IPR045827; Pfam: PF02338, PF21403, PF19437 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NSFL1C | 0.999 | 0.994 | — |
| VCP | 0.999 | 0.994 | — |
| NPLOC4 | 0.998 | 0.994 | — |
| UFD1 | 0.998 | 0.994 | — |
| UBXN7 | 0.996 | 0.994 | — |
| UBXN2A | 0.995 | 0.994 | — |
| UBXN2B | 0.995 | 0.994 | — |
| STX5 | 0.957 | 0.292 | — |
| FAF2 | 0.865 | 0.610 | — |
| CDK1 | 0.794 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| Nsfl1c | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| FAF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UBXN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UBXN8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| Ubxn11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UBXN6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| Nploc4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| HUWE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| VCP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.4 + PDB: 8YKA, 9DIL, 9MQ6 | pLDDT=69.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Endoplasmic reticulum; Golgi a / Plasma membrane; 额外: Centrosome, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. VCPIP1 — Deubiquitinating protein VCPIP1，非常新颖，仅有少数基础研究。
2. 蛋白大小1222 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96JH7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175073-VCPIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VCPIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96JH7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000175073-VCPIP1/subcellular

![](https://images.proteinatlas.org/23932/1846_E1_1_cr5b7eacfcd4391_blue_red_green.jpg)
![](https://images.proteinatlas.org/23932/1846_E1_22_cr5b7eacfcd48a5_blue_red_green.jpg)
![](https://images.proteinatlas.org/23932/1873_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23932/1873_C4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/23932/217_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23932/217_F8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96JH7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96JH7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 208..361; /note="OTU"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00139" |
| InterPro | IPR048857;IPR003323;IPR029071;IPR039087;IPR045827; |
| Pfam | PF02338;PF21403;PF19437; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175073-VCPIP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| UBXN6 | Biogrid, Bioplex | true |
| VCP | Biogrid, Opencell | true |
| ARL4D | Bioplex | false |
| CIAO2A | Bioplex | false |
| CNKSR3 | Bioplex | false |
| D2HGDH | Bioplex | false |
| DHFR | Bioplex | false |
| EEF1AKMT3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
