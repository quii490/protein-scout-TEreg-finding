---
type: protein-evaluation
gene: "GPR87"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPR87 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR87 / GPR95 |
| 蛋白名称 | G-protein coupled receptor 87 |
| 蛋白大小 | 358 aa / 41.4 kDa |
| UniProt ID | Q9BY21 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Lipid droplets, Mitochondria; 额外: Nucleoplasm; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 358 aa / 41.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000276, IPR017452, IPR008109; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Lipid droplets, Mitochondria; 额外: Nucleoplasm | Approved |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

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
| AlphaFold 平均 pLDDT | 81.9 |
| 高置信度残基 (pLDDT>90) 占比 | 52.5% |
| 置信残基 (pLDDT 70-90) 占比 | 26.8% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 8.9% |
| 有序区域 (pLDDT>70) 占比 | 79.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.9，有序区 79.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452, IPR008109; Pfam: PF00001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ALDH18A1 | 0.728 | 0.000 | — |
| LPAR3 | 0.682 | 0.000 | — |
| LPAR2 | 0.678 | 0.000 | — |
| LPAR1 | 0.659 | 0.000 | — |
| WFDC5 | 0.555 | 0.000 | — |
| OR56B4 | 0.523 | 0.000 | — |
| ENPP2 | 0.519 | 0.000 | — |
| GPR45 | 0.512 | 0.000 | — |
| OR52W1 | 0.498 | 0.000 | — |
| LYPD3 | 0.496 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RAMP3 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP1 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.9 + PDB: 无 | pLDDT=81.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / Lipid droplets, Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GPR87 — G-protein coupled receptor 87，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小358 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BY21
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138271-GPR87/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR87
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BY21
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Lipid droplets (approved)。来源: https://www.proteinatlas.org/ENSG00000138271-GPR87/subcellular

![](https://images.proteinatlas.org/66313/1244_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/66313/1244_C12_5_red_green.jpg)
![](https://images.proteinatlas.org/66313/1247_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/66313/1247_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/66313/1320_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/66313/1320_D4_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BY21-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BY21 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000276;IPR017452;IPR008109; |
| Pfam | PF00001; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138271-GPR87/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
