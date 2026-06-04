---
type: protein-evaluation
gene: "DPP8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DPP8 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=230，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPP8 |
| 蛋白名称 | Dipeptidyl peptidase 8 |
| 蛋白大小 | 898 aa / 103.4 kDa |
| UniProt ID | Q6V1X1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 898 aa / 103.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=230 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.4; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **62.5/180** | |
| **归一化总分** | | | **34.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 230 |
| PubMed broad count | 249 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Polygenic risk score for lower limb skeletal muscle mass and its interaction with protein and vitamin D intake in older adults.. *Nutrition*. PMID: 41616609
2. Identification of potential diagnostic and therapeutic apoptosis-related casual targets for osteoporosis: an integrated multi-omics analysis.. *J Bone Miner Metab*. PMID: 41870631
3. MST1 promotes microglial pyroptosis and neuroinflammation in alzheimer's disease by regulating the novel DPP8/NLRP1/Caspase-1/GSDMD-N axis.. *J Neuroinflammation*. PMID: 41689046
4. Proximity labeling reveals non-catalytic interactions between DPP9 and ubiquitin signaling complexes.. *Cell Mol Life Sci*. PMID: 41636814
5. Alogliptin.. **. PMID: 29939586

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.4 |
| 高置信度残基 (pLDDT>90) 占比 | 79.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 93.0% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.4，有序区 93.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PREP | 0.000 | 0.000 | — |
| SUMO1 | 0.000 | 0.000 | — |
| DPP7 | 0.000 | 0.000 | — |
| TFDP3 | 0.000 | 0.000 | — |
| HRK | 0.000 | 0.000 | — |
| APC | 0.000 | 0.000 | — |
| VPS50 | 0.000 | 0.000 | — |
| CARD8 | 0.000 | 0.000 | — |
| GCG | 0.000 | 0.000 | — |
| NLRP1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q16623 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q6V1X1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q13671 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |
| uniprotkb:A5PL33 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P09382 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P0CG47 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P17707 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q09019 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6NSI4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q86TI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.4 + PDB: 无 | pLDDT=90.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DPP8 — Dipeptidyl peptidase 8，研究基础较多，新颖性有限。
2. 蛋白大小898 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 230 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6V1X1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000074603-DPP8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPP8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6V1X1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
