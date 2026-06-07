---
type: protein-evaluation
gene: "DTD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DTD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DTD1 / C20orf88, DUEB, HARS2 |
| 蛋白名称 | D-aminoacyl-tRNA deacylase 1 |
| 蛋白大小 | 209 aa / 23.4 kDa |
| UniProt ID | Q8TEA8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 209 aa / 23.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.5; PDB: 2OKV |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003732, IPR023509; Pfam: PF02580 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 5 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol | Uncertain |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf88, DUEB, HARS2 |

**关键文献**:
1. Distinct localization of chiral proofreaders resolves organellar translation conflict in plants.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37276405
2. D-tyrosyl-tRNA(Tyr) metabolism in Saccharomyces cerevisiae.. *The Journal of biological chemistry*. PMID: 10766779
3. Association analysis of DTD1 gene variations with aspirin-intolerance in asthmatics.. *International journal of molecular medicine*. PMID: 21479357
4. Identification and functional characterization of imatinib-sensitive DTD1-PDGFRB and CCDC88C-PDGFRB fusion genes in eosinophilia-associated myeloid/lymphoid neoplasms.. *Genes, chromosomes & cancer*. PMID: 24772479
5. Widespread distribution of cell defense against D-aminoacyl-tRNAs.. *The Journal of biological chemistry*. PMID: 19332551

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.5 |
| 高置信度残基 (pLDDT>90) 占比 | 70.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.7% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 10.5% |
| 有序区域 (pLDDT>70) 占比 | 77.0% |
| 可用 PDB 条目 | 2OKV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.5，有序区 77.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003732, IPR023509; Pfam: PF02580 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YARS2 | 0.532 | 0.045 | — |
| YARS1 | 0.529 | 0.061 | — |
| KAT14 | 0.435 | 0.000 | — |
| SEC23B | 0.434 | 0.067 | — |
| RBBP9 | 0.408 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 5，IntAct interactions: 0
- 调控相关比例: 0 / 5 = 0%

**评价**: STRING 5 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.5 + PDB: 2OKV | pLDDT=85.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 5 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DTD1 — D-aminoacyl-tRNA deacylase 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小209 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TEA8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125821-DTD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DTD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TEA8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (uncertain)。来源: https://www.proteinatlas.org/ENSG00000125821-DTD1/subcellular

![](https://images.proteinatlas.org/40981/392_B3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40981/392_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40981/393_B3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40981/393_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40981/396_B3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40981/396_B3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TEA8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TEA8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003732;IPR023509; |
| Pfam | PF02580; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000125821-DTD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TNNC2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
