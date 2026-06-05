---
type: protein-evaluation
gene: "FBXO15"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXO15 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO15 / FBX15 |
| 蛋白名称 | F-box only protein 15 |
| 蛋白大小 | 510 aa / 57.3 kDa |
| UniProt ID | Q8NCQ5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 510 aa / 57.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810; Pfam: PF12937 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX15 |

**关键文献**:
1. Gastrodin reduces Aβ brain levels in an Alzheimer's disease mouse model by inhibiting P-glycoprotein ubiquitination.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 39541666
2. Generation of germline-competent induced pluripotent stem cells.. *Nature*. PMID: 17554338
3. Genome-to-genome analysis reveals associations between human and mycobacterial genetic variation in tuberculosis patients from Tanzania.. *BMC medical genomics*. PMID: 40457403
4. FBXO15 regulates P-glycoprotein/ABCB1 expression through the ubiquitin--proteasome pathway in cancer cells.. *Cancer science*. PMID: 23465077
5. Ubiquitination-Related miRNA-mRNA Interaction Is a Potential Mechanism in the Progression of Retinoblastoma.. *Investigative ophthalmology & visual science*. PMID: 34347012

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.6 |
| 高置信度残基 (pLDDT>90) 占比 | 36.5% |
| 置信残基 (pLDDT 70-90) 占比 | 39.0% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 18.8% |
| 有序区域 (pLDDT>70) 占比 | 75.5% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.6，有序区 75.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810; Pfam: PF12937 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.998 | 0.995 | — |
| NANOG | 0.859 | 0.000 | — |
| KLF4 | 0.844 | 0.000 | — |
| POU5F1 | 0.837 | 0.092 | — |
| SOX2 | 0.819 | 0.000 | — |
| LIN28A | 0.800 | 0.000 | — |
| CUL1 | 0.732 | 0.095 | — |
| MYC | 0.654 | 0.000 | — |
| PRDM14 | 0.643 | 0.000 | — |
| NR0B1 | 0.641 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hey | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| DARS2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HSPD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CPA6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HINT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| JPH3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| GAPDHS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.6 + PDB: 无 | pLDDT=76.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FBXO15 — F-box only protein 15，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小510 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NCQ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141665-FBXO15/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO15
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NCQ5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NCQ5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
