---
type: protein-evaluation
gene: "GPRC5D"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPRC5D — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=119，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPRC5D |
| 蛋白名称 | G-protein coupled receptor family C group 5 member D |
| 蛋白大小 | 345 aa / 38.8 kDa |
| UniProt ID | Q9NZD1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 345 aa / 38.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=119 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=76.0; PDB: 8YZK, 9IMA |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017978, IPR051753; Pfam: PF00003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **70.0/180** | |
| **归一化总分** | | | **38.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- plasma membrane (GO:0005886)
- receptor complex (GO:0043235)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 119 |
| PubMed broad count | 275 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Talquetamab, a T-Cell-Redirecting GPRC5D Bispecific Antibody for Multiple Myeloma.. *The New England journal of medicine*. PMID: 36507686
2. Mechanisms of antigen escape from BCMA- or GPRC5D-targeted immunotherapies in multiple myeloma.. *Nature medicine*. PMID: 37653344
3. Targeting GPRC5D for multiple myeloma therapy.. *Journal of hematology & oncology*. PMID: 39342286
4. GPRC5D is a target for the immunotherapy of multiple myeloma with rationally designed CAR T cells.. *Science translational medicine*. PMID: 30918115
5. Current Novel Targeted Therapeutic Strategies in Multiple Myeloma.. *International journal of molecular sciences*. PMID: 38892379

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 44.6% |
| 置信残基 (pLDDT 70-90) 占比 | 23.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 22.6% |
| 有序区域 (pLDDT>70) 占比 | 67.8% |
| 可用 PDB 条目 | 8YZK, 9IMA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8YZK, 9IMA）+ AlphaFold高质量预测（pLDDT=76.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017978, IPR051753; Pfam: PF00003 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FCRL5 | 0.829 | 0.091 | — |
| CEP70 | 0.705 | 0.000 | — |
| SLAMF7 | 0.696 | 0.000 | — |
| TNFRSF17 | 0.596 | 0.000 | — |
| CD38 | 0.560 | 0.000 | — |
| SDC1 | 0.532 | 0.000 | — |
| CCL4 | 0.507 | 0.095 | — |
| KRTAP3-1 | 0.479 | 0.000 | — |
| GPR156 | 0.476 | 0.000 | — |
| TNFRSF13B | 0.469 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ERMP1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FXYD3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| APOL3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TMEM208 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM120B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PRRT2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EMP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PMP22 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC66A1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 8YZK, 9IMA | pLDDT=76.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. GPRC5D — G-protein coupled receptor family C group 5 member D，研究基础较多，新颖性有限。
2. 蛋白大小345 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 119 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZD1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111291-GPRC5D/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPRC5D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZD1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NZD1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
