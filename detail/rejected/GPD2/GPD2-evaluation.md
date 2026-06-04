---
type: protein-evaluation
gene: "GPD2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPD2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=143，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPD2 |
| 蛋白名称 | Glycerol-3-phosphate dehydrogenase, mitochondrial |
| 蛋白大小 | 727 aa / 80.9 kDa |
| UniProt ID | P43304 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 727 aa / 80.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=143 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR031656, IPR038299, IPR011992, IPR018247, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.5/180** | |
| **归一化总分** | | | **38.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 143 |
| PubMed broad count | 240 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. GPD2 inhibition impairs coagulation function via ROS/NF-κB/P2Y12 pathway.. *Cellular & molecular biology letters*. PMID: 40682019
2. The role of GPD2 and glycolysis-related genes in cholangiocarcinoma: insights into prognostic biomarkers and tumor-immune interactions.. *Cancer cell international*. PMID: 41068957
3. GPD2: The relationship with cancer and neural stemness.. *Cells & development*. PMID: 36592694
4. Mitochondrial Glycerol-3-Phosphate Dehydrogenase Restricts HBV Replication via the TRIM28-Mediated Degradation of HBx.. *Journal of virology*. PMID: 37166302
5. Artificial intelligence-based epigenomic, transcriptomic and histologic signatures of tobacco use in oral squamous cell carcinoma.. *NPJ precision oncology*. PMID: 38851780

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.3 |
| 高置信度残基 (pLDDT>90) 占比 | 60.7% |
| 置信残基 (pLDDT 70-90) 占比 | 26.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 7.7% |
| 有序区域 (pLDDT>70) 占比 | 87.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.3，有序区 87.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031656, IPR038299, IPR011992, IPR018247, IPR002048; Pfam: PF01266, PF16901, PF13499 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPD1 | 0.997 | 0.093 | — |
| TKFC | 0.979 | 0.000 | — |
| GPAM | 0.955 | 0.000 | — |
| GNPAT | 0.932 | 0.000 | — |
| GPAT2 | 0.932 | 0.000 | — |
| SDHB | 0.930 | 0.210 | — |
| GPAT3 | 0.928 | 0.000 | — |
| GPAT4 | 0.915 | 0.000 | — |
| SDHA | 0.912 | 0.000 | — |
| GPD1L | 0.912 | 0.093 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP82 | psi-mi:"MI:0397"(two hybrid array) | pubmed:15766533 |
| GEM1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RKM2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| TDH2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| UFD4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| IMD4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CMK1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PPH22 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| VMA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SGF29 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-15346|pubmed:21734642 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.3 + PDB: 无 | pLDDT=86.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GPD2 — Glycerol-3-phosphate dehydrogenase, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小727 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 143 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P43304
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115159-GPD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P43304
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
