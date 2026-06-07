---
type: protein-evaluation
gene: "FAM217B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM217B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM217B / C20orf177 |
| 蛋白名称 | Protein FAM217B |
| 蛋白大小 | 383 aa / 42.1 kDa |
| UniProt ID | Q9NTX9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 383 aa / 42.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029266; Pfam: PF15344 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf177 |

**关键文献**:
1. Cerebrospinal Fluid Protein Biomarker Discovery in CLN3.. *Journal of proteome research*. PMID: 37338096
2. A Genome-Wide Methylation Approach Identifies a New Hypermethylated Gene Panel in Ulcerative Colitis.. *International journal of molecular sciences*. PMID: 27517910

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.2 |
| 高置信度残基 (pLDDT>90) 占比 | 4.4% |
| 置信残基 (pLDDT 70-90) 占比 | 13.3% |
| 中等置信 (pLDDT 50-70) 占比 | 41.8% |
| 低置信 (pLDDT<50) 占比 | 40.5% |
| 有序区域 (pLDDT>70) 占比 | 17.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.2），有序残基占 17.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029266; Pfam: PF15344 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCK1 | 0.769 | 0.744 | — |
| KIAA1614 | 0.695 | 0.000 | — |
| CD209 | 0.635 | 0.635 | — |
| DUSP6 | 0.611 | 0.611 | — |
| RAB11FIP1 | 0.591 | 0.591 | — |
| ASB8 | 0.558 | 0.000 | — |
| PPP1R3D | 0.546 | 0.000 | — |
| LRRC28 | 0.505 | 0.000 | — |
| IFT46 | 0.481 | 0.000 | — |
| RIBC2 | 0.475 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMARCE1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SPANXN3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SUOX | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| AIRIM | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CDCA7L | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ANKS1A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| L3MBTL2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HMBOX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| POLR2L | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TLE5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.2 + PDB: 无 | pLDDT=57.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM217B — Protein FAM217B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小383 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NTX9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196227-FAM217B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM217B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NTX9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000196227-FAM217B/subcellular

![](https://images.proteinatlas.org/41021/474_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/41021/474_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/41021/480_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/41021/480_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/41021/510_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/41021/510_C8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NTX9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NTX9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029266; |
| Pfam | PF15344; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000196227-FAM217B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANP32B | Intact | false |
| C1orf109 | Intact | false |
| C2CD6 | Intact | false |
| CCDC102B | Intact | false |
| CDCA7L | Intact | false |
| COIL | Bioplex | false |
| EXOC8 | Intact | false |
| HARS2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
