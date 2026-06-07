---
type: protein-evaluation
gene: "FAM240C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM240C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM240C |
| 蛋白名称 | Protein FAM240C |
| 蛋白大小 | 95 aa / 10.8 kDa |
| UniProt ID | A0A1B0GVR7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 95 aa / 10.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040261 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

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

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Promoter hypomethylation of CDH7: a novel epigenetic marker associated with cerebral small vessel disease.. *Frontiers in genetics*. PMID: 41890232

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.6 |
| 高置信度残基 (pLDDT>90) 占比 | 47.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.5% |
| 中等置信 (pLDDT 50-70) 占比 | 42.1% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 56.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.6，有序区 56.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040261 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMDD1 | 0.795 | 0.000 | — |
| SCYGR5 | 0.794 | 0.000 | — |
| SMIM38 | 0.794 | 0.000 | — |
| SCYGR7 | 0.794 | 0.000 | — |
| SMIM28 | 0.763 | 0.000 | — |
| ETDB | 0.720 | 0.000 | — |
| ETDA | 0.717 | 0.000 | — |
| ETDC | 0.716 | 0.000 | — |
| SCYGR1 | 0.670 | 0.000 | — |
| SMIM36 | 0.631 | 0.058 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.6 + PDB: 无 | pLDDT=78.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM240C — Protein FAM240C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小95 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A1B0GVR7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000216921-FAM240C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM240C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A1B0GVR7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000216921-FAM240C/subcellular

![](https://images.proteinatlas.org/73342/1817_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/73342/1817_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/73342/1970_D5_2_red_green.jpg)
![](https://images.proteinatlas.org/73342/1970_D5_6_red_green.jpg)
![](https://images.proteinatlas.org/73342/1983_A9_16_cr5e58ec085de5c_red_green.jpg)
![](https://images.proteinatlas.org/73342/1983_A9_6_cr5e58ec085c9b7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A0A1B0GVR7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A0A1B0GVR7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040261; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000216921-FAM240C/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
