---
type: protein-evaluation
gene: "SNURF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SNURF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SNURF / SNURF |
| 蛋白名称 | E3 ubiquitin-protein ligase RNF4 |
| 蛋白大小 | 190 aa / 21.3 kDa |
| UniProt ID | P78317 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Cytoplasm; Nucleus; Nucleus, PML body |
| 蛋白大小 | 8/10 | ×1 | 8 | 190 aa / 21.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=78 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=73.0; PDB: 2EA6, 2XEU, 4PPE |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043295, IPR047134, IPR001841, IPR013083, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Cytoplasm; Nucleus; Nucleus, PML body | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- microtubule end (GO:1990752)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 78 |
| PubMed broad count | 128 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SNURF |

**关键文献**:
1. Multigenerational exposure to DEHP drives dysregulation of imprinted gene Snurf to impair decidualization.. *Journal of hazardous materials*. PMID: 40267719
2. The RING finger protein SNURF is a bifunctional protein possessing DNA binding activity.. *The Journal of biological chemistry*. PMID: 11319220
3. Coregulator small nuclear RING finger protein (SNURF) enhances Sp1- and steroid receptor-mediated transcription by different mechanisms.. *The Journal of biological chemistry*. PMID: 10617653
4. Expression of SNURF-SNRPN upstream transcripts and epigenetic regulatory genes during human spermatogenesis.. *European journal of human genetics : EJHG*. PMID: 19471314
5. Small mosaic deletion encompassing the snoRNAs and SNURF-SNRPN results in an atypical Prader-Willi syndrome phenotype.. *American journal of medical genetics. Part A*. PMID: 24311433

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.0 |
| 高置信度残基 (pLDDT>90) 占比 | 30.5% |
| 置信残基 (pLDDT 70-90) 占比 | 13.2% |
| 中等置信 (pLDDT 50-70) 占比 | 50.0% |
| 低置信 (pLDDT<50) 占比 | 6.3% |
| 有序区域 (pLDDT>70) 占比 | 43.7% |
| 可用 PDB 条目 | 2EA6, 2XEU, 4PPE |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2EA6, 2XEU, 4PPE）+ AlphaFold高质量预测（pLDDT=73.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043295, IPR047134, IPR001841, IPR013083, IPR017907; Pfam: PF13639 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SNRPN | 0.961 | 0.000 | — |
| MKRN3 | 0.817 | 0.000 | — |
| NPAP1 | 0.647 | 0.000 | — |
| UBE3A | 0.616 | 0.000 | — |
| MAGEL2 | 0.602 | 0.000 | — |
| NDN | 0.601 | 0.000 | — |
| PEG3 | 0.598 | 0.058 | — |
| DIPK1B | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| cdsA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| UBE2D1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2L6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2T | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2W | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| RNF4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UEVLD | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 15
- 调控相关比例: 1 / 8 = 12%

**评价**: STRING 8 个预测互作，IntAct 15 个实验互作。调控相关配体占比 12%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.0 + PDB: 2EA6, 2XEU, 4PPE | pLDDT=73.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus, PML body / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 8 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SNURF — E3 ubiquitin-protein ligase RNF4，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 78 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78317
- Protein Atlas: https://www.proteinatlas.org/ENSG00000273173-SNURF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SNURF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78317
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
