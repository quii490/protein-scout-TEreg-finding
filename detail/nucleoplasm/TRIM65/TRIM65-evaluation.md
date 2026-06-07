---
type: protein-evaluation
gene: "TRIM65"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRIM65 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIM65 |
| 蛋白名称 | TRIM65 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | TRIM65 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Vesicles; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=49 篇 (≤60→6) |
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
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Vesicles | Supported |
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
| PubMed strict count | 49 |
| PubMed broad count | 71 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. TRIM65 promotes vascular smooth muscle cell phenotypic transformation by activating PI3K/Akt/mTOR signaling during atherogenesis.. *Atherosclerosis*. PMID: 38301602
2. TRIM65/NF2/YAP1 Signaling Coordinately Orchestrates Metabolic and Immune Advantages in Hepatocellular Carcinoma.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39005234
3. TRIM65 as a key regulator of ferroptosis and glycolysis in lactate-driven renal tubular injury and diabetic kidney disease.. *Cell reports*. PMID: 40748757
4. Research and development prospects of TRIM65.. *Journal of cancer research and clinical oncology*. PMID: 40844633
5. The Magic and Mystery of TRIM65 in Diseases.. *Current medicinal chemistry*. PMID: 38939997

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
| IFIH1 | 0.980 | 0.961 | — |
| ARRDC4 | 0.693 | 0.292 | — |
| TP53 | 0.686 | 0.625 | — |
| MRPL38 | 0.660 | 0.000 | — |
| TRAT1 | 0.596 | 0.000 | — |
| DDX58 | 0.590 | 0.318 | — |
| FBF1 | 0.578 | 0.000 | — |
| TRIM40 | 0.570 | 0.000 | — |
| WBP2 | 0.535 | 0.000 | — |
| TRIM23 | 0.519 | 0.068 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBE2U | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2Z | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| pepP | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| RBCK1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| ANAPC11 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| MARCHF7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| MKRN3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| CCNJL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GATD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm, Cytosol; 额外: Vesicles | 待确认 |
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
1. TRIM65 — TRIM65 (UniProt未获取)，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 49 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/TRIM65
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141569-TRIM65/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM65
- AlphaFold: https://alphafold.ebi.ac.uk/entry/TRIM65
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000141569-TRIM65/subcellular

![](https://images.proteinatlas.org/21575/187_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/21575/187_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/21575/188_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/21575/188_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/21575/246_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/21575/246_F10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PJ69 |
| SMART | SM00336;SM00184;SM00449; |
| UniProt Domain [FT] | DOMAIN 313..506; /note="B30.2/SPRY"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00548" |
| InterPro | IPR001870;IPR043136;IPR003879;IPR013320;IPR051051;IPR003877;IPR048222;IPR058030;IPR000315;IPR018957;IPR001841;IPR013083;IPR017907; |
| Pfam | PF00622;PF25600;PF00643;PF00097; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141569-TRIM65/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DHFR | Bioplex | false |
| DUSP6 | Biogrid | false |
| EEF1AKMT3 | Bioplex | false |
| IFIH1 | Biogrid | false |
| NPAS1 | Bioplex | false |
| NPRL2 | Bioplex | false |
| TNRC6A | Biogrid | false |
| TP53 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
