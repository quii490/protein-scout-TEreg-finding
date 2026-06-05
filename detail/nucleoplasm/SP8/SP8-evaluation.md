---
type: protein-evaluation
gene: "SP8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SP8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SP8 |
| 蛋白名称 | Transcription factor Sp8 |
| 蛋白大小 | 490 aa / 48.7 kDa |
| UniProt ID | Q8IXZ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 490 aa / 48.7 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=98 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036236, IPR013087; Pfam: PF00096 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 98 |
| PubMed broad count | 301 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Transcription factors SP5 and SP8 drive primary cilia formation in mammalian embryos.. *Science (New York, N.Y.)*. PMID: 40875857
2. Regulation of the Human IL-10RB Gene Expression by Sp8 and Sp9.. *Journal of Alzheimer's disease : JAD*. PMID: 35811529
3. Transcription factors SP5 and SP8 drive primary cilia formation.. *bioRxiv : the preprint server for biology*. PMID: 40501818
4. Regulation of axial elongation by Cdx.. *Developmental biology*. PMID: 34958748
5. Sp8 regulates inner ear development.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 24722637

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.0 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 76.1% |
| 有序区域 (pLDDT>70) 占比 | 17.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.0），有序残基占 17.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036236, IPR013087; Pfam: PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CALB2 | 0.870 | 0.095 | — |
| DNAH11 | 0.779 | 0.000 | — |
| EMX2 | 0.738 | 0.063 | — |
| WNT3 | 0.690 | 0.045 | — |
| GSX2 | 0.689 | 0.057 | — |
| ACRV1 | 0.679 | 0.091 | — |
| DLX2 | 0.624 | 0.071 | — |
| SHH | 0.608 | 0.090 | — |
| PAX6 | 0.600 | 0.070 | — |
| NR2F1 | 0.598 | 0.067 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HEYL | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ZNF273 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ZNF519 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.0 + PDB: 无 | pLDDT=47.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SP8 — Transcription factor Sp8，研究基础较多，新颖性有限。
2. 蛋白大小490 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 98 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=47.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXZ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164651-SP8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SP8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXZ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000164651-SP8/subcellular

![](https://images.proteinatlas.org/54006/1433_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/54006/1433_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/54006/1617_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/54006/1617_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/54006/1721_B1_31_red_green.jpg)
![](https://images.proteinatlas.org/54006/1721_B1_32_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IXZ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
