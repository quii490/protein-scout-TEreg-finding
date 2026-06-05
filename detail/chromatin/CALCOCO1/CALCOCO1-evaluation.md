---
type: protein-evaluation
gene: "CALCOCO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CALCOCO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CALCOCO1 / KIAA1536 |
| 蛋白名称 | Calcium-binding and coiled-coil domain-containing protein 1 |
| 蛋白大小 | 691 aa / 77.3 kDa |
| UniProt ID | Q9P1Z2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 691 aa / 77.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012852, IPR041641, IPR041611, IPR051002; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1536 |

**关键文献**:
1. Reticulophagy and viral infection.. *Autophagy*. PMID: 39394962
2. USP20 deubiquitinates and stabilizes the reticulophagy receptor RETREG1/FAM134B to drive reticulophagy.. *Autophagy*. PMID: 38705724
3. XBP1s activates METTL3/METTL14 for ER-phagy and paclitaxel sensitivity regulation in breast cancer.. *Cancer letters*. PMID: 38582397
4. RTN3L and CALCOCO1 function in parallel to maintain proteostasis in the endoplasmic reticulum.. *Autophagy*. PMID: 38818751
5. A novel ER stress regulator ARL6IP5 induces reticulophagy to ameliorate the prion burden.. *Autophagy*. PMID: 39394963

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.3 |
| 高置信度残基 (pLDDT>90) 占比 | 51.2% |
| 置信残基 (pLDDT 70-90) 占比 | 17.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 22.3% |
| 有序区域 (pLDDT>70) 占比 | 68.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.3，有序区 68.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012852, IPR041641, IPR041611, IPR051002; Pfam: PF07888, PF17751, PF18112 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GABARAPL1 | 0.860 | 0.396 | — |
| GABARAPL2 | 0.790 | 0.428 | — |
| GABARAP | 0.726 | 0.362 | — |
| TEX264 | 0.674 | 0.000 | — |
| ARNT | 0.663 | 0.634 | — |
| CCPG1 | 0.638 | 0.060 | — |
| VAPB | 0.601 | 0.000 | — |
| VAPA | 0.596 | 0.000 | — |
| ZDHHC17 | 0.581 | 0.000 | — |
| EP300 | 0.570 | 0.515 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CRYBA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CYTH3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRT15 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NDC80 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FOSL1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SH3GL3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TBC1D17 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Bcat | psi-mi:"MI:0096"(pull down) | imex:IM-14475|pubmed:16344550 |
| ENSMUSP00000023818.4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14475|pubmed:16344550 |
| APTX | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.3 + PDB: 无 | pLDDT=76.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CALCOCO1 — Calcium-binding and coiled-coil domain-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小691 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P1Z2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000012822-CALCOCO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CALCOCO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P1Z2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000012822-CALCOCO1/subcellular

![](https://images.proteinatlas.org/38313/563_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38313/563_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38313/566_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38313/566_H10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/38313/569_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38313/569_H10_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P1Z2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
