---
type: protein-evaluation
gene: "GLUD2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GLUD2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLUD2 / GLUDP1 |
| 蛋白名称 | Glutamate dehydrogenase 2, mitochondrial |
| 蛋白大小 | 558 aa / 61.4 kDa |
| UniProt ID | P49448 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion matrix |
| 蛋白大小 | 10/10 | ×1 | 10 | 558 aa / 61.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.2; PDB: 6G2U |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR046346, IPR006095, IPR006096, IPR006097, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion matrix | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)

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
| AlphaFold 平均 pLDDT | 90.2 |
| 高置信度残基 (pLDDT>90) 占比 | 86.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 10.2% |
| 有序区域 (pLDDT>70) 占比 | 88.9% |
| 可用 PDB 条目 | 6G2U |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.2，有序区 88.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046346, IPR006095, IPR006096, IPR006097, IPR033524; Pfam: PF00208, PF02812 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GLUL | 0.985 | 0.000 | — |
| GLUD1 | 0.984 | 0.835 | — |
| ALDH18A1 | 0.978 | 0.000 | — |
| PC | 0.976 | 0.000 | — |
| GLS | 0.976 | 0.000 | — |
| GLS2 | 0.975 | 0.000 | — |
| GOT1 | 0.970 | 0.101 | — |
| GOT1L1 | 0.970 | 0.101 | — |
| CPS1 | 0.968 | 0.053 | — |
| GOT2 | 0.967 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TOM1L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ATF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22304920|imex:IM-17307 |
| TRMT10C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12139|pubmed:18984158 |
| MYC | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| SH3GL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| KLHL22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GLUD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CEP135 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| CLPP | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24491|pubmed:26058080 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.2 + PDB: 6G2U | pLDDT=90.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion matrix / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GLUD2 — Glutamate dehydrogenase 2, mitochondrial，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小558 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49448
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182890-GLUD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLUD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49448
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
