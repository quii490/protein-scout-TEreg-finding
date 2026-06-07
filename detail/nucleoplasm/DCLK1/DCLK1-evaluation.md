---
type: protein-evaluation
gene: "DCLK1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DCLK1 — REJECTED (研究热度过高 (PubMed strict=225，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCLK1 / DCAMKL1, DCDC3A, KIAA0369 |
| 蛋白名称 | Serine/threonine-protein kinase DCLK1 |
| 蛋白大小 | 740 aa / 82.2 kDa |
| UniProt ID | O15075 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 740 aa / 82.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=225 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.2; PDB: 1MFW, 1MG4, 1UF0, 5JZJ, 5JZN, 6KYQ, 6KYR |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003533, IPR036572, IPR011009, IPR000719, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.0/180** | |
| **归一化总分** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 225 |
| PubMed broad count | 537 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DCAMKL1, DCDC3A, KIAA0369 |

**关键文献**:
1. Macrophage DCLK1 promotes atherosclerosis via binding to IKKβ and inducing inflammatory responses.. *EMBO molecular medicine*. PMID: 36896602
2. Nerve Growth Factor Promotes Gastric Tumorigenesis through Aberrant Cholinergic Signaling.. *Cancer cell*. PMID: 27989802
3. Recent advances in drug delivery systems for targeting cancer stem cells.. *Acta pharmaceutica Sinica. B*. PMID: 33532180
4. Molecular Subtyping of Triple-Negative Breast Cancers by Immunohistochemistry: Molecular Basis and Clinical Relevance.. *The oncologist*. PMID: 32406563
5. A nasal cell atlas reveals heterogeneity of tuft cells and their role in directing olfactory stem cell proliferation.. *Science immunology*. PMID: 38306414

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 32.2% |
| 置信残基 (pLDDT 70-90) 占比 | 30.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 29.6% |
| 有序区域 (pLDDT>70) 占比 | 63.1% |
| 可用 PDB 条目 | 1MFW, 1MG4, 1UF0, 5JZJ, 5JZN, 6KYQ, 6KYR, 7F3G, 7KX6, 7KX8 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1MFW, 1MG4, 1UF0, 5JZJ, 5JZN, 6KYQ, 6KYR, 7F3G, 7KX6, 7KX8）+ AlphaFold极高置信度预测（pLDDT=72.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003533, IPR036572, IPR011009, IPR000719, IPR017441; Pfam: PF03607, PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCX | 0.886 | 0.849 | — |
| NBEA | 0.816 | 0.000 | — |
| CALML3 | 0.775 | 0.129 | — |
| MAB21L1 | 0.775 | 0.000 | — |
| CALML6 | 0.774 | 0.129 | — |
| CALML4 | 0.774 | 0.129 | — |
| CALML5 | 0.773 | 0.129 | — |
| CALM3 | 0.772 | 0.129 | — |
| TRPM5 | 0.727 | 0.000 | — |
| LGR5 | 0.718 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| homer | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EBI-2930353 | psi-mi:"MI:0405"(competition binding) | imex:IM-15127|pubmed:20832753 |
| MYC | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| Atp6v1a | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:22707207|imex:IM-17710 |
| Mycbp2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| RASAL2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CBY1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 1MFW, 1MG4, 1UF0, 5JZJ, 5JZN,  | pLDDT=72.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DCLK1 — Serine/threonine-protein kinase DCLK1，研究基础较多，新颖性有限。
2. 蛋白大小740 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 225 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 225 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15075
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133083-DCLK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCLK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15075
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000133083-DCLK1/subcellular

![](https://images.proteinatlas.org/15040/1637_D7_13_cr57b31e51349b7_red_green.jpg)
![](https://images.proteinatlas.org/15040/1637_D7_2_cr57b31e49907cb_red_green.jpg)
![](https://images.proteinatlas.org/15040/1774_E1_3_cr5950fdc0b939d_red_green.jpg)
![](https://images.proteinatlas.org/15040/1774_E1_9_cr5950fdc0b968e_red_green.jpg)
![](https://images.proteinatlas.org/15040/1786_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/15040/1786_E3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15075-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15075 |
| SMART | SM00537;SM00220; |
| UniProt Domain [FT] | DOMAIN 57..143; /note="Doublecortin 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00072"; DOMAIN 186..269; /note="Doublecortin 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00072"; DOMAIN 390..647; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR003533;IPR036572;IPR011009;IPR000719;IPR017441;IPR008271; |
| Pfam | PF03607;PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000133083-DCLK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DCTN1 | Biogrid | false |
| DCX | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
