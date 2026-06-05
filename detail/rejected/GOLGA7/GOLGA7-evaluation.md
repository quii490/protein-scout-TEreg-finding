---
type: protein-evaluation
gene: "GOLGA7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GOLGA7 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOLGA7 / GCP16 |
| 蛋白名称 | Golgin subfamily A member 7 |
| 蛋白大小 | 137 aa / 15.8 kDa |
| UniProt ID | Q7Z5G4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 137 aa / 15.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.9; PDB: 8HF3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019383, IPR051371; Pfam: PF10256 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- Golgi membrane (GO:0000139)
- Golgi stack (GO:0005795)
- palmitoyltransferase complex (GO:0002178)
- tertiary granule lumen (GO:1904724)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GCP16 |

**关键文献**:
1. Functional dissection of the zDHHC palmitoyltransferase 5-golgin A7 palmitoylation complex.. *The Journal of biological chemistry*. PMID: 40930250
2. A ZDHHC5-GOLGA7 Protein Acyltransferase Complex Promotes Nonapoptotic Cell Death.. *Cell chemical biology*. PMID: 31631010
3. Loss of Golga7 Suppresses Oncogenic Nras-Driven Leukemogenesis without Detectable Toxicity in Adult Mice.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40091521
4. The interactions of ZDHHC5/GOLGA7 with SARS-CoV-2 spike (S) protein and their effects on S protein's subcellular localization, palmitoylation and pseudovirus entry.. *Virology journal*. PMID: 34961524
5. Golgi Apparatus Target Proteins in Gastroenterological Cancers: A Comprehensive Review of GOLPH3 and GOLGA Proteins.. *Cells*. PMID: 37508488

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.9 |
| 高置信度残基 (pLDDT>90) 占比 | 65.7% |
| 置信残基 (pLDDT 70-90) 占比 | 25.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 4.4% |
| 有序区域 (pLDDT>70) 占比 | 91.2% |
| 可用 PDB 条目 | 8HF3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.9，有序区 91.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019383, IPR051371; Pfam: PF10256 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZDHHC9 | 0.999 | 0.045 | — |
| ZDHHC5 | 0.996 | 0.637 | — |
| GOLGA3 | 0.939 | 0.292 | — |
| NRAS | 0.932 | 0.240 | — |
| ZFP36L2 | 0.918 | 0.000 | — |
| SPTLC1 | 0.904 | 0.000 | — |
| ORMDL3 | 0.904 | 0.000 | — |
| SPTLC2 | 0.900 | 0.000 | — |
| SPTSSA | 0.900 | 0.000 | — |
| SPTSSB | 0.900 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| ACTN2 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-25511|pubmed:25910212 |
| KCNIP4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MESD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NCALD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KCNIP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FAM72D | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KCNIP3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TSPAN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.9 + PDB: 8HF3 | pLDDT=88.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GOLGA7 — Golgin subfamily A member 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小137 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z5G4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147533-GOLGA7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOLGA7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z5G4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z5G4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
