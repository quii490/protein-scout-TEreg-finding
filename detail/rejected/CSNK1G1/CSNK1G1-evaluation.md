---
type: protein-evaluation
gene: "CSNK1G1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CSNK1G1 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSNK1G1 |
| 蛋白名称 | non-specific serine/threonine protein kinase |
| 蛋白大小 | 475 aa / 54.5 kDa |
| UniProt ID | U3KQB3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 475 aa / 54.5 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=71.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 24 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Cell-type-focused compound screen in human organoids reveals CK1 inhibition protects cone photoreceptors from death.. *Neuron*. PMID: 41916277
2. Stage-Resolved Phosphoproteomic Landscape of Mouse Spermiogenesis Reveals Key Kinase Signaling in Sperm Morphogenesis.. *Adv Sci (Weinh)*. PMID: 40903803
3. Differential analysis of testicular LncRNA in Kazakh horses of different ages.. *Int J Biol Macromol*. PMID: 40706934
4. Integration of multi-omics resources reveals genetic features associated with environmental adaptation in the Wuzhishan pig genome.. *J Therm Biol*. PMID: 40921116
5. Genome-wide analysis of genetic loci and candidate genes related to teat number traits in Dongliao black pigs.. *Front Genet*. PMID: 40438329

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.8 |
| 高置信度残基 (pLDDT>90) 占比 | 57.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.7% |
| 低置信 (pLDDT<50) 占比 | 35.6% |
| 有序区域 (pLDDT>70) 占比 | 62.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=71.8，有序区 62.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSNK1G2 | 0.000 | 0.000 | — |
| CSNK1G3 | 0.000 | 0.000 | — |
| LRP6 | 0.000 | 0.000 | — |
| TMEM185A | 0.000 | 0.000 | — |
| AXIN1 | 0.000 | 0.000 | — |
| MTF1 | 0.000 | 0.000 | — |
| STK16 | 0.000 | 0.000 | — |
| CD59 | 0.000 | 0.000 | — |
| CTNNB1 | 0.000 | 0.000 | — |
| PPM1B | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9HCP0 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8BTH8 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9HCP0-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P78368 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q8TAP6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:P60409 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:P08754 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P13987 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P35613 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P55084 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 30
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.8 + PDB: 无 | pLDDT=71.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CSNK1G1 -- non-specific serine/threonine protein kinase，非常新颖，仅有少数基础研究。
2. 蛋白大小475 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/U3KQB3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169118-CSNK1G1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSNK1G1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/U3KQB3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
