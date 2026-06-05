---
type: protein-evaluation
gene: "GNG2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNG2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNG2 |
| 蛋白名称 | Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-2 |
| 蛋白大小 | 71 aa / 7.8 kDa |
| UniProt ID | P59768 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; 额外: Vesicles; UniProt: Cell membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 71 aa / 7.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=66 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.6; PDB: 4KFM, 5HE0, 5HE1, 5HE2, 5HE3, 5UKK, 5UKL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001770, IPR015898, IPR036284; Pfam: PF00631 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Vesicles | Approved |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- heterotrimeric G-protein complex (GO:0005834)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)
- synapse (GO:0045202)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 66 |
| PubMed broad count | 93 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. GNG2 acts as a tumor suppressor in breast cancer through stimulating MRAS signaling.. *Cell death & disease*. PMID: 35322009
2. Alteration of gene expression profiling including GPR174 and GNG2 is associated with vasovagal syncope.. *Pediatric cardiology*. PMID: 25367286
3. Topography of Gng2- and NetrinG2-expression suggests an insular origin of the human claustrum.. *PloS one*. PMID: 22957104
4. Reduced GNG2 expression levels in mouse malignant melanomas and human melanoma cell lines.. *American journal of cancer research*. PMID: 22679562
5. miRNAs regulating the expressions of NTF3, GNG2 and ITGA7 are involved in the pathogenesis of abdominal aortic aneurysm in mice.. *General physiology and biophysics*. PMID: 33655887

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.6 |
| 高置信度残基 (pLDDT>90) 占比 | 71.8% |
| 置信残基 (pLDDT 70-90) 占比 | 14.1% |
| 中等置信 (pLDDT 50-70) 占比 | 14.1% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 85.9% |
| 可用 PDB 条目 | 4KFM, 5HE0, 5HE1, 5HE2, 5HE3, 5UKK, 5UKL, 5UKM, 5UZ7, 6B3J |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4KFM, 5HE0, 5HE1, 5HE2, 5HE3, 5UKK, 5UKL, 5UKM, 5UZ7, 6B3J）+ AlphaFold极高置信度预测（pLDDT=89.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001770, IPR015898, IPR036284; Pfam: PF00631 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNB1 | 0.999 | 0.999 | — |
| GNB3 | 0.999 | 0.996 | — |
| GNB5 | 0.999 | 0.996 | — |
| GNB4 | 0.999 | 0.997 | — |
| GNB2 | 0.999 | 0.997 | — |
| GNAI1 | 0.998 | 0.987 | — |
| GNAS | 0.997 | 0.937 | — |
| HTR7 | 0.983 | 0.831 | — |
| CCR5 | 0.982 | 0.816 | — |
| PREX1 | 0.981 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Fnta | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15451670 |
| GRK2 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:12764189 |
| Kcnk2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23021213|imex:IM-18125 |
| NUFIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HAX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DGUOK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RRP7A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAAF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDCA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARMC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.6 + PDB: 4KFM, 5HE0, 5HE1, 5HE2, 5HE3,  | pLDDT=89.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / Plasma membrane; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GNG2 — Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小71 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 66 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P59768
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186469-GNG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P59768
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P59768-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
