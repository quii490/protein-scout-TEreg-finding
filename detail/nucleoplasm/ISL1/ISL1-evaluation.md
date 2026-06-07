---
type: protein-evaluation
gene: "ISL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ISL1 — REJECTED (研究热度过高 (PubMed strict=739，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ISL1 |
| 蛋白名称 | Insulin gene enhancer protein ISL-1 |
| 蛋白大小 | 349 aa / 39.0 kDa |
| UniProt ID | P61371 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear speckles, Mitochondria; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 349 aa / 39.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=739 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR047169, IPR047 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear speckles, Mitochondria | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 739 |
| PubMed broad count | 1218 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Single-cell epigenomic and transcriptomic analysis unveils the pivotal role of GATA5/ISL1+ fibroblasts in cardiac repair post-myocardial infarction.. *Cardiovascular research*. PMID: 40460294
2. Cre reporter strains produced by targeted insertion of EYFP and ECFP into the ROSA26 locus.. *BMC developmental biology*. PMID: 11299042
3. The emergence of human primordial germ cell-like cells in stem cell-derived gastruloids.. *Science advances*. PMID: 40138398
4. Of travelling homeoproteins and medulloblastomas.. *Oncogene*. PMID: 40760093
5. Targeting ROCK/LIMK/cofilin signaling pathway in cancer.. *Archives of pharmacal research*. PMID: 31030376

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.9 |
| 高置信度残基 (pLDDT>90) 占比 | 35.8% |
| 置信残基 (pLDDT 70-90) 占比 | 22.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 30.4% |
| 有序区域 (pLDDT>70) 占比 | 58.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.9，有序区 58.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR047169, IPR047244; Pfam: PF00046, PF00412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LHX3 | 0.998 | 0.562 | — |
| LDB1 | 0.998 | 0.732 | — |
| LHX4 | 0.983 | 0.905 | — |
| LDB2 | 0.965 | 0.399 | — |
| SSBP2 | 0.904 | 0.844 | — |
| POU4F2 | 0.901 | 0.097 | — |
| NEUROG2 | 0.897 | 0.048 | — |
| NEUROG3 | 0.896 | 0.048 | — |
| PAX6 | 0.891 | 0.091 | — |
| MNX1 | 0.890 | 0.085 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| SMAD3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RELA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CDKN2B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| ZNF511 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| LHX4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| LDB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GMNN | psi-mi:"MI:0077"(nuclear magnetic resonance) | pubmed:22615398|imex:IM-27180 |
| SSBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.9 + PDB: 无 | pLDDT=71.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear speckles, Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ISL1 — Insulin gene enhancer protein ISL-1，研究基础较多，新颖性有限。
2. 蛋白大小349 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 739 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 739 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P61371
- Protein Atlas: https://www.proteinatlas.org/ENSG00000016082-ISL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ISL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P61371
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000016082-ISL1/subcellular

![](https://images.proteinatlas.org/48613/1792_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/48613/1792_G11_4_red_green.jpg)
![](https://images.proteinatlas.org/48613/1886_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/48613/1886_F10_4_red_green.jpg)
![](https://images.proteinatlas.org/48613/1919_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/48613/1919_D10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P61371-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P61371 |
| SMART | SM00389;SM00132; |
| UniProt Domain [FT] | DOMAIN 17..70; /note="LIM zinc-binding 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 79..133; /note="LIM zinc-binding 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125" |
| InterPro | IPR001356;IPR017970;IPR009057;IPR047169;IPR047244;IPR001781; |
| Pfam | PF00046;PF00412; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000016082-ISL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LHX4 | Intact, Biogrid | true |
| SSBP4 | Intact, Biogrid, Bioplex | true |
| ESR1 | Biogrid | false |
| HNF4A | Biogrid | false |
| LDB1 | Biogrid | false |
| SSBP2 | Biogrid | false |
| SSBP3 | Biogrid | false |
| SYNGAP1 | Intact, Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
