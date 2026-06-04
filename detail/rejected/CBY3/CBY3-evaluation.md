---
type: protein-evaluation
gene: "CBY3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CBY3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CBY3 |
| 蛋白名称 | Sperm annulus positioning complex subunit Chibby3 |
| 蛋白大小 | 242 aa / 27.3 kDa |
| UniProt ID | A6NI87 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell projection, cilium, flagellum |
| 蛋白大小 | 10/10 | ×1 | 10 | 242 aa / 27.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028118; Pfam: PF14645 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- sperm annulus (GO:0097227)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The Cby3/ciBAR1 complex positions the annulus along the sperm flagellum during spermiogenesis.. *The Journal of cell biology*. PMID: 38197861
2. Metagenomic and metatranscriptomic profiling of bronchoalveolar lavage fluid identifies microbial and host biomarkers of drug-resistant tuberculosis.. *Frontiers in cellular and infection microbiology*. PMID: 41693862

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.6 |
| 高置信度残基 (pLDDT>90) 占比 | 16.5% |
| 置信残基 (pLDDT 70-90) 占比 | 29.8% |
| 中等置信 (pLDDT 50-70) 占比 | 28.1% |
| 低置信 (pLDDT<50) 占比 | 25.6% |
| 有序区域 (pLDDT>70) 占比 | 46.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.6），有序残基占 46.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028118; Pfam: PF14645 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CBY2 | 0.708 | 0.000 | — |
| SAXO1 | 0.494 | 0.000 | — |
| ADAD2 | 0.491 | 0.000 | — |
| ADGRL1 | 0.473 | 0.469 | — |
| ADGRL3 | 0.473 | 0.469 | — |
| ADGRL2 | 0.473 | 0.469 | — |
| ANKRD31 | 0.472 | 0.000 | — |
| GNAS | 0.437 | 0.383 | — |
| GNAL | 0.437 | 0.383 | — |
| MEIOB | 0.421 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 12，IntAct interactions: 0
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.6 + PDB: 无 | pLDDT=67.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 12 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CBY3 — Sperm annulus positioning complex subunit Chibby3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小242 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NI87
- Protein Atlas: https://www.proteinatlas.org/search/CBY3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CBY3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NI87
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CBY3/CBY3-PAE.png]]
