---
type: protein-evaluation
gene: "SPATA2L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPATA2L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPATA2L / C16orf76 |
| 蛋白名称 | Spermatogenesis-associated protein 2-like protein |
| 蛋白大小 | 424 aa / 46.2 kDa |
| UniProt ID | Q8IUW3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Mitochondria; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 424 aa / 46.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR048839; Pfam: PF21388 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf76 |

**关键文献**:
1. Effect of a maternal high-fat diet with vegetable substitution on fetal brain transcriptome.. *The Journal of nutritional biochemistry*. PMID: 35691591
2. Spata2L Suppresses TLR4 Signaling by Promoting CYLD-Mediated Deubiquitination of TRAF6 and TAK1.. *Biochemistry. Biokhimiia*. PMID: 36180997
3. Novel genetic associations with childhood adipocytokines in Indian adolescents.. *Cytokine*. PMID: 40187068
4. Integrative Analysis of Omics Data Reveals Regulatory Network of CDK10 in Vitiligo Risk.. *Frontiers in genetics*. PMID: 33679896

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 47.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 31.4% |
| 有序区域 (pLDDT>70) 占比 | 63.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.2，有序区 63.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048839; Pfam: PF21388 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYLD | 0.955 | 0.209 | — |
| SHARPIN | 0.925 | 0.000 | — |
| RNF31 | 0.922 | 0.000 | — |
| SPATA2 | 0.921 | 0.000 | — |
| RBCK1 | 0.912 | 0.000 | — |
| VPS9D1 | 0.797 | 0.000 | — |
| ABHD8 | 0.514 | 0.000 | — |
| DBNDD1 | 0.489 | 0.000 | — |
| DEF8 | 0.455 | 0.000 | — |
| CENPBD1 | 0.435 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CYLD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CAMK2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| TNIP2 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| GRB2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| NCK2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| CEP135 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| CEP128 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| DCAF10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PAGE5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 无 | pLDDT=72.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Mitochondria; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

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
1. SPATA2L — Spermatogenesis-associated protein 2-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小424 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IUW3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158792-SPATA2L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPATA2L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IUW3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000158792-SPATA2L/subcellular

![](https://images.proteinatlas.org/41182/493_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41182/493_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41182/502_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41182/502_F9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41182/557_F9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41182/557_F9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IUW3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IUW3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR048839; |
| Pfam | PF21388; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000158792-SPATA2L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GRB2 | Intact, Biogrid | true |
| APOE | Intact | false |
| ATXN1 | Intact | false |
| ATXN10 | Intact | false |
| ATXN3 | Intact | false |
| CYLD | Biogrid | false |
| DBH | Intact | false |
| GFAP | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
