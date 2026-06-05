---
type: protein-evaluation
gene: "CEP78"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CEP78 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEP78 / C9orf81 |
| 蛋白名称 | Centrosomal protein of 78 kDa |
| 蛋白大小 | 689 aa / 76.4 kDa |
| UniProt ID | Q5JTW2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | ×1 | 10 | 689 aa / 76.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026212, IPR001611, IPR032675; Pfam: PF13516 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskeleton, microtu... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf81 |

**关键文献**:
1. CAKUT variants in PRPF8, DYRK2, and CEP78: implications for splicing and ciliogenesis.. *bioRxiv : the preprint server for biology*. PMID: 40777246
2. A novel frameshift variant in CEP78 associated with nonsyndromic retinitis pigmentosa, and a review of CEP78-related phenotypes.. *Ophthalmic genetics*. PMID: 35240912
3. Absence of CEP78 causes photoreceptor and sperm flagella impairments in mice and a human individual.. *eLife*. PMID: 36756949
4. HIV-1 Vpr hijacks EDD-DYRK2-DDB1(DCAF1) to disrupt centrosome homeostasis.. *The Journal of biological chemistry*. PMID: 29724823
5. Cep78 knockout causes sterility and oligoasthenoteratozoospermia in male mice.. *Scientific reports*. PMID: 39747485

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.0 |
| 高置信度残基 (pLDDT>90) 占比 | 29.9% |
| 置信残基 (pLDDT 70-90) 占比 | 22.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 37.6% |
| 有序区域 (pLDDT>70) 占比 | 52.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.0），有序残基占 52.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026212, IPR001611, IPR032675; Pfam: PF13516 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLK1 | 0.818 | 0.000 | — |
| DCAF1 | 0.766 | 0.625 | — |
| PSAT1 | 0.752 | 0.000 | — |
| DDB1 | 0.749 | 0.696 | — |
| CEP250 | 0.726 | 0.223 | — |
| FGFR1OP | 0.692 | 0.686 | — |
| UBR5 | 0.658 | 0.625 | — |
| CCP110 | 0.645 | 0.292 | — |
| DYRK2 | 0.640 | 0.510 | — |
| HAUS6 | 0.607 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000037596.8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SQSTM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| SH3BP4 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| NAP1L4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| DCAF1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| NSUN2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| UBR5 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| cutF | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.0 + PDB: 无 | pLDDT=64.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CEP78 — Centrosomal protein of 78 kDa，非常新颖，仅有少数基础研究。
2. 蛋白大小689 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JTW2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148019-CEP78/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEP78
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JTW2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JTW2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
