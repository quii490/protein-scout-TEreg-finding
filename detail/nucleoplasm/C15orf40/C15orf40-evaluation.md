---
type: protein-evaluation
gene: "C15orf40"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C15orf40 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C15orf40 |
| 蛋白名称 | UPF0235 protein C15orf40 |
| 蛋白大小 | 153 aa / 16.4 kDa |
| UniProt ID | Q8WUR7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 153 aa / 16.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003746, IPR036591; Pfam: PF02594 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular characterization and prognostic modeling of liquid-liquid phase separation-related genes in osteosarcoma based on single-cell sequencing and weighted gene co-expression network analysis.. *Translational cancer research*. PMID: 41510092
2. A 15q25.2 microdeletion phenotype for premature ovarian failure in a Chinese girl: a case report and review of literature.. *BMC medical genomics*. PMID: 32894148
3. KMT2C, a histone methyltransferase, is mutated in a family segregating non-syndromic primary failure of tooth eruption.. *Scientific reports*. PMID: 31712638

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.6 |
| 高置信度残基 (pLDDT>90) 占比 | 34.0% |
| 置信残基 (pLDDT 70-90) 占比 | 31.4% |
| 中等置信 (pLDDT 50-70) 占比 | 20.3% |
| 低置信 (pLDDT<50) 占比 | 14.4% |
| 有序区域 (pLDDT>70) 占比 | 65.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.6，有序区 65.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003746, IPR036591; Pfam: PF02594 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DRG1 | 0.802 | 0.797 | — |
| SLC25A1 | 0.798 | 0.797 | — |
| POLE2 | 0.798 | 0.797 | — |
| CS | 0.798 | 0.797 | — |
| GRN | 0.797 | 0.797 | — |
| SLC35E3 | 0.779 | 0.000 | — |
| DRG2 | 0.625 | 0.602 | — |
| CLIC2 | 0.610 | 0.610 | — |
| C8orf82 | 0.579 | 0.000 | — |
| PROSER2 | 0.560 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACSL3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SAP30 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CALML3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLIC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLHL36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000304177 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.6 + PDB: 无 | pLDDT=75.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C15orf40 — UPF0235 protein C15orf40，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小153 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WUR7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169609-C15orf40/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C15orf40
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WUR7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000169609-C15orf40/subcellular

![](https://images.proteinatlas.org/41947/1913_A20_1_red_green.jpg)
![](https://images.proteinatlas.org/41947/1913_A20_2_red_green.jpg)
![](https://images.proteinatlas.org/41947/2036_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/41947/2036_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/41947/2057_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/41947/2057_A10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WUR7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
