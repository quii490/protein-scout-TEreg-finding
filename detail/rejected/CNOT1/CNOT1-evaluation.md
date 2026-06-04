---
type: protein-evaluation
gene: "CNOT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CNOT1 — REJECTED (核定位证据不足 (核定位得分 3/10 <= 3); 研究热度过高 (PubMed strict=135，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNOT1 |
| 蛋白名称 | CCR4-NOT transcription complex subunit 1 |
| 蛋白大小 | 2376 aa / 266.9 kDa |
| UniProt ID | A5YKK6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | x4 | 12 | HPA: Cytosol; UniProt: Cytoplasm, P-body; Nucleus |
| 蛋白大小 | 2/10 | x1 | 2 | 2376 aa / 266.9 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=135 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=74.1; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **57.5/180** | |
| **归一化总分** | | | **31.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Uncertain |
| UniProt | Cytoplasm, P-body; Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 135 |
| PubMed broad count | 161 |
| 别名(未计入scoring) |  |

**关键文献**:
1. m(1)A-mediated regulation of BIRC2 mRNA stability drives apoptosis evasion and tumor progression in liver cancer.. *Cell Death Dis*. PMID: 41991508
2. CNOT1-Related Vissers-Bodmer Syndrome.. **. PMID: 41911374
3. Degron models: a toolbox for rapid in vivo depletion of essential proteins regulating mRNA metabolism.. *Commun Biol*. PMID: 41851445
4. Characterizing the interactions between murine cytomegalovirus M72 and the carbon catabolite repression 4-negative on TATA-less (CCR4-NOT) complex.. *Virology*. PMID: 41520498
5. Modeling patient variants of Cnot1 and Cdc42bpb results in distinct forms of congenital diaphragmatic hernia in mice.. *bioRxiv*. PMID: 42124667

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.1 |
| 高置信度残基 (pLDDT>90) 占比 | 18.6% |
| 置信残基 (pLDDT 70-90) 占比 | 57.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 16.5% |
| 有序区域 (pLDDT>70) 占比 | 76.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=74.1，有序区 76.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNOT10 | 0.000 | 0.000 | — |
| CNOT11 | 0.000 | 0.000 | — |
| CNOT3 | 0.000 | 0.000 | — |
| CNOT6 | 0.000 | 0.000 | — |
| CNOT2 | 0.000 | 0.000 | — |
| DDX6 | 0.000 | 0.000 | — |
| CNOT8 | 0.000 | 0.000 | — |
| CNOT9 | 0.000 | 0.000 | — |
| CNOT7 | 0.000 | 0.000 | — |
| CNOT4 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q6ZQ08 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:A5YKK6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q5NGF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P53829 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q8ZFX5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8CZZ7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:A0A7Y8RFP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:A0A5P8YBG5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9ULM6 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.1 + PDB: 无 | pLDDT=74.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, P-body; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CNOT1 -- CCR4-NOT transcription complex subunit 1，研究基础较多，新颖性有限。
2. 蛋白大小2376 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 135 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A5YKK6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125107-CNOT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNOT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A5YKK6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
