---
type: protein-evaluation
gene: "CLYBL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLYBL — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLYBL / CLB |
| 蛋白名称 | Citramalyl-CoA lyase, mitochondrial |
| 蛋白大小 | 340 aa / 37.4 kDa |
| UniProt ID | Q8N0X4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion |
| 蛋白大小 | 10/10 | x1 | 10 | 340 aa / 37.4 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=90.7; PDB: 5VXC, 5VXO, 5VXS |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR005000, IPR040186, IPR011206, IPR015813, IPR040 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Mitochondrion | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CLB |

**关键文献**:
1. Overcoming the Silencing of Doxycycline-Inducible Promoters in hiPSC-derived Cardiomyocytes.. *Open research Europe*. PMID: 39926351
2. Acetylation suppresses breast cancer progression by sustaining CLYBL stability.. *Journal of translational medicine*. PMID: 40211376
3. CLYBL averts vitamin B(12) depletion by repairing malyl-CoA.. *Nature chemical biology*. PMID: 40108300
4. The Human Knockout Gene CLYBL Connects Itaconate to Vitamin B(12).. *Cell*. PMID: 29056341
5. CLYBL is a polymorphic human enzyme with malate synthase and β-methylmalate synthase activity.. *Human molecular genetics*. PMID: 24334609

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.7 |
| 高置信度残基 (pLDDT>90) 占比 | 81.5% |
| 置信残基 (pLDDT 70-90) 占比 | 7.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 6.2% |
| 有序区域 (pLDDT>70) 占比 | 88.6% |
| 可用 PDB 条目 | 5VXC, 5VXO, 5VXS |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5VXC, 5VXO, 5VXS）+ AlphaFold高质量预测（pLDDT=90.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005000, IPR040186, IPR011206, IPR015813, IPR040442; Pfam: PF03328 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUGCT | 0.771 | 0.000 | — |
| ACO2 | 0.614 | 0.304 | — |
| FN1 | 0.602 | 0.000 | — |
| AUH | 0.599 | 0.140 | — |
| CS | 0.571 | 0.000 | — |
| GAPDH | 0.543 | 0.056 | — |
| PPP1R12C | 0.529 | 0.078 | — |
| ACO1 | 0.519 | 0.189 | — |
| CLPP | 0.506 | 0.337 | — |
| MRPL47 | 0.501 | 0.407 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| XXYLT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| - | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RNASE9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FAM181A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CD300E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FAM118B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| POLL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000339105 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.7 + PDB: 5VXC, 5VXO, 5VXS | pLDDT=90.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLYBL -- Citramalyl-CoA lyase, mitochondrial，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小340 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N0X4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125246-CLYBL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLYBL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N0X4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
