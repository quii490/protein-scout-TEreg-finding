---
type: protein-evaluation
gene: "SHFL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHFL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SHFL / C19orf66, FLJ11286, IRAV, RYDEN, SFL |
| 蛋白名称 | Shiftless antiviral inhibitor of ribosomal frameshifting protein |
| 蛋白大小 | 291 aa / 33.1 kDa |
| UniProt ID | Q9NUL5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus; Cytoplasm, P-body |
| 蛋白大小 | 10/10 | ×1 | 10 | 291 aa / 33.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR026795; Pfam: PF15135 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, P-body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- P-body (GO:0000932)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C19orf66, FLJ11286, IRAV, RYDEN, SFL |

**关键文献**:
1. Functional features of a novel interferon-stimulated gene SHFL: a comprehensive review.. *Frontiers in microbiology*. PMID: 38149274
2. The antiviral protein Shiftless blocks p-body formation during KSHV infection.. *bioRxiv : the preprint server for biology*. PMID: 38014318
3. Restriction of Flaviviruses by an Interferon-Stimulated Gene SHFL/C19orf66.. *International journal of molecular sciences*. PMID: 36293480
4. Shiftless, a Critical Piece of the Innate Immune Response to Viral Infection.. *Viruses*. PMID: 35746809
5. Mouse Liver-Expressed Shiftless Is an Evolutionarily Conserved Antiviral Effector Restricting Human and Murine Hepaciviruses.. *Microbiology spectrum*. PMID: 37341610

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.1 |
| 高置信度残基 (pLDDT>90) 占比 | 59.1% |
| 置信残基 (pLDDT 70-90) 占比 | 32.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 1.7% |
| 有序区域 (pLDDT>70) 占比 | 91.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.1，有序区 91.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026795; Pfam: PF15135 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MOV10 | 0.705 | 0.000 | — |
| IFI6 | 0.607 | 0.000 | — |
| OAS2 | 0.586 | 0.000 | — |
| ISG15 | 0.579 | 0.000 | — |
| UBE2L6 | 0.568 | 0.000 | — |
| HERC6 | 0.566 | 0.000 | — |
| IFI35 | 0.564 | 0.000 | — |
| IRF7 | 0.547 | 0.000 | — |
| OAS1 | 0.544 | 0.000 | — |
| ISG20 | 0.541 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000467182.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000253110.10 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| OCIAD2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| KRTAP10-9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ADAMTSL4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP4-12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MDFI | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRTAP4-4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.1 + PDB: 无 | pLDDT=88.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, P-body / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SHFL — Shiftless antiviral inhibitor of ribosomal frameshifting protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小291 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NUL5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130813-SHFL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SHFL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NUL5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000130813-SHFL/subcellular

![](https://images.proteinatlas.org/42001/421_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/42001/421_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/42001/425_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/42001/425_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/42001/427_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/42001/427_C6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NUL5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NUL5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026795; |
| Pfam | PF15135; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000130813-SHFL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TNS2 | Intact, Biogrid | true |
| DRICH1 | Intact | false |
| DTNBP1 | Intact | false |
| IKZF1 | Intact | false |
| KRT40 | Intact | false |
| KRTAP10-5 | Intact | false |
| KRTAP10-7 | Intact | false |
| KRTAP10-8 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
