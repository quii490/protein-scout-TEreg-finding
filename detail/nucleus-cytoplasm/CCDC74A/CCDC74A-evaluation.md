---
type: protein-evaluation
gene: "CCDC74A"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC74A 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC74A / CCDC74A |
| 蛋白全名 | Coiled-coil domain-containing protein 74A |
| 蛋白大小 | 378 aa / 41.6 kDa |
| UniProt ID | Q96AQ1 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Centrosome, Basal body |
| HPA IF 附加定位 | Nucleoplasm, Cytosol |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16 | HPA核为附加定位，主定位非核 |
| 蛋白大小 | 10/10 | x1 | 10 | 378 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=1 (Extremely novel) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold低置信(pLDDT=59.3)，新颖蛋白基线 |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (15条) |
| 互证加分 | — | max+3 | +1.0 | IntAct实验互作丰富(15条) (+0.5); InterPro注释丰富(3个结构域) (+0.5) |
| **加权总分** | | | **127.0/180** | |
| **归一化总分 (÷1.83)** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Centrosome, Basal body, Cytosol | Approved |
| UniProt | 无UniProt注释 | Swiss-Prot/TrEMBL |
| GO-CC | 无 | |

暂无PAE图

HPA IF 图像可用 (12张)，待下载。

**结论**: HPA核为附加定位，主定位非核

#### 3.2 蛋白大小评估

378 aa (200-800 aa ideal range)

**评价**: 378 aa / 41.6 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 1 |
| PubMed symbol_only | 3 |
| PubMed broad | 3 |
| 别名 | CCDC74A |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 1 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **A 12-gene panel in estimating hormone-treatment responses of castration-resistant prostate cancer patients generated using a combined analysis of bulk and single-cell sequencing data.** *Annals of medicine* (2023) PMID:37729607 -- Huang J et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 59.3 |
| pLDDT > 90 (Very High) | 20.6% |
| pLDDT 70-90 (High) | 8.5% |
| pLDDT 50-70 (Medium) | 19.8% |
| pLDDT < 50 (Low) | 51.1% |
| 有序区域 (pLDDT>70) 占比 | 29.1% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 预测置信度偏低（pLDDT=59.3，有序区域 29%）。作为新颖蛋白，属正常现象。

**评分: 6/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 存在注释结构域（0个），但未发现明确染色质/DNA结合域。新颖蛋白基线不扣分。

**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| CCDC74B | 0.913 | 0.610 | — |
| PSMD4 | 0.609 | 0.609 | — |
| PSMD13 | 0.609 | 0.609 | — |
| ADRM1 | 0.608 | 0.608 | — |
| PSMD10 | 0.607 | 0.607 | — |
| PSMC1 | 0.601 | 0.601 | — |
| PSMD14 | 0.596 | 0.596 | — |
| UCHL5 | 0.591 | 0.591 | — |
| PSMD6 | 0.591 | 0.591 | — |
| PSMC4 | 0.591 | 0.591 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| MTUS2 | 0397(two hybrid array) | imex:IM-27438|doi:10 | — |
| ZNF655 | 1356(validated two hybrid) | pubmed:32296183|imex | — |
| CEP19 | 1356(validated two hybrid) | pubmed:32296183|imex | — |
| SH2D1A | 0397(two hybrid array) | pubmed:25814554|imex | — |
| PSMD11 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| RGPD8 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| PSMD3 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| PSMD10 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| PSMC3 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| PSMC2 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |


**已知复合体成员** (GO Cellular Component):
- 无GO-CC注释

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 15
- 调控相关比例: 0/15 (0%)

**评价**: STRING实验分>0.5 (15条)

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 15 | 数据充分 |

**互证加分明细**:
- IntAct实验互作丰富(15条) (+0.5)
- InterPro注释丰富(3个结构域) (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (69.4/100)

**核心优势**:
1. Extremely novel -- PubMed=1篇
2. HPA核为附加定位，主定位非核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. AlphaFold预测质量待提升

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AQ1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC74A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AQ1
- STRING: https://string-db.org/cgi/network?identifiers=CCDC74A&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96AQ1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029422;IPR040370;IPR039496; |
| Pfam | PF14917;PF14916; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163040-CCDC74A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CEP19 | Intact | false |
| ZNF655 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
