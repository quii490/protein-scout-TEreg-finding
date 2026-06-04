---
type: protein-evaluation
gene: "C9orf40"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C9orf40 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C9orf40 |
| 蛋白名称 | Uncharacterized protein C9orf40 |
| 蛋白大小 | 194 aa / 21.1 kDa |
| UniProt ID | Q8IXQ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Centrosome; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 194 aa / 21.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042349, IPR033461; Pfam: PF15017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Centrosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A multidimensional systems biology analysis of cellular senescence in aging and disease.. *Genome biology*. PMID: 32264951
2. Genome-wide Association Study of 24-Hour Urinary Excretion of Calcium, Magnesium, and Uric Acid.. *Mayo Clinic proceedings. Innovations, quality & outcomes*. PMID: 31993563
3. RORB gene and 9q21.13 microdeletion: report on a patient with epilepsy and mild intellectual disability.. *European journal of medical genetics*. PMID: 24355400

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 23.7% |
| 中等置信 (pLDDT 50-70) 占比 | 51.5% |
| 低置信 (pLDDT<50) 占比 | 24.7% |
| 有序区域 (pLDDT>70) 占比 | 23.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=59.4），有序残基占 23.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042349, IPR033461; Pfam: PF15017 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C18orf54 | 0.606 | 0.000 | — |
| CCDC150 | 0.568 | 0.000 | — |
| C3orf14 | 0.510 | 0.000 | — |
| HAUS4 | 0.510 | 0.000 | — |
| DONSON | 0.490 | 0.000 | — |
| DNAJB8 | 0.468 | 0.468 | — |
| CT62 | 0.447 | 0.000 | — |
| ANKRD62 | 0.447 | 0.000 | — |
| GTF3C4 | 0.441 | 0.000 | — |
| MGME1 | 0.403 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 10，IntAct interactions: 0
- 调控相关比例: 1 / 10 = 10%

**评价**: STRING 10 个预测互作，IntAct 0 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.4 + PDB: 无 | pLDDT=59.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol; 额外: Centrosome | 待确认 |
| PPI | STRING + IntAct | 10 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C9orf40 — Uncharacterized protein C9orf40，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小194 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXQ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135045-C9orf40/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C9orf40
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXQ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
