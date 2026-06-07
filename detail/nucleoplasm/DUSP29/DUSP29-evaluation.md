---
type: protein-evaluation
gene: "DUSP29"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUSP29 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP29 |
| 蛋白名称 | Dual specificity phosphatase 29 |
| 蛋白大小 | 220 aa / 25.3 kDa |
| UniProt ID | Q68J44 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 220 aa / 25.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.8; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) |  |

**关键文献**:
1. DUSP29 does not regulate melanoma-myoblast interactions in a skeletal muscle co-culture model.. *Sci Rep*. PMID: 41741661
2. Identification of Expression Quantitative Trait Loci (eQTL) for Adipose-Specific Regulatory Mechanisms in Hanwoo (Korean Cattle).. *Animals (Basel)*. PMID: 41227413
3. DNA methylation in peripheral blood leukocytes in late onset Alzheimer's disease.. *J Alzheimers Dis Rep*. PMID: 40343304
4. Genetic Foundations of Nellore Traits: A Gene Prioritization and Functional Analyses of Genome-Wide Association Study Results.. *Genes (Basel)*. PMID: 39336722
5. Dual-specificity phosphatase 29 is induced during neurogenic skeletal muscle atrophy and attenuates glucocorticoid receptor activity in muscle cell culture.. *Am J Physiol Cell Physiol*. PMID: 32639872

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.8 |
| 高置信度残基 (pLDDT>90) 占比 | 72.3% |
| 置信残基 (pLDDT 70-90) 占比 | 9.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 12.3% |
| 有序区域 (pLDDT>70) 占比 | 81.8% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.8，有序区 81.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AMPD1 | 0.000 | 0.000 | — |
| RPL5 | 0.000 | 0.000 | — |
| DUSP23 | 0.000 | 0.000 | — |
| MS4A8 | 0.000 | 0.000 | — |
| SMIM12 | 0.000 | 0.000 | — |
| EPM2A | 0.000 | 0.000 | — |
| MTHFSD | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q68J44 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q8TBB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P62487 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q96D03 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96N21 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9HAS0 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9BVI4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9GZT8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9NRD5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 30
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.8 + PDB: 无 | pLDDT=86.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 7 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DUSP29 — Dual specificity phosphatase 29，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小220 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q68J44
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188716-DUSP29/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP29
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q68J44
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q68J44 |
| SMART | SM00195; |
| UniProt Domain [FT] | DOMAIN 54..202; /note="Tyrosine-protein phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160" |
| InterPro | IPR020405;IPR000340;IPR029021;IPR016130;IPR000387;IPR020422; |
| Pfam | PF00782; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188716-DUSP29/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARPC3 | Intact | false |
| ASPA | Intact | false |
| C17orf75 | Intact | false |
| CNTROB | Intact | false |
| DDIT4L | Intact | false |
| GOLGA6A | Intact | false |
| LNX1 | Intact | false |
| NIF3L1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
