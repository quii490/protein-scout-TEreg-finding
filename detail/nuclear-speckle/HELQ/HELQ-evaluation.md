---
type: protein-evaluation
gene: "HELQ"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HELQ 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HELQ / HEL308 |
| 蛋白名称 | Helicase POLQ-like |
| 蛋白大小 | 1101 aa / 124.1 kDa |
| UniProt ID | Q8TDG4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; 额外: Nucleoplasm; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 1101 aa / 124.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011545, IPR050474, IPR014001, IPR001650, IPR046 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- site of DNA damage (GO:0090734)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 71 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HEL308 |

**关键文献**:
1. HELQ is a dual-function DSB repair enzyme modulated by RPA and RAD51.. *Nature*. PMID: 34937945
2. HELQ as a DNA helicase: Its novel role in normal cell function and tumorigenesis (Review).. *Oncology reports*. PMID: 37921071
3. Helicase HELQ: Molecular Characters Fit for DSB Repair Function.. *International journal of molecular sciences*. PMID: 39201320
4. HELQ and EGR3 expression correlate with IGHV mutation status and prognosis in chronic lymphocytic leukemia.. *Journal of translational medicine*. PMID: 33485349
5. HELQ Maintains Genome Stability of Primordial Germ Cells by Inhibiting LINE-1 Expression.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 40542648

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.9 |
| 高置信度残基 (pLDDT>90) 占比 | 51.3% |
| 置信残基 (pLDDT 70-90) 占比 | 19.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 25.4% |
| 有序区域 (pLDDT>70) 占比 | 71.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.9，有序区 71.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011545, IPR050474, IPR014001, IPR001650, IPR046931; Pfam: PF00270, PF00271, PF20470 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POLN | 0.993 | 0.294 | — |
| POLA1 | 0.926 | 0.066 | — |
| RAD51C | 0.750 | 0.342 | — |
| RAD51 | 0.723 | 0.142 | — |
| FANCD2 | 0.698 | 0.342 | — |
| SRSF1 | 0.636 | 0.000 | — |
| RAD51B | 0.635 | 0.354 | — |
| MCM9 | 0.635 | 0.000 | — |
| FANCI | 0.618 | 0.292 | — |
| RAD51D | 0.610 | 0.354 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| fbaB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENST00000295488 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.9 + PDB: 无 | pLDDT=73.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nuclear speckles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HELQ — Helicase POLQ-like，非常新颖，仅有少数基础研究。
2. 蛋白大小1101 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TDG4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163312-HELQ/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HELQ
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TDG4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000163312-HELQ/subcellular

![](https://images.proteinatlas.org/36852/1070_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/36852/1070_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/36852/1076_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/36852/1076_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/36852/1177_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/36852/1177_E6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TDG4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TDG4 |
| SMART | SM00487;SM00490; |
| UniProt Domain [FT] | DOMAIN 346..518; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 566..758; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR011545;IPR050474;IPR014001;IPR001650;IPR046931;IPR027417;IPR048960;IPR036390; |
| Pfam | PF00270;PF00271;PF20470;PF21099; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163312-HELQ/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RAD51C | Intact, Biogrid | true |
| ATR | Biogrid | false |
| FANCD2 | Biogrid | false |
| RAD51B | Biogrid | false |
| RPA1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
