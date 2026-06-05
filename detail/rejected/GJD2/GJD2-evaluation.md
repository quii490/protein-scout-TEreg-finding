---
type: protein-evaluation
gene: "GJD2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GJD2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GJD2 / GJA9 |
| 蛋白名称 | Gap junction delta-2 protein |
| 蛋白大小 | 321 aa / 36.1 kDa |
| UniProt ID | Q9UKL4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell junction, gap junction |
| 蛋白大小 | 10/10 | ×1 | 10 | 321 aa / 36.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.4; PDB: 2N6A, 7XKI, 7XKK, 7XKT, 7XL8, 7XNH, 7XNV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000500, IPR002260, IPR019570, IPR017990, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cell junction, gap junction | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- connexin complex (GO:0005922)
- plasma membrane (GO:0005886)
- synapse (GO:0045202)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.4 |
| 高置信度残基 (pLDDT>90) 占比 | 36.4% |
| 置信残基 (pLDDT 70-90) 占比 | 29.0% |
| 中等置信 (pLDDT 50-70) 占比 | 10.6% |
| 低置信 (pLDDT<50) 占比 | 24.0% |
| 有序区域 (pLDDT>70) 占比 | 65.4% |
| 可用 PDB 条目 | 2N6A, 7XKI, 7XKK, 7XKT, 7XL8, 7XNH, 7XNV, 8HKP, 8IYG, 8QOJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2N6A, 7XKI, 7XKK, 7XKT, 7XL8, 7XNH, 7XNV, 8HKP, 8IYG, 8QOJ）+ AlphaFold极高置信度预测（pLDDT=72.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000500, IPR002260, IPR019570, IPR017990, IPR013092; Pfam: PF00029 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TJP1 | 0.985 | 0.071 | — |
| GJA1 | 0.945 | 0.081 | — |
| GJC1 | 0.931 | 0.000 | — |
| MAPK3 | 0.905 | 0.000 | — |
| CDK1 | 0.903 | 0.000 | — |
| MAPK1 | 0.900 | 0.000 | — |
| MAPK7 | 0.900 | 0.000 | — |
| GJB2 | 0.788 | 0.000 | — |
| TJP2 | 0.748 | 0.071 | — |
| MPDZ | 0.720 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NOS1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| MAGI2 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| MPDZ | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| PCLO | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| IL16 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| MAGI1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| PICK1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| MAST1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| GRIP1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| PALS2 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.4 + PDB: 2N6A, 7XKI, 7XKK, 7XKT, 7XL8,  | pLDDT=72.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, gap junction / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GJD2 — Gap junction delta-2 protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小321 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKL4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159248-GJD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GJD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKL4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UKL4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
