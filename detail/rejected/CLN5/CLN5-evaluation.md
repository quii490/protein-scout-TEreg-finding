---
type: protein-evaluation
gene: "CLN5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLN5 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=239，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLN5 |
| 蛋白名称 | Bis(monoacylglycero)phosphate synthase CLN5 |
| 蛋白大小 | 358 aa / 41.5 kDa |
| UniProt ID | O75503 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Lysosome; Membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 358 aa / 41.5 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=239 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=82.3; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.0/180** | |
| **归一化总分** | | | **33.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Lysosome; Membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 239 |
| PubMed broad count | 247 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CLN5 disease-causing mutations impact lysosomal biology by affecting intracellular degradation and protein trafficking.. *Biochim Biophys Acta Mol Basis Dis*. PMID: 42031177
2. PPARα and RXRα in the regulation of neuronal ceroid lipofuscinosis genes: implications for Batten disease therapy.. *NeuroImmune Pharm Ther*. PMID: 42146023
3. Extracellular vesicle-mediated release of bis(monoacylglycerol)phosphate is regulated by LRRK2 and glucocerebrosidase activity.. *Elife*. PMID: 41925724
4. Translational lipidomics reveals BMP and its precursor LPG as biomarkers for CLN5 Batten disease.. *bioRxiv*. PMID: 41890119
5. Brain-Directed AAV Gene Therapy Rescues a Mouse Model of the CLN5 Form of Neuronal Ceroid Lipofuscinosis Disease and Normalizes a Blood Plasma Biomarker of Neurodegeneration.. *Hum Gene Ther*. PMID: 41457644

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.3 |
| 高置信度残基 (pLDDT>90) 占比 | 64.2% |
| 置信残基 (pLDDT 70-90) 占比 | 12.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 14.8% |
| 有序区域 (pLDDT>70) 占比 | 76.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.3，有序区 76.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLN3 | 0.000 | 0.000 | — |
| CLN6 | 0.000 | 0.000 | — |
| CLN8 | 0.000 | 0.000 | — |
| PPT1 | 0.000 | 0.000 | — |
| MFSD8 | 0.000 | 0.000 | — |
| DNAJC5 | 0.000 | 0.000 | — |
| BTF3 | 0.000 | 0.000 | — |
| CTSD | 0.000 | 0.000 | — |
| KCTD7 | 0.000 | 0.000 | — |
| TPP1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O75503 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q5NF50 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| intact:EBI-23146846 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q13286 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q8TDT2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8IY26 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8IVJ1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q96JW4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:P01344-3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:P37268 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.3 + PDB: 无 | pLDDT=82.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Lysosome; Membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CLN5 -- Bis(monoacylglycero)phosphate synthase CLN5，研究基础较多，新颖性有限。
2. 蛋白大小358 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 239 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75503
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102805-CLN5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLN5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75503
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75503-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
