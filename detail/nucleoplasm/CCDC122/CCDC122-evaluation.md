---
type: protein-evaluation
gene: "CCDC122"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC122 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC122 / CCDC122 |
| 蛋白全名 | Coiled-coil domain-containing protein 122 |
| 蛋白大小 | 273 aa / 32.2 kDa |
| UniProt ID | Q5T0U0 |
| 子定位分类 | nucleoplasm |
| HPA IF 主定位 | Vesicles |
| HPA IF 附加定位 | Nucleoplasm |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16 | HPA核为附加定位，主定位非核 |
| 蛋白大小 | 10/10 | x1 | 10 | 273 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=7 (Extremely novel) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold高质量(pLDDT=88.9, >70%=87.5%) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 4/10 | x3 | 12 | STRING综合分>0.7 (5条)，主要为预测 |
| 互证加分 | — | max+3 | +0.5 | IntAct实验互作丰富(12条) (+0.5) |
| **加权总分** | | | **126.5/180** | |
| **归一化总分 (÷1.83)** | | | **69.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | 无UniProt注释 | Swiss-Prot/TrEMBL |
| GO-CC | 无 | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA核为附加定位，主定位非核

#### 3.2 蛋白大小评估

273 aa (200-800 aa ideal range)

**评价**: 273 aa / 32.2 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 7 |
| PubMed symbol_only | 12 |
| PubMed broad | 12 |
| 别名 | CCDC122 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 7 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Association between genetic variants in NOD2, C13orf31, and CCDC122 genes and leprosy among the Chinese Yi population.** *International journal of dermatology* (2016 Jan) PMID:26235265 -- Xiong JH et al.
2. **Integrating genetic regulation and schizophrenia-specific splicing quantitative expression with GWAS prioritizes novel risk genes for schizophrenia.** *Translational psychiatry* (2025 Oct 6) PMID:41053005 -- Li X et al.
3. **5hmC-profiles in Puerto Rican Hispanic/Latino men with aggressive prostate cancer.** *medRxiv : the preprint server for health sciences* (2024 Oct 27) PMID:39502659 -- Patel MS et al.
4. **5hmC-profiles in Puerto Rican Hispanic/Latino men with aggressive prostate cancer.** *Frontiers in oncology* (2025) PMID:40265030 -- Patel MS et al.
5. **CCDC122-LACC1 gene polymorphism is associated with protection against leprosy in a population from Northeastern Brazil: a case-control study.** *BMC infectious diseases* (2025 Dec 22) PMID:41430577 -- Freitas HA et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 88.9 |
| pLDDT > 90 (Very High) | 73.6% |
| pLDDT 70-90 (High) | 13.9% |
| pLDDT 50-70 (Medium) | 5.9% |
| pLDDT < 50 (Low) | 6.6% |
| 有序区域 (pLDDT>70) 占比 | 87.5% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 高质量预测（pLDDT=88.9，有序区域 88%）。

**评分: 8/10**。

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
| LACC1 | 0.949 | 0.000 | — |
| TNFSF15 | 0.779 | 0.000 | — |
| RIPK2 | 0.749 | 0.000 | — |
| LRRK2 | 0.720 | 0.000 | — |
| NOD2 | 0.704 | 0.000 | — |
| SPRYD7 | 0.641 | 0.000 | — |
| CFAP69 | 0.630 | 0.000 | — |
| PACRG | 0.584 | 0.000 | — |
| SLC11A1 | 0.547 | 0.000 | — |
| VIL1 | 0.543 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| recN | 0398(two hybrid pooling approach) | imex:IM-13779|pubmed | — |
| E9R5P7 | 0398(two hybrid pooling approach) | imex:IM-13779|pubmed | — |
| A0A0F7RLC1 | 0398(two hybrid pooling approach) | imex:IM-13779|pubmed | — |
| FAM167A | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| EXOC1 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| CCDC172 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| BORCS6 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| SYCE1 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |
| S100A2 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |


**已知复合体成员** (GO Cellular Component):
- 无GO-CC注释

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 9
- 调控相关比例: 0/15 (0%)

**评价**: STRING综合分>0.7 (5条)，主要为预测

**评分: 4/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 9 | 数据充分 |

**互证加分明细**:
- IntAct实验互作丰富(12条) (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (69.1/100)

**核心优势**:
1. Extremely novel -- PubMed=7篇
2. HPA核为附加定位，主定位非核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T0U0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC122
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T0U0
- STRING: https://string-db.org/cgi/network?identifiers=CCDC122&species=9606
