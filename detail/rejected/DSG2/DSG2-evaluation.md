---
type: protein-evaluation
gene: "DSG2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DSG2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=334，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DSG2 / CDHF5 |
| 蛋白名称 | Desmoglein-2 |
| 蛋白大小 | 1118 aa / 122.3 kDa |
| UniProt ID | Q14126 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DSG2/IF_images/U-251MG_1.jpg|U-251MG]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DSG2/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cell Junctions; 额外: Vesicles, Plasma membrane; UniProt: Cell membrane; Cell junction, desmosome; Cytoplasm |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1118 aa / 122.3 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=334 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.5; PDB: 2YQG, 5ERD, 5J5J, 6QNT, 6QNU, 6SIT, 7A7D |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050971, IPR002126, IPR015919, IPR020894, IPR027 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **59.0/180** | |
| **归一化总分** | | | **32.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cell Junctions; 额外: Vesicles, Plasma membrane | Supported |
| UniProt | Cell membrane; Cell junction, desmosome; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- apical plasma membrane (GO:0016324)
- cell junction (GO:0030054)
- cell surface (GO:0009986)
- cell-cell junction (GO:0005911)
- cornified envelope (GO:0001533)
- cytoplasm (GO:0005737)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 334 |
| PubMed broad count | 606 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CDHF5 |

**关键文献**:
1. Alzheimer's disease risk genes and mechanisms of disease pathogenesis.. *Biological psychiatry*. PMID: 24951455
2. Dilated Cardiomyopathy Overview.. **. PMID: 20301486
3. Interleukin-1β Drives Disease Progression in Arrhythmogenic Cardiomyopathy.. *bioRxiv : the preprint server for biology*. PMID: 39763850
4. Whole genome sequencing delineates regulatory, copy number, and cryptic splice variants in early onset cardiomyopathy.. *NPJ genomic medicine*. PMID: 35288587
5. Genotype-Specific Outcomes of Desmosomal Cardiomyopathies.. *Circulation*. PMID: 40406876

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.5 |
| 高置信度残基 (pLDDT>90) 占比 | 41.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 45.0% |
| 有序区域 (pLDDT>70) 占比 | 51.3% |
| 可用 PDB 条目 | 2YQG, 5ERD, 5J5J, 6QNT, 6QNU, 6SIT, 7A7D, 7AGF, 7AGG, 8QJX |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.5），有序残基占 51.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050971, IPR002126, IPR015919, IPR020894, IPR027397; Pfam: PF00028 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PKP2 | 0.999 | 0.360 | — |
| DSC2 | 0.999 | 0.897 | — |
| DSP | 0.998 | 0.045 | — |
| JUP | 0.997 | 0.760 | — |
| DSC3 | 0.961 | 0.000 | — |
| PKP3 | 0.926 | 0.360 | — |
| TMEM43 | 0.924 | 0.000 | — |
| PKP1 | 0.895 | 0.134 | — |
| GJA1 | 0.838 | 0.085 | — |
| DSG3 | 0.812 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=64.5 + PDB: 2YQG, 5ERD, 5J5J, 6QNT, 6QNU,  | pLDDT=64.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, desmosome; Cytoplasm / Cell Junctions; 额外: Vesicles, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DSG2 — Desmoglein-2，有一定研究基础，但仍存在niche空间。
2. 蛋白大小1118 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 334 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14126
- Protein Atlas: https://www.proteinatlas.org/ENSG00000046604-DSG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DSG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14126
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:20:06

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14126-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
