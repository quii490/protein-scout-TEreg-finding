---
type: protein-evaluation
gene: "R3HCC1L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## R3HCC1L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | R3HCC1L / C10orf28, GIDRP88 |
| 蛋白名称 | Coiled-coil domain-containing protein R3HCC1L |
| 蛋白大小 | 792 aa / 87.9 kDa |
| UniProt ID | Q7Z5L2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear speckles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 792 aa / 87.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012677, IPR039884 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf28, GIDRP88 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.8 |
| 高置信度残基 (pLDDT>90) 占比 | 10.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 71.5% |
| 有序区域 (pLDDT>70) 占比 | 19.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.8），有序残基占 19.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012677, IPR039884 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CBSL | 0.844 | 0.000 | — |
| CBS | 0.844 | 0.000 | — |
| SARS1 | 0.621 | 0.621 | — |
| TBL1X | 0.612 | 0.000 | — |
| LRRIQ3 | 0.512 | 0.421 | — |
| PDX1 | 0.448 | 0.000 | — |
| ZNF354A | 0.442 | 0.000 | — |
| C2orf42 | 0.438 | 0.000 | — |
| USPL1 | 0.435 | 0.000 | — |
| PHGDH | 0.433 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRRIQ3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SARS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EZR | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| EEF1G | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| EGLN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26972000|imex:IM-22750 |
| DNAAF19 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| POC1A | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| CEP19 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| MKS1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| CDKN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 12
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.8 + PDB: 无 | pLDDT=50.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nuclear speckles | 待确认 |
| PPI | STRING + IntAct | 10 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. R3HCC1L — Coiled-coil domain-containing protein R3HCC1L，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小792 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=50.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z5L2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166024-R3HCC1L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=R3HCC1L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z5L2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000166024-R3HCC1L/subcellular

![](https://images.proteinatlas.org/37367/517_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/37367/517_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/37367/520_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/37367/520_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/37367/523_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/37367/523_E4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z5L2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z5L2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012677;IPR039884; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
