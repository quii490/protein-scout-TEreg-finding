---
type: protein-evaluation
gene: "FAM229B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM229B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM229B / C6orf225 |
| 蛋白名称 | Protein FAM229B |
| 蛋白大小 | 80 aa / 8.7 kDa |
| UniProt ID | Q4G0N7 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM229B/IF_images/U-251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM229B/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 80 aa / 8.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028025; Pfam: PF14982 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf225 |

**关键文献**:
1. Learning-induced mRNA alterations in olfactory bulb mitral cells in neonatal rats.. *Learning & memory (Cold Spring Harbor, N.Y.)*. PMID: 32295841

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.5% |
| 中等置信 (pLDDT 50-70) 占比 | 80.0% |
| 低置信 (pLDDT<50) 占比 | 17.5% |
| 有序区域 (pLDDT>70) 占比 | 2.5% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM229B/FAM229B-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=56.1），有序残基占 2.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028025; Pfam: PF14982 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TSSK2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSSK1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 2
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.1 + PDB: 无 | pLDDT=56.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli, Golgi apparatus | 待确认 |
| PPI | STRING + IntAct | 0 + 2 interactions | 数据有限 |

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
1. FAM229B — Protein FAM229B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小80 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q4G0N7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000203778-FAM229B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM229B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4G0N7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM229B/FAM229B-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q4G0N7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028025; |
| Pfam | PF14982; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000203778-FAM229B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TSSK1B | Intact, Biogrid | true |
| TSSK2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
