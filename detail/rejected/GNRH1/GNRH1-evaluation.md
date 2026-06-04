---
type: protein-evaluation
gene: "GNRH1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNRH1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=322，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNRH1 / GNRH, GRH, LHRH |
| 蛋白名称 | Progonadoliberin-1 |
| 蛋白大小 | 92 aa / 10.4 kDa |
| UniProt ID | P01148 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted |
| 蛋白大小 | 5/10 | ×1 | 5 | 92 aa / 10.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=322 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=72.2; PDB: 4D5M, 9U4W |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002012, IPR019792, IPR004079; Pfam: PF00446 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65.0/180** | |
| **归一化总分** | | | **36.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Secreted | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon terminus (GO:0043679)
- cytoplasmic side of rough endoplasmic reticulum membrane (GO:0098556)
- dendrite (GO:0030425)
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)
- Golgi-associated vesicle (GO:0005798)
- neurosecretory vesicle (GO:1990008)
- perikaryon (GO:0043204)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 322 |
| PubMed broad count | 619 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GNRH, GRH, LHRH |

**关键文献**:
1. Isolated Gonadotropin-Releasing Hormone (GnRH) Deficiency.. **. PMID: 20301509
2. Development of the gonadotropin-releasing hormone system.. *Journal of neuroendocrinology*. PMID: 35067985
3. Hypogonadotropic hypogonadism and GNRH1 mutations in mice and humans.. *Frontiers of hormone research*. PMID: 20389089
4. Interleukin-30 subverts prostate cancer-endothelium crosstalk by fostering angiogenesis and activating immunoregulatory and oncogenic signaling pathways.. *Journal of experimental & clinical cancer research : CR*. PMID: 38087324
5. Genetics defects in GNRH1: a paradigm of hypothalamic congenital gonadotropin deficiency.. *Brain research*. PMID: 20887715

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 12.0% |
| 置信残基 (pLDDT 70-90) 占比 | 42.4% |
| 中等置信 (pLDDT 50-70) 占比 | 42.4% |
| 低置信 (pLDDT<50) 占比 | 3.3% |
| 有序区域 (pLDDT>70) 占比 | 54.4% |
| 可用 PDB 条目 | 4D5M, 9U4W |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4D5M, 9U4W）+ AlphaFold高质量预测（pLDDT=72.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002012, IPR019792, IPR004079; Pfam: PF00446 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNRHR | 0.999 | 0.000 | — |
| GNRH2 | 0.998 | 0.000 | — |
| KISS1R | 0.969 | 0.000 | — |
| KISS1 | 0.967 | 0.000 | — |
| AKT1 | 0.942 | 0.000 | — |
| MAPK3 | 0.935 | 0.000 | — |
| MAPK1 | 0.918 | 0.000 | — |
| AMH | 0.918 | 0.000 | — |
| AKT3 | 0.911 | 0.000 | — |
| AKT2 | 0.910 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Nol3 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:16249178|imex:IM-19255 |
| Srsf7 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:16249178|imex:IM-19255 |
| Tra2a | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:16249178|imex:IM-19255 |
| EMC8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MTX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EMC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM68 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MALSU1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EMC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 4D5M, 9U4W | pLDDT=72.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Secreted / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GNRH1 — Progonadoliberin-1，研究基础较多，新颖性有限。
2. 蛋白大小92 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 322 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P01148
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147437-GNRH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNRH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P01148
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
