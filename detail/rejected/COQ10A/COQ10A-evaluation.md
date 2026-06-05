---
type: protein-evaluation
gene: "COQ10A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COQ10A — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COQ10A |
| 蛋白名称 | Coenzyme Q-binding protein COQ10 homolog A, mitochondrial |
| 蛋白大小 | 247 aa / 27.7 kDa |
| UniProt ID | Q96MF6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Endoplasmic reticulum, Cytosol; 额外: Golgi apparatus; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 247 aa / 27.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=76.2; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR044996, IPR005031, IPR023393; Pfam: PF03364 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Cytosol; 额外: Golgi apparatus | Approved |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 11 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Plasma Biomarkers of Mitochondrial Dysfunction in Patients with Myasthenia Gravis.. *Medical sciences (Basel, Switzerland)*. PMID: 40843740
2. Identification and Experimental Validation of Biomarkers Associated With Mitochondria and Macrophage Polarization in Sepsis.. *Emergency medicine international*. PMID: 40421007
3. Construction of a prognostic model for colon cancer by combining endoplasmic reticulum stress responsive genes.. *Journal of proteomics*. PMID: 39159861
4. Human COQ10A and COQ10B are distinct lipid-binding START domain proteins required for coenzyme Q function.. *Journal of lipid research*. PMID: 31048406
5. Statin-associated myopathy: from genetic predisposition to clinical management.. *Physiological research*. PMID: 25428737

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.2 |
| 高置信度残基 (pLDDT>90) 占比 | 42.5% |
| 置信残基 (pLDDT 70-90) 占比 | 24.3% |
| 中等置信 (pLDDT 50-70) 占比 | 13.4% |
| 低置信 (pLDDT<50) 占比 | 19.8% |
| 有序区域 (pLDDT>70) 占比 | 66.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.2，有序区 66.8%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044996, IPR005031, IPR023393; Pfam: PF03364 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COQ3 | 0.764 | 0.000 | — |
| COQ4 | 0.756 | 0.000 | — |
| COQ6 | 0.747 | 0.000 | — |
| COQ8A | 0.746 | 0.236 | — |
| COQ8B | 0.742 | 0.236 | — |
| COQ2 | 0.733 | 0.079 | — |
| COQ5 | 0.702 | 0.000 | — |
| COQ7 | 0.685 | 0.071 | — |
| COQ9 | 0.675 | 0.000 | — |
| PDSS1 | 0.636 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=76.2 + PDB: 无 | pLDDT=76.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / Endoplasmic reticulum, Cytosol; 额外: Golgi apparatu | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. COQ10A -- Coenzyme Q-binding protein COQ10 homolog A, mitochondrial，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小247 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96MF6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135469-COQ10A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COQ10A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96MF6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96MF6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
