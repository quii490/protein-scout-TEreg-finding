---
type: protein-evaluation
gene: "CNST"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CNST — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNST / C1orf71 |
| 蛋白名称 | Consortin |
| 蛋白大小 | 725 aa / 79.6 kDa |
| UniProt ID | Q6PJW8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Vesicles; UniProt: Cell membrane; Golgi apparatus, trans-Golgi network membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 725 aa / 79.6 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=52.3; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR042318, IPR028129, IPR054132; Pfam: PF15281, PF |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Supported |
| UniProt | Cell membrane; Golgi apparatus, trans-Golgi network membrane; Cytoplasmic vesicle, secretory vesicle | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)
- protein-containing complex (GO:0032991)
- trans-Golgi network (GO:0005802)
- transport vesicle (GO:0030133)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) |  |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.3 |
| 高置信度残基 (pLDDT>90) 占比 | 6.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.1% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 65.1% |
| 有序区域 (pLDDT>70) 占比 | 22.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=52.3），有序残基占 22.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042318, IPR028129, IPR054132; Pfam: PF15281, PF22883 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATP6V1F | 0.986 | 0.835 | — |
| ATP6V1A | 0.975 | 0.745 | — |
| ATP6V1B2 | 0.975 | 0.745 | — |
| ATP6V1B1 | 0.975 | 0.745 | — |
| ATP6V1E1 | 0.975 | 0.746 | — |
| ATP6V1E2 | 0.975 | 0.746 | — |
| LIM2 | 0.975 | 0.745 | — |
| ATP6V0D1 | 0.974 | 0.747 | — |
| ATP6V0D2 | 0.974 | 0.747 | — |
| ATP6V0C | 0.971 | 0.841 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.3 + PDB: 无 | pLDDT=52.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Golgi apparatus, trans-Golgi networ / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CNST -- Consortin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小725 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=52.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PJW8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162852-CNST/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNST
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PJW8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
