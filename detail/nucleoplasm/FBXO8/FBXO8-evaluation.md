---
type: protein-evaluation
gene: "FBXO8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO8 / FBS, FBX8 |
| 蛋白名称 | F-box only protein 8 |
| 蛋白大小 | 319 aa / 37.1 kDa |
| UniProt ID | Q9NRD0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 319 aa / 37.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810, IPR048003, IPR023394, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBS, FBX8 |

**关键文献**:
1. Bilaterally cleft lip and bilateral thumb polydactyly with triphalangeal component in a patient with two de novo deletions of HSA 4q32 and 4q34 involving PDGFC, GRIA2, and FBXO8 genes.. *American journal of medical genetics. Part A*. PMID: 24038848
2. FBXO8 is a novel prognostic biomarker in different molecular subtypes of breast cancer and suppresses breast cancer progression by targeting c-MYC.. *Biochimica et biophysica acta. General subjects*. PMID: 38301858
3. Ubiquitination and ALL: Identifying FBXO8 as a prognostic biomarker and therapeutic target.. *Frontiers in immunology*. PMID: 40375984
4. Diagnostic and prognostic potential of FBXO8 expression in kidney renal clear cell carcinoma and its regulation of renal adenocarcinoma cells.. *Cancer genetics*. PMID: 39647237
5. Posttranscriptional Repression of FBXW7 and FBXO8 by microRNA-223 Regulates Ubiquitin-dependent Proteostasis in Periodontal Disease.. *Contemporary clinical dentistry*. PMID: 41953918

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.3 |
| 高置信度残基 (pLDDT>90) 占比 | 60.8% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 15.7% |
| 有序区域 (pLDDT>70) 占比 | 78.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=81.3，有序区 78.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR048003, IPR023394, IPR000904; Pfam: PF12937, PF01369 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.784 | 0.510 | — |
| ATG4A | 0.783 | 0.000 | — |
| CCNF | 0.684 | 0.000 | — |
| ARF6 | 0.617 | 0.356 | — |
| CEP44 | 0.609 | 0.000 | — |
| NXT2 | 0.608 | 0.000 | — |
| NSL1 | 0.595 | 0.053 | — |
| KRT18 | 0.553 | 0.093 | — |
| MYC | 0.551 | 0.510 | — |
| TMEM107 | 0.547 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SH3GLB2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| BIN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIP13 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |
| CDK16 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25032|pubmed:22184064 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.3 + PDB: 无 | pLDDT=81.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBXO8 — F-box only protein 8，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小319 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRD0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164117-FBXO8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRD0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
