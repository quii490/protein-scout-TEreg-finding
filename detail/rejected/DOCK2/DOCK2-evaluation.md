---
type: protein-evaluation
gene: "DOCK2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DOCK2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=220，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOCK2 / KIAA0209 |
| 蛋白名称 | Dedicator of cytokinesis protein 2 |
| 蛋白大小 | 1830 aa / 211.9 kDa |
| UniProt ID | Q92608 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endomembrane system; Cytoplasm, cytoskeleton |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1830 aa / 211.9 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=220 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.8; PDB: 2RQR, 2YIN, 3A98, 3B13, 6TGB, 6TGC |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR027007, IPR035892, IPR026799, IPR026 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.5/180** | |
| **归一化总分** | | | **38.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endomembrane system; Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 220 |
| PubMed broad count | 372 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0209 |

**关键文献**:
1. CB-Dock2: improved protein-ligand blind docking by integrating cavity detection, docking and homologous template fitting.. *Nucleic acids research*. PMID: 35609983
2. The pan-cancer proteome atlas, a mass spectrometry-based landscape for discovering tumor biology, biomarkers, and therapeutic targets.. *Cancer cell*. PMID: 40446800
3. Efficient evaluation of osteotoxicity and mechanisms of endocrine disrupting chemicals using network toxicology and molecular docking approaches: triclosan as a model compound.. *Ecotoxicology and environmental safety*. PMID: 40080935
4. DOCK2 is involved in the host genetics and biology of severe COVID-19.. *Nature*. PMID: 35940203
5. SULT2B1-CS-DOCK2 axis regulates effector T-cell exhaustion in HCC microenvironment.. *Hepatology (Baltimore, Md.)*. PMID: 36626623

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.8 |
| 高置信度残基 (pLDDT>90) 占比 | 42.2% |
| 置信残基 (pLDDT 70-90) 占比 | 40.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 12.7% |
| 有序区域 (pLDDT>70) 占比 | 83.1% |
| 可用 PDB 条目 | 2RQR, 2YIN, 3A98, 3B13, 6TGB, 6TGC |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2RQR, 2YIN, 3A98, 3B13, 6TGB, 6TGC）+ AlphaFold预测（pLDDT=79.8），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR027007, IPR035892, IPR026799, IPR026791; Pfam: PF06920, PF20422, PF20421 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELMO1 | 0.999 | 0.960 | — |
| RAC2 | 0.994 | 0.635 | — |
| RAC3 | 0.993 | 0.925 | — |
| RAC1 | 0.940 | 0.721 | — |
| FGR | 0.936 | 0.045 | — |
| HCK | 0.933 | 0.045 | — |
| SRC | 0.929 | 0.045 | — |
| LYN | 0.927 | 0.045 | — |
| CRK | 0.893 | 0.342 | — |
| PLD2 | 0.830 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=79.8 + PDB: 2RQR, 2YIN, 3A98, 3B13, 6TGB,  | pLDDT=79.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endomembrane system; Cytoplasm, cytoskeleton / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DOCK2 — Dedicator of cytokinesis protein 2，有一定研究基础，但仍存在niche空间。
2. 蛋白大小1830 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 220 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92608
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134516-DOCK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOCK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92608
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:18:24

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92608-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
