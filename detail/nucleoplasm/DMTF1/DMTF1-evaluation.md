---
type: protein-evaluation
gene: "DMTF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DMTF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMTF1 |
| 蛋白名称 | Cyclin-D-binding Myb-like transcription factor 1 |
| 蛋白大小 | 760 aa / 84.5 kDa |
| UniProt ID | Q9Y222 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 760 aa / 84.5 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=45 篇 (<=60->6) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=52.4; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 18 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 70 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Oncogenic DMTF1β promotes cancer cell motility by regulating autophagy through ULK1 stabilization.. *Mol Oncol*. PMID: 42187319
2. Identification of DMP1 as Novel p53 Repressed Transcriptional Target.. *Int J Mol Sci*. PMID: 41683766
3. Intratumor microbiota Delftialacustiris correlated with METTL3 to control development of papillary thyroid carcinoma.. *Cancer Cell Int*. PMID: 41612397
4. DMTF1 up-regulation rescues proliferation defect of telomere dysfunctional neural stem cells via the SWI/SNF-E2F axis.. *Sci Adv*. PMID: 41481722
5. Identification of bicalutamide resistance-related genes and prognosis prediction in patients with prostate cancer.. *Front Endocrinol (Lausanne)*. PMID: 37143720

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.4 |
| 高置信度残基 (pLDDT>90) 占比 | 6.1% |
| 置信残基 (pLDDT 70-90) 占比 | 29.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 59.9% |
| 有序区域 (pLDDT>70) 占比 | 36.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=52.4），有序残基占 36.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCND2 | 0.000 | 0.000 | — |
| TP53 | 0.000 | 0.000 | — |
| ANPEP | 0.000 | 0.000 | — |
| CCNL2 | 0.000 | 0.000 | — |
| BTAF1 | 0.000 | 0.000 | — |
| TMEM243 | 0.000 | 0.000 | — |
| RUNDC3B | 0.000 | 0.000 | — |
| CDK4 | 0.000 | 0.000 | — |
| PNISR | 0.000 | 0.000 | — |
| CCND1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9Y222 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:A0A6L8PKS7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8CE22 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:- |
| uniprotkb:O00629 | psi-mi:"MI:0053"(fluorescence polarization spectro | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P01106 | psi-mi:"MI:0053"(fluorescence polarization spectro | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 18，IntAct interactions: 6
- 调控相关比例: 0 / 18 = 0%

**评价**: STRING 18 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.4 + PDB: 无 | pLDDT=52.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 18 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. DMTF1 -- Cyclin-D-binding Myb-like transcription factor 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小760 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=52.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y222
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135164-DMTF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMTF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y222
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
