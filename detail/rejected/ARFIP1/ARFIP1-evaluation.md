---
type: protein-evaluation
gene: "ARFIP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ARFIP1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARFIP1 |
| 蛋白名称 | Arfaptin-1 |
| 蛋白大小 | 373 aa / 41.7 kDa |
| UniProt ID | P53367 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Golgi apparatus; Golgi apparatus, trans-Golgi network membra |
| 蛋白大小 | 10/10 | ×1 | 10 | 373 aa / 41.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027267, IPR010504, IPR030798; Pfam: PF06456 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Golgi apparatus; Golgi apparatus, trans-Golgi network membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi membrane (GO:0000139)
- trans-Golgi network membrane (GO:0032588)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Quantitative Proteomic and Metabolomic Profiling Reveals Altered Purine Metabolism in Acute Kidney Injury after On-Pump Coronary Artery Bypass Graft.. *Journal of proteome research*. PMID: 40549498
2. RNA-binding proteins potentially regulate alternative splicing of immune/inflammatory-associated genes during the progression of generalized pustular psoriasis.. *Archives of dermatological research*. PMID: 39158708
3. <italic>PDIA5</italic> and <italic>ARFIP1</italic> as Immunogenetic Biomarkers and Therapeutic Targets in Pancreatic Neuroendocrine Neoplasms: A Multi-Omics Study Integrating MR, Gene Expression Microarray, and Single-Cell Transcriptomics.. *Neuroendocrinology*. PMID: 41129479
4. Transcriptome analysis reveals modulation of differentially expressed genes in LPS-treated mouse macrophages (RAW264.7 cells) by grouper (Epinephelus coioides) Epinecidin-1.. *Fish & shellfish immunology*. PMID: 37327978
5. Inherited Spinocerebellar Ataxia Segregates with Intra-Familial Genetic Heterogeneity in a Consanguineous Pakistani Family: A Report of a Potential Novel Candidate Gene.. *DNA and cell biology*. PMID: 39506885

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.5 |
| 高置信度残基 (pLDDT>90) 占比 | 57.4% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 32.2% |
| 有序区域 (pLDDT>70) 占比 | 62.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=75.5，有序区 62.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027267, IPR010504, IPR030798; Pfam: PF06456 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARF6 | 0.914 | 0.160 | — |
| ARF3 | 0.907 | 0.638 | — |
| ARF1 | 0.899 | 0.527 | — |
| ARF5 | 0.861 | 0.317 | — |
| AKT1 | 0.835 | 0.000 | — |
| ARFIP2 | 0.785 | 0.768 | — |
| RAC1 | 0.688 | 0.075 | — |
| PICK1 | 0.606 | 0.420 | — |
| AMPH | 0.604 | 0.000 | — |
| TIGD4 | 0.591 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000395083.2 | psi-mi:"MI:0096"(pull down) | pubmed:22981988|imex:IM-27889 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| HSPA8 | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |
| BSND | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ARFIP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AFF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SYNGR3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RPRM | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TNFRSF10D | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.5 + PDB: 无 | pLDDT=75.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus; Golgi apparatus, trans-Golgi netw / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ARFIP1 — Arfaptin-1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小373 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P53367
- Protein Atlas: https://www.proteinatlas.org/search/ARFIP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARFIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P53367
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ARFIP1/IF_images/ARFIP1_IF_if_selected_60x60.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/ARFIP1/ARFIP1-PAE.png]]
