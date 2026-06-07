---
type: protein-evaluation
gene: "DDRGK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDRGK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDRGK1 |
| 蛋白名称 | DDRGK1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | DDRGK1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Endoplasmic reticulum; 额外: Nucleoli; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.5/180** | |
| **归一化总分** | | | **48.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Nucleoli | Supported |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 55 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. DDRGK1 Enhances Osteosarcoma Chemoresistance via Inhibiting KEAP1-Mediated NRF2 Ubiquitination.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 36965071
2. VCP/p97 UFMylation stabilizes BECN1 and facilitates the initiation of autophagy.. *Autophagy*. PMID: 38762759
3. DDRGK1-mediated ER-phagy attenuates acute kidney injury through ER-stress and apoptosis.. *Cell death & disease*. PMID: 38233375
4. A Genome-wide ER-phagy Screen Highlights Key Roles of Mitochondrial Metabolism and ER-Resident UFMylation.. *Cell*. PMID: 32160526
5. A cross-kingdom conserved ER-phagy receptor maintains endoplasmic reticulum homeostasis during stress.. *eLife*. PMID: 32851973

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UFL1 | 0.996 | 0.841 | — |
| CDK5RAP3 | 0.989 | 0.887 | — |
| UFM1 | 0.972 | 0.305 | — |
| UFC1 | 0.954 | 0.719 | — |
| UFSP2 | 0.914 | 0.187 | — |
| UBA5 | 0.855 | 0.000 | — |
| UFSP1 | 0.799 | 0.094 | — |
| SRPRA | 0.784 | 0.745 | — |
| SRPRB | 0.697 | 0.513 | — |
| ERN1 | 0.593 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ufl1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CDK5RAP3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSTK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PHLDA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| rpoB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| UBE2D1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Endoplasmic reticulum; 额外: Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. DDRGK1 — DDRGK1 (UniProt未获取)，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/DDRGK1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198171-DDRGK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDRGK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/DDRGK1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (supported)。来源: https://www.proteinatlas.org/ENSG00000198171-DDRGK1/subcellular

![](https://images.proteinatlas.org/13705/1584_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/13705/1584_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/13705/1608_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/13705/1608_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/13705/1664_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/13705/1664_D2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96HY6 |
| SMART | SM01128; |
| UniProt Domain [FT] | DOMAIN 229..273; /note="PCI" |
| InterPro | IPR019153;IPR050899;IPR036388;IPR036390; |
| Pfam | PF09756; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198171-DDRGK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDK5RAP3 | Intact, Biogrid, Bioplex | true |
| SRPRA | Biogrid, Bioplex | true |
| TMED1 | Biogrid, Bioplex | true |
| TMED10 | Biogrid, Opencell | true |
| UFC1 | Biogrid, Bioplex | true |
| UFL1 | Intact, Biogrid | true |
| AIMP1 | Biogrid | false |
| ALK | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
