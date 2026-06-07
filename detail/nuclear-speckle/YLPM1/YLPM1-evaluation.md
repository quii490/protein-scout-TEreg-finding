---
type: protein-evaluation
gene: "YLPM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YLPM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YLPM1 / C14orf170, ZAP3 |
| 蛋白名称 | YLP motif-containing protein 1 |
| 蛋白大小 | 2146 aa / 241.6 kDa |
| UniProt ID | P49750 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; UniProt: Nucleus; Nucleus speckle |
| 蛋白大小 | 2/10 | ×1 | 2 | 2146 aa / 241.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=43.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027417, IPR058903, IPR026314; Pfam: PF13671, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf170, ZAP3 |

**关键文献**:
1. Rare coding variant analysis for human diseases across biobanks and ancestries.. *Nature genetics*. PMID: 39210047
2. Discovery of obesity genes through cross-ancestry analysis.. *Nature communications*. PMID: 41168175
3. Analysis of somatic mutations in whole blood from 200,618 individuals identifies pervasive positive selection and novel drivers of clonal hematopoiesis.. *Nature genetics*. PMID: 38744975
4. Investigating causal relationships between gene expression and major depressive disorder via brain bulk-tissue and cell type-specific eQTL: A Mendelian randomization and Bayesian colocalization study.. *Journal of affective disorders*. PMID: 40311809
5. Discovery of novel obesity genes through cross-ancestry analysis.. *medRxiv : the preprint server for health sciences*. PMID: 39484254

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 43.2 |
| 高置信度残基 (pLDDT>90) 占比 | 1.4% |
| 置信残基 (pLDDT 70-90) 占比 | 15.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 78.1% |
| 有序区域 (pLDDT>70) 占比 | 16.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=43.2），有序残基占 16.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR058903, IPR026314; Pfam: PF13671, PF26583 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMARCC2 | 0.779 | 0.503 | — |
| PPP1CC | 0.762 | 0.750 | — |
| RBMX | 0.729 | 0.356 | — |
| PPP1CA | 0.718 | 0.710 | — |
| KHDRBS1 | 0.696 | 0.421 | — |
| EP400 | 0.675 | 0.000 | — |
| NONO | 0.671 | 0.464 | — |
| SFPQ | 0.656 | 0.615 | — |
| ZNF318 | 0.586 | 0.000 | — |
| SRGAP2 | 0.582 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pik3cb | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Prkar1a | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| CHGB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PRMT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BMP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NONO | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| PPP1CA | psi-mi:"MI:0018"(two hybrid) | imex:IM-16965|pubmed:22321011 |
| USP45 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=43.2 + PDB: 无 | pLDDT=43.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. YLPM1 — YLP motif-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2146 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=43.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49750
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119596-YLPM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YLPM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49750
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000119596-YLPM1/subcellular

![](https://images.proteinatlas.org/61123/1082_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/61123/1082_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/61123/1103_G11_3_red_green.jpg)
![](https://images.proteinatlas.org/61123/1103_G11_4_red_green.jpg)
![](https://images.proteinatlas.org/61123/1117_F5_4_red_green.jpg)
![](https://images.proteinatlas.org/61123/1117_F5_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49750-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P49750 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027417;IPR058903;IPR026314; |
| Pfam | PF13671;PF26583; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119596-YLPM1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CACNA1A | Intact, Biogrid | true |
| PPP1CA | Intact, Biogrid | true |
| PSPC1 | Biogrid, Opencell | true |
| SFPQ | Biogrid, Opencell | true |
| AR | Biogrid | false |
| BRD4 | Biogrid | false |
| CPSF6 | Opencell | false |
| DDX21 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
