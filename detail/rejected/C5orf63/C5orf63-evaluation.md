---
type: protein-evaluation
gene: "C5orf63"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## C5orf63 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C5orf63 |
| 蛋白名称 | Glutaredoxin-like protein C5orf63 |
| 蛋白大小 | 138 aa / 15.8 kDa |
| UniProt ID | A6NC05 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 138 aa / 15.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=45.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008554, IPR052565, IPR036249; Pfam: PF05768 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107/180** | |
| **归一化总分** | | | **59.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A genome-wide association study for shoulder impingement and rotator cuff disease.. *Journal of shoulder and elbow surgery*. PMID: 33482370
2. Microarray Expression Data Identify DCC as a Candidate Gene for Early Meningioma Progression.. *PloS one*. PMID: 27096627
3. Nonlinear dynamic genetic regulation identifies peripheral drivers of neurodegenerative disease progression.. *medRxiv : the preprint server for health sciences*. PMID: 41646748
4. Controlled human exposures to diesel exhaust: a human epigenome-wide experiment of target bronchial epithelial cells.. *Environmental epigenetics*. PMID: 33859829

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 45.2 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 0.0% |
| 中等置信 (pLDDT 50-70) 占比 | 31.9% |
| 低置信 (pLDDT<50) 占比 | 68.1% |
| 有序区域 (pLDDT>70) 占比 | 0.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=45.2），有序残基占 0.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008554, IPR052565, IPR036249; Pfam: PF05768 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MARCHF3 | 0.570 | 0.000 | — |
| MINAR2 | 0.542 | 0.000 | — |
| VOPP1 | 0.478 | 0.000 | — |
| C15orf40 | 0.470 | 0.000 | — |
| DENND5B | 0.454 | 0.000 | — |
| TEX43 | 0.452 | 0.000 | — |
| C8orf82 | 0.450 | 0.000 | — |
| OR5H14 | 0.448 | 0.000 | — |
| OXLD1 | 0.435 | 0.000 | — |
| PDIA6 | 0.409 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 10，IntAct interactions: 0
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=45.2 + PDB: 无 | pLDDT=45.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Mitochondria | 待确认 |
| PPI | STRING + IntAct | 10 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. C5orf63 — Glutaredoxin-like protein C5orf63，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小138 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=45.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NC05
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164241-C5orf63/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C5orf63
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NC05
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000164241-C5orf63/subcellular

![](https://images.proteinatlas.org/43240/562_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43240/562_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43240/568_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43240/568_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43240/575_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43240/575_C4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NC05-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
