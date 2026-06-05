---
type: protein-evaluation
gene: "DOCK5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DOCK5 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOCK5 |
| 蛋白名称 | Dedicator of cytokinesis protein 5 |
| 蛋白大小 | 1870 aa / 215.3 kDa |
| UniProt ID | Q9H7D0 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DOCK5/IF_images/NIH-3T3_1.jpg|NIH 3T3]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DOCK5/IF_images/A-549_1.jpg|A-549]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm; Cell membrane; Cell projection, podosome |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1870 aa / 215.3 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.9; PDB: 7DPA, 8JHK, 8XM7, 8ZJ2, 8ZJI, 8ZJJ, 8ZJK |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR027007, IPR035892, IPR030717, IPR026 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Cytoplasm; Cell membrane; Cell projection, podosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- plasma membrane (GO:0005886)
- podosome (GO:0002102)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 87 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Dock5 Deficiency Promotes Proteinuric Kidney Diseases via Modulating Podocyte Lipid Metabolism.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38161229
2. Discrete placental gene expression signatures accompany diabetic disease classifications during pregnancy.. *American journal of obstetrics and gynecology*. PMID: 38763341
3. DOCK5 and DOCK1 regulate Caco-2 intestinal epithelial cell spreading and migration on collagen IV.. *The Journal of biological chemistry*. PMID: 19004829
4. DOCK5 regulates energy balance and hepatic insulin sensitivity by targeting mTORC1 signaling.. *EMBO reports*. PMID: 31885214
5. Conformational alteration of DOCK5•ELMO1 signalosome on lipid membrane.. *Communications biology*. PMID: 41233496

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.9 |
| 高置信度残基 (pLDDT>90) 占比 | 39.9% |
| 置信残基 (pLDDT 70-90) 占比 | 42.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 14.4% |
| 有序区域 (pLDDT>70) 占比 | 81.9% |
| 可用 PDB 条目 | 7DPA, 8JHK, 8XM7, 8ZJ2, 8ZJI, 8ZJJ, 8ZJK, 8ZJL, 8ZJM |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7DPA, 8JHK, 8XM7, 8ZJ2, 8ZJI, 8ZJJ, 8ZJK, 8ZJL, 8ZJM）+ AlphaFold预测（pLDDT=78.9），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR027007, IPR035892, IPR030717, IPR026791; Pfam: PF06920, PF20422, PF20421 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELMO1 | 0.990 | 0.980 | — |
| RAC3 | 0.937 | 0.925 | — |
| CRK | 0.885 | 0.613 | — |
| ELMO2 | 0.864 | 0.725 | — |
| CRKL | 0.835 | 0.540 | — |
| ELMO3 | 0.815 | 0.661 | — |
| RHOG | 0.814 | 0.357 | — |
| CDC42 | 0.748 | 0.284 | — |
| RAC1 | 0.739 | 0.354 | — |
| TNFRSF10D | 0.738 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=78.9 + PDB: 7DPA, 8JHK, 8XM7, 8ZJ2, 8ZJI,  | pLDDT=78.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cell membrane; Cell projection, podosom / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DOCK5 — Dedicator of cytokinesis protein 5，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1870 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H7D0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147459-DOCK5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOCK5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H7D0
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:18:29

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H7D0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
