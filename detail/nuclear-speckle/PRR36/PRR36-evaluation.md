---
type: protein-evaluation
gene: "PRR36"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRR36 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRR36 |
| 蛋白名称 | Proline-rich protein 36 |
| 蛋白大小 | 1346 aa / 132.7 kDa |
| UniProt ID | Q9H6K5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm, Nuclear speckles; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1346 aa / 132.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027907; Pfam: PF15363 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.5/180** | |
| **归一化总分** | | | **62.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Nuclear speckles | Approved |
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
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Clinical, histopathologic and molecular features of idiopathic and diabetic nodular mesangial sclerosis in humans.. *Nephrology, dialysis, transplantation : official publication of the European Dialysis and Transplant Association - European Renal Association*. PMID: 33537765
2. A reconstruction of the gene for ribulose bisphosphate carboxylase from Rhodospirillum rubrum that expresses the authentic enzyme in Escherichia coli.. *Gene*. PMID: 3084334

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.8% |
| 中等置信 (pLDDT 50-70) 占比 | 11.4% |
| 低置信 (pLDDT<50) 占比 | 85.8% |
| 有序区域 (pLDDT>70) 占比 | 2.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=42.3），有序残基占 2.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027907; Pfam: PF15363 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EVI5L | 0.507 | 0.000 | — |
| UHRF1BP1L | 0.506 | 0.000 | — |
| PCDHGB3 | 0.505 | 0.000 | — |
| PCDHGB1 | 0.478 | 0.000 | — |
| PCDHGA5 | 0.478 | 0.000 | — |
| ARHGEF38 | 0.450 | 0.046 | — |
| PCDHGA4 | 0.448 | 0.000 | — |
| PCDHGB2 | 0.447 | 0.000 | — |
| PCDHGA6 | 0.436 | 0.000 | — |
| PCDHGA2 | 0.434 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Mycbp2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| DNAJB11 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ARHGAP21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| FZR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBXW7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 5
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=42.3 + PDB: 无 | pLDDT=42.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus; 额外: Nucleoplasm, Nuclear speckles | 待确认 |
| PPI | STRING + IntAct | 12 + 5 interactions | 数据充分 |

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
1. PRR36 — Proline-rich protein 36，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1346 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=42.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H6K5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183248-PRR36/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRR36
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H6K5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000183248-PRR36/subcellular

![](https://images.proteinatlas.org/62741/1374_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62741/1374_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62741/1376_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62741/1376_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62741/1511_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62741/1511_G8_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H6K5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H6K5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027907; |
| Pfam | PF15363; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183248-PRR36/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARHGAP21 | Biogrid, Opencell | true |
| FBXW7 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
