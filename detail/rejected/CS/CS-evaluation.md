---
type: protein-evaluation
gene: "CS"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CS — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=115113，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CS |
| 蛋白名称 | Citrate synthase, mitochondrial |
| 蛋白大小 | 466 aa / 51.7 kDa |
| UniProt ID | O75390 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion matrix |
| 蛋白大小 | 10/10 | x1 | 10 | 466 aa / 51.7 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=115113 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=94.0; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.5/180** | |
| **归一化总分** | | | **35.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Enhanced |
| UniProt | Mitochondrion matrix | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 115113 |
| PubMed broad count | 634186 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Prolonged intratumoral treatment with TLR7/8 agonist R848 regulates the tumor immune microenvironment resulting in enhanced antitumor activity.. *Cancer Biol Ther*. PMID: 42124329
2. Intestinal epithelial Syndecan-1 maintains mucosal homeostasis in inflammatory bowel disease by enhancing Faecalibacterium prausnitzii biofilm formation.. *Gut Microbes*. PMID: 42068031
3. Peripartum dynamics of ischemia and heart failure biomarkers: the impact of delivery mode.. *J Matern Fetal Neonatal Med*. PMID: 42178205
4. Subacromial bursitis: current evidence and future directions in injection-based therapies-A narrative review.. *Ann Med*. PMID: 42139015
5. Clinical features and longitudinal assessment in outcomes of chronic obstructive pulmonary disease with biomass smoke exposure history: A prospective study of the RealDTC cohort.. *Pulmonology*. PMID: 42112598

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.0 |
| 高置信度残基 (pLDDT>90) 占比 | 91.8% |
| 置信残基 (pLDDT 70-90) 占比 | 1.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 5.6% |
| 有序区域 (pLDDT>70) 占比 | 93.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.0，有序区 93.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACO1 | 0.000 | 0.000 | — |
| ACO2 | 0.000 | 0.000 | — |
| MDH2 | 0.000 | 0.000 | — |
| ACLY | 0.000 | 0.000 | — |
| DLAT | 0.000 | 0.000 | — |
| SDHB | 0.000 | 0.000 | — |
| IDH2 | 0.000 | 0.000 | — |
| IDH1 | 0.000 | 0.000 | — |
| FH | 0.000 | 0.000 | — |
| PC | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O75390 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:Q8VHF5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P18487 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9NYS7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9CZU6 | psi-mi:"MI:0028"(cosedimentation in solution) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q29RK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P17612-2 | psi-mi:"MI:0096"(pull down) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.0 + PDB: 无 | pLDDT=94.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion matrix / Mitochondria | 一致 |
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
1. CS -- Citrate synthase, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小466 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 115113 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75390
- Protein Atlas: https://www.proteinatlas.org/ENSG00000062485-CS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75390
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
