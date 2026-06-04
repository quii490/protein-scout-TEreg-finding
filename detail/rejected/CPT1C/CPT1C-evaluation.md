---
type: protein-evaluation
gene: "CPT1C"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CPT1C — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=161，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPT1C |
| 蛋白名称 | Palmitoyl thioesterase CPT1C |
| 蛋白大小 | 803 aa / 91.0 kDa |
| UniProt ID | Q8TCG5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell projection, dendrite; Cell projection, axon; Endoplasmi |
| 蛋白大小 | 8/10 | x1 | 8 | 803 aa / 91.0 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=161 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=88.6; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **58.5/180** | |
| **归一化总分** | | | **32.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cell projection, dendrite; Cell projection, axon; Endoplasmic reticulum membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 161 |
| PubMed broad count | 161 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Alcohol consumption in metabolic dysfunction-associated steatotic liver disease (MASLD): understanding the gut-liver crosstalk for clinical translation.. *Gut Microbes*. PMID: 41723574
2. Combining machine learning and multi-omics analysis to explore the role of CPT1C in colorectal tumor cancer transformation.. *Sci Rep*. PMID: 42032056
3. Correction to "Loss-of-Function Variants in CPT1C: No Support for a Causal Role in Hereditary Spastic Paraplegia".. *Mov Disord*. PMID: 41969176
4. Fenofibrate targets PPARα-CPT1C axis to reverse aging by regulating lipid metabolism and mitochondrial function.. *Pharmacol Res*. PMID: 41765248
5. Loss-of-Function Variants in CPT1C: No Support for a Causal Role in Hereditary Spastic Paraplegia.. *Mov Disord*. PMID: 41312619

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.6 |
| 高置信度残基 (pLDDT>90) 占比 | 73.5% |
| 置信残基 (pLDDT 70-90) 占比 | 16.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 6.8% |
| 有序区域 (pLDDT>70) 占比 | 90.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.6，有序区 90.1%），结构可靠。

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
| uniprotkb:P49593 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| intact:EBI-54262002 | psi-mi:"MI:2195"(clash) | pubmed:- |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 2
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.6 + PDB: 无 | pLDDT=88.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, dendrite; Cell projection, axon;  / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 0 + 2 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CPT1C -- Palmitoyl thioesterase CPT1C，研究基础较多，新颖性有限。
2. 蛋白大小803 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 161 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TCG5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169169-CPT1C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPT1C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TCG5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
