---
type: protein-evaluation
gene: "FANCB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FANCB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FANCB |
| 蛋白名称 | Fanconi anemia group B protein |
| 蛋白大小 | 859 aa / 97.7 kDa |
| UniProt ID | Q8NB91 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 859 aa / 97.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=72 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=71.0; PDB: 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033333 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.0/180** | |
| **归一化总分** | | | **62.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- Fanconi anaemia nuclear complex (GO:0043240)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 72 |
| PubMed broad count | 100 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Fanconi Anemia.. **. PMID: 20301575
2. Pathogenic mutations identified by a multimodality approach in 117 Japanese Fanconi anemia patients.. *Haematologica*. PMID: 30792206
3. Molecular analysis of Fanconi anemia: the experience of the Bone Marrow Failure Study Group of the Italian Association of Pediatric Onco-Hematology.. *Haematologica*. PMID: 24584348
4. Whole-genome sequencing identifies new candidate genes for nonobstructive azoospermia.. *Andrology*. PMID: 36017582
5. New advances in the DNA damage response network of Fanconi anemia and BRCA proteins. FAAP95 replaces BRCA2 as the true FANCB protein.. *Cell cycle (Georgetown, Tex.)*. PMID: 15611632

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.0 |
| 高置信度残基 (pLDDT>90) 占比 | 15.7% |
| 置信残基 (pLDDT 70-90) 占比 | 49.7% |
| 中等置信 (pLDDT 50-70) 占比 | 14.2% |
| 低置信 (pLDDT<50) 占比 | 20.4% |
| 有序区域 (pLDDT>70) 占比 | 65.4% |
| 可用 PDB 条目 | 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FANCB/FANCB-PAE.png]]

**评价**: PDB实验结构（7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV）+ AlphaFold极高置信度预测（pLDDT=71.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033333 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCF | 0.999 | 0.998 | — |
| FAAP20 | 0.999 | 0.994 | — |
| CENPS | 0.999 | 0.994 | — |
| FANCE | 0.999 | 0.998 | — |
| FANCI | 0.999 | 0.800 | — |
| FANCL | 0.999 | 0.998 | — |
| FANCC | 0.999 | 0.998 | — |
| FANCG | 0.999 | 0.998 | — |
| FANCM | 0.999 | 0.994 | — |
| FAAP100 | 0.999 | 0.998 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Fancc | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| UBE2T | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PSMB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FANCM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17289582|imex:IM-25488 |
| FAAP24 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17289582|imex:IM-25488 |
| FANCA | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17289582|imex:IM-25488 |
| PPP1R7 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DNAJC7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| THBS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL6R | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.0 + PDB: 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT,  | pLDDT=71.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FANCB — Fanconi anemia group B protein，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小859 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 72 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NB91
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181544-FANCB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FANCB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NB91
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FANCB/FANCB-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NB91 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR033333; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000181544-FANCB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FAAP100 | Intact, Biogrid | true |
| FANCA | Biogrid, Opencell | true |
| FANCC | Biogrid, Bioplex | true |
| CENPS | Biogrid | false |
| FAAP20 | Biogrid | false |
| FANCF | Biogrid | false |
| FANCG | Biogrid | false |
| FANCL | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
