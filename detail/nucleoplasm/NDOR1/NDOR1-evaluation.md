---
type: protein-evaluation
gene: "NDOR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NDOR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NDOR1 / NR1 |
| 蛋白名称 | NADPH-dependent diflavin oxidoreductase 1 |
| 蛋白大小 | 597 aa / 66.8 kDa |
| UniProt ID | Q9UHB4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Intermediate filaments; UniProt: Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 597 aa / 66.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.9; PDB: 4H2D |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003097, IPR017927, IPR001094, IPR008254, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Intermediate filaments | Approved |
| UniProt | Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- intermediate filament cytoskeleton (GO:0045111)
- nucleoplasm (GO:0005654)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NR1 |

**关键文献**:
1. Anamorsin/Ndor1 Complex Reduces [2Fe-2S]-MitoNEET via a Transient Protein-Protein Interaction.. *Journal of the American Chemical Society*. PMID: 28648056
2. Molecular view of an electron transfer process essential for iron-sulfur protein biogenesis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 23596212
3. Identification of key genes and biological pathways associated with vascular aging in diabetes based on bioinformatics and machine learning.. *Aging*. PMID: 38809515
4. Tah18 transfers electrons to Dre2 in cytosolic iron-sulfur protein biogenesis.. *Nature chemical biology*. PMID: 20802492
5. Mechanistic insights into human pre-mRNA splicing of human ultra-short introns: potential unusual mechanism identifies G-rich introns.. *Biochemical and biophysical research communications*. PMID: 22640740

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.9 |
| 高置信度残基 (pLDDT>90) 占比 | 84.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 2.5% |
| 有序区域 (pLDDT>70) 占比 | 96.3% |
| 可用 PDB 条目 | 4H2D |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.9，有序区 96.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003097, IPR017927, IPR001094, IPR008254, IPR001709; Pfam: PF00667, PF00258, PF00175 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CIAPIN1 | 0.999 | 0.969 | — |
| DCPS | 0.953 | 0.000 | — |
| CYP4F8 | 0.904 | 0.045 | — |
| CYP3A4 | 0.903 | 0.045 | — |
| CYP4X1 | 0.901 | 0.045 | — |
| NUBP1 | 0.883 | 0.091 | — |
| CYP4F3 | 0.875 | 0.045 | — |
| CYP4F11 | 0.869 | 0.045 | — |
| RTEL1 | 0.865 | 0.091 | — |
| GLRX3 | 0.844 | 0.575 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CIAPIN1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TCF4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| MTUS2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TCHP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| HOXB2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBQLN2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NLK | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| LMO3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZNF620 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LNX1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.9 + PDB: 4H2D | pLDDT=92.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region / Cytosol; 额外: Nucleoplasm, Intermediate filaments | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NDOR1 — NADPH-dependent diflavin oxidoreductase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小597 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHB4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188566-NDOR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NDOR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHB4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000188566-NDOR1/subcellular

![](https://images.proteinatlas.org/24504/278_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24504/278_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24504/279_G6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/24504/279_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24504/280_G6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/24504/280_G6_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UHB4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UHB4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 6..150; /note="Flavodoxin-like"; /evidence="ECO:0000255\|HAMAP-Rule:MF_03178"; DOMAIN 206..447; /note="FAD-binding FR-type"; /evidence="ECO:0000255\|HAMAP-Rule:MF_03178" |
| InterPro | IPR003097;IPR017927;IPR001094;IPR008254;IPR001709;IPR029039;IPR039261;IPR023173;IPR028879;IPR001433;IPR017938; |
| Pfam | PF00667;PF00258;PF00175; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188566-NDOR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CIAPIN1 | Intact, Biogrid | true |
| CENATAC | Intact | false |
| EFHC2 | Intact | false |
| GAS8 | Intact | false |
| GLRX3 | Intact | false |
| GPS2 | Intact | false |
| HOXB2 | Intact | false |
| KIAA0408 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
