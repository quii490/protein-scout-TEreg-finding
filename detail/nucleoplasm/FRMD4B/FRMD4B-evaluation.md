---
type: protein-evaluation
gene: "FRMD4B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FRMD4B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FRMD4B / GRSP1, KIAA1013 |
| 蛋白名称 | FERM domain-containing protein 4B |
| 蛋白大小 | 1034 aa / 118.0 kDa |
| UniProt ID | Q9Y2L6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Centriolar satellite; 额外: Nucleoplasm, Golgi apparatus; UniProt: Cytoplasm, cytoskeleton; Cell junction, tight junction; Cell |
| 蛋白大小 | 8/10 | ×1 | 8 | 1034 aa / 118.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019749, IPR021774, IPR014352, IPR035963, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centriolar satellite; 额外: Nucleoplasm, Golgi apparatus | Approved |
| UniProt | Cytoplasm, cytoskeleton; Cell junction, tight junction; Cell junction, adherens junction | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- bicellular tight junction (GO:0005923)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- extracellular space (GO:0005615)
- ruffle (GO:0001726)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GRSP1, KIAA1013 |

**关键文献**:
1. Towards a transcriptomic biomarker for the classification of melanocytic neoplasms.. *PLoS genetics*. PMID: 41042798
2. Gene Identification for Ocular Congenital Cranial Motor Neuron Disorders Using Human Sequencing, Zebrafish Screening, and Protein Binding Microarrays.. *Investigative ophthalmology & visual science*. PMID: 40162949
3. Common variants in HSPB7 and FRMD4B associated with advanced heart failure.. *Circulation. Cardiovascular genetics*. PMID: 20124441
4. Unveiling novel macrophage-specific biomarkers in MASH through single-cell sequencing for diagnostic modeling.. *Journal of lipid research*. PMID: 42061510
5. Knocking Down FRMD4A, a Factor Associated with the Brain Development Disorder and a Risk Factor for Alzheimer's Disease, Using RNA-Targeting CRISPR/Cas13 Reveals Its Role in Cell Morphogenesis.. *International journal of molecular sciences*. PMID: 41155374

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.2 |
| 高置信度残基 (pLDDT>90) 占比 | 27.7% |
| 置信残基 (pLDDT 70-90) 占比 | 16.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 46.5% |
| 有序区域 (pLDDT>70) 占比 | 43.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.2），有序残基占 43.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019749, IPR021774, IPR014352, IPR035963, IPR019748; Pfam: PF11819, PF09380, PF00373 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYTH1 | 0.890 | 0.267 | — |
| CYTH3 | 0.872 | 0.114 | — |
| CYTH4 | 0.664 | 0.114 | — |
| CYTH2 | 0.645 | 0.114 | — |
| HSPB7 | 0.544 | 0.000 | — |
| TMTC4 | 0.519 | 0.000 | — |
| EOGT | 0.478 | 0.000 | — |
| GPA33 | 0.461 | 0.000 | — |
| PLEKHA5 | 0.461 | 0.094 | — |
| TMF1 | 0.453 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Crk | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Csk | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Inpp5d | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Ptpn6 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Syk | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Ptpn11 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Zap70 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Sh2b1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| AFDN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 13
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.2 + PDB: 无 | pLDDT=62.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cell junction, tight junc / Centriolar satellite; 额外: Nucleoplasm, Golgi appar | 一致 |
| PPI | STRING + IntAct | 14 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FRMD4B — FERM domain-containing protein 4B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1034 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2L6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114541-FRMD4B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FRMD4B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2L6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
