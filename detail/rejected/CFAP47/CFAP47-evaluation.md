---
type: protein-evaluation
gene: "CFAP47"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CFAP47 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CFAP47 / CHDC2, CXorf22, CXorf30, CXorf59 |
| 蛋白名称 | Cilia- and flagella-associated protein 47 |
| 蛋白大小 | 3187 aa / 361.6 kDa |
| UniProt ID | Q6ZTR5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton, flagellum basal body |
| 蛋白大小 | 0/10 | ×1 | 0 | 3187 aa / 361.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR056343, IPR001715, IPR036872, IPR013783, IPR058 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytoskeleton, flagellum basal body | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cilium (GO:0005929)
- sperm head-tail coupling apparatus (GO:0120212)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CHDC2, CXorf22, CXorf30, CXorf59 |

**关键文献**:
1. Deleterious variants in X-linked CFAP47 induce asthenoteratozoospermia and primary male infertility.. *American journal of human genetics*. PMID: 33472045
2. CFAP47 is a novel causative gene implicated in X-linked polycystic kidney disease.. *medRxiv : the preprint server for health sciences*. PMID: 38633811
3. Analysis of clinical characteristics and histopathological transcription in 40 patients afflicted by epilepsy stemming from focal cortical dysplasia.. *Epilepsia open*. PMID: 38491953
4. WDR87 interacts with CFAP47 protein in the middle piece of spermatozoa flagella to participate in sperm tail assembly.. *Molecular human reproduction*. PMID: 36571501
5. Mutations in CFAP47, a previously reported MMAF causative gene, also contribute to the respiratory defects in patients with PCD.. *Molecular genetics & genomic medicine*. PMID: 37723893

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.5 |
| 高置信度残基 (pLDDT>90) 占比 | 3.7% |
| 置信残基 (pLDDT 70-90) 占比 | 66.2% |
| 中等置信 (pLDDT 50-70) 占比 | 11.6% |
| 低置信 (pLDDT<50) 占比 | 18.5% |
| 有序区域 (pLDDT>70) 占比 | 69.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=71.5，有序区 69.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056343, IPR001715, IPR036872, IPR013783, IPR058952; Pfam: PF24529, PF26579 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LRGUK | 0.746 | 0.521 | — |
| TTC29 | 0.703 | 0.000 | — |
| CFAP43 | 0.699 | 0.000 | — |
| CFAP65 | 0.652 | 0.000 | — |
| LRRC43 | 0.646 | 0.136 | — |
| VWA3B | 0.630 | 0.000 | — |
| CFAP74 | 0.616 | 0.309 | — |
| CFAP70 | 0.599 | 0.000 | — |
| MAATS1 | 0.586 | 0.100 | — |
| WDR66 | 0.571 | 0.100 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RPL35 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SRP54 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:25604459|imex:IM-23333 |
| ESR2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:25604459|imex:IM-23333 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.5 + PDB: 无 | pLDDT=71.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, flagellum basal body / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CFAP47 — Cilia- and flagella-associated protein 47，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小3187 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZTR5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165164-CFAP47/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CFAP47
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZTR5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
