---
type: protein-evaluation
gene: "FANCD2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FANCD2 — REJECTED (研究热度过高 (PubMed strict=790，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FANCD2 / FACD |
| 蛋白名称 | Fanconi anemia group D2 protein |
| 蛋白大小 | 1451 aa / 164.1 kDa |
| UniProt ID | Q9BXW9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Nucleoli, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1451 aa / 164.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=790 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.7; PDB: 6VAA, 6VAD, 6VAE, 6VAF, 7AY1, 7KZQ, 7KZR |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029448; Pfam: PF14631 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Nucleoli, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- condensed chromosome (GO:0000793)
- cytosol (GO:0005829)
- DNA repair complex (GO:1990391)
- nuclear body (GO:0016604)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 790 |
| PubMed broad count | 1290 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FACD |

**关键文献**:
1. Homologous-recombination-deficient tumours are dependent on Polθ-mediated repair.. *Nature*. PMID: 25642963
2. FANCD2-FANCI surveys DNA and recognizes double- to single-stranded junctions.. *Nature*. PMID: 39085614
3. Modeling injury and repair in kidney organoids reveals that homologous recombination governs tubular intrinsic repair.. *Science translational medicine*. PMID: 35235339
4. FBXL12 degrades FANCD2 to regulate replication recovery and promote cancer cell survival under conditions of replication stress.. *Molecular cell*. PMID: 37591242
5. Fanconi anemia.. *Seminars in hematology*. PMID: 16822457

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.7 |
| 高置信度残基 (pLDDT>90) 占比 | 32.6% |
| 置信残基 (pLDDT 70-90) 占比 | 42.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 16.7% |
| 有序区域 (pLDDT>70) 占比 | 75.5% |
| 可用 PDB 条目 | 6VAA, 6VAD, 6VAE, 6VAF, 7AY1, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6VAA, 6VAD, 6VAE, 6VAF, 7AY1, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV）+ AlphaFold极高置信度预测（pLDDT=76.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029448; Pfam: PF14631 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAN1 | 0.999 | 0.833 | — |
| FANCB | 0.999 | 0.800 | — |
| FANCC | 0.999 | 0.911 | — |
| FANCE | 0.999 | 0.971 | — |
| UBE2T | 0.999 | 0.852 | — |
| FANCF | 0.999 | 0.800 | — |
| FANCA | 0.999 | 0.912 | — |
| BRCA1 | 0.999 | 0.779 | — |
| FANCG | 0.999 | 0.854 | — |
| BRCA2 | 0.999 | 0.842 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BRCA2 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:15115758 |
| TRAF6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TNFRSF1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TNFRSF1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| FANCE | psi-mi:"MI:0018"(two hybrid) | pubmed:12649160|imex:IM-19947 |
| FANCG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14933|pubmed:18212739 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17314511 |
| MEN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12874027|imex:IM-18979 |
| Smyd5 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| FSCN1 | psi-mi:"MI:0096"(pull down) | imex:IM-15159|pubmed:20603015 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.7 + PDB: 6VAA, 6VAD, 6VAE, 6VAF, 7AY1,  | pLDDT=76.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear bodies; 额外: Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FANCD2 — Fanconi anemia group D2 protein，研究基础较多，新颖性有限。
2. 蛋白大小1451 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 790 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 790 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXW9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144554-FANCD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FANCD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXW9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000144554-FANCD2/subcellular

![](https://images.proteinatlas.org/16117/949_F3_4_red_green.jpg)
![](https://images.proteinatlas.org/16117/949_F3_5_red_green.jpg)
![](https://images.proteinatlas.org/63742/1132_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/63742/1132_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/63742/1139_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/63742/1139_D10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BXW9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BXW9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029448; |
| Pfam | PF14631; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144554-FANCD2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BRCA1 | Intact, Biogrid | true |
| BRCA2 | Intact, Biogrid | true |
| CEBPD | Intact, Biogrid | true |
| EGFR | Intact, Biogrid | true |
| FANCE | Intact, Biogrid | true |
| FANCI | Intact, Biogrid | true |
| MEN1 | Intact, Biogrid | true |
| MRE11 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
