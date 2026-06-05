---
type: protein-evaluation
gene: "CRYAA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRYAA — REJECTED (研究热度过高 (PubMed strict=189，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRYAA |
| 蛋白名称 | Alpha-crystallin A chain |
| 蛋白大小 | 173 aa / 19.9 kDa |
| UniProt ID | P02489 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | x1 | 8 | 173 aa / 19.9 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=189 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=74.7; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 189 |
| PubMed broad count | 234 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Evaluating gene-disease relationship strength in crystallin genes in association with pediatric cataracts.. *Ophthalmic Genet*. PMID: 42091610
2. αA-Crystallin Attenuates Retinal Ischemia-Reperfusion Injury.. *Curr Eye Res*. PMID: 41529094
3. Melatonin Enhances Thermal Resilience and Extends Worker Lifespan in Apis cerana via Redox-Metabolic Reprogramming.. *Insects*. PMID: 42042421
4. Integrated analysis of gut microbiota and transcriptional responses reveals thermotolerance mechanisms in Arma chinensis.. *Ecotoxicol Environ Saf*. PMID: 41895145
5. Genetic analysis and clinical characteristics of sporadic and familial congenital cataracts in southern Chinese families.. *Front Genet*. PMID: 41822754

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.7 |
| 高置信度残基 (pLDDT>90) 占比 | 41.0% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 26.6% |
| 低置信 (pLDDT<50) 占比 | 15.0% |
| 有序区域 (pLDDT>70) 占比 | 58.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.7，有序区 58.3%），结构基本可用。

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
| uniprotkb:P02489 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9H8Y8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9NZD8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P02511 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q96HA8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 30
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.7 + PDB: 无 | pLDDT=74.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 30 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CRYAA -- Alpha-crystallin A chain，研究基础较多，新颖性有限。
2. 蛋白大小173 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 189 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 189 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P02489
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160202-CRYAA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRYAA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P02489
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P02489-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
