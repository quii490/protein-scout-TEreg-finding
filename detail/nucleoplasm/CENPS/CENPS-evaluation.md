---
type: protein-evaluation
gene: "CENPS"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CENPS 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPS / APITD1 / FAAP16 / MHF1 |
| 蛋白名称 | Centromere protein S |
| 蛋白大小 | 138 aa / 15.9 kDa |
| UniProt ID | Q8N2Z9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: —; UniProt: Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore |
| 蛋白大小 | 8/10 | ×1 | 8 | 138 aa / 15.9 kDa |
| 研究新颖性 | 7/10 | ×5 | 35 | PubMed strict=75 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=89.4; PDB: 暂无 |
| 调控结构域 | 10/10 | ×2 | 20 | InterPro: IPR029003, IPR009072; Pfam: PF15630 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **153.2/180** | |
| **归一化总分 (÷1.83)** | | | **83.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | — | — |
| UniProt | Nucleus | ECO:0000269, ECO:0000269, ECO:0000269
| UniProt | Chromosome, centromere | ECO:0000269, ECO:0000269
| UniProt | Chromosome, centromere, kinetochore | ECO:0000269

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- chromatin (GO:0000785) [IDA:ComplexPortal]
- cytosol (GO:0005829) [TAS:Reactome]
- FANCM-MHF complex (GO:0071821) [IDA:UniProtKB]
- Fanconi anaemia nuclear complex (GO:0043240) [IDA:UniProtKB]
- inner kinetochore (GO:0000939) [IPI:ComplexPortal]
- nucleoplasm (GO:0005654) [TAS:Reactome]
- nucleus (GO:0005634) [NAS:ComplexPortal]

**结论**: HPA: —; UniProt: Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore

#### 3.2 蛋白大小评估

**评价**: 138 aa / 15.9 kDa，大小适合大部分生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 75 |
| PubMed 搜索链接 | [CENPS PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CENPS) |

**关键文献**:
暂无文献记录。

**评价**: 有一定研究基础。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.4 |
| 高置信度残基 (pLDDT>90) 占比 | 80.4% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.8% |
| 低置信 (pLDDT<50) 占比 | 8.7% |
| 有序区域 (pLDDT>70) 占比 | 85.5% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029003, IPR009072; Pfam: PF15630 |

**染色质调控潜力分析**: 存在染色质/调控相关结构域/功能特征: nucleosome, dna-binding, remodeling, kinetochore

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCE | 0.999 | 0.994 | — |
| CENPT | 0.999 | 0.975 | — |
| FANCF | 0.999 | 0.994 | — |
| CENPC | 0.999 | 0.800 | — |
| CENPX | 0.999 | 0.999 | — |
| FAAP24 | 0.999 | 0.994 | — |
| FANCB | 0.999 | 0.994 | — |
| FANCM | 0.999 | 0.999 | — |
| FANCC | 0.999 | 0.994 | — |
| FANCL | 0.999 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CENPT | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:22304917|imex:IM-17361 |
| CENPW | psi-mi:"MI:0071"(molecular sieving) | pubmed:22304917|imex:IM-17361 |
| CENPX | psi-mi:"MI:0071"(molecular sieving) | pubmed:22304917|imex:IM-17361 |
| CTNNA3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LHX4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000308583.2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| HOMEZ | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| CENPO | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SPRED1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217|doi:10.1016/j.celrep.2020.108050 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=89.4, v6 | 预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore / — | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 83.7/100

**核心优势**:
1. CENPS — Centromere protein S，较新颖，PubMed 75 篇。
2. 蛋白大小138 aa，适合大部分生化实验。
3. AlphaFold pLDDT=89.4，结构预测质量高。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计 ChIP-seq/CUT&RUN 验证染色质结合
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N2Z9
- Protein Atlas: https://www.proteinatlas.org/search/CENPS
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N2Z9
- STRING: https://string-db.org/network/9606.CENPS
- Packet data timestamp: 2026-06-03 04:47:29

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N2Z9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
