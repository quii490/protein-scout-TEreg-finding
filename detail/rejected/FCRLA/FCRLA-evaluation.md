---
type: protein-evaluation
gene: "FCRLA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FCRLA — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FCRLA / FCRL, FCRL1, FCRLM1, FCRX, FREB |
| 蛋白名称 | Fc receptor-like A |
| 蛋白大小 | 359 aa / 38.9 kDa |
| UniProt ID | Q7L513 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 359 aa / 38.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=75.2; PDB: 4HWN |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007110, IPR036179, IPR013783, IPR050488, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **97.0/180** | |
| **归一化总分** | | | **53.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- external side of plasma membrane (GO:0009897)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FCRL, FCRL1, FCRLM1, FCRX, FREB |

**关键文献**:
1. Differential expression of FCRLA in naïve and activated mouse B cells.. *Cellular immunology*. PMID: 22078318
2. B cell-specific protein FCRLA is expressed by plasmacytoid dendritic cells in humans.. *Cytometry. Part B, Clinical cytometry*. PMID: 29236355
3. Characterization of human FCRLA isoforms.. *Immunology letters*. PMID: 23742757
4. TNFα activation of the PLEKHA5-FCRLA axis disturbs lipid metabolism, leading to the progression of cutaneous malignant melanoma.. *Lipids in health and disease*. PMID: 40462127
5. FCRLA is a resident endoplasmic reticulum protein that associates with intracellular Igs, IgM, IgG and IgA.. *International immunology*. PMID: 21149418

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 47.4% |
| 置信残基 (pLDDT 70-90) 占比 | 18.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.5% |
| 低置信 (pLDDT<50) 占比 | 25.1% |
| 有序区域 (pLDDT>70) 占比 | 65.5% |
| 可用 PDB 条目 | 4HWN |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=75.2，有序区 65.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007110, IPR036179, IPR013783, IPR050488, IPR003599; Pfam: PF13895 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD19 | 0.931 | 0.000 | — |
| VPREB3 | 0.886 | 0.126 | — |
| BLK | 0.855 | 0.102 | — |
| CD79A | 0.823 | 0.000 | — |
| MS4A1 | 0.800 | 0.092 | — |
| NIBAN3 | 0.780 | 0.000 | — |
| MEIS1 | 0.766 | 0.000 | — |
| CD79B | 0.761 | 0.000 | — |
| HOXA9 | 0.718 | 0.000 | — |
| NUP98 | 0.718 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Traf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| A0A0G2RQ53 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| aspA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| tap | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0F7R924 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SNUPN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 4HWN | pLDDT=75.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FCRLA — Fc receptor-like A，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小359 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L513
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132185-FCRLA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FCRLA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L513
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
