---
type: protein-evaluation
gene: "GPD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPD1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPD1 |
| 蛋白名称 | Glycerol-3-phosphate dehydrogenase [NAD(+)], cytoplasmic |
| 蛋白大小 | 349 aa / 37.6 kDa |
| UniProt ID | P21695 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 349 aa / 37.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.4; PDB: 1WPQ, 1X0V, 1X0X, 6E8Y, 6E8Z, 6E90, 6PYP |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008927, IPR013328, IPR006168, IPR006109, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.4 |
| 高置信度残基 (pLDDT>90) 占比 | 94.6% |
| 置信残基 (pLDDT 70-90) 占比 | 4.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.5% |
| 可用 PDB 条目 | 1WPQ, 1X0V, 1X0X, 6E8Y, 6E8Z, 6E90, 6PYP |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1WPQ, 1X0V, 1X0X, 6E8Y, 6E8Z, 6E90, 6PYP）+ AlphaFold极高置信度预测（pLDDT=96.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008927, IPR013328, IPR006168, IPR006109, IPR017751; Pfam: PF07479, PF01210 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPD2 | 0.997 | 0.093 | — |
| GPAM | 0.972 | 0.000 | — |
| GNPAT | 0.967 | 0.000 | — |
| GPAT2 | 0.959 | 0.000 | — |
| GPAT3 | 0.942 | 0.000 | — |
| GPD1L | 0.942 | 0.411 | — |
| GPAT4 | 0.932 | 0.000 | — |
| AGPAT2 | 0.904 | 0.000 | — |
| ADPRM | 0.902 | 0.000 | — |
| AGPAT3 | 0.892 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COP1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| ACC1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| AAP1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| IMD4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| APA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| TDH1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| GND1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16284124 |
| PTN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| POMP | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| GCN5 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-15346|pubmed:21734642 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.4 + PDB: 1WPQ, 1X0V, 1X0X, 6E8Y, 6E8Z,  | pLDDT=96.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPD1 — Glycerol-3-phosphate dehydrogenase [NAD(+)], cytoplasmic，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小349 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P21695
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167588-GPD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P21695
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
