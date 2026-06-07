---
type: protein-evaluation
gene: "PADI3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PADI3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PADI3 / PAD3, PDI3 |
| 蛋白名称 | Protein-arginine deiminase type-3 |
| 蛋白大小 | 664 aa / 74.7 kDa |
| UniProt ID | Q9ULW8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 664 aa / 74.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.7; PDB: 6CE1, 7D4Y, 7D56, 7D5R, 7D5V, 7D8N, 7DAN |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008972, IPR004303, IPR013530, IPR036556, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PAD3, PDI3 |

**关键文献**:
1. Citrullination of pyruvate kinase M2 by PADI1 and PADI3 regulates glycolysis and cancer cell proliferation.. *Nature communications*. PMID: 33741961
2. Pseudogenization of the Hair-Related Genes PADI3 and S100A3 in Cetaceans and Hippopotamus amphibius.. *Journal of molecular evolution*. PMID: 37787841
3. Assessment of the Genetic Spectrum of Uncombable Hair Syndrome in a Cohort of 107 Individuals.. *JAMA dermatology*. PMID: 36044230
4. Variant PADI3 in Central Centrifugal Cicatricial Alopecia.. *The New England journal of medicine*. PMID: 30763140
5. Deimination in epidermal barrier and hair formation.. *Philosophical transactions of the Royal Society of London. Series B, Biological sciences*. PMID: 37778378

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.7 |
| 高置信度残基 (pLDDT>90) 占比 | 84.2% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 96.2% |
| 可用 PDB 条目 | 6CE1, 7D4Y, 7D56, 7D5R, 7D5V, 7D8N, 7DAN |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6CE1, 7D4Y, 7D56, 7D5R, 7D5V, 7D8N, 7DAN）+ AlphaFold极高置信度预测（pLDDT=93.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008972, IPR004303, IPR013530, IPR036556, IPR013732; Pfam: PF03068, PF08527, PF08526 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TCHH | 0.885 | 0.000 | — |
| FLG2 | 0.846 | 0.000 | — |
| FLG | 0.839 | 0.000 | — |
| S100A3 | 0.707 | 0.000 | — |
| H3C13 | 0.622 | 0.000 | — |
| H3C12 | 0.622 | 0.000 | — |
| SPARC | 0.491 | 0.000 | — |
| ELANE | 0.469 | 0.000 | — |
| PRTN3 | 0.456 | 0.000 | — |
| PADI1 | 0.436 | 0.330 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000486702.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RAB11B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| INCA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| REL | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KIF3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SMARCD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OAZ3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NFKB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PML | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NFKB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 15
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.7 + PDB: 6CE1, 7D4Y, 7D56, 7D5R, 7D5V,  | pLDDT=93.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Vesicles, Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 12 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PADI3 — Protein-arginine deiminase type-3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小664 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULW8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142619-PADI3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PADI3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULW8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000142619-PADI3/subcellular

![](https://images.proteinatlas.org/43739/1125_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43739/1125_A4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43739/1386_F11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43739/1386_F11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43739/516_G5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43739/516_G5_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9ULW8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9ULW8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008972;IPR004303;IPR013530;IPR036556;IPR013732;IPR038685;IPR013733; |
| Pfam | PF03068;PF08527;PF08526; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000142619-PADI3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANXA9 | Bioplex | false |
| ATP5PB | Intact | false |
| CAPZA2 | Bioplex | false |
| DNALI1 | Intact | false |
| FOS | Bioplex | false |
| INCA1 | Intact | false |
| KLF11 | Intact | false |
| MAPK3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
