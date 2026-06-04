---
type: protein-evaluation
gene: "FAM149B1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FAM149B1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM149B1 / KIAA0974 |
| 蛋白名称 | Primary cilium assembly protein FAM149B1 |
| 蛋白大小 | 582 aa / 64.6 kDa |
| UniProt ID | Q96BN6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Microtubules, Primary cilium; 额外: Cytosol; UniProt: Cell projection, cilium |
| 蛋白大小 | 10/10 | ×1 | 10 | 582 aa / 64.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR022194, IPR039630; Pfam: PF12516 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules, Primary cilium; 额外: Cytosol | Approved |
| UniProt | Cell projection, cilium | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cilium (GO:0005929)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0974 |

**关键文献**:
1. BROMI/TBC1D32 together with CCRK/CDK20 and FAM149B1/JBTS36 contributes to intraflagellar transport turnaround involving ICK/CILK1.. *Molecular biology of the cell*. PMID: 35609210
2. Comprehensive Proteomics and Machine Learning Analysis to Distinguish Follicular Adenoma and Follicular Thyroid Carcinoma from Indeterminate Thyroid Nodules.. *Endocrinology and metabolism (Seoul, Korea)*. PMID: 40205804
3. xbx-4, a homolog of the Joubert syndrome gene FAM149B1, acts via the CCRK and RCK kinase cascade to regulate cilia morphology.. *Current biology : CB*. PMID: 34731674
4. Screening the hub genes and analyzing the mechanisms in discharged COVID-19 patients retesting positive through bioinformatics analysis.. *Journal of clinical laboratory analysis*. PMID: 35657140
5. Bi-allelic Mutations in FAM149B1 Cause Abnormal Primary Cilium and a Range of Ciliopathy Phenotypes in Humans.. *American journal of human genetics*. PMID: 30905400

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.0 |
| 高置信度残基 (pLDDT>90) 占比 | 5.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.8% |
| 中等置信 (pLDDT 50-70) 占比 | 21.5% |
| 低置信 (pLDDT<50) 占比 | 62.5% |
| 有序区域 (pLDDT>70) 占比 | 16.0% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=52.0），有序残基占 16.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022194, IPR039630; Pfam: PF12516 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNAJC9 | 0.967 | 0.000 | — |
| TBC1D32 | 0.886 | 0.831 | — |
| CFAP20 | 0.826 | 0.785 | — |
| DNAJB4 | 0.555 | 0.000 | — |
| HAL | 0.541 | 0.000 | — |
| LRRC69 | 0.479 | 0.000 | — |
| ENOX2 | 0.471 | 0.000 | — |
| C21orf62 | 0.470 | 0.000 | — |
| TMEM260 | 0.465 | 0.000 | — |
| NEU1 | 0.451 | 0.217 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TBC1D32 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TESC | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| CFAP20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NPW | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.0 + PDB: 无 | pLDDT=52.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium / Microtubules, Primary cilium; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FAM149B1 — Primary cilium assembly protein FAM149B1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小582 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=52.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96BN6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138286-FAM149B1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM149B1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BN6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
