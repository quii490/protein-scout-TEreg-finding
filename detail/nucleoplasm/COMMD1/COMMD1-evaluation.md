---
type: protein-evaluation
gene: "COMMD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COMMD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COMMD1 / C2orf5, MURR1 |
| 蛋白名称 | COMM domain-containing protein 1 |
| 蛋白大小 | 190 aa / 21.2 kDa |
| UniProt ID | Q8N668 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Endosome membrane; Cytoplasmic vesicle;  |
| 蛋白大小 | 8/10 | x1 | 8 | 190 aa / 21.2 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=86.4; PDB: 2H2M, 8F2R, 8F2U, 8P0W |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR017920, IPR033776, IPR037351; Pfam: PF07258, PF |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **140.5/180** | |
| **归一化总分** | | | **78.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Endosome membrane; Cytoplasmic vesicle; Early endosome; Recycling endosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul2-RING ubiquitin ligase complex (GO:0031462)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- early endosome (GO:0005769)
- endosome (GO:0005768)
- endosome membrane (GO:0010008)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) |  |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.4 |
| 高置信度残基 (pLDDT>90) 占比 | 60.5% |
| 置信残基 (pLDDT 70-90) 占比 | 26.3% |
| 中等置信 (pLDDT 50-70) 占比 | 12.6% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 86.8% |
| 可用 PDB 条目 | 2H2M, 8F2R, 8F2U, 8P0W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量（pLDDT=86.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017920, IPR033776, IPR037351; Pfam: PF07258, PF17221 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL2 | 0.999 | 0.735 | — |
| CCDC22 | 0.996 | 0.867 | — |
| COMMD6 | 0.995 | 0.878 | — |
| VPS35L | 0.988 | 0.837 | — |
| CCDC93 | 0.988 | 0.847 | — |
| KAT2A | 0.986 | 0.292 | — |
| COMMD10 | 0.980 | 0.853 | — |
| ATP7B | 0.978 | 0.625 | — |
| COMMD9 | 0.977 | 0.828 | — |
| COMMD4 | 0.976 | 0.883 | — |

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
| 三维结构 | AlphaFold pLDDT=86.4 + PDB: 2H2M, 8F2R, 8F2U, 8P0W | pLDDT=86.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Endosome membrane; Cytoplasmic / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. COMMD1 -- COMM domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N668
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173163-COMMD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COMMD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N668
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000173163-COMMD1/subcellular

![](https://images.proteinatlas.org/49223/682_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/49223/682_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/49223/757_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/49223/757_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/49223/761_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/49223/761_F3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N668-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N668 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 118..186; /note="COMM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00602" |
| InterPro | IPR017920;IPR033776;IPR037351; |
| Pfam | PF07258;PF17221; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000173163-COMMD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATP7B | Intact, Biogrid | true |
| CCDC22 | Intact, Biogrid, Opencell, Bioplex | true |
| CCDC93 | Intact, Biogrid, Opencell, Bioplex | true |
| COMMD10 | Intact, Biogrid, Opencell, Bioplex | true |
| COMMD2 | Intact, Biogrid, Opencell, Bioplex | true |
| COMMD3 | Intact, Biogrid, Bioplex | true |
| COMMD4 | Intact, Biogrid, Opencell, Bioplex | true |
| COMMD5 | Intact, Biogrid, Opencell, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
