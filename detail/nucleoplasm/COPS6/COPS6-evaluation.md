---
type: protein-evaluation
gene: "COPS6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COPS6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COPS6 |
| 蛋白名称 | COP9 signalosome complex subunit 6 |
| 蛋白大小 | 327 aa / 36.2 kDa |
| UniProt ID | Q7L5N1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | x1 | 10 | 327 aa / 36.2 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=84.9; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, perinuclear region | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 59 |
| 别名(未计入scoring) |  |

**关键文献**:
1. A high-resolution plasma proteomic framework for stratifying treatment resistance and ultra-resistance in schizophrenia.. *Schizophr Res*. PMID: 42048856
2. ZNF460 Promotes the m6A Modification of COPS6 to Facilitate Immune Escape in Colorectal Cancer.. *FASEB J*. PMID: 41806184
3. Targeting the COP9 signalosome overcomes platinum resistance in ovarian cancer through two distinct genome stability mechanisms.. *bioRxiv*. PMID: 40799594
4. Identification of a novel matrix metalloproteinases-related prognostic signature in hepatocellular carcinoma.. *Aging (Albany NY)*. PMID: 38761174
5. Mechanisms and potential applications of COPS6 in pan-cancer therapy.. *World J Clin Oncol*. PMID: 38576589

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.9 |
| 高置信度残基 (pLDDT>90) 占比 | 62.7% |
| 置信残基 (pLDDT 70-90) 占比 | 21.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 8.3% |
| 有序区域 (pLDDT>70) 占比 | 84.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=84.9，有序区 84.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q7L5N1 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q96SN7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 30
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.9 + PDB: 无 | pLDDT=84.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, perinuclear region / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 30 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. COPS6 -- COP9 signalosome complex subunit 6，非常新颖，仅有少数基础研究。
2. 蛋白大小327 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L5N1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168090-COPS6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COPS6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L5N1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
