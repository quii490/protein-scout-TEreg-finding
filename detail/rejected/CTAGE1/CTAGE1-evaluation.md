---
type: protein-evaluation
gene: "CTAGE1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CTAGE1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTAGE1 / CTAGE2 |
| 蛋白名称 | cTAGE family member 2 |
| 蛋白大小 | 745 aa / 85.3 kDa |
| UniProt ID | Q96RT6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 745 aa / 85.3 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=69.4; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR051500 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 9 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- endoplasmic reticulum exit site (GO:0070971)
- endoplasmic reticulum membrane (GO:0005789)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 270 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CTAGE2 |

**关键文献**:
1. Proteogenomic landscape of gastric adenocarcinoma peritoneal metastases.. *iScience*. PMID: 37305699
2. Immune and inflammation-related gene polymorphisms and susceptibility to tuberculosis in Southern Xinjiang population: A case-control analysis.. *International journal of immunogenetics*. PMID: 34958532
3. Ectopic expression of cancer-testis antigens in cutaneous T-cell lymphoma patients.. *Clinical cancer research : an official journal of the American Association for Cancer Research*. PMID: 24850846
4. Frequent genomic copy number gain and overexpression of GATA-6 in pancreatic carcinoma.. *Cancer biology & therapy*. PMID: 18769116
5. Genome-wide association analysis of diverticular disease points towards neuromuscular, connective tissue and epithelial pathomechanisms.. *Gut*. PMID: 30661054

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.4 |
| 高置信度残基 (pLDDT>90) 占比 | 45.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 38.9% |
| 有序区域 (pLDDT>70) 占比 | 56.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.4），有序残基占 56.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051500 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC68 | 0.955 | 0.000 | — |
| TCAF2C | 0.545 | 0.000 | — |
| SPANXA2 | 0.506 | 0.091 | — |
| MAGEA12 | 0.498 | 0.071 | — |
| GAGE1 | 0.482 | 0.045 | — |
| SPANXA1 | 0.475 | 0.091 | — |
| DDX43 | 0.467 | 0.095 | — |
| LUZP4 | 0.425 | 0.052 | — |
| PREB | 0.412 | 0.061 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 9，IntAct interactions: 0
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.4 + PDB: 无 | pLDDT=69.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 9 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CTAGE1 -- cTAGE family member 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小745 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96RT6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000212710-CTAGE1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTAGE1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96RT6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96RT6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
