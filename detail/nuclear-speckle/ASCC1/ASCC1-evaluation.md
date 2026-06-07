---
type: protein-evaluation
gene: "ASCC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ASCC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASCC1 |
| 蛋白名称 | Activating signal cointegrator 1 complex subunit 1 |
| 蛋白大小 | 400 aa / 45.5 kDa |
| UniProt ID | Q8N9N2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 400 aa / 45.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.4; PDB: 8TLY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019510, IPR009210, IPR009097, IPR047538, IPR004 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- DNA repair complex (GO:1990391)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. ASCC1 structures and bioinformatics reveal a novel helix-clasp-helix RNA-binding motif linked to a two-histidine phosphodiesterase.. *The Journal of biological chemistry*. PMID: 38750793
2. Germline mutations in MSR1, ASCC1, and CTHRC1 in patients with Barrett esophagus and esophageal adenocarcinoma.. *JAMA*. PMID: 21791690
3. Association between non-Caucasian-specific ASCC1 gene polymorphism and osteoporosis and obesity in Korean postmenopausal women.. *Journal of bone and mineral metabolism*. PMID: 32653958
4. Investigating the role of ASCC1 in the causation of bone fragility.. *Frontiers in endocrinology*. PMID: 37455927
5. Congenital myopathy as a new phenotype caused by two undescribed variants in ASCC1 gene.. *American journal of medical genetics. Part A*. PMID: 35838082

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.4 |
| 高置信度残基 (pLDDT>90) 占比 | 17.2% |
| 置信残基 (pLDDT 70-90) 占比 | 38.2% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 32.8% |
| 有序区域 (pLDDT>70) 占比 | 55.4% |
| 可用 PDB 条目 | 8TLY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.4），有序残基占 55.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019510, IPR009210, IPR009097, IPR047538, IPR004088; Pfam: PF10469, PF00013 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASCC2 | 0.999 | 0.857 | — |
| ASCC3 | 0.999 | 0.834 | — |
| TRIP4 | 0.986 | 0.861 | — |
| ALKBH3 | 0.946 | 0.834 | — |
| DAP3 | 0.848 | 0.831 | — |
| YBEY | 0.832 | 0.831 | — |
| RPS11 | 0.828 | 0.826 | — |
| MRPL13 | 0.774 | 0.758 | — |
| MRPL47 | 0.768 | 0.758 | — |
| MRPL46 | 0.768 | 0.758 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CD74 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| DOK1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| KSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |
| IGLL5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IGKC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IGHG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IGHG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FGB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.4 + PDB: 8TLY | pLDDT=65.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ASCC1 — Activating signal cointegrator 1 complex subunit 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小400 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N9N2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138303-ASCC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASCC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N9N2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000138303-ASCC1/subcellular

![](https://images.proteinatlas.org/57567/1240_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/57567/1240_B10_3_red_green.jpg)
![](https://images.proteinatlas.org/57567/983_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/57567/983_G7_4_red_green.jpg)
![](https://images.proteinatlas.org/57567/991_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/57567/991_G7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N9N2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N9N2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 86..148; /note="KH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00117" |
| InterPro | IPR019510;IPR009210;IPR009097;IPR047538;IPR004088;IPR036612; |
| Pfam | PF10469;PF00013; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138303-ASCC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ASCC3 | Intact, Biogrid | true |
| ASCC2 | Biogrid | false |
| EIF3B | Opencell | false |
| EIF4A1 | Opencell | false |
| ESR1 | Biogrid | false |
| GSPT1 | Opencell | false |
| PSPC1 | Opencell | false |
| RACK1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
