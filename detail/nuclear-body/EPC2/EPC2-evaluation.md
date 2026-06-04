---
type: protein-evaluation
gene: "EPC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EPC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EPC2 |
| 蛋白名称 | Enhancer of polycomb homolog 2 |
| 蛋白大小 | 807 aa / 91.1 kDa |
| UniProt ID | Q52LR7 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EPC2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EPC2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 807 aa / 91.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024943, IPR019542, IPR009607; Pfam: PF06752, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- NuA4 histone acetyltransferase complex (GO:0035267)
- nucleosome (GO:0000786)
- nucleus (GO:0005634)
- piccolo histone acetyltransferase complex (GO:0032777)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 92 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Detergent exposure induces epithelial barrier dysfunction and eosinophilic inflammation in the esophagus.. *Allergy*. PMID: 35899466
2. IL-13-induced STAT3-dependent signaling networks regulate esophageal epithelial proliferation in eosinophilic esophagitis.. *The Journal of allergy and clinical immunology*. PMID: 37652141
3. Modelling Barrett's oesophagus.. *Biochemical Society transactions*. PMID: 20298176
4. Enhancers of Polycomb EPC1 and EPC2 sustain the oncogenic potential of MLL leukemia stem cells.. *Leukemia*. PMID: 24166297
5. Autophagy mitigates ethanol-induced mitochondrial dysfunction and oxidative stress in esophageal keratinocytes.. *PloS one*. PMID: 32966340

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.0 |
| 高置信度残基 (pLDDT>90) 占比 | 13.3% |
| 置信残基 (pLDDT 70-90) 占比 | 21.4% |
| 中等置信 (pLDDT 50-70) 占比 | 15.6% |
| 低置信 (pLDDT<50) 占比 | 49.7% |
| 有序区域 (pLDDT>70) 占比 | 34.7% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EPC2/EPC2-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=57.0），有序残基占 34.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024943, IPR019542, IPR009607; Pfam: PF06752, PF10513 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEAF6 | 0.998 | 0.959 | — |
| TRRAP | 0.997 | 0.963 | — |
| DMAP1 | 0.997 | 0.912 | — |
| ING3 | 0.993 | 0.902 | — |
| YEATS4 | 0.993 | 0.943 | — |
| MORF4L1 | 0.991 | 0.912 | — |
| MRGBP | 0.991 | 0.918 | — |
| KAT5 | 0.987 | 0.910 | — |
| ACTL6A | 0.983 | 0.810 | — |
| BRD8 | 0.983 | 0.624 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RUVBL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| MRGBP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| VPS72 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15647280 |
| ACTL6A | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:15647280 |
| Myc | psi-mi:"MI:0096"(pull down) | pubmed:20946988|imex:IM-15160 |
| Dmap1 | psi-mi:"MI:0096"(pull down) | pubmed:20946988|imex:IM-15160 |
| Kat5 | psi-mi:"MI:0096"(pull down) | pubmed:20946988|imex:IM-15160 |
| CEP63 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| MBTD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27153538|imex:IM-27061 |
| KSR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.0 + PDB: 无 | pLDDT=57.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EPC2 — Enhancer of polycomb homolog 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小807 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q52LR7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135999-EPC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EPC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q52LR7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/EPC2/EPC2-PAE.png]]




