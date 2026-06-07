---
type: protein-evaluation
gene: "C19orf67"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C19orf67 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C19orf67 |
| 蛋白名称 | UPF0575 protein C19orf67 |
| 蛋白大小 | 358 aa / 39.8 kDa |
| UniProt ID | A6NJJ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm, Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 358 aa / 39.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR021748; Pfam: PF11771 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.5/180** | |
| **归一化总分** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.8 |
| 高置信度残基 (pLDDT>90) 占比 | 36.9% |
| 置信残基 (pLDDT 70-90) 占比 | 23.7% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 27.9% |
| 有序区域 (pLDDT>70) 占比 | 60.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.8，有序区 60.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021748; Pfam: PF11771 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C19orf53 | 0.584 | 0.000 | — |
| CCDC130 | 0.542 | 0.000 | — |
| C19orf57 | 0.541 | 0.000 | — |
| ZSWIM4 | 0.477 | 0.000 | — |
| PALM3 | 0.476 | 0.000 | — |
| PODNL1 | 0.474 | 0.000 | — |
| SAMD1 | 0.471 | 0.000 | — |
| ADGRE3 | 0.418 | 0.000 | — |
| SLC22A18AS | 0.418 | 0.000 | — |
| DCAF15 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 10，IntAct interactions: 0
- 调控相关比例: 1 / 10 = 10%

**评价**: STRING 10 个预测互作，IntAct 0 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.8 + PDB: 无 | pLDDT=71.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nucleoplasm, Nucleoli | 待确认 |
| PPI | STRING + IntAct | 10 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C19orf67 — UPF0575 protein C19orf67，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小358 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NJJ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188032-C19orf67/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C19orf67
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NJJ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000188032-C19orf67/subcellular

![](https://images.proteinatlas.org/46351/1977_G8_35_cr5e56872cd7180_red_green.jpg)
![](https://images.proteinatlas.org/46351/1977_G8_52_cr5e56872cd7c94_red_green.jpg)
![](https://images.proteinatlas.org/46351/2007_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/46351/2007_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/46351/2024_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/46351/2024_E4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NJJ6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A6NJJ6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR021748; |
| Pfam | PF11771; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188032-C19orf67/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
