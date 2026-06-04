---
type: protein-evaluation
gene: "ECI2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ECI2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ECI2 |
| 蛋白名称 | Enoyl-CoA delta isomerase 2 |
| 蛋白大小 | 394 aa / 43.6 kDa |
| UniProt ID | O75521 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Peroxisomes, Mitochondria; UniProt: Mitochondrion; Peroxisome matrix |
| 蛋白大小 | 10/10 | ×1 | 10 | 394 aa / 43.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.4; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.5/180** | |
| **归一化总分** | | | **52.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Peroxisomes, Mitochondria | Enhanced |
| UniProt | Mitochondrion; Peroxisome matrix | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 62 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Genetic Architecture of Addiction-Relevant Behaviors in Outbred Sprague-Dawley Rats Reveals Loci for Anxiety-Like and Nociceptive Traits.. *Genes Brain Behav*. PMID: 42145201
2. Genetic Architecture of Addiction-Relevant Behaviors in Outbred Sprague-Dawley Rats Reveals Loci for Anxiety-Like and Nociceptive Traits.. *bioRxiv*. PMID: 41757122
3. Yucan granules alleviate renal injury in diabetic nephropathy by targeting ECH1, DHRS4, ECI2, and ECHS1.. *J Ethnopharmacol*. PMID: 41106567
4. CPT1A exacerbates trastuzumab-induced cardiotoxicity via promotion of mitochondrial dysfunction.. *Int J Biol Macromol*. PMID: 41386618
5. Transcriptomic and single-cell insights into mitochondrial genes NDUFA8, ECI2, and ACADM in acute myocardial infarction.. *Gene*. PMID: 40619072

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.4 |
| 高置信度残基 (pLDDT>90) 占比 | 72.8% |
| 置信残基 (pLDDT 70-90) 占比 | 12.4% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 12.9% |
| 有序区域 (pLDDT>70) 占比 | 85.2% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.4，有序区 85.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ECI1 | 0.000 | 0.000 | — |
| HADHB | 0.000 | 0.000 | — |
| ACAA2 | 0.000 | 0.000 | — |
| ACAA1 | 0.000 | 0.000 | — |
| ACAT2 | 0.000 | 0.000 | — |
| CARTPT | 0.000 | 0.000 | — |
| ACAT1 | 0.000 | 0.000 | — |
| EHHADH | 0.000 | 0.000 | — |
| ACOX1 | 0.000 | 0.000 | — |
| SCP2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O75521 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O23299 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q08558 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:- |
| uniprotkb:Q9WUR2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:A0A6B3UZY3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O00151 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O14497 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O15027-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75526 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O95714 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.4 + PDB: 无 | pLDDT=87.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion; Peroxisome matrix / Peroxisomes, Mitochondria | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ECI2 — Enoyl-CoA delta isomerase 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小394 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75521
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198721-ECI2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ECI2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75521
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
