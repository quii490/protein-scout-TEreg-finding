---
type: protein-evaluation
gene: "C8orf82"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C8orf82 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C8orf82 |
| 蛋白名称 | UPF0598 protein C8orf82 |
| 蛋白大小 | 216 aa / 23.9 kDa |
| UniProt ID | Q6P1X6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 216 aa / 23.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR028108; Pfam: PF14956 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrion (GO:0005739)

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
| AlphaFold 平均 pLDDT | 87.0 |
| 高置信度残基 (pLDDT>90) 占比 | 76.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 12.0% |
| 有序区域 (pLDDT>70) 占比 | 85.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.0，有序区 85.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028108; Pfam: PF14956 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ETFA | 0.777 | 0.776 | — |
| ETFB | 0.649 | 0.618 | — |
| C15orf40 | 0.579 | 0.000 | — |
| THNSL1 | 0.547 | 0.000 | — |
| ZNF845 | 0.511 | 0.000 | — |
| C2orf69 | 0.471 | 0.000 | — |
| DGLUCY | 0.451 | 0.000 | — |
| C5orf63 | 0.450 | 0.000 | — |
| NINJ2 | 0.446 | 0.000 | — |
| MYL5 | 0.444 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSPD1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| MGST3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TRMT61B | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| PDK1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| MRPS27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ETFA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| - | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ETFB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FECH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-29649|pubmed:36836934 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 9
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.0 + PDB: 无 | pLDDT=87.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 14 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. C8orf82 — UPF0598 protein C8orf82，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小216 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P1X6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213563-C8orf82/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C8orf82
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P1X6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000213563-C8orf82/subcellular

![](https://images.proteinatlas.org/34331/921_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/34331/921_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/34331/923_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/34331/923_B4_3_red_green.jpg)
![](https://images.proteinatlas.org/34331/931_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/34331/931_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P1X6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P1X6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028108; |
| Pfam | PF14956; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000213563-C8orf82/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ETFA | Biogrid, Bioplex | true |
| CLPP | Biogrid | false |
| ETFB | Biogrid | false |
| MRPS27 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
