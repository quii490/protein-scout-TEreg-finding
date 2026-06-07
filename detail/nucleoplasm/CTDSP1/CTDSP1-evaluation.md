---
type: protein-evaluation
gene: "CTDSP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CTDSP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTDSP1 |
| 蛋白名称 | CTDSP1 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | CTDSP1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | x4 | 20 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 5/10 | x1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 4/10 | x3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **97/180** | |
| **归一化总分** | | | **53.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | 无注释 | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据存在但较为混杂。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 66 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Targeting the C-Terminal Domain Small Phosphatase 1.. *Life (Basel, Switzerland)*. PMID: 32397221
2. [SCP Phosphatases and Oncogenesis].. *Molekuliarnaia biologiia*. PMID: 34432772
3. Tumor Suppressor Properties of Small C-Terminal Domain Phosphatases in Clear Cell Renal Cell Carcinoma.. *International journal of molecular sciences*. PMID: 37629167
4. GPC5 suppresses lung cancer progression and metastasis via intracellular CTDSP1/AhR/ARNT signaling axis and extracellular exosome secretion.. *Oncogene*. PMID: 34079082
5. Elabela, a Novel Peptide, Exerts Neuroprotective Effects Against Ischemic Stroke Through the APJ/miR-124-3p/CTDSP1/AKT Pathway.. *Cellular and molecular neurobiology*. PMID: 37106272

**评价**: 非常新颖，仅有少数基础研究。

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

**PAE**: AlphaFold数据未获取。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CTDSP1 -- CTDSP1 (UniProt未获取)，非常新颖，仅有少数基础研究。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/CTDSP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144579-CTDSP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTDSP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/CTDSP1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000144579-CTDSP1/subcellular

![](https://images.proteinatlas.org/62654/1106_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/62654/1106_B9_4_red_green.jpg)
![](https://images.proteinatlas.org/62654/1148_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/62654/1148_B9_3_red_green.jpg)
![](https://images.proteinatlas.org/62654/1294_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/62654/1294_C9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9GZU7 |
| SMART | SM00577; |
| UniProt Domain [FT] | DOMAIN 86..244; /note="FCP1 homology"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00336" |
| InterPro | IPR011948;IPR004274;IPR036412;IPR023214;IPR040078;IPR050365; |
| Pfam | PF03031; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144579-CTDSP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDCA3 | Intact, Biogrid | true |
| MBP | Intact, Biogrid | true |
| PNMA1 | Intact, Biogrid | true |
| ACTN3 | Intact | false |
| BAG3 | Intact | false |
| CDKN2C | Intact | false |
| CRYBA2 | Intact | false |
| CSTF2T | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
