---
type: protein-evaluation
gene: "TWIST1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TWIST1 — REJECTED (研究热度过高 (PubMed strict=1457，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TWIST1 / BHLHA38, TWIST |
| 蛋白名称 | Twist-related protein 1 |
| 蛋白大小 | 202 aa / 21.0 kDa |
| UniProt ID | Q15672 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 202 aa / 21.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1457 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.3; PDB: 2MJV, 8OSB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR050283, IPR036638, IPR047093; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.5/180** | |
| **归一化总分** | | | **46.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1457 |
| PubMed broad count | 3104 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHA38, TWIST |

**关键文献**:
1. Transcription factor Twist1 drives fibroblast activation to promote kidney fibrosis via signaling proteins Prrx1/TNC.. *Kidney international*. PMID: 39181396
2. Redundant or separate entities?--roles of Twist1 and Twist2 as molecular switches during gene transcription.. *Nucleic acids research*. PMID: 20935057
3. Autophagy regulates tumor growth and metastasis.. *bioRxiv : the preprint server for biology*. PMID: 37961427
4. Twist1-Induced Epithelial Dissemination Requires Prkd1 Signaling.. *Cancer research*. PMID: 31676574
5. TWIST1 Homodimers and Heterodimers Orchestrate Lineage-Specific Differentiation.. *Molecular and cellular biology*. PMID: 32179550

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.3 |
| 高置信度残基 (pLDDT>90) 占比 | 20.3% |
| 置信残基 (pLDDT 70-90) 占比 | 15.8% |
| 中等置信 (pLDDT 50-70) 占比 | 41.6% |
| 低置信 (pLDDT<50) 占比 | 22.3% |
| 有序区域 (pLDDT>70) 占比 | 36.1% |
| 可用 PDB 条目 | 2MJV, 8OSB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.3），有序残基占 36.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR050283, IPR036638, IPR047093; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RUNX2 | 0.972 | 0.081 | — |
| TP53 | 0.967 | 0.628 | — |
| G3BP2 | 0.960 | 0.292 | — |
| CD44 | 0.959 | 0.000 | — |
| SNAI2 | 0.952 | 0.000 | — |
| TWIST2 | 0.939 | 0.292 | — |
| ZEB1 | 0.932 | 0.000 | — |
| SNAI1 | 0.901 | 0.000 | — |
| MSX2 | 0.901 | 0.000 | — |
| TCF12 | 0.900 | 0.588 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000242261.5 | psi-mi:"MI:0096"(pull down) | pubmed:24525235|imex:IM-22300 |
| Sox2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |
| ETS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12059|pubmed:18598946 |
| RABGAP1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| TP53 | psi-mi:"MI:0049"(filter binding) | pubmed:18504427|imex:IM-16564 |
| KAT2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18504427|imex:IM-16564 |
| CITED1 | psi-mi:"MI:0096"(pull down) | pubmed:22975381|imex:IM-17775 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22975381|imex:IM-17775 |
| TCF3 | psi-mi:"MI:0018"(two hybrid) | pubmed:10749989|imex:IM-27510 |
| CETN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.3 + PDB: 2MJV, 8OSB | pLDDT=66.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TWIST1 — Twist-related protein 1，研究基础较多，新颖性有限。
2. 蛋白大小202 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1457 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1457 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15672
- Protein Atlas: https://www.proteinatlas.org/ENSG00000122691-TWIST1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TWIST1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15672
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15672-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15672 |
| SMART | SM00353; |
| UniProt Domain [FT] | DOMAIN 108..159; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR050283;IPR036638;IPR047093; |
| Pfam | PF00010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000122691-TWIST1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KAT2B | Intact, Biogrid | true |
| KMT5A | Intact, Biogrid | true |
| STAT3 | Intact, Biogrid | true |
| TCF4 | Intact, Biogrid | true |
| TP53 | Intact, Biogrid | true |
| BRD4 | Intact | false |
| BTRC | Biogrid | false |
| CBLC | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
