---
type: protein-evaluation
gene: "FAM151B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM151B — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM151B |
| 蛋白名称 | Protein FAM151B |
| 蛋白大小 | 276 aa / 31.4 kDa |
| UniProt ID | Q6UXP7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 276 aa / 31.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019356; Pfam: PF10223 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- extracellular space (GO:0005615)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Fam151b, the mouse homologue of C.elegans menorin gene, is essential for retinal function.. *Scientific reports*. PMID: 31949211
2. A dendritic guidance receptor functions in both ligand dependent and independent modes.. *PLoS genetics*. PMID: 41348823
3. Dynamic genomic changes in methotrexate-resistant human cancer cell lines beyond DHFR amplification suggest potential new targets for preventing drug resistance.. *British journal of cancer*. PMID: 38594370
4. Identification of genes whose expression is altered by obesity throughout the arterial tree.. *Physiological genomics*. PMID: 25271210
5. A novel lncRNA FAM151B-DT regulates degradation of aggregation prone proteins.. *Molecular psychiatry*. PMID: 41053434

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.6 |
| 高置信度残基 (pLDDT>90) 占比 | 92.8% |
| 置信残基 (pLDDT 70-90) 占比 | 3.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 96.4% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.6，有序区 96.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019356; Pfam: PF10223 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZFYVE16 | 0.653 | 0.000 | — |
| LINGO3 | 0.518 | 0.288 | — |
| ARMC1 | 0.514 | 0.000 | — |
| PXMP4 | 0.512 | 0.000 | — |
| ANKRD34B | 0.507 | 0.000 | — |
| GTSF1L | 0.490 | 0.000 | — |
| NUDT22 | 0.490 | 0.000 | — |
| MRPL18 | 0.473 | 0.000 | — |
| BORCS8 | 0.426 | 0.000 | — |
| SEPTIN11 | 0.423 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIM15 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 1
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.6 + PDB: 无 | pLDDT=94.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol | 一致 |
| PPI | STRING + IntAct | 13 + 1 interactions | 数据充分 |

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
1. FAM151B — Protein FAM151B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小276 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UXP7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152380-FAM151B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM151B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UXP7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
