---
type: protein-evaluation
gene: "FAM131C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM131C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM131C / C1orf117 |
| 蛋白名称 | Protein FAM131C |
| 蛋白大小 | 280 aa / 30.4 kDa |
| UniProt ID | Q96AQ9 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM131C/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM131C/IF_images/A-549_1.jpg|A-549]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Intermediate filaments, Cytosol; 额外: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 280 aa / 30.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026782; Pfam: PF15010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Intermediate filaments, Cytosol; 额外: Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf117 |

**关键文献**:
1. Genome-Wide Association Screening Determines Peripheral Players in Male Fertility Maintenance.. *International journal of molecular sciences*. PMID: 36613967
2. Bioinformatics analysis identifies PSMB8 as a key gene in the cutaneous malignant melanoma tumor microenvironment.. *Annals of translational medicine*. PMID: 36660621
3. DWH24: a new antibody for fluorescence-based cell death analysis.. *Methods and applications in fluorescence*. PMID: 37612784
4. Identification of Human N-Myristoylated Proteins from Human Complementary DNA Resources by Cell-Free and Cellular Metabolic Labeling Analyses.. *PloS one*. PMID: 26308446

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.9 |
| 高置信度残基 (pLDDT>90) 占比 | 8.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 45.4% |
| 低置信 (pLDDT<50) 占比 | 36.4% |
| 有序区域 (pLDDT>70) 占比 | 18.2% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM131C/FAM131C-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=57.9），有序残基占 18.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026782; Pfam: PF15010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HPCAL4 | 0.713 | 0.692 | — |
| TMEM82 | 0.654 | 0.000 | — |
| PRAMEF18 | 0.582 | 0.000 | — |
| PRAMEF7 | 0.574 | 0.000 | — |
| PPIAL4D | 0.570 | 0.000 | — |
| VSNL1 | 0.565 | 0.545 | — |
| NIPAL3 | 0.526 | 0.000 | — |
| HR | 0.523 | 0.000 | — |
| MAN1C1 | 0.502 | 0.000 | — |
| DRICH1 | 0.481 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VSNL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAD1L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GRN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DNAJA3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ENSP00000364814.4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| HPCAL4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NDN | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| LMO3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.9 + PDB: 无 | pLDDT=57.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Intermediate filaments, Cytosol; 额外: Nucleoli | 待确认 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM131C — Protein FAM131C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小280 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AQ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185519-FAM131C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM131C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AQ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM131C/FAM131C-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96AQ9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026782; |
| Pfam | PF15010; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185519-FAM131C/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GRN | Intact | false |
| HPCAL4 | Intact | false |
| LMO3 | Intact | false |
| NDN | Biogrid | false |
| VSNL1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
