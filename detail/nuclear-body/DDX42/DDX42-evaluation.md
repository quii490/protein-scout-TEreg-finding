---
type: protein-evaluation
gene: "DDX42"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX42 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX42 |
| 蛋白名称 | ATP-dependent RNA helicase DDX42 |
| 蛋白大小 | 938 aa / 103.0 kDa |
| UniProt ID | Q86XP3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nuclear speckles; UniProt: Cytoplasm; Nucleus; Nucleus, Cajal body; Nucleus speckle |
| 蛋白大小 | 8/10 | x1 | 8 | 938 aa / 103.0 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=27 篇 (<=40->8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=66.1; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Enhanced |
| UniProt | Cytoplasm; Nucleus; Nucleus, Cajal body; Nucleus speckle | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 32 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Identification of Novel Susceptibility Genes for Early-Onset Colorectal Cancer Through Germline Rare Variant Burden Testing.. *Cancers (Basel)*. PMID: 41463182
2. Identification and experimental validation of common genes associated with both pulmonary arterial hypertension and major depressive disorder.. *Front Psychiatry*. PMID: 41280439
3. Biomarker identification through spatial proteomics for the characterization of indeterminate thyroid nodules.. *Endocrine*. PMID: 40790099
4. SUGP1 loss drives SF3B1 hotspot mutant missplicing in cancer.. *Cell Rep*. PMID: 40714635
5. Phosphoprotein Profile of Ameloblastoma.. *Asian Pac J Cancer Prev*. PMID: 40849725

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.1 |
| 高置信度残基 (pLDDT>90) 占比 | 32.7% |
| 置信残基 (pLDDT 70-90) 占比 | 17.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 42.1% |
| 有序区域 (pLDDT>70) 占比 | 50.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.1），有序残基占 50.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SF3B1 | 0.000 | 0.000 | — |
| SF3A2 | 0.000 | 0.000 | — |
| SF3B3 | 0.000 | 0.000 | — |
| SF3B5 | 0.000 | 0.000 | — |
| PHF5A | 0.000 | 0.000 | — |
| SF3B4 | 0.000 | 0.000 | — |
| SF3B2 | 0.000 | 0.000 | — |
| DHX15 | 0.000 | 0.000 | — |
| SF3B6 | 0.000 | 0.000 | — |
| SF3A1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q86XP3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P37867 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q81QG0 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q810A7 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:O95573 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q9H3N1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q9UBS4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q86XP3-2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.1 + PDB: 无 | pLDDT=66.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus, Cajal body; Nucleus s / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. DDX42 -- ATP-dependent RNA helicase DDX42，非常新颖，仅有少数基础研究。
2. 蛋白大小938 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=66.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86XP3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198231-DDX42/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX42
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86XP3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
