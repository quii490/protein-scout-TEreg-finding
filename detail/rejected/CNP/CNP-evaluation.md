---
type: protein-evaluation
gene: "CNP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CNP — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=4388，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNP |
| 蛋白名称 | 2',3'-cyclic-nucleotide 3'-phosphodiesterase |
| 蛋白大小 | 421 aa / 47.6 kDa |
| UniProt ID | P09543 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Plasma membrane; UniProt: Melanosome; Mitochondrion; Cell membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 421 aa / 47.6 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=4388 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=87.2; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.5/180** | |
| **归一化总分** | | | **35.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Approved |
| UniProt | Melanosome; Mitochondrion; Cell membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4388 |
| PubMed broad count | 6321 |
| 别名(未计入scoring) |  |

**关键文献**:
1. A novel activity of chitosan nanoparticles as an enhancer of biofilm formation in resistant Diarrheagenic Escherichia coli strains.. *Carbohydr Res*. PMID: 42191415
2. Single-stage C-N-P removal and ultra-low net sludge production driven by cyclic oxygen exposure and side-stream acidogenesis in an intermittent-aeration IFAS-OSA system.. *Bioresour Technol*. PMID: 42067159
3. Electroactive carriers promote simultaneous nitrification and denitrification (SND) coupled with enhanced biological phosphorus removal (EBPR) via synergistic microbial enrichment, metabolic intensification, and electron transfer facilitation.. *Bioresour Technol*. PMID: 42035959
4. A novel β-casein peptide‑zinc chelate with enhanced zinc transport capacity: Preparation, chelation mechanism, and in vitro stability.. *Food Chem*. PMID: 42085756
5. ATP-fueled STING activation of manganese coordinated nanoagonist to boost antitumor immunity.. *Bioact Mater*. PMID: 41716675

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 73.6% |
| 置信残基 (pLDDT 70-90) 占比 | 13.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 10.5% |
| 有序区域 (pLDDT>70) 占比 | 87.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.2，有序区 87.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MBP | 0.000 | 0.000 | — |
| GFAP | 0.000 | 0.000 | — |
| MAG | 0.000 | 0.000 | — |
| PLP1 | 0.000 | 0.000 | — |
| MOG | 0.000 | 0.000 | — |
| OLIG2 | 0.000 | 0.000 | — |
| DNAJC7 | 0.000 | 0.000 | — |
| GALC | 0.000 | 0.000 | — |
| TTC25 | 0.000 | 0.000 | — |
| OLIG1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P06623 | psi-mi:"MI:0096"(pull down) | pubmed:- |
| uniprotkb:P16330 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P09543 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P04156 | psi-mi:"MI:0089"(protein array) | pubmed:- |
| uniprotkb:P13233 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NTG7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 无 | pLDDT=87.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Melanosome; Mitochondrion; Cell membrane / Plasma membrane | 一致 |
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
1. CNP -- 2',3'-cyclic-nucleotide 3'-phosphodiesterase，研究基础较多，新颖性有限。
2. 蛋白大小421 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4388 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P09543
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173786-CNP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P09543
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P09543-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
