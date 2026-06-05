---
type: protein-evaluation
gene: "GJA8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GJA8 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=145，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GJA8 |
| 蛋白名称 | Gap junction alpha-8 protein |
| 蛋白大小 | 433 aa / 48.2 kDa |
| UniProt ID | P48165 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell junction, gap junction |
| 蛋白大小 | 10/10 | ×1 | 10 | 433 aa / 48.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=145 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000500, IPR002266, IPR019570, IPR017990, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **60.0/180** | |
| **归一化总分** | | | **33.3/100** | |

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

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 145 |
| PubMed broad count | 179 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. 1q21.1 Recurrent Deletion.. **. PMID: 21348049
2. Charged multivesicular body protein 4b forms complexes with gap junction proteins during lens fiber cell differentiation.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 36880430
3. GJA8-associated developmental eye disorders: a new multicentre study highlights mutational hotspots and genotype-phenotype correlations.. *European journal of human genetics : EJHG*. PMID: 40301690
4. Different GJA8 missense variants reveal distinct pathogenic mechanisms in congenital cataract.. *Life sciences*. PMID: 40158616
5. Genetic association of GJA8 with long-segment Hirschsprung's disease in southern Chinese children.. *Translational pediatrics*. PMID: 39263294

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.9 |
| 高置信度残基 (pLDDT>90) 占比 | 30.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 47.6% |
| 有序区域 (pLDDT>70) 占比 | 48.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.9），有序残基占 48.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000500, IPR002266, IPR019570, IPR017990, IPR013092; Pfam: PF00029, PF03509 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GJA3 | 0.995 | 0.000 | — |
| MIP | 0.959 | 0.099 | — |
| GJB2 | 0.956 | 0.080 | — |
| BFSP2 | 0.946 | 0.000 | — |
| CRYGD | 0.938 | 0.000 | — |
| CRYBB2 | 0.936 | 0.000 | — |
| CRYBB1 | 0.927 | 0.000 | — |
| CRYGS | 0.922 | 0.000 | — |
| GJA1 | 0.907 | 0.161 | — |
| GJD3 | 0.906 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MIP | psi-mi:"MI:0096"(pull down) | pubmed:15802270 |
| CCDC167 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PMP22 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KIR2DL3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| UBXN8 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TMEM239 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CYBC1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TMEM60 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SEC22B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TMEM242 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.9 + PDB: 无 | pLDDT=64.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, gap junction / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GJA8 — Gap junction alpha-8 protein，研究基础较多，新颖性有限。
2. 蛋白大小433 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 145 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P48165
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121634-GJA8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GJA8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P48165
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P48165-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
