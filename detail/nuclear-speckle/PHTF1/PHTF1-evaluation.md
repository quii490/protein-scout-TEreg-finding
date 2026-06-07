---
type: protein-evaluation
gene: "PHTF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHTF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHTF1 / PHTF |
| 蛋白名称 | Protein PHTF1 |
| 蛋白大小 | 762 aa / 87.3 kDa |
| UniProt ID | Q9UMS5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; 额外: Nucleoli; UniProt: Endoplasmic reticulum membrane; Golgi apparatus, cis-Golgi n |
| 蛋白大小 | 10/10 | ×1 | 10 | 762 aa / 87.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039775, IPR021980; Pfam: PF12129 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoli | Approved |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus, cis-Golgi network membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- Golgi apparatus (GO:0005794)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PHTF |

**关键文献**:
1. Molecular characterization of a novel gene family (PHTF) conserved from Drosophila to mammals.. *Genomics*. PMID: 10729229
2. Associations of GWAS-Supported Non-MHC Genes with Autoimmune Thyroiditis in Patients with Type 1 Diabetes.. *Diabetes, metabolic syndrome and obesity : targets and therapy*. PMID: 34234497
3. Phtf1 is an integral membrane protein localized in an endoplasmic reticulum domain in maturing male germ cells.. *Biology of reproduction*. PMID: 12604659
4. Analysis of the expression of PHTF1 and related genes in acute lymphoblastic leukemia.. *Cancer cell international*. PMID: 26448723
5. Putative homeodomain transcription factor 1 interacts with the feminization factor homolog fem1b in male germ cells.. *Biology of reproduction*. PMID: 15601915

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.5 |
| 高置信度残基 (pLDDT>90) 占比 | 14.3% |
| 置信残基 (pLDDT 70-90) 占比 | 37.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 40.2% |
| 有序区域 (pLDDT>70) 占比 | 51.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.5），有序残基占 51.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039775, IPR021980; Pfam: PF12129 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RSBN1 | 0.872 | 0.000 | — |
| HNF1A | 0.791 | 0.045 | — |
| MAGI3 | 0.767 | 0.178 | — |
| BCL2L15 | 0.654 | 0.000 | — |
| PTPN22 | 0.644 | 0.106 | — |
| PHTF2 | 0.628 | 0.610 | — |
| AP4B1 | 0.584 | 0.000 | — |
| FEM1B | 0.526 | 0.098 | — |
| DCLRE1B | 0.512 | 0.000 | — |
| SWT1 | 0.509 | 0.062 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H2AC4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CAPN5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LYPD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPR156 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Cited4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| HOXB9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| PHTF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000369604 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.5 + PDB: 无 | pLDDT=61.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus, c / Nuclear bodies; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

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
1. PHTF1 — Protein PHTF1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小762 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UMS5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116793-PHTF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHTF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UMS5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000116793-PHTF1/subcellular

![](https://images.proteinatlas.org/59486/1070_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/59486/1070_G11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/59486/1076_G11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/59486/1076_G11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/59486/1171_C10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/59486/1171_C10_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UMS5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UMS5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 6..150; /note="PHTF"; /evidence="ECO:0000255" |
| InterPro | IPR039775;IPR021980; |
| Pfam | PF12129; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000116793-PHTF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| STK4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
