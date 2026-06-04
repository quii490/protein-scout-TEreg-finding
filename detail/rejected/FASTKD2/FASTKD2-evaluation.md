---
type: protein-evaluation
gene: "FASTKD2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FASTKD2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FASTKD2 / KIAA0971 |
| 蛋白名称 | FAST kinase domain-containing protein 2, mitochondrial |
| 蛋白大小 | 710 aa / 81.5 kDa |
| UniProt ID | Q9NYY8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion matrix, mitochondrion nucleoid; Mitochondrion  |
| 蛋白大小 | 10/10 | ×1 | 10 | 710 aa / 81.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013579, IPR050870, IPR010622, IPR013584; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion matrix, mitochondrion nucleoid; Mitochondrion matrix | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- mitochondrial matrix (GO:0005759)
- mitochondrial nucleoid (GO:0042645)
- mitochondrion (GO:0005739)
- ribonucleoprotein granule (GO:0035770)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0971 |

**关键文献**:
1. Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview.. **. PMID: 26425749
2. FASTKD2-Related Combined Oxidative Phosphorylation Deficiency.. **. PMID: 41343688
3. Challenges in Genetic Diagnosis of Mitochondrial Diseases: What Can Functional Genomics' Studies Do?. *Endocrine, metabolic & immune disorders drug targets*. PMID: 38111113
4. FASTKD2 is an RNA-binding protein required for mitochondrial RNA processing and translation.. *RNA (New York, N.Y.)*. PMID: 26370583
5. Expanding the genetic spectrum of mitochondrial diseases in Tunisia: novel variants revealed by whole-exome sequencing.. *Frontiers in genetics*. PMID: 38283147

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 57.9% |
| 置信残基 (pLDDT 70-90) 占比 | 13.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 24.6% |
| 有序区域 (pLDDT>70) 占比 | 71.1% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=75.2，有序区 71.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013579, IPR050870, IPR010622, IPR013584; Pfam: PF06743, PF08368, PF08373 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NGRN | 0.968 | 0.777 | — |
| FASTK | 0.945 | 0.000 | — |
| MTERF3 | 0.939 | 0.764 | — |
| RPUSD4 | 0.929 | 0.614 | — |
| PTCD1 | 0.923 | 0.725 | — |
| TRUB2 | 0.920 | 0.782 | — |
| DDX28 | 0.911 | 0.736 | — |
| RPUSD3 | 0.838 | 0.000 | — |
| GRSF1 | 0.825 | 0.253 | — |
| LRPPRC | 0.799 | 0.088 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-21354662 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 4505953 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PHLDA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| APIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| SH2D3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 无 | pLDDT=75.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion matrix, mitochondrion nucleoid; Mito / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FASTKD2 — FAST kinase domain-containing protein 2, mitochondrial，非常新颖，仅有少数基础研究。
2. 蛋白大小710 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYY8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118246-FASTKD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FASTKD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYY8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
