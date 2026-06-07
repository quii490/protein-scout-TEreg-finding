---
type: protein-evaluation
gene: "ANKRD36C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKRD36C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKRD36C |
| 蛋白名称 | Ankyrin repeat domain-containing protein 36C |
| 蛋白大小 | 1778 aa / 199.7 kDa |
| UniProt ID | Q5JPF3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1778 aa / 199.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050657, IPR002110, IPR036770, IPR039497; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.5/180** | |
| **归一化总分** | | | **62.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The impaired response of nasal epithelial cells to microplastic stimulation in asthma and COPD.. *Scientific reports*. PMID: 39905077
2. Integrated whole-exome and bulk transcriptome sequencing delineates the dynamic evolution from preneoplasia to invasive lung adenocarcinoma featured with ground-glass nodules.. *Cancer medicine*. PMID: 38864483
3. The CC2D2B is a novel genetic modifier of the clinical phenotype in patients with hereditary angioedema due to C1 inhibitor deficiency.. *Gene*. PMID: 38679185
4. Gene expression analysis of primary gingival cancer by whole exome sequencing in thirteen Chinese patients.. *International journal of clinical and experimental pathology*. PMID: 32782722
5. [Exploring the association between de novo mutations and non-syndromic cleft lip with or without palate based on whole exome sequencing of case-parent trios].. *Beijing da xue xue bao. Yi xue ban = Journal of Peking University. Health sciences*. PMID: 35701113

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.3 |
| 高置信度残基 (pLDDT>90) 占比 | 8.2% |
| 置信残基 (pLDDT 70-90) 占比 | 28.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 57.2% |
| 有序区域 (pLDDT>70) 占比 | 36.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.3），有序残基占 36.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050657, IPR002110, IPR036770, IPR039497; Pfam: PF00023, PF12796, PF13637 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANKRD36 | 0.999 | 0.000 | — |
| ANKRD36B | 0.896 | 0.279 | — |
| FAHD2B | 0.519 | 0.000 | — |
| ZNF717 | 0.507 | 0.091 | — |
| CDKN2D | 0.501 | 0.000 | — |
| CDKN2C | 0.482 | 0.000 | — |
| FAM178B | 0.480 | 0.000 | — |
| LOC112267897 | 0.476 | 0.093 | — |
| FAM104B | 0.471 | 0.000 | — |
| ASB12 | 0.454 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000403302.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| aspS | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ANKRD36B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATG16L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31015422|imex:IM-29997 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.3 + PDB: 无 | pLDDT=51.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ANKRD36C — Ankyrin repeat domain-containing protein 36C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1778 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=51.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JPF3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174501-ANKRD36C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANKRD36C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JPF3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000174501-ANKRD36C/subcellular

![](https://images.proteinatlas.org/51757/1002_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/51757/1002_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/51757/1004_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/51757/1004_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/57661/1060_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/57661/1060_F6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JPF3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5JPF3 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050657;IPR002110;IPR036770;IPR039497; |
| Pfam | PF00023;PF12796;PF13637;PF14915; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000174501-ANKRD36C/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
