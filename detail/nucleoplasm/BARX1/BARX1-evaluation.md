---
type: protein-evaluation
gene: "BARX1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BARX1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BARX1 |
| 蛋白名称 | Homeobox protein BarH-like 1 |
| 蛋白大小 | 254 aa / 27.3 kDa |
| UniProt ID | Q9HBU1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 254 aa / 27.3 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=96 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.8; PDB: 2DMT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR020479, IPR017970, IPR050848, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
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
| PubMed strict count | 96 |
| PubMed broad count | 139 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Barx1 and evolutionary changes in feeding.. *Journal of anatomy*. PMID: 16313395
2. BARX1 promotes osteosarcoma cell proliferation and invasion by regulating HSPA6 expression.. *Journal of orthopaedic surgery and research*. PMID: 36927457
3. Role of BARX1 in Development and Disease.. *Genesis (New York, N.Y. : 2000)*. PMID: 41840842
4. Cloning, characterization, localization, and mutational screening of the human BARX1 gene.. *Genomics*. PMID: 10995576
5. ZFP36 loss-mediated BARX1 stabilization promotes malignant phenotypes by transactivating master oncogenes in NSCLC.. *Cell death & disease*. PMID: 37587140

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.8 |
| 高置信度残基 (pLDDT>90) 占比 | 20.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.7% |
| 中等置信 (pLDDT 50-70) 占比 | 47.6% |
| 低置信 (pLDDT<50) 占比 | 26.8% |
| 有序区域 (pLDDT>70) 占比 | 25.6% |
| 可用 PDB 条目 | 2DMT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.8），有序残基占 25.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR020479, IPR017970, IPR050848, IPR009057; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BMP4 | 0.740 | 0.000 | — |
| SFRP2 | 0.731 | 0.088 | — |
| FGF8 | 0.714 | 0.000 | — |
| SHH | 0.682 | 0.000 | — |
| PAX9 | 0.659 | 0.000 | — |
| MSX1 | 0.659 | 0.000 | — |
| NKX3-2 | 0.652 | 0.045 | — |
| LHX8 | 0.650 | 0.104 | — |
| SFRP1 | 0.641 | 0.088 | — |
| NOG | 0.623 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HOXD9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CYP17A1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Znf641 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Dlx1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.8 + PDB: 2DMT | pLDDT=63.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BARX1 — Homeobox protein BarH-like 1，研究基础较多，新颖性有限。
2. 蛋白大小254 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 96 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HBU1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131668-BARX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BARX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HBU1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000131668-BARX1/subcellular

![](https://images.proteinatlas.org/55858/1501_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/55858/1501_C8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HBU1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HBU1 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR020479;IPR017970;IPR050848;IPR009057;IPR000047; |
| Pfam | PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000131668-BARX1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
