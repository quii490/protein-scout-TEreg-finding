---
type: protein-evaluation
gene: "DSC1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DSC1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=125，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DSC1 / CDHF1 |
| 蛋白名称 | Desmocollin-1 |
| 蛋白大小 | 894 aa / 100.0 kDa |
| UniProt ID | Q08554 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell junction, desmosome |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 894 aa / 100.0 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=125 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.7; PDB: 5IRY |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050971, IPR002126, IPR015919, IPR020894, IPR014 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.5/180** | |
| **归一化总分** | | | **35.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cell junction, desmosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cornified envelope (GO:0001533)
- desmosome (GO:0030057)
- extracellular exosome (GO:0070062)
- ficolin-1-rich granule membrane (GO:0101003)
- gap junction (GO:0005921)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 125 |
| PubMed broad count | 270 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CDHF1 |

**关键文献**:
1. IgA pemphigus.. *Clinics in dermatology*. PMID: 21679872
2. The Drosophila Sodium Channel 1 (DSC1): The founding member of a new family of voltage-gated cation channels.. *Pesticide biochemistry and physiology*. PMID: 25987218
3. HDLs and the pathogenesis of atherosclerosis.. *Current opinion in cardiology*. PMID: 29561322
4. CircRAB11FIP1 promoted autophagy flux of ovarian cancer through DSC1 and miR-129.. *Cell death & disease*. PMID: 33637694
5. Lower DSC1 expression is related to the poor differentiation and prognosis of head and neck squamous cell carcinoma (HNSCC).. *Journal of cancer research and clinical oncology*. PMID: 27601166

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.7 |
| 高置信度残基 (pLDDT>90) 占比 | 48.4% |
| 置信残基 (pLDDT 70-90) 占比 | 22.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 23.6% |
| 有序区域 (pLDDT>70) 占比 | 71.3% |
| 可用 PDB 条目 | 5IRY |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=76.7，有序区 71.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050971, IPR002126, IPR015919, IPR020894, IPR014868; Pfam: PF00028, PF08758 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DSG1 | 0.998 | 0.625 | — |
| CDSN | 0.997 | 0.280 | — |
| DSP | 0.959 | 0.508 | — |
| JUP | 0.913 | 0.525 | — |
| PKP1 | 0.905 | 0.543 | — |
| LOR | 0.832 | 0.000 | — |
| PPL | 0.819 | 0.045 | — |
| FLG | 0.814 | 0.046 | — |
| DSG3 | 0.806 | 0.000 | — |
| PKP3 | 0.804 | 0.304 | — |

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
| 三维结构 | AlphaFold pLDDT=76.7 + PDB: 5IRY | pLDDT=76.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, desmosome / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DSC1 — Desmocollin-1，有一定研究基础，但仍存在niche空间。
2. 蛋白大小894 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 125 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q08554
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134765-DSC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DSC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q08554
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:19:59

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q08554-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
