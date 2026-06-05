---
type: protein-evaluation
gene: "RBP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RBP1 — REJECTED (研究热度过高 (PubMed strict=225，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RBP1 / CRBP1 |
| 蛋白名称 | Retinol-binding protein 1 |
| 蛋白大小 | 135 aa / 15.8 kDa |
| UniProt ID | P09455 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Lipid droplet |
| 蛋白大小 | 8/10 | ×1 | 8 | 135 aa / 15.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=225 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.7; PDB: 5H8T, 5H9A, 5HA1, 5HBS, 5LJB, 5LJC, 5LJD |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012674, IPR031264, IPR000463, IPR031259, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm; Lipid droplet | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- lipid droplet (GO:0005811)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 225 |
| PubMed broad count | 362 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CRBP1 |

**关键文献**:
1. RNA Pol II inhibition activates cell death independently from the loss of transcription.. *Cell*. PMID: 40818455
2. Altered RBP1 Gene Expression Impacts Epithelial Cell Retinoic Acid, Proliferation, and Microenvironment.. *Cells*. PMID: 35269414
3. Coronary artery disease-associated immune gene RBP1 and its pan-cancer analysis.. *Frontiers in cardiovascular medicine*. PMID: 36970364
4. Retinoblastoma binding protein-1 (RBP1) is a Runx2 coactivator and promotes osteoblastic differentiation.. *BMC musculoskeletal disorders*. PMID: 20509905
5. Retinoic acid homeostasis and disease.. *Current topics in developmental biology*. PMID: 39870434

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.7 |
| 高置信度残基 (pLDDT>90) 占比 | 96.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.0% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.3% |
| 可用 PDB 条目 | 5H8T, 5H9A, 5HA1, 5HBS, 5LJB, 5LJC, 5LJD, 5LJE, 5LJG, 5LJH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5H8T, 5H9A, 5HA1, 5HBS, 5LJB, 5LJC, 5LJD, 5LJE, 5LJG, 5LJH）+ AlphaFold极高置信度预测（pLDDT=96.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012674, IPR031264, IPR000463, IPR031259, IPR000566; Pfam: PF00061 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STRA6 | 0.979 | 0.000 | — |
| LRAT | 0.951 | 0.000 | — |
| RDH11 | 0.910 | 0.045 | — |
| RBP4 | 0.910 | 0.000 | — |
| RLBP1 | 0.861 | 0.000 | — |
| RBP3 | 0.802 | 0.000 | — |
| TTR | 0.758 | 0.000 | — |
| ALDH1A1 | 0.750 | 0.000 | — |
| CYP26A1 | 0.719 | 0.000 | — |
| RARS1 | 0.719 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MRN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| NGR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SIS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| HSC82 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| GOLGA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:27107014|imex:IM-24995 |
| SF3B4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:27107014|imex:IM-24995 |
| Q26280 | psi-mi:"MI:0045"(experimental interaction detectio | pubmed:unassigned4 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.7 + PDB: 5H8T, 5H9A, 5HA1, 5HBS, 5LJB,  | pLDDT=96.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Lipid droplet / Cytosol; 额外: Nucleoplasm | 一致 |
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
1. RBP1 — Retinol-binding protein 1，研究基础较多，新颖性有限。
2. 蛋白大小135 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 225 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 225 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P09455
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114115-RBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P09455
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000114115-RBP1/subcellular

![](https://images.proteinatlas.org/7338/1193_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/7338/1193_D1_3_red_green.jpg)
![](https://images.proteinatlas.org/7338/1223_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/7338/1223_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/7338/1294_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/7338/1294_G12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P09455-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
