---
type: protein-evaluation
gene: "COX16"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COX16 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COX16 / C14orf112 |
| 蛋白名称 | Cytochrome c oxidase assembly protein COX16 homolog, mitochondrial |
| 蛋白大小 | 106 aa / 12.3 kDa |
| UniProt ID | Q9P0S2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 8/10 | x1 | 8 | 106 aa / 12.3 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=75.7; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR020164; Pfam: PF14138 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf112 |

**关键文献**:
1. DAZAP1 Phase Separation Regulates Mitochondrial Metabolism to Facilitate Invasion and Metastasis of Oral Squamous Cell Carcinoma.. *Cancer research*. PMID: 39120588
2. COX16 promotes COX2 metallation and assembly during respiratory complex IV biogenesis.. *eLife*. PMID: 29381136
3. SUMOylation of SYNJ2BP-COX16 promotes breast cancer progression through DRP1-mediated mitochondrial fission.. *Cancer letters*. PMID: 35998797
4. Cox16 protein is physically associated with Cox1p assembly intermediates and with cytochrome oxidase.. *The Journal of biological chemistry*. PMID: 28821616
5. A novel cancer-associated membrane signature predicts prognosis and therapeutic response for lung adenocarcinoma.. *Scientific reports*. PMID: 40664871

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.7 |
| 高置信度残基 (pLDDT>90) 占比 | 10.4% |
| 置信残基 (pLDDT 70-90) 占比 | 57.5% |
| 中等置信 (pLDDT 50-70) 占比 | 32.1% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 67.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.7，有序区 67.9%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020164; Pfam: PF14138 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COA3 | 0.828 | 0.292 | — |
| TMEM109 | 0.804 | 0.000 | — |
| GATB | 0.793 | 0.000 | — |
| COA6 | 0.774 | 0.000 | — |
| COX17 | 0.747 | 0.000 | — |
| COX18 | 0.745 | 0.000 | — |
| SURF1 | 0.663 | 0.000 | — |
| COX20 | 0.660 | 0.000 | — |
| PET100 | 0.656 | 0.000 | — |
| SCO1 | 0.650 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.7 + PDB: 无 | pLDDT=75.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. COX16 -- Cytochrome c oxidase assembly protein COX16 homolog, mitochondrial，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小106 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P0S2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133983-COX16/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COX16
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P0S2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P0S2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
