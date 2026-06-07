---
type: protein-evaluation
gene: "SMAD7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SMAD7 — REJECTED (研究热度过高 (PubMed strict=1893，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMAD7 |
| 蛋白名称 | SMAD7 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | SMAD7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Centrosome, Basal body; 额外: Nucleoli fibrillar ; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1893 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **56.5/180** | |
| **归一化总分** | | | **31.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome, Basal body; 额外: Nucleoli fibrillar center, Cytosol | Supported |
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
| PubMed strict count | 1893 |
| PubMed broad count | 3257 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Fibroblast Smad7 Induction Protects the Remodeling Pressure-Overloaded Heart.. *Circulation research*. PMID: 38899461
2. Smad7 in the hippocampus contributes to memory impairment in aged mice after anesthesia and surgery.. *Journal of neuroinflammation*. PMID: 37507781
3. PHF14 enhances DNA methylation of SMAD7 gene to promote TGF-β-driven lung adenocarcinoma metastasis.. *Cell discovery*. PMID: 37072414
4. Ginsenoside Rb1 Relieves Cellular Senescence and Pulmonary Fibrosis by Promoting NRF2/QKI/SMAD7 Axis.. *The American journal of Chinese medicine*. PMID: 39756830
5. Smad7:β-catenin complex regulates myogenic gene transcription.. *Cell death & disease*. PMID: 31097718

**评价**: 研究基础较多，新颖性有限。

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
| SMURF2 | 0.999 | 0.960 | — |
| TGFBR1 | 0.999 | 0.934 | — |
| NEDD4L | 0.999 | 0.975 | — |
| SMURF1 | 0.999 | 0.994 | — |
| YAP1 | 0.998 | 0.979 | — |
| RNF111 | 0.997 | 0.645 | — |
| TGFBR2 | 0.994 | 0.644 | — |
| UCHL5 | 0.993 | 0.292 | — |
| TGFB1 | 0.989 | 0.095 | — |
| SMAD6 | 0.984 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| "l | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG15109 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| COPS5 | psi-mi:"MI:0018"(two hybrid) | pubmed:14993265|imex:IM-17233 |
| SMAD4 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:15128733|imex:IM-23719 |
| SKI | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:15128733|imex:IM-23719 |
| PRMT5 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:19032343|imex:IM-23720 |
| HDAC3 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:19032343|imex:IM-23720 |
| TBL1XR1 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:19032343|imex:IM-23720 |
| EP300 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:25303530|imex:IM-23610 |
| Lasp | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm, Centrosome, Basal body; 额外: Nucleoli  | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SMAD7 — SMAD7 (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 1893 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1893 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/SMAD7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101665-SMAD7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMAD7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/SMAD7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000101665-SMAD7/subcellular

![](https://images.proteinatlas.org/28897/2147_G11_20_red_green.jpg)
![](https://images.proteinatlas.org/28897/2147_G11_58_red_green.jpg)
![](https://images.proteinatlas.org/28897/2152_C5_22_red_green.jpg)
![](https://images.proteinatlas.org/28897/2152_C5_25_red_green.jpg)
![](https://images.proteinatlas.org/28897/2169_C8_56_red_green.jpg)
![](https://images.proteinatlas.org/28897/2169_C8_81_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15105 |
| SMART | SM00523;SM00524; |
| UniProt Domain [FT] | DOMAIN 64..207; /note="MH1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00438"; DOMAIN 261..426; /note="MH2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00439" |
| InterPro | IPR013790;IPR003619;IPR013019;IPR017855;IPR001132;IPR008984;IPR036578; |
| Pfam | PF03165;PF03166; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000101665-SMAD7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACVR1B | Intact, Biogrid | true |
| COPS5 | Intact, Biogrid | true |
| SMURF2 | Intact, Biogrid | true |
| WWP2 | Intact, Biogrid | true |
| YAP1 | Intact, Biogrid | true |
| AXIN1 | Intact | false |
| AXIN2 | Biogrid | false |
| BMPR1A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
