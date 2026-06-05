---
type: protein-evaluation
gene: "CRACR2B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRACR2B — REJECTED (核定位证据不足 (核定位得分 3/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRACR2B |
| 蛋白名称 | EF-hand calcium-binding domain-containing protein 4A |
| 蛋白大小 | 399 aa / 45.0 kDa |
| UniProt ID | Q8N4Y2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | x4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 399 aa / 45.0 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=76.9; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The transcriptome of the rat subfornical organ is altered in response to early postnatal overnutrition.. *IBRO Rep*. PMID: 30135952

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.9 |
| 高置信度残基 (pLDDT>90) 占比 | 37.6% |
| 置信残基 (pLDDT 70-90) 占比 | 32.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 19.3% |
| 有序区域 (pLDDT>70) 占比 | 70.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.9，有序区 70.4%），结构基本可用。

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
| uniprotkb:Q96LW7-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9BSF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8N4Y2-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9UBH0 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q99757 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9NRE2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8N8B7-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8TBB1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 30
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.9 + PDB: 无 | pLDDT=76.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 0 + 30 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CRACR2B -- EF-hand calcium-binding domain-containing protein 4A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小399 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N4Y2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177685-CRACR2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRACR2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N4Y2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N4Y2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
