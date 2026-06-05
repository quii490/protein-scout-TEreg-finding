---
type: protein-evaluation
gene: "DNAJA2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJA2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJA2 |
| 蛋白名称 | DnaJ homolog subfamily A member 2 |
| 蛋白大小 | 412 aa / 45.7 kDa |
| UniProt ID | O60884 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoli, Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 412 aa / 45.7 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=53 篇 (<=60->6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=83.4; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 4/10 | x3 | 12 | STRING 25 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 63 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Expression of progerin enhances disease-related endpoints in a tau seeding reporter cell system.. *Geroscience*. PMID: 40660080
2. DNAJA2 inhibits Newcastle disease virus replication by targeting its V protein to modulate the MDA5-MAVS pathway.. *BMC Microbiol*. PMID: 41430554
3. Heat shock protein DNAJA2 controls insulin signaling and glucose homeostasis by preventing spontaneous insulin receptor endocytosis.. *Nat Commun*. PMID: 41233317
4. Genes Encoding Heat Shock Proteins Are Associated with Risk and Clinical Course of Severe COVID-19: A Pilot Study.. *Int J Mol Sci*. PMID: 41009536
5. Genetic variants in HSP40 co-chaperones modulate ischemic heart disease risk.. *Mol Biol Rep*. PMID: 40928562

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.4 |
| 高置信度残基 (pLDDT>90) 占比 | 51.0% |
| 置信残基 (pLDDT 70-90) 占比 | 31.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 10.9% |
| 有序区域 (pLDDT>70) 占比 | 82.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.4，有序区 82.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.000 | 0.000 | — |
| HSPA1B | 0.000 | 0.000 | — |
| HSPA1L | 0.000 | 0.000 | — |
| DNAJA1 | 0.000 | 0.000 | — |
| HSPA2 | 0.000 | 0.000 | — |
| DNAJB1 | 0.000 | 0.000 | — |
| HSPA4 | 0.000 | 0.000 | — |
| HSP90AA1 | 0.000 | 0.000 | — |
| DNAJA4 | 0.000 | 0.000 | — |
| STIP1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 25，IntAct interactions: 0
- 调控相关比例: 5 / 20 = 25%

**评价**: STRING 25 个预测互作，IntAct 0 个实验互作。调控相关配体占比 25%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.4 + PDB: 无 | pLDDT=83.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. DNAJA2 -- DnaJ homolog subfamily A member 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小412 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60884
- Protein Atlas: https://www.proteinatlas.org/ENSG00000069345-DNAJA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60884
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60884-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
