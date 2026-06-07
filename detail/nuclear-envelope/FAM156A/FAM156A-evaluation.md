---
type: protein-evaluation
gene: "FAM156A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM156A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM156A / TMEM29 |
| 蛋白名称 | Protein FAM156A/FAM156B |
| 蛋白大小 | 213 aa / 24.4 kDa |
| UniProt ID | Q8NDB6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 213 aa / 24.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029096; Pfam: PF15549 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 5 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TMEM29 |

**关键文献**:
1. Gene expression signature of non-involved lung tissue associated with survival in lung adenocarcinoma patients.. *Carcinogenesis*. PMID: 23978379
2. A computational approach to candidate gene prioritization for X-linked mental retardation using annotation-based binary filtering and motif-based linear discriminatory analysis.. *Biology direct*. PMID: 21668950

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.7 |
| 高置信度残基 (pLDDT>90) 占比 | 16.0% |
| 置信残基 (pLDDT 70-90) 占比 | 25.8% |
| 中等置信 (pLDDT 50-70) 占比 | 35.7% |
| 低置信 (pLDDT<50) 占比 | 22.5% |
| 有序区域 (pLDDT>70) 占比 | 41.8% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/FAM156A/FAM156A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=66.7），有序残基占 41.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029096; Pfam: PF15549 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBM41 | 0.479 | 0.000 | — |
| TMEM164 | 0.463 | 0.000 | — |
| TMEM120A | 0.428 | 0.000 | — |
| SLX1B | 0.404 | 0.000 | — |
| DYDC2 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAGEA11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GADD45G | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FAM156B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CRACR2A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ATRIP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| TFIP11 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| SAT1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| TEX11 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 5，IntAct interactions: 8
- 调控相关比例: 0 / 5 = 0%

**评价**: STRING 5 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.7 + PDB: 无 | pLDDT=66.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 5 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM156A — Protein FAM156A/FAM156B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小213 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NDB6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000268350-FAM156A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM156A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDB6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/FAM156A/FAM156A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NDB6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029096; |
| Pfam | PF15549; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000268350-FAM156A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATRIP | Intact | false |
| CRACR2A | Intact | false |
| GADD45G | Intact | false |
| SAT1 | Intact | false |
| TEX11 | Intact | false |
| TFIP11 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
