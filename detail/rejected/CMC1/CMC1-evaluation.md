---
type: protein-evaluation
gene: "CMC1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CMC1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=241，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMC1 |
| 蛋白名称 | COX assembly mitochondrial protein homolog |
| 蛋白大小 | 106 aa / 12.5 kDa |
| UniProt ID | Q7Z7K0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion |
| 蛋白大小 | 8/10 | x1 | 8 | 106 aa / 12.5 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=241 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=87.0; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 21 partners; IntAct 26 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **62.0/180** | |
| **归一化总分** | | | **34.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Mitochondrion | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 241 |
| PubMed broad count | 246 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Valorization of Pineapple Crown for Carboxymethylcellulose Production: Optimization of Pulping Processes, Structural Characterization, and Potential as Seed Coating.. *Polymers (Basel)*. PMID: 42198160
2. Assessing active thumb palmar and radial abduction in persons with thumb carpometacarpal osteoarthritis via intermetacarpal distance methods: an exploration of validity, reliability, and precision.. *Clin Rheumatol*. PMID: 41739403
3. Effectiveness of exercise therapy in patients with thumb carpometacarpal osteoarthritis: A multicenter, randomized controlled trial.. *Osteoarthritis Cartilage*. PMID: 41138847
4. Additional Surgery after Trapeziectomy with Ligament Reconstruction and Tendon Interposition: An 8 Year Follow-Up of 1369 Patients.. *Plast Reconstr Surg*. PMID: 41989312
5. Characterization and structural analysis of a GH51 arabinofuranosidase Cabf51 catalyzing the transformation of ginsenoside Rc and compound MC1 into ginsenoside Rd and ginsenoside F2.. *Int J Biol Macromol*. PMID: 41791537

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.0 |
| 高置信度残基 (pLDDT>90) 占比 | 77.4% |
| 置信残基 (pLDDT 70-90) 占比 | 6.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 8.5% |
| 有序区域 (pLDDT>70) 占比 | 84.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.0，有序区 84.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COA3 | 0.000 | 0.000 | — |
| COX14 | 0.000 | 0.000 | — |
| COA5 | 0.000 | 0.000 | — |
| COX17 | 0.000 | 0.000 | — |
| COX16 | 0.000 | 0.000 | — |
| COA6 | 0.000 | 0.000 | — |
| TIMM10 | 0.000 | 0.000 | — |
| CMC2 | 0.000 | 0.000 | — |
| AZI2 | 0.000 | 0.000 | — |
| CHCHD7 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P36064 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P10591 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:P11484 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:Q9UTK4 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:O14122 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9HDV4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O74910 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:O74560 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q7Z7K0 | psi-mi:"MI:0276"(blue native page) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P00395 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 21，IntAct interactions: 26
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 21 个预测互作，IntAct 26 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.0 + PDB: 无 | pLDDT=87.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 21 + 26 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CMC1 -- COX assembly mitochondrial protein homolog，研究基础较多，新颖性有限。
2. 蛋白大小106 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 241 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z7K0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187118-CMC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z7K0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
