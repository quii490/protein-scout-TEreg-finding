---
type: protein-evaluation
gene: "FAM193B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM193B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM193B / IRIZIO, KIAA1931 |
| 蛋白名称 | Protein FAM193B |
| 蛋白大小 | 902 aa / 96.5 kDa |
| UniProt ID | Q96PV7 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM193B/IF_images/CACO-2_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM193B/IF_images/RT-4_1.jpg|RT-4]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 902 aa / 96.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029717, IPR031802; Pfam: PF15914 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IRIZIO, KIAA1931 |

**关键文献**:
1. Identification of Sex-Specific Genetic Variants Associated With Tau PET.. *Neurology. Genetics*. PMID: 36530928
2. Integrate single-cell and transcriptome analyses to explore the prognostic genes related to TRPM4 in bladder cancer.. *Frontiers in bioengineering and biotechnology*. PMID: 42052292
3. Interactions of cullin3/KCTD5 complexes with both cytoplasmic and nuclear proteins: Evidence for a role in protein stabilization.. *Biochemical and biophysical research communications*. PMID: 26188516

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.4 |
| 高置信度残基 (pLDDT>90) 占比 | 6.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 15.0% |
| 低置信 (pLDDT<50) 占比 | 65.4% |
| 有序区域 (pLDDT>70) 占比 | 19.6% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM193B/FAM193B-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=52.4），有序残基占 19.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029717, IPR031802; Pfam: PF15914 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRIM10 | 0.525 | 0.525 | — |
| CLASRP | 0.511 | 0.000 | — |
| PRR7 | 0.498 | 0.000 | — |
| KCTD5 | 0.480 | 0.292 | — |
| DDX41 | 0.465 | 0.000 | — |
| LRCH4 | 0.451 | 0.000 | — |
| ERICH5 | 0.448 | 0.000 | — |
| TMED9 | 0.446 | 0.000 | — |
| CUL3 | 0.431 | 0.292 | — |
| LRRC45 | 0.410 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LDOC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SPANXN2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GSK3B | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CNOT11 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRIM10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GOLGA2 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| TRIM23 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| TRIM27 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| ACP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:27107014|imex:IM-24995 |
| ENST00000514747 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 12
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.4 + PDB: 无 | pLDDT=52.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 11 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM193B — Protein FAM193B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小902 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=52.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96PV7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146067-FAM193B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM193B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96PV7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM193B/FAM193B-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96PV7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029717;IPR031802; |
| Pfam | PF15914; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000146067-FAM193B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CNOT11 | Intact | false |
| CUL3 | Biogrid | false |
| GSK3A | Biogrid | false |
| GSK3B | Biogrid | false |
| KCTD5 | Biogrid | false |
| SPANXN2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
