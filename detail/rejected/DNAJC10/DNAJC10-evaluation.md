---
type: protein-evaluation
gene: "DNAJC10"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJC10 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC10 |
| 蛋白名称 | Endoplasmic reticulum disulfide reductase DNAJC10 |
| 蛋白大小 | 793 aa / 91.1 kDa |
| UniProt ID | Q8IXB1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum lumen |
| 蛋白大小 | 10/10 | x1 | 10 | 793 aa / 91.1 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=33 篇 (<=40->8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=89.4; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Endoplasmic reticulum lumen | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 56 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The genetic associations of DNAJC family members with Parkinson's disease: comprehensive evidence from burden analysis and Mendelian randomization.. *Hum Genet*. PMID: 41951985
2. Whole genome analysis of selection associated with resistance to heat stress in chickens.. *Sci Rep*. PMID: 41946774
3. Expression of progerin enhances disease-related endpoints in a tau seeding reporter cell system.. *Geroscience*. PMID: 40660080
4. Unveiling FLNC variants: iPSC-derived myogenic cells as a model to study disease mechanisms.. *Skelet Muscle*. PMID: 41680819
5. Proteasome Inhibition Amplifies Endoplasmic Reticulum (ER) Stress Responses: Comparative Proteomics of Chinese Hamster Ovary Cell Lines.. *Biomolecules*. PMID: 41750347

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.4 |
| 高置信度残基 (pLDDT>90) 占比 | 64.9% |
| 置信残基 (pLDDT 70-90) 占比 | 29.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 1.3% |
| 有序区域 (pLDDT>70) 占比 | 94.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.4，有序区 94.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA5 | 0.000 | 0.000 | — |
| EDEM1 | 0.000 | 0.000 | — |
| HYOU1 | 0.000 | 0.000 | — |
| SEL1L | 0.000 | 0.000 | — |
| HSP90B1 | 0.000 | 0.000 | — |
| CALR | 0.000 | 0.000 | — |
| OS9 | 0.000 | 0.000 | — |
| CANX | 0.000 | 0.000 | — |
| HSPA4 | 0.000 | 0.000 | — |
| FOXRED2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q498R3 | psi-mi:"MI:0232"(transcriptional complementation a | pubmed:- |
| uniprotkb:Q8N4C5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8IXB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P06761 | psi-mi:"MI:0232"(transcriptional complementation a | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.4 + PDB: 无 | pLDDT=89.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum lumen / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: *** (REJECTED)

**核心优势**:
1. DNAJC10 -- Endoplasmic reticulum disulfide reductase DNAJC10，非常新颖，仅有少数基础研究。
2. 蛋白大小793 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXB1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000077232-DNAJC10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXB1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
