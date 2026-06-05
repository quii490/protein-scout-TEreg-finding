---
type: protein-evaluation
gene: "COX17"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COX17 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3); 研究热度过高 (PubMed strict=138，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COX17 |
| 蛋白名称 | Cytochrome c oxidase copper chaperone |
| 蛋白大小 | 63 aa / 6.9 kDa |
| UniProt ID | Q14061 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Mitochondria; UniProt: Mitochondrion intermembrane space; Cytoplasm |
| 蛋白大小 | 5/10 | x1 | 5 | 63 aa / 6.9 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=138 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=72.2; PDB: 2L0Y, 2LGQ, 2RN9, 2RNB |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR009069, IPR007745; Pfam: PF05051 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65.5/180** | |
| **归一化总分** | | | **36.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Supported |
| UniProt | Mitochondrion intermembrane space; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrial intermembrane space (GO:0005758)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 138 |
| PubMed broad count | 216 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Copper metabolism in cell death and autophagy.. *Autophagy*. PMID: 37055935
2. Copper homeostasis and neurodegenerative diseases.. *Neural regeneration research*. PMID: 39589160
3. COX17 acetylation via MOF-KANSL complex promotes mitochondrial integrity and function.. *Nature metabolism*. PMID: 37813994
4. Characterization and localization of human COX17, a gene involved in mitochondrial copper transport.. *Human genetics*. PMID: 10982038
5. Roles of Copper Transport Systems Members in Breast Cancer.. *Cancer medicine*. PMID: 39676279

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 6.3% |
| 置信残基 (pLDDT 70-90) 占比 | 54.0% |
| 中等置信 (pLDDT 50-70) 占比 | 17.5% |
| 低置信 (pLDDT<50) 占比 | 22.2% |
| 有序区域 (pLDDT>70) 占比 | 60.3% |
| 可用 PDB 条目 | 2L0Y, 2LGQ, 2RN9, 2RNB |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量（pLDDT=72.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009069, IPR007745; Pfam: PF05051 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHCHD4 | 0.998 | 0.978 | — |
| SCO1 | 0.994 | 0.466 | — |
| COX19 | 0.984 | 0.000 | — |
| SCO2 | 0.980 | 0.460 | — |
| ATOX1 | 0.954 | 0.109 | — |
| COX11 | 0.939 | 0.000 | — |
| MT-CO2 | 0.894 | 0.000 | — |
| COA6 | 0.864 | 0.000 | — |
| CHCHD7 | 0.860 | 0.000 | — |
| GFER | 0.844 | 0.136 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 2L0Y, 2LGQ, 2RN9, 2RNB | pLDDT=72.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion intermembrane space; Cytoplasm / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. COX17 -- Cytochrome c oxidase copper chaperone，研究基础较多，新颖性有限。
2. 蛋白大小63 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 138 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14061
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138495-COX17/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COX17
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14061
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14061-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
