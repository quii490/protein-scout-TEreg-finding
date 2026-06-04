---
type: protein-evaluation
gene: "FAM149A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM149A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM149A |
| 蛋白名称 | Protein FAM149A |
| 蛋白大小 | 773 aa / 82.7 kDa |
| UniProt ID | A5PLN7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 773 aa / 82.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR022194, IPR039630; Pfam: PF12516 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genomic selection pressure discovery using site-frequency spectrum and reduced local variability statistics in Pakistani Dera-Din-Panah goat.. *Tropical animal health and production*. PMID: 37750990
2. Whole exome sequencing identified FAM149A as a plausible causative gene for congenital hereditary endothelial dystrophy, affecting Nrf2-Antioxidant signaling upon oxidative stress.. *Free radical biology & medicine*. PMID: 34303830
3. Prenatal diagnosis of a 4.5-Mb deletion at chromosome 4q35.1q35.2: Case report and literature review.. *Molecular cytogenetics*. PMID: 34794455
4. A Preliminary Genome-Wide Association Study of Acute Mountain Sickness Susceptibility in a Group of Nepalese Pilgrims Ascending to 4380 m.. *High altitude medicine & biology*. PMID: 26600424

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.2 |
| 高置信度残基 (pLDDT>90) 占比 | 3.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 17.2% |
| 低置信 (pLDDT<50) 占比 | 69.5% |
| 有序区域 (pLDDT>70) 占比 | 13.3% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=49.2），有序残基占 13.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022194, IPR039630; Pfam: PF12516 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TLR3 | 0.587 | 0.000 | — |
| TRIML1 | 0.583 | 0.000 | — |
| FRG1 | 0.581 | 0.000 | — |
| HAL | 0.541 | 0.000 | — |
| SORBS2 | 0.528 | 0.000 | — |
| CYP4V2 | 0.512 | 0.000 | — |
| FRG2 | 0.506 | 0.000 | — |
| STOX2 | 0.486 | 0.000 | — |
| CCDC110 | 0.485 | 0.000 | — |
| C4orf47 | 0.459 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TESC | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.2 + PDB: 无 | pLDDT=49.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus | 待确认 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FAM149A — Protein FAM149A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小773 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=49.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A5PLN7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109794-FAM149A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM149A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A5PLN7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
