---
type: protein-evaluation
gene: "SYCP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SYCP1 — REJECTED (研究热度过高 (PubMed strict=114，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYCP1 / SCP1 |
| 蛋白名称 | Synaptonemal complex protein 1 |
| 蛋白大小 | 976 aa / 114.2 kDa |
| UniProt ID | Q15431 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Cytosol; UniProt: Nucleus; Chromosome; Chromosome, centromere |
| 蛋白大小 | 8/10 | ×1 | 8 | 976 aa / 114.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=114 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=70.2; PDB: 4YTO, 6F5X, 6F62, 6F63, 6F64 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008827; Pfam: PF05483 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Cytosol | Approved |
| UniProt | Nucleus; Chromosome; Chromosome, centromere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- autosome (GO:0030849)
- central element (GO:0000801)
- chromosome (GO:0005694)
- chromosome, centromeric region (GO:0000775)
- male germ cell nucleus (GO:0001673)
- synaptonemal complex (GO:0000795)
- transverse filament (GO:0000802)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 114 |
| PubMed broad count | 213 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SCP1 |

**关键文献**:
1. Meiotic chromatin-associated HSF5 is indispensable for pachynema progression and male fertility.. *Nucleic acids research*. PMID: 39162221
2. Histone demethylase KDM2A recruits HCFC1 and E2F1 to orchestrate male germ cell meiotic entry and progression.. *The EMBO journal*. PMID: 39160277
3. METTL16 is Required for Meiotic Sex Chromosome Inactivation and DSB Formation and Recombination during Male Meiosis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39607422
4. hnRNPC Functions with HuR to Regulate Alternative Splicing in an m6A-Dependent Manner and is Essential for Meiosis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39921484
5. A rare frameshift mutation in SYCP1 is associated with human male infertility.. *Molecular human reproduction*. PMID: 35377450

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.2 |
| 高置信度残基 (pLDDT>90) 占比 | 28.5% |
| 置信残基 (pLDDT 70-90) 占比 | 36.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 28.8% |
| 有序区域 (pLDDT>70) 占比 | 64.8% |
| 可用 PDB 条目 | 4YTO, 6F5X, 6F62, 6F63, 6F64 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4YTO, 6F5X, 6F62, 6F63, 6F64）+ AlphaFold极高置信度预测（pLDDT=70.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008827; Pfam: PF05483 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYCE1 | 0.998 | 0.132 | — |
| SYCE2 | 0.998 | 0.095 | — |
| SYCP3 | 0.996 | 0.095 | — |
| SYCP2 | 0.991 | 0.000 | — |
| TEX12 | 0.983 | 0.000 | — |
| SYCE3 | 0.967 | 0.000 | — |
| REC8 | 0.911 | 0.119 | — |
| HORMAD1 | 0.878 | 0.048 | — |
| SMC1B | 0.857 | 0.075 | — |
| STAG3 | 0.842 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Uba1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HSPA5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| CREB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATG16L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31015422|imex:IM-29997 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.2 + PDB: 4YTO, 6F5X, 6F62, 6F63, 6F64 | pLDDT=70.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Chromosome, centromere / Nuclear bodies, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SYCP1 — Synaptonemal complex protein 1，研究基础较多，新颖性有限。
2. 蛋白大小976 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 114 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 114 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15431
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198765-SYCP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYCP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15431
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000198765-SYCP1/subcellular

![](https://images.proteinatlas.org/21083/1926_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21083/1926_C2_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15431-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15431 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008827; |
| Pfam | PF05483; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198765-SYCP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PKM | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
