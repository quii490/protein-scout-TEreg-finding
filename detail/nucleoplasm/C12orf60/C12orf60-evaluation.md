---
type: protein-evaluation
gene: "C12orf60"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C12orf60 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C12orf60 |
| 蛋白名称 | Uncharacterized protein C12orf60 |
| 蛋白大小 | 245 aa / 27.6 kDa |
| UniProt ID | Q5U649 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm, Vesicles, Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 245 aa / 27.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027895; Pfam: PF15047 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Vesicles, Plasma membrane | Approved |
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
| PubMed broad count | 1 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.8 |
| 高置信度残基 (pLDDT>90) 占比 | 44.5% |
| 置信残基 (pLDDT 70-90) 占比 | 30.2% |
| 中等置信 (pLDDT 50-70) 占比 | 17.1% |
| 低置信 (pLDDT<50) 占比 | 8.2% |
| 有序区域 (pLDDT>70) 占比 | 74.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.8，有序区 74.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027895; Pfam: PF15047 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMCO3 | 0.615 | 0.000 | — |
| ERP27 | 0.540 | 0.324 | — |
| BMP4 | 0.450 | 0.450 | — |
| ZNF678 | 0.450 | 0.000 | — |
| C3orf67 | 0.447 | 0.000 | — |
| FAM234B | 0.439 | 0.000 | — |
| DYM | 0.416 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ERP27 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BMP4 | psi-mi:"MI:0231"(mammalian protein protein interac | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 2
- 调控相关比例: 1 / 7 = 14%

**评价**: STRING 7 个预测互作，IntAct 2 个实验互作。调控相关配体占比 14%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.8 + PDB: 无 | pLDDT=80.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nucleoplasm, Vesicles, Plasma membran | 待确认 |
| PPI | STRING + IntAct | 7 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C12orf60 — Uncharacterized protein C12orf60，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小245 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5U649
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182993-C12orf60/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C12orf60
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5U649
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000182993-C12orf60/subcellular

![](https://images.proteinatlas.org/42461/1609_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42461/1609_G12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/42461/1634_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42461/1634_G12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/42461/1723_G5_11_cr57eab2dd75d6f_blue_red_green.jpg)
![](https://images.proteinatlas.org/42461/1723_G5_17_cr57eab2e5dc6e6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5U649-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5U649 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027895; |
| Pfam | PF15047; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182993-C12orf60/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ERP27 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
