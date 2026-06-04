---
type: protein-evaluation
gene: "C4orf47"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## C4orf47 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C4orf47 / C4orf47 |
| 蛋白名称 | Cilia-and flagella-associated protein 96 |
| 蛋白大小 | 309 aa / 34.4 kDa |
| UniProt ID | A7E2U8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Principal piece, End piece; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | ×1 | 10 | 309 aa / 34.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029358; Pfam: PF15239 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Principal piece, End piece | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 9+0 non-motile cilium (GO:0097731)
- centrosome (GO:0005813)
- cytoplasmic microtubule (GO:0005881)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C4orf47 |

**关键文献**:
1. C4orf47 contributes to the dormancy of pancreatic cancer under hypoxic conditions.. *Journal of Cancer*. PMID: 36741255
2. Proteomic analysis of mammalian sperm cells identifies new components of the centrosome.. *Journal of cell science*. PMID: 25074808

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.9 |
| 高置信度残基 (pLDDT>90) 占比 | 6.8% |
| 置信残基 (pLDDT 70-90) 占比 | 58.3% |
| 中等置信 (pLDDT 50-70) 占比 | 32.4% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 65.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=73.9，有序区 65.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029358; Pfam: PF15239 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC96 | 0.776 | 0.000 | — |
| C7orf31 | 0.694 | 0.000 | — |
| C5orf49 | 0.677 | 0.000 | — |
| CFAP299 | 0.670 | 0.000 | — |
| IQUB | 0.642 | 0.000 | — |
| EFCAB1 | 0.614 | 0.045 | — |
| ARMC3 | 0.603 | 0.000 | — |
| C9orf116 | 0.600 | 0.000 | — |
| CCDC38 | 0.581 | 0.000 | — |
| CCDC116 | 0.580 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CFAP96 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.9 + PDB: 无 | pLDDT=73.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Principal piece, End piece | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

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
1. C4orf47 — Cilia-and flagella-associated protein 96，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小309 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A7E2U8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205129-C4orf47/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C4orf47
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A7E2U8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
