---
type: protein-evaluation
gene: "HLF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HLF — REJECTED (研究热度过高 (PubMed strict=647，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HLF |
| 蛋白名称 | Hepatic leukemia factor |
| 蛋白大小 | 295 aa / 33.2 kDa |
| UniProt ID | Q16534 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 295 aa / 33.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=647 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347, IPR040223; Pfam: PF07716 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 647 |
| PubMed broad count | 1342 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Effect of Low-Fat vs Low-Carbohydrate Diet on 12-Month Weight Loss in Overweight Adults and the Association With Genotype Pattern or Insulin Secretion: The DIETFITS Randomized Clinical Trial.. *JAMA*. PMID: 29466592
2. Lung extracellular matrix modulates KRT5(+) basal cell activity in pulmonary fibrosis.. *Nature communications*. PMID: 37758700
3. Astrocyte-derived lactoferrin inhibits neuronal ferroptosis by reducing iron content and GPX4 degradation in APP/PS1 transgenic mice.. *Pharmacological research*. PMID: 39306020
4. Cellular and Molecular Mechanisms of Hypertrophy of Ligamentum Flavum.. *Biomolecules*. PMID: 39456209
5. HLF promotes ovarian cancer progression and chemoresistance via regulating Hippo signaling pathway.. *Cell death & disease*. PMID: 37709768

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.8 |
| 高置信度残基 (pLDDT>90) 占比 | 39.0% |
| 置信残基 (pLDDT 70-90) 占比 | 14.2% |
| 中等置信 (pLDDT 50-70) 占比 | 19.7% |
| 低置信 (pLDDT<50) 占比 | 27.1% |
| 有序区域 (pLDDT>70) 占比 | 53.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=71.8，有序区 53.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347, IPR040223; Pfam: PF07716 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TLE6 | 0.788 | 0.000 | — |
| NFIL3 | 0.767 | 0.510 | — |
| TLE2 | 0.766 | 0.000 | — |
| SRPX2 | 0.760 | 0.000 | — |
| TCF3 | 0.748 | 0.000 | — |
| ANXA8 | 0.715 | 0.051 | — |
| TFPT | 0.697 | 0.000 | — |
| ARNTL | 0.672 | 0.090 | — |
| PRCC | 0.651 | 0.000 | — |
| CRY1 | 0.629 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DBP | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| sbcB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| pheS | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| recJ | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000226067.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| gatA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Bmal1 | psi-mi:"MI:0018"(two hybrid) | pubmed:9704006|imex:IM-20272 |
| ARNT | psi-mi:"MI:0018"(two hybrid) | pubmed:9704006|imex:IM-20272 |
| ggt | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ttr | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.8 + PDB: 无 | pLDDT=71.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. HLF — Hepatic leukemia factor，研究基础较多，新颖性有限。
2. 蛋白大小295 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 647 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 647 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16534
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108924-HLF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HLF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16534
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
