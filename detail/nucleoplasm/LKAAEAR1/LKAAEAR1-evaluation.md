---
type: protein-evaluation
gene: "LKAAEAR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LKAAEAR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LKAAEAR1 / C20orf201 |
| 蛋白名称 | Protein LKAAEAR1 |
| 蛋白大小 | 194 aa / 21.5 kDa |
| UniProt ID | Q8TD35 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 194 aa / 21.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029152; Pfam: PF15478 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf201 |

**关键文献**:
1. Transcriptional Alterations in the Trigeminal Ganglia, Nucleus and Peripheral Blood Mononuclear Cells in a Rat Orofacial Pain Model.. *Frontiers in molecular neuroscience*. PMID: 29997476

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.0 |
| 高置信度残基 (pLDDT>90) 占比 | 29.4% |
| 置信残基 (pLDDT 70-90) 占比 | 23.7% |
| 中等置信 (pLDDT 50-70) 占比 | 21.1% |
| 低置信 (pLDDT<50) 占比 | 25.8% |
| 有序区域 (pLDDT>70) 占比 | 53.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.0，有序区 53.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029152; Pfam: PF15478 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMEM191C | 0.880 | 0.000 | — |
| C4orf17 | 0.670 | 0.000 | — |
| ARRDC5 | 0.611 | 0.000 | — |
| CRYBG2 | 0.507 | 0.000 | — |
| NT5C1B-RDH14 | 0.507 | 0.000 | — |
| NT5C1B | 0.506 | 0.000 | — |
| TDRD12 | 0.447 | 0.000 | — |
| AASS | 0.445 | 0.000 | — |
| MRM2 | 0.434 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KRT27 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 1
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.0 + PDB: 无 | pLDDT=71.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 9 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LKAAEAR1 — Protein LKAAEAR1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小194 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TD35
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171695-LKAAEAR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LKAAEAR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TD35
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000171695-LKAAEAR1/subcellular

![](https://images.proteinatlas.org/56463/1675_B1_33_red_green.jpg)
![](https://images.proteinatlas.org/56463/1675_B1_34_red_green.jpg)
![](https://images.proteinatlas.org/56463/1681_B1_3_red_green.jpg)
![](https://images.proteinatlas.org/56463/1681_B1_5_red_green.jpg)
![](https://images.proteinatlas.org/56463/1778_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/56463/1778_G6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TD35-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TD35 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029152; |
| Pfam | PF15478; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171695-LKAAEAR1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
