---
type: protein-evaluation
gene: "GLRX5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GLRX5 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLRX5 / C14orf87 |
| 蛋白名称 | Glutaredoxin-related protein 5, mitochondrial |
| 蛋白大小 | 157 aa / 16.6 kDa |
| UniProt ID | Q86SX6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion matrix |
| 蛋白大小 | 8/10 | ×1 | 8 | 157 aa / 16.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=68 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=82.3; PDB: 2MMZ, 2WUL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002109, IPR033658, IPR004480, IPR036249; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion matrix | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- dendrite (GO:0030425)
- iron-sulfur cluster assembly complex (GO:1990229)
- mitochondrial matrix (GO:0005759)
- mitochondrion (GO:0005739)
- neuronal cell body (GO:0043025)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 68 |
| PubMed broad count | 89 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf87 |

**关键文献**:
1. HACE1, GLRX5, and ELP2 gene variant cause spastic paraplegies.. *Acta neurologica Belgica*. PMID: 33813722
2. Functional Analysis of GLRX5 Mutants Reveals Distinct Functionalities of GLRX5 Protein.. *Journal of cellular biochemistry*. PMID: 26100117
3. Lipoic acid biosynthesis defects.. *Journal of inherited metabolic disease*. PMID: 24777537
4. GLRX5 is a prognostic marker in bladder cancer and correlates with activation of cancer-associated fibroblasts in the tumor microenvironment.. *Experimental cell research*. PMID: 41485701
5. GLRX5-associated [Fe-S] cluster biogenesis disorder: further characterisation of the neurological phenotype and long-term outcome.. *Orphanet journal of rare diseases*. PMID: 34732213

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.3 |
| 高置信度残基 (pLDDT>90) 占比 | 68.8% |
| 置信残基 (pLDDT 70-90) 占比 | 2.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 19.7% |
| 有序区域 (pLDDT>70) 占比 | 71.3% |
| 可用 PDB 条目 | 2MMZ, 2WUL |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2MMZ, 2WUL）+ AlphaFold高质量预测（pLDDT=82.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002109, IPR033658, IPR004480, IPR036249; Pfam: PF00462 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BOLA3 | 0.996 | 0.889 | — |
| BOLA1 | 0.987 | 0.840 | — |
| ISCA2 | 0.971 | 0.162 | — |
| ISCA1 | 0.959 | 0.000 | — |
| HSCB | 0.944 | 0.510 | — |
| SLC25A38 | 0.943 | 0.000 | — |
| GLRX | 0.920 | 0.000 | — |
| ISCU | 0.911 | 0.000 | — |
| NFS1 | 0.909 | 0.000 | — |
| BOLA2 | 0.905 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rasgrf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| VHL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| KEAP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EBI-6929338 | psi-mi:"MI:0018"(two hybrid) | pubmed:24136289|doi:10.1039/C3 |
| HSPD1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| MGST3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TRMT61B | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| NDUFS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| SPATA20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.3 + PDB: 2MMZ, 2WUL | pLDDT=82.3, v6 | 预测+实验 |
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

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GLRX5 — Glutaredoxin-related protein 5, mitochondrial，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小157 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 68 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86SX6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182512-GLRX5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLRX5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86SX6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
