---
type: protein-evaluation
gene: "DOCK8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DOCK8 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=221，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOCK8 |
| 蛋白名称 | Dedicator of cytokinesis protein 8 |
| 蛋白大小 | 2099 aa / 238.5 kDa |
| UniProt ID | Q8NF50 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DOCK8/IF_images/REH_1.jpg|REH]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DOCK8/IF_images/THP-1_1.jpg|THP-1]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane, Cytosol; UniProt: Cytoplasm; Cell membrane; Cell projection, lamellipodium mem |
| 📏 蛋白大小 | 2/10 | ×1 | 2 | 2099 aa / 238.5 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=221 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.6; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR037808, IPR027007, IPR035892, IPR026 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **55.0/180** | |
| **归一化总分** | | | **30.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasm; Cell membrane; Cell projection, lamellipodium membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cell leading edge (GO:0031252)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- lamellipodium membrane (GO:0031258)
- leading edge membrane (GO:0031256)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 221 |
| PubMed broad count | 509 |
| 别名(未计入scoring) |  |

**关键文献**:
1. De novo genic mutations among a Chinese autism spectrum disorder cohort.. *Nature communications*. PMID: 27824329
2. Pathogenesis of Autoimmunity/Systemic Lupus Erythematosus (SLE).. *Cells*. PMID: 40710333
3. Hyper IgE Syndromes.. *Current pediatric reviews*. PMID: 37702167
4. DOCK8 deficiency.. *Annals of the New York Academy of Sciences*. PMID: 22236427
5. DOCK8 gene mutation alters cell subsets, BCR signaling, and cell metabolism in B cells.. *Cell death & disease*. PMID: 39616183

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.6 |
| 高置信度残基 (pLDDT>90) 占比 | 26.1% |
| 置信残基 (pLDDT 70-90) 占比 | 46.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 19.5% |
| 有序区域 (pLDDT>70) 占比 | 72.7% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.6，有序区 72.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR037808, IPR027007, IPR035892, IPR026791; Pfam: PF06920, PF20422, PF20421 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.997 | 0.831 | — |
| WAS | 0.956 | 0.000 | — |
| LRCH1 | 0.935 | 0.840 | — |
| KANK1 | 0.935 | 0.000 | — |
| LRCH3 | 0.929 | 0.827 | — |
| RHOJ | 0.922 | 0.177 | — |
| WIPF1 | 0.904 | 0.000 | — |
| DOCK7 | 0.882 | 0.790 | — |
| DOCK6 | 0.881 | 0.802 | — |
| DMRT1 | 0.846 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=74.6 + PDB: 无 | pLDDT=74.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cell membrane; Cell projection, lamelli / Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DOCK8 — Dedicator of cytokinesis protein 8，有一定研究基础，但仍存在niche空间。
2. 蛋白大小2099 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 221 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NF50
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107099-DOCK8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOCK8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NF50
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:18:41

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NF50-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
