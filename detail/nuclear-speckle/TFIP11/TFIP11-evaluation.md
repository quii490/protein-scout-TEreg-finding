---
type: protein-evaluation
gene: "TFIP11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TFIP11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TFIP11 / STIP |
| 蛋白名称 | Tuftelin-interacting protein 11 |
| 蛋白大小 | 837 aa / 96.8 kDa |
| UniProt ID | Q9UBB9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 837 aa / 96.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=73.9; PDB: 8RO2 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000467, IPR022783, IPR022159, IPR024933, IPR045 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.0/180** | |
| **归一化总分** | | | **75.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- catalytic step 2 spliceosome (GO:0071013)
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- extracellular matrix (GO:0031012)
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- spliceosomal complex (GO:0005681)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: STIP |

**关键文献**:
1. Impact of tooth mineral tissues genes on dental caries: A birth-cohort study.. *Journal of dentistry*. PMID: 37031884
2. Structural organization and cellular localization of tuftelin-interacting protein 11 (TFIP11).. *Cellular and molecular life sciences : CMLS*. PMID: 15868102
3. TFIP11, CCNL1 and EWSR1 Protein-protein Interactions, and Their Nuclear Localization.. *International journal of molecular sciences*. PMID: 19122807
4. Dental caries: Genetic and protein interactions.. *Archives of oral biology*. PMID: 31476523
5. TFIP11 interacts with mDEAH9, an RNA helicase involved in spliceosome disassembly.. *International journal of molecular sciences*. PMID: 19165350

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.9 |
| 高置信度残基 (pLDDT>90) 占比 | 34.5% |
| 置信残基 (pLDDT 70-90) 占比 | 28.1% |
| 中等置信 (pLDDT 50-70) 占比 | 18.4% |
| 低置信 (pLDDT<50) 占比 | 19.0% |
| 有序区域 (pLDDT>70) 占比 | 62.6% |
| 可用 PDB 条目 | 8RO2 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=73.9，有序区 62.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000467, IPR022783, IPR022159, IPR024933, IPR045211; Pfam: PF01585, PF07842, PF12457 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DHX15 | 0.999 | 0.989 | — |
| EFTUD2 | 0.989 | 0.965 | — |
| CRNKL1 | 0.988 | 0.966 | — |
| TUFT1 | 0.984 | 0.292 | — |
| CDC40 | 0.981 | 0.846 | — |
| SNRPA1 | 0.979 | 0.946 | — |
| GCFC2 | 0.978 | 0.418 | — |
| BUD31 | 0.972 | 0.966 | — |
| XAB2 | 0.971 | 0.843 | — |
| PRPF8 | 0.969 | 0.953 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000480171.1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| TRAPPC4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Q81Y62 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CCP110 | psi-mi:"MI:0018"(two hybrid) | pubmed:16760425 |
| HSP90AA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19875381 |
| Prpf8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| thiL | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| sbcC2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.9 + PDB: 8RO2 | pLDDT=73.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TFIP11 — Tuftelin-interacting protein 11，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小837 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBB9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100109-TFIP11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TFIP11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBB9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000100109-TFIP11/subcellular

![](https://images.proteinatlas.org/27085/249_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/27085/249_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/27085/251_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/27085/251_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/27085/290_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/27085/290_B6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
