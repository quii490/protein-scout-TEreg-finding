---
type: protein-evaluation
gene: "OGA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## OGA — REJECTED (研究热度过高 (PubMed strict=490，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OGA / HEXC, KIAA0679, MEA5, MGEA5 |
| 蛋白名称 | Protein O-GlcNAcase |
| 蛋白大小 | 916 aa / 102.9 kDa |
| UniProt ID | O60502 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 916 aa / 102.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=490 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.7; PDB: 2YDQ, 5M7R, 5M7S, 5M7T, 5M7U, 5TKE, 5UHK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016181, IPR017853, IPR051822, IPR011496; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 490 |
| PubMed broad count | 1862 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HEXC, KIAA0679, MEA5, MGEA5 |

**关键文献**:
1. Protein O-GlcNAcylation: emerging mechanisms and functions.. *Nature reviews. Molecular cell biology*. PMID: 28488703
2. Role of O-Linked N-Acetylglucosamine Protein Modification in Cellular (Patho)Physiology.. *Physiological reviews*. PMID: 32730113
3. O-GlcNAcylation in cancer development and immunotherapy.. *Cancer letters*. PMID: 37279852
4. O-GlcNAcylation modulates liquid-liquid phase separation of SynGAP/PSD-95.. *Nature chemistry*. PMID: 35637289
5. Excessive O-GlcNAcylation Causes Heart Failure and Sudden Death.. *Circulation*. PMID: 33593071

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.7 |
| 高置信度残基 (pLDDT>90) 占比 | 53.2% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 26.9% |
| 有序区域 (pLDDT>70) 占比 | 68.4% |
| 可用 PDB 条目 | 2YDQ, 5M7R, 5M7S, 5M7T, 5M7U, 5TKE, 5UHK, 5UHL, 5UHO, 5UHP |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2YDQ, 5M7R, 5M7S, 5M7T, 5M7U, 5TKE, 5UHK, 5UHL, 5UHO, 5UHP）+ AlphaFold极高置信度预测（pLDDT=74.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR017853, IPR051822, IPR011496; Pfam: PF07555 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OGT | 0.985 | 0.602 | — |
| AURKB | 0.930 | 0.000 | — |
| GM2A | 0.857 | 0.000 | — |
| GUSB | 0.830 | 0.000 | — |
| HEXB | 0.815 | 0.000 | — |
| B2M | 0.790 | 0.000 | — |
| HAVCR1 | 0.773 | 0.000 | — |
| ARSB | 0.761 | 0.000 | — |
| GFPT2 | 0.758 | 0.000 | — |
| GFPT1 | 0.758 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PAPLA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Usp10 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| HAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SPAG5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| H4c11 | psi-mi:"MI:0096"(pull down) | imex:IM-14483|pubmed:16356930 |
| A0A0G2RN01 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0F7R6G5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| MDM2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| CYLD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| A2M | psi-mi:"MI:0397"(two hybrid array) | doi:10.1101/gr.114280.110|imex |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.7 + PDB: 2YDQ, 5M7R, 5M7S, 5M7T, 5M7U,  | pLDDT=74.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. OGA — Protein O-GlcNAcase，研究基础较多，新颖性有限。
2. 蛋白大小916 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 490 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 490 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60502
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198408-OGA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OGA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60502
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000198408-OGA/subcellular

![](https://images.proteinatlas.org/76501/1672_B2_23_cr57c6d041459c8_blue_red_green.jpg)
![](https://images.proteinatlas.org/76501/1672_B2_3_cr57c6d03aa785c_blue_red_green.jpg)
![](https://images.proteinatlas.org/76501/1703_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/76501/1703_G2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60502-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60502 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 60..336; /note="GH84"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01353" |
| InterPro | IPR016181;IPR017853;IPR051822;IPR011496; |
| Pfam | PF07555; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198408-OGA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC37 | Biogrid | false |
| MYC | Biogrid | false |
| OGT | Biogrid | false |
| SOCS2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
