---
type: protein-evaluation
gene: "GPR62"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR62 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR62 |
| 蛋白名称 | G-protein coupled receptor 62 |
| 蛋白大小 | 368 aa / 37.6 kDa |
| UniProt ID | Q9BZJ7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Endosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 368 aa / 37.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000276, IPR017452; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Endosome membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endosome (GO:0005768)
- endosome membrane (GO:0010008)
- plasma membrane (GO:0005886)
- receptor complex (GO:0043235)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Constitutive Activity among Orphan Class-A G Protein Coupled Receptors.. *PloS one*. PMID: 26384023
2. Orphan G Protein Coupled Receptors in Affective Disorders.. *Genes*. PMID: 32599826
3. Orphan GPR61, GPR62 and GPR135 receptors and the melatonin MT(2) receptor reciprocally modulate their signaling functions.. *Scientific reports*. PMID: 28827538
4. The oligodendrocyte-enriched orphan G protein-coupled receptor Gpr62 is dispensable for central nervous system myelination.. *Neural development*. PMID: 34844642
5. Orphan G Protein-Coupled Receptors: A Novel Research Frontier in Autism and Associated Disorders.. *Archiv der Pharmazie*. PMID: 40538218

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.5 |
| 高置信度残基 (pLDDT>90) 占比 | 35.6% |
| 置信残基 (pLDDT 70-90) 占比 | 30.2% |
| 中等置信 (pLDDT 50-70) 占比 | 22.0% |
| 低置信 (pLDDT<50) 占比 | 12.2% |
| 有序区域 (pLDDT>70) 占比 | 65.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=76.5，有序区 65.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452; Pfam: PF00001 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPER1 | 0.909 | 0.000 | — |
| GPR135 | 0.633 | 0.000 | — |
| GPR26 | 0.604 | 0.000 | — |
| GPR162 | 0.584 | 0.000 | — |
| GPR52 | 0.523 | 0.000 | — |
| OPALIN | 0.515 | 0.000 | — |
| GPR25 | 0.509 | 0.000 | — |
| GPR50 | 0.498 | 0.000 | — |
| GPR101 | 0.498 | 0.000 | — |
| GPR45 | 0.495 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RAMP2 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP1 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP3 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.5 + PDB: 无 | pLDDT=76.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Endosome membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

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
1. GPR62 — G-protein coupled receptor 62，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小368 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZJ7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180929-GPR62/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR62
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZJ7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
